---
name: ds-ab-experimentation
description: Use when designing or analyzing randomized A/B experiments with primary metrics, guardrails, randomization checks, and treatment-effect inference.
metadata:
  version: "1.1.0"
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
