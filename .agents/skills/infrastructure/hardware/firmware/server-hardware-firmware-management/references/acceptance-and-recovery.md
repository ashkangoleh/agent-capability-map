# server-hardware-firmware-management: specialist evaluation and negative controls

Domain `infrastructure/hardware/firmware`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Inventory firmware by exact SKU, board, NIC/HBA and accelerator.
2. Review release notes, security advisories and compatibility; avoid unsupported component mixes.
3. Use authenticated Redfish/vendor tooling, isolate BMC network and rotate unique credentials.
4. Stage updates by cohort with power redundancy, workload evacuation and console recovery.

## Challenge / acceptance
- **Challenge:** Lose a node, permission or control plane while applying a scoped change. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Actual target identity, SLO, rollback prerequisites and failure isolation are independently checked. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - Interrupted firmware update can brick hardware; require supported recovery.
- BMC is a high-privilege attack surface; isolate and audit.
- NIC/HBA firmware changes driver/link behavior; validate compatibility.
- **Stop/review:** No destructive, credential or production control-plane changes without authorization. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://www.dmtf.org/standards/redfish
- https://uefi.org/specifications
- https://www.opencompute.org/

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
