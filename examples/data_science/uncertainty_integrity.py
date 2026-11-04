"""Auditable split-conformal and probability-calibration arithmetic.

These diagnostics do not train a model, test exchangeability, or certify
conditional coverage, independence or deployment performance.
"""

from math import ceil, isfinite
from numbers import Integral, Real


def _finite_number(value, label):
    if isinstance(value, bool) or not isinstance(value, Real) or not isfinite(float(value)):
        raise ValueError(f"{label} must be a finite real number")
    return float(value)


def audit_partitions(train_ids, calibration_ids, evaluation_ids):
    """Check uniqueness/disjointness of observation IDs in three held-out sets.

    IDs are observation IDs, not proofs of entity, temporal or feature independence.
    """
    parts = {}
    for name, values in (
        ("train", train_ids),
        ("calibration", calibration_ids),
        ("evaluation", evaluation_ids),
    ):
        values = list(values)
        if not values or any(not isinstance(x, str) or not x.strip() for x in values):
            raise ValueError(f"{name} must contain non-empty string observation IDs")
        items = set(values)
        if len(items) != len(values):
            raise ValueError(f"{name} has repeated observation IDs")
        parts[name] = items
    if (parts["train"] & parts["calibration"] or
        parts["train"] & parts["evaluation"] or
        parts["calibration"] & parts["evaluation"]):
        raise ValueError("Train, calibration and evaluation IDs must be disjoint")
    return {name + "_rows": len(items) for name, items in parts.items()}


def split_conformal_radius(absolute_residuals, *, alpha=0.1):
    """Finite-sample split-conformal absolute-residual radius for exchangeable data.

    k = ceil((n+1)*(1-alpha)), using the k-th *smallest* score (1-indexed).
    If k>n, the finite quantile is +infinity. Fail closed rather than
    silently issuing an unbounded interval or an unsupported finite claim.
    """
    alpha = _finite_number(alpha, "alpha")
    if not 0.0 < alpha < 1.0:
        raise ValueError("alpha must be strictly between zero and one")
    scores = [_finite_number(x, "absolute residual") for x in absolute_residuals]
    if not scores:
        raise ValueError("At least one calibration residual is required")
    if any(score < 0 for score in scores):
        raise ValueError("Absolute residuals must not be negative")
    n = len(scores)
    k = ceil((n + 1) * (1 - alpha))
    if k > n:
        raise ValueError("Calibration set too small for finite split-conformal radius")
    return {"calibration_count": n, "rank": k, "alpha": alpha,
            "radius": sorted(scores)[k - 1]}


def regression_interval_report(y_true, y_pred, *, radius):
    """Descriptive empirical coverage on a separately reserved evaluation set."""
    radius = _finite_number(radius, "radius")
    if radius < 0:
        raise ValueError("radius must not be negative")
    truth = [_finite_number(x, "observed target") for x in y_true]
    pred = [_finite_number(x, "prediction") for x in y_pred]
    if not truth or len(truth) != len(pred):
        raise ValueError("Target and prediction arrays must have equal nonzero length")
    covered = sum(abs(actual - forecast) <= radius for actual, forecast in zip(truth, pred))
    return {"evaluation_count": len(truth), "covered": covered,
            "empirical_coverage": covered / len(truth), "interval_width": 2 * radius}


def binary_probability_report(labels, probabilities, *, bins=10, min_bin_size=5):
    """Descriptive Brier and fixed-bin reliability on untouched evaluation data.

    Brier score combines calibration, discrimination and uncertainty. Neither
    Brier nor a binned reliability table establishes perfect calibration.
    """
    if isinstance(bins, bool) or not isinstance(bins, Integral) or bins < 2:
        raise ValueError("bins must be an integer >= 2")
    if isinstance(min_bin_size, bool) or not isinstance(min_bin_size, Integral) or min_bin_size < 1:
        raise ValueError("min_bin_size must be a positive integer")
    labels = list(labels)
    probabilities = list(probabilities)
    if not labels or len(labels) != len(probabilities):
        raise ValueError("Labels and probabilities must have equal nonzero length")
    if any(isinstance(x, bool) or not isinstance(x, Integral) or x not in (0, 1) for x in labels):
        raise ValueError("Binary labels must be integers 0 or 1")
    probs = [_finite_number(x, "predicted probability") for x in probabilities]
    if any(p < 0 or p > 1 for p in probs):
        raise ValueError("Predicted probabilities must be between zero and one")
    counts = [0] * bins
    sum_probs = [0.0] * bins
    sum_labels = [0] * bins
    for y, p in zip(labels, probs):
        position = min(bins - 1, int(p * bins))
        counts[position] += 1
        sum_probs[position] += p
        sum_labels[position] += int(y)
    reliability = [
        {"bin": i, "count": counts[i],
         "mean_probability": sum_probs[i] / counts[i] if counts[i] >= min_bin_size else None,
         "event_rate": sum_labels[i] / counts[i] if counts[i] >= min_bin_size else None}
        for i in range(bins)
    ]
    return {"evaluation_count": len(labels),
            "brier_score": sum((p - y) ** 2 for p, y in zip(probs, labels)) / len(labels),
            "prevalence": sum(labels) / len(labels), "reliability": reliability,
            "min_bin_size": int(min_bin_size)}
