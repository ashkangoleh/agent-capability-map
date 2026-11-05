# ds-shap-explainability: specialist evaluation and negative controls

Domain `data/data-science/modeling`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Define the explanation target: raw margin, probability, log-odds, expected value or another model output. State the scale in every report.
2. Verify the model and preprocessing pipeline are frozen and match the prediction path. Explain the same feature representation the model actually consumes.
3. Select a background dataset that represents the intended reference population. Document sampling, time window and privacy constraints.
4. Choose an explainer appropriate to the model and computational budget. Verify whether the implementation uses conditional, interventional or another feature-dependence assumption.

## Challenge / acceptance
- **Challenge:** Shift sampling frame, intervention timing or held-out cohort. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Evaluate uncertainty intervals, leakage diagnostics and falsifiable baselines. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - Do not explain a model with a different preprocessing pipeline from production.
- Do not compare SHAP values across models or cohorts without compatible scales and baselines.
- Do not infer intervention outcomes from observational attributions.
- **Stop/review:** No accuracy or causal claim based on a dashboard or pipeline-success status alone. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://shap.readthedocs.io/en/latest/

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
