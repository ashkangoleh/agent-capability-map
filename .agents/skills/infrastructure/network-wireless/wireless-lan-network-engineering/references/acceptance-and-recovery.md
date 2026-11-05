# wireless-lan-network-engineering: specialist evaluation and negative controls

Domain `infrastructure/network-wireless`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Use RF survey and interference evidence to design channel width, power, AP placement and density.
2. Separate corporate, guest, IoT and management access with explicit segmentation and client isolation.
3. Design WPA3/Enterprise and 802.1X EAP with redundant RADIUS, certificate lifecycle and identity mapping.
4. Tune roaming, band steering, airtime fairness, multicast and QoS using observed client behavior.

## Challenge / acceptance
- **Challenge:** Lose a node, permission or control plane while applying a scoped change. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Actual target identity, SLO, rollback prerequisites and failure isolation are independently checked. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - Poor RF cannot be fixed by adding SSIDs; reassess co-channel interference and density.
- Expired certificates or RADIUS outage can cause mass auth failure; test redundancy and alert on expiry.
- Legacy IoT clients must be isolated, not allowed to weaken corporate WLAN.
- **Stop/review:** No destructive, credential or production control-plane changes without authorization. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://www.wi-fi.org/discover-wi-fi/security
- https://www.rfc-editor.org/rfc/rfc3748
- https://www.cisco.com/c/en/us/solutions/enterprise-networks/what-is-wireless.html

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
