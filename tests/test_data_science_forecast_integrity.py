import unittest
from datetime import datetime, timedelta, timezone
from examples.data_science.forecast_integrity import (
    rolling_origin_splits, audit_forecast_availability, quantile_forecast_report,
    hierarchy_coherence_report, intermittent_demand_profile,
)

class ForecastIntegrityTests(unittest.TestCase):
    def setUp(self):
        self.t = [datetime(2026, 1, 1, tzinfo=timezone.utc) + timedelta(days=i) for i in range(12)]

    def test_origin_expanding(self):
        folds = rolling_origin_splits(12, min_train_size=5, horizon=2, step=2, gap=1)
        self.assertEqual([(f['train'], f['evaluation']) for f in folds],
                         [((0, 5), (6, 8)), ((0, 7), (8, 10)), ((0, 9), (10, 12))])

    def test_origin_rolling(self):
        folds = rolling_origin_splits(12, min_train_size=4, horizon=2, step=3, max_train_size=4)
        self.assertEqual([f['train'] for f in folds], [(0, 4), (3, 7), (6, 10)])

    def test_origin_multiple_horizons(self):
        self.assertEqual(len(rolling_origin_splits(9, min_train_size=4, horizon=3, step=1)), 3)

    def test_origin_insufficient(self):
        with self.assertRaisesRegex(ValueError, 'Insufficient'):
            rolling_origin_splits(6, min_train_size=4, horizon=3)

    def test_origin_bad_bounds(self):
        for kwargs in ({'step': 0}, {'gap': -1}, {'min_train_size': True}, {'max_train_size': 2}):
            with self.subTest(kwargs=kwargs), self.assertRaises(ValueError):
                rolling_origin_splits(12, **dict({'min_train_size': 4, 'horizon': 2}, **kwargs))

    def test_origin_window_bound(self):
        with self.assertRaisesRegex(ValueError, 'Too many'):
            rolling_origin_splits(100, min_train_size=4, horizon=2, max_windows=2)

    def test_availability_valid(self):
        labels = [t + timedelta(days=1) for t in self.t]
        labels[2] = self.t[2]  # The last training label is available at origin.
        v = audit_forecast_availability(self.t, labels,
                                        train_indices=[0, 1, 2], evaluation_indices=[5, 6],
                                        future_covariate_available_times=[self.t[0]] * 12)
        self.assertEqual(v['origin_at'], self.t[2])

    def test_availability_delayed_label(self):
        with self.assertRaisesRegex(ValueError, 'label unavailable'):
            audit_forecast_availability(self.t, [t + timedelta(days=5) for t in self.t],
                                        train_indices=[0, 1, 2], evaluation_indices=[5])

    def test_availability_future_covariate(self):
        with self.assertRaisesRegex(ValueError, 'covariate unavailable'):
            audit_forecast_availability(self.t, self.t, train_indices=[0, 1], evaluation_indices=[5],
                                        future_covariate_available_times=self.t)

    def test_availability_reverse(self):
        with self.assertRaisesRegex(ValueError, 'at/before'):
            audit_forecast_availability(self.t, self.t, train_indices=[5], evaluation_indices=[1])

    def test_availability_overlap(self):
        with self.assertRaisesRegex(ValueError, 'overlap'):
            audit_forecast_availability(self.t, self.t, train_indices=[0, 1], evaluation_indices=[1, 2])

    def test_availability_naive(self):
        with self.assertRaisesRegex(ValueError, 'timezone-aware'):
            audit_forecast_availability([datetime(2026, 1, 1), datetime(2026, 1, 2)],
                                        self.t[:2], train_indices=[0], evaluation_indices=[1])

    def test_availability_non_monotone(self):
        with self.assertRaisesRegex(ValueError, 'strictly increasing'):
            audit_forecast_availability([self.t[0], self.t[0]], [self.t[0]] * 2,
                                        train_indices=[0], evaluation_indices=[1])

    def test_quantiles_score_and_coverage(self):
        v = quantile_forecast_report([0, 10], {0.1: [-2, 8], 0.9: [2, 12]})
        self.assertEqual(v['empirical_interval_coverage'], 1)
        self.assertEqual(v['nominal_interval_mass'], 0.8)
        self.assertEqual(v['mean_interval_width'], 4)
        self.assertAlmostEqual(v['pinball_by_quantile'][0.1], 0.2)

    def test_quantiles_cross(self):
        with self.assertRaisesRegex(ValueError, 'crossing'):
            quantile_forecast_report([0], {0.1: [2], 0.9: [1]})

    def test_quantiles_length(self):
        with self.assertRaisesRegex(ValueError, 'match'):
            quantile_forecast_report([0, 1], {0.1: [0], 0.9: [1, 2]})

    def test_quantiles_level(self):
        for level in (0, 1, True, float('nan')):
            with self.subTest(level=level), self.assertRaises(ValueError):
                quantile_forecast_report([0], {level: [0], 0.9: [1]})

    def test_quantiles_nonfinite(self):
        with self.assertRaisesRegex(ValueError, 'finite'):
            quantile_forecast_report([0], {0.1: [float('inf')], 0.9: [1]})

    def test_quantiles_overflow(self):
        with self.assertRaisesRegex(ValueError, 'overflow'):
            quantile_forecast_report([1e308], {0.1: [-1e308], 0.9: [1e308]})

    def test_coherence_yes(self):
        v = hierarchy_coherence_report({'a': [1, 2], 'b': [3, 4]}, {'total': [4, 6]}, {'total': ['a', 'b']})
        self.assertTrue(v['coherent'])

    def test_coherence_no(self):
        v = hierarchy_coherence_report({'a': [1], 'b': [2]}, {'total': [4]}, {'total': ['a', 'b']})
        self.assertFalse(v['coherent'])
        self.assertEqual(v['errors_by_parent']['total'], [1])

    def test_coherence_unknown_member(self):
        with self.assertRaisesRegex(ValueError, 'unique, known'):
            hierarchy_coherence_report({'a': [1]}, {'total': [1]}, {'total': ['x']})

    def test_coherence_duplicate_member(self):
        with self.assertRaisesRegex(ValueError, 'unique, known'):
            hierarchy_coherence_report({'a': [1]}, {'total': [1]}, {'total': ['a', 'a']})

    def test_coherence_horizon(self):
        with self.assertRaisesRegex(ValueError, 'share a nonempty'):
            hierarchy_coherence_report({'a': [1]}, {'total': [1, 2]}, {'total': ['a']})

    def test_intermittent_profile(self):
        v = intermittent_demand_profile([0, 0, 4, 0, 2, 0], statuses=['observed'] * 6)
        self.assertEqual(v['average_demand_interval'], 3)
        self.assertEqual(v['mean_nonzero_size'], 3)

    def test_intermittent_all_zero(self):
        v = intermittent_demand_profile([0, 0], statuses=['observed', 'observed'])
        self.assertIsNone(v['average_demand_interval'])

    def test_intermittent_stockout(self):
        with self.assertRaisesRegex(ValueError, 'reconstruction'):
            intermittent_demand_profile([0, 0], statuses=['observed', 'stockout'])

    def test_intermittent_missing(self):
        with self.assertRaisesRegex(ValueError, 'reconstruction'):
            intermittent_demand_profile([0], statuses=['missing'])

    def test_intermittent_negative(self):
        with self.assertRaisesRegex(ValueError, 'nonnegative'):
            intermittent_demand_profile([-1], statuses=['observed'])

    def test_intermittent_bad_status(self):
        with self.assertRaisesRegex(ValueError, 'Unexpected'):
            intermittent_demand_profile([0], statuses=['unexpected'])

if __name__ == '__main__':
    unittest.main()
