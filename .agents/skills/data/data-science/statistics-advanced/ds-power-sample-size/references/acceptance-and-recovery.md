# ds-power-sample-size: specialist evaluation and negative controls

Domain `data/data-science/statistics-advanced`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Define the primary estimand, analysis population, outcome scale and smallest effect that would change the decision.
2. Choose a test/estimator consistent with the design: continuous, binary, count, time-to-event, paired, clustered, repeated-measures or non-inferiority.
3. Specify type-I error, desired power, allocation ratio, one- or two-sided alternative and multiplicity adjustment before calculating sample size.
4. Estimate nuisance parameters from prior data or a blinded pilot. Use conservative variance and baseline-rate assumptions; document uncertainty.

## Challenge / acceptance
- **Challenge:** Shift sampling frame, intervention timing or held-out cohort. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Evaluate uncertainty intervals, leakage diagnostics and falsifiable baselines. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - Do not compute power from an effect estimate selected because it looked promising.
- Do not ignore clustering, repeated users, multiplicity or sequential monitoring.
- If baseline variance or traffic assumptions are weak, provide a sensitivity range rather than a single precise number.
- **Stop/review:** No accuracy or causal claim based on a dashboard or pipeline-success status alone. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://www.statsmodels.org/stable/stats.html
- https://docs.scipy.org/doc/scipy/reference/stats.html

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
