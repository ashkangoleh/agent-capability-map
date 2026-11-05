---
name: ds-sequential-experimentation
description: Use when experiments are monitored repeatedly, stopped early, adapted, or analyzed with sequentially valid inference.
metadata:
  version: "1.1.1"
---

# ds-sequential-experimentation

## Activation boundary

Use when the experiment design permits interim looks, early stopping, adaptive allocation or continuous monitoring. For a single predeclared fixed-horizon analysis, use ds-ab-experimentation.

## Required context

Randomization unit, primary estimand, metric, guardrails, look schedule, stopping boundaries, allocation policy, expected duration, multiplicity and experiment ownership.

## Workflow

1. Decide whether the design is fixed-horizon or sequential before launch. Specify the monitoring cadence, maximum sample/duration and stopping rules.
2. Select a valid sequential procedure: group-sequential alpha spending, always-valid p-values/confidence sequences, mixture sequential probability ratio tests or another method with documented guarantees.
3. Distinguish interim monitoring from adaptive treatment assignment. Adaptive allocation changes the data-generating design and requires design-specific inference.
4. Predeclare efficacy, futility and safety boundaries. Define whether stopping can occur for primary outcomes, guardrails or operational failures.
5. Validate randomization and sample-ratio metrics at every look. Account for delayed outcomes, exposure maturation, repeated users and assignment clusters.
6. Use pre-treatment covariates for variance reduction only when the sequential method supports the adjustment. Keep post-treatment variables out of adjustment.
7. Report the stopping time, number of looks, boundary crossed, cumulative information, effect estimate and sequentially valid interval or p-value.
8. Simulate operating characteristics under null and plausible alternatives: type-I error, power, expected sample size, stopping probability and guardrail behavior.
9. Monitor implementation drift and ensure dashboards use the same sequential method as the final analysis.

## Interim-monitoring validity gate

1. Record whether the experiment was designed for fixed-horizon analysis, group-sequential looks or continuous monitoring **before observing outcomes**. A dashboard showing ordinary fixed-horizon p-values repeatedly is not a valid early-stopping rule.
2. For group-sequential procedures, specify information time/fractions, overall family-wise type-I error budget, look schedule, efficacy/futility boundaries and alpha-spending model. **An alpha-spending function is cumulative error allocation, not permission to use the same nominal p-value threshold at every look.** Boundary values depend on the joint distribution and design.
3. Distinguish always-valid p-values, confidence sequences and sequential e-values by their actual mathematical guarantees; verify estimator assumptions, metric maturity and cluster dependence against the supported procedure. Do not claim confidence sequences are interchangeable with ordinary repeated confidence intervals.
4. For treatment adaptation or changing allocation, re-estimate inference under the actual randomization probabilities and design; reassess sample-ratio diagnostics separately because a fixed expected ratio may no longer apply.
5. Track user-level outcome delays, exposure cohorts, repeat users, missing data and overlapping windows. Require the same sequential definition in monitoring/guardrail dashboards and decision reports.
6. Before enabling automatic stopping, simulate at least null, realistic positive, realistic negative, delayed-outcome and drift scenarios with the actual schedule. Record estimated type-I error, power, sample usage and stopping frequency **from measured simulations**, not assumed targets.
7. If the experiment ran with unplanned peeking or changed boundaries after inspecting effects, **mark nominal inferential guarantees invalid** and request a defensible new confirmatory experiment or explicitly exploratory analysis.

## Evidence and output contract

Return `estimand | randomization unit | monitoring rule | looks/information fractions | sequential boundary | multiplicity | delayed outcomes | simulated error/power | actual stopping outcome | limitations`. A post-hoc fixed-horizon p-value does not retrospectively justify optional stopping. For assignment logs use the dedicated A/B skill; a basic SRM p-value is not itself a sequentially valid repeated-monitoring statistic.

## Failure modes and abstention

- Do not repeatedly inspect ordinary fixed-horizon p-values and stop when one crosses a threshold.
- Do not treat a Bayesian posterior probability as automatically equivalent to frequentist sequential error control.
- Do not change stopping boundaries after seeing outcomes.
- Do not apply IID sequential methods to cluster-randomized or adaptive experiments without a valid design.
- If the actual monitoring process differs from the planned one, do not claim the nominal error guarantee.

## Validation checklist

- [ ] Sequential design and stopping rules are predeclared.
- [ ] Chosen procedure matches the monitoring process.
- [ ] Type-I error and power are simulated or otherwise justified.
- [ ] Assignment integrity and outcome maturity are checked at each look.
- [ ] Final report includes stopping time and sequentially valid inference.

## Authoritative references

- https://pubsonline.informs.org/doi/abs/10.1287/opre.2021.2135
- https://arxiv.org/abs/1512.04922
- https://www.statsig.com/perspectives/ab-testing-statistics
- https://online.stat.psu.edu/stat509/Lesson10

## Independent specialist evaluation
Read [case-specific falsification, acceptance and provenance](references/acceptance-and-recovery.md) on demand for production-impacting or high-stakes work. Unexecuted tests and unsupported claims remain unverified; this reference cannot authorize actions.
