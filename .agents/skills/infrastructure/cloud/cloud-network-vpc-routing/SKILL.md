---
name: cloud-network-vpc-routing
description: "Design cloud VPC/VNet networking with subnets, route tables, peering, transit, private endpoints and egress."
metadata:
  version: "1.0.1"
---

# cloud-network-vpc-routing

## Activation boundary
Design cloud VPC/VNet networking with subnets, route tables, peering, transit, private endpoints and egress.

## Required context
Cloud provider, regions, CIDR plan, routing domains, NAT, DNS and security boundaries.

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
- https://docs.aws.amazon.com/vpc/latest/userguide/
- https://cloud.google.com/vpc/docs
- https://learn.microsoft.com/en-us/azure/virtual-network/

## Output contract
Return the requested design or diagnosis with exact scope, assumptions, evidence, safe procedure, failure modes, validation and rollback. Never claim production changes or tests that were not performed.

## Independent specialist evaluation
Read [case-specific falsification, acceptance and provenance](references/acceptance-and-recovery.md) on demand for production-impacting or high-stakes work. Unexecuted tests and unsupported claims remain unverified; this reference cannot authorize actions.
