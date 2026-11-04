# Unified Capability Map — Consolidation and Completeness Audit

**Audit snapshot:** 2026-11-04  
**Consolidated branch:** `feat/unified-master-capability-map`  
**Baseline:** `main` plus the comprehensive Data Engineering, Data Science and Infrastructure work already present on `feat/comprehensive-data-science-infrastructure`.

## Consolidation result

The repository exposed one comprehensive feature branch containing the Data Engineering, Data Science and Infrastructure expansions. No separate live feature branches named for Data Science or Infrastructure were found in the repository branch search. This unified branch is therefore based on the complete comprehensive branch rather than attempting an unsafe unrelated-history merge.

- Consolidated source branch: `feat/comprehensive-data-science-infrastructure`
- Source head: `29505024130134fc4587990a7dba84e362a278b7`
- Delta against `main` at audit time: 60 commits ahead, 0 behind at source-branch snapshot; the unified branch adds consolidation fixes and audit documentation.
- Inventory at source head: 273 `SKILL.md` files and 42 top-level domain maps.
- `main` remains unchanged. This branch is not yet merged into `main`.

## Domain maturity assessment

| Domain | Assessment | What exists | What remains incomplete |
|---|---|---|---|
| Data Engineering | Broad structural coverage; operational depth uneven | Ingestion, CDC, batch/streaming, orchestration, transformation, formats, lakehouse/catalogs, warehouse/federation, quality, governance, DataOps, reliability, cloud, serving and architecture | Several packages are only starter guidance; missing versioned compatibility matrices, executable reference implementations, engine-specific failure/recovery playbooks, load/performance evidence, and broad positive/negative routing fixtures |
| Data Science | Medium; new taxonomy and skills added, not yet validated | Scientific computing, statistics, Bayesian methods, experimentation, causal design, classical ML, calibration, explainability, forecasting, survival, recommendation, graph, geospatial, simulation, optimization and text analytics | Sparse specialist coverage for survey design, missing-data MNAR sensitivity, robust/nonparametric inference, econometrics, NLP multilingual evaluation, advanced causal estimators, model fairness, uncertainty/calibration and real reproducible notebooks/datasets |
| Infrastructure Engineering | Broad taxonomy; operational implementation incomplete | IaC, GitOps, CI/CD, DevSecOps, SRE, networking, cloud, Linux/Windows, virtualization, storage, database operations, Kubernetes, service mesh and platform engineering | New packages need tested procedures and version matrices; gaps include IAM/identity lifecycle, PKI/CA operations, incident response runbooks, production DR drills, hardware/firmware, observability cost/cardinality, capacity models and multi-cloud failure testing |
| AI & ML Engineering | Existing domain; not audited as a full expansion in this change | LLM/RAG, deep learning, ML, MLOps, vision, speech and responsible AI routes | Needs separate coverage audit for distributed training, evaluation methodology, serving, inference optimization, model governance, safety, feature lifecycle and production observability |
| Software Engineering | Existing domain; partial specialist coverage | Backend, frontend, architecture, languages, testing and developer tools | Mobile development is mapped-only; needs framework-specific skills, secure SDLC depth, API compatibility and production testing |
| Other business/science domains | Mostly taxonomy-level | Broad top-level discovery maps | Many domains are map-only or have only a small number of generic skills; they are not complete professional capability packs |

## Explicitly mapped-only top-level domains

The root catalog explicitly marks these domains as having no specialized validated skills yet:

- content & publishing
- people & hr
- education & learning
- finance & accounting
- legal & compliance
- health & medicine
- science & mathematics
- e-commerce & retail
- sales & revenue
- customer experience & support
- media & entertainment
- games & interactive
- manufacturing & industry
- logistics & supply chain
- construction & architecture
- energy & sustainability
- agriculture & food systems
- government & public policy
- travel & hospitality
- sports & fitness
- personal productivity & life

This is not a defect if the intended state is discoverable taxonomy. It is incomplete if the requirement is production-grade coverage for every listed domain.

## Validation status and blockers

The initial GitHub Actions run exposed duplicate sibling route IDs and stale cross-domain relation endpoints. These were corrected by disambiguating the new specialist nodes and preserving the original statistics, geospatial and network registries.

```
Duplicate sibling ID orchestration: domains/data/data-engineering/map.yaml
```

The root catalog now validates with 273 unique active skill IDs. The remaining workflow failure at the last completed run is a stale unit-test assertion that expected 41 top-level domains; Data Science promotion correctly increases the count to 42. The assertion and coverage snapshot are being updated, then the workflow must be rerun.

The failed graph-validation step prevented the CLI/security/overlay test step from running. Therefore:
- YAML graph validation: **PASS** (273 unique active skills; 186 registries; 25 typed relations)
- Graph evaluation: **PASS** (289/291 routing fixtures at the previous run; two specialist triggers were corrected in the next commit; rerun pending)
- Coverage report: **PASS at structural step**; final refreshed report pending
- CLI, security and overlay unit tests: **30/31 passed**; one stale assertion expected 41 rather than 42 top-level domains
- Host compatibility (Codex, OpenCode, Copilot, Claude Code, etc.): **NOT VERIFIED**
- Semantic routing quality: **NOT MEASURED**
- Production readiness: **NOT ESTABLISHED**

## Required completion gates

1. Reproduce and fix the duplicate sibling ID; run the full workflow on this unified branch.
2. Verify every active registry path exists and every active skill ID is unique and present exactly once in the master index.
3. Validate all YAML references, typed cross-domain edges, cycles, route depth and unresolved paths.
4. Expand routing fixtures to include positive, negative, ambiguous, near-miss, multilingual and adversarial prompts across all three technical domains.
5. Test resolver behavior, not only registry parsing; record false-positive and false-negative rates.
6. Add per-skill version/context prerequisites, evidence requirements, safe execution boundaries and recovery/rollback behavior where relevant.
7. Add reproducible examples and versioned compatibility notes for major tools; distinguish conceptual skills from runnable integrations.
8. Run host-specific compatibility tests and record exact host/model/version combinations.
9. Only after required checks pass, open/review/merge the pull request to `main`.

## Interpretation

A skill file or active YAML node is not proof of a complete capability. This audit separates taxonomy coverage, structural registration, validated routing, executable procedure and production evidence. Only the first two are substantially represented today; the latter stages remain incomplete.
