# ds-causal-inference: specialist evaluation and negative controls

Domain `data/data-science/experimentation`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Define the estimand before choosing an estimator: ATE, ATT, LATE, CATE, policy effect or another explicit contrast. Specify population, treatment versions and time horizon.
2. Identify the assignment mechanism. Prefer randomized assignment when feasible and ethical; otherwise explain why an observational or quasi-experimental design is credible.
3. Draw a causal DAG and distinguish pre-treatment confounders from mediators, colliders and post-treatment variables. Do not adjust mechanically for every available covariate.
4. Check consistency, exchangeability, positivity/overlap, interference and measurement assumptions relevant to the design.

## Challenge / acceptance
- **Challenge:** Shift sampling frame, intervention timing or held-out cohort. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Evaluate uncertainty intervals, leakage diagnostics and falsifiable baselines. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - Do not call predictive feature importance or an adjusted regression coefficient a causal effect without an identification argument.
- Do not select a method by package availability.
- Do not interpret a non-significant pre-trend test as proof of parallel trends.
- **Stop/review:** No accuracy or causal claim based on a dashboard or pipeline-success status alone. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://mixtape.scunning.com/
- https://docs.doubleml.org/stable/guide/guide.html
- https://www.pywhy.org/dowhy/
- https://www.pywhy.org/dowhy/v0.11/user_guide/causal_tasks/estimating_causal_effects/index.html

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
