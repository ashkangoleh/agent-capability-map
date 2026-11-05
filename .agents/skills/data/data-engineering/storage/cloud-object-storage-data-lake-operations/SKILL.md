---
name: cloud-object-storage-data-lake-operations
description: "Engineer S3, GCS and ADLS data lakes with lifecycle, consistency, security and safe publication protocols."
metadata:
  version: "1.0.1"
---

# cloud-object-storage-data-lake-operations

## Activation boundary
Engineer S3, GCS and ADLS data lakes with lifecycle, consistency, security and safe publication protocols.

## Required context
Provider, region, bucket policy, versioning, encryption, lifecycle, client and table format.

## Production procedure
1. Choose semantics from durability, consistency, access patterns and recovery needs.
2. Define partitioning, layout, replication, lifecycle and metadata ownership.
3. Apply encryption, least privilege, credential rotation and audit.
4. Coordinate cleanup, TTL, snapshots, retention and replay.
5. Test partial upload, node loss, credential expiry, lifecycle deletion and restore.

## Failure modes and recovery
- Validate the complete source-to-sink or control-plane boundary; component-level success is not an end-to-end guarantee.
- Verify partial commits, duplicate/replay behavior, schema drift, concurrency and rollback limits.
- Do not disable security controls or claim unverified exactly-once, atomicity or performance.

## Validation and acceptance
- Verify deployed versions and exact connector/engine compatibility against primary documentation.
- Test representative success, duplicate/replay, schema evolution and partial-failure recovery.
- Record ownership, monitoring, rollback and unresolved assumptions.

## Official or primary references
- https://docs.aws.amazon.com/AmazonS3/latest/userguide/
- https://cloud.google.com/storage/docs
- https://learn.microsoft.com/en-us/azure/storage/blobs/

## Output contract
Deliver the requested implementation or diagnosis with explicit assumptions, version constraints, failure semantics and reproducible validation. Do not fabricate benchmarks, APIs or test results.

## Independent operational verification
For deployable changes and incident response, consult the [specialist recovery and falsification protocol](references/acceptance-and-recovery.md) on demand. Preserve verified runtime evidence and refuse privileged mutations without authorization.
