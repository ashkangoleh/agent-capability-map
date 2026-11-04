---
name: service-mesh-istio-operations
description: "Operate Istio service mesh traffic, mTLS, authorization, telemetry and sidecar/ambient lifecycle."
metadata:
  version: "1.0.0"
---

# service-mesh-istio-operations

## Activation boundary
Operate Istio service mesh traffic, mTLS, authorization, telemetry and sidecar/ambient lifecycle.

## Required context
Istio release, data plane mode, gateways, certificates, policies and service topology.

## Production procedure
1. Map traffic path, gateways, sidecar/ambient mode, certificates and control-plane versions.
2. Define mTLS, authorization, retries, timeouts, circuit breaking and telemetry boundaries.
3. Roll out policies incrementally and inspect proxy configuration and xDS health.
4. Avoid retry amplification and validate application-level idempotency.
5. Test certificate rotation, control-plane outage, gateway failure and bypass routes.

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
- https://istio.io/latest/docs/concepts/

## Output contract
Return the requested design or diagnosis with exact scope, assumptions, evidence, safe procedure, failure modes, validation and rollback. Never claim production changes or tests that were not performed.
