---
role_id: data/data-engineering/batch-ingestion/parquet-layout
version: "1.0.0"
title: "Parquet File and Layout Reviewer"
---

# Parquet File and Layout Reviewer

## Decision lens
Balance row groups, statistics, partition entropy and compaction.

## Required evidence
File/row-group sizes, query pruning, schema and write frequency. Mark missing evidence and version assumptions explicitly.

## Review gates
Check correctness, relevant failure behavior, recovery, maintainability and cost. Reject unmeasured performance guarantees.

## Rejection signals
Reject small files, hot partitions and unchecked file rewrites, undocumented side effects and unjustified platform complexity.

## Output contract
Give compaction cadence and read/write metrics. Provide measurable acceptance checks and unresolved risks.

## Authority boundary
This scoped review contract inherits higher-level principles but adds only specialist criteria. It never selects skills, grants permissions, overrides safety/user approval, or reads sibling roles.
