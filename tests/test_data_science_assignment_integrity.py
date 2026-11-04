import math
import unittest
from examples.data_science.assignment_integrity import audit_assignment_ratio


class AssignmentIntegrityTests(unittest.TestCase):
    def test_balanced_arms(self):
        data = [(f"u{i}", "A" if i % 2 else "B") for i in range(100)]
        r = audit_assignment_ratio(data, {"A": .5, "B": .5})
        self.assertEqual(r["status"], "no_srm_alarm_detected")
        self.assertAlmostEqual(r["approx_p_value"], 1.0)

    def test_srm_alarm(self):
        data = [(f"u{i}", "A" if i < 850 else "B") for i in range(1000)]
        r = audit_assignment_ratio(data, {"A": .5, "B": .5})
        self.assertEqual(r["status"], "investigate_srm")
        self.assertLess(r["approx_p_value"], .001)

    def test_custom_allocation_not_false_alarm(self):
        data = [(f"u{i}", "A" if i < 80 else "B") for i in range(100)]
        r = audit_assignment_ratio(data, {"A": .8, "B": .2})
        self.assertEqual(r["status"], "no_srm_alarm_detected")
        self.assertEqual(r["chi_square"], 0)

    def test_deduplicates_repeated_event(self):
        data = [(f"u{i}", "A" if i % 2 else "B") for i in range(100)]
        r = audit_assignment_ratio(data + [data[0], data[1]], {"A": .5, "B": .5})
        self.assertEqual(r["total_randomized_units"], 100)
        self.assertEqual(r["duplicate_assignment_events"], 2)

    def test_conflicting_assignment_rejected(self):
        with self.assertRaisesRegex(ValueError, "Conflicting"):
            audit_assignment_ratio([("u1", "A"), ("u1", "B")], {"A": .5, "B": .5})

    def test_no_data_inconclusive(self):
        r = audit_assignment_ratio([], {"A": .5, "B": .5})
        self.assertEqual(r["status"], "insufficient_expected_count")
        self.assertIsNone(r["approx_p_value"])

    def test_sparse_expected_inconclusive(self):
        r = audit_assignment_ratio([("u1", "A")] * 10, {"A": .99, "B": .01})
        self.assertEqual(r["status"], "insufficient_expected_count")

    def test_expected_at_five_is_valid(self):
        data = [(str(i), "A") for i in range(10)]
        r = audit_assignment_ratio(data, {"A": .5, "B": .5})
        self.assertIsNotNone(r["approx_p_value"])

    def test_unknown_arm_rejected(self):
        with self.assertRaisesRegex(ValueError, "unknown arm"):
            audit_assignment_ratio([("u1", "C")], {"A": .5, "B": .5})

    def test_unhashable_arm_rejected(self):
        with self.assertRaisesRegex(ValueError, "Arm must be a string"):
            audit_assignment_ratio([("u1", ["A"])], {"A": .5, "B": .5})

    def test_malformed_event_rejected(self):
        with self.assertRaisesRegex(ValueError, "pair"):
            audit_assignment_ratio([("u1",)], {"A": .5, "B": .5})

    def test_invalid_unit_rejected(self):
        with self.assertRaisesRegex(ValueError, "unit IDs"):
            audit_assignment_ratio([("  ", "A")], {"A": .5, "B": .5})

    def test_three_arms_rejected(self):
        with self.assertRaisesRegex(ValueError, "Exactly two"):
            audit_assignment_ratio([], {"A": .3, "B": .3, "C": .4})

    def test_bad_ratio_rejected(self):
        for ratio in (float("nan"), float("inf"), -1, 0, 1, True):
            with self.subTest(ratio=ratio), self.assertRaises(ValueError):
                audit_assignment_ratio([], {"A": ratio, "B": .5})

    def test_ratio_sum_rejected(self):
        with self.assertRaisesRegex(ValueError, "sum to one"):
            audit_assignment_ratio([], {"A": .7, "B": .4})

    def test_bad_alpha_rejected(self):
        for alpha in (float("nan"), float("inf"), 0, 1, True):
            with self.subTest(alpha=alpha), self.assertRaises(ValueError):
                audit_assignment_ratio([], {"A": .5, "B": .5}, alpha=alpha)

    def test_bad_expected_threshold_rejected(self):
        for threshold in (float("nan"), float("inf"), 4, True):
            with self.subTest(threshold=threshold), self.assertRaises(ValueError):
                audit_assignment_ratio([], {"A": .5, "B": .5}, minimum_expected_per_arm=threshold)

    def test_large_sample_pvalue_finite(self):
        data = [(f"u{i}", "A" if i < 750 else "B") for i in range(1000)]
        r = audit_assignment_ratio(data, {"A": .5, "B": .5})
        self.assertTrue(math.isfinite(r["approx_p_value"]))


if __name__ == "__main__":
    unittest.main()
