---
name: apache-fluss-streaming-storage
description: "Operate Apache Fluss as streaming storage with log and primary-key tables, buckets, replication, remote storage and Flink tiering."
license: Proprietary
metadata:
  version: "1.1.1"
---

# apache-fluss-streaming-storage

## Activation boundary
Use for Fluss streaming storage. Fluss is not a general-purpose broker replacement, query engine or open table format.

## Required inputs
Fluss release; topology; Coordinator/Tablet sizing; table type; bucket key; replication; remote storage; Flink version.

## Production workflow
1. Choose Log Table versus Primary Key Table from update/delete semantics.
2. Define partition/bucket keys and evaluate hot-bucket skew; ordering is not one global order.
3. Validate coordinator, tablet and replica topology across failure domains.
4. Configure remote storage separately from hot local storage.
5. Integrate compatible Flink connector and define checkpoint/commit/tiering ownership.
6. Monitor bucket throughput, replication lag, tablet health and tiering progress.

## Failure modes and recovery
- Hot bucket: revisit key distribution and bucket count.
- Tablet failure: verify replicas before full write rate resumes.
- Tiering backlog: inspect Flink and remote storage.
- Metadata loss: follow release-specific recovery; do not recreate directories manually.

## Validation and evidence
- Test writes, updates/deletes, failover, replica recovery and Flink checkpoint restore.
- Measure skew, replication lag, storage amplification and tiering delay.
- Record exact Fluss/Flink versions.

## Output contract
Return table model, topology, bucket strategy, tiering design and recovery limits.

## Official references
- https://fluss.apache.org/docs/
- https://github.com/apache/fluss

## Independent operational verification
For deployable changes and incident response, consult the [specialist recovery and falsification protocol](references/acceptance-and-recovery.md) on demand. Preserve verified runtime evidence and refuse privileged mutations without authorization.
