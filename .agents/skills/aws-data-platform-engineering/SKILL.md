---
name: aws-data-platform-engineering
description: "Design AWS data platforms across S3, Glue, Athena, EMR, Redshift, Kinesis/MSK and Lake Formation."
license: Proprietary
metadata:
  version: "1.1.0"
---

# aws-data-platform-engineering

## Activation boundary
Use for AWS-native data platform architecture and service operations, not generic AWS infrastructure networking.

## Required context
Account/region; data volume; latency; sources; IAM roles; S3 layout; Glue Catalog; compute/warehouse; residency and cost.

## Production procedure
1. Select S3 landing zones with bucket ownership, encryption, versioning, lifecycle and object-lock needs.
2. Choose Glue Data Catalog/Lake Formation for metadata and fine-grained access; test direct S3 access separately.
3. Choose Glue ETL, EMR/Spark, Athena, Redshift or managed streaming from workload and latency.
4. Select Kinesis or MSK from event semantics, Kafka ecosystem, retention and consumer needs.
5. Use DMS/Glue connectors for source movement only after validating CDC and schema behavior.
6. Define IAM roles, KMS, Lake Formation grants, network and audit paths.
7. Model cost across compute, scans, requests, storage, egress and idle resources.

## Failure modes and recovery
- S3 direct access bypasses table grants: restrict bucket/prefix policies.
- Glue crawler schema drift: enforce contract and reviewed catalog updates.
- Kinesis shard throttling: scale shards or use on-demand with quota/cost review.
- EMR job retry duplicates: make sink writes idempotent.
- Cross-region replication: verify residency, encryption and recovery.

## Validation and acceptance
- Test IAM with workload roles, DMS/CDC restart, Glue schema change, Athena query and S3 restore.
- Measure freshness, scan bytes, job duration, stream lag and cost.

## Output contract
Return AWS service topology, IAM/catalog model, data flow, recovery and cost plan.

## Official or primary references
- https://docs.aws.amazon.com/whitepapers/latest/building-data-lakes/building-data-lake-aws.html
- https://docs.aws.amazon.com/lake-formation/latest/dg/what-is-lake-formation.html
- https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html
