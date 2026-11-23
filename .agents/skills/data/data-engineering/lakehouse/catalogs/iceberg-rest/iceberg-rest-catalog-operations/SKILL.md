---
name: iceberg-rest-catalog-operations
description: "Operate vendor-neutral Apache Iceberg REST catalogs: endpoint discovery, authorization, short-lived storage credentials, concurrent commits and cross-engine recovery."
license: Proprietary
metadata:
  version: "1.0.1"
---

# iceberg-rest-catalog-operations

## Activation boundary
Use for vendor-neutral Iceberg REST catalog protocol and multi-engine interoperability (Spark, Flink, Trino and other supported clients). Do not use as the owner of Apache Polaris or Lakekeeper vendor administration, OpenMetadata/DataHub governance, Iceberg compaction or schema-evolution work. Hand off product-specific IAM and warehouse settings to their specialist skills.

## Required inputs
- Server/product version, REST endpoint, warehouse/prefix, deployment and client/engine versions.
- Auth mechanism (OAuth2, Basic, SigV4 or provider-specific), principal and namespace/table grants; never request plaintext secrets in a report.
- Object-store provider and region, FileIO/credential delegation model, read/write requirements and token lifetime.
- Tables, current metadata/snapshot IDs, concurrency, commit/retry policy, target SLO and recovery RPO/RTO.
- Known supported protocol endpoints: read the catalog's config/endpoint-discovery response instead of presuming all extensions exist.

## Production workflow
1. Confirm the catalog implements the Iceberg REST protocol and verify deployed server and client compatibility with the published spec, not just a vendor feature table.
2. Confirm connectivity, TLS certificate trust, service identity, HTTP timeout, root URI and negotiated warehouse/prefix via the read-only `GET /v1/config` flow (relative to the configured service base URI). Do not assume a hard-coded prefix or that optional endpoints exist.
3. Resolve namespace/table listing and load endpoints with a least-privilege read-only principal; check pagination, namespacing, table metadata format/version and current snapshot visibility.
4. Separate **catalog API authorization** from **object storage permissions**. Confirm whether credential vending or remote signing is supported by this server and client; negotiate requested access delegation, validate credential expiry/refresh and scope, and avoid exposing tokens in logs or engine UI.
5. For writes, establish write grants, commit preconditions/requirements, expected current metadata/snapshot ID and multi-writer isolation. Treat a successful HTTP response as necessary but not sufficient: read back the table state and validate the committed snapshot.
6. On commit conflicts, reload current metadata, assess application-level idempotency and recalculate a safe commit; never blindly replay a mutation against a new table snapshot.
7. On timeout or indeterminate response, query the catalog and object metadata first to establish whether the commit landed. Do **not** automatically retry CREATE/DROP/RENAME/commit operations without resolving outcome.
8. Test Spark and a second client against the *same* table: create/read/append/overwrite only in a disposable namespace, verify schema, snapshot visibility, delete semantics and engine support. Do not assume all engines implement the same protocol extensions.
9. Define versioned roll-forward/rollback, metadata restore and disaster recovery boundaries. Restoring catalog metadata alone is not equivalent to restoring data objects, authorization or expired credentials.

## Failure modes and recovery
- **401/403**: isolate catalog identity, namespace privileges, delegated storage permissions and refresh-token expiry; never enlarge permissions by default.
- **404/not supported**: check negotiated endpoint set, namespace/prefix and protocol extension support before changing table state.
- **409/conflict**: reload table state, resolve concurrent writer history and replan; avoid losing successful commits.
- **429/5xx**: use bounded, jittered retry only for safe/idempotent reads; for write requests first resolve commit outcome.
- **Expired temporary storage credentials**: refresh through supported catalog/client mechanisms and verify job recovery; do not fall back to embedded static cloud secrets.
- **Partial data/file writes or stale cache**: compare catalog snapshot/file manifests against objects and engine read results; schedule orphan cleanup only after retention and ownership checks.
- **Cross-engine mismatch**: check table format version, SQL DDL support, FileIO, view endpoints and client compatibility before rewriting data.

## Validation and evidence
- Capture redacted endpoint/config negotiation, server/client version matrix, privileges and delegation mechanism.
- Prove successful read-only tests, controlled multi-writer commit conflict, timeout-after-commit reconciliation, token expiry during a long scan and same-table reads from two engines.
- Compare snapshot IDs and row counts after replay; retain manifest/object evidence when investigating orphaned files.
- Measure catalog p95/p99 latency, authorization failures, commit-conflict rate, token refresh failures, stale-read duration, and recovery time.
- Keep findings classified: **protocol specified**, **provider/engine documented**, **reproduced in target deployment**, or **unknown**.

## Output contract
Return selected vendor-neutral operations path, compatibility/authorization matrix, read/write and concurrent commit contract, failure and recovery procedures, verification evidence and open production risks. Decline unverified exactly-once claims.

## Official references
- https://iceberg.apache.org/rest-catalog-spec/
- https://iceberg.apache.org/docs/latest/rest-catalog/
- https://iceberg.apache.org/docs/nightly/rest-protocol/

## Independent operational verification
For deployable changes and incident response, consult the [specialist recovery and falsification protocol](references/acceptance-and-recovery.md) on demand. Preserve verified runtime evidence and refuse privileged mutations without authorization.
