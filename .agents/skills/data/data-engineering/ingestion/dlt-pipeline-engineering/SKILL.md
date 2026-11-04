---
name: dlt-pipeline-engineering
description: "Build dlt pipelines with explicit source resources, incremental state, schema evolution, destination loading and reproducible recovery."
license: Proprietary
metadata:
  version: "1.1.0"
---

# dlt-pipeline-engineering

## Activation boundary
Use for the Python dlt library. Keep source extraction, resource selection, pipeline state and destination load semantics explicit.

## Required context
dlt version; source/resource; cursor or primary key; destination; write disposition; schema; state location; run frequency and retries.

## Production procedure
1. Model sources/resources explicitly and select only required tables/endpoints.
2. Choose incremental cursor, primary key and initial value; verify monotonicity and late-update behavior.
3. Choose append, merge or replace from mutation semantics; define deduplication and delete propagation separately.
4. Persist pipeline state in the correct destination/state location and define backup/restore.
5. Configure schema evolution, type hints, nested data and destination type mapping.
6. Set pagination, API rate limits, batching and parallelism.
7. Separate extraction retry from destination load retry; failed load must not silently advance source state.
8. Use run/package metadata to distinguish extracted, normalized, loaded and failed packages.

## Failure modes and recovery
- Cursor skips late updates: use overlap or source change sequence and deduplicate.
- State lost: restore matching pipeline/source identity; do not restart at latest by default.
- Schema drift: quarantine incompatible changes and preserve raw payload.
- Partial destination load: inspect package/job state before retry.
- Replace mode deletes good data: validate scope and use staging/swap when supported.

## Validation and acceptance
- Test first load, incremental continuation, late updates, duplicates, schema change, load failure and state restore.
- Reconcile source and destination counts at a stable cursor boundary.
- Record cursor, state location, package IDs, rejected rows and destination commit.

## Output contract
Return source/resource model, cursor/state design, write disposition, schema policy and recovery procedure.

## Official or primary references
- https://dlthub.com/docs/
- https://dlthub.com/docs/general-usage/incremental-loading
