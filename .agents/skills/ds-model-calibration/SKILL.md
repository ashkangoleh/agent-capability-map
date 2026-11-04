---
name: ds-model-calibration
description: Use when evaluating or correcting probability calibration, prediction thresholds, and decision costs for classification models.
metadata:
  version: "1.1.0"
---

# ds-model-calibration

## Activation boundary

Use when model scores are interpreted as probabilities or converted into operational decisions. Calibration is distinct from ranking/discrimination and from causal treatment-effect estimation.

## Required context

Prediction horizon, target definition, prevalence, score distribution, calibration data, class costs, capacity constraints and subgroup definitions.

## Workflow

1. Check whether the model output is a probability, margin, ranking score or transformed score. Do not apply probability calibration to an arbitrary score without defining the mapping.
2. Evaluate discrimination and calibration separately. Use log loss/Brier score, reliability diagrams, calibration intercept/slope and subgroup calibration; include confidence intervals where feasible.
3. Reserve an independent calibration set or use cross-fitting. Never fit a calibrator on the final test labels.
4. Compare sigmoid/Platt, isotonic or other justified calibration methods against the uncalibrated baseline. Isotonic can overfit with limited calibration data.
5. Select thresholds from an explicit cost matrix, capacity limit, utility function or policy constraint. Report precision, recall, false-positive/negative counts and expected cost across thresholds.
6. Evaluate threshold and calibration stability across time, prevalence shifts, key subgroups and data-quality changes.
7. If prevalence or covariate distributions shift, reassess calibration. Prior-probability adjustment requires assumptions and should not be applied automatically.
8. Record the calibrator, split, threshold, objective, subgroup metrics and retraining trigger separately from the base model.

## Decision rules

- Good ROC-AUC does not imply calibrated probabilities.
- A 0.5 threshold is not generally optimal.
- Calibration can change ranking for some methods; re-evaluate discrimination after calibration.
- Global calibration does not guarantee subgroup calibration.

## Failure modes and abstention

- Do not optimize thresholds on the final test set.
- Do not report calibration from the training set.
- Do not treat threshold tuning as a substitute for fairness or policy review.
- If calibration data are too small or not representative, report uncertainty and avoid false precision.

## Validation checklist

- [ ] Probability semantics and prediction horizon are explicit.
- [ ] Calibration is measured on independent data.
- [ ] Discrimination and calibration are reported separately.
- [ ] Threshold is tied to costs/capacity, not convention.
- [ ] Stability and subgroup calibration are checked.

## Authoritative reference

- https://scikit-learn.org/stable/modules/calibration.html
