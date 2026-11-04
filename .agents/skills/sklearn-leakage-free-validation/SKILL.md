---
name: sklearn-leakage-free-validation
description: "Design leakage-resistant scikit-learn model validation with group-aware, time-aware and label-availability-aware split contracts, nested tuning and honest holdout evidence."
metadata:
  version: "1.1.0"
---

# sklearn-leakage-free-validation

## Activation boundary

Use for **model evaluation and cross-validation design** in scikit-learn, including training/test separation, group/time leakage, target-aware preprocessing and reproducible generalization estimates. A mention of "scikit-learn" alone is insufficient to activate this skill. For causal identification, conformal coverage guarantees, probability calibration, feature-store point-in-time joins or deployment, route to their respective specialists rather than guessing.

## Required context

- Prediction task, target and observation grain; unit of independence (person, device, customer, site, panel, household).
- Feature observation time, feature publication/availability time, prediction decision time, label event time and label **availability** time.
- Deployment evaluation horizon; temporal autocorrelation, overlapping label windows, duplicates, repeated entities and distribution shift.
- Class prevalence, metric/cost matrix, groups, split design, number of independent groups, train/test sizes, tuning budget and protected final test period.
- Exact Python/scikit-learn release, source data lineage, preprocessing and feature-selection operations, random seeds and environment provenance.

## Production workflow

1. Define a **time-of-prediction contract** before choosing a splitter. For each row, distinguish when a feature was measured from when it became usable and when the outcome became known. Reject features derived after the decision timestamp (including rolling aggregates using future rows and target-proxy joins).
2. Choose a split that reflects **how the model will be deployed**:
   - IID independent examples: train/validation/test, stratifying classification targets where appropriate.
   - Repeated users/devices/organizations: use group-disjoint outer splits (`GroupKFold`, `GroupShuffleSplit`, or `StratifiedGroupKFold` when class balance and group separation both matter). Ensure the group count supports the fold count. `StratifiedKFold` alone does **not** prevent entity reuse across folds.
   - Time-dependent samples: train only on earlier observations, hold out future windows, and choose realistic forecast horizon and label-maturation delay. `TimeSeriesSplit(gap=...)` gap counts **samples**, not time units, and its comparable-duration interpretation assumes equally spaced samples; irregular intervals or overlapping labels require a custom calendar/purged split.
   - Both repeated entities and temporal dependence: **neither `GroupKFold` nor `TimeSeriesSplit` alone guarantees both constraints**. Use a task-specific splitter with explicit entity and chronological/label-availability checks, or abstain until a valid evaluation design exists.
3. Validate split invariants **before fitting any model**. Verify no row-ID or entity overlap (when grouping is required), chronological separation, label availability before the next prediction period and realistic embargo for overlapping horizons. A duplicate-content scan and external-data provenance review are separate checks.
4. Put `SimpleImputer`, scaling, encoding, supervised feature selection and learned transformations inside a `Pipeline`/`ColumnTransformer` that is fitted **within each training fold**. For target encoding, build out-of-fold encodings inside training partitions; never use future/test labels. If resampling is required, use an implementation that resamples **training folds only**; don't apply SMOTE or other learned resampling to the full dataset before splitting.
5. Perform hyperparameter search inside training data. Use nested CV for an unbiased model-selection-process estimate where feasible; otherwise report that repeated selection on the same validation data can inflate results. The outer test or chronologically future holdout must remain untouched by all tuning, thresholds, feature decisions, calibration and stopping.
6. Ensure model comparison uses **identical outer splits** and consistent metrics. Report fold-level distribution, baseline, uncertainty/variability, subgroup/group performance, distribution drift and operational costs. Beware that a high score may reflect target proxies, dependent observations or changing label prevalence.
7. Refit the chosen pipeline using the allowed train+validation data only; evaluate the protected holdout **once** at the end. If results inform a new model selection cycle, this holdout is no longer an unbiased final test; obtain another prospective evaluation.
8. Record dataset and code hashes, exact sklearn/estimator versions, split indices/group and temporal definitions, preprocessing pipeline, randomness controls, tuned search space, metric definition and decision threshold. For randomized splitters use a fixed splitter seed for comparable fold allocations across competing models; document estimator randomness separately.
9. Audit splits with `examples/data_science/split_integrity.py` (standard library; see example below) and preserve errors as validation evidence. This helper checks index, optional group, chronological and label-availability invariants; **it does not establish the absence of every leakage mechanism**.

## Executable split-contract example

Run from the repository root (Python 3.10+; no third-party dependencies):

```python
from datetime import datetime, timedelta, timezone

from examples.data_science.split_integrity import validate_split_contract

t0 = datetime(2026, 1, 1, tzinfo=timezone.utc)
times = [t0 + timedelta(days=i) for i in range(6)]
labels_ready = [t + timedelta(days=1) for t in times]

result = validate_split_contract(
    train_indices=[0, 1],
    test_indices=[4, 5],
    n_samples=6,
    prediction_times=times,
    label_available_times=labels_ready,
    forward_only=True,
)
assert result == {"train_rows": 2, "test_rows": 2}
```

The helper verifies declared boundaries, not statistical independence, prediction-time feature availability, a complete sklearn `Pipeline` or actual absence of target leakage. In real grouped and temporal datasets, enforce both requirements and verify labels' true maturation times.

## Failure modes and recovery

- **Target leakage from full-dataset preprocessing**: discard contaminated measurements, rebuild fold-local transformations and rerun against untouched folds.
- **Repeated entities across folds**: redesign group keys and use group-disjoint splits; re-estimate performance.
- **Temporal or horizon leakage**: rebuild from chronological prediction and label-availability fields, add horizon-appropriate purge/embargo and repeat backtest.
- **Insufficient independent groups**: decrease folds or change evaluation design; do not force misleading group CV.
- **Post-hoc metric, threshold or model selection on holdout**: mark the holdout compromised; require prospective holdout for unbiased final evidence.
- **Training-serving feature skew**: verify feature timestamp, availability and join parity; model CV alone does not measure online validity.
- **Label/feature late arrival, drift or missing classes**: report invalid folds or uncertain estimates rather than silently dropping difficult periods or groups.
- **Unsupported API/version**: pin documented sklearn behavior. `GroupKFold(shuffle=..., random_state=...)` was introduced in scikit-learn 1.6; do not generate these options for older deployments.

## Validation and evidence

- [ ] Grain, decision time, availability time and label horizon recorded.
- [ ] Group/time/label window split validated; exact group collision and future-label examples included.
- [ ] All learned transforms/feature selection inside fold-local pipeline; final test held out.
- [ ] Resampling and target encoding confined to training folds.
- [ ] Tuning evaluated with separate outer CV or limitations explicitly reported.
- [ ] Baseline, per-fold results, uncertainty, subgroup/temporal degradation and costs documented.
- [ ] Exact release and reproducible dataset/split artifacts retained.
- [ ] `python -m unittest discover -s tests -p 'test_data_science_split_integrity.py' -v` passes in the deployed repository environment.

## Output contract

Return the prediction/label availability contract; selected split strategy and why; explicit leakage audit and negative checks; runnable sklearn pipeline only after confirming the runtime and version; fold-level validation evidence; held-out results (if actually measured); uncertainty and open risks. Never invent accuracy or imply that structural split checks certify a model.

## Authoritative references

- https://scikit-learn.org/stable/common_pitfalls.html
- https://scikit-learn.org/stable/modules/cross_validation.html
- https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html
- https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html
- https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedGroupKFold.html
