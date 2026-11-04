---
name: ds-classical-nlp
description: "Build classical NLP workflows with tokenization, sparse features and language-aware evaluation."
metadata:
  version: "1.0.0"
---

# ds-classical-nlp

## Activation boundary
Build classical NLP workflows with tokenization, sparse features and language-aware evaluation.

## Required context
Language, tokenization, labels, class balance, privacy and vocabulary drift.

## Analysis procedure
1. Define text unit, language, label policy, privacy and target task.
2. Build reproducible tokenization/vectorization inside the training pipeline.
3. Compare sparse baselines with complex representations only when justified.
4. Evaluate per-class, language and temporal performance; inspect annotation noise.
5. Monitor vocabulary drift, sensitive text leakage and preprocessing parity.

## Failure modes and safeguards
- Do not infer causality from predictive association or treat a p-value as effect size.
- Protect temporal/group boundaries, label availability, sampling design and multiplicity assumptions.
- Report uncertainty, sensitivity, calibration and population limitations; do not fabricate performance.

## Validation
- Reproduce from a clean environment and immutable data/split definitions.
- Test leakage, missingness, subgroup stability, sensitivity and generalization.
- Record library versions, seeds, assumptions, metrics and limitations.

## Official reference
- https://scikit-learn.org/stable/tutorial/text_analytics/

## Output contract
Return the analysis/modeling result with estimand, assumptions, validation design, uncertainty, reproducibility and decision implications. Separate observed evidence from inference.
