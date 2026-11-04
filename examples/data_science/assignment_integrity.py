"""Read-only, two-arm assignment-level sample-ratio diagnostic.

The diagnostic does not estimate treatment effects or prove randomization quality.
"""

from collections import Counter
from math import erfc, isclose, isfinite, sqrt
from typing import Iterable, Mapping


def audit_assignment_ratio(
    assignments: Iterable[tuple[str, str]],
    expected_allocation: Mapping[str, float],
    *,
    alpha: float = 0.001,
    minimum_expected_per_arm: float = 5.0,
) -> dict:
    """Count unique randomized units and flag large two-arm allocation deviations.

    Use an assignment log, not exposure/conversion/metric records. The chi-square
    p-value uses the asymptotic df=1 survival function and is only returned when
    each expected count meets the declared threshold. SRM is diagnostic only.
    """
    if len(expected_allocation) != 2:
        raise ValueError("Exactly two randomized arms are supported")
    arms = tuple(expected_allocation)
    if any(not isinstance(arm, str) or not arm.strip() for arm in arms):
        raise ValueError("Arm names must be non-empty strings")
    allocation = tuple(expected_allocation[arm] for arm in arms)
    if any(isinstance(x, bool) or not isinstance(x, (int, float)) or
           not isfinite(x) or x <= 0 or x >= 1 for x in allocation):
        raise ValueError("Expected allocations must be finite probabilities in (0,1)")
    if not isclose(sum(allocation), 1.0, rel_tol=0.0, abs_tol=1e-12):
        raise ValueError("Expected allocations must sum to one")
    if isinstance(alpha, bool) or not isinstance(alpha, (int, float)) or not isfinite(alpha) or not 0 < alpha < 1:
        raise ValueError("alpha must be a finite probability in (0,1)")
    if isinstance(minimum_expected_per_arm, bool) or not isinstance(minimum_expected_per_arm, (int, float)) or not isfinite(minimum_expected_per_arm) or minimum_expected_per_arm < 5:
        raise ValueError("minimum_expected_per_arm must be finite and at least 5")
    units: dict[str, str] = {}
    duplicates = 0
    for item in assignments:
        if not isinstance(item, (tuple, list)) or len(item) != 2:
            raise ValueError("Each assignment must be a (unit_id, arm) pair")
        unit, arm = item
        if not isinstance(unit, str) or not unit.strip():
            raise ValueError("Randomization unit IDs must be non-empty strings")
        if arm not in expected_allocation:
            raise ValueError("Assignment contains an unknown arm")
        if unit in units:
            if units[unit] != arm:
                raise ValueError("Conflicting assignments for one randomization unit")
            duplicates += 1
        else:
            units[unit] = arm
    observed = Counter(units.values())
    n = len(units)
    expected_counts = {arm: n * weight for arm, weight in zip(arms, allocation)}
    result = {
        "total_randomized_units": n,
        "duplicate_assignment_events": duplicates,
        "observed_counts": {arm: observed[arm] for arm in arms},
        "expected_counts": expected_counts,
        "alpha": float(alpha),
        "status": "insufficient_expected_count",
        "chi_square": None,
        "approx_p_value": None,
    }
    if min(expected_counts.values()) < minimum_expected_per_arm:
        return result
    chi_sq = sum((observed[arm] - expected_counts[arm]) ** 2 / expected_counts[arm] for arm in arms)
    p_value = erfc(sqrt(chi_sq / 2.0))
    result.update({
        "chi_square": chi_sq,
        "approx_p_value": p_value,
        "status": "investigate_srm" if p_value < alpha else "no_srm_alarm_detected",
    })
    return result
