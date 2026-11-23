---
name: gcp-data-platform-engineering
description: "Design GCP data platforms across BigQuery, Dataflow, Dataproc, Pub/Sub and Cloud Storage."
license: Proprietary
metadata:
  version: "1.1.1"
---

# gcp-data-platform-engineering

## Activation boundary
Use for GCP-native data platform architecture and service operations.

## Required context
Organization/project/region; Pub/Sub event rate; BigQuery workload; Dataflow/Dataproc runtime; GCS; IAM; quotas and cost.

## Production procedure
1. Define project and service-account boundaries, VPC-SC/data perimeter needs and regional residency.
2. Choose Cloud Storage landing zones and lifecycle; define object identity and retention.
3. Use Pub/Sub for event transport and Dataflow/Beam for streaming/batch processing when semantics fit.
4. Use Dataproc/Spark for workloads requiring Spark ecosystem or custom libraries.
5. Design BigQuery partitioning/clustering, Storage Write API mode and slot/reservation model.
6. Govern datasets with IAM, authorized views, row/column policies and audit.
7. Monitor quotas, streaming buffer, Dataflow watermark/backlog, BigQuery slots and cost.

## Failure modes and recovery
- Pub/Sub redelivery: use idempotent consumers and ack after durable sink commit.
- Dataflow watermark stalls: inspect source partitions and slow transforms.
- BigQuery append timeout: determine Storage Write API commit/offset state before retry.
- GCS IAM bypass: restrict direct bucket access.
- Regional mismatch: align source, processing and warehouse locations.

## Validation and acceptance
- Test Pub/Sub replay, Dataflow worker loss, BigQuery write offsets, schema change and GCS restore.
- Measure watermark, write latency, slot utilization, bytes scanned and cost.

## Output contract
Return GCP service topology, identity/perimeter model, ingestion/compute choice and SLO/cost gates.

## Official or primary references
- https://cloud.google.com/architecture/data-lakes
- https://cloud.google.com/dataflow/docs
- https://cloud.google.com/bigquery/docs

## Independent operational verification
For deployable changes or incidents, read [specialist acceptance and recovery evidence](references/acceptance-and-recovery.md) on demand. Its specific fault/restore oracle is a review gate, not proof of execution or permission to modify a system.
