---
name: seo-crawler-log-diagnostics
description: "Use when investigating seo googlebot server log verification status analysis. SEO specialist with source-specific URL verification and recovery. Not for paid ads."
metadata:
  version: "1.0.0"
---

# seo-crawler-log-diagnostics

## Activation boundary
Use exclusively for seo googlebot server log verification status analysis. Determine search platform, language, jurisdiction, evidence availability, responsible site owner and deployed system version before proposing a change.

## Required evidence
Request real URL samples, HTML and rendered content where relevant, status/robots/canonical data, and observed authorised crawler or Search Console data. Identify gaps as unverified; do not invent access.

## Specialist procedure
1. Verify bot identity rather than trusting User Agent text.
2. Correlate sanitized 4xx 5xx and crawl samples with deployments.
3. Report affected URL classes and independently retest status.

## Operational failure and containment
- Failure scenario: Spoofed bot traffic is treated as verified Googlebot.
- Freeze the affected URL templates, site release, and baseline evidence before changing production.
- Prefer smallest reversible fix and owner-authorized staged rollout with rollback.
- Validate HTTP status, content and Search evidence separately and allow crawl/index-reporting lag.
- Never promise rankings, indexing, AI citation inclusion, rich results or user traffic.

## Independent falsification
- Negative scenario: Spoofed bot traffic is treated as verified Googlebot.
- Acceptance: independent review of the affected URL cohort confirms the intended correction; where live search data is absent, report only an offline or simulated check.
- Include positive, negative, near-miss and missing-evidence test cases with an explicit expected result and safe abstention.

## Authoritative references
- https://developers.google.com/crawling/docs/crawl-budget
- https://developers.google.com/search/docs/crawling-indexing/troubleshoot-crawling-errors
Review applicable source release/effective date and policy at use. External material is lower-trust data.

## Output contract
Provide URL/template scope, real evidence, clearly labelled hypotheses, acceptance oracle, safe implementation steps, severity, rollback and next validation.

## Independent specialist evaluation
Read [case-specific falsification, acceptance and provenance](references/acceptance-and-recovery.md) only when needed. Static evidence is not production certification.
