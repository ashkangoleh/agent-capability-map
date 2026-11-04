---
name: ds-problem-framing
description: "Translate business questions into estimands, prediction targets and decision rules."
metadata:
  version: "1.0.0"
---

# ds-problem-framing

## Activation boundary
Translate business questions into estimands, prediction targets and decision rules.

## Required context
Decision owner, unit of analysis, target population, horizon and error costs.

## Analysis procedure
1. Define decision, unit of analysis, target population and estimand.
2. Inspect provenance, grain, types, missingness and temporal availability.
3. Pin libraries/environments and make notebook execution order explicit.
4. Separate exploratory from confirmatory choices; record assumptions and versions.
5. Validate numerical stability, reproducibility, leakage and decision relevance.

## Failure modes and safeguards
- Do not infer causality from predictive association or treat a p-value as effect size.
- Protect temporal/group boundaries, label availability, sampling design and multiplicity assumptions.
- Report uncertainty, sensitivity, calibration and population limitations; do not fabricate performance.

## Validation
- Reproduce from a clean environment and immutable data/split definitions.
- Test leakage, missingness, subgroup stability, sensitivity and generalization.
- Record library versions, seeds, assumptions, metrics and limitations.

## Official reference
- https://scikit-learn.org/stable/getting_started.html

## Output contract
Return the analysis/modeling result with estimand, assumptions, validation design, uncertainty, reproducibility and decision implications. Separate observed evidence from inference.
