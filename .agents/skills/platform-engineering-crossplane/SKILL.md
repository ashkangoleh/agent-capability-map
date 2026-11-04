---
name: platform-engineering-crossplane
description: "Design Crossplane compositions and claims as a Kubernetes-native infrastructure control plane."
metadata:
  version: "1.0.0"
---

# platform-engineering-crossplane

## Activation boundary
Design Crossplane compositions and claims as a Kubernetes-native infrastructure control plane.

## Required context
Crossplane version, providers, XRDs, compositions, connection secrets and cloud identity.

## Production procedure
1. Define developer personas, paved paths, service ownership and supported golden paths.
2. Separate control plane from workload plane; version templates and platform APIs.
3. Use least-privilege identities, policy guardrails and self-service audit.
4. Measure lead time, failure rate, adoption and platform support burden.
5. Test provider outage, reconciliation loops, template upgrades and tenant isolation.

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
- https://docs.crossplane.io/

## Output contract
Return the requested design or diagnosis with exact scope, assumptions, evidence, safe procedure, failure modes, validation and rollback. Never claim production changes or tests that were not performed.
