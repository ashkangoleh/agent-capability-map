---
name: dremio-presto-query-federation
description: "Design Dremio and Presto/Trino federation with pushdown, source limits, identity and consistency boundaries."
license: Proprietary
metadata:
  version: "1.1.1"
---

# dremio-presto-query-federation

## Activation boundary
Use for query federation across heterogeneous systems. Federation does not guarantee source transaction consistency or eliminate data movement.

## Required context
Engine/version; connector versions; source query limits; identity propagation; schemas; network; workload and latency SLO.

## Production procedure
1. Classify sources by pushdown capability, transaction isolation, statistics, data types and concurrency limits.
2. Inspect physical plans to verify predicate/projection pushdown and identify exchanges/materialization.
3. Define source-specific credentials and identity propagation; test row-level access at source.
4. Use reflections/materializations/caching only when freshness and invalidation are explicit.
5. Control concurrency and query admission to protect operational source databases.
6. Validate timestamp, decimal, nested type, collation and null semantics across engines.
7. Set query timeouts, retries and cancellation behavior; avoid retry storms against sources.

## Failure modes and recovery
- No pushdown: reduce remote scans or materialize a governed intermediate.
- Source overload: isolate workloads and cap concurrency.
- Inconsistent results: define snapshot/isolation limitations across sources.
- Credential leakage: use scoped source credentials and audit identity mapping.
- Schema drift: refresh metadata and contract-test dependent queries.

## Validation and acceptance
- Test plan pushdown, source outage, auth denial, schema drift and high concurrency.
- Measure bytes moved, source CPU, query latency, queue time and cache freshness.

## Output contract
Return federation topology, pushdown evidence, identity model, source-protection limits and recovery plan.

## Official or primary references
- https://trino.io/docs/current/
- https://docs.dremio.com/current/

## Independent operational verification
For deployable changes and incident response, consult the [specialist recovery and falsification protocol](references/acceptance-and-recovery.md) on demand. Preserve verified runtime evidence and refuse privileged mutations without authorization.
