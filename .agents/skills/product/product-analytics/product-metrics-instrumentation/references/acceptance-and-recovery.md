# product-metrics-instrumentation: specialist evaluation and negative controls

Domain `product/product-analytics`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Start from the business decision, not dashboard widgets. Define product outcomes and leading indicators separately from vanity metrics.
2. Define each metric's exact grain, unit, numerator, denominator, cohort assignment, event time, time zone and exclusions; specify treatment of late/corrected events.
3. Design the event taxonomy and identity graph: anonymous to logged-in transitions, duplicate events, idempotency keys and schema versions.
4. Distinguish activation from registration, retention from repeat sessions, and paid conversion from gross transactions. Do not substitute sessions for users without explanation.

## Challenge / acceptance
- **Challenge:** Introduce a conflicting stakeholder request or change activation metric definition. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Research-backed prioritization and falsifiable release metric survive the change. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** Unknown evidence remains UNKNOWN.
- **Stop/review:** No guaranteed adoption or unverified business uplift. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://developers.google.com/analytics/devguides/collection/ga4/events
- https://developers.google.com/analytics/devguides/collection/protocol/ga4/validating-events

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
