---
name: parquet-orc-columnar-storage
description: "Choose and tune Parquet and ORC using row groups/stripes, codecs, statistics and scan patterns."
metadata:
  version: "1.0.1"
---

# parquet-orc-columnar-storage

## Activation boundary
Choose and tune Parquet and ORC using row groups/stripes, codecs, statistics and scan patterns.

## Required context
Reader/writer engines, file sizes, row groups, cardinality, predicates and object storage.

## Production procedure
1. Verify reader/writer support and logical-type mappings for every engine and deployed release.
2. Tune row groups, stripes, encoding and compression from representative scan patterns.
3. Preserve decimals, timestamps, nested structures and schema evolution rules.
4. Inspect statistics and pruning effectiveness.
5. Test cross-engine reads, historical files, null/nested values and corrupt objects.

## Failure modes and recovery
- Validate the complete source-to-sink or control-plane boundary; component-level success is not an end-to-end guarantee.
- Verify partial commits, duplicate/replay behavior, schema drift, concurrency and rollback limits.
- Do not disable security controls or claim unverified exactly-once, atomicity or performance.

## Validation and acceptance
- Verify deployed versions and exact connector/engine compatibility against primary documentation.
- Test representative success, duplicate/replay, schema evolution and partial-failure recovery.
- Record ownership, monitoring, rollback and unresolved assumptions.

## Official or primary references
- https://parquet.apache.org/docs/
- https://orc.apache.org/docs/

## Output contract
Deliver the requested implementation or diagnosis with explicit assumptions, version constraints, failure semantics and reproducible validation. Do not fabricate benchmarks, APIs or test results.

## Independent operational verification
For deployable changes and incident response, consult the [specialist recovery and falsification protocol](references/acceptance-and-recovery.md) on demand. Preserve verified runtime evidence and refuse privileged mutations without authorization.
