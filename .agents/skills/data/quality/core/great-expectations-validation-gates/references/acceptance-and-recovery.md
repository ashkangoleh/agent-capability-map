# great-expectations-validation-gates: specialist evaluation and negative controls

Domain `data/quality/core`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Define data contract and business-key grain before choosing reusable Expectations.
2. Verify the installed GX Core APIs and versions rather than copying outdated legacy checkpoints.
3. Create suites around datasets and batch definitions, including schema, uniqueness, nulls and domain invariants.
4. Separate warning, quarantine and fail-closed checks according to downstream business impact.

## Challenge / acceptance
- **Challenge:** Inject null-key, duplicate and schema mismatch. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Fail-closed publication with clean reconciliation and actionable alert owner. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** Unknown evidence remains UNKNOWN.
- **Stop/review:** No accuracy or causal claim based on a dashboard or pipeline-success status alone. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://docs.greatexpectations.io/docs/core/define_expectations/organize_expectation_suites/
- https://docs.greatexpectations.io/

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
