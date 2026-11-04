# Data Domain Completeness Status

**Assessment:** Broad structural coverage; not complete or production-certified.

The Data root exposes nine first-class subdomains: Data Engineering, Data Science & Applied Statistics, Analytics Engineering, Database Engineering, Data Analysis, Business Intelligence, Data Governance, Data Quality and Data Architecture.

| Subdomain | Current evidence | Status |
|---|---|---|
| Data Engineering | Broad tool/skill coverage; managed warehouse operations, broker/streaming SQL breadth, catalog operations, version compatibility and production recovery evidence remain gaps. | Incomplete |
| Data Science | 26 declared capability areas have active specialist routes; independent statistical review, representative datasets and version-tested procedures remain outstanding. | Structural coverage complete; validation incomplete |
| Analytics Engineering | dbt, dimensional modeling and semantic-layer routes exist. | Requires independent depth audit |
| Database Engineering | Relational SQL, PostgreSQL, MySQL and StarRocks routes exist. | Requires engine and operational coverage audit |
| Data Analysis | SQL metrics, cohort/retention, experimentation, reconciliation, visualization and Polars routes exist. | Requires independent depth audit |
| Business Intelligence | Dashboard and Superset routes exist. | Requires broader BI tool and governance audit |
| Data Governance | Catalog and lineage routes exist. | Requires policy, ownership, access and lifecycle audit |
| Data Quality | Quality contracts and validation tools exist. | Requires cross-engine execution and failure evidence |
| Data Architecture | Architecture and platform design routes exist. | Requires reference architecture and migration evidence |

## Completion gates

- Complete each subdomain against current tools, concepts, standards and managed-service variants.
- Distinguish active specialist skills from mapped-only nodes.
- Add positive, negative, ambiguous and Persian/English routing tests.
- Verify version-specific commands, APIs, connectors and operational procedures.
- Test idempotency, replay, backfill, late data, schema evolution, recovery, access control and cost where applicable.
- Conduct independent domain-specialist review before claiming production readiness.

A registry count or green deterministic routing suite is not proof of expert correctness or production readiness.

## Current progression checkpoint — 2026-11-04

**Decision:** The top-level `data` domain is **NOT COMPLETE**. No other top-level domain should be designated next until this domain has undergone subdomain-by-subdomain depth review. User authorized continuing with the next Data subdomain; **`data/data-science`** is the next focused workstream. Work on one subdomain at a time; do not label outstanding work as complete.

The exact `pre_release` tree contains nine child entries. These statements describe verified route/registry structure in the branch and outstanding evidence, not successful real-agent execution:

| Sequence | Subdomain | Structural observation | Minimum remaining gate |
|---|---|---|---|
| 1 | Data Engineering | 23 direct capability scopes, broad specialists including Iceberg REST, Polaris, Lakekeeper, Nessie and Gravitino | Full-suite validation, version-pinned integrations, broker/streaming SQL depth, failure injection, recovery/replay and host benchmark |
| 2 | Data Science & Applied Statistics **(NEXT)** | 20 direct category maps; 42 registered specialists/26 declared capability areas per prior audit | Independent estimator evaluation, representative datasets, temporal/group leakage, coverage/calibration, multilingual/near-miss and host benchmark |
| 3 | Analytics Engineering | 3 category scopes: dbt, dimensional modeling, semantic layer | Incremental/restatement semantics, contracts/versions/access, MetricFlow/YAML-version compatibility, late facts/metric grain and cross-warehouse test behavior |
| 4 | Database Engineering | 2 direct scopes: relational databases and StarRocks | SQL/transaction/locking/replication/performance depth, other engine inventories, rollout/recovery and negative routing |
| 5 | Data Analysis | 6 direct scopes: SQL, retention/funnel, experiments, Polars, visualization, reconciliation | Broader analytical methods, metric provenance, statistical guardrails, versioned runnable cases and reporting validation |
| 6 | Business Intelligence | 2 scopes: Superset and dashboard analysis | Looker/Power BI/other BI capability boundaries, semantic definitions, RLS, refresh, dashboard governance and migration |
| 7 | Data Governance | 2 scopes: metadata catalog and lineage | Ownership, access policy/ABAC, PII and classification, retention, metadata quality, regulatory/jurisdictional distinctions and audit proof |
| 8 | Data Quality | Flat registry of 2 active entries in `domains/data/quality-skills.yaml` | Dedicated routing taxonomy for quality dimensions, reconciliation, anomaly/drift, contracts/SLAs, incident response and cross-engine tests |
| 9 | Data Architecture | Flat registry of 1 active specialist in `domains/data/architecture/skills.yaml` | Separate capability branches for architecture, distributed contracts, multi-engine boundaries, migration, governance and reference implementations |

**Status interpretation:** "Active" means the resolver has an explicit reachable package, not that all methods are correct or tested; "structurally complete" for Data Science applies only to its *declared 26-capability matrix* and does not imply production readiness.

### Exit criteria for each subdomain

1. Document a bounded capability matrix and actual registered specialist IDs, uncovered use cases and non-goals; avoid increasing skill count without a clear task boundary.
2. Validate graph, stable routing, overlapping-domain selection, negative/ambiguous/Persian-English cases, token budget and explicit abstention.
3. Verify maintained vendor/standard references and version constraints. Run reproducible examples against target runtimes where feasible.
4. Include failure states, idempotency, retries, authorization, restoration, rollout/rollback, costs and operational SLOs where applicable.
5. Record executed CI commit SHA, full test counts and real host/behavioral evaluation results. Mark unavailable evidence **NOT VERIFIED**, not PASS.
6. Only then close the subdomain or record explicitly scoped limitations; revisit the Data root assessment after all nine workstreams.

### Data Science progress recorded on 2026-11-04

The `model-validation` workstream has a hardened existing sklearn specialist, a dependency-free executable split-integrity example, 17 locally executed boundary checks, 11 additional deterministic route fixtures and a dedicated test suite. The 42-specialist inventory has **not** increased; this is a depth/quality improvement, not more taxonomy. `docs/DATA_SCIENCE_VALIDATION_PROTOCOL.md` defines its acceptance evidence.

**Not finished:** full repo Python/CI validation, reproducible sklearn experiment, causal identification/experimentation, conformal/calibration, forecasting and statistical inference validation, all-domain behavioral benchmark and multi-host tests. Data Science remains structurally covered but not independently certified. Continue with **causal inference and experimentation** after resolving/recording the new CI/test evidence.

### Next workstream: Data Science validation

Start with the 42 specialist skills and their mapped task boundaries. Compare real method assumptions and independent reference datasets, especially leakage-free validation, survey/multiple-testing inference, causal identification, forecasting under distribution shift and conformal calibration. Verify primary references and test both positive and hard negative prompts rather than adding unrelated libraries. The [scikit-learn common pitfalls guide](https://scikit-learn.org/stable/common_pitfalls.html) is a canonical source for data leakage and preprocessing boundaries. The dbt [Semantic Layer YAML reference](https://docs.getdbt.com/reference/semantic-layer-reference) and [model governance](https://docs.getdbt.com/docs/mesh/govern/about-model-governance) are reference starting points for the **later** Analytics Engineering workstream; validate version and product entitlement before applying.

Do not start `infrastructure` or another top-level domain simply because the Data Engineering branch has many registered skills.
