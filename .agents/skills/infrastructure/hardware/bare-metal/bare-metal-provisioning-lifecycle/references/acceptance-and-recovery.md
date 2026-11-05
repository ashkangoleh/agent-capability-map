# bare-metal-provisioning-lifecycle: specialist evaluation and negative controls

Domain `infrastructure/hardware/bare-metal`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Discover hardware through Redfish/IPMI and reconcile serial, model, NIC, disk, firmware and rack.
2. Design isolated provisioning network, boot chain, signed artifacts and temporary credentials.
3. Build immutable images with pinned packages, kernel, drivers and security baseline.
4. Provision canary cohorts; validate device health, enrollment, monitoring and convergence.

## Challenge / acceptance
- **Challenge:** Lose a node, permission or control plane while applying a scoped change. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Actual target identity, SLO, rollback prerequisites and failure isolation are independently checked. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - PXE/DHCP mistakes can reimage wrong host; require identity checks and authorization.
- Untrusted boot artifacts compromise fleet; verify signatures and Secure Boot.
- Firmware mismatch can break boot/network; test SKU matrix.
- **Stop/review:** No destructive, credential or production control-plane changes without authorization. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://maas.io/docs
- https://metal3.io/documentation.html
- https://docs.tinkerbell.org/

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
