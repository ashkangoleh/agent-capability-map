---
name: apache-paimon-streaming-lakehouse
description: "Design Apache Paimon tables with LSM storage, changelog production, Flink/Spark integration, compaction and snapshot lifecycle."
license: Proprietary
metadata:
  version: "1.1.1"
---

# apache-paimon-streaming-lakehouse

## Activation boundary
Use for Apache Paimon table design and streaming lakehouse operations. Paimon semantics are not identical to Iceberg, Hudi or Delta.

## Required context
Paimon version; Flink/Spark versions; append-only or primary-key table; bucket/partition keys; merge engine; changelog; snapshots; catalog/storage.

## Production procedure
1. Select append-only versus primary-key table from update/delete semantics and required changelog output.
2. Define partition/bucket strategy; model skew and hot keys before fixing bucket count.
3. Select merge engine and sequence field where source ordering matters; document late/out-of-order resolution.
4. Choose changelog producer mode from downstream consumer requirements.
5. Configure write buffer, compaction, snapshot expiration and file sizing from measured workload.
6. Validate Flink/Spark connector and catalog compatibility for exact releases.
7. Secure object-store/catalog credentials separately and assign retention/cleanup ownership.

## Failure modes and recovery
- Compaction backlog: inspect write rate, bucket skew and compaction resources.
- Changelog gaps: verify producer mode and sequence semantics before replay.
- Primary-key conflicts: define deterministic ordering and merge behavior.
- Snapshot growth: expire only after recovery windows are considered.
- Connector mismatch: pin compatible engine and Paimon versions.

## Validation and acceptance
- Test inserts, updates, deletes, out-of-order events, changelog, checkpoint recovery and compaction.
- Compare streaming output with deterministic batch reference.
- Measure write amplification, file count, compaction lag and read latency.

## Output contract
Return table model, merge/changelog semantics, bucket design, engine compatibility and maintenance plan.

## Official or primary references
- https://paimon.apache.org/docs/
- https://github.com/apache/paimon

## Independent operational verification
For deployable changes and incident response, consult the [specialist recovery and falsification protocol](references/acceptance-and-recovery.md) on demand. Preserve verified runtime evidence and refuse privileged mutations without authorization.
