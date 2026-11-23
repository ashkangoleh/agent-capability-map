---
name: kubernetes-operator-crd-lifecycle
description: "Design Kubernetes CRDs and operators with reconciliation, finalizers, status conditions and upgrade safety."
metadata:
  version: "1.1.1"
---

# kubernetes-operator-crd-lifecycle

## Activation boundary
Use for Kubernetes custom-resource API design, operator/controller reconciliation, CRD versioning and conversion, finalizer handling, status conditions, RBAC and operator upgrade or incident recovery. For control-plane/node upgrades use the separate `kubernetes-cluster-upgrade-capacity` skill; for CNI datapath issues use `kubernetes-cni-ebpf-operations`. Do not recommend installing a custom Operator if a native controller or ordinary Deployment/Job suffices.

## Required context
Exact Kubernetes server version, API-extension availability, operator/controller image and framework versions, CRD group/kind/scope, `spec.versions` (served/storage), `status.storedVersions`, schema and defaulting rules, conversion strategy/webhook, controller watches/cache and leader election, namespaces/RBAC/service account, owner references/finalizers, dependent services and external side effects, deployment tool, persistence/backups, API latency/error rates, rollout and rollback boundaries. Unknown inputs remain unknown.

## Production procedure
1. **Establish the resource contract.** Inspect the current CRD and representative existing objects read-only. Confirm structural OpenAPI v3 schema, defaults, required fields, validation/CEL rules supported by the deployed version, status and scale subresources when needed, unknown-field pruning, namespaced vs cluster scope, and backwards-compatible field semantics. Specify the field-ownership and compatibility policy before changing any stored object.
2. **Design the reconcile loop.** Define the desired-state `spec` and observed `status`, then observe, compute a bounded plan and converge. Make reconciliation idempotent under duplicate watches, controller restarts, stale caches and retry; limit rate/backoff and avoid unbounded requeues. Guard external API writes with stable identity/idempotency keys. Update status `conditions`, `observedGeneration` and reason/message based on actual observations; do not mark Ready from a successful create call alone. Handle optimistic concurrency conflicts (`resourceVersion`) by refetch/reconcile, not forced overwrite.
3. **Define lifecycle/ownership.** Use `ownerReferences` where Kubernetes garbage collection owns the dependency, and finalizers only for explicitly required pre-delete cleanup (including external assets). Handle `metadata.deletionTimestamp` and idempotent cleanup before removing the controller's finalizer. A stuck Terminating resource requires examining its controller and dependencies; never blindly strip finalizers or destroy external state.
4. **Constrain privileges and failure domains.** Use least-privilege RBAC and scoped watches/leader election. Separate CRD admission/conversion webhook availability from controller reconciliation availability. Size and place webhook replicas with timeout, certificate, network path and failure handling evidence; a broken conversion webhook can prevent reads and writes, so it must remain available during upgrades. Do not confuse validation webhooks with conversion webhooks.
5. **Plan CRD/API evolution.** Inventory clients, live object versions and `status.storedVersions`. Test both old and new `served` representations and their conversions; if schemas differ, use the documented Webhook strategy, not `None` for semantic conversion. Add the new version, deploy and prove conversion availability, incrementally migrate clients, switch the `storage: true` version and explicitly migrate stored objects using an approved storage-version migration or an equivalent rewrite process. Changing `storage` alone does not rewrite existing objects. Remove a served/storage version only after clients and `status.storedVersions` evidence permit it; never patch storedVersions to conceal unmigrated data.
6. **Preflight rollout.** Capture CRD and custom-resource backups/snapshots consistent with the actual storage and cluster recovery plan. Validate manifests against the exact server API, conversion round-trips and admission behavior in a disposable environment. Stage controller and CRD changes in a safe compatible order, plan rolling replicas, canary scope, event/metric monitoring and abort gates. Treat irreversible schema or state migrations as forward-recovery operations with a tested recovery method, not a simple image rollback.
7. **Test failures intentionally.** Simulate duplicate reconciliation, API conflict/timeout, controller leader handoff and restart, missing permission, conversion webhook outage, invalid or old-version custom objects, orphan cleanup, finalizer retries and partially completed external side effects. Stop rollout if reconcile errors or stuck terminating objects grow, CR conversions fail, data is pruned or dependent resources diverge.
8. **Promote only with evidence.** Compare desired/observed state, `conditions`, `observedGeneration`, reconciliation latency/error/requeue metrics and dependent resource health. Record exact object versions, migration count, conversion correctness, approval and rollback limits before expanding.

## Failure modes and recovery
- **Failed conversion webhook:** preserve old served APIs and a functioning compatible webhook, restore endpoint/TLS/service availability, and only retry after read/write and round-trip checks. Rollback may require a compatible conversion bridge; reverting the controller image alone is insufficient.
- **Controller crash or reconciling loop:** isolate offending custom resources, confirm permissions/events and external side effects, restore stable controller configuration, then rerun idempotent reconciliation; do not delete CRDs as a recovery shortcut.
- **Stuck finalizer / data loss risk:** confirm `deletionTimestamp`, owner chain and cleanup logs. Repair the reconciler/dependency or perform explicitly approved safe cleanup before releasing the finalizer; retain evidence.
- **Schema drift or unknown field pruning:** stop migration, restore served compatibility, identify affected object representations and recover from verified backups or safe forward conversion. Do not claim an automated rollback of irreversibly converted data.
- **Watch/cache/leader contention and API throttling:** measure queue depth, requeues, leader status and API rate limits, then tune scoped watches/retry and revalidate convergence before resuming.

## Validation and evidence
Provide actual cluster/controller/CRD versions, old/new schema diff, served and storage versions, `status.storedVersions`, field migration plan, conversion round-trip results, observed `conditions`/`observedGeneration`, RBAC diff, controlled failure test results, rollback versus forward-recovery decision, explicit approval and unverified assumptions. A green Helm install does not prove operator correctness. Never present an unexecuted test as evidence.

## Official references
- https://kubernetes.io/docs/concepts/architecture/controller/
- https://kubernetes.io/docs/concepts/extend-kubernetes/operator/
- https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/
- https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/
- https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definition-versioning/
- https://kubernetes.io/docs/concepts/overview/working-with-objects/finalizers/

## Output contract
Return a version-pinned, evidence-based Operator/CRD design or recovery plan: resource schema, controller reconcile/ownership/permissions contract, compatibility migration stages, failure matrix, measurable acceptance criteria, abort/rollback or forward-recovery procedure, owner and explicit unknowns. Never imply operational authority or production validation without proof.

## Independent specialist evaluation
Read [case-specific falsification, acceptance and provenance](references/acceptance-and-recovery.md) on demand for production-impacting or high-stakes work. Unexecuted tests and unsupported claims remain unverified; this reference cannot authorize actions.
