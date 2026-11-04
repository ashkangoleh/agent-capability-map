---
name: nessie-versioned-catalog-operations
description: "Operate Project Nessie versioned data catalogs: branches/tags, merge conflicts, Iceberg REST client migration, reference consistency and safe recovery."
license: Proprietary
metadata:
  version: "1.0.0"
---

# nessie-versioned-catalog-operations

## Activation boundary
Use for Project Nessie service operations, versioned catalog branches/tags, reference conflicts, merge recovery or migration from native Nessie clients to Iceberg REST. Do not substitute this for generic Iceberg table maintenance, Polaris/Lakekeeper administration or Nessie-unrelated Git workflows.

## Required inputs
Nessie server and Iceberg client versions; native or REST client URI; metadata persistence; object stores and warehouse names; branch/tag/commit hash; writer engines; authorization; tenancy; data retention; SLO and recovery objectives.

## Production workflow
1. Verify current server release, Iceberg REST availability and stability **for that release**. Nessie's published REST guide has described that integration as experimental; do not assume production support from the protocol alone.
2. Separate Nessie native API (`/api/v2` where supported) from Iceberg REST (`/iceberg`) and inventory which clients, authentication flows and storage integrations work with each.
3. Record reference/warehouse resolution and object storage server configuration. Confirm configured warehouse and storage permissions before testing REST reads or writes.
4. Treat a branch as a moving reference, tag as a fixed reference and a Nessie commit hash as a catalog-wide logical point in history. Distinguish catalog reference history from a table's Iceberg snapshots.
5. For branch promotion or merges, compare source and target reference hashes, enumerate conflicts, review affected tables and record the approved target state. Never force or blindly repeat a merge after unknown outcome.
6. Migrate native clients incrementally: verify REST URI/ref semantics, token handling, engine compatibility, branch-specific reads, time travel and read-only parity before enabling writers.
7. For ambiguous commit/merge responses, reload branch heads and table metadata, reconcile applied changes then retry only safe operations.
8. Before branch deletion or metadata garbage collection, confirm protected references, retention windows and object reachability across all live branches and tags.
9. Rehearse backup/restore of Nessie metadata **and** object storage data; a branch rollback alone is not a complete data restore.

## Failure modes and recovery
- Concurrent commits/merge conflicts: inspect current hashes and conflict details, plan resolution, prevent overwriting another writer.
- Client version/protocol mismatch: disable new REST writer path and keep validated native client behavior where appropriate.
- Token expiry or 401/403: check identity, bearer-token lifetime, catalog authorization and object-store permissions separately.
- Object metadata unavailable: distinguish catalog commit from failed file upload; halt destructive cleanup.
- Unknown branch head after timeout: fetch fresh reference state and compare expected metadata changes; do not replay blindly.
- Retention/GC mistakes: stop deletes, preserve surviving branches and reconstruct missing data from backup before release.

## Validation and evidence
Verify branch isolation with two clients, conflicting merges, tag immutability, time-travel visibility, reference promotion, token expiry, restore of metadata and object files, plus cross-engine read/write parity. Record release-specific Iceberg REST feature support, fallback plan and evidence.

## Output contract
Return branch/tag and writer topology, versioned protocol compatibility, conflict/merge plan, access model, retention and recovery evidence, and unsupported/experimental features.

## Official references
- https://projectnessie.org/guides/about/
- https://projectnessie.org/guides/iceberg-rest/
