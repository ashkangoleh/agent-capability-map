# cloud-architecture-reference-design: specialist evaluation and negative controls

Domain `infrastructure/cloud/architecture`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Translate requirements into measurable availability, latency, recovery, security, sovereignty, cost and operability attributes.
2. Choose tenancy, region/AZ, connectivity, DNS, identity federation, encryption and audit architecture.
3. Map shared services and failure domains; document provider-native versus portable components and lock-in intentionally.
4. Design observability, backup, patching, quotas, capacity, FinOps and incident ownership as first-class capabilities.

## Challenge / acceptance
- **Challenge:** Remove a role or overload one region. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** No overbroad privilege, budget overrun or hidden cross-region dependence. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - Multi-cloud does not automatically improve resilience; shared identity/DNS/control planes can remain common-mode.
- Abstraction can erase provider capabilities while adding operational complexity.
- Cross-region replication is not proof of recoverability; test application-consistent restore.
- **Stop/review:** No destructive, credential or production control-plane changes without authorization. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html
- https://learn.microsoft.com/azure/well-architected/
- https://cloud.google.com/architecture/framework

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
