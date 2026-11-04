---
name: oracle-goldengate-cdc-operations
description: Operate Oracle GoldenGate Extract, trails, distribution paths and Replicat with recoverable CDC and controlled initial-load handoff.
metadata:
  version: "1.0.0"
---

# Oracle GoldenGate CDC Operations

## Activation boundary

Use for Oracle GoldenGate change capture, transactional replication, initial-load plus CDC handoff, trail transport, Replicat apply, checkpoint recovery and lag diagnosis. Do not activate for generic Oracle SQL tuning, Data Pump-only migration or Debezium configuration.

## Required context

Collect source and target database products and versions, GoldenGate release and deployment model, Extract and Replicat modes, source logging configuration, table keys, DDL scope, transaction volume, latency objective, trail storage, network topology, security model, retention and RPO/RTO.

## Production procedure

1. Verify the exact GoldenGate release, supported source/target combination, deployment architecture and feature compatibility from the current Oracle documentation. Do not transfer Classic Architecture commands to Microservices Architecture without validation.
2. Separate initial load from continuous synchronization. Define a consistent source snapshot boundary and the corresponding CDC start position; prove that the handoff has neither a gap nor an overlap that creates unhandled duplicates.
3. Prepare the source database for log-based capture. Verify required supplemental logging, table-level logging such as TRANDATA, privileges, logging mode and supported data types for the selected database. For an online instantiation that combines initial load and CDC, add the required TRANDATA before starting the initial-load Extract where the source platform requires it.
4. Select the supported Extract capture method for the source. Record the source checkpoint, transaction boundary and expected log-retention window before starting capture.
5. Design the topology explicitly: Extract, local trail, Distribution/Receiver path where applicable, remote trail and Replicat. Keep capture and apply independently recoverable; size trail storage for target outages and planned maintenance.
6. Configure schema/table mapping, key selection, column conversion, DDL handling and conflict behavior. Treat keyless updates, key changes, LOBs, character-set conversion and unsupported DDL as explicit design decisions.
7. Select Replicat mode and parallelism only after defining transaction ordering and target-side dependencies. Parallel apply can change concurrency behavior; do not trade away required ordering for throughput.
8. A checkpoint table is required for non-parallel Replicats; verify the checkpoint mechanism for the exact Replicat mode. The checkpoint transaction must remain aligned with the apply transaction. Use supported AdminClient, REST or web operations; never edit trail files, checkpoint files, checkpoint tables or parameter files directly.
9. Create the recommended GoldenGate heartbeat configuration where supported. Monitor Extract lag, trail growth, distribution-path lag, Replicat lag, abends, discarded records, heartbeat latency, target apply errors and disk headroom as separate signals.
10. Define recovery from the last valid checkpoint and retained trail. Reposition only with a documented source/target reconciliation plan; validate transaction boundaries before restarting production traffic.
11. Reconcile source and target using stable keys, source commit watermarks, row counts and sampled value checks. Test schema evolution and restart behavior before rollout.

## Failure modes and recovery

- Source log retention expires before Extract catches up: the capture gap may require a controlled re-instantiation, not a blind restart.
- Trail storage fills or distribution paths stall: preserve trail files, restore capacity and verify checkpoints before purging.
- Replicat repeatedly abends on a row or DDL operation: isolate the failing transaction and determine whether the issue is mapping, unsupported data, target constraint or ordering.
- Missing supplemental logging or stable keys can make updates/deletes incomplete or ambiguous.
- For GoldenGate for SQL Server CDC capture, the SQL Server CDC cleanup job can purge staging rows before Extract consumes them. Validate the capture/log-reader job and use the GoldenGate Purge Change Data task rather than allowing an independent cleanup job to delete unconsumed staging data.
- Checkpoint-table, trail or process state must not be manually edited as a shortcut.
- A healthy Extract does not prove a healthy end-to-end pipeline; monitor capture, transport and apply independently.

## Validation and acceptance

- Prove the initial-load/CDC boundary with a repeatable source snapshot and transaction watermark.
- Test process restart, target outage, network interruption, trail retention, duplicate delivery and schema change.
- Compare source and target state after recovery, including deletes and updates.
- Record exact product versions, configuration evidence, observed lag and unresolved assumptions.
- Do not claim end-to-end exactly-once or zero data loss from checkpoint behavior alone.

## Official references

- Oracle GoldenGate 26ai Microservices Architecture: https://docs.oracle.com/en/database/goldengate/core/26/coredoc/index.html
- Replication components, trails and checkpoints: https://docs.oracle.com/en/database/goldengate/core/26/coredoc/overview-components-data-replication-oracle-goldengate.html
- Preparing GoldenGate for SQL Server CDC capture and staging-data purge: https://docs.oracle.com/en/database/goldengate/core/26/coredoc/prepare-preparing-database-oracle-goldengate-cdc-capture.html
- Extract/Replicat prerequisites, TRANDATA and checkpoint tables: https://docs.oracle.com/en/database/goldengate/core/26/coredoc/configure-ogg-adding-extract-and-replicat.html
- Adding Extract and Replicat processes: https://docs.oracle.com/en/database/goldengate/core/26/coredoc/configure-ogg-adding-extract-and-replicat.html

## Output contract

Deliver a version-specific capture/apply design, source preparation checklist, initial-load handoff, trail/checkpoint topology, monitoring plan, recovery runbook, validation evidence and explicit limits. Mark unsupported source/target combinations and unknown licensing or deployment constraints instead of guessing.
