# storage-san-nas-nvmeof: specialist evaluation and negative controls

Domain `infrastructure/storage-engineering/advanced-storage`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Classify I/O pattern, latency, throughput, queue depth and consistency needs.
2. Design redundant fabrics, zoning, LUN masking and multipath across failure domains.
3. Validate HBA/NIC firmware, driver, kernel, ALUA/path policy and protocol compatibility.
4. Monitor latency, queue depth, path errors, cache, capacity, rebuild and replication lag.

## Challenge / acceptance
- **Challenge:** Lose a node, permission or control plane while applying a scoped change. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Actual target identity, SLO, rollback prerequisites and failure isolation are independently checked. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - Wrong multipath settings cause duplicate I/O or path flapping.
- Zoning/ACL mistakes expose or disconnect LUNs.
- NVMe-oF depends on network and NUMA topology.
- **Stop/review:** No destructive, credential or production control-plane changes without authorization. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://www.snia.org/education/technical_resources
- https://nvmexpress.org/specifications/
- https://docs.netapp.com/

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
