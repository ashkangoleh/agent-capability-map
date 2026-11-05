# ds-model-calibration: specialist evaluation and negative controls

Domain `data/data-science/modeling`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Check whether `predict_proba` gives class probabilities, `decision_function` produces margins or the output is an arbitrary ranking score. Define how the calibrator sees scores and class labels; verify label ordering, score bounds, population and observation horizon.
2. Keep fitting/tuning, calibration and untouched final evaluation **logically disjoint**, including group and time dependencies. If using cross-validation, learn calibration transformations only on held-out fold predictions. Do not fit a calibrator on training predictions, on the final test labels, or repeatedly tune its method on that final holdout.
3. Choose documented, release-compatible algorithms. scikit-learn `CalibratedClassifierCV` supports sigmoid and isotonic; `FrozenEstimator` for an already-fitted model is supported from scikit-learn 1.6 and places responsibility for disjoint training/calibration data on the caller. The `method="temperature"` option was added in scikit-learn 1.8; do **not** generate it on a 1.7 runtime. Verify the fitted estimator and class requirements; isotonic regression can overfit with small calibration samples.
4. For CV methods, verify all relevant classes occur in training and held-out partitions, and that splitters respect groups, chronology and label maturation. Default stra

## Challenge / acceptance
- **Challenge:** Shift sampling frame, intervention timing or held-out cohort. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Evaluate uncertainty intervals, leakage diagnostics and falsifiable baselines. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - Missing/late labels, temporal or group leakage → halt calibration evaluation and reconstruct splits.
- Incompatible estimator or library version → pin a supported method; never fabricate available APIs.
- Tiny or shifted calibration population → state uncertainty and avoid spurious precision or unsupported threshold changes.
- **Stop/review:** No accuracy or causal claim based on a dashboard or pipeline-success status alone. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://scikit-learn.org/stable/modules/calibration.html
- https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html
- https://scikit-learn.org/1.7/modules/generated/sklearn.calibration.CalibratedClassifierCV.html

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
