# kubernetes-rollout-safety: specialist evaluation and negative controls

Domain `infrastructure/kubernetes/rollout`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Start read-only. Confirm cluster, namespace, current release, exact manifest diff, dependencies and RBAC; never assume an environment from prior messages.
2. Inspect strategy, maxSurge/maxUnavailable, readiness/liveness/startup probes, resource requests, quotas, PDB, topology constraints, secrets and schema migrations.
3. Distinguish Deployment revision rollback from rollback of databases, config outside Pod templates, or other irreversible side effects.
4. Set preflight gates: validated YAML and rendered Helm manifests, policy checks, image provenance, baseline health, backup and recovery capability.

## Challenge / acceptance
- **Challenge:** Inject unavailable node, admission denial and stale rollout. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Workload health and availability remain within verified SLO; rollback tested. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** Unknown evidence remains UNKNOWN.
- **Stop/review:** No destructive, credential or production control-plane changes without authorization. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
- https://helm.sh/docs/helm/helm_upgrade/
- https://kubernetes.io/docs/concepts/configuration/liveness-readiness-startup-probes/

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
