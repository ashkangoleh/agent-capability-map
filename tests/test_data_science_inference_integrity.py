import unittest
from math import isclose
from examples.data_science.inference_integrity import (
    adjust_pvalues, survey_design_guard, pool_scalar_imputations,
)


class InferenceIntegrityTests(unittest.TestCase):
    def test_bh_original_order(self):
        v = adjust_pvalues([0.04, 0.001, 0.03, 0.20], method="fdr_bh")
        self.assertEqual(v["reject"], [False, True, False, False])
        for actual, target in zip(v["adjusted_pvalues"], [0.05333333333333334, .004, .05333333333333334, .2]):
            self.assertAlmostEqual(actual, target)

    def test_by_more_conservative(self):
        bh = adjust_pvalues([.001, .02, .04], method="fdr_bh")
        by = adjust_pvalues([.001, .02, .04], method="fdr_by")
        self.assertTrue(all(y >= x for x, y in zip(bh["adjusted_pvalues"], by["adjusted_pvalues"])))

    def test_holm_stepdown(self):
        v = adjust_pvalues([.02, .001, .04], method="holm")
        for actual, target in zip(v["adjusted_pvalues"], [.04, .003, .04]):
            self.assertAlmostEqual(actual, target)

    def test_bonferroni(self):
        self.assertEqual(adjust_pvalues([.01, .40], method="bonferroni")["adjusted_pvalues"], [.02, .8])

    def test_tie_and_extremes(self):
        self.assertEqual(adjust_pvalues([1, 0, 0], method="fdr_bh")["adjusted_pvalues"], [1, 0, 0])

    def test_invalid_pvalues(self):
        for p in (-1, 1.1, float("nan"), float("inf"), True, "x", 10 ** 1000):
            with self.subTest(p=p), self.assertRaises(ValueError):
                adjust_pvalues([p])

    def test_invalid_alpha(self):
        for alpha in (0, 1, float("nan"), True):
            with self.subTest(alpha=alpha), self.assertRaises(ValueError):
                adjust_pvalues([.1], alpha=alpha)

    def test_invalid_method(self):
        with self.assertRaisesRegex(ValueError, "Unsupported"):
            adjust_pvalues([.1], method="fdr_adaptive")

    def test_empty_family_rejected(self):
        with self.assertRaisesRegex(ValueError, "nonempty"):
            adjust_pvalues([])

    def test_survey_weighted_mean_and_kish(self):
        r = survey_design_guard([1, 3, 5, 7], [1, 1, 2, 2],
                                strata=["S", "S", "S", "S"],
                                psus=["a", "a", "b", "b"])
        self.assertEqual(r["weighted_mean_descriptive"], 14 / 3)
        self.assertAlmostEqual(r["kish_weight_effective_n_descriptive"], 3.6)
        self.assertIsNone(r["design_based_standard_error"])

    def test_survey_two_strata(self):
        r = survey_design_guard([1, 2, 3, 4], [1, 1, 1, 1],
                                strata=["A", "A", "B", "B"], psus=["1", "2", "1", "2"])
        self.assertEqual(r["strata"], 2)
        self.assertEqual(r["psus"], 4)

    def test_survey_lonely_psu(self):
        with self.assertRaisesRegex(ValueError, "Lonely PSU"):
            survey_design_guard([1, 2], [1, 1], strata=["A", "A"], psus=["same", "same"])

    def test_survey_zero_weight(self):
        with self.assertRaisesRegex(ValueError, "strictly positive"):
            survey_design_guard([1, 2], [0, 1], strata=["A", "A"], psus=["1", "2"])

    def test_survey_bad_length(self):
        with self.assertRaisesRegex(ValueError, "lengths"):
            survey_design_guard([1, 2], [1], strata=["A", "A"], psus=["1", "2"])

    def test_survey_bad_stratum(self):
        with self.assertRaisesRegex(ValueError, "strata"):
            survey_design_guard([1, 2], [1, 1], strata=["", "A"], psus=["1", "2"])

    def test_survey_bad_psu(self):
        with self.assertRaisesRegex(ValueError, "PSU"):
            survey_design_guard([1, 2], [1, 1], strata=["A", "A"], psus=["", "2"])

    def test_rubin_fixed_mean(self):
        r = pool_scalar_imputations([4, 6, 5], [1, 1, 1])
        self.assertEqual(r["pooled_estimate"], 5)
        self.assertEqual(r["between_variance"], 1)
        self.assertAlmostEqual(r["total_variance"], 1 + 4 / 3)
        self.assertAlmostEqual(r["pooled_standard_error"] ** 2, r["total_variance"])
        self.assertIsNone(r["confidence_interval"])

    def test_rubin_constant_estimates(self):
        r = pool_scalar_imputations([2, 2], [4, 4])
        self.assertEqual(r["between_variance"], 0)
        self.assertEqual(r["pooled_standard_error"], 2)

    def test_rubin_few_imputations(self):
        with self.assertRaisesRegex(ValueError, ">=2"):
            pool_scalar_imputations([3], [1])

    def test_rubin_mismatch(self):
        with self.assertRaisesRegex(ValueError, "matched"):
            pool_scalar_imputations([1, 2], [1])

    def test_rubin_negative_variance(self):
        with self.assertRaisesRegex(ValueError, "nonnegative"):
            pool_scalar_imputations([1, 2], [1, -1])

    def test_rubin_nonfinite(self):
        with self.assertRaises(ValueError):
            pool_scalar_imputations([1, float("inf")], [1, 1])

    def test_rubin_overflow(self):
        with self.assertRaisesRegex(ValueError, "overflow"):
            pool_scalar_imputations([-1e308, 1e308], [1, 1])
