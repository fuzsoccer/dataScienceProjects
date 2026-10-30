"""Run from repository root: python scripts/run.py all."""
import argparse
import csv
import json
from collections import Counter
from pathlib import Path

from .acquire import fetch
from .tracking import engineer


def write_csv(path, rows):
    if rows:
        fields = list(dict.fromkeys(key for row in rows for key in row))
        with path.open("w", newline="", encoding="utf-8") as stream:
            writer = csv.DictWriter(stream, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows)


def inspect(root):
    report = {"statsbomb": {}, "metrica_events": {}}
    player_rows = []
    for path in sorted((root / "data/raw/statsbomb/events").glob("*.json")):
        events = json.loads(path.read_text(encoding="utf-8"))
        ids = [e["id"] for e in events]
        bad_locations = [e["id"] for e in events if "location" in e and (len(e["location"]) < 2 or not (0 <= e["location"][0] <= 120 and 0 <= e["location"][1] <= 80))]
        report["statsbomb"][path.stem] = {"events": len(events), "duplicate_ids": len(ids)-len(set(ids)), "bad_locations": len(bad_locations), "events_without_location": sum("location" not in e for e in events), "event_types": dict(Counter(e["type"]["name"] for e in events))}
        players = {}
        for e in events:
            if "player" not in e:
                continue
            key = (e["team"]["id"], e["player"]["id"])
            row = players.setdefault(key, dict(match_id=path.stem, team_id=key[0], team=e["team"]["name"], player_id=key[1], player=e["player"]["name"], passes=0, completed_passes=0, shots=0, xg=0.0, pressures=0))
            kind = e["type"]["name"]
            if kind == "Pass":
                row["passes"] += 1
                row["completed_passes"] += int("outcome" not in e["pass"])
            if kind == "Shot":
                row["shots"] += 1
                row["xg"] += e["shot"].get("statsbomb_xg", 0)
            row["pressures"] += int(kind == "Pressure")
        player_rows.extend(players.values())
    for path in sorted((root / "data/raw/metrica").glob("*RawEventsData.csv")):
        with path.open(newline="", encoding="utf-8-sig") as stream:
            rows = list(csv.DictReader(stream))
        report["metrica_events"][path.stem] = {"rows": len(rows), "columns": list(rows[0]) if rows else [], "types": dict(Counter(r.get("Type", "") for r in rows))}
    if not report["statsbomb"] or not report["metrica_events"]:
        raise ValueError("Required data absent; run fetch first")
    write_csv(root / "data/processed/statsbomb_player_match.csv", player_rows)
    (root / "reports/inspection.json").write_text(json.dumps(report, indent=2) + "\n")
    return report


def features(root, output_stride=25):
    report, summaries = {}, []
    paths = sorted((root / "data/raw/metrica").glob("*RawTrackingData_*_Team.csv.gz"))
    if not paths:
        raise ValueError("No tracking data; run fetch first")
    for path in paths:
        match, team_part = path.stem.split("_RawTrackingData_")
        team = team_part.removesuffix("_Team.csv")
        quality, rows = engineer(path, match, team, root / "data/processed" / f"{match}_{team}_features.csv.gz", output_stride=output_stride)
        quality["output_stride_frames"] = output_stride
        report[f"{match}_{team}"] = quality
        summaries.extend(rows)
    write_csv(root / "reports/tracking_player_summary.csv", summaries)
    (root / "reports/tracking_quality.json").write_text(json.dumps(report, indent=2) + "\n")
    return report


def check(inspection, tracking):
    errors = []
    for name, report in inspection["statsbomb"].items():
        if report["duplicate_ids"] or report["bad_locations"] or not report["events"]:
            errors.append(f"StatsBomb {name}: invalid IDs/locations or empty data")
    for name, report in tracking.items():
        if not report["frames"] or report["duplicate_or_unordered_frames"] or report["invalid_time_steps"] or report["partial_player_positions"]:
            errors.append(f"Metrica {name}: invalid frame sequence, time steps, or partial positions")
    # Missing positions, off-pitch coordinates and speed spikes are surfaced for review,
    # rather than silently removing legitimate substitutions and out-of-play movement.
    if errors:
        raise ValueError("; ".join(errors))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["fetch", "inspect", "features", "check", "all"])
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--competition", type=int, default=43)
    parser.add_argument("--season", type=int, default=106)
    parser.add_argument("--matches", type=int, default=3)
    parser.add_argument("--output-stride", type=int, default=25, help="Retain every Nth frame in feature CSV; summaries always use all frames")
    parser.add_argument("--game", type=int, choices=[1, 2], default=1)
    args = parser.parse_args()
    if args.matches < 1 or args.output_stride < 1:
        parser.error("--matches and --output-stride must be positive")
    root = args.root.resolve()
    for folder in ["reports", "data/processed"]:
        (root / folder).mkdir(parents=True, exist_ok=True)
    if args.command in ("fetch", "all"):
        fetch(root, args.competition, args.season, args.matches, args.game)
    if args.command in ("inspect", "all", "check"):
        inspection = inspect(root)
    if args.command in ("features", "all", "check"):
        tracking = features(root, args.output_stride)
    if args.command in ("all", "check"):
        check(inspection, tracking)
    print(f"Completed {args.command}. Reports: {root / 'reports'}")
