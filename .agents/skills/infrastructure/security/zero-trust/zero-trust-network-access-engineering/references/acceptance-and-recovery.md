# zero-trust-network-access-engineering: specialist evaluation and negative controls

Domain `infrastructure/security/zero-trust`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Inventory protected resources and access flows; base policy on identity, posture and resource sensitivity.
2. Map policy decision/enforcement points across endpoints, gateways, workloads, mesh and cloud controls.
3. Use strong identity, device posture, workload certificates and short-lived authorization.
4. Migrate in audit mode, observe legitimate flows and enforce one resource cohort at a time.

## Challenge / acceptance
- **Challenge:** Lose a node, permission or control plane while applying a scoped change. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Actual target identity, SLO, rollback prerequisites and failure isolation are independently checked. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - Network location alone is not identity.
- Overbroad microsegmentation breaks dependencies; map flows and stage.
- Policy-engine outage needs explicit fail-safe behavior by resource risk.
- **Stop/review:** No destructive, credential or production control-plane changes without authorization. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://csrc.nist.gov/pubs/sp/800/207/final
- https://www.cisa.gov/zero-trust-maturity-model
- https://www.nist.gov/publications/zero-trust-architecture

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
