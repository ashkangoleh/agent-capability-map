# kubernetes-operator-crd-lifecycle: specialist evaluation and negative controls

Domain `infrastructure/containers-orchestration/kubernetes/operators-extensions`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. **Establish the resource contract.** Inspect the current CRD and representative existing objects read-only. Confirm structural OpenAPI v3 schema, defaults, required fields, validation/CEL rules supported by the deployed version, status and scale subresources when needed, unknown-field pruning, namespaced vs cluster scope, and backwards-compatible field semantics. Specify the field-ownership and compatibility policy before changing any stored object.
2. **Design the reconcile loop.** Define the desired-state `spec` and observed `status`, then observe, compute a bounded plan and converge. Make reconciliation idempotent under duplicate watches, controller restarts, stale caches and retry; limit rate/backoff and avoid unbounded requeues. Guard external API writes with stable identity/idempotency keys. Update status `conditions`, `observedGeneration` and reason/message based on actual observations; do not mark Ready from a successful create call alone. Handle optimistic concurrency conflicts (`resourceVersion`) by refetch/reconcile, not forced overwrite.
3. **Define lifecycle/ownership.** Use `ownerReferences` where Kubernetes garbage collection owns the dependency, and finalizers only for explicitly required pre-delete cleanup (including external assets). Handle `metadata.deletion

## Challenge / acceptance
- **Challenge:** Lose a node, permission or control plane while applying a scoped change. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Actual target identity, SLO, rollback prerequisites and failure isolation are independently checked. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - **Failed conversion webhook:** preserve old served APIs and a functioning compatible webhook, restore endpoint/TLS/service availability, and only retry after read/write and round-trip checks. Rollback may require a compatible conversion bridge; reverting the controller image alone is insufficient.
- **Controller crash or reconciling loop:** isolate offending custom resources, confirm permissions/events and external side effects, restore stable controller configuration, then rerun idempotent reconciliation; do not delete CRDs as a recovery shortcut.
- **Stuck finalizer / data loss risk:** confirm `deletionTimestamp`, owner chain and cleanup logs. Repair the reconciler/dependency or perform explicitly approved safe cleanup before releasing the finalizer; retain evidence.
- **Stop/review:** No destructive, credential or production control-plane changes without authorization. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://kubernetes.io/docs/concepts/architecture/controller/
- https://kubernetes.io/docs/concepts/extend-kubernetes/operator/
- https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/
- https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/
- https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definition-versioning/
- https://kubernetes.io/docs/concepts/overview/working-with-objects/finalizers/

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
