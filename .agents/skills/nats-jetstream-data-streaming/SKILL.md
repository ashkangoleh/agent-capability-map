---
name: nats-jetstream-data-streaming
description: "Operate NATS JetStream streams and durable consumers with acknowledgement, redelivery, replay, retention and idempotent sink handling."
license: Proprietary
metadata:
  version: "1.1.0"
---

# nats-jetstream-data-streaming

## Activation boundary
Use for persistent JetStream pipelines. Core NATS is ephemeral at-most-once; JetStream adds persistence and replay.

## Required inputs
NATS versions; subjects; storage; retention; replicas; consumer/ack policy; max delivery; message rate; replay needs.

## Production workflow
1. Define subjects, storage, retention and replica count.
2. Create durable consumers with explicit delivery, ack, timeout and backoff.
3. Define stable message identity; dedup windows are not end-to-end exactly-once.
4. Select pull/push and batch limits from downstream capacity.
5. Acknowledge only after durable sink commit; use idempotency for external effects.
6. Define DLQ/quarantine and replay by sequence/time; monitor pending and redelivery.

## Failure modes and recovery
- Unacked redelivery: inspect ack timing and sink commit.
- Consumer lag: scale only within sink concurrency limits.
- Retention eviction: expired data cannot be replayed.
- Duplicate publication: use stable IDs and idempotent sinks.
- Replica loss: verify quorum and storage health.

## Validation and evidence
- Test restart, leader failover, disconnect, ack timeout, replay and retention expiry.
- Measure publish latency, lag, redelivery, pending bytes and recovery time.

## Output contract
Return stream/consumer config, retention rationale, ack boundary and replay runbook.

## Official references
- https://docs.nats.io/concepts/jetstream
- https://docs.nats.io/learn/jetstream/
