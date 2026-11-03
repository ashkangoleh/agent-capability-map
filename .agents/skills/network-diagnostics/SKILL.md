---
name: network-diagnostics
description: Diagnose DNS, routing, TCP, TLS, proxy, firewall, load-balancer and connectivity failures using safe layer-by-layer network evidence and reproducible tests.
license: Proprietary
metadata:
  version: "1.0.0"
---

# Network troubleshooting

## Activate
Use when the requested deliverable is to diagnose reachability, name resolution, latency, handshake failures, routing or security filtering. Do not activate for generic Kubernetes rollout or app-code debugging unless network evidence points here.

## Procedure
1. Establish client and destination scope, environment, protocol, port, expected route, proxy policy, permitted tests and blast radius.
2. Identify the failure layer: DNS -> route -> transport -> TLS -> HTTP/application. Do not conflate HTTP 503, a proxy CONNECT failure, and a TCP timeout.
3. Prefer read-only evidence: resolver results, route table, listener binding, firewall policy, network logs, connection traces and certificate chain.
4. Choose narrowly scoped diagnostic probes permitted by the operator. Avoid broad scans or configuration changes without approval.
5. Distinguish client-side, proxy, intermediate device, service mesh and destination failures with independent observations.
6. Give a falsifiable likely cause, next discriminating test, safe remediation, verification and rollback.

## Outputs
Symptom matrix, evidence per layer, root-cause confidence qualified by observed tests, commands scoped to the environment and a recovery plan. Never infer security policy from a single error code.

## Reference
https://www.rfc-editor.org/rfc/rfc9110
