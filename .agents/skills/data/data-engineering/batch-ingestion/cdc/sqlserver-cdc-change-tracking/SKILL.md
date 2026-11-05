---
name: sqlserver-cdc-change-tracking
description: Design SQL Server Change Data Capture and Change Tracking ingestion with LSN validity, retention and consistent incremental extraction.
metadata:
  version: "1.0.1"
---

# SQL Server CDC and Change Tracking Engineering

## Activation boundary

Use for incremental extraction from SQL Server or supported Azure SQL offerings using Change Data Capture (CDC) or Change Tracking (CT). Do not treat CDC and CT as interchangeable, and do not assume SQL Server Agent behavior is identical across SQL Server, Azure SQL Managed Instance and Azure SQL Database.

## Critical mechanism distinction

- CDC asynchronously reads committed transaction-log changes into change tables. It exposes operation metadata, commit LSN ordering and captured column values, including before/after rows for updates.
- Change Tracking records that rows changed and exposes keys/version metadata; it does not preserve the historical values or every intermediate mutation. The consumer normally reads the current source row.
- Choose CDC when downstream consumers need change history or captured values. Choose CT when changed-key detection is sufficient and current row state is the required result.

## Required context

Collect SQL Server/Azure SQL product and version, database compatibility level, recovery/replication configuration, capture or tracking mode, source table keys, capture columns, retention, SQL Agent availability, expected lag, extraction cadence, consumer checkpoint store and target idempotency.

## CDC production procedure

1. Confirm edition and service-tier support, database/table enablement, required permissions and the capture mechanism for the exact deployment type.
2. Enable CDC at database and table scope. Record capture-instance names, captured columns, primary key/net-change configuration and the current validity interval.
3. Monitor the capture job or log-reader integration. For SQL Server and Azure SQL Managed Instance, verify SQL Server Agent and the CDC capture/cleanup jobs; do not assume this operational model for Azure SQL Database.
4. Read changes over explicit LSN intervals. Track the consumer watermark separately from the source high watermark. Use the documented minimum and maximum LSN functions and increment the previous lower bound correctly.
5. Wait until the capture process has advanced through the requested upper time boundary before converting that boundary to an LSN. Do not assume a wall-clock timestamp is immediately queryable in CDC tables.
6. Interpret operation metadata correctly: inserts, deletes and update before/after images are distinct records. Preserve transaction order using commit LSN and sequence metadata; deduplicate by a stable event identity.
7. Keep every extraction interval inside the capture instance validity interval. If cleanup advances the low watermark beyond the consumer checkpoint, stop and perform an explicit gap/reinitialization procedure.
8. Treat capture-instance schema as a versioned contract. For incompatible source DDL, plan a second capture instance and an overlapping cutover where supported; do not assume a tracked table automatically changes its captured shape.
9. Monitor capture latency, high/low LSN watermarks, cleanup retention, change-table growth, transaction-log reuse and consumer lag.
10. Apply changes with idempotent keys and explicit delete semantics. Commit the sink effect before advancing the durable consumer watermark unless both are covered by one atomic transaction.

## Change Tracking production procedure

1. Confirm that only changed-row identity and version information are required; CT is not a historical change log.
2. Capture a consistent baseline and its change-tracking version. Use the documented snapshot-consistency approach so concurrent writes are not lost between baseline extraction and incremental reads.
3. Query changed keys with CHANGETABLE and the last durable version. Validate that the stored version is not older than CHANGE_TRACKING_MIN_VALID_VERSION for every tracked table.
4. Join changed keys back to the source table to obtain current values. Handle deleted keys separately because the current row no longer exists.
5. Advance the consumer version only after the downstream sink is committed and reconciled.
6. Monitor retention cleanup and reinitialize when the consumer version falls outside the valid window.

## Failure modes and recovery

- Capture job stopped or behind: the source transaction log may not truncate as expected and CDC latency grows.
- Cleanup retention overtakes a consumer watermark: the requested LSN interval is no longer complete.
- A query requests an LSN outside the capture instance validity interval: stop rather than silently skipping data.
- CT retention expires before the consumer reads changes: re-baseline; the old version cannot be replayed.
- Update before/after rows are treated as independent business updates: downstream state becomes incorrect.
- Source DDL changes alter capture shape or invalidate assumptions: coordinate a new capture instance and cutover.
- CDC and transactional replication share log-reader behavior in some configurations; verify the actual topology and supported settings.

## Validation and acceptance

- Test inserts, deletes, multiple updates in one transaction, duplicate delivery, delayed capture, cleanup, source restart and DDL evolution.
- Reconcile source and target at a known LSN or CT version.
- Verify that every persisted consumer checkpoint remains inside the source validity interval.
- Record product/SKU, capture mode, retention, job state, permissions and target commit semantics.
- Do not claim end-to-end exactly-once from LSN ordering alone.

## Official references

- SQL Server CDC overview and change-table semantics: https://learn.microsoft.com/en-us/sql/relational-databases/track-changes/about-change-data-capture-sql-server
- CDC administration, monitoring and cleanup: https://learn.microsoft.com/en-us/sql/relational-databases/track-changes/administer-and-monitor-change-data-capture-sql-server
- Querying CDC change data and LSN ranges: https://learn.microsoft.com/en-us/sql/relational-databases/track-changes/work-with-change-data-sql-server
- CDC versus Change Tracking: https://learn.microsoft.com/en-us/sql/relational-databases/track-changes/track-data-changes-sql-server

## Output contract

Deliver the CDC-versus-CT decision, exact source prerequisites, LSN/version checkpoint model, retention and cleanup policy, sink idempotency, recovery/re-baseline plan, monitoring and reconciliation tests. Verify behavior for the exact SQL Server or Azure SQL deployment before giving production commands.

## Independent operational verification
For production-impacting recommendations or incident handling, load [acceptance and recovery protocol](references/acceptance-and-recovery.md) only after this skill is selected. It defines a domain-specific fault-injection oracle, evidence ledger and safe recovery conditions. Do not imply the tests were executed or that this reference grants tool permissions.
