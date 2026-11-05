# Continuation Checkpoint — Agent Capability Map

**Updated:** 2026-11-05
**Canonical repository:** `ashkangoleh/agent-capability-map` (private)
**Canonical working branch:** `pre_release`
**Verified branch HEAD immediately before this update:** `67e553cf6306313cee486e2ef205c96cdae8e831` (always fetch HEAD again in a new chat)
**Integration policy:** Work only in `pre_release` unless the user explicitly changes this. Do not merge into `main` without explicit approval. Do not create `feat/*` or `fix/*` branches for this work.

## LATEST ACTIVE CHECKPOINT — Infrastructure hierarchical roles + cross-platform CLI (2026-11-05)

- Working branch `pre_release`, verified baseline before changes `fe54e763f7fb9e01e9598927eea266681edb1cf1`. No `main` merge and no other branches.
- Added **96** new `domains/infrastructure/<logical-route>/ROLE.md` contracts to existing Infrastructure root role. Expected **97/97** active graph nodes across **22** Infrastructure map files with independent roles, including 16 first-level scopes and deep Kubernetes/Network Advanced/DevSecOps/GitOps/CI-CD.
- New role inventory expected: **263** roles (127 Data, 97 Infrastructure, 39 other roots). Existing SKILL.md content, registration, ids, triggers and status unchanged: 344 total / 95 Infrastructure / 0 flat.
- Dynamic `tests/test_domain_roles.py` inventory asserts no missing/orphan Infrastructure role, exact logical routes, no inheritance truncation, <=8192 bytes per selected route, and representative route checks.
- Added cross-platform Node CLI `node/bin/capability-map.mjs` with `package.json` bin `capability-map-node`, local `npm link`. This is a `shell:false` Python subprocess bridge requiring Python >=3.10, installed project and source checkout. NOT a Node-only implementation, NOT published to npm.
- Improved host instruction generation to embed `--root` and platform-specific Unix/PowerShell quoting. Enabled Claude role directory read access and scoped Edit-deny settings; still not OS-level read-only. Added Python CLI and Node integration tests and a Windows+Ubuntu GitHub Actions matrix.
- Docs: `docs/CROSS_PLATFORM_CLI.md`, `docs/DOMAIN_ROLE_DESIGN_BACKLOG.md`, `docs/HOST_COMPATIBILITY_ACCEPTANCE.md` and README.
- Full CI against **new commit** is REQUIRED. Current modifications are not yet production-certified, real native agents not tested, no measured A/B role quality improvements; the remaining **39** top-level domains still lack complete nested role hierarchies.
- Next domain requires explicit user approval; stay scoped to Infrastructure and cross-platform launcher fixes until CI is green.

## HISTORICAL CHECKPOINT — Data role inheritance fixture repair (2026-11-05)

- Previous `pre_release` HEAD: `831d5d0ac61d725314aa11eaa81ecf18e574e9d0`. Workflow run `42056541209` graph/routing checks PASSED; the full unittest phase FAILED only two stale test expectations for Airflow/Kafka role inheritance (225 tests, 2 failures, 1 skipped).
- Both requests resolve their correct existing skills and now return a more specific leaf role, at `data/data-engineering/orchestration/airflow` and `data/data-engineering/messaging/kafka` respectively. Old test expectations stopped at the parent. Corrected exactly these two expectations; no role files, skill bodies, routing semantics or allowlist policy modified.
- Re-run full GitHub Actions for the new commit before marking the migration green. The 127/127-role Data inventory test had passed independently in the failed run.

## HISTORICAL CHECKPOINT — Complete Data Graph role coverage (2026-11-05)

- Verified baseline `pre_release` HEAD `9cdd9e1a665bae6e87a8c7d6c2d4b59ac078e6f7`, full CI run `42055168134` passed for hierarchical role loading (YAML graph + full tests). Do not merge `main` or create feature branches.
- Added 58 additional distinct Data specialist ROLE.md files across analytics engineering, BI, data analysis, relational/database engineering, governance, messaging, orchestration, streaming SQL, Lakehouse catalogs, and warehouse/cloud engines.
- Total now **127 Data role contracts including Data root**, corresponding to **all 127 active logical Data graph nodes** across 21 map files. Each node's `role_id` is its **logical route**, not its sometimes-different physical YAML map path. All 41 top-level domain roles remain; repository total roles should be **167** (41 root + 126 nested Data).
- Added dynamic `test_complete_data_graph_role_inventory` to traverse all active Data node scopes; enforce role existence, exact route ownership, no orphan role contract, 21 maps and 127 role scopes. This is structural coverage only, **not** demonstration of answer quality or production validity.
- `role_paths` list is parent-to-child, with compatibility `role_path` alias and bounded 8 files/8192 bytes, only after master matched result. Domain allowlist and overlays remain constrained. New domains/subdomains require role contracts when they become part of the relevant rollout.
- Expected inventory remains 344 SKILL.md total, 95 Infrastructure and 0 flat; do not claim CI for this new head until GitHub Actions run is independently checked.
- Next domain role hierarchy is Infrastructure **only after explicit user approval under one-domain-at-a-time workflow**; native five-host and A/B quality evaluations remain UNVERIFIED.

## HISTORICAL CHECKPOINT — Hierarchical Domain Roles, Data Pilot (2026-11-05)

- Baseline `pre_release` HEAD `95e1da143ab5dfb3cdd4069062e76676d2a52b1d`; no main merge or feature branch. User requires **independent specialist roles at meaningful hierarchical layers**, not only root domains.
- Added support for parent-to-child `role_paths` on matched master results; preserved existing top-level `role_path` compatibility alias, existing skill_id and skill_path, and five-domain user allowlist. Overlay/non-matched results provide no role paths.
- Canonical nested role location: `domains/<logical-route-components>/ROLE.md`, validated against route IDs and safe paths; optional nested roles inherit the parent if absent; invalid nested roles fail closed. Max **8 roles / 8192 bytes** combined, 4096 per file.
- Data-only pilot creates independent roles at nine first-level Data subdomains, domain-specific second-level branches and deep Spark and recovery paths. No automatic role for every trivial routing node. The exact added role inventory and validation results must be counted from Git tree and tests; do **not** claim all nested roles for 41 domains are finished.
- Updated bootstrap and installer to read the returned role_paths in order; changed instructions and regression tests, not routing triggers, skill bodies, permission grants or registered domain scopes.
- Required validation: 344 global skills, 95 Infrastructure, zero flat and all 41 root roles, all 469 routing fixtures, complete unit suite. Check push CI for **new** commit SHA, separately from base `95e1da143ab5dfb3cdd4069062e76676d2a52b1d`.
- Follow-up: evaluate actual quality of the Data roles, finish missing meaningful Data subdomains, then continue Infrastructure and other domains **one domain at a time**, checking user approval before advancing when appropriate. Native host load behavior and measured response improvement remain unverified.

## HISTORICAL CHECKPOINT — Domain roles for all 41 active top-level domains (2026-11-05)

- Baseline `pre_release`: `a559a69e926adbea86a4eaad4760d434bff321fd`. User explicitly authorized roles for **all current domains**, not just Infrastructure. Do not merge `main` or create branches.
- Add `domains/<domain-id>/ROLE.md` for every active top-level domain in `catalog/root.yaml` (41). Each is a concise domain-specific output-quality review contract, **not a skill**.
- `capability_map/router.py` now validates role metadata, fixed safe paths, size and section schema; `Router.validate()` checks all top-level roles. For `matched` master results only, the resolver adds `role_path`. Disabled/unmatched/ambiguous/overlay results do not advertise any role. User scope max-five selection and all skill routing remain unchanged.
- `AGENTS.md` and all host installer instruction texts tell hosts to read the single matched role and selected skill, without scanning sibling domains. This is progressive loading guidance only; no measured LLM uplift, no native-host runtime test, no permission boundary guarantee.
- New `tests/test_domain_roles.py` covers full catalog, semantic contract fields, role file safety, match/blocked/overlay behavior and installer contract. Expect 344 total skills, 95 Infrastructure, zero flat; 469 preexisting routing fixtures unchanged.
- Check latest commit CI exact HEAD before claiming PASS; green tests cannot prove all 41 roles improve answer quality. A/B evaluation by domain is still outstanding.

## HISTORICAL CHECKPOINT — Kubernetes Operator and DR specialist-depth review + domain roles backlog (2026-11-05)

- Canonical working branch is `pre_release`. Baseline verified HEAD before this change: `8bc0555ce36309da76f7857f2f9bca088947d475`. Do not merge to `main` or create new branches.
- Updated **exactly two** existing SKILL.md bodies: `kubernetes-operator-crd-lifecycle` and `backup-dr-restore-exercises`; metadata version `1.0.0` → `1.1.0`. Stable IDs, physical paths, source registries, triggers and excludes unchanged.
- Kubernetes Operator/CRD content now covers schema validation, controller idempotent reconcile, status and observedGeneration, deletion finalizers, conversion webhook/served/storage versions, stored-version migration, rollback limitations, failure injections and real evidence.
- Backup/DR content now covers dependency-aware recovery points, backup immutability/keys, isolation, PITR, actual RPO/RTO evidence, consistency and validation, split brain, failback and cost/cleanup.
- Added focused content/path/routing regression test in `tests/test_infrastructure_coverage.py` and audited the corrective rationale in `docs/INFRASTRUCTURE_COVERAGE_AUDIT.md`. No fixture count change (469).
- **Explicit user requirement for future work:** design a separate quality-enhancing **role per domain**. Captured in `docs/DOMAIN_ROLE_DESIGN_BACKLOG.md`; this is **not implemented**, must be optionally loaded only after authorized skill resolution, preserve minimal bootstrap, avoid redundant role stacking, and be evaluated per-domain with host/quality/token/security tests before rollout. Infrastructure pilot role candidate is Principal Infrastructure Reliability & Platform Architect.
- Do not claim production compatibility or tested RPO/RTO; **no Kubernetes cluster or AWS resource was operated**. Final gate: verify GitHub Actions run bound to the new commit SHA; required inventory stays 344 total/95 Infrastructure/0 flat.
- Infrastructure overall expert-depth/completeness remains **NOT CERTIFIED** and next domain is blocked pending explicit user approval.

## HISTORICAL CHECKPOINT — Falco specialist-depth review (2026-11-05)

- Baseline `pre_release` HEAD: `c4918e585f5153de82275b9615625ce2d1731a59`. Continue Infrastructure only; no branch creation or main merge.
- After completing DevSecOps, Kubernetes and SRE structural splits, reviewed representative SKILL.md bodies and found a **nontrivial quality gap**: the Falco runtime skill had generic SAST/DAST/SCA content rather than Falco-specific detection, event-drop and driver operations.
- Updated the existing `runtime-security-falco` SKILL.md in place to version `1.1.0`. Kept ID, description, registry, triggers, scope and physical path unchanged. Added official-source-grounded preflight, modern eBPF/kmod driver handling, ruleset validation/overrides, safe rollout/rollback, event/drop/output metrics and benign-event validation.
- Added a focused `test_falco_runtime_skill_is_operationally_specific` regression test in `tests/test_infrastructure_coverage.py` and an audit explanation in `docs/INFRASTRUCTURE_COVERAGE_AUDIT.md`.
- No real Falco binary, kernel drivers, Kubernetes cluster or external host was executed. Claims of production rule validity, runtime compatibility and performance **NOT VERIFIED**.
- Current inventory should remain 344 total SKILL.md, 95 Infrastructure, 0 flat; 469 deterministic fixtures unchanged. Check the new SHA's CI before reporting PASS.
- Representative spot-check found Kubernetes Operator and Backup/DR skills also contain generic procedures. They are next candidates for version-pinned content audit, not automatically certified by green CI.

## HISTORICAL CHECKPOINT — Infrastructure SRE taxonomy (2026-11-05)

- Baseline `pre_release` HEAD: `6bb09f00c3866234ec633a9f4cb29e86d8034fed`; only Infrastructure work is authorized. No `main` changes and no new branches.
- Decomposed the four-skill `sre-practices` registry into explicit `slo-governance`, `capacity-engineering`, `failure-injection` and `disaster-recovery` routes under `domains/infrastructure/sre-reliability/map.yaml`.
- Four SKILL.md manifest Git blobs are relocated byte-for-byte to `.agents/skills/infrastructure/sre-reliability/<category>/<skill-id>/SKILL.md`; original content, skill IDs, triggers, excludes and descriptions preserved. Removed old registry/path entries.
- Added targeted tests for four existing `infra-expanded-` fixtures and a negative near-miss to retain Incident Management ownership. Existing 469 routing fixtures remain unchanged.
- Required CI gates: validate all YAML maps, 469 fixtures and full unit suite at **new** commit SHA. Required physical inventory 344 global / 95 Infrastructure / 0 flat.
- Scope is structural routing only; Infrastructure remains incomplete pending specialist code/procedure reviews, version-pinned system testing, injected failures, multi-host validation and source-aligned taxonomy for other categories.

## HISTORICAL CHECKPOINT — Infrastructure Kubernetes split (2026-11-05)

- Previous `pre_release` HEAD: `9196917d7467134e15e1f0e46576dda14b386337` (DevSecOps split; CI must be confirmed independently for that commit).
- Continued **Infrastructure only**, no new branch or merge to `main`.
- Split `domains/infrastructure/kubernetes/skills.yaml` (3 skills) into three independent leaf registries: `cluster-lifecycle`, `operators-extensions`, `cni-datapath`; replaced the overloaded `cluster-lifecycle` entry in `domains/infrastructure/kubernetes/map.yaml`.
- Relocated three existing SKILL.md files to `.agents/skills/infrastructure/containers-orchestration/kubernetes/<category>/<skill-id>/SKILL.md` with identical Git blob SHAs. Deleted old source paths and broad registry. All original skill bodies, IDs, triggers and excludes preserved.
- Added positive route/category/path checks for three existing fixtures and a NetworkPolicy-vs-CNI near-miss regression to `tests/test_infrastructure_coverage.py`. No existing fixtures modified.
- Required inventory: 344 global manifests, 95 Infrastructure, 0 flat; full YAML graph validation, all 469 routing fixtures and Python unit tests must pass against **this new SHA** before marking successful.
- Outstanding: SRE broad registry, historically mismatched source taxonomy, genuine negative/ambiguous multilingual benchmark, official version-pinned operations audit for 95 skills and real five-agent loading/allowlist tests. Infrastructure **NOT fully production-certified**.

## HISTORICAL CHECKPOINT — Infrastructure DevSecOps category isolation (2026-11-05)

- Base HEAD: `32b4f903d3214e46d6b8252eeb26afcfa50ece9d` on `pre_release`. This increment remains **Infrastructure-only**; no branch creation or `main` changes.
- Decomposed a six-entry `domains/infrastructure/devsecops/skills.yaml` registry into `domains/infrastructure/infrastructure-security/devsecops/map.yaml` with four leaf categories (`policy-gates`, `supply-chain`, `runtime-security`, `workload-identity`) and dedicated skill registries.
- Reused original six SKILL.md Git blob SHAs at new paths under `.agents/skills/infrastructure/infrastructure-security/devsecops/<category>/<skill-id>/SKILL.md`. Deleted their old physical paths, and the obsolete broad registry.
- Updated `domains/infrastructure/infrastructure-security/map.yaml` to follow the DevSecOps submap. All IDs, contents, skill triggers, excludes and **469** existing fixtures remain the same; only the routing path gains one category.
- Extended `tests/test_infrastructure_coverage.py` to verify 6/6 existing fixture resolutions, exact category routes, one-to-one registry ownership, canonical paths and removal of flat/old DevSecOps paths.
- Structural invariants required: **344** global skill manifests, **95** Infrastructure manifests, **0** flat legacy manifests, and exactly six unique DevSecOps specialists.
- `CI` for this new commit must be verified by matching the GitHub Actions run's head SHA, not inherited from `32b4f903d3214e46d6b8252eeb26afcfa50ece9d`.
- Additional Infrastructure gaps remain: cluster-lifecycle Kubernetes, SRE and other multi-skill registries; negative/ambiguous/bilingual routing benchmarks; per-skill source/version audits and failure-injection recovery procedures; native integration and domain allowlist enforcement on five actual agent hosts.
- External evidence: CNCF TAG Security cloud-native security lifecycle/supply-chain guidance. This supports taxonomy boundaries, not correctness certification.

## HISTORICAL CHECKPOINT — Infrastructure all-specialist fixture inventory (2026-11-05)

- Baseline `pre_release` commit: `c72c9be560f198b7d90f30e4a72c4b5bb48abfd7`. Continue **Infrastructure** only; user did not authorize moving to other domains.
- After auditing all **95** active Infrastructure IDs against `tests/fixtures/yaml-routing-cases.yaml`, **94/95** had a deterministic matching fixture; `platform-operations` had none.
- Added two platform-operations fixtures (English and Persian/English) and a dynamic test in `tests/test_infrastructure_coverage.py` requiring at least one matched routing fixture for every active Infrastructure skill ID. Fixture total increases from 467 to **469**; skill inventory remains **344 total**, **95 Infrastructure**.
- This is a **fixture reachability gate only**. It does not establish semantic classification correctness, false-positive/negative rates, operational production readiness, or real host skill loading.
- Check the current HEAD's **push CI** graph/fixture and full unit suite before asserting PASS. Additional negative/near-miss and real-version operations evidence remain open.
- Earlier infrastructure Advanced Networking 7-skill migration (commit `c72c9be560f198b7d90f30e4a72c4b5bb48abfd7`) must have green CI before relying on its new hierarchy.

## HISTORICAL CHECKPOINT — Infrastructure Advanced Networking taxonomy (2026-11-05)

- Canonical branch: `pre_release`; verified baseline HEAD: `8d0e3324185619f26e21ed3b1cc74edf217f4c2e`. Never merge `main` or open new feature/fix branches for this work.
- User explicitly prioritized Infrastructure before any other domain. There are **95 Infrastructure specialist manifests**, **16 first-level active scopes**, all physical skills are domain nested; expert-depth, semantic routing quality and host compatibility remain **NOT CERTIFIED**.
- Identified `domains/infrastructure/networking/map.yaml` → `network-advanced` as an overloaded seven-skill registry; created `domains/infrastructure/networking/network-advanced/map.yaml` with five real capability categories and five dedicated registries.
- Migrated seven SKILL.md manifests (each reuses its exact prior Git blob SHA) under `.agents/skills/infrastructure/networking/network-advanced/<category>/<skill-id>/SKILL.md`; deleted the seven old paths and stale `domains/infrastructure/network-advanced/skills.yaml`.
- Preserved all seven skill IDs, complete Markdown bodies, triggers, exclusions and existing deterministic fixture cases. Route strings now have one extra category level: `infrastructure/networking/network-advanced/<category>`.
- Extended `tests/test_infrastructure_coverage.py` to assert all seven fixture selections, exact hierarchical route, canonical source path, absence of obsolete source and bounded file inspection.
- Structural invariants required after commit: 344 physical skill manifests, 95 Infrastructure skills, zero flat legacy manifests. CI on the new HEAD must pass graph validation, deterministic fixtures and full Python test suite before stating green.
- **Remaining Infrastructure work:** inspect other broad registries (DevSecOps, Kubernetes cluster-lifecycle, SRE) and historically inconsistent source paths; audit 95 specialist procedures against official versioned docs with failure/recovery tests; perform real-agent host benchmarks. Do not treat physical nesting, one successful CI, or the agent-skills format as evidence of domain professional completeness.
- Latest previous successful CI: `42016010204` at `8d0e3324185619f26e21ed3b1cc74edf217f4c2e`. A new CI outcome is necessary for this change.

## HISTORICAL CHECKPOINT — Host-bootstrap verification contract (2026-11-05)

- Baseline HEAD before this change: `a65d48a59188ea00a16840b4b846deea31a2c9e1` on `pre_release`.
- Final 16 flat skill migration **PASSED** full GitHub Actions run `42014842454` at `1678fe619d708071131e98e0db52764c202629ae`.
- Recovery registry isolation **PASSED** full GitHub Actions run `42015373146` at `a65d48a59188ea00a16840b4b846deea31a2c9e1`.
- Added `tests/test_host_bootstrap_contract.py` to test simulated installation for Codex, Claude Code, OpenCode, GitHub Copilot and Cursor into an isolated temporary home, and explicit resolver selection for the nested recovery skill. No actual agent host is launched.
- Added `docs/HOST_COMPATIBILITY_ACCEPTANCE.md` for version-specific native discovery distinctions, explicit router-vs-native loading boundary, scope isolation, production risks and required live host acceptance protocol.
- Cleaned stale/repeated skill-library README lines; maintained 344/344 nested physical skill manifests and no changes to SKILL.md bodies or 467 routing fixtures.
- **Critical:** raw source native discovery can advertise skills outside the user's selected scope; the Python router's domain allowlist does not automatically govern native host skill scanners. Explicit bootstrap resolver is the supported integration. Live host invocation and scope enforcement remain **NOT VERIFIED**.
- The post-commit CI for this host-contract change must be checked; do not claim PASS for a new SHA by relying on the two preceding green runs.
- Data top-level completeness and production host compatibility still need independent evidence. No other domain scope added.

## HISTORICAL CHECKPOINT — Recovery registry isolation (2026-11-05)

- Branch: `pre_release`; baseline SHA before this change: `1678fe619d708071131e98e0db52764c202629ae`.
- Created `domains/data/data-engineering/batch-ingestion/recovery/skills.yaml` containing the **unchanged** existing `pipeline-backfill-recovery` registry record.
- The `recovery` child of `domains/data/data-engineering/batch-ingestion/map.yaml` now uses the dedicated registry rather than `domains/data/general-skills.yaml`.
- Removed the backfill specialist's former record from `domains/data/general-skills.yaml`, leaving the unrelated general entries intact. This prevents recovery from offering dbt/general engineering choices and stops the database generic route from advertising a backfill specialist.
- Updated `tests/test_data_engineering_coverage.py` to assert isolated registry contents, canonical manifest path, no stale entry in the shared general registry and representative backfill routing. Existing routing fixtures remain unchanged.
- Physical manifest count stays **344/344 nested, 0 flat**, with no changes to any SKILL.md contents or IDs.
- This is an intentional routing-visibility change; recheck actual GitHub Actions graph, routing fixtures and the entire unittest suite on the new commit before reporting PASS.
- The remaining `data/general-skills.yaml` still serves the database relational generic route; its broader generic skills need separate semantic review, not an unreviewed renaming or wholesale deletion.
- Host-native skill discovery and actual LLM invocation across five target clients: **NOT VERIFIED**. Data subdomain specialist completeness: **NOT VERIFIED**.

## HISTORICAL CHECKPOINT — Final 16 legacy-flat skills nested (2026-11-05)

- Canonical working branch: `pre_release`; baseline HEAD before this migration: `61b304fdf8e4749bcd87a5de76912c2f79968c63`. Do not merge `main` or create feat/fix branches.
- Migrated all 16 remaining flat `SKILL.md` manifests to domain/category paths, retaining **identical Git blob SHA** for each moved file; no SKILL body, ID, trigger, exclusion or routing map changed. The migrated skill folders had no bundled sibling source files.
- Updated exactly eight owner registries: `domains/agent-systems/graph-skills.yaml`, `domains/business/graph-skills.yaml`, `domains/infrastructure/database/new-specialists.yaml`, `domains/marketing/graph-skills.yaml`, `domains/product/graph-skills.yaml`, `domains/seo/graph-skills.yaml`, `domains/research/graph-skills.yaml`, `domains/design/graph-skills.yaml`.
- Canonical physical layout now **344/344 nested, zero flat** (structural only); verify final Git tree before declaring this checked.
- Added a global source/registry consistency test ensuring every physical `SKILL.md` is registered, registered paths have one physical manifest, every manifest is under its owning top-level domain and no legacy flat path remains.
- The current `data/data-engineering/batch-ingestion/recovery` route still references a shared general registry; changing this routing semantics requires separate tests and an independent change.
- Validation gates: check post-commit GitHub Actions push run including YAML graph/fixture and entire unittest suite; do not claim PASS from old runs. Native discovery/integration for Codex, Claude Code, Cursor, Copilot, and OpenCode is **NOT VERIFIED**.
- **Data** breadth/depth and host-level production certification remain **INCOMPLETE** even though physical nesting is structurally complete. Do not switch domain workstream without explicit user approval.

## HISTORICAL CHECKPOINT — Data Engineering backfill recovery source migration (2026-11-05)

- Canonical branch: `pre_release`; baseline HEAD before this atomic migration: `48e169c52421318ed5bd294bc4f23ff4e5dd2d3d`. Never merge to `main` or create a new branch without user approval.
- Target: `pipeline-backfill-recovery`, categorized as **Data / Data Engineering / Batch Ingestion / Recovery**.
- Canonical file: `.agents/skills/data/data-engineering/batch-ingestion/recovery/pipeline-backfill-recovery/SKILL.md`; removed flat `.agents/skills/pipeline-backfill-recovery/SKILL.md`.
- Source `SKILL.md` is reused with its **unchanged Git blob SHA** `9b48fb6e58cbce15c21618d33cd64fe131e7db94`; original frontmatter, skill ID, instructions, bundled resource inventory and behavior are unchanged.
- The only YAML registry `path` replacement is in `domains/data/general-skills.yaml`. The `recovery` child in `domains/data/data-engineering/batch-ingestion/map.yaml` deliberately continues to reference that shared registry to avoid a routing behavior change.
- `tests/test_data_engineering_coverage.py` enforces one canonical nested manifest, absence of the flat source, registry selection and existing deterministic routing fixture behavior. No routing triggers, fixture count, skill IDs or examples added.
- Expected source inventory after the atomic move: **344 total**, **328 domain-nested (95.35%)**, **16 flat (4.65%)**. Verify against the published tree and run all tests.
- Pre-migration `pre_release` GitHub Actions push run **42000161037** at baseline HEAD passed validation and unit tests. **The migration commit's own CI run must be independently checked before reporting PASS.**
- Native auto-discovery of nested skills across Codex, Claude Code, OpenCode, Cursor and Copilot remains **NOT VERIFIED**. The registered YAML Router path is the canonical source mechanism. The full Data domain is still incomplete.
- Next: inspect actual migration SHA and full push CI job/step conclusions, check unique Git blob SHA and manifest counts, then continue only with the user-approved Data subdomain workstream.

## HISTORICAL CHECKPOINT — Infrastructure Advanced Storage migration (2026-11-05)

**Repository:** `ashkangoleh/agent-capability-map`, **branch:** `pre_release` only.
**Head before this checkpoint edit:** `c694c947d479527f1650bb89a01962e29d706f20`. Always fetch live HEAD on future continuation.
**User request:** choose one previously flat domain, classify skills #8 and #9, migrate one category, and report structural progress after each change. Do not add examples.

- #8 `object-storage-infrastructure-operations`: **Infrastructure / Storage Engineering / Advanced Storage**.
- #9 `pipeline-backfill-recovery`: **Data / Data Engineering / Batch Ingestion / Recovery**. It is **not moved in this increment** and remains a flat skill.
- Migrated the complete Advanced Storage registry's **two** skills (#8 and #17 `storage-san-nas-nvmeof`) to `.agents/skills/infrastructure/storage-engineering/advanced-storage/<skill-id>/SKILL.md`.
- Updated `domains/infrastructure/storage/new-specialists.yaml` and extended `tests/test_infrastructure_coverage.py` to enforce canonical paths and absence of old flat duplicates.
- Pre-commit tree validation verified **2/2 identical Git blob SHAs**, removal of flat originals and constant 344 physical SKILL manifests.
- **Structural progress:** 327/344 domain-nested (95.06%), 17 flat (4.94%). This is **file layout only**, not project completion, all-agent compatibility or production readiness.
- Initial CI runs failed due to stale generic Data registry paths. Those two references were corrected in `domains/data/general-skills.yaml`, and the PySpark test now reads the path selected by Router. The next CI run passed YAML graph validation but reported 22 legacy flat-path assertions in three older coverage test files. All three have been updated to read registry/router-selected canonical paths in commit `e3233c36ad423543fb21e43d66e6717f6a53e4c7`. Full CI success must still be checked at the latest live HEAD.
- Historical `docs/SKILL_LIBRARY_LAYOUT.md` describes the earlier two-category canary. Current source of truth is the registered `path` in the relevant YAML; independent native host discovery of deeply nested paths remains host-specific.
- Next candidate for a **separate user-approved category migration**: `pipeline-backfill-recovery` via `domains/data/general-skills.yaml` and the batch-ingestion recovery route. Maintain a one-file-per-ID invariant and update all referencing registries.

**Acceptance status:** 2/2 identical Git blob SHAs and registry paths verified; YAML graph validation passed after generic registry repairs. The full Python unit suite and host discovery require a successful post-fix CI run; do not claim green CI without checking the latest workflow.


## HISTORICAL CHECKPOINT — Data Science Foundations categorized (2026-11-05)

**User scope:** Keep organizing `.agents/skills` by domain/subdomain/category, avoid adding unnecessary examples, preserve IDs and the explicit YAML Router. Current top-level work stays on **all of Data**; active subdomain remains **Data Science**, not another domain.

**Repository:** `ashkangoleh/agent-capability-map` (private). **Working branch:** `pre_release`. Never merge `main` or create unrelated branches without explicit approval.  
**Head observed before this checkpoint commit:** `34bf0b80e1d31a874d993979f97d72d2dc530812` — fetch live HEAD again in a new conversation.

### This increment completed

- **Phase 2: `foundations`**: moved four instruction-only SKILL packages to `.agents/skills/data/data-science/foundations/<skill-id>/SKILL.md`: `ds-problem-framing`, `ds-scientific-python`, `ds-r-statistics`, `ds-jupyter-reproducibility`.
- Verified all **4/4** destination Git blob SHAs are identical to source; updated `domains/data/data-science/foundations/skills.yaml`; removed **4/4** flat originals after verifying copies.
- Updated `tests/test_data_science_skill_layout.py` to verify both migrated families, ten stable routing cases and unique source ownership for all 42 Data Science skills.
- Audited `tests/test_data_science_coverage.py` and `tests/test_data_science_inference_routing.py` for relevant hardcoded flat-path dependencies; no outstanding direct references found in those inspected test files.
- Reconciled layout documentation in `docs/SKILL_LIBRARY_LAYOUT.md`, `.agents/skills/README.md`, `docs/DATA_SCIENCE_REMAINING_SKILLS_AUDIT.md`, and the root `README.md`.
- **Cumulative state: 10 of 42 Data Science skills in 2 migrated categories**, 32 remain in old flat paths; **344 total master skill IDs** and **467 routing fixtures** are intentionally unchanged. No new examples, skill IDs or trigger phrases.
- Recreated the exact published Python lexical scoring formula in independent JS and checked **10/10** moved skill selection requests against the live YAML. This is **not** real Python Router execution or host compatibility evidence.

### Blocking evidence and next action

1. **Actual CI is still UNVERIFIED.** The GitHub connector yielded `statuses: []` and its workflow-runs API is restricted to PR-triggered runs. Its empty response is **not a passing push workflow**. Container network access does not permit cloning private GitHub. Do not claim the branch has passed validation.
2. Prioritize verification of a checked-out `pre_release` with `python -m capability_map validate`, `python scripts/evaluate_graph.py`, `python scripts/report_coverage.py --summary`, and `python -m unittest discover -s tests -v`. Record actual exit codes and SHA. Independently test native/explicit selection in target hosts; nested source directories may not be auto-discovered everywhere.
3. When validation evidence permits, **next category** for tidy source migration: `data/data-science/model-validation` (4 registered skills). Inspect its full companion bundles and references, migrate as a unit, update its registry and tests, compare Git blob SHAs, retire originals. Do not move all 32 remaining in a single unsafe change.
4. Continue the remaining Data Science method/deployment reviews. Do not assert Data Science or the entire nine-subdomain Data domain is complete. Confirm which Data subdomain to tackle next only after Data Science acceptance.

**Authoritative detailed files:** `docs/SKILL_LIBRARY_LAYOUT.md`, `docs/DATA_SCIENCE_REMAINING_SKILLS_AUDIT.md`, and the previous checkpoint history below.


## HISTORICAL CHECKPOINT — Domain-organized source skills phase 1 (2026-11-05)

**User instruction:** Stop adding unnecessary example files. Clean up `.agents/skills` by organizing skills inside meaningful domain/subdomain/category folders, **without breaking the master router**. Continue only with the active `data/data-science` subdomain, not Infrastructure or other top-level domains.

**Branch:** `pre_release` only; do not touch `main`. **Latest observed HEAD before this checkpoint update:** `4283a5ee0dea741e96ff170c3655ab64b4cfd1e2`; always fetch current HEAD from GitHub on a new chat.

### Changes actually made

- Migrated **six** current `statistics-advanced` skills into canonical domain-scoped source directories: `.agents/skills/data/data-science/statistics-advanced/<skill-id>/SKILL.md`.
- Kept all six skill IDs, contents, YAML triggers and descriptions unchanged. All six destination Git blobs were verified **identical to old source blob SHAs**. Original flat files removed to avoid duplicate manifest activation.
- Updated `domains/data/data-science/statistics-advanced/skills.yaml` to new registered paths. Updated `tests/test_data_science_inference_routing.py` to resolve actual registry paths rather than hardcode flat folders.
- Added `tests/test_data_science_skill_layout.py`: verifies canonical six paths, no flat duplicates, representative route selection, and structural inventory/unique ownership of all **42 Data Science skills** (source only; not yet executed on full repo).
- Documented the phased layout, native host risks and scope in `docs/SKILL_LIBRARY_LAYOUT.md`, `.agents/skills/README.md`, and `README.md`; created `docs/DATA_SCIENCE_REMAINING_SKILLS_AUDIT.md` with a 20-category inventory and acceptance plan.
- **No example files, new skills, ID changes or routing fixtures** were added in this increment. Master skill IDs should remain **344** and deterministic fixture cases **467** until independently recounted.

### Critical compatibility note

- Some clients/plugins discover only immediate-child native skill directories; nested source layout is **not inherently portable for native auto-discovery**. This repository's explicit **YAML Registry + Router** path selection is the intended source mechanism. **Do not claim all clients natively discover nested source skills.** If a host needs flat installed skills, assess an independent, explicitly selected host-specific export rather than retaining permanent duplicate SKILL manifests.
- Only 6/42 Data Science skills have been migrated so far. **36 still have original flat paths** and are intentionally untouched until testing validates migration safety; the rest of the 344-ID library is unchanged. This is an incremental canary, not full structural completion.

### Next steps, in priority order

1. Verify actual GitHub Actions **push** run and execute live `pre_release` full `python -m capability_map validate`, `python scripts/evaluate_graph.py`, `python scripts/report_coverage.py --summary`, and `python -m unittest discover -s tests -v`; investigate any path/host regressions. Do not infer PASS from static source checks.
2. Run actual host tests (Codex, Claude Code, OpenCode, Cursor, Copilot) to determine whether an explicit router-selected nested path loads correctly and to evaluate native discovery limitations.
3. Only after these gates, reorganize the **remaining 36 Data Science skill packages** by their 19 categories, one category at a time, including any bundled assets. Do not bulk-migrate all 344 without compatibility evidence. Continue reviewing statistical correctness for the still unaudited families.
4. Keep Data Science and all nine Data subdomains **INCOMPLETE** until tests, method validation and real agent behavior are verified. Get user approval before moving to the next Data subdomain.
5. Update this checkpoint with actual test evidence, new HEAD, paths moved and risks after the next substantive milestone.


## Earlier continuation — Data Science uncertainty/calibration (2026-11-05)

**Repository:** `ashkangoleh/agent-capability-map` (private); **working branch:** `pre_release`; `main` must remain unchanged without explicit approval.  
**Verified HEAD before checkpoint update:** `c9bc535441075852b6d58e2d61ee18182f3dfc58`. In a future chat, always fetch live HEAD; this SHA becomes historical as soon as this checkpoint is committed.  
**Current user-approved workstream:** Entire top-level `data` (nine subdomains) in sequence; **active subdomain `data/data-science`** (42 existing specialists), **NEXT family: forecasting**. Neither Data Science nor all Data is complete. Do not automatically switch to Infrastructure or any other top-level domain.

### Just completed: Conformal Prediction + Probability Calibration

- Rewrote existing `.agents/skills/ds-conformal-prediction-uncertainty/SKILL.md` (v1.1.0) and `.agents/skills/ds-model-calibration/SKILL.md` (v1.2.0), preserving original IDs and routes.
- Explicit boundary: **split conformal** gives nominal *marginal* predictive coverage under exchangeability, using exact finite-sample `k=ceil((n+1)*(1-alpha))` order-statistic; it does not prove time/subgroup/individual conditional coverage.
- Explicit boundary: probability calibration needs independent base training/calibration/final evaluation; Brier alone is not a pure calibration metric; sklearn `FrozenEstimator` exists from 1.6, `temperature` scaling from 1.8 (verify deployed version). MAPIE v1 API must be pinned.
- Added reproducible dependency-free arithmetic `examples/data_science/uncertainty_integrity.py`: non-overlapping observation IDs, finite-sample residual quantile with insufficient-`n` fail-close, descriptive regression coverage and bin-level binary probability reliability with sparse bins suppressed. **It does not train a model or prove exchangeability.**
- Added `tests/test_data_science_uncertainty_integrity.py`: **23/23 local unit tests executed successfully** against locally source-equivalent exact code. Added `tests/test_data_science_uncertainty_routing.py`, **15** `ds-uncertainty-*` fixtures covering English, Persian and hard-negative method boundaries; a separate JS lexical-router reconstruction matched 15/15 new requests (**not** actual Python router or CI).
- Current committed file inventory: **423** deterministic routing fixtures; **344** unique master skill IDs. No new skill ID in this increment.
- Official references, evidence and remaining acceptance gates documented in `docs/DATA_SCIENCE_UNCERTAINTY_CALIBRATION_PROTOCOL.md`. Updated README and domain audit/status documents.

### Critical verification constraints

1. **NOT VERIFIED:** full `python -m capability_map validate`, `scripts/evaluate_graph.py`, `scripts/report_coverage.py --summary`, all `unittest` cases on current GitHub checkout, GitHub Actions push CI outcome, runtime-pinned sklearn/MAPIE integration, real agent host invocation and independent stats review. The connector returns no conventional commit status checks, and its workflow-runs action is PR-limited. Never claim green CI based on these incomplete signals.
2. **NEXT within Data Science:** inspect forecasting skills/maps and test real rolling-origin/time/horizon split contracts, probabilistic forecasts (quantile monotonicity/calibration), hierarchical reconciliation, intermittent demand, drift and late labels. Reuse existing skills before creating new ones; add precise positive, negative and Persian/English routing coverage. Require versioned official references and documented failure/recovery.
3. After forecasting, continue statistical inference/surveys, Bayesian/causal/multilingual evaluation and remaining Data Science inventory. Respect user preference to progress one Data subdomain at a time; defer other top-level domains.
4. Data Engineering still has outstanding broker/streaming, catalog and production proof gaps; maintain backlog, **do not label it complete**. All nine Data subdomains need independent depth and host evaluation before Data root completion.

## Previous continuation — Data Science causal/experimentation (2026-11-04)

**Canonical branch:** `pre_release` (never merge `main` without explicit approval).  
**Verified HEAD immediately before this checkpoint update:** `9d56442425bed146ad26ea05c15492b19492d0d0`; fetch live HEAD again in every new conversation.  
**Active domain and next subfamily:** `data/data-science`; **conformal prediction + probability calibration**. **Do not switch back to Data Engineering automatically**: it has unresolved work, but current user-approved progression is across all nine Data subdomains one at a time. Never claim Data Science or Data top-level complete prematurely.

### Just completed in causal inference + experimentation

- Hardened three existing skills: `ds-causal-inference`, `ds-ab-experimentation`, `ds-sequential-experimentation`, including identification assumptions/refutation, assignment-level SRM diagnostics, sequential alpha spending and stopping validity; no new skill IDs.
- Added executable `examples/data_science/assignment_integrity.py` and `tests/test_data_science_assignment_integrity.py`. **18 unit tests were actually run locally** against source-equivalent code; this is not the entire repo test suite.
- Registered **12 `ds-causal-exp-*` routing cases**, including bilingual and near-miss cases, plus `tests/test_data_science_causal_experimentation.py`. File inventory: **408 total fixtures**, **344 unique master skill IDs**.
- A separate JS reconstruction of lexical routing against the current GitHub YAML matched all 12 new cases. **This is not actual Python Router/CI execution**. No full push CI status or end-to-end host validation verified.
- Source-referenced detailed review: `docs/DATA_SCIENCE_CAUSAL_EXPERIMENTATION_PROTOCOL.md`. Related previous slice: `docs/DATA_SCIENCE_VALIDATION_PROTOCOL.md`.
- Severe limits: chi-square SRM helper is for independent *two-arm* assignment-unit events, not observed exposure or post-treatment outcomes; it is not a causal estimator and does not prove randomization correctness. Multi-arm/blocked/adaptive designs need a distinct test.

### Immediate next actions

1. At **current live HEAD**, execute and record `python -m capability_map validate`, `python scripts/evaluate_graph.py`, `python scripts/report_coverage.py --summary`, `python -m unittest discover -s tests -v`; inspect actual GitHub Actions push workflow. Do not report PASS on static fixture source alone.
2. In Data Science only, audit and strengthen `ds-conformal-prediction-uncertainty` and `ds-model-calibration` with clear exchangeability/calibration/test isolation, risk/coverage guarantees, subgroup uncertainty, temporal drift and credible version-specific references.
3. Add targeted executable, negative and bilingual fixtures; separately evaluate real model task selection across hosts. Then proceed within Data Science to forecasting, statistical/survey methods and the rest of its 42-skill inventory.
4. Data Engineering still has catalog, broker/streaming and versioned production-recovery gaps; return to it only by an explicit progression decision. Work through the nine Data subdomains and seek approval before another **top-level** domain.

## HISTORICAL CHECKPOINT — Data Science inference/surveys increment (2026-11-05)

**Repo:** `ashkangoleh/agent-capability-map` (private)  
**Branch:** `pre_release`, never merge into `main` or create feature/fix branches unless the user explicitly changes scope.  
**HEAD before this checkpoint commit:** `cc6f1067620fbdfbe3074001e241cf96cda6ffb2` (historical immediately upon commit; always fetch live head again).  
**Approved top-level domain:** all nine subdomains of `data`; still **NOT COMPLETE**.  
**Current active subdomain:** `data/data-science` (42 specialist skill IDs declared); still **NOT COMPLETE / not production-certified**.  
**NEXT:** review remaining Data Science specialist boundaries, run full Python graph/routing/unit suite and GitHub Actions, then conduct version-pinned model/survey integration and actual host/agent semantic benchmarks. Do not automatically progress into Analytics Engineering, Infrastructure or other top-level domains.

### Completed in the latest increment

1. Hardened **five existing** SKILL packages, no new IDs: `ds-multiple-testing-control`, `ds-survey-sampling-design`, `ds-missing-data`, `ds-robust-nonparametric-inference`, `ds-bayesian-pymc-stan`. Improved precise FWER/FDR method boundaries, strata/PSU and inclusion/response weights, Rubin pooling, cluster/paired resampling, MCMC sampler diagnostics and abstention.
2. Created `examples/data_science/inference_integrity.py` and `tests/test_data_science_inference_integrity.py`. **23/23 Python tests actually ran locally and passed**; exact Git blob SHAs independently matched: source `b37958b1fd30c6b9898719ef8dfb2633ed492c0d`, tests `ffe9b08d94ffb0dd19c5e14112641c081453ac93`.
3. Seeded cross-library arithmetic check with installed **statsmodels 0.14.6**, NumPy 2.3.5, SciPy 1.17.0: Bonferroni, Holm, BH and BY adjusted p-values and rejection flags matched **600/600** comparisons, across p-value vector sizes 1, 2, 3, 5, 20 and 100. These validate math only, **not original p-value validity or dependence/stopping assumptions**.
4. Added `tests/test_data_science_inference_routing.py` and **22** `ds-inference-*` positive, bilingual, hard-negative/cross-domain routing fixtures. The *separate JavaScript lexical-router reconstruction* matched 22/22 new requests. **This does NOT establish the actual Python Router test suite PASS**.
5. Inventory now contains **467 declared deterministic fixtures**, **344 unique master skill IDs**. Detailed technical document: `docs/DATA_SCIENCE_INFERENCE_SURVEY_VALIDATION_PROTOCOL.md`. Updated `README.md`, Data Science audit and Data root status.
6. **Failure/claim boundaries:** Survey helper returns descriptive weighted mean/Kish weight-only effective N and explicitly **no** design-based standard error; lonely PSU fails closed. Rubin scalar pooling reports estimate/total variance but no degrees-of-freedom CI; it does not impute data. BH/BY arithmetic does not guarantee FDR without study-design assumptions. Bayesian references are reviewed but **no MCMC sampler run** was performed.

### Immediate actions next time

1. Fetch `pre_release` live HEAD and this **LATEST ACTIVE CHECKPOINT** first.
2. Execute and retain logs/exit statuses: `python -m capability_map validate`, `python scripts/evaluate_graph.py`, `python scripts/report_coverage.py --summary`, `python -m unittest discover -s tests -v`. Inspect actual GitHub Actions push workflow jobs, not only PR-bound workflow-run query. If unable to run, state **NOT VERIFIED**.
3. Complete outstanding Data Science specialist audit across statistical power, simulation, survival, geospatial, recommendation, robust/Bayesian, fairness and multilingual scientific NLP. Evaluate intent boundaries using positive/negative/Persian-English cases and controlled host agent runs. Avoid adding skill wrappers just to increase counts.
4. Run reproducible release-pinned integration samples: survey variance with R `survey`, MI pooling with `mice`/statsmodels, actual Bayesian posterior diagnostics, and previous Data Science family integration tests. Confirm assumptions and failures, not only static routing.
5. Keep Data Science and all of Data **incomplete** until verified acceptance criteria, and get user approval before beginning another Data subdomain. Update this checkpoint with the latest commit and verified evidence.

## HISTORICAL CHECKPOINT — Previous Data Science Forecasting increment (2026-11-05)

**Canonical repo:** `ashkangoleh/agent-capability-map` (private)  
**Working branch:** `pre_release` (no `main` merge, no new feature/fix branch without explicit approval)  
**HEAD verified immediately before this checkpoint commit:** `b5e24555163f95a25c2d96d41e1d952a6b74eccb` — always fetch live `pre_release` HEAD again at the start of a future chat.  
**Active top-level domain:** `data` (nine subdomains; overall INCOMPLETE)  
**Active subdomain:** `data/data-science` (42 structural specialist skills, 26 declared capability areas; not production-certified)  
**NEXT focused specialty family:** statistical inference, survey design, robust/Bayesian uncertainty and multiple-testing validity. **Do not change to another Data subdomain until user authorizes a move; do not switch to Infrastructure.**

### Just implemented, verified and committed

1. Hardened **four existing** forecasting SKILL packages in place: `time-series-forecast-backtesting`, `ds-probabilistic-forecasting`, `ds-hierarchical-forecasting` and `ds-intermittent-demand-forecasting`; no new skill IDs. Defined operation contracts for origin/label/covariate availability, rolling-origin vs calendar gap, pinball loss and quantile crossing, hierarchy version/coherence and stockout-censored demand.
2. Created `examples/data_science/forecast_integrity.py` and `tests/test_data_science_forecast_integrity.py`: **30/30 tests actually ran locally and passed** using standard-library Python. Verified both files have the **exact same Git blob SHAs** in `pre_release` as the locally executed files (source `c7e5d72ea84364f03ad35814fd9e5aee8dd0daa3`, tests `e8ff06777b921e03b59b7a3852e7d95174c978ad`).
3. Added `tests/test_data_science_forecast_routing.py` and **22** `ds-forecast-*` positive, near-miss and mixed-language fixtures. File inventory now **445** deterministic routing fixtures and **344** unique master skill IDs.
4. Verified **22/22** of the new routes with a separate **JavaScript reconstruction** of lexical matching against the GitHub YAML graph, and found no duplicate triggers in edited maps. **This is NOT execution of the actual Python Router, nor evidence that all 445 fixtures pass.**
5. Recorded decision matrix, references, reproducible examples, safeguards and acceptance commands in `docs/DATA_SCIENCE_FORECASTING_VALIDATION_PROTOCOL.md`; updated README, Data Science audit and Data top-level status docs.

### Exact limits and remaining validation

- Full `python -m capability_map validate`, `python scripts/evaluate_graph.py`, `python scripts/report_coverage.py --summary`, `python -m unittest discover -s tests -v` **on live branch HEAD** and GitHub Actions push CI result: **NOT VERIFIED**. Previous GitHub connector status checks returned no status entries; do not describe that as PASS.
- The forecasting helper does **not** fit actual models or establish calendar-aware embargo, as-of source data provenance, hierarchical probabilistic reconciliation, version-specific engine compatibility or uncensored demand.
- Before declaring Data Science complete, obtain reproducible trained-model/horizon backtests, independent statistical review, actual real-agent host routing benchmarks and full coverage of all declared capability areas.
- The larger top-level Data domain still has seven unaudited subdomains, plus unresolved Data Engineering reliability/broker/catalog/warehouse evidence. Never state that Data is complete.

### Immediate action for a new conversation

1. Fetch `pre_release` HEAD and read this **LATEST ACTIVE CHECKPOINT**, `docs/DATA_DOMAIN_COMPLETENESS_STATUS.md`, `docs/DATA_SCIENCE_COVERAGE_AUDIT.md` and the last forecasting validation protocol.
2. Run or independently retrieve the full Python tests and GitHub push CI status. Fix any failures and record actual SHA/log evidence before claiming branch health.
3. Advance **within Data Science** to existing statistical inference/survey/robust/Bayesian skills: audit estimator assumptions, multiplicity, survey weights/design effects, missing-data mechanisms and inference under dependence. Improve evidence and negative/ambiguous/bilingual routes with runnable reference checks; do not add duplicates for quantity.
4. After this Data Science subfamily, finish the remaining Data Science review and seek explicit approval before switching to the next of the nine Data subdomains. Do not select another top-level domain unilaterally.
5. Update this file after each substantive increment, with new HEAD, executed test evidence, actual files, open risks and next workstream.

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

## Earlier Data Science model-validation slice — 2026-11-04

**Current active subdomain is still `data/data-science`**; only the model-validation family was improved in this increment. Neither Data Science nor the whole Data domain is complete. Data Engineering remains broad but unverified and separately backlogged.

Changes on `pre_release`:
- Rewrote existing `.agents/skills/sklearn-leakage-free-validation/SKILL.md` (version 1.1.0) for split selection, group/time leakage, future label availability, nested tuning, preprocessing isolation, failure/recovery and version-aware source references.
- Changed `catalog/root.yaml`, `domains/data/map.yaml`, `domains/data/data-science/map.yaml`, and `domains/data/data-science/model-validation/skills.yaml` to preserve Data Science discovery but **abstain** on lone `sklearn` or `scikit-learn`, requiring task-discriminative validation intent.
- Added `examples/data_science/split_integrity.py` (no mandatory third-party dependencies; optional NumPy arrays) and `tests/test_data_science_split_integrity.py`. Local tests run on the source-equivalent helper: **17 passed**. Catches index/group/time/label-availability boundary violations, but does NOT certify whole-pipeline leakage freedom.
- Added 11 `ds-validation-*` routing fixtures and `tests/test_data_science_validation_routing.py`; total fixture YAML **396**; master skill ID YAML remains **344 unique**. The 11 cases were checked successfully with a **separate JS lexical routing reconstruction**, NOT Python `Router.resolve` or CI.
- Updated `README.md`, `docs/DATA_SCIENCE_COVERAGE_AUDIT.md`, and `docs/DATA_DOMAIN_COMPLETENESS_STATUS.md`. Detailed decision matrix and evidence limits: `docs/DATA_SCIENCE_VALIDATION_PROTOCOL.md`.

**Critical nuance:** future forecasting of known entities may reuse entities across train/test; group-disjoint evaluation is specifically needed for unseen-entity generalization. A `TimeSeriesSplit` sample gap is not equivalent to a wall-clock embargo, and overlapping labels can invalidate simple chronological validation.

**Next steps within Data Science:**
1. Obtain actual `pre_release` push GitHub Actions validation and run `python -m capability_map validate`, `python scripts/evaluate_graph.py`, `python scripts/report_coverage.py --summary`, and `python -m unittest discover -s tests -v` at the current head. No full-suite green result has been verified.
2. Validate a version-pinned sklearn synthetic example using actual `Pipeline`, group/time splitters, late labels, nested tuning and real fitted data; measure and label all results (not invented benchmarks).
3. Advance to the **causal inference + experimentation** specialist family: causal identification assumptions, randomized unit/cluster integrity, inference and sequential stopping with hard negative and bilingual routing tests.
4. Then conformal/calibration, forecasting, inference/survey science and the remaining 42-skill specialist review. Keep all nine Data subdomains open until their own gates pass.

**Checkpoint source HEAD before this documentation update:** `8f11ffdd8ec666996f821aab785e43f6f4c7c037`. Fetch live branch HEAD at the beginning of the next chat.

## Data top-level scope decision — 2026-11-04

The user explicitly clarified that the completion target is **all of `data`**, not only `data/data-engineering`, and authorized the next subdomain. The top-level Data domain is **NOT COMPLETE**. It has **nine first-class subdomains**. Do **not** switch to Infrastructure or any unrelated top-level domain now.

**Next active subdomain:** `data/data-science` — review its 42 registered skills and 26 declared areas with independent, reproducible statistical method evaluation, leakage / temporal validation checks and negative / ambiguous / multilingual routing tests. This is a scope transition, **not** a declaration that Data Engineering is done. Its outstanding work remains queued.

The next sequence after Data Science is Analytics Engineering, Database Engineering, Data Analysis, Business Intelligence, Data Governance, Data Quality and Data Architecture, each subject to audit, operational validation and user-approved progression. The live subdomain inventory and exact acceptance gates are in `docs/DATA_DOMAIN_COMPLETENESS_STATUS.md`.

This turn also removed one duplicated `false discovery rate correction` trigger in `domains/data/map.yaml` and added a structural uniqueness regression test in `tests/test_data_science_coverage.py`. **The Python test suite/CI have not been verified against the resulting HEAD.** Run validations before claiming pass.

## Historical Data Engineering backlog (not current active domain)

**Historical working domain: `data/data-engineering`. It remains incomplete and is not the currently active subdomain.**
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

## Current next-action pointer

The **first section of this file** (`Current authoritative continuation — Data Science`) supersedes earlier next-action lists. Always read live HEAD and the latest domain audit before making changes. Current approved workstream: Data Science conformal/calibration, not a switch to another top-level domain.

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
