# aws-infrastructure-operations: specialist evaluation and negative controls

Domain `infrastructure/cloud/providers`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Inspect account/OUs, SCP inheritance, delegated admins and break-glass before account changes.
2. Design VPC/subnet/route boundaries, transit, private endpoints, egress and DNS across accounts.
3. Use federation, role assumption and workload roles; avoid long-lived keys and broad admin grants.
4. Centralize CloudTrail, Config, security findings, KMS, backup and protected log retention.

## Challenge / acceptance
- **Challenge:** Remove a role or overload one region. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** No overbroad privilege, budget overrun or hidden cross-region dependence. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - SCP/IAM changes can lock out administrators; preserve tested break-glass.
- Overlapping CIDRs or route propagation can break hybrid connectivity.
- Central log permissions can expose or erase audit evidence.
- **Stop/review:** No destructive, credential or production control-plane changes without authorization. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html
- https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html
- https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
