---
name: kubernetes-cni-ebpf-operations
description: "Operate Kubernetes CNI and eBPF networking with IPAM, routing, policy, MTU and datapath diagnostics."
metadata:
  version: "1.0.0"
---

# kubernetes-cni-ebpf-operations

## Activation boundary
Operate Kubernetes CNI and eBPF networking with IPAM, routing, policy, MTU and datapath diagnostics.

## Required context
CNI/version, kernel, IPAM mode, routing mode, kube-proxy replacement and network policy.

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
- https://docs.cilium.io/en/stable/network/concepts/

## Output contract
Return the requested design or diagnosis with exact scope, assumptions, evidence, safe procedure, failure modes, validation and rollback. Never claim production changes or tests that were not performed.
