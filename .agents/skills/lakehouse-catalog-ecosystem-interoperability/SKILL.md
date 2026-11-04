---
name: lakehouse-catalog-ecosystem-interoperability
description: "Evaluate Hive Metastore, Glue, Unity Catalog, Nessie, Polaris, Lakekeeper and Gravitino control-plane behavior."
metadata:
  version: "1.0.0"
---

# lakehouse-catalog-ecosystem-interoperability

## Activation boundary
Evaluate Hive Metastore, Glue, Unity Catalog, Nessie, Polaris, Lakekeeper and Gravitino control-plane behavior.

## Required context
Table format, engines, catalog APIs, auth, credential vending, storage and metadata backup.

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
- https://projectnessie.org/
- https://gravitino.apache.org/docs/1.3.0/overview/
- https://iceberg.apache.org/spec/#rest-catalog-api

## Output contract
Deliver the requested implementation or diagnosis with explicit assumptions, version constraints, failure semantics and reproducible validation. Do not fabricate benchmarks, APIs or test results.
