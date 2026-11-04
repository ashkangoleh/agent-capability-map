"""Bounded, model-free forecasting validation contracts.

All time series are single-series unless a caller explicitly splits panels first.
These checks do not fit models or prove future covariate availability from source logs.
"""

from datetime import datetime
from math import fsum, isclose, isfinite
from numbers import Integral, Real


def _positive_int(value, name, *, allow_zero=False):
    if isinstance(value, bool) or not isinstance(value, Integral) or value < (0 if allow_zero else 1):
        raise ValueError(f"{name} must be a {'nonnegative' if allow_zero else 'positive'} integer")
    return int(value)


def _finite(value, name):
    if isinstance(value, bool) or not isinstance(value, Real):
        raise ValueError(f"{name} must be finite")
    try:
        number = float(value)
    except (OverflowError, TypeError, ValueError) as exc:
        raise ValueError(f"{name} must be finite") from exc
    if not isfinite(number):
        raise ValueError(f"{name} must be finite")
    return number


def rolling_origin_splits(n_observations, *, min_train_size, horizon, step=1,
                          gap=0, max_train_size=None, max_windows=1000):
    """Return expanding/rolling train and future index ranges, half-open.

    The gap is measured in *observations*, never calendar duration. Overlapping
    horizons are allowed when step < horizon, so fold errors are dependent.
    """
    n = _positive_int(n_observations, "n_observations")
    initial = _positive_int(min_train_size, "min_train_size")
    horizon = _positive_int(horizon, "horizon")
    step = _positive_int(step, "step")
    gap = _positive_int(gap, "gap", allow_zero=True)
    limit = _positive_int(max_windows, "max_windows")
    maximum = None if max_train_size is None else _positive_int(max_train_size, "max_train_size")
    if maximum is not None and maximum < initial:
        raise ValueError("max_train_size must be >= min_train_size")
    if initial + gap + horizon > n:
        raise ValueError("Insufficient observations for train, gap and horizon")
    folds = []
    train_stop = initial
    while train_stop + gap + horizon <= n:
        if len(folds) == limit:
            raise ValueError("Too many rolling-origin folds; increase max_windows explicitly")
        train_start = max(0, train_stop - maximum) if maximum is not None else 0
        start = train_stop + gap
        folds.append({
            "train": (train_start, train_stop),
            "evaluation": (start, start + horizon),
            "origin_index": train_stop - 1,
            "horizon": horizon,
        })
        train_stop += step
    return folds


def audit_forecast_availability(observation_times, label_available_times, *,
                                train_indices, evaluation_indices,
                                future_covariate_available_times=None):
    """Enforce a historical forecast origin without future labels or exogenous data.

    This is *one* series. Times must be aware and strictly increasing; calendars,
    materialization latency and data lineage require separate source validation.
    """
    observations = list(observation_times)
    labels = list(label_available_times)
    n = len(observations)
    if n < 2 or len(labels) != n:
        raise ValueError("Observation and label timestamp lengths must match (at least two)")
    arrays = [observations, labels]
    if future_covariate_available_times is not None:
        future_available = list(future_covariate_available_times)
        if len(future_available) != n:
            raise ValueError("Future covariate availability lengths must match")
        arrays.append(future_available)
    else:
        future_available = None
    for array in arrays:
        if any(not isinstance(t, datetime) or t.tzinfo is None or t.utcoffset() is None for t in array):
            raise ValueError("Timestamps must be timezone-aware datetimes")
    if any(b <= a for a, b in zip(observations, observations[1:])):
        raise ValueError("Observation timestamps must be strictly increasing")

    def checked(indices, label):
        values = list(indices)
        if not values or any(isinstance(i, bool) or not isinstance(i, Integral) or i < 0 or i >= n for i in values):
            raise ValueError(f"{label} indices must be valid and non-empty")
        if len(set(values)) != len(values):
            raise ValueError(f"{label} contains duplicate indices")
        return set(values)

    train = checked(train_indices, "Train")
    evaluation = checked(evaluation_indices, "Evaluation")
    if train & evaluation:
        raise ValueError("Train/evaluation indices overlap")
    origin = max(observations[i] for i in train)
    if min(observations[i] for i in evaluation) <= origin:
        raise ValueError("Evaluation includes information at/before forecast origin")
    if any(labels[i] > origin for i in train):
        raise ValueError("Training label unavailable at forecast origin")
    if future_available is not None and any(future_available[i] > origin for i in evaluation):
        raise ValueError("Future covariate unavailable at forecast origin")
    return {"train_rows": len(train), "evaluation_rows": len(evaluation), "origin_at": origin}


def quantile_forecast_report(actual, quantile_forecasts):
    """Compute empirical pinball and interval checks on previously held-out rows."""
    y = [_finite(v, "actual") for v in actual]
    if not y or len(quantile_forecasts) < 2:
        raise ValueError("Need nonempty actual values and at least two quantile levels")
    predictions = {}
    for q, values in quantile_forecasts.items():
        level = _finite(q, "quantile level")
        if not 0 < level < 1 or level in predictions:
            raise ValueError("Quantile levels must be distinct in (0, 1)")
        forecast = [_finite(v, "quantile prediction") for v in values]
        if len(forecast) != len(y):
            raise ValueError("Quantile arrays must match actual length")
        predictions[level] = forecast
    levels = sorted(predictions)
    for i in range(len(y)):
        if any(predictions[a][i] > predictions[b][i] for a, b in zip(levels, levels[1:])):
            raise ValueError("Quantile crossing detected; do not silently reorder predictions")
    losses = {}
    for q in levels:
        individual = []
        for actual_value, pred in zip(y, predictions[q]):
            err = actual_value - pred
            if not isfinite(err):
                raise ValueError("Quantile error overflow")
            individual.append(q * err if err >= 0 else (q - 1) * err)
        loss = fsum(individual) / len(y)
        if not isfinite(loss):
            raise ValueError("Pinball loss overflow")
        losses[q] = loss
    lo, hi = predictions[levels[0]], predictions[levels[-1]]
    widths = [upper - lower for lower, upper in zip(lo, hi)]
    if any(not isfinite(w) for w in widths):
        raise ValueError("Quantile interval width overflow")
    coverage = sum(left <= v <= right for v, left, right in zip(y, lo, hi)) / len(y)
    return {"evaluation_rows": len(y), "pinball_by_quantile": losses,
            "outer_quantile_levels": (levels[0], levels[-1]),
            "nominal_interval_mass": levels[-1] - levels[0],
            "empirical_interval_coverage": coverage,
            "mean_interval_width": fsum(widths) / len(widths)}


def hierarchy_coherence_report(bottom_forecasts, parent_forecasts, membership, *, tolerance=1e-9):
    """Check one-level additive coherence; does not perform reconciliation."""
    tol = _finite(tolerance, "tolerance")
    if tol < 0:
        raise ValueError("tolerance must be nonnegative")
    if not bottom_forecasts or not parent_forecasts or set(membership) != set(parent_forecasts):
        raise ValueError("Parent membership and forecast keys must match and be nonempty")
    bottom = {name: [_finite(v, "bottom forecast") for v in values]
              for name, values in bottom_forecasts.items()}
    parents = {name: [_finite(v, "parent forecast") for v in values]
               for name, values in parent_forecasts.items()}
    sizes = {len(values) for values in list(bottom.values()) + list(parents.values())}
    if len(sizes) != 1 or 0 in sizes:
        raise ValueError("All hierarchical forecast series must share a nonempty horizon")
    errors = {}
    coherent = True
    for parent, children in membership.items():
        ids = list(children)
        if not ids or len(ids) != len(set(ids)) or any(key not in bottom for key in ids):
            raise ValueError("Each parent requires unique, known bottom series")
        diffs = []
        for i, expected in enumerate(parents[parent]):
            total = fsum(bottom[key][i] for key in ids)
            difference = expected - total
            if not isfinite(difference):
                raise ValueError("Hierarchical sum overflow")
            diffs.append(difference)
            if not isclose(expected, total, rel_tol=0, abs_tol=tol):
                coherent = False
        errors[parent] = diffs
    return {"coherent": coherent, "absolute_tolerance": tol, "errors_by_parent": errors}


def intermittent_demand_profile(demand, *, statuses):
    """Reject stockout/missing observations rather than recoding them as zero demand."""
    values = [_finite(value, "demand") for value in demand]
    states = list(statuses)
    if not values or len(states) != len(values):
        raise ValueError("Demand and status lengths must match and be nonempty")
    if any(state not in ("observed", "missing", "stockout") for state in states):
        raise ValueError("Unexpected demand observation status")
    if any(v < 0 for v in values):
        raise ValueError("Demand must be nonnegative")
    if any(state != "observed" for state in states):
        raise ValueError("Stockout/missing observations require separate demand reconstruction")
    nonzero = [v for v in values if v > 0]
    return {"periods": len(values), "nonzero_periods": len(nonzero),
            "zero_fraction": (len(values) - len(nonzero)) / len(values),
            "average_demand_interval": len(values) / len(nonzero) if nonzero else None,
            "mean_nonzero_size": fsum(nonzero) / len(nonzero) if nonzero else None}
