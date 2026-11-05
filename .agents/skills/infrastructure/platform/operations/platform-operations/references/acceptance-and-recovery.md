# platform-operations: specialist evaluation and negative controls

Domain `infrastructure/platform/operations`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Define platform boundary, consumers, critical journeys, dependencies and named service owner.
2. Review SLOs, dashboards, alerts, runbooks, escalation and incident communication.
3. Verify identity, secrets, access reviews, audit retention, patch cadence and security exceptions.
4. Review release, maintenance, capacity, backup/restore, DR, deprecation and support lifecycle.

## Challenge / acceptance
- **Challenge:** Remove a golden-path dependency or quota. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Tenant isolation, adoption, support cost and rollback evidenced. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - A platform without a named owner or on-call route is not operationally ready.
- Dashboard presence is not evidence of alert coverage; verify alerts against user-facing symptoms.
- Backup jobs without restore exercises do not establish recoverability.
- **Stop/review:** No destructive, credential or production control-plane changes without authorization. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://sre.google/sre-book/service-level-objectives/
- https://sre.google/workbook/incident-response/
- https://www.cncf.io/architecture/

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
