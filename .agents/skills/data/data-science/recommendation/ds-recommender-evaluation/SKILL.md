---
name: ds-recommender-evaluation
description: "Evaluate recommendation systems with temporal splits, candidate generation and ranking metrics."
metadata:
  version: "1.0.1"
---

# ds-recommender-evaluation

## Activation boundary
Evaluate recommendation systems with temporal splits, candidate generation and ranking metrics.

## Required context
User/item grain, exposure logs, candidates, labels, temporal split and objective.

## Analysis procedure
1. Define user-item grain, exposure, candidate set and ranking objective.
2. Use temporal splits and prevent exposure/label leakage.
3. Evaluate retrieval and ranking stages separately.
4. Check popularity bias, cold start, coverage and diversity.
5. Do not infer online causal lift from offline metrics.

## Failure modes and safeguards
- Do not infer causality from predictive association or treat a p-value as effect size.
- Protect temporal/group boundaries, label availability, sampling design and multiplicity assumptions.
- Report uncertainty, sensitivity, calibration and population limitations; do not fabricate performance.

## Validation
- Reproduce from a clean environment and immutable data/split definitions.
- Test leakage, missingness, subgroup stability, sensitivity and generalization.
- Record library versions, seeds, assumptions, metrics and limitations.

## Official reference
- https://recbole.io/docs/

## Output contract
Return the analysis/modeling result with estimand, assumptions, validation design, uncertainty, reproducibility and decision implications. Separate observed evidence from inference.

## Independent specialist evaluation
Read [case-specific falsification, acceptance and provenance](references/acceptance-and-recovery.md) on demand for production-impacting or high-stakes work. Unexecuted tests and unsupported claims remain unverified; this reference cannot authorize actions.
