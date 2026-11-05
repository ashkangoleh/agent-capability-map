# ds-gradient-boosting: specialist evaluation and negative controls

Domain `data/data-science/modeling`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Establish a simple baseline and define task-aligned metrics, business costs and decision thresholds.
2. Split by time, entity or group before fitting any learned preprocessing. Preserve an untouched final test set.
3. Choose the family deliberately: XGBoost for flexible objective/regularization and ecosystem support, LightGBM for efficient histogram-based training at scale, CatBoost when categorical handling and ordered statistics are useful. Verify actual workload fit rather than relying on generic speed claims.
4. Define objective, evaluation metric, learning rate, tree depth/leaves, minimum child data, row/column sampling, regularization and missing-value semantics.

## Challenge / acceptance
- **Challenge:** Shift sampling frame, intervention timing or held-out cohort. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Evaluate uncertainty intervals, leakage diagnostics and falsifiable baselines. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - Do not use random row splits for repeated entities or temporal prediction without justification.
- Do not tune repeatedly on the final test set.
- Do not infer production calibration from training or resampled validation data.
- **Stop/review:** No accuracy or causal claim based on a dashboard or pipeline-success status alone. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://xgboost.readthedocs.io/
- https://lightgbm.readthedocs.io/
- https://catboost.ai/en/docs/

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
