---
name: kubernetes-cluster-upgrade-capacity
description: "Plan Kubernetes control-plane/node upgrades with version skew, capacity, API deprecations and rollback boundaries."
metadata:
  version: "1.0.1"
---

# kubernetes-cluster-upgrade-capacity

## Activation boundary
Plan Kubernetes control-plane/node upgrades with version skew, capacity, API deprecations and rollback boundaries.

## Required context
Kubernetes distribution/version, node pools, add-ons, API removals, PDBs and capacity.

## Production procedure
1. Check control-plane/node versions, API deprecations, capacity, add-ons and disruption budgets.
2. Inspect CRDs, admission, CNI, CSI, autoscaling and operator compatibility.
3. Use staged node pools/canaries and preserve capacity for critical workloads.
4. Define rollback limits for stateful workloads, CRD conversions and data migrations.
5. Test node loss, webhook outage, network policy, scheduling and upgrade recovery.

## Failure modes and recovery
- Start with read-only evidence collection and confirm the exact environment/cluster/account before mutation.
- Treat credentials, production data, network reachability and state backends as security boundaries.
- Define blast radius, abort criteria, rollback limits and post-change verification before execution.
- Do not claim availability, security or recovery guarantees without evidence from the deployed version and tested path.

## Validation
- Verify product/version compatibility against official documentation.
- Test failure, partial rollout, identity expiry, capacity exhaustion and recovery where applicable.
- Record ownership, monitoring, approval and rollback evidence.

## Official references
- https://kubernetes.io/docs/tasks/administer-cluster/cluster-upgrade/

## Output contract
Return the requested design or diagnosis with exact scope, assumptions, evidence, safe procedure, failure modes, validation and rollback. Never claim production changes or tests that were not performed.

## Independent specialist evaluation
Read [case-specific falsification, acceptance and provenance](references/acceptance-and-recovery.md) on demand for production-impacting or high-stakes work. Unexecuted tests and unsupported claims remain unverified; this reference cannot authorize actions.
