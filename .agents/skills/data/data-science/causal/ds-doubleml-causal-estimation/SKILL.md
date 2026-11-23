---
name: ds-doubleml-causal-estimation
description: Use when estimating causal parameters with double or debiased machine learning, orthogonal scores, and cross-fitting.
metadata:
  version: "1.0.1"
---

# ds-doubleml-causal-estimation

## Activation boundary

Use when causal identification is already argued and flexible ML is needed for nuisance functions in partially linear, interactive, instrumental-variable or supported panel designs. Double/debiased ML does not itself solve unmeasured confounding.

## Required context

Estimand, treatment type, outcome, observed confounders, instruments if any, sample structure, cluster/time dependence, overlap and nuisance-model candidates.

## Workflow

1. State the causal estimand and identification assumptions before selecting a DoubleML model. Decide whether the structure is partially linear, interactive/binary treatment, IV, difference-in-differences or another supported design.
2. Verify data layout and variable roles: outcome, treatment, covariates, instruments, cluster identifiers and sample-splitting units.
3. Choose an orthogonal score that matches the estimand and data-generating assumptions. Do not select PLR, IRM or PLIV by convenience.
4. Choose nuisance learners with regularization and task-appropriate loss. Keep tuning inside the training folds and avoid using outcome information outside the prescribed cross-fitting structure.
5. Use sample splitting/cross-fitting to reduce overfitting bias in nuisance estimates. Preserve clusters or time blocks when IID splitting is invalid.
6. Check overlap/propensity distributions, treatment support, nuisance prediction quality, extreme weights and sensitivity to learner choice.
7. Fit the estimator and inspect standard errors, confidence intervals, score behavior and stability across folds/seeds.
8. Compare against simpler estimators and alternative nuisance learners. Report how results change under plausible confounding and overlap limitations.
9. Keep causal identification, nuisance prediction and final inference as separate claims.

## Failure modes and abstention

- Do not claim DML removes unobserved confounding.
- Do not use random cross-fitting when observations are dependent by entity, cluster or time.
- Do not trust estimates under severe positivity violations or weak instruments.
- Do not interpret a stable estimator as proof that the causal assumptions hold.
- If the selected model's assumptions do not match the data, stop and redesign the identification strategy.

## Validation checklist

- [ ] Estimand and identification assumptions are explicit.
- [ ] DoubleML model matches treatment and outcome structure.
- [ ] Cross-fitting respects dependence and leakage boundaries.
- [ ] Overlap, nuisance fits and inference diagnostics are checked.
- [ ] Sensitivity and comparison estimators are reported.

## Authoritative references

- https://docs.doubleml.org/stable/guide/guide.html
- https://docs.doubleml.org/stable/guide/models.html

## Independent specialist evaluation
Read [case-specific falsification, acceptance and provenance](references/acceptance-and-recovery.md) on demand for production-impacting or high-stakes work. Unexecuted tests and unsupported claims remain unverified; this reference cannot authorize actions.
