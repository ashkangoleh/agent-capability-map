---
name: ds-hierarchical-forecasting
description: "Forecast hierarchical time series and reconcile product, geography and aggregate levels."
metadata:
  version: "1.0.0"
---

# ds-hierarchical-forecasting

## Activation boundary
Forecast hierarchical time series and reconcile product, geography and aggregate levels.

## Required context
Hierarchy, horizon, base models, aggregation constraints and rolling backtest.

## Analysis procedure
1. Define forecast origin, horizon, hierarchy and business loss.
2. Use rolling-origin backtests and prevent future leakage.
3. Compare seasonal baselines with candidate models.
4. Reconcile forecasts and evaluate by level and horizon.
5. Quantify uncertainty, drift and bias.

## Failure modes and safeguards
- Do not infer causality from predictive association or treat a p-value as effect size.
- Protect temporal/group boundaries, label availability, sampling design and multiplicity assumptions.
- Report uncertainty, sensitivity, calibration and population limitations; do not fabricate performance.

## Validation
- Reproduce from a clean environment and immutable data/split definitions.
- Test leakage, missingness, subgroup stability, sensitivity and generalization.
- Record library versions, seeds, assumptions, metrics and limitations.

## Official reference
- https://otexts.com/fpp3/

## Output contract
Return the analysis/modeling result with estimand, assumptions, validation design, uncertainty, reproducibility and decision implications. Separate observed evidence from inference.
