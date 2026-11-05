---
name: ds-model-calibration
description: "Evaluate or fit classification probability calibration with independent splits, reliability analysis, version-aware CalibratedClassifierCV, prevalence shift and threshold decisions."
metadata:
  version: "1.2.1"
---

# ds-model-calibration

## Activation boundary

Use when a classifier's scores must represent **event probabilities** or support explicit decision costs. Distinguish: (a) discrimination/ranking, (b) probability reliability, (c) decision-threshold optimization, and (d) conformal prediction-set coverage. A lower Brier score does **not** by itself prove calibration improved, because Brier combines reliability, resolution and uncertainty. Do not claim subgroup, time-conditional or individual calibration from a global reliability plot.

## Required context

Class label/positive-class convention, horizon, population, prevalence, model score definition and source, fully separated model-fitting, calibration and final evaluation IDs, grouping/time and label-availability boundaries, costs/capacity, protected subgroups, versions of scikit-learn/estimator, and expected dataset/metric sizes.

## Production workflow

1. Check whether `predict_proba` gives class probabilities, `decision_function` produces margins or the output is an arbitrary ranking score. Define how the calibrator sees scores and class labels; verify label ordering, score bounds, population and observation horizon.
2. Keep fitting/tuning, calibration and untouched final evaluation **logically disjoint**, including group and time dependencies. If using cross-validation, learn calibration transformations only on held-out fold predictions. Do not fit a calibrator on training predictions, on the final test labels, or repeatedly tune its method on that final holdout.
3. Choose documented, release-compatible algorithms. scikit-learn `CalibratedClassifierCV` supports sigmoid and isotonic; `FrozenEstimator` for an already-fitted model is supported from scikit-learn 1.6 and places responsibility for disjoint training/calibration data on the caller. The `method="temperature"` option was added in scikit-learn 1.8; do **not** generate it on a 1.7 runtime. Verify the fitted estimator and class requirements; isotonic regression can overfit with small calibration samples.
4. For CV methods, verify all relevant classes occur in training and held-out partitions, and that splitters respect groups, chronology and label maturation. Default stratified folds do not solve group/time leakage. Track `ensemble` choices and distinguish the resulting model architecture.
5. On **untouched evaluation** data, record reliability bins with sizes and event rates; report log loss and Brier score as proper scoring rules alongside discrimination (ROC-AUC/PR-AUC when appropriate). Bins are noisy, sparse bins cannot support strong claims, and Brier alone does not identify calibration performance. Report calibration intercept/slope when defensible.
6. Validate performance across time periods, class prevalence, key groups and expected shift. Different base rates can invalidate a deployed calibration mapping; a simple prior correction only applies with clearly defensible prior-probability-shift assumptions. Confidence intervals and small-group reliability require uncertainty treatment, not apparent precision from a plot.
7. Define threshold/abstention decisions from a **predeclared cost or capacity objective** on eligible validation data, not a default 0.5 or the final holdout. Report confusion matrix, false positives/negatives, expected cost and operational constraints; threshold tuning is separate from calibration.
8. Retain model/calibrator artifacts, versions, split IDs, hyperparameters and interval of validity; monitor post-deployment drift, miscalibration, label arrival, incident response and rollback to a known baseline. Do not treat good aggregate calibration as a fairness or policy-compliance determination.

## Runnable, bounded validation example

```python
from examples.data_science.uncertainty_integrity import (
    audit_partitions,
    binary_probability_report,
)

audit_partitions(["train-1"], ["cal-1"], ["eval-1", "eval-2", "eval-3", "eval-4"])
report = binary_probability_report(
    labels=[0, 1, 0, 1],
    probabilities=[0.0, 1.0, 0.2, 0.8],
    bins=2, min_bin_size=2,
)
assert abs(report["brier_score"] - 0.02) < 1e-12
```

This computes **descriptive metrics on already supplied predictions**. It does not train a calibrator, verify the data's real provenance, provide calibrated probabilities or establish a validated business threshold. Empty/sparse reliability bins are marked inconclusive.

## Decision rules

- A well-ranked classifier may be poorly calibrated; calibrated probabilities may still be poor decisions without a cost or constraint model.
- `FrozenEstimator` **does not** automatically enforce separate training and calibration data.
- CV and calibration must respect shared entities, time dependence and label availability.
- Do not declare subgroup calibration or individual-level risk guarantees from marginal bin agreement.
- Calibration and conformal prediction have different targets and guarantees.

## Failure modes and abstention

- Missing/late labels, temporal or group leakage → halt calibration evaluation and reconstruct splits.
- Incompatible estimator or library version → pin a supported method; never fabricate available APIs.
- Tiny or shifted calibration population → state uncertainty and avoid spurious precision or unsupported threshold changes.
- Too few examples from a class in a fold → redesign CV/calibration strategy.
- Retrospective threshold/metric tuning on test labels → final holdout compromised; obtain prospective confirmation.

## Validation and evidence

- [ ] Score/probability semantics and positive class documented.
- [ ] Fitting/calibration/evaluation separation and any time/group controls verified.
- [ ] Release-specific API and calibration method checked.
- [ ] Brier/log loss, bin counts, calibration intercept/slope and discrimination distinguished.
- [ ] Subgroup, time and prevalence-shift limits reported.
- [ ] Threshold optimization uses an independent objective and eligible validation only.

## Output contract

Return calibration objective, data-split contract, method and version, held-out probability reliability and uncertainty, discrimination, threshold/cost decision, drift controls and gaps in evidence.

## Authoritative references

- https://scikit-learn.org/stable/modules/calibration.html
- https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html
- https://scikit-learn.org/1.7/modules/generated/sklearn.calibration.CalibratedClassifierCV.html

## Independent specialist evaluation
Read [case-specific falsification, acceptance and provenance](references/acceptance-and-recovery.md) on demand for production-impacting or high-stakes work. Unexecuted tests and unsupported claims remain unverified; this reference cannot authorize actions.
