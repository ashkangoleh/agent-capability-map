"""Dependency-free numerical validation guards, not a statistical inference engine.

Use a design-aware library for survey variance, clustered bootstrap, MI degrees
of freedom, and model estimation. Do not promote diagnostics into guarantees.
"""

from math import fsum, isfinite, sqrt
from numbers import Real


def _number(value, name):
    if isinstance(value, bool) or not isinstance(value, Real):
        raise ValueError(f"{name} must be finite")
    try:
        result = float(value)
    except (OverflowError, ValueError, TypeError) as exc:
        raise ValueError(f"{name} must be finite") from exc
    if not isfinite(result):
        raise ValueError(f"{name} must be finite")
    return result


def adjust_pvalues(pvalues, *, method="holm", alpha=0.05):
    """Bonferroni, Holm (FWER), BH/BY (FDR); original input order preserved.

    The caller must define the complete hypothesis family and validate the
    applicable dependence/stopping assumptions before interpreting results.
    """
    alpha = _number(alpha, "alpha")
    if not 0 < alpha < 1:
        raise ValueError("alpha must be in (0, 1)")
    if method not in {"bonferroni", "holm", "fdr_bh", "fdr_by"}:
        raise ValueError("Unsupported multiple-testing method")
    values = [_number(p, "p-value") for p in pvalues]
    if not values or any(p < 0 or p > 1 for p in values):
        raise ValueError("p-values must be nonempty and in [0, 1]")
    n = len(values)
    order = sorted(range(n), key=lambda i: (values[i], i))
    ordered = [values[i] for i in order]
    if method == "bonferroni":
        adjusted = [min(1.0, p * n) for p in ordered]
    elif method == "holm":
        adjusted = []
        running = 0.0
        for i, p in enumerate(ordered):
            running = max(running, min(1.0, (n - i) * p))
            adjusted.append(running)
    else:
        factor = fsum(1.0 / k for k in range(1, n + 1)) if method == "fdr_by" else 1.0
        adjusted = [0.0] * n
        running = 1.0
        for i in range(n - 1, -1, -1):
            running = min(running, ordered[i] * n * factor / (i + 1))
            adjusted[i] = running
    restored = [0.0] * n
    for idx, value in zip(order, adjusted):
        restored[idx] = value
    return {
        "method": method,
        "alpha": alpha,
        "hypotheses": n,
        "adjusted_pvalues": restored,
        "reject": [p <= alpha for p in restored],
    }


def survey_design_guard(values, weights, *, strata, psus):
    """Validate one-stage design structure and compute descriptive weighted mean.

    The returned Kish weight effective size is NOT a design-based variance
    or a substitute for PSU/stratum-aware uncertainty. Reject lonely PSUs.
    """
    values = [_number(x, "survey value") for x in values]
    weights = [_number(x, "survey weight") for x in weights]
    strata, psus = list(strata), list(psus)
    n = len(values)
    if not n or any(len(x) != n for x in (weights, strata, psus)):
        raise ValueError("Survey arrays must have equal nonzero lengths")
    if any(w <= 0 for w in weights):
        raise ValueError("Survey weights must be strictly positive")
    for ids, name in ((strata, "strata"), (psus, "PSU")):
        if any(not isinstance(x, str) or not x.strip() for x in ids):
            raise ValueError(f"{name} must contain nonempty string IDs")
    design = {}
    for stratum, psu in zip(strata, psus):
        design.setdefault(stratum, set()).add(psu)
    if any(len(group) < 2 for group in design.values()):
        raise ValueError("Lonely PSU stratum: variance requires a documented design-specific rule")
    total = fsum(weights)
    weighted_sum = fsum(w * x for w, x in zip(weights, values))
    squared = fsum(w * w for w in weights)
    if not all(isfinite(x) for x in (total, weighted_sum, squared)) or total <= 0 or squared <= 0:
        raise ValueError("Weighted calculation overflow")
    return {
        "records": n,
        "strata": len(design),
        "psus": sum(len(x) for x in design.values()),
        "weighted_mean_descriptive": weighted_sum / total,
        "kish_weight_effective_n_descriptive": (total * total) / squared,
        "design_based_standard_error": None,
    }


def pool_scalar_imputations(estimates, within_variances):
    """Rubin scalar pooling variance; CI/df and imputation model are out of scope.

    Pool model estimates, NOT pooled rows. Within variances must be calculated
    separately for each properly imputed dataset with its analysis design.
    """
    means = [_number(x, "estimate") for x in estimates]
    within = [_number(x, "within variance") for x in within_variances]
    m = len(means)
    if m < 2 or len(within) != m or any(v < 0 for v in within):
        raise ValueError("Need >=2 estimates with matched nonnegative within variances")
    try:
        qbar = fsum(means) / m
        wbar = fsum(within) / m
        b = fsum((q - qbar) ** 2 for q in means) / (m - 1)
        total = wbar + (1 + 1 / m) * b
    except OverflowError as exc:
        raise ValueError("Imputation pooling overflow") from exc
    if not all(isfinite(x) for x in (qbar, wbar, b, total)) or total < 0:
        raise ValueError("Imputation pooling overflow")
    return {
        "imputations": m,
        "pooled_estimate": qbar,
        "within_variance": wbar,
        "between_variance": b,
        "total_variance": total,
        "pooled_standard_error": sqrt(total),
        "confidence_interval": None,
    }
