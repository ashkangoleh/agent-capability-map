---
name: gravitino-federated-catalog-operations
description: "Operate Apache Gravitino metalakes, federated catalogs and Iceberg REST service with version-scoped access control, discovery and upgrade recovery."
license: Proprietary
metadata:
  version: "1.0.1"
---

# gravitino-federated-catalog-operations

## Activation boundary
Use for Apache Gravitino server, metalake/catalog lifecycle, federated metadata discovery, Iceberg REST service or multi-catalog governance operations. The unified Gravitino API is **not** interchangeable with its Iceberg REST service; do not mistake either for a general-purpose transactional data engine.

## Required inputs
Exact Gravitino release, deployment mode and metadata store; metalake(s); catalog providers and backends; registered data source ownership; Iceberg REST service endpoint/client versions; identity provider and authorization; storage permissions; backup/restore and query-engine versions.

## Production workflow
1. Pin the exact server and connector versions. Distinguish documented capabilities in released documentation from `/docs/next/`; avoid claiming an optional API exists without endpoint discovery or version-specific evidence.
2. Inventory metalakes, registered catalogs, underlying systems and schema namespaces. Gravitino federates metadata; registering a catalog does not copy source data or provide a new physical table store.
3. Validate the Gravitino unified control-plane API separately from the Iceberg REST service. Test metalake/catalog listing and version-supported create/read/update/delete; do not assume the same schema or route across both services.
4. Establish catalog owner, least-privilege role, credentials rotation and source-side IAM. Verify that delegated storage access is supported by the configured backend and engine; distinguish service authorization from object-store permissions.
5. For Iceberg REST, inspect supported endpoints/feature exclusions for the deployed version (including pagination, multi-table operations and views), then test schema/table metadata and credential vending with a disposable namespace.
6. Test metadata drift, backend connectivity, source deletion and cache/search visibility. A successful control-plane response does not guarantee underlying source data is queryable.
7. Plan connector/server upgrades against release notes and migration guides; check metadata schema changes, query-engine connector behavior, rollback compatibility and startup dependencies.
8. Before force-deleting a catalog, determine if the operation removes only registration or source objects for that provider/release. Record ownership, blast radius and a tested restore path.

## Failure modes and recovery
- Catalog listing succeeds but query fails: distinguish cached metadata from source backend connectivity and storage grants.
- 401/403/credential vending failure: inspect Gravitino identity policy, catalog backend authorization and object access separately.
- REST endpoint unsupported: inspect the installed release's capability matrix; don't invent fallback compatibility.
- Upgrade regression: pin/revert connector version and restore metadata DB from tested backup only when migration compatibility permits.
- Force delete or schema drift: stop dependent workloads; reconcile metadata and source inventory before replay.
- Metadata DB or REST service outage: restore agreed RPO/RTO and verify cross-engine catalog visibility.

## Validation and evidence
Test catalog discovery, namespace/table create/list/read/delete in a disposable source, unauthorized access, token expiry, backend outage, provider-specific no-op/force-delete semantics, snapshot compatibility, query-engine connector upgrades and metadata DB recovery.

## Output contract
Return metalake/provider inventory, interface separation, versioned capability matrix, IAM/delegation boundaries, failure/upgrade plan and validation evidence.

## Official references
- https://gravitino.apache.org/docs/1.2.1/iceberg-rest-service/
- https://gravitino.apache.org/docs/next/iceberg-rest-service/
- https://gravitino.apache.org/docs/next/catalogs-and-schemas/
- https://gravitino.apache.org/blog/gravitino-1-3-1-release-notes/

## Independent operational verification
For deployable changes and incident response, consult the [specialist recovery and falsification protocol](references/acceptance-and-recovery.md) on demand. Preserve verified runtime evidence and refuse privileged mutations without authorization.
