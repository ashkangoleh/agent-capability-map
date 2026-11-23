# sklearn-leakage-free-validation: specialist evaluation and negative controls

Domain `data/data-science/model-validation`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
- Prediction task, target and observation grain; unit of independence (person, device, customer, site, panel, household).
- Feature observation time, feature publication/availability time, prediction decision time, label event time and label **availability** time.
- Deployment evaluation horizon; temporal autocorrelation, overlapping label windows, duplicates, repeated entities and distribution shift.
- Class prevalence, metric/cost matrix, groups, split design, number of independent groups, train/test sizes, tuning budget and protected final test period.

## Preserve skill-specific method
1. Define a **time-of-prediction contract** before choosing a splitter. For each row, distinguish when a feature was measured from when it became usable and when the outcome became known. Reject features derived after the decision timestamp (including rolling aggregates using future rows and target-proxy joins).
2. Choose a split that reflects **how the model will be deployed**:
- IID independent examples: train/validation/test, stratifying classification targets where appropriate.
- Repeated users/devices/organizations: use group-disjoint outer splits (`GroupKFold`, `GroupShuffleSplit`, or `StratifiedGroupKFold` when class balance and group separation both matter). Ensure the group count supports the fold count. `StratifiedKFold` alone does **not** prevent entity reuse across folds.

## Challenge / acceptance
- **Challenge:** Shift sampling frame, intervention timing or held-out cohort. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Evaluate uncertainty intervals, leakage diagnostics and falsifiable baselines. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - **Target leakage from full-dataset preprocessing**: discard contaminated measurements, rebuild fold-local transformations and rerun against untouched folds.
- **Repeated entities across folds**: redesign group keys and use group-disjoint splits; re-estimate performance.
- **Temporal or horizon leakage**: rebuild from chronological prediction and label-availability fields, add horizon-appropriate purge/embargo and repeat backtest.
- **Stop/review:** No accuracy or causal claim based on a dashboard or pipeline-success status alone. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://scikit-learn.org/stable/common_pitfalls.html
- https://scikit-learn.org/stable/modules/cross_validation.html
- https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html
- https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html
- https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedGroupKFold.html

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
