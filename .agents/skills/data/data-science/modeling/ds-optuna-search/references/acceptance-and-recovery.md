# ds-optuna-search: specialist evaluation and negative controls

Domain `data/data-science/modeling`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Freeze the data split and metric before search. Use nested cross-validation or a separate final holdout when model selection itself is part of the evaluation.
2. Define a search space from model semantics and plausible scales. Prefer log distributions for scale parameters and conditional branches for incompatible model families.
3. Build an objective that fits preprocessing inside each training fold and returns a metric aggregated across the correct validation folds.
4. Select a sampler based on the search structure and budget. Use random search as a baseline; use TPE or another adaptive sampler only when its added complexity is justified.

## Challenge / acceptance
- **Challenge:** Shift sampling frame, intervention timing or held-out cohort. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Evaluate uncertainty intervals, leakage diagnostics and falsifiable baselines. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - Do not tune repeatedly against the same holdout.
- Do not parallelize with uncontrolled shared random state and then claim bitwise reproducibility.
- Do not compare trials that used different data, feature availability or evaluation rules.
- **Stop/review:** No accuracy or causal claim based on a dashboard or pipeline-success status alone. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://optuna.readthedocs.io/en/stable/

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
