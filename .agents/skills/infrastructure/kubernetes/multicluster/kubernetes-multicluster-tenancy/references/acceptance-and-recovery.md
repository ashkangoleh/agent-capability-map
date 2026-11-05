# kubernetes-multicluster-tenancy: specialist evaluation and negative controls

Domain `infrastructure/kubernetes/multicluster`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Choose cluster boundaries from blast radius, regulation, ownership and operating cost.
2. Standardize API versions, add-ons, CNI/CSI, identity, admission, observability and backup.
3. Define tenant isolation across namespaces, RBAC, network policy, quotas, node pools and secrets.
4. Design placement, traffic failover, service discovery and data locality without assuming global ordering.

## Challenge / acceptance
- **Challenge:** Inject unavailable node, admission denial and stale rollout. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Workload health and availability remain within verified SLO; rollback tested. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - Fleet-wide policy rollout multiplies mistakes; stage by cohort.
- Cross-cluster DNS/networking creates common-mode dependencies.
- Management-plane outage can stall reconciliation; document manual recovery.
- **Stop/review:** No destructive, credential or production control-plane changes without authorization. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://cluster-api.sigs.k8s.io/
- https://kubernetes.io/docs/concepts/cluster-administration/
- https://kubernetes.io/docs/concepts/security/

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
