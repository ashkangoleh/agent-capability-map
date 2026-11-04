---
name: ds-intermittent-demand-forecasting
description: Use when forecasting sparse, lumpy, or intermittent demand with many zero periods and irregular non-zero events.
metadata:
  version: "1.0.0"
---

# ds-intermittent-demand-forecasting

## Activation boundary

Use for spare parts, low-volume SKUs, infrequent events or other demand series with many zero periods. Do not apply intermittent-demand methods to missing or stockout-censored observations without first reconstructing the demand process.

## Required context

Item/location grain, time bucket, zero frequency, demand occurrence and size, stockout/censoring indicators, lead time, replenishment policy and service-level objective.

## Workflow

1. Distinguish true zero demand from stockout, assortment changes, inactive items, missing feeds and delayed data. Model demand only after this classification.
2. Profile average demand interval, non-zero size, coefficient of variation and series length. Segment intermittent, erratic, lumpy and smooth patterns as diagnostics, not immutable labels.
3. Establish simple baselines and compare Croston-family methods, SBA, TSB, ADIDA/IMAPA and suitable pooled or machine-learning approaches.
4. Separate occurrence probability from demand size when the business decision benefits from that decomposition. TSB-style updating may react differently to obsolescence than classical Croston.
5. Use rolling-origin evaluation and evaluate at the replenishment lead-time horizon. Preserve zero-heavy periods and avoid random splits.
6. Avoid MAPE and other unstable percentage metrics near zero. Compare scaled errors, bias, service-level attainment, stockout cost, excess inventory and quantile loss.
7. Evaluate aggregate performance and tail behavior by item age, location, demand class and lead time. Check cold-start and obsolescence separately.
8. Translate forecasts into inventory decisions with explicit review period, lead-time distribution, target service level and order constraints.
9. Monitor occurrence rate, size distribution, forecast bias, stockout censoring and item lifecycle; define fallback and retirement policies.

## Failure modes and abstention

- Do not interpret stockout sales as true zero demand.
- Do not select a model using aggregate error while ignoring stockout or holding costs.
- Do not forecast inactive/obsolete items as if their demand process were stationary.
- Do not claim probabilistic intervals from methods that return point forecasts only.
- If the observation process cannot distinguish zero demand from unavailable inventory, report the limitation before forecasting.

## Validation checklist

- [ ] True zero, stockout and missing feed are separated.
- [ ] Intermittency and lifecycle are profiled.
- [ ] Croston/SBA/TSB and simple baselines are compared where appropriate.
- [ ] Lead-time and inventory costs drive evaluation.
- [ ] Obsolescence, cold-start and drift are monitored.

## Authoritative references

- https://nixtlaverse.nixtla.io/statsforecast/
- https://github.com/Nixtla/statsforecast
