# edge-compute-fleet-operations: specialist evaluation and negative controls

Domain `infrastructure/edge/compute`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Classify sites by connectivity, power, compute, storage, physical security and recovery access.
2. Choose lightweight runtime/Kubernetes only where orchestration benefits justify lifecycle cost.
3. Design fleet identity, enrollment, signed updates, staged OTA, local rollback and secure decommission.
4. Buffer telemetry/events during disconnection with bounded retention, clock handling and replay dedup.

## Challenge / acceptance
- **Challenge:** Lose a node, permission or control plane while applying a scoped change. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Actual target identity, SLO, rollback prerequisites and failure isolation are independently checked. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - Offline sites retain stale desired state; define bounded autonomy.
- Power loss during OTA can brick devices; use atomic/A-B updates where supported.
- Physical compromise exposes local credentials; use hardware-backed identity if possible.
- **Stop/review:** No destructive, credential or production control-plane changes without authorization. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://docs.k3s.io/
- https://kubeedge.io/docs/
- https://www.cncf.io/projects/

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
