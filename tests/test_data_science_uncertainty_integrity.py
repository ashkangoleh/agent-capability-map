import math
import unittest
from examples.data_science.uncertainty_integrity import (
    audit_partitions,
    binary_probability_report,
    regression_interval_report,
    split_conformal_radius,
)


class UncertaintyIntegrityTests(unittest.TestCase):
    def test_disjoint_partitions(self):
        self.assertEqual(audit_partitions(["a"], ["b", "c"], ["d"]),
                         {"train_rows": 1, "calibration_rows": 2, "evaluation_rows": 1})

    def test_training_calibration_overlap(self):
        with self.assertRaisesRegex(ValueError, "disjoint"):
            audit_partitions(["a"], ["a"], ["c"])

    def test_calibration_evaluation_overlap(self):
        with self.assertRaisesRegex(ValueError, "disjoint"):
            audit_partitions(["a"], ["b"], ["b"])

    def test_duplicate_observation_id(self):
        with self.assertRaisesRegex(ValueError, "repeated"):
            audit_partitions(["a", "a"], ["b"], ["c"])

    def test_blank_observation_id(self):
        with self.assertRaisesRegex(ValueError, "non-empty"):
            audit_partitions(["  "], ["b"], ["c"])

    def test_quantile_rank_not_interpolated(self):
        result = split_conformal_radius([1, 4, 2, 9, 3, 5, 6, 7, 8], alpha=0.1)
        self.assertEqual(result["rank"], 9)
        self.assertEqual(result["radius"], 9)

    def test_quantile_invariant_to_order(self):
        one = split_conformal_radius(list(range(1, 20)), alpha=0.2)
        two = split_conformal_radius(list(reversed(range(1, 20))), alpha=0.2)
        self.assertEqual(one, two)
        self.assertEqual(one["rank"], 16)

    def test_conformal_tiny_sample_rejected(self):
        with self.assertRaisesRegex(ValueError, "too small"):
            split_conformal_radius([1, 2], alpha=0.1)

    def test_quantile_bad_alpha_rejected(self):
        for alpha in (0, 1, True, float("nan"), float("inf")):
            with self.subTest(alpha=alpha), self.assertRaises(ValueError):
                split_conformal_radius([1, 2, 3], alpha=alpha)

    def test_bad_residual_rejected(self):
        for bad in (-1, float("nan"), float("inf"), True):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                split_conformal_radius([1, bad, 3], alpha=0.5)

    def test_interval_empirical_coverage(self):
        result = regression_interval_report([1, 3, 10], [2, 2, 2], radius=1)
        self.assertEqual(result["covered"], 2)
        self.assertEqual(result["empirical_coverage"], 2 / 3)
        self.assertEqual(result["interval_width"], 2)

    def test_interval_zero_inclusive(self):
        self.assertEqual(regression_interval_report([1], [1], radius=0)["covered"], 1)

    def test_invalid_interval_radius_rejected(self):
        for radius in (-1, float("nan"), float("inf"), True):
            with self.subTest(radius=radius), self.assertRaises(ValueError):
                regression_interval_report([1], [1], radius=radius)

    def test_mismatched_interval_sizes(self):
        with self.assertRaisesRegex(ValueError, "nonzero length"):
            regression_interval_report([1, 2], [1], radius=1)

    def test_brier_and_reliability(self):
        a = binary_probability_report([0, 1, 0, 1], [0, 1, 0.2, 0.8], bins=2, min_bin_size=2)
        self.assertAlmostEqual(a["brier_score"], 0.02)
        self.assertEqual(a["prevalence"], 0.5)
        self.assertEqual([x["count"] for x in a["reliability"]], [2, 2])
        self.assertEqual([x["event_rate"] for x in a["reliability"]], [0, 1])

    def test_sparse_bins_suppressed(self):
        a = binary_probability_report([0, 1], [0.1, 0.9], bins=2, min_bin_size=2)
        self.assertIsNone(a["reliability"][0]["event_rate"])
        self.assertIsNone(a["reliability"][1]["mean_probability"])

    def test_probability_one_last_bin(self):
        a = binary_probability_report([1], [1.0], bins=3, min_bin_size=1)
        self.assertEqual(a["reliability"][2]["count"], 1)

    def test_probability_bounds_fail(self):
        for p in (-0.01, 1.01, float("nan"), float("inf"), True):
            with self.subTest(p=p), self.assertRaises(ValueError):
                binary_probability_report([1], [p])

    def test_invalid_labels_fail(self):
        for y in (-1, 2, True, 0.5):
            with self.subTest(y=y), self.assertRaises(ValueError):
                binary_probability_report([y], [0.5])

    def test_mismatched_probability_lengths(self):
        with self.assertRaisesRegex(ValueError, "nonzero length"):
            binary_probability_report([0, 1], [0.2])

    def test_bad_bin_settings(self):
        for kwargs in ({"bins": 1}, {"bins": True}, {"min_bin_size": 0}, {"min_bin_size": True}):
            with self.subTest(kwargs=kwargs), self.assertRaises(ValueError):
                binary_probability_report([0], [0.1], **kwargs)


if __name__ == "__main__":
    unittest.main()
