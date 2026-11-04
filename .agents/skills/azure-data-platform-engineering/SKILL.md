---
name: azure-data-platform-engineering
description: "Design Azure data platforms across ADLS Gen2, Data Factory, Fabric, Synapse and Event Hubs."
license: Proprietary
metadata:
  version: "1.1.0"
---

# azure-data-platform-engineering

## Activation boundary
Use for Azure-native data platform architecture and service operations.

## Required context
Subscription/tenant; ADLS account; identity; Data Factory/Fabric/Synapse; Event Hubs; region; network and governance.

## Production procedure
1. Define tenant/subscription and managed identity boundaries; prefer workload identity over stored secrets.
2. Design ADLS Gen2 hierarchical namespace, ACLs, lifecycle, private endpoints and zone layout.
3. Choose Data Factory for connector/orchestration, Fabric or Synapse for managed analytics, and Event Hubs for event transport.
4. Validate Event Hubs partitioning, consumer groups, retention and checkpoint ownership.
5. Define catalog/governance with Purview/Fabric capabilities; distinguish catalog metadata from storage ACLs.
6. Set network isolation, private endpoints, Key Vault, diagnostic settings and policy.
7. Model capacity, CU/warehouse sizing, data movement, egress and idle cost.

## Failure modes and recovery
- ADLS ACL mismatch: test both RBAC and POSIX ACL evaluation.
- Managed identity failure: verify role assignment scope and token audience.
- Event Hubs checkpoint loss: preserve checkpoint store and define replay.
- Data Factory retry duplicates: make sink idempotent.
- Fabric capacity throttling: monitor CU saturation and workload isolation.

## Validation and acceptance
- Test identity and ACLs, private endpoint access, Event Hubs replay, pipeline restart and restore.
- Measure pipeline latency, capacity throttling, data movement and cost.

## Output contract
Return Azure service topology, identity/network/governance model, workload placement and recovery plan.

## Official or primary references
- https://learn.microsoft.com/azure/architecture/data-guide/
- https://learn.microsoft.com/azure/storage/blobs/data-lake-storage-introduction
- https://learn.microsoft.com/azure/event-hubs/event-hubs-about
