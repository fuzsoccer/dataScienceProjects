import csv
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from soccer.tracking import engineer


class TrackingTests(unittest.TestCase):
    def test_boundaries_gaps_spikes_and_units(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parent) as folder:
            raw, out = Path(folder)/"raw.csv", Path(folder)/"out.csv"
            with raw.open("w", newline="") as stream:
                writer = csv.writer(stream)
                writer.writerows([
                    ["", "", "", "Home", "Home", "", ""],
                    ["", "", "", "7", "", "", ""],
                    ["Period", "Frame", "Time [s]", "Player7", "", "Ball", ""],
                    [1, 1, 0, .5, .5, .5, .5],
                    [1, 2, .04, .501, .5, .5, .5],
                    [1, 3, .08, "NaN", "NaN", .5, .5],
                    [1, 4, .12, .7, .5, .5, .5],
                    [1, 5, .16, .9, .5, .5, .5],
                    [2, 6, 2700, .1, .5, .5, .5],
                    [2, 7, 2700.04, .101, .5, .5, .5],
                ])
            quality, summary = engineer(raw, "test", "Home", out)
            with out.open() as stream:
                rows = list(csv.DictReader(stream))
            self.assertAlmostEqual(float(rows[1]["speed_mps"]), 2.625)
            self.assertEqual(rows[2]["speed_mps"], "")  # gap
            self.assertEqual(rows[4]["speed_mps"], "")  # period boundary
            self.assertEqual(quality["rejected_speed_intervals"], 1)
            self.assertAlmostEqual(summary[0]["distance_m"], .21)
            self.assertEqual(quality["missing_player_positions"], 1)
            sparse_quality, sparse_summary = engineer(raw, "test", "Home", Path(folder)/"sparse.csv", output_stride=25)
            self.assertEqual(summary, sparse_summary)
            self.assertEqual(quality, sparse_quality)


if __name__ == "__main__":
    unittest.main()
