---
name: ds-ab-experimentation
description: Use when designing or analyzing randomized A/B experiments with primary metrics, guardrails, randomization checks, and treatment-effect inference.
metadata:
  version: "1.2.0"
---

# ds-ab-experimentation

## Activation boundary

Use for randomized product, pricing, UX, marketing or operational experiments. Use ds-sequential-experimentation when monitoring or stopping rules permit repeated looks or adaptive allocation.

## Required context

- Hypothesis, primary estimand, primary metric and guardrail metrics.
- Randomization unit, eligibility, assignment and exposure timestamps.
- Baseline rate/variance, expected effect, alpha, power, allocation ratio and planned duration.
- Clustering, repeated users, network interference, seasonality and experiment overlap.

## Workflow

1. Pre-register the hypothesis, primary outcome, guardrails, eligibility, randomization unit, analysis population and stopping rule.
2. Verify randomization before reading outcome effects. Check sample-ratio mismatch overall and by key strata, assignment/exposure parity, duplicate assignments, contamination and attrition.
3. Estimate power and minimum detectable effect using the actual randomization unit. Inflate for clustering, repeated measures, attrition and multiplicity when appropriate.
4. Use intent-to-treat as the primary estimate. Report treatment-on-treated or per-protocol estimates only as secondary analyses with explicit assumptions.
5. Choose an estimator aligned to the design: difference in means/proportions, regression adjustment, cluster-level analysis or randomization inference. Preserve assignment-unit dependence in uncertainty estimates.
6. Consider CUPED or pre-treatment covariate adjustment only with pre-treatment information. Validate variance reduction out of sample and never adjust for post-treatment mediators.
7. Report absolute and relative effects, confidence intervals, guardrails, segment heterogeneity and practical impact. Control multiplicity for multiple primary metrics or confirmatory segments.
8. Check novelty, seasonality, interference, experiment interaction and delayed outcomes before declaring a result durable.

## Assignment integrity, SRM and exposure diagnostics

1. Require a durable, **pre-outcome assignment event** keyed by the actual randomization unit. Count each assigned unit exactly once, not repeated exposure, impression, conversion or outcome rows. Deduplicate idempotent assignment events and **fail closed on one unit assigned to conflicting arms**.
2. Validate the intended allocation ratio, eligibility, experiment and assignment timestamp, identity stability, mutually exclusive buckets and stratification. Segment the check by relevant platform, geography and assignment epoch when the policy differs; do not pool incompatible allocation policies.
3. For an **independent two-arm assignment** use the executable diagnostic `examples/data_science/assignment_integrity.py` to compare observed unique randomized-unit counts against the predeclared allocation. Its Pearson chi-square p-value is a large-sample approximation (df=1); it only reports a value when **both expected counts are at least five**. An alert at the default `alpha=0.001` calls for investigation, not automatic rebalancing, deletion of observations or proof of bias.
4. Check assignment data and exposure/metric pipelines **separately**. Exposure-only ratios are subject to post-assignment selection and do not substitute for randomized allocation counts. Diagnose selective telemetry loss, client retries, bot filtering, time-window boundaries, sample eligibility drift and duplicated IDs.
5. Interpret assignment-ratio tests against the **actual allocation mechanism**: fixed-quota/block or adaptive randomization can require different null distributions or stratum-specific tests; do not apply a naive independent Bernoulli chi-square and present its p-value as valid.
6. If SRM/identity conflicts arise, freeze causal interpretation and investigate the source and eligibility/assignment records. Do not declare a trustworthy intent-to-treat effect until assignment and missingness assumptions are defensible. A non-alert does not prove randomization, absence of interference or unbiased outcomes.

### Executable assignment diagnostic

From the repository root, with Python 3.10+ and no external libraries:

```python
from examples.data_science.assignment_integrity import audit_assignment_ratio

events = [(f"user-{i}", "control" if i % 2 else "treatment") for i in range(100)]
result = audit_assignment_ratio(events, {"control": 0.5, "treatment": 0.5})
assert result["status"] == "no_srm_alarm_detected"
assert result["total_randomized_units"] == 100
```

Use this only for **two independent randomized arms**; it is a pre-analysis diagnostic, not an effect estimator. The input must come from assignment logs, not selected exposed users. For multi-arm, stratified, clustered, forced balance, sequential or adaptive designs, select and justify a design-appropriate test and uncertainty method. Reproduce the helper tests with `python -m unittest discover -s tests -p 'test_data_science_assignment_integrity.py' -v`.

## Decision rules

- A statistically significant result can still be operationally immaterial; compare effects with predeclared decision thresholds.
- A sample-ratio mismatch is a diagnostic alarm, not a metric to ignore or automatically repair.
- Repeated peeking invalidates fixed-horizon p-values unless the analysis uses a valid sequential procedure.
- Do not promote post-hoc subgroup findings to confirmatory claims.

## Failure modes and abstention

- Pause interpretation when assignment integrity or exposure logging is broken.
- Do not stop early because a nominal p-value crossed 0.05 unless the stopping rule supports it.
- Do not use user-level standard errors for cluster-randomized assignment without accounting for clusters.
- If the primary metric or analysis population changed after seeing results, label the analysis exploratory.

## Validation checklist

- [ ] Randomization and sample-ratio checks pass.
- [ ] Analysis follows the predeclared estimand and stopping rule.
- [ ] Uncertainty respects the randomization unit.
- [ ] Guardrails and multiplicity are addressed.
- [ ] Results include practical significance and reproducible cohort definitions.

## Authoritative references

- https://www.statsig.com/perspectives/ab-testing-statistics
- https://www.statsmodels.org/stable/stats.html
- https://exp-platform.com/Documents/2019_KDDFabijanGupchupFuptaOmhoverVermeerDmitriev.pdf
