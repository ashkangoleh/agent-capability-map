# Continuation Checkpoint — Agent Capability Map

**Updated:** 2026-11-04
**Canonical repository:** `ashkangoleh/agent-capability-map` (private)
**Canonical working branch:** `pre_release`
**Verified branch HEAD before this checkpoint:** `18ae642a95d4d9dc4f58d726f61d557de5b20e75`
**Integration policy:** Work only in `pre_release` unless the user explicitly changes this. Do not merge into `main` without explicit approval. Do not create `feat/*` or `fix/*` branches for this work.

## Product intent — non-negotiable

Create a broad, role-agnostic **Global Master Skill / Capability Router**, not a single-domain project and not a prompt that loads every skill. It should work for software engineers, data engineers, infrastructure/platform/SRE, data science, analytics, marketing/SEO, business and other roles.

Routing architecture:

```text
Small host-specific global bootstrap
  -> global master YAML root
  -> selected top-level domain
  -> selected subdomain (nested as needed)
  -> capability / technology registry
  -> validated prebuilt SKILL.md
  -> optional references and scripts on demand
```

Host targets: Codex, Claude Code, OpenCode, GitHub Copilot and Cursor (actual integration must be tested separately per host). Follow the Agent Skills `SKILL.md` standard. Use progressive discovery/loading, avoid bulk skill injection, and distinguish *mapped taxonomy* from *active registered skills* and *execution-proven procedures*. Keep personal/project overlays explicit, collision-safe and separate from the master library. Requests should route from natural task intent; manual slash commands are not a required interface.

Domain selection: users choose **up to five non-overlapping selectable domain scopes** in one application (including nested scopes such as `data/data-engineering`). Parent+child double selection is rejected. Selection is a user-level allowlist, fails closed with `domain_not_enabled`, and does not mean loading every descendant skill into context. User-controlled domain selection is already implemented. Preserve the existing dry-run / `--apply` semantics.

## User's collaboration rules

1. **Work one domain at a time.** Finish its inventory, gaps, implementation and validation before proposing the next domain.
2. **Ask the user for approval before moving to the next domain.** Do not autonomously switch domains even if other domains have known gaps.
3. Keep specialist coverage very broad but never claim literally complete or production-ready without evidence. Prioritize meaningful procedures, not empty `SKILL.md` wrappers or a large count.
4. Make small, traceable increments with concrete file names, tests and remaining risks. Do not make unnecessary new branches.
5. Maintain this checkpoint after substantive milestones so a new ChatGPT conversation can recover exact current goals, status, next action, current branch and SHA.

## Verified state on 2026-11-04

- Repository is private; branch `pre_release` exists and is **104 commits ahead of `main`, 0 behind** at the pre-checkpoint reference. `main` is not merged.
- The latest branch HEAD immediately before this checkpoint is `18ae642a95d4d9dc4f58d726f61d557de5b20e75`, a test fix replacing brittle exact global skill-count assertions with lower bounds.
- `catalog/master-skill-ids.yaml` currently contains **341 listed skill IDs** (counted directly).
- `README.md` and `docs/UNIFIED_COMPLETENESS_AUDIT.md` still state **322 active skills**; these inventory claims are **stale relative to the ID index and require a fresh report and registry validation**. Do not equate 341 indexed IDs with 341 independently validated, execution-proven skills.
- README reports **41 top-level domains**, **16 Infrastructure selectable scopes**, **95 unique Infrastructure specialists**, **348 deterministic routing fixtures**, **54 unit tests**, and **83 nested maps** at its prior audit. Treat these figures as historical until rerun on current HEAD.
- The prior audit explicitly shows Infrastructure and Data Science have strong structural coverage but lack independent production/host evaluation. The nine Data subdomains are not all audited.
- The most recent user discussion reported **19 additional Data Engineering specialist skills**; verify the exact skills via the branch diff and latest registry before describing them as finished.
- GitHub connector returned no associated PR workflow runs or combined status checks for the last observed commit. **Do not say the latest CI is green** on that evidence alone.
- Real semantic routing accuracy, false activation rates, actual token usage improvements and end-to-end multi-host compatibility remain unmeasured/unverified.

## Current active domain and unresolved work

**Current working domain: `data/data-engineering`. It is not finished.**
Cross-check `docs/DATA_ENGINEERING_TOOL_MATRIX.md`, `docs/DATA_ENGINEERING_SKILLS.md`, and `docs/DATA_DOMAIN_COMPLETENESS_STATUS.md`.

Documented gaps include managed warehouses (Snowflake/BigQuery/Redshift/Databricks SQL) and their operating procedures; broker and streaming-SQL breadth; catalog operations; version-specific compatibility; reproducible implementations; recovery, idempotency and replay; and comprehensive negative/ambiguous/mixed Persian-English routing evaluations. Some individual skills may already exist: audit before creating duplicates.

Data Science: 26 defined areas have structural routes and 42 specialist skills, but independent expert validation and version-tested examples remain.
Infrastructure: 16 first-class scopes and 95 specialist skills (historical report), but independent operational/compatibility validation remains.
Other domains should only be taken up after user approval.

## Immediate next action for a follow-up conversation

1. Fetch `pre_release` HEAD and read this checkpoint and `docs/UNIFIED_COMPLETENESS_AUDIT.md`; do not trust this file's SHA as permanent.
2. Run or independently validate live inventory, YAML graph, routing fixtures and Python tests. Reconcile 341 ID-index count against 322 stale report. Check latest GitHub Actions checks before declaring a pass.
3. In **Data Engineering only**, compare the actual newly added 19 skills, routes, official sources and negative tests against the gap matrix. Close missing operational coverage in small focused commits, one capability family at a time.
4. After demonstrable completion, report what is and is not verified, then **ask which domain to take next**. Do not choose the next domain unilaterally.
5. Update this file with new HEAD, active domain, progress, gaps, test evidence and next agreed task.

## Quality gates before calling a domain complete

- Accurate taxonomy plus live registered skill inventory; no broken links, duplicate IDs or silent overlays.
- Each important skill has scoped triggers/exclusions, operational workflow, inputs, realistic failure/recovery, quality and security boundaries, official references, and version caveats where needed.
- Positive, negative, near-miss, ambiguous and bilingual routing tests; anti-false-positive and abstention behaviors.
- Report validation, deterministic routing and unit-test status at the *actual* current HEAD.
- Explicitly distinguish structural correctness from model/host behavioral evaluations and production certification.

## Primary reading order

1. `README.md`
2. `docs/CONTINUATION_CHECKPOINT.md`
3. `docs/UNIFIED_COMPLETENESS_AUDIT.md`
4. `docs/DATA_DOMAIN_COMPLETENESS_STATUS.md`
5. `docs/DATA_ENGINEERING_TOOL_MATRIX.md`
6. `docs/INFRASTRUCTURE_COVERAGE_AUDIT.md`
7. `docs/DOMAIN_SELECTION.md`

**Required correction discipline:** When a document conflicts with the current files or test results, trust the currently verified source, report the discrepancy, and update stale documentation only after validation.
