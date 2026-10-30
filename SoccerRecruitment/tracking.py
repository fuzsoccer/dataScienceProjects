"""Streaming Metrica CSV parsing and strictly backward-looking features."""
import csv
import gzip
import math
from collections import defaultdict


def number(value):
    try:
        result = float(value)
        return result if math.isfinite(result) else None
    except (ValueError, TypeError):
        return None


def frames(path):
    opener = gzip.open if str(path).endswith(".gz") else open
    with opener(path, "rt", newline="", encoding="utf-8-sig") as stream:
        reader = csv.reader(stream)
        next(reader)  # team labels
        shirts = next(reader)
        header = next(reader)
        if header[:3] != ["Period", "Frame", "Time [s]"]:
            raise ValueError(f"Unexpected Metrica header: {header[:3]}")
        players = [(i, shirts[i]) for i in range(3, len(header) - 2, 2)]
        if any(not shirt for _, shirt in players) or len({s for _, s in players}) != len(players):
            raise ValueError("Missing or duplicate player identifiers")
        for row in reader:
            if len(row) != len(header):
                raise ValueError("Malformed tracking row")
            positions = {shirt: (number(row[i]), number(row[i + 1])) for i, shirt in players}
            yield int(row[0]), int(row[1]), float(row[2]), positions, (number(row[-2]), number(row[-1]))


def engineer(path, match, team, output, output_stride=1):
    previous = {}
    totals = defaultdict(lambda: defaultdict(float))
    quality = dict(frames=0, duplicate_or_unordered_frames=0, invalid_time_steps=0,
                   missing_player_positions=0, partial_player_positions=0,
                   outside_pitch_positions=0, rejected_speed_intervals=0,
                   missing_ball_positions=0, min_dt_s=None, max_dt_s=None)
    last_key = None
    opener = gzip.open if str(output).endswith(".gz") else open
    with opener(output, "wt", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=["match_id", "team", "player_id", "period", "frame", "time_s", "x_m", "y_m", "dt_s", "speed_mps", "distance_step_m", "ball_distance_m"])
        writer.writeheader()
        for period, frame, t, positions, ball in frames(path):
            quality["frames"] += 1
            key = (period, frame)
            if last_key is not None and key <= last_key:
                quality["duplicate_or_unordered_frames"] += 1
            last_key = key
            if None in ball:
                quality["missing_ball_positions"] += 1
            for player, (x, y) in positions.items():
                total = totals[player]
                total["frames"] += 1
                if x is None or y is None:
                    quality["missing_player_positions"] += 1
                    quality["partial_player_positions"] += int((x is None) != (y is None))
                    previous.pop(player, None)
                    continue
                quality["outside_pitch_positions"] += int(not (0 <= x <= 1 and 0 <= y <= 1))
                x, y = x * 105, y * 68
                total["observed_frames"] += 1
                dt = speed = distance = None
                if player in previous:
                    p, old_frame, old_t, old_x, old_y = previous[player]
                    candidate_dt = t - old_t
                    if p == period:
                        quality["min_dt_s"] = candidate_dt if quality["min_dt_s"] is None else min(quality["min_dt_s"], candidate_dt)
                        quality["max_dt_s"] = candidate_dt if quality["max_dt_s"] is None else max(quality["max_dt_s"], candidate_dt)
                        if 0 < candidate_dt <= 0.2 and frame == old_frame + 1:
                            dt = candidate_dt
                            step = math.hypot(x-old_x, y-old_y)
                            candidate_speed = step / dt
                            if candidate_speed <= 12:
                                speed, distance = candidate_speed, step
                                total["valid_interval_s"] += dt
                                total["distance_m"] += step
                                total["high_speed_s"] += dt * (speed >= 7)
                                total["speed_max_mps"] = max(total["speed_max_mps"], speed)
                            else:
                                quality["rejected_speed_intervals"] += 1
                        else:
                            quality["invalid_time_steps"] += 1
                previous[player] = (period, frame, t, x, y)
                ball_distance = None if None in ball else math.hypot(x-ball[0]*105, y-ball[1]*68)
                if frame % output_stride == 0:
                    writer.writerow(dict(match_id=match, team=team, player_id=player, period=period, frame=frame, time_s=t, x_m=x, y_m=y, dt_s=dt, speed_mps=speed, distance_step_m=distance, ball_distance_m=ball_distance))
    summaries = []
    for player, total in sorted(totals.items()):
        summaries.append(dict(match_id=match, team=team, player_id=player, **total,
                              position_coverage=total["observed_frames"]/total["frames"],
                              mean_speed_mps=total["distance_m"]/total["valid_interval_s"] if total["valid_interval_s"] else None))
    return quality, summaries
