# os-fleet-patching-compliance: specialist evaluation and negative controls

Domain `infrastructure/compute/os-fleet`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Inventory hosts by role, OS, kernel, driver dependencies and criticality.
2. Review vendor advisories and package changelogs; separate security, kernel and firmware changes.
3. Use canary rings, signed packages and reproducible manifests; stage reboots around quorum and workload constraints.
4. Preserve console/OOB access, backups and known-good boot entries before kernel or driver changes.

## Challenge / acceptance
- **Challenge:** Lose a node, permission or control plane while applying a scoped change. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Actual target identity, SLO, rollback prerequisites and failure isolation are independently checked. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - Successful package installation does not prove the new kernel booted.
- Repository drift creates non-reproducible fleets; pin and record package sources.
- Remote access can disappear after network, firewall or driver changes; preserve console recovery.
- **Stop/review:** No destructive, credential or production control-plane changes without authorization. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://ubuntu.com/server/docs
- https://docs.redhat.com/
- https://learn.microsoft.com/windows-server/

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
