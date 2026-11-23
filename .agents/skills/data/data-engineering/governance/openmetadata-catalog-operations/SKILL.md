---
name: openmetadata-catalog-operations
description: "Operate OpenMetadata ingestion, lineage, ownership, profiling, quality and catalog governance workflows."
license: Proprietary
metadata:
  version: "1.1.1"
---

# openmetadata-catalog-operations

## Activation boundary
Use for OpenMetadata metadata operations. It is not an Iceberg REST table catalog and does not replace table commit/locking.

## Required inputs
Release; deployment; metadata DB/search; connector versions; source services; schedules; identity; lineage/quality needs.

## Production workflow
1. Define service connections and least-privilege source credentials.
2. Separate metadata, usage, lineage, profiler and test-suite ingestion schedules.
3. Pin connector/server versions and validate source permissions/API limits.
4. Configure ownership, domains, glossary, classifications and data products.
5. Integrate OpenLineage/native connectors and verify table versus column lineage separately.
6. Scope profiling to avoid source load and sensitive value exposure.
7. Test restore, reindex, connector rerun and upgrade.

## Failure modes and recovery
- Ingestion failure: separate source auth/API, connector parse and search indexing.
- Duplicate entities: validate service identity and FQN before deletion.
- Lineage gaps: inspect integration support; green sync does not prove lineage.
- Search inconsistency: verify ingestion and index state.
- Profiler overload: reduce sampling and exclude sensitive columns.

## Validation and evidence
- Test metadata, usage, lineage, profiling, ownership and deletion.
- Verify column lineage with known SQL pipelines.
- Test RBAC using non-admin roles and measure metadata freshness.

## Output contract
Return connector matrix, ingestion schedule, governance model, lineage coverage, security and recovery.

## Official references
- https://docs.open-metadata.org/latest/connectors/ingestion
- https://docs.open-metadata.org/latest/

## Independent operational verification
For deployable changes and incident response, consult the [specialist recovery and falsification protocol](references/acceptance-and-recovery.md) on demand. Preserve verified runtime evidence and refuse privileged mutations without authorization.
