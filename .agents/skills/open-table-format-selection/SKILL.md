---
name: open-table-format-selection
description: "Select Iceberg, Delta Lake, Hudi, Paimon or DuckLake by workload, interoperability and maintenance requirements."
metadata:
  version: "1.0.0"
---

# open-table-format-selection

## Activation boundary
Select Iceberg, Delta Lake, Hudi, Paimon or DuckLake by workload, interoperability and maintenance requirements.

## Required context
Engine releases, catalog, object store, append/upsert/delete, streaming, schema evolution and maintenance.

## Production procedure
1. Verify format/catalog/engine compatibility for deployed versions and required features.
2. Define authoritative writer, commit protocol, schema/partition evolution and conflict handling.
3. Plan snapshots, manifests, compaction, vacuum and orphan cleanup with retention.
4. Validate identity, credential vending and direct object access separately from catalog policy.
5. Test concurrent commits, metadata outage, maintenance interruption and restore.

## Failure modes and recovery
- Validate the complete source-to-sink or control-plane boundary; component-level success is not an end-to-end guarantee.
- Verify partial commits, duplicate/replay behavior, schema drift, concurrency and rollback limits.
- Do not disable security controls or claim unverified exactly-once, atomicity or performance.

## Validation and acceptance
- Verify deployed versions and exact connector/engine compatibility against primary documentation.
- Test representative success, duplicate/replay, schema evolution and partial-failure recovery.
- Record ownership, monitoring, rollback and unresolved assumptions.

## Official or primary references
- https://iceberg.apache.org/docs/latest/
- https://docs.delta.io/latest/index.html
- https://hudi.apache.org/docs/overview/
- https://paimon.apache.org/docs/1.4/
- https://ducklake.select/

## Output contract
Deliver the requested implementation or diagnosis with explicit assumptions, version constraints, failure semantics and reproducible validation. Do not fabricate benchmarks, APIs or test results.
