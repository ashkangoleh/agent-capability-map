# oci-infrastructure-operations: specialist evaluation and negative controls

Domain `infrastructure/cloud/providers`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Define compartment hierarchy, tags, delegated admin and policy inheritance.
2. Design VCNs, subnets, route tables, NSGs, DRGs, service gateways and hybrid links.
3. Use dynamic groups, resource principals and least privilege; avoid user API keys for workloads.
4. Enable Cloud Guard, audit, logging, Vault, backup and protected evidence retention.

## Challenge / acceptance
- **Challenge:** Remove a role or overload one region. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** No overbroad privilege, budget overrun or hidden cross-region dependence. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - Compartment policy inheritance can unexpectedly grant/deny; inspect effective policy.
- DRG routes and overlapping CIDRs can blackhole traffic.
- Dynamic-group rules must be tested against actual resource identity.
- **Stop/review:** No destructive, credential or production control-plane changes without authorization. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://docs.oracle.com/en/solutions/oci-landing-zones/
- https://docs.oracle.com/en-us/iaas/Content/GSG/Concepts/concepts.htm
- https://docs.oracle.com/en-us/iaas/Content/Security/Concepts/security.htm

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
