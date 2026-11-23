---
name: time-series-forecast-backtesting
description: "Design and audit rolling-origin forecasting with horizon-specific backtests, delayed labels, origin-time covariates and operational leakage safeguards."
metadata:
  version: "1.1.1"
---

# time-series-forecast-backtesting

## Activation boundary

Use when a user needs a defensible **time-series evaluation design**, especially rolling/expanding origins, evaluation horizon, training window and data-latency contracts. Point forecasting is not identical to probabilistic interval validation; use `ds-probabilistic-forecasting` for quantile/distribution metrics, `ds-hierarchical-forecasting` for reconciliation and `ds-intermittent-demand-forecasting` for sparse demand/inventory objectives. Do not use random train/test shuffling for future forecasting.

## Required context

Series IDs and observation grain; timezone/calendar and actual sampling regularity; decision origin, horizon, step, retraining cadence, max history, forecast cutoff, delayed target/feature availability; release timestamp for future exogenous inputs; seasonality, hierarchy, missingness, censored demand, costs, SLO and expected structural drift.

## Production workflow

1. Define the `origin_at` decision timestamp and information set for **each** backtest. An observed value is not automatically available when measured; use label-materialization and feature-publication timestamps. For weather/promotions, distinguish planned values known at origin from realized values collected later.
2. Choose expanding versus fixed-width rolling windows, `initial_window`, `h`, `step_size`, `n_windows` and `refit` schedule. Hold out an untouched future period after model selection. The `step_size` between origins can be less than the horizon; then evaluation windows overlap and their errors are not independent.
3. Validate monotonically increasing, deduplicated timestamps **per series**, expected regularity, timezones/DST, missing periods and late/corrected labels before applying a splitter. Unevenly spaced observations are **not** made equal-duration by an index-based `gap`.
4. Fit scalers, imputers, transformations, lag features, model selection and intervals **inside the available training window at each origin**. An exogenous variable for a future timestamp is allowed only if its forecast/planned value was truly published before `origin_at`; actual future observations are leakage.
5. Compare last-value, seasonal-naive and task-specific robust baselines. Preserve a horizon-dependent metric panel (e.g. MAE/RMSE, MASE if its scaling denominator is meaningful, cost and service level); avoid MAPE on zero-heavy or signed values.
6. Measure per-horizon, per-season, per-series-volume and event/holiday failure modes. Account for bias and drift; compare refit frequencies and model compute cost. Distinguish training residuals from **out-of-sample** rolling-origin errors.
7. Pin runtime versions and document the actual cross-validation API. StatsForecast accepts `h`, `step_size` and `n_windows`, returning a `cutoff` column; verify exact installed release. In scikit-learn, `TimeSeriesSplit(gap)` is an observation count, **not a calendar-duration embargo**, and equal spacing is assumed for fold-duration comparability.
8. Define readiness gates: alert on stale labels/features, missing forecast batches, over-budget latency, horizon degradation and invalid assumptions; fall back to a measured seasonal baseline with an auditable rollback rather than silently publishing unsupported accuracy.

## Runnable split and availability checks

`examples/data_science/forecast_integrity.py` is a dependency-free, **single-series** precondition check, not a model trainer or benchmark:

```python
from examples.data_science.forecast_integrity import rolling_origin_splits

folds = rolling_origin_splits(12, min_train_size=5, horizon=2, step=2, gap=1)
assert [f["evaluation"] for f in folds] == [(6, 8), (8, 10), (10, 12)]
```

Use `audit_forecast_availability` with actual timezone-aware publication timestamps for each origin. Index-based folds cannot establish real-time latency, feature lineage, stationarity, calendar-aware embargoes or cross-series independence.

## Failure modes and abstention

- Last training label or a future exogenous value not yet published at `origin_at` → reject that fold; reconstruct as-of inputs.
- Duplicate or irregular timestamps → validate per-series calendar; use an explicit calendar-aware splitter rather than assuming a fixed index gap.
- Zero-heavy demand, missing vs stockout-censored observations → route to intermittent-demand quality gates.
- Changing hierarchy, retraining/selection over test windows, missing classes or data drift → rebuild the backtest and record selection/lineage.
- Inadequate history for seasonal baseline or requested forecast horizon → report unsupported/no evaluation; never invent benchmark performance.

## Validation and evidence

- [ ] Origins, horizon and step, refit cadence and forecast train/test boundaries recorded.
- [ ] All training targets and future covariates available at their claimed origins.
- [ ] Baseline and candidate models evaluated on identical origin/horizon sets.
- [ ] Horizon-specific out-of-sample metrics, uncertainty and error dependence reported.
- [ ] Version, seasonality assumptions, anomalies, monitoring and fallback recorded.

## Output contract

Return a reproducible origin/horizon plan, data-availability proof, fold evidence, baselines, per-horizon metrics, operational costs, failure modes, drift detection and deployment/rollback decision. Never treat a generated index split as a trained model.

## Official and primary references

- https://otexts.com/fpp3/tscv.html
- https://nixtla.github.io/statsforecast/docs/tutorials/crossvalidation.html
- https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html

## Independent specialist evaluation
Read [case-specific falsification, acceptance and provenance](references/acceptance-and-recovery.md) on demand for production-impacting or high-stakes work. Unexecuted tests and unsupported claims remain unverified; this reference cannot authorize actions.
