---
name: opensearch-analytics-index-engineering
description: "Use OpenSearch for search-oriented ingestion and analytics with mappings, shards, refresh, ISM and bulk APIs."
license: Proprietary
metadata:
  version: "1.1.1"
---

# opensearch-analytics-index-engineering

## Activation boundary
Use for search/index-oriented analytics and log/event retrieval. Do not use OpenSearch as a substitute for a relational warehouse without query-fit evidence.

## Required context
OpenSearch version; document shape; mappings; ingest rate; query patterns; shard count; retention; replicas; security and ISM.

## Production procedure
1. Define document identity, routing key, mapping and dynamic-field policy before indexing.
2. Choose shard/replica count and rollover strategy from index size, query concurrency and recovery.
3. Use bulk ingestion with bounded batch size, retry classification and per-item error inspection.
4. Set refresh interval from search freshness needs; avoid forced refresh per document.
5. Configure ISM rollover, retention, snapshots and restore validation.
6. Use ingest pipelines only for deterministic transformations; keep complex business transformations upstream.
7. Monitor shard allocation, segment merges, heap, indexing pressure, query latency and rejected writes.

## Failure modes and recovery
- Mapping explosion: disable uncontrolled dynamic fields and reindex with explicit mapping.
- Hot shards: revisit routing and shard sizing.
- Bulk partial errors: inspect per-item status before retry.
- Merge/refresh pressure: tune ingest batch and refresh interval.
- Snapshot restore gap: test repository permissions and index metadata recovery.

## Validation and acceptance
- Test mapping evolution, bulk retry, rollover, retention deletion, snapshot restore and shard loss.
- Measure indexing throughput, search p95/p99, heap, merge time and storage amplification.

## Output contract
Return mapping, shard/rollover design, bulk policy, ISM/snapshot plan and operational thresholds.

## Official or primary references
- https://opensearch.org/docs/latest/
- https://opensearch.org/docs/latest/im-plugin/ism/index/

## Independent operational verification
For deployable changes and incident response, consult the [specialist recovery and falsification protocol](references/acceptance-and-recovery.md) on demand. Preserve verified runtime evidence and refuse privileged mutations without authorization.
