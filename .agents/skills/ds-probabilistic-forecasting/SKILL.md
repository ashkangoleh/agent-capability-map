---
name: ds-probabilistic-forecasting
description: Use when forecasting predictive distributions, quantiles, prediction intervals, or uncertainty across multiple time-series horizons.
metadata:
  version: "1.0.0"
---

# ds-probabilistic-forecasting

## Activation boundary

Use when decisions depend on uncertainty, tail risk, service levels or quantiles rather than only a point forecast. Use ds-intermittent-demand-forecasting for sparse demand with many zero periods.

## Required context

Series grain, frequency, horizon, forecast origin, target distribution, covariate availability, seasonality, hierarchy, decision loss and interval/quantile requirements.

## Workflow

1. Define the predictive target and horizon. Specify whether decisions use quantiles, intervals, full distributions, exceedance probabilities or scenario paths.
2. Establish seasonal-naive and simple statistical baselines. Use rolling-origin backtests with the same information available at each forecast origin.
3. Select a distributional strategy: parametric predictive distributions, quantile regression, model ensembles, simulation or conformalized intervals. State the assumptions and what uncertainty sources are represented.
4. Evaluate with proper scoring rules aligned to the target: pinball loss for quantiles, CRPS or log score for distributions, and coverage/width for intervals.
5. Check calibration by horizon, series segment, season, geography and target range. Inspect sharpness only alongside calibration.
6. Handle non-negative, count, bounded and zero-inflated outcomes with appropriate support. Do not clip negative forecasts without quantifying the resulting bias.
7. Reconcile probabilistic forecasts across hierarchies when aggregation constraints matter; point reconciliation alone does not define coherent joint uncertainty.
8. Evaluate covariate uncertainty, scenario assumptions, structural breaks and distribution shift. Distinguish parameter uncertainty from irreducible process variation.
9. Report forecast distributions, quantiles, calibration, proper scores, horizon degradation and decision implications.

## Failure modes and abstention

- Do not call a point forecast plus an arbitrary percentage band a prediction interval.
- Do not use in-sample residuals as if they were independent future errors.
- Do not compare quantile forecasts using only point-error metrics.
- Do not claim conditional coverage from a marginal guarantee.
- If the calibration window is unrepresentative or regime shift is severe, report degraded reliability.

## Validation checklist

- [ ] Forecast origin and information set are explicit.
- [ ] Backtesting is rolling-origin and leakage-safe.
- [ ] Proper probabilistic scores and calibration are reported.
- [ ] Coverage and sharpness are evaluated by horizon and subgroup.
- [ ] Distribution support and hierarchy constraints are checked.

## Authoritative references

- https://nixtlaverse.nixtla.io/statsforecast/
- https://scikit-learn.org/stable/modules/calibration.html
