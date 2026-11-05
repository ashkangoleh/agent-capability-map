# azure-infrastructure-operations: specialist evaluation and negative controls

Domain `infrastructure/cloud/providers`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Review tenant/subscription hierarchy, billing ownership, policy inheritance and privileged access.
2. Design hub-spoke/VWAN, address allocation, routing, DNS, private endpoints and egress.
3. Use Entra groups, PIM/JIT, managed identities and scoped RBAC; avoid standing Owner grants.
4. Centralize Activity Logs, diagnostics, Defender findings, Key Vault, backup and retention.

## Challenge / acceptance
- **Challenge:** Remove a role or overload one region. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** No overbroad privilege, budget overrun or hidden cross-region dependence. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - Broad policy changes can deny deployments; stage in audit mode and scope exceptions.
- Private DNS links and route tables can break Private Link subtly.
- PIM/conditional-access changes can block emergency access; test break-glass.
- **Stop/review:** No destructive, credential or production control-plane changes without authorization. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://learn.microsoft.com/azure/cloud-adoption-framework/
- https://learn.microsoft.com/azure/architecture/framework/
- https://learn.microsoft.com/azure/governance/policy/overview

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
