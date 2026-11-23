---
name: ds-intermittent-demand-forecasting
description: "Forecast intermittent demand with zero-versus-stockout-censoring checks, occurrence-size methods, lifecycle drift and lead-time inventory evaluation."
metadata:
  version: "1.1.1"
---

# ds-intermittent-demand-forecasting

## Activation boundary

Use for sparse/zero-heavy, lumpy or obsolete-able demand series such as slow-moving SKUs and infrequent events. Use **true demand**, not sales suppressed by a stockout or missing telemetry. Distinguish descriptive intermittency from an inventory decision and a calibrated lead-time demand distribution.

## Required context

Unique SKU/location, complete time buckets, inventory availability and stockout events, zero/nonzero demand and missing periods, assortment start/end, lead-time distribution, service-level target, nonnegative support, obsolescence risk, cost and observation release latency.

## Production workflow

1. Classify every time bucket: **observed true zero**, positive demand, **stockout-censored**, missing feed, inactive/discontinued product or unobserved prelaunch period. A zero sale during an outage is not a zero demand label. Reject contaminated periods until their observation mechanism is resolved.
2. Profile nonzero frequency, `ADI = number of eligible buckets / nonzero eligible buckets`, nonzero demand sizes, series history and lifecycle. All-zero series have undefined ADI and size, **not** automatic proof of permanent obsolescence. Document grouping threshold heuristics as descriptive, not immutable business classes.
3. Compare a credible simple baseline and Croston-family variants (Croston, bias-adjusted SBA, TSB) plus ADIDA/IMAPA when supported by the installed StatsForecast release. Croston-family outputs are not automatically probabilistic demand distributions.
4. For obsolescence, TSB-style methods separately update **demand occurrence probability every period** and demand size on positive periods; verify how changing occurrence probability and item retirement are reflected in the target version.
5. Forecast at the **replenishment decision origin** for the true lead-time/review horizon, with future lead-time uncertainty if relevant. Use rolling-origin windows with enough history, preserve zero-heavy evaluation periods and censoring indicators.
6. Avoid MAPE on zeros and choose meaningful scaled errors only where their denominators exist. Evaluate volume-weighted bias, lead-time cumulative demand, inventory holding/stockout costs and realized service level; do not optimize a smooth-series MAE alone.
7. Separate cold-start, assortment churn, replacements and phase-out items from stable intermittent demand. Prevent survivorship bias from dropping inactive/zero-heavy SKUs in backtests.
8. Validate `Croston/SBA/TSB` APIs and outputs against exact package release and actual data; record fallback on sparse history, missingness or stockout uncertainty, and monitor inventory service levels, demand-interval drift and obsolescence.

## Runnable contamination guard

```python
from examples.data_science.forecast_integrity import intermittent_demand_profile

profile = intermittent_demand_profile(
    [0, 0, 4, 0, 2, 0],
    statuses=["observed"] * 6,
)
assert profile["average_demand_interval"] == 3.0
```

The profiler rejects `stockout` or `missing` buckets rather than silently recoding them to zeros. It does **not** estimate counterfactual unconstrained demand or fit an intermittent forecasting model.

## Failure modes and abstention

- Unknown stockout history or missing observation state → decline a precise true-demand forecast until data provenance is reconciled.
- Very few nonzero periods or entirely zero history → mark unstable/undefined size and ADI; report cold-start or obsolescence uncertainty.
- Abrupt changes in occurrence rate or lifecycle → review model class/fallback; do not mechanically extrapolate past positive events.
- Inventory/safety stock chosen from point forecast only → require calibrated lead-time distribution or explicit conservative policy.

## Validation and evidence

- [ ] Zero, missing, stockout and lifecycle types reconciled.
- [ ] ADI/occurrence/size and valid SKU-horizon population recorded.
- [ ] Croston/SBA/TSB/version, baseline, forecast horizon and objective documented.
- [ ] Lead-time service-level/holding/stockout costs evaluated.
- [ ] Cold-start, obsolescence, shift and failure fallback demonstrated.

## Output contract

Return validated demand-observation contract, intermittency profile, version-aware model comparison, origin-aligned backtests, decision costs, uncertainty, lifecycle exceptions and rollout/rollback triggers. Unsupported zero/censoring assumptions must be explicit.

## Primary and official references

- https://nixtla.github.io/statsforecast/
- https://github.com/Nixtla/statsforecast
- https://help.sap.com/docs/SAP_HANA_PLATFORM/319d36de4fd64ac3afbf91b1fb3ce8de/croston-tsb-method-8203847.html

## Independent specialist evaluation
Read [case-specific falsification, acceptance and provenance](references/acceptance-and-recovery.md) on demand for production-impacting or high-stakes work. Unexecuted tests and unsupported claims remain unverified; this reference cannot authorize actions.
