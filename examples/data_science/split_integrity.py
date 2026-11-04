"""Check declared fold boundaries; this does not prove a model is leakage-free."""

from datetime import datetime
from typing import Sequence


def validate_split_contract(
    train_indices: Sequence[int],
    test_indices: Sequence[int],
    *,
    n_samples: int,
    groups: Sequence[object] | None = None,
    prediction_times: Sequence[datetime] | None = None,
    label_available_times: Sequence[datetime] | None = None,
    forward_only: bool = False,
) -> dict[str, int]:
    """Fail closed for index, group and optional forward-only temporal leakage.

    All temporal inputs must be timezone-aware datetimes. A global time order
    is conservative: grouped/time-aware tasks need a design-specific splitter.
    A gap in row counts is not equivalent to a wall-clock embargo.
    """
    if isinstance(n_samples, bool) or not isinstance(n_samples, int) or n_samples < 2:
        raise ValueError("n_samples must be an integer >= 2")

    def indices(values: Sequence[int], label: str) -> set[int]:
        if not values:
            raise ValueError(f"{label} must be non-empty")
        if any(isinstance(i, bool) or not isinstance(i, int) or i < 0 or i >= n_samples for i in values):
            raise ValueError(f"{label} contains invalid indices")
        if len(set(values)) != len(values):
            raise ValueError(f"{label} contains repeated indices")
        return set(values)

    train = indices(train_indices, "train_indices")
    test = indices(test_indices, "test_indices")
    if train & test:
        raise ValueError("Train/test index overlap")

    if groups is not None:
        if len(groups) != n_samples:
            raise ValueError("groups length must match n_samples")
        try:
            train_groups = {groups[i] for i in train}
            test_groups = {groups[i] for i in test}
        except TypeError as exc:
            raise ValueError("groups must contain hashable values") from exc
        if train_groups & test_groups:
            raise ValueError("Train/test group overlap")

    if label_available_times is not None and not forward_only:
        raise ValueError("label_available_times requires forward_only=True")
    if forward_only and prediction_times is None:
        raise ValueError("forward_only requires prediction_times")

    def checked_times(values: Sequence[datetime] | None, label: str) -> None:
        if values is None:
            return
        if len(values) != n_samples:
            raise ValueError(f"{label} length must match n_samples")
        if any(not isinstance(t, datetime) or t.tzinfo is None or t.utcoffset() is None for t in values):
            raise ValueError(f"{label} must contain timezone-aware datetimes")

    checked_times(prediction_times, "prediction_times")
    checked_times(label_available_times, "label_available_times")
    if forward_only:
        first_test_time = min(prediction_times[i] for i in test)
        if max(prediction_times[i] for i in train) >= first_test_time:
            raise ValueError("Train prediction time is not strictly before test")
        if label_available_times is not None:
            if max(label_available_times[i] for i in train) >= first_test_time:
                raise ValueError("Train label is not available before test prediction")

    return {"train_rows": len(train), "test_rows": len(test)}
