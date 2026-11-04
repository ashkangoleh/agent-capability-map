---
name: lakehouse-catalog-ecosystem-interoperability
description: "Evaluate table catalogs and metadata platforms across API compatibility, commit coordination, auth, namespace semantics and engine interoperability."
license: Proprietary
metadata:
  version: "1.1.0"
---

# lakehouse-catalog-ecosystem-interoperability

## Activation boundary
Use for Iceberg/lakehouse table catalog interoperability across Hive Metastore, Glue, Unity Catalog, Nessie, Polaris, Lakekeeper and Gravitino. Metadata governance catalogs are a separate role.

## Required context
Format/version; catalog/version; engines/versions; REST/native protocol; auth/credential vending; object store; writer concurrency; tenancy.

## Production procedure
1. Classify catalog role: transactional table metadata, metadata governance/discovery or cloud control plane.
2. Build engine × format × catalog matrix for read, append, overwrite, deletes, schema evolution and maintenance.
3. Verify REST API, OAuth/signing, credential vending, namespace behavior and extensions.
4. Define commit coordination, optimistic concurrency, locking and conflict resolution.
5. Separate catalog authorization from object-store authorization; test credential vending and direct storage access.
6. Define namespace ownership, multi-tenant isolation, audit, metadata backup and DR.
7. Test one engine write, another read and a third maintenance operation, including concurrent commits.
8. Plan catalog migration with metadata preservation, identifier mapping, cutover freeze and rollback.

## Failure modes and recovery
- Catalog accepts metadata but engine cannot read: inspect unsupported extensions and auth flow.
- Concurrent commit conflict: retry only after refresh and idempotency proof.
- Credential vending failure: separate catalog auth from object-store IAM.
- Catalog backup without files: restore metadata and storage from coordinated points.
- Governance catalog mistaken for table catalog: keep lineage separate from commit path.

## Validation and acceptance
- Test cross-engine read/write, concurrent commit, schema evolution, deletes, credential expiry and failover.
- Validate namespace isolation, backup/restore and migration.
- Record exact versions and unsupported combinations.

## Output contract
Return catalog role, compatibility matrix, commit/auth model, migration and recovery design.

## Official or primary references
- https://iceberg.apache.org/docs/latest/rest-catalog/
- https://polaris.apache.org/
- https://docs.lakekeeper.io/
- https://projectnessie.org/
- https://gravitino.apache.org/
