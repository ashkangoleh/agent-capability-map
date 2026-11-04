# Roadmap

## Current integration baseline — 2026-11-04

- Canonical branch: `pre_release`.
- Inventory: 41 top-level domains and 276 active SKILL.md packages.
- Validation: 297 deterministic routing fixtures and 31 unit tests pass on the current baseline.
- Data Engineering expansion is in progress; the first source-specific CDC tranche covers Oracle GoldenGate, SQL Server CDC/Change Tracking and MongoDB Change Streams.
- Next priorities: engine-specific warehouse skills, managed/event-streaming platforms, catalog and metadata operations, then deeper per-skill version and recovery evidence.

## Phase 1 — Foundation (current branch)

- Root operating contract and hierarchical routing.
- Broad cross-functional domain taxonomy.
- Local per-domain registries.
- Initial production-oriented starter skills.
- Evidence and anti-hallucination protocol.
- Registry validation and CI.
- Evaluation methodology.

## Phase 2 — Coverage expansion

Prioritize skills by actual recurring tasks and evaluation gaps:
- technology: API design, code review, testing strategy, security review;
- data: SQL optimization, Spark optimization, dbt modeling, data quality, streaming reliability, warehouse/lakehouse architecture;
- AI/ML: agent evaluation, prompt-injection defense, retrieval evaluation, model selection;
- product: product analytics, experimentation, roadmap prioritization, pricing;
- marketing: content strategy, lifecycle/CRM, performance marketing, attribution;
- SEO: technical crawl diagnostics, content briefs, local SEO, international SEO;
- design: design systems, accessibility audits, research synthesis;
- business: financial modeling, process analysis, sales enablement;
- research: literature review, source audit, executive reports;
- governance: privacy and compliance research with jurisdiction-specific safeguards.

## Phase 3 — Runtime adapters

- Validate behavior in Codex, Claude Code, and other target clients.
- Add a small registry query tool only if native skill discovery is insufficient.
- Add token and routing telemetry where the host exposes reliable measurements.
- Add cache invalidation and versioning for loaded skills and references.

## Phase 4 — Evaluation and governance

- Curated benchmark prompts for every active skill.
- Human-reviewed scoring rubrics.
- Regression gates for routing and evidence quality.
- Skill provenance, review ownership, and expiry metadata.
- Automated stale-reference checks where source URLs can be tested safely.

## Explicit non-goals for the foundation

- No graph database.
- No vector database for a small registry.
- No multi-agent orchestration by default.
- No claim of zero hallucination.
- No automatic execution of arbitrary skill scripts.

## Phase 2 — Initial specialist expansion (2026-11-03)

12 targeted SKILL.md packages added for dbt incremental models, data quality, data backfill, Structured Streaming, Kubernetes rollout, product experiments, product metrics, marketing measurement, SEO indexability, structured data, agent evaluation and editorial briefing. CI structural validation and deterministic routing fixtures do not replace host-level evaluation or human review.

## Cross-domain specialist expansion (2026-11-03)

A separate branch `feat/cross-domain-skill-expansion` adds 29 specialist skills across 29 previously unsupported or new top-level domains, plus 8 taxonomy extensions. All 41 top-level domains now have at least one active skill but complete subdomain coverage, semantic/multilingual routing, and independent host-level quality assessment remain planned work.

## Deep Data Engineering expansion — 2026-11-03

The branch `feat/data-engineering-deep-skills` adds 29 specialized skills and seven nested YAML maps plus activated Ray, Argo, Pulsar, RabbitMQ and Kinesis nodes across CDC, distributed processing, orchestration, lakehouse maintenance, warehouse engines, model governance and data observability. Technology-specific routes preserve generic fallbacks where the request lacks enough detail. Structural and lexical tests do not validate model correctness, cost or runtime semantics.

## Unified platform, analytics and ML reference branch — 2026-11-03

`feat/master-reference-platform-data-ai` consolidates all previously completed changes and adds **63** specialized SKILL.md files: Infrastructure 18, Data Science + Data Analysis/BI 17, AI/ML 17 and additional Data Engineering 11. The YAML graph now covers 41 top-level domains and 151 active skills. Future expansion should be prioritized by measured user tasks, routing false positives, quality regressions and maintenance ownership—not exhaustive buzzword enumeration.

Pending maturity gates: real agent-host integration tests beyond Claude Code, test-set generalization, human-reviewed skill output, vulnerability/permission testing, actual token budgets, reference freshness automation, and observable acceptance of production SLO/replay semantics.
