---
name: ds-panel-econometrics
description: Use when estimating panel-data relationships with fixed or random effects, clustered inference, event studies, or staggered treatment adoption.
metadata:
  version: "1.0.0"
---

# ds-panel-econometrics

## Activation boundary

Use for repeated observations over entities and time where unobserved heterogeneity, serial correlation or treatment timing affect inference. Do not confuse a panel dataset with an ordinary repeated-row regression.

## Required context

Entity/time keys, balancedness, outcome, treatment timing, covariates, panel dimensions, missing periods, assignment level and target estimand.

## Workflow

1. Validate one row per entity-period, time frequency, duplicate keys, gaps, entry/exit, changing identifiers and treatment timing.
2. Define the estimand and variation used for identification: within-entity, between-entity, within-time or treatment-timing variation.
3. Compare pooled, entity fixed-effects, time fixed-effects, two-way fixed-effects and random-effects structures. State the assumptions required for each; do not choose random effects solely for efficiency.
4. Check serial correlation, cross-sectional dependence, heteroskedasticity, few clusters, unit roots and common shocks where relevant.
5. Cluster standard errors at the assignment/dependence level. With few clusters, use an appropriate small-sample or randomization-based method rather than trusting asymptotic cluster-robust errors.
6. For difference-in-differences, inspect treatment timing, anticipation, pre-trends, composition changes and treatment-effect heterogeneity. Avoid naive two-way fixed-effects interpretation under staggered adoption without checking its estimand and weighting.
7. For event studies, define the omitted period, event-time window, cohort composition and simultaneous confidence intervals. Treat pre-trend tests as diagnostics, not proof of parallel trends.
8. Run placebo dates/outcomes, alternative windows, balanced/unbalanced panel sensitivity and leave-one-cluster-out checks.
9. Report coefficient interpretation, fixed effects, standard-error structure, panel counts, missingness and identification limitations.

## Failure modes and abstention

- Do not use ordinary IID standard errors for serially correlated panels.
- Do not interpret entity fixed effects as controlling for time-varying confounding.
- Do not assume parallel trends because a pre-trend test is non-significant.
- Do not report a single two-way fixed-effects coefficient as a homogeneous ATT under arbitrary staggered adoption.
- If the assignment level or treatment timing is unclear, do not claim causal identification.

## Validation checklist

- [ ] Entity-period grain and panel structure are validated.
- [ ] Estimand and source of identifying variation are explicit.
- [ ] Standard errors respect serial/cluster dependence.
- [ ] Staggered adoption and event-study assumptions are checked.
- [ ] Placebo and sensitivity analyses are reported.

## Authoritative references

- https://docs.doubleml.org/stable/guide/models.html
- https://bashtage.github.io/linearmodels/
