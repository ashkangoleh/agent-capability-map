# configuration-management-puppet-chef-salt: specialist evaluation and negative controls

Domain `infrastructure/iac/configuration-management`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Define desired state, ownership and dependencies; separate provisioning, configuration and app deployment.
2. Choose agent/pull/push model based on scale, offline tolerance and control-plane availability.
3. Make resources idempotent, pin modules/cookbooks/formulas and test OS/version matrices.
4. Separate secrets from manifests and secure agent/control-plane communication.

## Challenge / acceptance
- **Challenge:** Lose a node, permission or control plane while applying a scoped change. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Actual target identity, SLO, rollback prerequisites and failure isolation are independently checked. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - Non-idempotent resources cause repeated restarts and drift.
- Controller outage can stall compliance; document local behavior and recovery.
- Unpinned dependencies make builds non-reproducible.
- **Stop/review:** No destructive, credential or production control-plane changes without authorization. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://www.puppet.com/docs
- https://docs.chef.io/
- https://docs.saltproject.io/

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
