---
name: ds-conformal-prediction-uncertainty
description: Use when constructing distribution-free prediction intervals, prediction sets, or risk-controlled decisions with conformal methods.
metadata:
  version: "1.0.0"
---

# ds-conformal-prediction-uncertainty

## Activation boundary

Use for predictive uncertainty around regression values or classification labels. Do not confuse conformal prediction intervals with confidence intervals for parameters or Bayesian credible intervals.

## Required context

Base model, target, calibration population, exchangeability unit, time/group structure, desired marginal coverage, subgroup risks and decision costs.

## Workflow

1. Define the prediction target and coverage level. Decide whether the required guarantee is marginal, group-conditional, class-conditional, time-conditional or risk-based.
2. Split data into training, calibration and final evaluation partitions before fitting or selecting the base model. Keep the calibration labels unavailable to model fitting and tuning.
3. Choose a conformal method appropriate to the data structure: split conformal for a simple holdout, cross-validation/jackknife variants when data efficiency is important, and time/group-aware methods when IID exchangeability is not credible.
4. Select a nonconformity score aligned to the task. For regression, assess residual scaling and heteroskedasticity; for classification, assess score and class imbalance effects.
5. Estimate the finite-sample calibration quantile using the correct order-statistic correction. Do not substitute an ordinary empirical quantile without checking the method's finite-sample rule.
6. Evaluate empirical coverage, interval width or prediction-set size on untouched data. Report coverage by time, class, geography and important subgroups.
7. Test sensitivity to distribution shift and exchangeability violations. Use adaptive or weighted methods only when their assumptions and guarantees are understood.
8. Record model version, calibration window, data split, score definition, nominal coverage and observed coverage.

## Decision rules

- Standard split conformal provides marginal coverage under exchangeability; it does not guarantee exact conditional coverage for every subgroup.
- Temporal dependence, covariate shift and concept drift can invalidate standard guarantees.
- Narrow intervals are not useful if coverage is materially below target.
- Risk-control guarantees are metric- and procedure-specific.

## Failure modes and abstention

- Do not calibrate on training data used to fit the base model.
- Do not tune the method repeatedly on the final evaluation set.
- Do not claim individual-level or subgroup guarantees from marginal coverage.
- If exchangeability is implausible and no justified adaptation is available, report empirical uncertainty without a formal guarantee.

## Validation checklist

- [ ] Calibration data are separate from model fitting and tuning.
- [ ] Exchangeability assumptions match the data.
- [ ] Finite-sample quantile correction is respected.
- [ ] Coverage and sharpness are measured on untouched data.
- [ ] Subgroup and temporal coverage are reported.

## Authoritative references

- https://mapie.readthedocs.io/en/stable/index.html
- https://github.com/scikit-learn-contrib/MAPIE
