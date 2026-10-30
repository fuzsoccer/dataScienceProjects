"""Offline publication contracts and known-value tests of notebook functions."""
import json
import math
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def notebook(name):
    return json.loads((ROOT / "notebooks" / name).read_text(encoding="utf-8"))


def functions(name, marker, namespace):
    cells = notebook(name)["cells"]
    source = next("".join(c["source"]) for c in cells if c["cell_type"] == "code" and marker in "".join(c["source"]))
    exec(compile(source, name, "exec"), namespace)
    return namespace


class NotebookContracts(unittest.TestCase):
    def test_publication_cells_are_portable_and_cleared(self):
        paths = sorted((ROOT / "notebooks").glob("*.ipynb"))
        self.assertEqual(len(paths), 8)
        for path in paths:
            nb = json.loads(path.read_text(encoding="utf-8"))
            ids = [c["id"] for c in nb["cells"]]
            self.assertEqual(len(ids), len(set(ids)), path.name)
            for cell in nb["cells"]:
                source = "".join(cell["source"])
                for personal_path in ("C:\\Users\\", "iCloudDrive", "SAVED_PROJECT"):
                    self.assertNotIn(personal_path, source, path.name)
                if cell["cell_type"] == "code":
                    self.assertEqual(cell["outputs"], [], path.name)
                    self.assertIsNone(cell["execution_count"], path.name)
                    compile(source, f"{path.name}:{cell['id']}", "exec")

    def test_setup_enables_missing_data_on_fresh_checkout(self):
        source = "\n".join("".join(c["source"]) for c in notebook("01_setup.ipynb")["cells"])
        self.assertIn('DOWNLOAD_DATA = not (ROOT / "data/raw/metrica/Sample_Game_1_RawEventsData.csv").is_file()', source)
        self.assertIn('REBUILD_FEATURES = not (ROOT / "reports/tracking_quality.json").is_file()', source)


class ExpectedThreatTests(unittest.TestCase):
    def setUp(self):
        self.ns = functions("06_expected_threat.ipynb", "def fit_xt(", {"NX": 2, "NY": 1})

    def test_known_surface_signed_changes_and_missing_support(self):
        def action(kind, start, end=None, successful=False, goal=False):
            return dict(kind=kind, start_zone=start, end_zone=end, successful=successful, goal=goal)

        model = self.ns["fit_xt"]([
            action("Pass", 0, 1, True), action("Pass", 0),
            action("Shot", 1, goal=True), action("Shot", 1),
        ], nx=2, ny=1)
        self.assertAlmostEqual(model["values"][0], .25)
        self.assertAlmostEqual(model["values"][1], .5)
        self.assertAlmostEqual(self.ns["rate_movement"](action("Carry", 1, 0, True), model), -.25)
        self.assertIsNone(self.ns["rate_movement"](action("Pass", 0), model))
        model["start_counts"][0] = 0
        self.assertIsNone(self.ns["rate_movement"](action("Pass", 0, 1, True), model))

    def test_coordinate_bounds_and_invalid_completed_endpoint(self):
        self.assertEqual(self.ns["zone"]([120, 80], 2, 1), 1)
        self.assertIsNone(self.ns["zone"]([math.nan, 40], 2, 1))
        event = dict(id="test", index=1, period=1, timestamp="00:01:00.000", type={"name": "Pass"},
                     play_pattern={"name": "Regular Play"}, team={"id": 1, "name": "Team"},
                     player={"id": 1, "name": "Player"}, location=[60, 40])
        event["pass"] = {"end_location": [130, 40]}
        actions, audit = self.ns["extract_actions"]([event], "test", 2, 1)
        self.assertEqual(actions, [])
        self.assertEqual(audit["invalid_successful_end"], 1)


class ParticipationTests(unittest.TestCase):
    def test_stoppage_halftime_substitution_and_bench_dismissal(self):
        ns = functions("04_striker_profiles.ipynb", "def playing_time(", {"Counter": Counter})
        roster, events = set(), []
        for team in (1, 2):
            lineup = []
            for player in range(team * 100, team * 100 + 11):
                roster.add((team, player))
                lineup.append({"player": {"id": player, "name": str(player)}})
            events.append(dict(type={"name": "Starting XI"}, period=1, timestamp="00:00:00.000",
                               team={"id": team, "name": str(team)}, tactics={"lineup": lineup}))
        roster.update({(1, 199), (1, 198)})
        events.extend([
            dict(type={"name": "Half End"}, period=1, timestamp="00:50:00.000"),
            dict(type={"name": "Half End"}, period=2, timestamp="00:48:00.000"),
            dict(type={"name": "Substitution"}, period=2, timestamp="00:00:00.000",
                 team={"id": 1, "name": "Team"}, player={"id": 100, "name": "Outgoing"},
                 substitution={"replacement": {"id": 199, "name": "Incoming"}}),
            dict(type={"name": "Bad Behaviour"}, period=2, timestamp="00:10:00.000",
                 team={"id": 1, "name": "Team"}, player={"id": 198, "name": "Bench"},
                 position={"name": "Substitute"}, bad_behaviour={"card": {"name": "Red Card"}}),
        ])
        rows, audit = ns["playing_time"](events, roster)
        self.assertAlmostEqual(rows[(1, 100)]["minutes"], 50)
        self.assertAlmostEqual(rows[(1, 199)]["minutes"], 48)
        self.assertNotIn((1, 198), rows)
        self.assertEqual(audit["bench_discipline_events"], 1)
        self.assertEqual(audit["dismissals"], 0)
        self.assertAlmostEqual(sum(r["minutes"] for k, r in rows.items() if k[0] == 1), 11 * 98)
