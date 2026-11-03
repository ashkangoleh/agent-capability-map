---
name: data-cdc-pipelines
description: Implement or review database change data capture pipelines with snapshot handoff, event ordering, deletion semantics, idempotency, replay and sink reconciliation.
license: Proprietary
metadata:
  version: "1.0.0"
---

# CDC ingestion reliability

## Activate
Use for relational change streams, Debezium/connector-based CDC, incremental change capture, snapshot + stream consistency, or applying CDC events into an analytical sink. An ordinary batch ETL job stays with data-engineering-implementation.

## Procedure
1. Verify source engine/version, log or replication mode, connector capabilities, retention, topology, permissions and sink key semantics.
2. Define snapshot boundary, log position or offset, capture gap handling, table identity, schema evolution, transaction ordering and deletion semantics.
3. Design at-least-once replay tolerance with stable event IDs, deterministic upsert/delete, dedup, tombstones and sink idempotency.
4. Specify offset acknowledgement vs sink commit ordering. Analyze what happens when the sink commits but the acknowledgement fails.
5. Handle schema drift, primary-key changes, long-running transactions, lag, backpressure, snapshot retry and retention expiry.
6. Test inserts, updates, deletes, duplicates, reordered events, restart, failed snapshot, backfill and source/sink count reconciliation.

## Outputs
CDC contract, source-to-sink state machine, implementation/config only for verified versions, failure matrix, tests and recovery runbook.

## Reference
https://debezium.io/documentation/reference/stable/
