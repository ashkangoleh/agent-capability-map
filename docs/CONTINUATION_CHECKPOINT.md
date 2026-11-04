# Continuation Checkpoint — Agent Capability Map

**Updated:** 2026-11-05
**Canonical repository:** `ashkangoleh/agent-capability-map` (private)
**Canonical working branch:** `pre_release`
**Verified branch HEAD immediately before this update:** `67e553cf6306313cee486e2ef205c96cdae8e831` (always fetch HEAD again in a new chat)
**Integration policy:** Work only in `pre_release` unless the user explicitly changes this. Do not merge into `main` without explicit approval. Do not create `feat/*` or `fix/*` branches for this work.

## LATEST ACTIVE CHECKPOINT — Data Science Foundations categorized (2026-11-05)

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
