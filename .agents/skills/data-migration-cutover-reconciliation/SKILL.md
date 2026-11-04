---
name: data-migration-cutover-reconciliation
description: "Plan cross-platform data migrations using consistent snapshots, CDC convergence, cutover gates, reconciliation, rollback and dual-run controls."
license: Proprietary
metadata:
  version: "1.1.0"
---

# data-migration-cutover-reconciliation

## Activation boundary
Use for migrations between databases, warehouses, lakehouses and storage platforms. A successful bulk copy is not proof of correctness.

## Required inputs
Source/target versions; dataset inventory; volume/change rate; downtime; consistency; CDC; type differences; RPO/RTO; rollback constraints.

## Production workflow
1. Inventory tables, keys, dependencies, permissions, schedules and consumers.
2. Map decimals, timestamps, collations, arrays, JSON, binary and nullability explicitly.
3. Choose bulk snapshot, CDC, unload/load or dual-run and define consistent log position.
4. Make extraction repeatable and load idempotent with checkpoints/manifests.
5. Run CDC to convergence; handle deletes, ordering and schema changes.
6. Reconcile counts, key coverage, duplicates, nulls, aggregates and checksums.
7. Gate writes, drain transactions, record final source position and cut over with rollback criteria.

## Failure modes and recovery
- Snapshot/CDC gap: stop and re-establish a consistent boundary.
- Out-of-order changes: deduplicate by source identity/version.
- Type truncation: quarantine; never silently narrow.
- Target drift: reconcile by key/version.
- Rollback after target writes: define reverse replication or no-return point.

## Validation and evidence
- Test CDC restart, log expiry, schema evolution, deletes, target outage, replay and rollback.
- Measure load throughput, lag, convergence, cutover and recovery time.
- Require owner sign-off on exceptions.

## Output contract
Return inventory, mapping, snapshot/CDC strategy, reconciliation and cutover/rollback runbook.

## Official references
- https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html
- https://debezium.io/documentation/reference/stable/
