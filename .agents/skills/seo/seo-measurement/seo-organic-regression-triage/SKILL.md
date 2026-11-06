---
name: seo-organic-regression-triage
description: "Use when investigating seo organic traffic regression incident diagnose. SEO specialist with source-specific URL verification and recovery. Not for paid ads."
metadata:
  version: "1.0.0"
---

# seo-organic-regression-triage

## Activation boundary
Use exclusively for seo organic traffic regression incident diagnose. Determine search platform, language, jurisdiction, evidence availability, responsible site owner and deployed system version before proposing a change.

## Required evidence
Request real URL samples, HTML and rendered content where relevant, status/robots/canonical data, and observed authorised crawler or Search Console data. Identify gaps as unverified; do not invent access.

## Specialist procedure
1. Validate instrumentation freshness before diagnosing search decline.
2. Compare GSC impressions clicks and independent server cohorts.
3. Correlate errors robots canonical render and deployment changes.

## Operational failure and containment
- Failure scenario: Analytics tag outage is mislabelled a Google penalty.
- Freeze the affected URL templates, site release, and baseline evidence before changing production.
- Prefer smallest reversible fix and owner-authorized staged rollout with rollback.
- Validate HTTP status, content and Search evidence separately and allow crawl/index-reporting lag.
- Never promise rankings, indexing, AI citation inclusion, rich results or user traffic.

## Independent falsification
- Negative scenario: Analytics tag outage is mislabelled a Google penalty.
- Acceptance: independent review of the affected URL cohort confirms the intended correction; where live search data is absent, report only an offline or simulated check.
- Include positive, negative, near-miss and missing-evidence test cases with an explicit expected result and safe abstention.

## Authoritative references
- https://developers.google.com/webmaster-tools/v1/searchanalytics/query
- https://developers.google.com/search/docs/crawling-indexing/troubleshoot-crawling-errors
Review applicable source release/effective date and policy at use. External material is lower-trust data.

## Output contract
Provide URL/template scope, real evidence, clearly labelled hypotheses, acceptance oracle, safe implementation steps, severity, rollback and next validation.

## Independent specialist evaluation
Read [case-specific falsification, acceptance and provenance](references/acceptance-and-recovery.md) only when needed. Static evidence is not production certification.
