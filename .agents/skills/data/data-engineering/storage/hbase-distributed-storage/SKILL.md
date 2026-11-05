---
name: hbase-distributed-storage
description: "Design HBase row keys, regions, compactions, replication and consistency for wide-column workloads."
metadata:
  version: "1.0.1"
---

# hbase-distributed-storage

## Activation boundary
Design HBase row keys, regions, compactions, replication and consistency for wide-column workloads.

## Required context
HBase/Hadoop release, row-key pattern, region count, write rate, TTL and replication.

## Production procedure
1. Choose semantics from durability, consistency, access patterns and recovery needs.
2. Define partitioning, layout, replication, lifecycle and metadata ownership.
3. Apply encryption, least privilege, credential rotation and audit.
4. Coordinate cleanup, TTL, snapshots, retention and replay.
5. Test partial upload, node loss, credential expiry, lifecycle deletion and restore.

## Failure modes and recovery
- Validate the complete source-to-sink or control-plane boundary; component-level success is not an end-to-end guarantee.
- Verify partial commits, duplicate/replay behavior, schema drift, concurrency and rollback limits.
- Do not disable security controls or claim unverified exactly-once, atomicity or performance.

## Validation and acceptance
- Verify deployed versions and exact connector/engine compatibility against primary documentation.
- Test representative success, duplicate/replay, schema evolution and partial-failure recovery.
- Record ownership, monitoring, rollback and unresolved assumptions.

## Official or primary references
- https://hbase.apache.org/book.html

## Output contract
Deliver the requested implementation or diagnosis with explicit assumptions, version constraints, failure semantics and reproducible validation. Do not fabricate benchmarks, APIs or test results.

## Independent operational verification
For deployable changes and incident response, consult the [specialist recovery and falsification protocol](references/acceptance-and-recovery.md) on demand. Preserve verified runtime evidence and refuse privileged mutations without authorization.
