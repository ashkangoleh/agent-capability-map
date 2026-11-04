---
name: ds-probabilistic-forecasting
description: "Validate forecast quantiles and predictive distributions with horizon-specific pinball loss, crossing, calibration, support and distribution-shift safeguards."
metadata:
  version: "1.1.0"
---

# ds-probabilistic-forecasting

## Activation boundary

Use for forecasting **conditional distributions or quantiles by future horizon** where business cost depends on uncertainty. A point forecast plus an arbitrary percentage band is not a calibrated prediction interval. Use `ds-conformal-prediction-uncertainty` for exchangeability-dependent split-conformal guarantees, `ds-hierarchical-forecasting` for joint hierarchical coherence, and `ds-intermittent-demand-forecasting` for sparse-demand lifecycle decisions.

## Required context

Target and support (nonnegative, count, bounded or continuous); forecast origin and horizons; quantile levels/interval mass; decision cost and tail risk; calibration/evaluation windows; seasonality, entity and event segments; availability/shift assumptions; runtime versions and group sample sizes.

## Production workflow

1. Specify a predictive target, valid support and **each horizon**. Quantiles describe predictive distribution tails; quantile interval mass `q_high-q_low` is a target mass, not an empirical or conditional coverage guarantee.
2. Use rolling-origin windows and an honest out-of-sample holdout with the information actually available at origin; never calibrate intervals on all-series in-sample residuals and reuse those same outcomes as independent tests.
3. Choose a release-supported quantile/parametric/ensemble/simulation/conformal forecasting method. Record forecast origin, model version, quantile levels and covariate scenarios, especially uncertainty in future covariates.
4. Validate **quantile monotonicity on every observation and horizon** (`q_0.1 <= q_0.5 <= q_0.9`). Do not silently sort crossing predictions into apparently valid outputs; correct the model/reconciliation method and revalidate.
5. Measure **pinball loss** separately by quantile and horizon, empirical interval coverage and mean width; use CRPS or log score only for methods providing the relevant distribution, with assumptions and implementation version recorded. Mean pinball at `q=0.5` is half MAE for the same predictions.
6. Check calibration/sharpness together and distribution support: zero inflation, bounded/count outputs, tail events, holiday spikes and subgroup sample sizes. Avoid clipping negative forecasts without evaluating the induced distribution and bias.
7. Under shift, recalibrate and report degraded empirical reliability explicitly. IID conformal marginal coverage is **not automatically valid** under temporal dependence, even if nominal coverage happened to hold historically.
8. For hierarchies, point forecasts adding correctly does **not** imply coherent joint predictive distributions; validate sample/pathwise or probabilistic reconciliation separately.
9. Publish version-pinned model, origin/horizon metrics, scenario assumptions, monitoring thresholds and a baseline fallback/retrain policy. Use decision cost rather than narrowest interval as the default objective.

## Runnable arithmetic and scope

```python
from examples.data_science.forecast_integrity import quantile_forecast_report

out = quantile_forecast_report([0, 10], {0.1: [-2, 8], 0.9: [2, 12]})
assert out["empirical_interval_coverage"] == 1.0
assert out["nominal_interval_mass"] == 0.8
```

This is arithmetic on supplied **already held-out** observations. It does not fit a probabilistic model, check independence or guarantee nominal coverage. Test quantile crossing and numerical overflow with `python -m unittest discover -s tests -p 'test_data_science_forecast_integrity.py' -v`.

## Failure modes and abstention

- Crossing quantiles, missing horizons or invalid probability levels → fail rather than silently rearrange scores.
- Short calibration sample, drift, autocorrelation or changed covariate distribution → report nominal guarantee as unsupported.
- Sparse counts or inventory stockouts → use zero-demand and availability controls, not a continuous Gaussian forecast by default.
- Aggregate marginal interval coverage hiding undercoverage at important horizons/segments → report each segment separately and treat tiny groups as uncertain.

## Validation and evidence

- [ ] Origin/horizon, target support, quantile semantics and data lineage identified.
- [ ] No quantile crossing; proper scores and empirical coverage reported by horizon.
- [ ] Probabilistic/marginal assumptions distinguished from conditional guarantees.
- [ ] Tail, shift, subgroup and decision-cost diagnostics documented.
- [ ] Runtime version, model comparison and rollback/fallback supported by evidence.

## Output contract

Return supported quantile/distribution contract, per-horizon proper scores, coverage/width, support and crossing checks, uncertainty and operational cost, assumptions and fallback. No fabricated confidence, coverage guarantees or model results.

## Official references

- https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_pinball_loss.html
- https://otexts.com/fpp3/
- https://nixtla.github.io/statsforecast/docs/tutorials/crossvalidation.html
