import unittest
from datetime import datetime, timedelta, timezone

from examples.data_science.split_integrity import validate_split_contract


class SplitIntegrityTests(unittest.TestCase):
    def setUp(self):
        self.ts = [datetime(2026, 1, 1, tzinfo=timezone.utc) + timedelta(days=i) for i in range(6)]

    def test_valid_grouped_split(self):
        result = validate_split_contract([0, 1], [2, 3], n_samples=4, groups=["a", "a", "b", "b"])
        self.assertEqual(result, {"train_rows": 2, "test_rows": 2})

    def test_valid_temporal_split_with_delayed_labels(self):
        result = validate_split_contract([0, 1], [4, 5], n_samples=6, prediction_times=self.ts,
                                         label_available_times=[t + timedelta(days=1) for t in self.ts],
                                         forward_only=True)
        self.assertEqual(result["test_rows"], 2)

    def test_index_overlap_rejected(self):
        with self.assertRaisesRegex(ValueError, "index overlap"):
            validate_split_contract([0, 1], [1, 2], n_samples=4)

    def test_repeated_indices_rejected(self):
        with self.assertRaisesRegex(ValueError, "repeated indices"):
            validate_split_contract([0, 0], [1], n_samples=3)

    def test_boolean_index_rejected(self):
        with self.assertRaisesRegex(ValueError, "invalid indices"):
            validate_split_contract([True], [1], n_samples=3)

    def test_invalid_dataset_size_rejected(self):
        with self.assertRaisesRegex(ValueError, "n_samples"):
            validate_split_contract([0], [1], n_samples=True)

    def test_numpy_indices_when_available(self):
        try:
            import numpy as np
        except ImportError:
            self.skipTest("optional numpy is not installed")
        result = validate_split_contract(np.array([0, 1]), np.array([2, 3]), n_samples=4,
                                         groups=np.array(["a", "a", "b", "b"]))
        self.assertEqual(result, {"train_rows": 2, "test_rows": 2})

    def test_out_of_range_rejected(self):
        with self.assertRaisesRegex(ValueError, "invalid indices"):
            validate_split_contract([0], [3], n_samples=3)

    def test_group_overlap_rejected(self):
        with self.assertRaisesRegex(ValueError, "group overlap"):
            validate_split_contract([0], [1], n_samples=2, groups=["same", "same"])

    def test_group_length_rejected(self):
        with self.assertRaisesRegex(ValueError, "groups length"):
            validate_split_contract([0], [1], n_samples=2, groups=["a"])

    def test_forward_split_missing_times_rejected(self):
        with self.assertRaisesRegex(ValueError, "requires prediction_times"):
            validate_split_contract([0], [1], n_samples=2, forward_only=True)

    def test_temporal_reverse_rejected(self):
        with self.assertRaisesRegex(ValueError, "not strictly before"):
            validate_split_contract([4, 5], [0, 1], n_samples=6, prediction_times=self.ts,
                                    forward_only=True)

    def test_temporal_duplicate_timestamp_rejected(self):
        ts = [self.ts[0], self.ts[0]]
        with self.assertRaisesRegex(ValueError, "not strictly before"):
            validate_split_contract([0], [1], n_samples=2, prediction_times=ts, forward_only=True)

    def test_label_availability_rejected(self):
        labels = [t + timedelta(days=5) for t in self.ts]
        with self.assertRaisesRegex(ValueError, "label is not available"):
            validate_split_contract([0, 1], [4, 5], n_samples=6, prediction_times=self.ts,
                                    label_available_times=labels, forward_only=True)

    def test_naive_timestamp_rejected(self):
        bad = [datetime(2026, 1, 1), datetime(2026, 1, 2)]
        with self.assertRaisesRegex(ValueError, "timezone-aware"):
            validate_split_contract([0], [1], n_samples=2, prediction_times=bad, forward_only=True)

    def test_label_availability_requires_forward_only(self):
        with self.assertRaisesRegex(ValueError, "requires forward_only"):
            validate_split_contract([0], [1], n_samples=2, label_available_times=self.ts[:2])

    def test_time_array_length_rejected(self):
        with self.assertRaisesRegex(ValueError, "length must match"):
            validate_split_contract([0], [1], n_samples=2, prediction_times=self.ts, forward_only=True)


if __name__ == "__main__":
    unittest.main()
