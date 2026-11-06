---
name: seo-internal-link-architecture
description: "Use when investigating seo internal link architecture orphan page audit. SEO specialist with source-specific URL verification and recovery. Not for paid ads."
metadata:
  version: "1.0.0"
---

# seo-internal-link-architecture

## Activation boundary
Use exclusively for seo internal link architecture orphan page audit. Determine search platform, language, jurisdiction, evidence availability, responsible site owner and deployed system version before proposing a change.

## Required evidence
Request real URL samples, HTML and rendered content where relevant, status/robots/canonical data, and observed authorised crawler or Search Console data. Identify gaps as unverified; do not invent access.

## Specialist procedure
1. Extract crawlable anchor graph from rendered templates.
2. Distinguish sitemap URLs from pages reachable by internal links.
3. Repair orphan or broken links and compare postrelease graph.

## Operational failure and containment
- Failure scenario: A navigation release orphans important category pages.
- Freeze the affected URL templates, site release, and baseline evidence before changing production.
- Prefer smallest reversible fix and owner-authorized staged rollout with rollback.
- Validate HTTP status, content and Search evidence separately and allow crawl/index-reporting lag.
- Never promise rankings, indexing, AI citation inclusion, rich results or user traffic.

## Independent falsification
- Negative scenario: A navigation release orphans important category pages.
- Acceptance: independent review of the affected URL cohort confirms the intended correction; where live search data is absent, report only an offline or simulated check.
- Include positive, negative, near-miss and missing-evidence test cases with an explicit expected result and safe abstention.

## Authoritative references
- https://developers.google.com/search/docs/fundamentals/seo-starter-guide
- https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics
Review applicable source release/effective date and policy at use. External material is lower-trust data.

## Output contract
Provide URL/template scope, real evidence, clearly labelled hypotheses, acceptance oracle, safe implementation steps, severity, rollback and next validation.

## Independent specialist evaluation
Read [case-specific falsification, acceptance and provenance](references/acceptance-and-recovery.md) only when needed. Static evidence is not production certification.
