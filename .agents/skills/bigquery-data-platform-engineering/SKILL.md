---
name: bigquery-data-platform-engineering
description: "Engineer BigQuery batch and streaming ingestion, Storage Write API offsets, partitioning, clustering, materialized views and cost controls."
license: Proprietary
metadata:
  version: "1.1.0"
---

# bigquery-data-platform-engineering

## Activation boundary
Use for BigQuery ingestion and warehouse engineering. Load jobs, legacy streaming inserts and Storage Write API have different guarantees.

## Required inputs
Project/location; partitioning; latency; write API mode; offsets; quota; schema evolution; query/slot/cost model.

## Production workflow
1. Prefer load jobs for bulk files; choose Storage Write API for continuous ingestion.
2. For gRPC application-created streams, persist offsets and commit protocol when exactly-once append is required.
3. Document dedup limitations for REST and legacy streaming paths.
4. Design partitioning/clustering from predicates, retention and late arrival.
5. Account for streaming buffers and visibility behavior.
6. Define schema updates, rejected rows, dead-letter and replay.
7. Tune slots/reservations and materialized views.

## Failure modes and recovery
- Append timeout: determine commit status before retry.
- Buffer visibility: validate before destructive overwrite.
- Quota exhaustion: backpressure producers.
- Partition skew: inspect hot partitions and late events.
- Region mismatch: align processing and storage locations.

## Validation and evidence
- Test offsets, retries, schema notifications and transactions.
- Verify pruning, clustering and materialized view refresh.
- Reconcile source counts and duplicates; measure latency, slots and cost.

## Output contract
Return API choice, offset design, table layout, IAM, recovery and cost limits.

## Official references
- https://docs.cloud.google.com/bigquery/docs/write-api-intro
- https://docs.cloud.google.com/bigquery/docs/write-api-grpc
