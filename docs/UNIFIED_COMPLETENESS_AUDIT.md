# Pre-release Capability Map — Consolidation and Completeness Audit

**Audit snapshot:** 2026-11-04  
**Canonical branch:** `pre_release`  
**Audit baseline HEAD:** `751cf133d39075fa516425a5e31dc647eae068f6`  
**Baseline:** `main` plus the unified YAML capability map and the latest comprehensive Data Engineering, Data Science and Infrastructure changes.

## Consolidation result

The `pre_release` branch was created from the latest unified branch, then integrated with the five newer commits from `feat/comprehensive-data-science-infrastructure` that were not present in the unified snapshot. The integration is a two-parent merge, preserving both histories. The old JSON/ROUTER-oriented `feat/hierarchical-skill-graph-v2` branch was not merged wholesale because its layout is superseded by the current YAML graph; useful specialist content can be ported selectively.

- Integrated source branch: `feat/comprehensive-data-science-infrastructure`
- Integrated source head: `a34921adc0026c6e7091d0523d5996a1c3152644`
- At this audit snapshot, `pre_release` is 84 commits ahead of `main`, 0 behind; 300 changed paths.
- `main` remains unchanged.
- PR #3 was integrated into `pre_release`; PR #2 still points to the older unified branch and must not be treated as the release candidate.

## Current inventory

| Measure | Current value |
|---|---:|
| Top-level domains | 42 |
| Active SKILL.md packages | 276 |
| Nested map files | 68 |
| Skill registries | 186 |
| Deterministic routing fixtures | 297 |
| Unit tests | 31 |

These are structural inventory values, not a completeness or production-readiness score. Use `python scripts/report_coverage.py --summary` for live counts.

## Domain maturity assessment

| Domain | Assessment | What exists | What remains incomplete |
|---|---|---|---|
| Data Engineering | Broad structural coverage; operational depth uneven | Ingestion, CDC, batch/streaming, orchestration, transformation, formats, lakehouse/catalogs, warehouse/federation, quality, governance, DataOps, reliability, cloud, serving and architecture. The CDC route now includes Oracle GoldenGate, SQL Server CDC/Change Tracking and MongoDB Change Streams. | Engine-specific managed warehouse procedures, broader broker and streaming-SQL coverage, catalog operations, versioned compatibility matrices, runnable reference implementations, production failure/recovery evidence and deeper routing evaluation. |
| Data Science | Medium; broad taxonomy and specialist routes | Scientific computing, statistics, Bayesian methods, experimentation, causal design, classical ML, calibration, explainability, forecasting, survival, recommendation, graph, geospatial, simulation, optimization and text analytics. | Sparse specialist coverage for robust/nonparametric inference, econometrics, MNAR sensitivity, multilingual NLP evaluation, advanced causal estimators, fairness, uncertainty and reproducible notebooks/datasets. |
| Infrastructure Engineering | Broad taxonomy; operational implementation incomplete | IaC, GitOps, CI/CD, DevSecOps, SRE, networking, cloud, Linux/Windows, virtualization, storage, database operations, Kubernetes, service mesh and platform engineering. | Version-tested procedures, identity lifecycle, PKI/CA operations, production DR drills, hardware/firmware, observability cardinality/cost, capacity models and multi-cloud failure testing. |
| AI & ML Engineering | Existing domain; separate audit required | LLM/RAG, deep learning, ML, MLOps, vision, speech and responsible AI routes. | Distributed training, evaluation methodology, inference optimization, model governance, safety, feature lifecycle and production observability. |
| Software Engineering | Partial specialist coverage | Backend, frontend, architecture, languages, testing and developer tools. | Mobile framework coverage, secure SDLC depth, API compatibility and production testing. |
| Other domains | Mixed maturity | Broad discovery taxonomy with selected specialist packages. | Many subdomains remain mapped-only or have narrow starter skills; they are not complete professional capability packs. |

## Validation status

- YAML graph validation: **PASS** (276 indexed active skills; 186 registries; typed relations validated).
- Deterministic routing evaluation: **PASS** (297 fixtures; no failed cases).
- Coverage report: **PASS** (42 top-level domains; 276 indexed active skills; 68 maps).
- CLI, security and overlay unit tests: **PASS** (31/31).
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

## Interpretation

A Skill file or active YAML node is not proof of a complete capability. This audit separates taxonomy coverage, structural registration, deterministic routing, executable procedure, host compatibility and production evidence. Only the first three have meaningful automated evidence today; the latter stages remain incomplete.
