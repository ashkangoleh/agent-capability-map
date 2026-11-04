---
name: apache-seatunnel-data-integration
description: "Engineer Apache SeaTunnel batch and streaming data integration with connector, engine, checkpoint and sink guarantees."
license: Proprietary
metadata:
  version: "1.1.0"
---

# apache-seatunnel-data-integration

## Activation boundary
Use for SeaTunnel source-to-sink integration, connector selection, batch/stream execution and CDC. Connector guarantees differ by release and plugin.

## Required inputs
SeaTunnel/connector versions; Zeta, Flink or Spark engine; source/sink; mode; schema; throughput; checkpoint storage; security.

## Production workflow
1. Pin the SeaTunnel release and connector artifact; verify connector support in that release.
2. Separate connector behavior from Zeta, Flink or Spark runtime semantics.
3. Build a source/sink capability matrix: snapshot, CDC, offsets, schema evolution, transactions and supported types.
4. Define checkpoint, restart, backpressure, source throttling and sink commit behavior.
5. Canary a bounded slice; expand only after source/sink reconciliation.

## Failure modes and recovery
- Plugin mismatch: pin engine and connector artifacts together.
- Checkpoint restore failure: verify source offsets and sink commit state before replay.
- Schema drift: quarantine incompatible records; do not silently coerce types.
- Partial publication: reconcile committed batches before retry.

## Validation and evidence
- Test snapshot, incremental continuation, restart, duplicates, deletes and schema evolution.
- Measure lag, throughput, checkpoint duration, rejected rows and sink commit outcome.
- Verify delivery guarantees for the exact source/engine/sink combination.

## Output contract
Return connector/version matrix, execution architecture, guarantee boundaries, recovery runbook and rollout gates.

## Official references
- https://seatunnel.apache.org/docs/
- https://github.com/apache/seatunnel
