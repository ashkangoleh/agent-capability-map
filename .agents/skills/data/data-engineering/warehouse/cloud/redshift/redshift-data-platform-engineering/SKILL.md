---
name: redshift-data-platform-engineering
description: "Engineer Amazon Redshift COPY and streaming ingestion, MPP distribution, sort keys, materialized views, WLM and maintenance."
license: Proprietary
metadata:
  version: "1.1.1"
---

# redshift-data-platform-engineering

## Activation boundary
Use for Redshift engineering. Distinguish provisioned clusters from Serverless and verify features against deployment mode.

## Required inputs
Deployment mode; compute; source format; COPY/streaming path; concurrency; table size; sort/distribution; freshness/cost.

## Production workflow
1. Choose COPY for bulk files and supported streaming ingestion for event sources.
2. Design distribution and sort keys from joins, filters, skew and size; evaluate AUTO optimization.
3. Use compression defaults unless measurements support overrides.
4. Design materialized views with incremental refresh eligibility in mind.
5. Configure WLM priorities and ETL/BI isolation.
6. Schedule vacuum/analyze only where needed; monitor system views and plans.

## Failure modes and recovery
- COPY duplicates: use manifests and validate replay.
- Distribution skew: inspect slice-level distribution.
- MV full refresh: inspect eligibility.
- Queue buildup: separate workload classes.
- Maintenance overload: avoid redundant manual jobs.

## Validation and evidence
- Test COPY retry, duplicate files, streaming restart and MV refresh.
- Measure skew, queue time, latency, throughput and cost.
- Validate access with production roles.

## Output contract
Return load strategy, physical design, WLM, maintenance, security and benchmark evidence.

## Official references
- https://docs.aws.amazon.com/redshift/latest/dg/c_best-practices-sort-key.html
- https://docs.aws.amazon.com/redshift/latest/dg/c_choosing_dist_sort.html

## Independent operational verification
For deployable changes and incident response, consult the [specialist recovery and falsification protocol](references/acceptance-and-recovery.md) on demand. Preserve verified runtime evidence and refuse privileged mutations without authorization.
