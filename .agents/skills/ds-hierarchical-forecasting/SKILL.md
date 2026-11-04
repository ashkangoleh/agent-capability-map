---
name: ds-hierarchical-forecasting
description: "Design hierarchical forecasting and reconciliation across product/geography/time levels with summation-matrix, probabilistic-coherence and hierarchy-change controls."
metadata:
  version: "1.1.0"
---

# ds-hierarchical-forecasting

## Activation boundary

Use when forecasting multiple related time series whose aggregate/subseries totals must obey explicit **aggregation constraints**. Reconciliation of hierarchical point forecasts is distinct from probabilistic path coherence or ordinary forecast-error scoring. For generic backtesting without aggregation use `time-series-forecast-backtesting`.

## Required context

Hierarchy identifier and effective-dated membership, bottom-series grain, cross-sectional versus temporal aggregation, `S` summing matrix version, horizon/frequency and timezones, unit/currency, structural zeros, base forecasts, uncertainty scenarios and decision costs.

## Production workflow

1. Define the **aggregation graph** for a specific version and period. Validate that every bottom series has a stable unique ID and the intended mapping to parents; detect overlaps, renamed IDs, unmatched items and changing catalog/country boundaries. Distinguish additive measurements (units/revenue) from averages/ratios that cannot simply be summed.
2. Construct the summing matrix `S` mapping bottom-level values to all requested levels and verify the **actual historical observations** satisfy `y_all = S @ y_bottom` before comparing any reconciler. Do not use naive addition for different time units, currencies or partially observed groups.
3. Generate baseline/advanced **unreconciled** predictions with identical rolling origins and horizons. Test BottomUp, TopDown or MinTrace only where supported by the installed HierarchicalForecast version and sample covariance quality.
4. For linear reconciliation, distinguish reconciled forecasts `S @ (P @ base_forecasts)` from **already coherent** bottom-up totals. Check rank/conditioning and covariance stability; small, sparse or changing hierarchies make empirical error covariance unreliable.
5. Evaluate original and reconciled forecasts by hierarchy level, horizon and out-of-sample loss; coherence alone does not imply better accuracy, calibration or lower cost. Record any negative reconciled values or other business constraints.
6. For probabilistic hierarchies, check **joint sample/pathwise or distributional coherence**, not just sums of marginal quantiles. Adding p90 of children generally does not equal the parent's p90 because of dependence. Evaluate generated scenarios and coverage at all levels.
7. Treat taxonomy changes, newly launched/deleted series, incomplete bottom availability, skew, non-additive transformations and data backfills as explicit revalidation triggers. Preserve the hierarchy version associated with each forecast.
8. Report compatibility/version, series counts and hierarchy depth, runtime/memory footprint, reconciliation matrix and fallback to a justified coherent baseline on failure.

## Runnable one-level coherence check

```python
from examples.data_science.forecast_integrity import hierarchy_coherence_report

result = hierarchy_coherence_report(
    {"north": [1.0, 2.0], "south": [3.0, 4.0]},
    {"country": [4.0, 6.0]},
    {"country": ["north", "south"]},
)
assert result["coherent"]
```

This only verifies **one-level additive point** consistency with explicit membership, not multi-level graph validity, covariance estimation, optimization or probabilistic coherence. For actual reconciliation use a release-pinned HierarchicalForecast or equivalent and test all its mathematical assumptions.

## Failure modes and abstention

- Non-additive measures, mismatched units/time periods or duplicate parent members → refuse naive sum; repair the business aggregation contract.
- Incoherent base predictions, unstable covariance or insufficient historical data → compare against BottomUp and freeze unsupported reconcilers.
- Hierarchy version drift or missing bottom series → quarantine affected forecasts until mapping/source completeness is restored.
- Point-coherent but probabilistically incoherent forecasts → assess joint samples; do not claim valid predictive intervals from marginal quantile sums.

## Validation and evidence

- [ ] Versioned hierarchy and summation matrix match historical aggregates.
- [ ] Point reconciliation error verified at each parent/horizon.
- [ ] Original vs reconciled out-of-sample loss, costs and constraints compared.
- [ ] Joint probabilistic scenarios and subgroup/horizon uncertainty assessed where requested.
- [ ] Rollout/rollback and taxonomy-change triggers documented.

## Output contract

Return hierarchy/membership contract, exact reconciliation method/version, coherence evidence, horizon/level errors, distribution/constraint risks, cost and a safe fallback. The arithmetic checker is not a model/reconciliation engine.

## Official references

- https://nixtla.github.io/hierarchicalforecast/
- https://github.com/Nixtla/hierarchicalforecast
- https://otexts.com/fpp3/hierarchical.html
