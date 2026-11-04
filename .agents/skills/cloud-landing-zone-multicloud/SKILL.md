---
name: cloud-landing-zone-multicloud
description: "Build cloud landing zones with account/project/subscription boundaries, identity, network, logging and guardrails."
metadata:
  version: "1.0.0"
---

# cloud-landing-zone-multicloud

## Activation boundary
Build cloud landing zones with account/project/subscription boundaries, identity, network, logging and guardrails.

## Required context
Cloud provider, org structure, identity provider, regions, compliance, connectivity and ownership.

## Production procedure
1. Define account/project/subscription boundaries, region, CIDR plan, identity and service ownership.
2. Design routing, private connectivity, KMS, audit and policy guardrails together.
3. Use IaC plans and policy checks; isolate state and credentials per environment.
4. Model quotas, shared cost, egress, recovery and regional dependencies.
5. Test identity federation, route propagation, quota exhaustion and DR.

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
- https://docs.aws.amazon.com/prescriptive-guidance/latest/landing-zone-implementation/
- https://cloud.google.com/architecture/landing-zones

## Output contract
Return the requested design or diagnosis with exact scope, assumptions, evidence, safe procedure, failure modes, validation and rollback. Never claim production changes or tests that were not performed.
