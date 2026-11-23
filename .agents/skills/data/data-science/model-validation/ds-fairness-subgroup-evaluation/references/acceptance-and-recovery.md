# ds-fairness-subgroup-evaluation: specialist evaluation and negative controls

Domain `data/data-science/model-validation`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Identify the potential harms and affected groups with domain and policy owners. Define intersections and the unit at which harm occurs.
2. Audit group representation, missing sensitive attributes, label quality, selection mechanisms and sample sizes. Do not assume observed labels are unbiased ground truth.
3. Select metrics from the harm model rather than choosing one generic fairness score:
- selection-rate or demographic-parity differences;

## Challenge / acceptance
- **Challenge:** Shift sampling frame, intervention timing or held-out cohort. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Evaluate uncertainty intervals, leakage diagnostics and falsifiable baselines. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - Do not publish unstable metrics for very small groups as precise facts.
- Do not infer absence of bias from one parity metric.
- Do not use sensitive attributes in mitigation or decisioning without authorization and legal/policy review.
- **Stop/review:** No accuracy or causal claim based on a dashboard or pipeline-success status alone. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://fairlearn.org/main/
- https://fairlearn.org/main/user_guide/fairness_in_machine_learning.html

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
