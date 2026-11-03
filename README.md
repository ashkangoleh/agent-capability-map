# Agent Capability Map — Global Master Skill Router

Global-first, YAML-driven, hierarchical discovery for reusable skills across coding agents. A single master map serves all projects. A user can **add personal skills** globally or per project without changing the master repository.

The master map currently covers 41 broad domains and many mapped subdomains. The cross-domain expansion introduces 29 specialist skills (21 in previously mapped domains and 8 in newly introduced domains). Every top-level domain has at least one active specialist, but most subdomains remain mapped-only and require further implementation and evaluation. The first specialist expansion adds 12 focused skills; see [Coverage](docs/SKILL_COVERAGE.md) for active versus mapped nodes and exact routing examples. **Mapped is not implemented.** Only validated, registered SKILL.md files are active. The taxonomy is intentionally extensible; no finite list contains every possible specialty.

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
git clone -b feat/cross-domain-skill-expansion https://github.com/ashkangoleh/agent-capability-map.git ~/agent-capability-map
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
   selected .agents/skills/<name>/SKILL.md
           |
   selective references and tests
           +
   registered personal.yaml or project AGENTS.md overlay
~~~

The hierarchical maps form the primary discovery tree. Typed cross-domain dependency edges are available on demand for explicitly related capabilities; a graph database is not needed for this version.

## Language support

The initial resolver uses bounded, deterministic phrase matching, including selected Persian and English aliases. It does not implement semantic understanding or infer arbitrary synonyms. In mixed-language tasks, the host can provide a concise, accurate canonical intent. Missing or ambiguous matches must lead to clarification, not invented skill selection.


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

The `feat/data-engineering-deep-skills` branch adds 24 specialist skills for Flink, Beam, Scala Spark, Kafka Connect/consumers, Debezium CDC, Airflow backfill, Dagster, Prefect, OpenLineage, Iceberg, Delta Lake, Hudi, Trino, DuckDB, StarRocks, dbt snapshots, dimensional modeling, Parquet and data-platform architecture.

Technology-specific maps are loaded progressively. A StarRocks Stream Load request now routes to a StarRocks load skill; an Iceberg compaction request routes to Iceberg maintenance. Generic requests retain a bounded fallback where appropriate.

For routing and limitations see [Data Engineering Deep Skills](docs/DATA_ENGINEERING_SKILLS.md). Full behavioral correctness and token savings have not yet been measured across agents.

## Domain expansion

The authoritative live report is `python scripts/report_coverage.py` and the compact summary is `python scripts/report_coverage.py --summary`. A top-level domain with one active skill is **not** complete coverage of that discipline. See [Cross-domain expansion](docs/CROSS_DOMAIN_EXPANSION.md) and [Research sources](docs/RESEARCH_SOURCES.md). The current branch intentionally keeps legacy unsupported subdomains in the mapped-only state.
