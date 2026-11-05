# ds-doubleml-causal-estimation: specialist evaluation and negative controls

Domain `data/data-science/causal`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. State the causal estimand and identification assumptions before selecting a DoubleML model. Decide whether the structure is partially linear, interactive/binary treatment, IV, difference-in-differences or another supported design.
2. Verify data layout and variable roles: outcome, treatment, covariates, instruments, cluster identifiers and sample-splitting units.
3. Choose an orthogonal score that matches the estimand and data-generating assumptions. Do not select PLR, IRM or PLIV by convenience.
4. Choose nuisance learners with regularization and task-appropriate loss. Keep tuning inside the training folds and avoid using outcome information outside the prescribed cross-fitting structure.

## Challenge / acceptance
- **Challenge:** Shift sampling frame, intervention timing or held-out cohort. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Evaluate uncertainty intervals, leakage diagnostics and falsifiable baselines. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - Do not claim DML removes unobserved confounding.
- Do not use random cross-fitting when observations are dependent by entity, cluster or time.
- Do not trust estimates under severe positivity violations or weak instruments.
- **Stop/review:** No accuracy or causal claim based on a dashboard or pipeline-success status alone. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://docs.doubleml.org/stable/guide/guide.html
- https://docs.doubleml.org/stable/guide/models.html

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
