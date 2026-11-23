# marketing-measurement-attribution: specialist evaluation and negative controls

Domain `marketing/marketing-analytics`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Define channel-level decisions and causal questions. Separate acquisition/source reporting, conversion tracking and incremental lift estimation.
2. Define event contracts with source, event time, campaign identifiers, UTM conventions, deduplication, session/user linkage and consent gating.
3. Verify current platform measurement APIs, recommended versus custom events, event parameter requirements and debugging behavior from official docs.
4. Reconcile tracked conversions to orders/transactions, accounting or backend events, documenting refunds, attribution windows, cross-device gaps and unconsented traffic.

## Challenge / acceptance
- **Challenge:** Shift audience targeting, attribution window or spend cap. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Conversion metrics are deduplicated, holdouts and unit economics evaluated with consent. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** Unknown evidence remains UNKNOWN.
- **Stop/review:** No guaranteed reach, ROAS or sensitive audience inference. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

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
