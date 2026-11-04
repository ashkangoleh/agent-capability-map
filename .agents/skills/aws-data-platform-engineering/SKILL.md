---
name: aws-data-platform-engineering
description: "Design AWS data platforms across S3, Glue, Athena, EMR, Redshift, Kinesis/MSK and Lake Formation."
metadata:
  version: "1.0.0"
---

# aws-data-platform-engineering

## Activation boundary
Design AWS data platforms across S3, Glue, Athena, EMR, Redshift, Kinesis/MSK and Lake Formation.

## Required context
Account/region, IAM, VPC, S3, Glue Catalog, compute, workload SLO, KMS and billing.

## Production procedure
1. Map storage, catalog, ingestion, compute, warehouse, streaming and governance boundaries.
2. Design workload identity, network isolation, KMS, region/residency and private connectivity together.
3. Choose managed versus self-managed components from runtime control and operating burden.
4. Model quotas, concurrency, egress, pricing and DR.
5. Test identity propagation, cross-account access, quota exhaustion and restore.

## Failure modes and recovery
- Validate the complete source-to-sink or control-plane boundary; component-level success is not an end-to-end guarantee.
- Verify partial commits, duplicate/replay behavior, schema drift, concurrency and rollback limits.
- Do not disable security controls or claim unverified exactly-once, atomicity or performance.

## Validation and acceptance
- Verify deployed versions and exact connector/engine compatibility against primary documentation.
- Test representative success, duplicate/replay, schema evolution and partial-failure recovery.
- Record ownership, monitoring, rollback and unresolved assumptions.

## Official or primary references
- https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html
- https://docs.aws.amazon.com/lake-formation/latest/dg/what-is-lake-formation.html

## Output contract
Deliver the requested implementation or diagnosis with explicit assumptions, version constraints, failure semantics and reproducible validation. Do not fabricate benchmarks, APIs or test results.
