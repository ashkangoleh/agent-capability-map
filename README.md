# Agent Capability Map

A domain-agnostic, evidence-aware capability system for AI agents.

The project maps user intent to a small set of verified capabilities, loads only the selected skill instructions, and retrieves supporting references only when needed. It covers technology, data, AI/ML, agent systems, product, marketing, SEO, design, business operations, research, governance, and people/learning.

## Core objectives

1. Lower context cost through progressive disclosure.
2. Reduce unsupported claims with evidence requirements, source hierarchy, explicit uncertainty, and abstention.
3. Improve task execution with small, composable skills and clear activation boundaries.
4. Stay portable through the open Agent Skills folder format.
5. Make quality measurable through CI validation and routing/evidence evaluation.

## Repository map

- AGENTS.md — root operating contract and master router.
- catalog/domains.json — runtime domain map; catalog/coverage-taxonomy.yaml — planned comprehensive, nested domain and tool inventory (not a list of implemented skills).
- domains/*/ROUTER.md — domain-specific routing instructions.
- domains/*/skills.json — metadata for skills in that domain only.
- .agents/skills/*/SKILL.md — independent, discoverable capability instructions; optional parent_skill/related_skills edges are domain-local registry metadata.
- docs/ — architecture, skill graph, engineering guardrails, client compatibility, evaluation, and authoring.
- tests/fixtures/routing-cases.json — labeled positive, negative, near-miss, and abstention cases.
- scripts/validate_registry.py — dependency-free structural validator.
- tests/ — validation tests.

## Agent quick start

1. Read AGENTS.md.
2. Read catalog/domains.json and select the smallest relevant domain set.
3. Read only the selected domain router and its local skills.json.
4. Follow specialization edges to the most specific matching leaf; load only that SKILL.md. Load a second skill only for a real cross-capability dependency.
5. Read referenced resources only at the point of need.
6. If no skill matches, do not invent one; use a suitable general research workflow or state the capability gap.

## Validation

    python -m pip install -r requirements-dev.txt
    python scripts/validate_taxonomy.py
    python scripts/validate_registry.py
    python -m unittest discover -s tests -v
    python scripts/inspect_skill_graph.py pyspark-skew-diagnostics

Registry validation uses only the Python standard library; YAML taxonomy validation requires PyYAML at authoring/CI time, not at agent runtime.

## Example: PySpark specialization

In the data registry, data-engineering-implementation -> pyspark-pipelines -> pyspark-joins -> pyspark-skew-diagnostics is a **selection path**, not a recursive load path. An end-to-end PySpark job selects pyspark-pipelines; a join cardinality bug selects pyspark-joins; measured skew selects pyspark-skew-diagnostics. Only the chosen leaf is loaded. See docs/SKILL_GRAPH.md and docs/CLIENT_COMPATIBILITY.md.

## Scope and honesty

The goal is a large library of **pre-authored, actionable skills** spanning data engineering (including AWS/GCP/Azure data tools), data science/ML, software, cloud/platform, DevOps/SRE/DevSecOps, networking, datacenter, product, business, marketing and SEO. The initial coverage charter is at docs/COVERAGE_CHARTER.md. A taxonomy entry is **mapped**, not an active SKILL.md. Only entries in active skill registries represent implemented skills. The master router must remain compact as coverage grows.

## Important limitation

This repository defines a portable map and operating contract; AGENTS.md and the registry do not magically implement a runtime loader. A host agent must support Agent Skills or provide file-read/tool access. Native semantic routing, runtime token telemetry, and automatic loading are integration concerns, not claimed as implemented here.

## Design principle

Discover narrowly. Load deliberately. Verify claims. Abstain when evidence is missing.
