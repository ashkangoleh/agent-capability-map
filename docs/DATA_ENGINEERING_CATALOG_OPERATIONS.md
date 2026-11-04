# Iceberg REST Catalog Operations — Data Engineering

**Branch:** `pre_release`  
**Scope:** `data/data-engineering/lakehouse/catalogs/iceberg-rest`  
**Status:** Specialist route and deterministic test cases added; not independently runtime-validated.

## Why this capability is separate

Iceberg REST is a **protocol** used by multiple catalog implementations. Apache Polaris and Lakekeeper are specific **implementations** with separate deployment, authorization, storage and upgrade behavior. DataHub and OpenMetadata are metadata/governance catalogs, not transaction coordinators for Iceberg commits.

| User intent | Required specialist |
|---|---|
| Verify REST endpoint discovery, catalog authentication, delegated storage access, commit conflict or cross-engine read/write on a generic Iceberg REST catalog | `iceberg-rest-catalog-operations` |
| Operate Polaris-specific principal roles, catalog roles, storage grants or deployment | `polaris-iceberg-catalog-operations` |
| Operate Lakekeeper-specific warehouse permissions, storage profiles or lifecycle | `lakekeeper-iceberg-catalog-operations` |
| Manage Iceberg schema/partition changes | `iceberg-table-schema-partition-evolution` |
| Plan Iceberg compaction/snapshot expiry | `iceberg-compaction-retention` |
| Operate OpenMetadata metadata ingestion and lineage | `openmetadata-catalog-operations` |

The generic route intentionally excludes `polaris` and `lakekeeper`. Cross-vendor comparison requests may need explicit composition; the deterministic router is not a semantic planner.

## Operational evidence checklist

1. **Compatibility:** server release, REST protocol feature/endpoints, client/engine versions, table format version and FileIO documented. Record unsupported optional endpoints.
2. **Authentication:** catalog principal, TLS/auth flow and scoped namespace/table actions distinguished from object storage authority. Never print credentials in logs or engine configuration dumps.
3. **Storage:** credential vending/remote signing availability and delegation negotiation explicitly tested. Credentials can expire during long jobs; confirm refresh behavior or fail closed.
4. **Concurrency:** test two writers with a controlled conflicting update and inspect server/engine behavior; do not equate HTTP retries with safe commit retries.
5. **Ambiguous outcomes:** inject a client timeout after server commit; read current table state/snapshot and reconcile, then retry only when safe.
6. **Recovery:** distinguish live metadata from uploaded data files; test snapshot visibility, retention, object cleanup hazards and restore permissions.
7. **Interoperability:** read and write the same disposable table from two supported engines; capture schema and row count/snapshot checks, including engine feature limitations.
8. **Observability:** catalog latency, auth failures, commit conflicts, stale reads, token refresh failures and recovery time.

### Version and source discipline

- The [REST catalog specification](https://iceberg.apache.org/rest-catalog-spec/) defines protocol operations; not every optional endpoint is implemented by every server.
- The [Iceberg REST catalog client documentation](https://iceberg.apache.org/docs/latest/rest-catalog/) lists authentication modes, paging/retry settings, TLS considerations and token redaction warnings. Validate documented properties against the deployed Iceberg client version.
- The [REST protocol concepts](https://iceberg.apache.org/docs/nightly/rest-protocol/) cover config negotiation and delegated storage access. *Nightly documentation is not an assertion that a feature exists in the target release.*
- Consult provider-specific official documentation for Polaris/Lakekeeper on permissions, warehouse provisioning and storage delegation. Do not silently generalize provider behavior.

## Routing verification

```sh
python -m capability_map validate
python scripts/report_coverage.py --summary
python scripts/evaluate_graph.py
python -m unittest tests.test_iceberg_rest_catalog_coverage -v
python -m unittest discover -s tests -v
```

The new fixtures include vendor-neutral discovery, delegated credential expiry, commit timeout recovery, a Persian/English case, vendor-specific exclusions, and an Iceberg schema-evolution near miss. **Fixture additions and test-source review are not proof that commands ran or passed**. A measured model/host benchmark and real engine test environment remain out of scope for this increment.

## Remaining catalog backlog

- Nessie and Gravitino: inventory their maintained production feature sets, route boundaries, version-specific implementations and auth; add skills only where distinct operations justify them.
- Polaris and Lakekeeper: independently check operational claims against supported releases and reproduce IAM/credential vending cases.
- Engine compatibility: generate a version-pinned Spark/Flink/Trino/DuckDB matrix from official adapters and run representative integrations.
- CI/host integration: confirm full router tests and real host invocation. Record false-positive, near-miss and abstention rates.

**No domain-complete or production-ready claim is made by this document.**
