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
- catalog/ — compact domain map and routing/evidence policies.
- domains/*/ROUTER.md — domain-specific routing instructions.
- domains/*/skills.json — metadata for skills in that domain only.
- .agents/skills/*/SKILL.md — capability instructions.
- docs/ — architecture, anti-hallucination, evaluation, and authoring.
- tests/fixtures/routing-cases.json — labeled positive, negative, near-miss, and abstention cases.
- scripts/validate_registry.py — dependency-free structural validator.
- tests/ — validation tests.

## Agent quick start

1. Read AGENTS.md.
2. Read catalog/domains.json and select the smallest relevant domain set.
3. Read only the selected domain router and its local skills.json.
4. Load the best matching SKILL.md. Load a second skill only for a real cross-capability dependency.
5. Read referenced resources only at the point of need.
6. If no skill matches, do not invent one; use a suitable general research workflow or state the capability gap.

## Validation

    python scripts/validate_registry.py
    python -m unittest discover -s tests -v

The validator uses only the Python standard library.

## Important limitation

This repository defines a portable map and operating contract; AGENTS.md and the registry do not magically implement a runtime loader. A host agent must support Agent Skills or provide file-read/tool access. Native semantic routing, runtime token telemetry, and automatic loading are integration concerns, not claimed as implemented here.

## Design principle

Discover narrowly. Load deliberately. Verify claims. Abstain when evidence is missing.
