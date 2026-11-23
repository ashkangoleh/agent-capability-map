# cloud-network-vpc-routing: specialist evaluation and negative controls

Domain `infrastructure/cloud`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Define account/project/subscription boundaries, region, CIDR plan, identity and service ownership.
2. Design routing, private connectivity, KMS, audit and policy guardrails together.
3. Use IaC plans and policy checks; isolate state and credentials per environment.
4. Model quotas, shared cost, egress, recovery and regional dependencies.

## Challenge / acceptance
- **Challenge:** Remove a role or overload one region. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** No overbroad privilege, budget overrun or hidden cross-region dependence. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - Start with read-only evidence collection and confirm the exact environment/cluster/account before mutation.
- Treat credentials, production data, network reachability and state backends as security boundaries.
- Define blast radius, abort criteria, rollback limits and post-change verification before execution.
- **Stop/review:** No destructive, credential or production control-plane changes without authorization. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://docs.aws.amazon.com/vpc/latest/userguide/
- https://cloud.google.com/vpc/docs
- https://learn.microsoft.com/en-us/azure/virtual-network/

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
