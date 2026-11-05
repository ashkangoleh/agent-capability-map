---
name: network-firewall-segmentation
description: "Design network segmentation and firewall policy with least privilege, stateful flow reasoning and auditability."
metadata:
  version: "1.0.0"
---

# network-firewall-segmentation

## Activation boundary
Design network segmentation and firewall policy with least privilege, stateful flow reasoning and auditability.

## Required context
Zones, trust boundaries, flows, NAT, identity, rule ownership and change window.

## Production procedure
1. Draw the actual packet path and trust zones before changing routes or policies.
2. Inspect DNS, routing, MTU, NAT, TLS/SNI, proxies, conntrack and firewall state separately.
3. Validate control-plane convergence and data-plane reachability from both endpoints.
4. Use least-privilege rules, staged rollout and out-of-band recovery for network changes.
5. Test failover, asymmetric routes, MTU blackholes, certificate expiry and DNS cache behavior.

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
- https://www.nist.gov/cyberframework

## Output contract
Return the requested design or diagnosis with exact scope, assumptions, evidence, safe procedure, failure modes, validation and rollback. Never claim production changes or tests that were not performed.
