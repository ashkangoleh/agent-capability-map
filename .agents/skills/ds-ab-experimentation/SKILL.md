---
name: ds-ab-experimentation
description: "Analyze randomized experiments with predeclared primary metrics, guardrails and sequential validity."
metadata:
  version: "1.0.0"
---

# ds-ab-experimentation

## Activation boundary
Analyze randomized experiments with predeclared primary metrics, guardrails and sequential validity.

## Required context
Randomization unit, exposure, primary/guardrail metrics, sample ratio and stopping rule.

## Analysis procedure
1. Predeclare primary outcome, guardrails, eligibility, assignment unit and stopping rule.
2. Check randomization, exposure, sample ratio, contamination and interference.
3. Estimate power and MDE before inspecting outcomes.
4. Analyze treatment effects with uncertainty and multiplicity controls.
5. Do not re-label post-hoc findings as confirmatory.

## Failure modes and safeguards
- Do not infer causality from predictive association or treat a p-value as effect size.
- Protect temporal/group boundaries, label availability, sampling design and multiplicity assumptions.
- Report uncertainty, sensitivity, calibration and population limitations; do not fabricate performance.

## Validation
- Reproduce from a clean environment and immutable data/split definitions.
- Test leakage, missingness, subgroup stability, sensitivity and generalization.
- Record library versions, seeds, assumptions, metrics and limitations.

## Official reference
- https://www.statsig.com/perspectives/ab-testing-statistics

## Output contract
Return the analysis/modeling result with estimand, assumptions, validation design, uncertainty, reproducibility and decision implications. Separate observed evidence from inference.
