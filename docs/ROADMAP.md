# Roadmap

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
