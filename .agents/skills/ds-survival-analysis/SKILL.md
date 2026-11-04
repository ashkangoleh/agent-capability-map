---
name: ds-survival-analysis
description: "Analyze time-to-event outcomes with censoring, competing risks and hazard assumptions."
metadata:
  version: "1.0.0"
---

# ds-survival-analysis

## Activation boundary
Analyze time-to-event outcomes with censoring, competing risks and hazard assumptions.

## Required context
Time origin, event definition, censoring mechanism, competing events and follow-up.

## Analysis procedure
1. Define time origin, event, censoring, competing risks and estimand.
2. Inspect censoring assumptions, follow-up and delayed entry.
3. Choose survival methods from assumptions and event structure.
4. Check proportional hazards, calibration and time-dependent discrimination.
5. Report absolute risk and sensitivity over meaningful horizons.

## Failure modes and safeguards
- Do not infer causality from predictive association or treat a p-value as effect size.
- Protect temporal/group boundaries, label availability, sampling design and multiplicity assumptions.
- Report uncertainty, sensitivity, calibration and population limitations; do not fabricate performance.

## Validation
- Reproduce from a clean environment and immutable data/split definitions.
- Test leakage, missingness, subgroup stability, sensitivity and generalization.
- Record library versions, seeds, assumptions, metrics and limitations.

## Official reference
- https://lifelines.readthedocs.io/en/latest/

## Output contract
Return the analysis/modeling result with estimand, assumptions, validation design, uncertainty, reproducibility and decision implications. Separate observed evidence from inference.
