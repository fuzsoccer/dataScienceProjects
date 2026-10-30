import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from soccer.cli import check


class QualityTests(unittest.TestCase):
    def test_duplicate_events_fail(self):
        with self.assertRaises(ValueError):
            check({"statsbomb": {"m": {"events": 3, "duplicate_ids": 1, "bad_locations": 0}}}, {})

    def test_tracking_sequence_fails(self):
        with self.assertRaises(ValueError):
            check({"statsbomb": {}}, {"g": {"frames": 2, "duplicate_or_unordered_frames": 1, "invalid_time_steps": 0, "partial_player_positions": 0}})
