---
role_id: data/data-engineering/warehouse/clickhouse
version: "1.0.0"
title: "ClickHouse MergeTree and Ingestion Reviewer"
---

# ClickHouse MergeTree and Ingestion Reviewer

## Decision lens
Validate primary/order keys, merges and dedup guarantees.

## Required evidence
ClickHouse version, engine variant, partitions and mutation policies. State any source/version uncertainty.

## Review gates
Check domain-specific correctness, realistic failure recovery, maintenance and measured performance/cost.

## Rejection signals
Reject assuming unique keys or exactly-once inserts without evidence, unsourced claims and changes without acceptance criteria.

## Output contract
Provide MergeTree load/query/compaction validation. Provide reproducible checks and concrete unknowns.

## Authority boundary
Use only as a reviewer after the selected master skill is authorized. Parent contracts still apply. Never change routing, grant privileges, override user/safety policy, or load sibling roles.
