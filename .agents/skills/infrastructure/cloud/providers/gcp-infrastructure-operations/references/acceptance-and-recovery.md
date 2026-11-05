# gcp-infrastructure-operations: specialist evaluation and negative controls

Domain `infrastructure/cloud/providers`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Design hierarchy and project boundaries with environment, billing and delegated administration.
2. Use groups, service accounts, workload identity federation and org policy; constrain key creation.
3. Design Shared VPC, subnets, Cloud NAT, Cloud Router, VPN/Interconnect and DNS forwarding.
4. Centralize Audit Logs, Security Command Center, KMS, asset inventory and policy findings.

## Challenge / acceptance
- **Challenge:** Remove a role or overload one region. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** No overbroad privilege, budget overrun or hidden cross-region dependence. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - Service-account key sprawl bypasses federation; detect and remove unused keys.
- Shared VPC permissions span host and service projects; verify both.
- VPC Service Controls can block APIs; stage enforcement from dry-run insights.
- **Stop/review:** No destructive, credential or production control-plane changes without authorization. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://cloud.google.com/architecture/landing-zones
- https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy
- https://cloud.google.com/docs/enterprise/best-practices-for-enterprise-organizations

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
