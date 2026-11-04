---
name: ds-sequential-experimentation
description: Use when experiments are monitored repeatedly, stopped early, adapted, or analyzed with sequentially valid inference.
metadata:
  version: "1.0.0"
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
