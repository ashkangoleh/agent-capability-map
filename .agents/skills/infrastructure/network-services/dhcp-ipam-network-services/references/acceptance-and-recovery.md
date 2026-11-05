# dhcp-ipam-network-services: specialist evaluation and negative controls

Domain `infrastructure/network-services`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Establish a source of truth for prefixes, VLANs, reservations, gateways, DHCP options and ownership.
2. Design scope boundaries, lease duration, relay, failover and IPv6 SLAAC/DHCPv6 responsibilities.
3. Protect DHCP with snooping/guarding and trusted relays; restrict dynamic DNS update credentials.
4. Validate IPAM-to-DHCP/DNS automation with dry-run diffs and conflict detection.

## Challenge / acceptance
- **Challenge:** Lose a node, permission or control plane while applying a scoped change. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Actual target identity, SLO, rollback prerequisites and failure isolation are independently checked. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - Stale IPAM causes overlapping allocations; reconcile live leases and ARP/ND first.
- Relay/firewall errors can create partial site outages; test each routed segment.
- Inconsistent failover state can allocate duplicates.
- **Stop/review:** No destructive, credential or production control-plane changes without authorization. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://kea.readthedocs.io/
- https://docs.netbox.dev/
- https://www.rfc-editor.org/rfc/rfc2131

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
