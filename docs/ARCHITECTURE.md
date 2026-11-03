# Architecture

## Objective

Provide a portable capability map that routes a task through progressively narrower metadata and loads only the instructions and resources needed for that task.

## Layers

1. Root contract — AGENTS.md: stable global rules, routing sequence, safety, evidence, and context discipline.
2. Domain catalog — catalog/domains.json: compact map of domain IDs, descriptions, routers, and subdomains.
3. Domain router — domains/<domain>/ROUTER.md: domain-specific disambiguation and routing constraints.
4. Local registry — domains/<domain>/skills.json: concise metadata for skills in the selected domain only.
5. Skill — .agents/skills/<id>/SKILL.md: actionable procedure for one coherent capability.
6. Resources — references/, scripts/, assets/: loaded or executed only when the active skill needs them.

## Why hierarchical routing

A flat registry makes every request compete against every skill and encourages broad context loading. Hierarchical routing narrows the search space before detailed instructions are read. Local registries keep future growth from forcing every domain's metadata into every request.

## Runtime contract

This repository does not implement a universal loader. A compatible host must read AGENTS.md as repository guidance, access the catalog and selected domain files, discover skills under .agents/skills or load them by explicit path, and provide file/resource access. Native Agent Skills clients can use SKILL.md packages, but discovery and routing behavior varies by host. Verify actual client behavior rather than assuming every client interprets the custom domain registry.

## Routing lifecycle

Parse intent → select domain → read domain router → inspect local registry → select skill → load SKILL.md → fetch exact resources → execute → verify → report.

## Composition

Use one skill for one coherent unit of work. Compose skills only where a real dependency exists. A product launch may require product discovery, marketing strategy, and SEO; a request to write a PRD should not load all three.

## Why no graph database yet

The domain hierarchy is shallow and the registry is small. JSON files, paths, and deterministic validation are simpler to review, version, diff, and cache. Add semantic retrieval or a graph only after measured misses, ambiguous routing, or dependency complexity justify the added complexity.
