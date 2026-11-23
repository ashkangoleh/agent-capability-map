# ds-panel-econometrics: specialist evaluation and negative controls

Domain `data/data-science/causal`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Validate one row per entity-period, time frequency, duplicate keys, gaps, entry/exit, changing identifiers and treatment timing.
2. Define the estimand and variation used for identification: within-entity, between-entity, within-time or treatment-timing variation.
3. Compare pooled, entity fixed-effects, time fixed-effects, two-way fixed-effects and random-effects structures. State the assumptions required for each; do not choose random effects solely for efficiency.
4. Check serial correlation, cross-sectional dependence, heteroskedasticity, few clusters, unit roots and common shocks where relevant.

## Challenge / acceptance
- **Challenge:** Shift sampling frame, intervention timing or held-out cohort. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Evaluate uncertainty intervals, leakage diagnostics and falsifiable baselines. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - Do not use ordinary IID standard errors for serially correlated panels.
- Do not interpret entity fixed effects as controlling for time-varying confounding.
- Do not assume parallel trends because a pre-trend test is non-significant.
- **Stop/review:** No accuracy or causal claim based on a dashboard or pipeline-success status alone. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://docs.doubleml.org/stable/guide/models.html
- https://bashtage.github.io/linearmodels/

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
