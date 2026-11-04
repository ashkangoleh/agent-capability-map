---
name: redpanda-event-streaming
description: "Operate Redpanda Kafka-API-compatible streaming clusters with Raft replication, tiered storage, consumer recovery and migration controls."
license: Proprietary
metadata:
  version: "1.1.0"
---

# redpanda-event-streaming

## Activation boundary
Use for Redpanda cluster/client operations. Kafka API compatibility does not imply identical support for every broker, admin or ecosystem feature.

## Required context
Redpanda release; topology; rack/zone layout; partitions/replication; client versions; tiered storage; workload and retention.

## Production procedure
1. Build a feature compatibility matrix for required Kafka APIs, transactions, Connect, Streams and ACLs against the deployed release.
2. Design partitions, replication, rack awareness and retention from throughput, consumer parallelism and recovery objectives.
3. Validate Raft quorum, leader distribution, disk capacity and network latency across failure domains.
4. Configure tiered storage/cache and remote retention separately; verify remote restore and object lifecycle.
5. Tune producer batching, compression, acknowledgements and idempotence from durability/latency goals.
6. Monitor consumer lag, leadership, under-replicated partitions, disk, remote storage and request latency.
7. Plan Kafka migration with topic/config export, offset policy, dual-run prevention and consumer restart behavior.

## Failure modes and recovery
- API mismatch: pin supported clients or remove unsupported feature dependency.
- Quorum loss: restore replicas and verify leadership before full write load.
- Tiered fetch delay: inspect remote access and cache hit rate.
- Consumer lag after migration: validate offset and partition mapping.
- Disk exhaustion: enforce retention/tiering before replica recovery is starved.

## Validation and acceptance
- Test broker/zone failure, leader election, consumer restart, tiered fetch, retention expiry and rolling upgrade.
- Measure produce/fetch p99, replication lag, consumer lag, storage and recovery time.

## Output contract
Return API compatibility matrix, topology, retention plan, migration runbook and recovery evidence.

## Official or primary references
- https://docs.redpanda.com/
- https://docs.redpanda.com/current/manage/cluster-maintenance/rolling-upgrades/
