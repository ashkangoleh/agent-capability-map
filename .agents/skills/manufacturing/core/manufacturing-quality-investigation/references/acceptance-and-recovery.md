# manufacturing-quality-investigation: specialist evaluation and negative controls

Domain `manufacturing/core`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Define the defect and affected process window with traceable lot/serial boundaries, observed rate and known impact.
2. Contain suspect output safely under plant policy; do not direct unsafe machine operation.
3. Separate symptom from hypotheses; review material, machine, method, measurement, environment and operator conditions.
4. Validate measurement repeatability and data collection bias before interpreting control charts or rates.

## Challenge / acceptance
- **Challenge:** Inject out-of-spec process data or altered bill of materials. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Lot genealogy, defect containment and safety limits are verifiable. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** Unknown evidence remains UNKNOWN.
- **Stop/review:** No equipment actuation or process safety approval without qualified engineer. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://asq.org/quality-resources/root-cause-analysis
- https://www.nist.gov/el

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
