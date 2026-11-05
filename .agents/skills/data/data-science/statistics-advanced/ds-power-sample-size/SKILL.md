---
name: ds-power-sample-size
description: Use when calculating or simulating sample size, statistical power, minimum detectable effects, or experiment duration.
metadata:
  version: "1.1.1"
---

# ds-power-sample-size

## Activation boundary

Use before data collection or before interpreting an experiment's ability to detect a meaningful effect. Do not treat post-hoc observed power as evidence that a non-significant result is informative.

## Required context

Estimand, outcome type, baseline rate/variance, smallest worthwhile effect, alpha, target power, allocation ratio, randomization unit, expected attrition, multiplicity and analysis plan.

## Workflow

1. Define the primary estimand, analysis population, outcome scale and smallest effect that would change the decision.
2. Choose a test/estimator consistent with the design: continuous, binary, count, time-to-event, paired, clustered, repeated-measures or non-inferiority.
3. Specify type-I error, desired power, allocation ratio, one- or two-sided alternative and multiplicity adjustment before calculating sample size.
4. Estimate nuisance parameters from prior data or a blinded pilot. Use conservative variance and baseline-rate assumptions; document uncertainty.
5. For cluster randomization, account for intraclass correlation and unequal cluster sizes using a design effect or simulation. Count independent clusters, not only individuals.
6. Include attrition, noncompliance, delayed outcomes, repeated looks and unequal exposure. Do not inflate sample size by an arbitrary percentage without a stated mechanism.
7. Use analytical formulas for standard designs and simulation for complex metrics, non-Gaussian outcomes, adaptive designs or nonlinear estimators.
8. Run sensitivity grids over baseline rate, variance, effect size, ICC, allocation and attrition. Report the power curve and feasibility constraints.
9. Translate sample size into duration using eligible traffic, assignment unit, seasonality and exposure latency; avoid stopping at a calendar date before outcomes mature.

## Decision rules

- Power is conditional on the assumed effect, variance, design and analysis.
- A larger sample cannot repair biased assignment, poor measurement or invalid inference.
- For non-inferiority/equivalence, define the margin and direction explicitly; ordinary superiority power is not interchangeable.
- Do not use observed post-hoc power as a substitute for confidence intervals.

## Failure modes and abstention

- Do not compute power from an effect estimate selected because it looked promising.
- Do not ignore clustering, repeated users, multiplicity or sequential monitoring.
- If baseline variance or traffic assumptions are weak, provide a sensitivity range rather than a single precise number.

## Validation checklist

- [ ] Design, estimand and smallest worthwhile effect are explicit.
- [ ] Alpha, power and multiplicity policy are predeclared.
- [ ] Cluster/repeated-measure structure is included.
- [ ] Sensitivity analysis and duration feasibility are reported.
- [ ] Analysis plan matches the power calculation.

## Authoritative references

- https://www.statsmodels.org/stable/stats.html
- https://docs.scipy.org/doc/scipy/reference/stats.html

## Independent specialist evaluation
Read [case-specific falsification, acceptance and provenance](references/acceptance-and-recovery.md) on demand for production-impacting or high-stakes work. Unexecuted tests and unsupported claims remain unverified; this reference cannot authorize actions.
