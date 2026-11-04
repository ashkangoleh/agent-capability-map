---
name: ds-missing-data
description: "Diagnose MCAR/MAR/MNAR assumptions and choose defensible imputation or sensitivity methods."
metadata:
  version: "1.0.0"
---

# ds-missing-data

## Activation boundary
Diagnose MCAR/MAR/MNAR assumptions and choose defensible imputation or sensitivity methods.

## Required context
Missingness patterns, collection process, estimand, time ordering and downstream model.

## Analysis procedure
1. Write estimand and assumptions before selecting a test/model.
2. Check independence, distributional assumptions, sampling, missingness and multiplicity.
3. Report effect size and uncertainty intervals, not only p-values.
4. Run sensitivity analyses and document unverifiable assumptions.
5. Check power, robustness and generalization.

## Failure modes and safeguards
- Do not infer causality from predictive association or treat a p-value as effect size.
- Protect temporal/group boundaries, label availability, sampling design and multiplicity assumptions.
- Report uncertainty, sensitivity, calibration and population limitations; do not fabricate performance.

## Validation
- Reproduce from a clean environment and immutable data/split definitions.
- Test leakage, missingness, subgroup stability, sensitivity and generalization.
- Record library versions, seeds, assumptions, metrics and limitations.

## Official reference
- https://scikit-learn.org/stable/modules/impute.html

## Output contract
Return the analysis/modeling result with estimand, assumptions, validation design, uncertainty, reproducibility and decision implications. Separate observed evidence from inference.
