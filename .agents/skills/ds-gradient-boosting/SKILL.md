---
name: ds-gradient-boosting
description: "Train and compare gradient-boosted trees with leakage-safe validation, regularization and task-aligned metrics."
metadata:
  version: "1.0.0"
---

# ds-gradient-boosting

## Activation boundary
Train and compare gradient-boosted trees with leakage-safe validation, regularization and task-aligned metrics.

## Required context
Task, feature schema, split, class prevalence, hardware and library versions.

## Analysis procedure
1. Define target, prediction time, entity grain and feature availability before splitting.
2. Use temporal/group splits and fit preprocessing only inside training folds.
3. Compare baselines with tuned models using task-aligned metrics and calibration.
4. Use nested validation or a held-out set; control compute and seeds.
5. Inspect subgroup errors, drift, stability and explainability.

## Failure modes and safeguards
- Do not infer causality from predictive association or treat a p-value as effect size.
- Protect temporal/group boundaries, label availability, sampling design and multiplicity assumptions.
- Report uncertainty, sensitivity, calibration and population limitations; do not fabricate performance.

## Validation
- Reproduce from a clean environment and immutable data/split definitions.
- Test leakage, missingness, subgroup stability, sensitivity and generalization.
- Record library versions, seeds, assumptions, metrics and limitations.

## Official reference
- https://xgboost.readthedocs.io/

## Output contract
Return the analysis/modeling result with estimand, assumptions, validation design, uncertainty, reproducibility and decision implications. Separate observed evidence from inference.
