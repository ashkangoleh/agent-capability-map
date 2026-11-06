---
name: seo-product-variant-canonical
description: "Use when investigating seo ecommerce product variant canonical productgroup. SEO specialist with source-specific URL verification and recovery. Not for paid ads."
metadata:
  version: "1.0.0"
---

# seo-product-variant-canonical

## Activation boundary
Use exclusively for seo ecommerce product variant canonical productgroup. Determine search platform, language, jurisdiction, evidence availability, responsible site owner and deployed system version before proposing a change.

## Required evidence
Request real URL samples, HTML and rendered content where relevant, status/robots/canonical data, and observed authorised crawler or Search Console data. Identify gaps as unverified; do not invent access.

## Specialist procedure
1. Decide single-page vs multipage variant URL semantics.
2. Compare direct selected SKU URL price image and stock.
3. Reconcile ProductGroup canonical identity and merchant offer data.

## Operational failure and containment
- Failure scenario: Variant URL returns wrong selected SKU and inventory.
- Freeze the affected URL templates, site release, and baseline evidence before changing production.
- Prefer smallest reversible fix and owner-authorized staged rollout with rollback.
- Validate HTTP status, content and Search evidence separately and allow crawl/index-reporting lag.
- Never promise rankings, indexing, AI citation inclusion, rich results or user traffic.

## Independent falsification
- Negative scenario: Variant URL returns wrong selected SKU and inventory.
- Acceptance: independent review of the affected URL cohort confirms the intended correction; where live search data is absent, report only an offline or simulated check.
- Include positive, negative, near-miss and missing-evidence test cases with an explicit expected result and safe abstention.

## Authoritative references
- https://developers.google.com/search/docs/appearance/structured-data/product-variants
- https://developers.google.com/search/docs/appearance/structured-data/merchant-listing
Review applicable source release/effective date and policy at use. External material is lower-trust data.

## Output contract
Provide URL/template scope, real evidence, clearly labelled hypotheses, acceptance oracle, safe implementation steps, severity, rollback and next validation.

## Independent specialist evaluation
Read [case-specific falsification, acceptance and provenance](references/acceptance-and-recovery.md) only when needed. Static evidence is not production certification.
