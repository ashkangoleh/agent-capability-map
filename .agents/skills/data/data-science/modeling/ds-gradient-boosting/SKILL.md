---
name: ds-gradient-boosting
description: Use when training, tuning, diagnosing, or comparing gradient-boosted tree models such as XGBoost, LightGBM, and CatBoost.
metadata:
  version: "1.1.1"
---

# ds-gradient-boosting

## Activation boundary

Use for tabular regression, classification or ranking with boosted decision trees. Do not default to boosting when a linear, generalized linear, calibrated baseline or interpretable model is sufficient.

## Required context

Target and prediction timestamp, entity grain, feature schema, split strategy, class prevalence, missing/categorical features, latency and memory constraints.

## Workflow

1. Establish a simple baseline and define task-aligned metrics, business costs and decision thresholds.
2. Split by time, entity or group before fitting any learned preprocessing. Preserve an untouched final test set.
3. Choose the family deliberately: XGBoost for flexible objective/regularization and ecosystem support, LightGBM for efficient histogram-based training at scale, CatBoost when categorical handling and ordered statistics are useful. Verify actual workload fit rather than relying on generic speed claims.
4. Define objective, evaluation metric, learning rate, tree depth/leaves, minimum child data, row/column sampling, regularization and missing-value semantics.
5. Use early stopping only on a validation set separated from the final test. Keep feature selection and tuning inside training folds.
6. Inspect class imbalance, sample weights, label noise, leakage, categorical cardinality and rare categories. Do not assume resampling is harmless.
7. Compare performance, calibration, latency, memory, model size and stability across seeds and time periods.
8. Diagnose residuals and errors by subgroup, target range, time and feature availability. Use SHAP or permutation analysis only with their assumptions and limitations.
9. Freeze the model-selection process before final test evaluation; retain training data version, split IDs, environment and model parameters.

## Decision rules

- Tree depth/leaves and learning rate jointly control complexity; tune them as a structured search, not isolated knobs.
- A ranking metric, probability metric and threshold metric answer different questions.
- Feature importance is not causal effect.
- If latency or memory dominates, benchmark the serving path rather than training time alone.

## Failure modes and abstention

- Do not use random row splits for repeated entities or temporal prediction without justification.
- Do not tune repeatedly on the final test set.
- Do not infer production calibration from training or resampled validation data.
- If a simpler baseline is within uncertainty and cheaper to operate, prefer it.

## Validation checklist

- [ ] Leakage-safe temporal/group split and baseline exist.
- [ ] Objective and metric match the decision.
- [ ] Early stopping and tuning avoid final-test reuse.
- [ ] Calibration and subgroup errors are evaluated.
- [ ] Runtime, memory and model size are measured.

## Authoritative references

- https://xgboost.readthedocs.io/
- https://lightgbm.readthedocs.io/
- https://catboost.ai/en/docs/

## Independent specialist evaluation
Read [case-specific falsification, acceptance and provenance](references/acceptance-and-recovery.md) on demand for production-impacting or high-stakes work. Unexecuted tests and unsupported claims remain unverified; this reference cannot authorize actions.
