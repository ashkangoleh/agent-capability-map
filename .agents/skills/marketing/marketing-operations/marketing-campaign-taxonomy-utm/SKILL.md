---
name: marketing-campaign-taxonomy-utm
description: "Use for standardize channel/campaign identifiers without losing historical attribution comparability. Activate only when the task concerns marketing operations; exclude unrelated SEO, general data engineering and generic product experiments."
metadata:
  version: "1.0.0"
---

# marketing-campaign-taxonomy-utm

## Activation boundary
Standardize channel/campaign identifiers without losing historical attribution comparability. Do not assume provider features, law, account eligibility, real campaign performance, or tool permissions.

## Required inputs
Existing UTM conventions, paid platform IDs, channel mapping, tagging permissions, source exports, redirect rules and reporting consumers. Determine actual platform/API release, market/jurisdiction, consent and business decision owner before execution.

## Specialist procedure
1. Define immutable campaign IDs and bounded naming/UTM dimensions with character encoding, case and reserved-value rules.
2. Separate canonical IDs from human-readable labels; document ownership, schema changes and allowed backfills.
3. Test redirects and nested query strings for parameter loss, duplication and accidental personally identifiable data.
4. Implement exceptions and unknown-channel buckets without silently rewriting historical campaign source classifications.
5. Publish data-quality controls, reporting migration checks and a rollback plan for collector changes.

## Operational failure and recovery
- Failure: A naming change silently fragments campaign reporting or exposes private data in URL parameters.
- Containment: stop or quarantine the affected campaign, audience, conversion uploads or spend pathway as appropriate; identify the authorised incident owner.
- Recovery: fix the source issue, replay/reconcile against a frozen ledger or sample, verify that late events or previous recipients are not double-counted, then resume by approved staged release.
- Do not modify remote platforms, send messages, spend budget, export personal data, or claim account access without explicit authorization.

## Independent falsification
- Negative/adversarial case: A new campaign alias collides with an old ID; reject until mapped explicitly.
- Independent acceptance oracle: Sample click-to-conversion journeys preserve canonical IDs and reproduce old/new channel totals under documented mapping.
- Record actual observed evidence, test environment, sample coverage, expected outcome and uncertainty; a proposed test is not an executed test.

## Official source starting points
- https://support.google.com/analytics/answer/9267735/
Check the exact published/current version, effective date, API eligibility and local rules at execution; source URLs are not operational certification.

## Output contract
Produce a scoped artifact, decision criteria, evidence/source ledger, assumptions, failure thresholds, test cases, owner, rollback trigger and unresolved risks. Separate observed facts, hypotheses and recommendations. Do not fabricate audience sizes, conversion rates, ROAS or impact estimates.

## Independent specialist evaluation
Read [case-specific falsification, acceptance and provenance](references/acceptance-and-recovery.md) on demand for production-impacting work. Passing static registry checks does not prove correctness or authorize any action.
