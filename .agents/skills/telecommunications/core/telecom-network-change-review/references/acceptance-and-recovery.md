# telecom-network-change-review: specialist evaluation and negative controls

Domain `telecommunications/core`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Identify network topology, customer-impacting paths, control plane and data plane separately.
2. Verify actual standard release and vendor-specific implementation before using protocol assumptions.
3. Inspect addressing, routes, redundancy, signaling and capacity limits from verified telemetry.
4. Specify proposed change with affected links/services, expected convergence, fallback and monitoring.

## Challenge / acceptance
- **Challenge:** Simulate link loss, latency spike or changed subscriber authorization. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Service availability, interoperability and privacy metrics meet explicit test criteria. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** Unknown evidence remains UNKNOWN.
- **Stop/review:** No carrier network changes without permission and incident rollback. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://www.3gpp.org/specifications
- https://www.itu.int/en/ITU-T/Pages/default.aspx

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
