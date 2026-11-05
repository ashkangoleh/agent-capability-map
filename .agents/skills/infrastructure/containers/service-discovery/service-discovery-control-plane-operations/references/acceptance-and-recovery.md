# service-discovery-control-plane-operations: specialist evaluation and negative controls

Domain `infrastructure/containers/service-discovery`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Identify whether the system provides discovery, configuration, leader election or Kubernetes control-plane state.
2. Design quorum and failure domains; validate latency, disk fsync, snapshots and compaction.
3. Secure peer/client traffic with mTLS, ACLs and least-privilege registration tokens.
4. Tune health checks, deregistration, DNS TTL, stale reads and client retry to avoid herds.

## Challenge / acceptance
- **Challenge:** Lose a node, permission or control plane while applying a scoped change. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Actual target identity, SLO, rollback prerequisites and failure isolation are independently checked. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - Quorum loss makes writes unavailable; do not force-remove members without recovery plan.
- Slow disk or compaction destabilizes etcd.
- Stale DNS caches outlive deregistration.
- **Stop/review:** No destructive, credential or production control-plane changes without authorization. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://developer.hashicorp.com/consul/docs
- https://etcd.io/docs/
- https://coredns.io/manual/toc/

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
