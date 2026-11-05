# network-switching-enterprise-routing: specialist evaluation and negative controls

Domain `infrastructure/network-switching`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Map actual forwarding paths and inventory VLANs, trunks, SVIs, VRFs, port-channels and gateways.
2. Validate STP root, loop protections, storm control and LACP member consistency.
3. Review OSPF/IS-IS areas, route filtering, redistribution, ECMP and EVPN/VXLAN control/data plane.
4. Check MTU end to end including overlays, storage and jumbo-frame dependencies.

## Challenge / acceptance
- **Challenge:** Lose a node, permission or control plane while applying a scoped change. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Actual target identity, SLO, rollback prerequisites and failure isolation are independently checked. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - Trunk VLAN mismatch can isolate subsets of hosts.
- STP/LACP changes can create loops or blackholes; preserve OOB access.
- Overlay MTU mismatch often causes selective large-packet failure.
- **Stop/review:** No destructive, credential or production control-plane changes without authorization. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://www.rfc-editor.org/rfc/rfc2328
- https://www.rfc-editor.org/rfc/rfc7432
- https://www.rfc-editor.org/rfc/rfc7348

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
