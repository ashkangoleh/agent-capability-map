# infrastructure-architecture-decision-review: specialist evaluation and negative controls

Domain `infrastructure/architecture/review`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Translate requirements into measurable availability, latency, throughput, recovery, security, sovereignty and cost attributes.
2. Map dependencies across identity, DNS, network, compute, storage, control planes, telemetry and on-call ownership.
3. Compare a simpler alternative and a credible scale/resilience option including migration and lock-in costs.
4. Review provisioning, upgrades, patching, capacity, backup, incident response, decommission and exit path.

## Challenge / acceptance
- **Challenge:** Lose a node, permission or control plane while applying a scoped change. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Actual target identity, SLO, rollback prerequisites and failure isolation are independently checked. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - Diagrams omit shared dependencies; validate actual control planes and failure paths.
- HA claims without failure testing are design assumptions.
- Abstraction adds operations cost; require concrete need.
- **Stop/review:** No destructive, credential or production control-plane changes without authorization. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://www.cncf.io/architecture/
- https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html
- https://sre.google/sre-book/

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
