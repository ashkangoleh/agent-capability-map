# Continuation Checkpoint — Agent Capability Map

**Updated:** 2026-11-04
**Canonical repository:** `ashkangoleh/agent-capability-map` (private)
**Canonical working branch:** `pre_release`
**Verified branch HEAD immediately before this update:** `67e553cf6306313cee486e2ef205c96cdae8e831` (always fetch HEAD again in a new chat)
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
- `catalog/master-skill-ids.yaml` now contains **344 unique listed skill IDs** (counted directly after three new catalog specialists).
- `README.md` now distinguishes **344 current registered IDs** from the historical verified **322**; `docs/UNIFIED_COMPLETENESS_AUDIT.md` retains its old audit section and adds a dated post-audit delta. The 344 indexed IDs require a fresh full graph validation before being called 344 active/proven specialist skills.
- At the earlier audit, the repository had **41 top-level domains**, **16 Infrastructure selectable scopes**, **95 unique Infrastructure specialists**, **348 routing fixtures**, **54 unit tests**, and **83 nested maps**. The current fixtures YAML has **385 cases**; no full-suite passing result has been established against the newest branch.
- The prior audit explicitly shows Infrastructure and Data Science have strong structural coverage but lack independent production/host evaluation. The nine Data subdomains are not all audited.
- The newer Data Engineering coverage test explicitly enumerates **19 additional Data Engineering specialist skill IDs**, and the current registry/index shows them. Their source and positive tests exist; execution of the whole Python suite still needs confirmation.
- GitHub connector returned no associated PR workflow runs or combined status checks for the last observed commit. **Do not say the latest CI is green** on that evidence alone.
- Real semantic routing accuracy, false activation rates, actual token usage improvements and end-to-end multi-host compatibility remain unmeasured/unverified.

## Current active domain and unresolved work

**Current working domain: `data/data-engineering`. It is not finished.**
Cross-check `docs/DATA_ENGINEERING_TOOL_MATRIX.md`, `docs/DATA_ENGINEERING_SKILLS.md`, and `docs/DATA_DOMAIN_COMPLETENESS_STATUS.md`.

Documented gaps include managed warehouses (Snowflake/BigQuery/Redshift/Databricks SQL) and their operating procedures; broker and streaming-SQL breadth; catalog operations; version-specific compatibility; reproducible implementations; recovery, idempotency and replay; and comprehensive negative/ambiguous/mixed Persian-English routing evaluations. Some individual skills may already exist: audit before creating duplicates.

Data Science: 26 defined areas have structural routes and 42 specialist skills, but independent expert validation and version-tested examples remain.
Infrastructure: 16 first-class scopes and 95 specialist skills (historical report), but independent operational/compatibility validation remains.
Other domains should only be taken up after user approval.

## Work completed in the 2026-11-04 continuation

Completed on `pre_release` without creating or merging branches:

- Added three domain-specific `SKILL.md` packages:
  - `iceberg-rest-catalog-operations`: Iceberg REST discovery, short-lived storage credentials, concurrent/indeterminate commits and cross-engine interoperability.
  - `nessie-versioned-catalog-operations`: Project Nessie branches/tags, conflict-aware merges and native API vs Iceberg REST migration. Vendor docs currently flag its Iceberg REST integration as experimental; verify target release.
  - `gravitino-federated-catalog-operations`: Gravitino metalakes, federated metadata, Iceberg REST service separation, version-gated features and upgrade recovery.
- Added separate registries and first-class catalog children; updated all required ancestor YAML triggers while preserving `Polaris` and `Lakekeeper`. The generic Iceberg REST route excludes the four implementation names.
- Added `tests/test_iceberg_rest_catalog_coverage.py` and `tests/test_catalog_vendor_coverage.py`. Added **15** deterministic positive/near-miss/mixed-language fixture cases; total fixture count **385**. Updated `README.md`, `docs/DATA_ENGINEERING_SKILLS.md`, `docs/DATA_ENGINEERING_TOOL_MATRIX.md`, `docs/DATA_ENGINEERING_CATALOG_OPERATIONS.md`, and `docs/UNIFIED_COMPLETENESS_AUDIT.md`.
- A **separate JavaScript reconstruction** of Python lexical matching against the actual GitHub YAML produced the expected routes on **15/15 new cases**; simple source/index checks found 344 unique IDs and all expected skill headings. This is **not** an actual Python unittest, `Router.validate()` execution or GitHub Actions result.
- The GitHub connector did not return traditional commit status checks and only exposes PR-triggered workflow runs. The push-workflow status remains **UNKNOWN / NOT VERIFIED**. Do not assert green CI or production readiness.

### Scope remaining inside Data Engineering

1. Run the actual Python validator, deterministic fixture runner, unit suite, and coverage script on `pre_release` HEAD; inspect the `validate.yml` push workflow. Fix any failures before adding further skills.
2. Version-test Polaris, Lakekeeper, Nessie and Gravitino using official **release-pinned** docs and at least one integration fixture per provider; especially branch merges, delegated credentials and catalog metadata recovery.
3. Next capability family *within Data Engineering*: broker and streaming SQL operations, negative/ambiguous routing and production failure/replay examples. Then warehouse execution and managed-service compatibility. Only proceed to other top-level domains with explicit user approval.
4. Continue a broader semantic/host-routing benchmark; don't convert deterministic lexical fixture passes into ungrounded accuracy estimates.

## Immediate next action for a follow-up conversation

1. Fetch `pre_release` HEAD and read this checkpoint and `docs/UNIFIED_COMPLETENESS_AUDIT.md`; the branch may advance beyond any SHA in this file.
2. Run `python -m capability_map validate`, `python scripts/evaluate_graph.py`, `python scripts/report_coverage.py --summary` and `python -m unittest discover -s tests -v` against current HEAD. Investigate any failures and inspect the push CI run. Never report PASS based on static fixtures alone.
3. Stay in **Data Engineering**. Finish catalog integration/compatibility evidence or advance to the next gap family (brokers and streaming SQL), with focused skills, negative/ambiguous fixtures and production recovery details. No unrelated domain work.
4. After a domain reaches verifiable acceptance gates, explain remaining limits and **ask which domain to work on next**. Do not choose the next domain unilaterally.
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
