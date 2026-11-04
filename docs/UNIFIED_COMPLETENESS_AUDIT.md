# Pre-release Capability Map — Consolidation and Completeness Audit

**Audit snapshot:** 2026-11-04  
**Canonical branch:** `pre_release`  
**Audited code snapshot HEAD:** `868d269dd7dc2d40d41a99ea1b6f3e9e8e1cb803`  
**Baseline:** `main` plus the unified YAML capability map and the latest comprehensive Data Engineering, Data Science and Infrastructure changes.

## Consolidation result

The `pre_release` branch was created from the latest unified branch, then integrated with the five newer commits from `feat/comprehensive-data-science-infrastructure` that were not present in the unified snapshot. The integration is a two-parent merge, preserving both histories. The old JSON/ROUTER-oriented `feat/hierarchical-skill-graph-v2` branch was not merged wholesale because its layout is superseded by the current YAML graph; useful specialist content can be ported selectively.

- Integrated source branch: `feat/comprehensive-data-science-infrastructure`
- Integrated source head: `a34921adc0026c6e7091d0523d5996a1c3152644`
- At this audit snapshot, `pre_release` is 96 commits ahead of `main`, 0 behind; 300 changed paths.
- `main` remains unchanged.
- User-scoped domain selection is implemented: up to five non-overlapping active map scopes, dry-run by default, atomic user-profile updates, and fail-closed `domain_not_enabled` routing.
- Data Science is registered canonically at `data/data-science`, under the Data domain.
- PR #3 was integrated into `pre_release`; PR #2 still points to the older unified branch and must not be treated as the release candidate.

## Current inventory

| Measure | Current value |
|---|---:|
| Top-level domains | 41 |
| Active SKILL.md packages | 322 |
| Nested map files | 83 |
| Deterministic routing fixtures | 348 |
| Unit tests | 54 |

These are structural inventory values, not a completeness or production-readiness score. Use `python scripts/report_coverage.py --summary` for live counts.

## Post-audit structural additions (2026-11-04; not a new test certification)

After the historical audited SHA above, Data Engineering added 19 specialist packages and three additional catalog specialists: vendor-neutral Iceberg REST, Project Nessie and Apache Gravitino. At this documentation update, the committed master skill-ID YAML lists **344 IDs** and the deterministic fixture YAML lists **385 cases**. These are direct file inventory counts. The historical 322 active skills, 348 fixtures and 54 unit tests in the audit table above refer to an earlier validated snapshot; they are **not** claimed as passing results on the updated branch.

The catalog update includes protocol version and credential-delegation boundaries, vendor-specific routing exclusions, merge/commit timeout recovery, and tests for Persian/English and negative scope collisions. See `docs/DATA_ENGINEERING_CATALOG_OPERATIONS.md`. Full `Router.validate()`, routing fixture evaluation, unit suite, host integrations and real external catalog tests must be rerun and recorded against the newest HEAD.

## Domain maturity assessment

| Domain | Assessment | What exists | What remains incomplete |
|---|---|---|---|
| Data Engineering | Broad structural coverage; operational depth uneven | Ingestion, CDC, batch/streaming, orchestration, transformation, formats, lakehouse/catalogs, warehouse/federation, quality, governance, DataOps, reliability, cloud, serving and architecture. The CDC route now includes Oracle GoldenGate, SQL Server CDC/Change Tracking and MongoDB Change Streams. | Engine-specific managed warehouse procedures, broader broker and streaming-SQL coverage, catalog operations, versioned compatibility matrices, runnable reference implementations, production failure/recovery evidence and deeper routing evaluation. |
| Data Science | Broad specialist coverage; operational depth still under evaluation | 42 active specialist skills across 20 subdomain maps and 26 defined capability areas: scientific computing, EDA, frequentist and Bayesian inference, robust/nonparametric methods, multiple testing, complex surveys, experimentation, causal ML, panel econometrics, missing data, classical ML, calibration, fairness assessment, conformal uncertainty, forecasting, survival, recommendation, graph, geospatial, simulation, optimization, reproducible notebooks and multilingual NLP. | All 26 defined capability areas have active specialist routes; this is structural coverage, not proof of expert correctness. Remaining work: independent task evaluation, deeper causal-design evidence, domain-specific reference datasets, subgroup uncertainty for low-resource populations, forecasting under distribution shift, version-tested examples and periodic source maintenance. Legal fairness conclusions and deployment/MLOps remain outside this domain's scope. |
| Infrastructure Engineering | Broad structural coverage across 16 first-class selectable scopes; operational depth still under review | 95 unique active specialist skills: 60 existing skills retained and re-homed plus 35 new packages. Coverage includes Compute/OS, Networking, Cloud, IaC, Virtualization, Containers/Kubernetes, DevOps Delivery, Platform Engineering, SRE, Observability, Infrastructure Security, Storage, Database Infrastructure, Edge, Hardware/Data Center and Architecture/Governance. All 35 new specialists have positive routing fixtures. | Per-skill version-tested procedures and independent specialist review; deeper provider-specific edge cases, hardware/firmware compatibility, identity/PKI lifecycle, production DR drills, multi-cloud failure tests, negative/ambiguous/multilingual routing evaluation and real host compatibility. Structural coverage is not production certification. |
| AI & ML Engineering | Existing domain; separate audit required | LLM/RAG, deep learning, ML, MLOps, vision, speech and responsible AI routes. | Distributed training, evaluation methodology, inference optimization, model governance, safety, feature lifecycle and production observability. |
| Software Engineering | Partial specialist coverage | Backend, frontend, architecture, languages, testing and developer tools. | Mobile framework coverage, secure SDLC depth, API compatibility and production testing. |
| Other domains | Mixed maturity | Broad discovery taxonomy with selected specialist packages. | Many subdomains remain mapped-only or have narrow starter skills; they are not complete professional capability packs. |

## Validation status

- YAML graph validation: **PASS** (322 indexed active skills; 83 maps; typed relations validated).
- Deterministic routing evaluation: **PASS** (348 fixtures; no failed cases, including 35 new Infrastructure specialist routes).
- Coverage report: **PASS** (41 top-level domains; 322 indexed active skills; 83 maps; 124 mapped-only subdomain nodes).
- CLI, security, overlay and Infrastructure coverage unit tests: **PASS** (54/54).
- Host compatibility (Codex, OpenCode, Copilot, Claude Code, Cursor): **NOT VERIFIED**.
- Semantic routing quality and false-positive/false-negative rates: **NOT MEASURED**.
- Production readiness: **NOT ESTABLISHED**.

## Required completion gates

1. Complete the Data Engineering inventory against current production tool ecosystems; distinguish active specialists from mapped-only technologies.
2. Add missing tool families only when each has a clear task boundary, maintained official references and failure/recovery procedure.
3. Expand positive, negative, near-miss, ambiguous and Persian/English routing fixtures for every new specialist.
4. Add versioned compatibility notes and reproducible examples for major engines and connectors.
5. Verify idempotency, duplicate delivery, ordering, replay, backfill, late data, schema evolution, partial publication and rollback for relevant pipelines.
6. Measure resolver false positives/false negatives using a labeled benchmark; deterministic fixture success is not semantic model accuracy.
7. Test real host invocation, skill discovery, file access and context loading on each supported Agent Host.
8. Human review remains required before opening or merging a release PR to `main`.

Data Science detail: see `docs/DATA_SCIENCE_COVERAGE_AUDIT.md` for the 26-area capability matrix, new specialist boundaries and remaining limitations. Infrastructure detail: see `docs/INFRASTRUCTURE_COVERAGE_AUDIT.md` and `docs/INFRASTRUCTURE_TOOL_MATRIX.md`. The Data root has nine first-class subdomains, but the overall Data domain is not complete; see `docs/DATA_DOMAIN_COMPLETENESS_STATUS.md`. Domain-selection semantics and security rules are documented in `docs/DOMAIN_SELECTION.md`.

## Interpretation

A Skill file or active YAML node is not proof of a complete capability. This audit separates taxonomy coverage, structural registration, deterministic routing, executable procedure, host compatibility and production evidence. Only the first three have meaningful automated evidence today; the latter stages remain incomplete.
