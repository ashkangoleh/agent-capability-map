# Agent Capability Map — Global Master Skill Router

Global-first, YAML-driven, hierarchical discovery for reusable skills across coding agents. A single master map serves all projects. A user can **add personal skills** globally or per project without changing the master repository.

The last recorded full graph audit counted 41 top-level domains and 322 active SKILL.md packages, with 348 deterministic fixtures and 54 unit tests passing **at that historical snapshot**. Subsequent Data Engineering expansion has increased the master skill-ID index to **344 entries** and the routing fixture file to **467 cases**; these new totals are file counts, **not a newly run passing test result**. Re-run the live report, YAML graph validation and all tests on the current branch before asserting active totals or CI success. Infrastructure now has 16 first-class selectable scopes and 95 unique active specialist skills. The Data domain is still incomplete: Data Engineering needs further operational depth, Data Science has structural coverage but incomplete independent validation, and seven other Data subdomains need focused audits. Get live counts with `python scripts/report_coverage.py --summary`. **Mapped is not implemented.** Only validated, registered SKILL.md files are active. The taxonomy is intentionally extensible; no finite list contains every possible specialty.

## Operating contract

1. An agent receives an ordinary task, such as "Create a new PySpark project."
2. Small global instructions ask it to call the read-only resolver with the task intent.
3. Resolver checks the top-level YAML map, then only the selected child maps, then its local skill registry.
4. It returns a verified path to the best matching SKILL.md, or an explicit needs_clarification/unavailable/unmatched status.
5. The host agent reads only the selected SKILL.md and necessary references.
6. Personal/project skills are considered **only when explicitly registered**. IDs cannot silently overwrite master IDs.

**No slash command is required** to express the task. However, a host must actually follow its global instructions and be able to invoke the CLI. Invocation reliability and token savings are not yet measured; this is not a universal native plugin.

## Install globally (per user, local machine)

Prerequisites: Python 3.10+, Git, and permission to create global instruction files.

~~~sh
git clone -b pre_release https://github.com/ashkangoleh/agent-capability-map.git ~/agent-capability-map
cd ~/agent-capability-map
python3 -m venv .venv
.venv/bin/python -m pip install -e .
.venv/bin/python -m capability_map validate
~~~

Review what will change before touching existing instructions:

~~~sh
.venv/bin/python -m capability_map install --hosts codex claude opencode copilot cursor
~~~

Apply only after reviewing the target paths:

~~~sh
.venv/bin/python -m capability_map install --hosts codex claude opencode copilot cursor --apply
~~~

This writes a managed, concise block into user-level instruction files while preserving all unrelated content. Cursor receives one global router SKILL.md. It does **not** copy every specialist skill into native host folders.

For Claude Code, the installer also updates the user-level `settings.json` (or `$CLAUDE_CONFIG_DIR/settings.json` when configured): it adds only the repository's `.agents/skills` directory to `permissions.additionalDirectories` so reads are available without the outside-workspace prompt, and adds a path-scoped `Edit(//.../.agents/skills/**)` deny rule for Claude's built-in file-edit tools. This is included in the dry-run preview and is applied only with `--apply`. Existing JSON settings are preserved; malformed JSON and symlink destinations fail closed. The edit deny is a host-tool guard, not OS-level immutability: arbitrary shell subprocesses are outside that rule's enforcement boundary.

| Host | User-level bootstrap |
|---|---|
| Codex | ~/.codex/AGENTS.md |
| Claude Code | ~/.claude/CLAUDE.md |
| OpenCode | ~/.config/opencode/AGENTS.md |
| GitHub Copilot CLI / supported VS Code sessions | ~/.copilot/copilot-instructions.md |
| Cursor | ~/.cursor/skills/master-capability-router/SKILL.md |

These are host-specific entry points, **not guarantees** that all remote/cloud agent runs discover local user instructions. Native skill discovery, invocation and permissions vary. For VS Code/Cursor, verify the active harness, environment and applicable user rules. Global installation means the current user/machine; repeat in each remote worker/cloud container as appropriate.

The installed Python interpreter must remain available and the cloned repository path must remain stable. The installer intentionally supports dry-run by default and refuses unsafe symlink targets or unmanaged Cursor skill collisions.

## Select the domains available to the router

Domain selection is user-controlled and independent of host installation. The user may enable up to **five non-overlapping domain scopes** in one operation. A scope can be a top-level domain (for example `infrastructure`) or a nested domain (for example `data/data-engineering` or `data/data-science`). Selecting `data` enables all of its descendants; selecting `data` together with `data/data-engineering` is rejected as redundant.

Preview the available scopes and current profile:

~~~sh
capability-map domains list
capability-map domains list --prefix data
capability-map domains status
~~~

Replace the current selection (dry-run by default):

~~~sh
capability-map domains apply --domains data/data-engineering data/data-science infrastructure
~~~

Persist the selection only after reviewing the preview:

~~~sh
capability-map domains apply --domains data/data-engineering data/data-science infrastructure --apply
~~~

Use `domains add` and `domains remove` for incremental changes; use `domains clear --apply` to remove the allowlist and restore unrestricted routing. The profile is stored at `~/.config/agent-capability-map/domains.yaml`, is local to the user, and is shared by hosts that invoke this CLI. Apply is an atomic profile update; it does not copy, install, or execute domain software or skill files.

When a profile exists, the resolver traverses only selected branches. A request outside the selection returns `domain_not_enabled`; it must not bypass the allowlist by scanning the repository. With no profile, existing unrestricted routing behavior is preserved. The five-scope limit controls enabled domain roots, **not** the number of skills inside them: progressive disclosure still returns one selected skill path at a time.

See [Domain selection](docs/DOMAIN_SELECTION.md) for validation, overlap rules and lifecycle details.

## Use and inspect the YAML graph

~~~sh
.venv/bin/python -m capability_map resolve --request "Create a new PySpark project" --project .
.venv/bin/python -m capability_map resolve --request "Write PySpark DataFrame joins" --project .
.venv/bin/python -m capability_map resolve --request "Create an Airflow DAG with retries" --project .
.venv/bin/python -m capability_map validate
.venv/bin/python -m capability_map related --route data/data-engineering/distributed-processing/spark/pyspark
~~~

Inspect the JSON field skill_path only when status is matched. The lexical match_strength is a routing heuristic, **not a calibrated probability of correctness**. Ambiguous tasks return clarification options; unsupported mapped domains do not activate fictional skills. Multiple equally relevant domains may require explicit composition.

## Register your personal skills — this step is mandatory

**Unregistered personal files are NOT discovered by the master router.** You must register them in a YAML manifest and, for project-specific skills, explicitly point to the manifest in the project's AGENTS.md.

### Option A: global personal skills

Create the file below (in your own home directory):

~~~text
~/.config/agent-capability-map/personal.yaml
~~~

Example:

~~~yaml
schema_version: 1
skills:
  - id: my-company-pyspark
    path: skills/my-company-pyspark/SKILL.md
    route: [data, data-engineering, distributed-processing, spark, pyspark]
    triggers:
      - enterprise pyspark project
      - company spark templates
    excludes:
      - regular open-source pyspark
    status: active
~~~

Create the referenced skill under:

~~~text
~/.config/agent-capability-map/skills/my-company-pyspark/SKILL.md
~~~

The SKILL.md must follow the open Agent Skills standard: valid YAML frontmatter, name matching the directory, and a discriminative description. The personal ID must not collide with a master skill ID.

### Option B: per-project skills (registered in AGENTS.md)

In the PROJECT ROOT AGENTS.md, add exactly:

~~~text
<!-- capability-map: overlay=.capability-map.yaml -->
~~~

Create .capability-map.yaml in the same project root:

~~~yaml
schema_version: 1
skills:
  - id: team-pyspark-quality
    path: .agents/skills/team-pyspark-quality/SKILL.md
    route: [data, data-engineering, distributed-processing, spark, pyspark]
    triggers:
      - enterprise pyspark quality checks
      - team data quality conventions
    excludes: []
    status: active
~~~

Then create and test (the project argument is required for project overlay validation):

~~~sh
capability-map validate --project /path/to/my-project
~~~


~~~text
my-project/.agents/skills/team-pyspark-quality/SKILL.md
~~~

This skill exists alongside master skills. Both sources may match; the more specific lexical trigger wins. On equal matches the router asks for clarification rather than silently overwriting one source. Skills cannot escape their registered project/user root through path traversal or symlinks. **Do not place secrets or blindly trusted instructions into skill files.**

You can register more than one project YAML manifest by adding another explicit marker. The master router never scans arbitrary project folders looking for instructions.

### What to put in the project AGENTS.md

Put repository-specific constraints, conventions and the overlay registration marker in AGENTS.md. Do not copy the entire master router into every repository. Repo instructions are additive to global host instructions and do not grant privileged access to arbitrary skills.

## Architecture

~~~text
Global host instructions / optional Cursor router skill
           |
   capability-map resolve
           |
   catalog/root.yaml
           |
   domains/<domain>/map.yaml
           |
   <subdomain>/map.yaml ...
           |
   <technology>/<api>/skills.yaml
           |
   selected registry.path -> SKILL.md (flat or domain-nested source)
           |
   selective references and tests
           +
   registered personal.yaml or project AGENTS.md overlay
~~~

The hierarchical maps form the primary discovery tree. Typed cross-domain dependency edges are available on demand for explicitly related capabilities; a graph database is not needed for this version.

## Language support

The initial resolver uses bounded, deterministic phrase matching, including selected Persian and English aliases. It does not implement semantic understanding or infer arbitrary synonyms. In mixed-language tasks, the host can provide a concise, accurate canonical intent. Missing or ambiguous matches must lead to clarification, not invented skill selection.


## Skill source directory organization

The source skill library is being organized **incrementally** by domain and category. Two verified content-preserving moves relocated six `data/data-science/statistics-advanced` and four `data/data-science/foundations` skill packages into `.agents/skills/data/data-science/<category>/<skill-id>/SKILL.md`. Their stable IDs and YAML routing remain unchanged; the original flat SKILL.md duplicates were retired.

**Registry paths are authoritative.** The remaining 32 Data Science skills and the rest of the master library currently retain their registered flat paths. Direct native auto-discovery of deeply nested source skills is **not universally guaranteed** across Codex, Claude Code, Cursor, Copilot or OpenCode; the project's explicit router remains the supported source selector. Native-host discovery/export must be verified separately before claiming compatibility.

Read `docs/SKILL_LIBRARY_LAYOUT.md` for layout rules, proof limitations, and the staged migration plan. Do not auto-load all skills or create permanent flat duplicates to make a folder appear organized.

## Compatibility and validation

~~~sh
.venv/bin/python scripts/report_coverage.py --summary
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python -m capability_map validate
.venv/bin/python scripts/evaluate_graph.py
~~~

CI checks syntax, references, linked SKILL.md metadata, path security and test fixtures. Passing these checks does **not** prove language-model routing accuracy, lower token usage or zero hallucinations. Evaluation must compare actual model runs, source evidence quality, false activations, task success, cost and abstention.

## References and design sources

- https://agentskills.io/specification
- https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra
- https://docs.opencode.ai/docs/rules/
- https://cursor.com/help/customization/skills
- https://code.visualstudio.com/docs/agent-customization/custom-instructions
- https://github.com/DietrichGebert/ponytail/blob/main/docs/agent-portability.md
- https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html

Original JSON registries under catalog/ and domains/*/skills.json remain for historical comparison only. **The executable router now reads only catalog/root.yaml and its linked YAML files.**

## Deep Data Engineering Skills

The historical `feat/data-engineering-deep-skills` phase added 29 specialist skills for Flink, Beam, Scala Spark, Kafka Connect/consumers, Debezium CDC, Airflow backfill, Dagster, Prefect, OpenLineage, Iceberg, Delta Lake, Hudi, Trino, DuckDB, StarRocks, dbt snapshots, dimensional modeling, Parquet, Ray Data, Argo Workflows, Pulsar, RabbitMQ, Kinesis and data-platform architecture.

Technology-specific maps are loaded progressively. A StarRocks Stream Load request now routes to a StarRocks load skill; an Iceberg compaction request routes to Iceberg maintenance. Generic requests retain a bounded fallback where appropriate.

For routing and limitations see [Data Engineering Deep Skills](docs/DATA_ENGINEERING_SKILLS.md). Full behavioral correctness and token savings have not yet been measured across agents.

## Domain expansion

The authoritative live report is `python scripts/report_coverage.py` and the compact summary is `python scripts/report_coverage.py --summary`. A top-level domain with one active skill is **not** complete coverage of that discipline. See [Cross-domain expansion](docs/CROSS_DOMAIN_EXPANSION.md) and [Research sources](docs/RESEARCH_SOURCES.md). The current branch intentionally keeps legacy unsupported subdomains in the mapped-only state.

## Unified reference expansion

The historical `feat/master-reference-platform-data-ai` snapshot introduced 63 specialists across Infrastructure, Data Science, Data Analysis/BI, MLOps/LLM AI and Data Engineering. Its work is now consolidated into `pre_release`; the current fixture suite and coverage report are the authoritative validation sources.

### Canonical reference branch

**`pre_release` is the canonical integration branch.** It combines the unified YAML capability map with the latest comprehensive Data Engineering, Data Science and Infrastructure updates. It is intentionally not merged into `main` while the Data Engineering completion and host-compatibility work continue. Read [UNIFIED_COMPLETENESS_AUDIT.md](docs/UNIFIED_COMPLETENESS_AUDIT.md) for current maturity and known limits.

> The CLI validates and selects skill paths. The referenced software tools (e.g. Spark, Airflow, PyTorch, Kubernetes, MLflow) are **not installed by this repository**. Skill text describes procedures, not executable infrastructure or verified cloud access. Host-specific global instruction installation remains an independent, permission-scoped step.

## Comprehensive Data Engineering expansion

This branch adds 49 specialist packages for lifecycle/modeling, ingestion/CDC, streaming, orchestration, SQL transformation, formats, storage, warehouses/OLAP, quality, governance, DataOps, reliability, performance, cloud data platforms, serving, lakehouse and multi-engine architecture. See `docs/DATA_ENGINEERING_TOOL_MATRIX.md`. Tool inclusion is not proof of installation or availability.

## First-class Data Science domain

Data Science is a first-class subdomain under Data & Analytics, alongside Data Engineering, Analytics Engineering, Data Analysis, Database Engineering, BI and Governance. It now contains 42 active specialist skills across statistical inference, robust/nonparametric methods, Bayesian modeling, experiments, causal ML, panel econometrics, classical ML, calibration, fairness assessment, conformal uncertainty, forecasting, survival, recommendation, geospatial science, optimization, multilingual NLP and scientific computing. See docs/DATA_SCIENCE_TOOL_MATRIX.md. AI/ML remains a separate top-level domain for deep learning, LLM engineering, MLOps and model serving.

## Expanded Infrastructure Engineering

Infrastructure now has 16 first-class selectable scopes and 95 unique active specialist skills across Compute & OS, Networking, Cloud, IaC, Virtualization, Containers/Kubernetes, DevOps Delivery, Platform Engineering, SRE, Observability, Infrastructure Security, Storage, Database Infrastructure, Edge, Hardware/Data Center and Architecture/Governance. This expansion adds 35 specialist packages and consolidates duplicate registrations without deleting existing specialist IDs. All 35 new specialists had positive routing fixtures at the historical Infrastructure audit; that audit passed 348 deterministic routing fixtures and 54 unit tests. The updated branch has not yet been independently revalidated. This is structural and lexical validation, not production certification. See [Infrastructure Coverage Audit](docs/INFRASTRUCTURE_COVERAGE_AUDIT.md) and [Infrastructure Tool Matrix](docs/INFRASTRUCTURE_TOOL_MATRIX.md).

## Unified master branch

The current consolidated development branch is `pre_release`. See `docs/UNIFIED_COMPLETENESS_AUDIT.md` for domain maturity, known gaps, validation status and merge gates. This branch is not production-certified and has not been merged to `main`.
