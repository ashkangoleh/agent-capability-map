# network-automation-sdn: specialist evaluation and negative controls

Domain `infrastructure/network-automation`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Reconcile devices, links, prefixes, roles and ownership in a source of truth.
2. Select supported NETCONF, RESTCONF, gNMI/gNOI, vendor API or CLI interfaces per device release.
3. Render version-controlled intent and validate schema, policy, dependencies and device syntax.
4. Deploy by failure domain with canaries, transactional commit where supported and concurrency limits.

## Challenge / acceptance
- **Challenge:** Lose a node, permission or control plane while applying a scoped change. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Actual target identity, SLO, rollback prerequisites and failure isolation are independently checked. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - Vendor model gaps can create incomplete configuration; test every hardware/OS family.
- Concurrent writers overwrite changes; enforce ownership or locks.
- Management-plane loss can strand automation; preserve console/OOB recovery.
- **Stop/review:** No destructive, credential or production control-plane changes without authorization. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://www.openconfig.net/
- https://docs.ansible.com/ansible/latest/network/
- https://docs.netbox.dev/

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
