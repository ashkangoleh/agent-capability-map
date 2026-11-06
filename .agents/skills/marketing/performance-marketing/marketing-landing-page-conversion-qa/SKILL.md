---
name: marketing-landing-page-conversion-qa
description: "Use for validate post-click user journey and transaction integrity before scaling acquisition. Activate only when the task concerns performance marketing; exclude unrelated SEO, general data engineering and generic product experiments."
metadata:
  version: "1.0.0"
---

# marketing-landing-page-conversion-qa

## Activation boundary
Validate post-click user journey and transaction integrity before scaling acquisition. Do not assume provider features, law, account eligibility, real campaign performance, or tool permissions.

## Required inputs
Landing URL matrix, offer/copy, browsers, mobile devices, load budget, checkout access, consent, event IDs and backend conversion source. Determine actual platform/API release, market/jurisdiction, consent and business decision owner before execution.

## Specialist procedure
1. Create a URL matrix for campaign parameters, redirects, region, device and language and verify final destinations.
2. Test offer parity, accessibility, content trust, form errors, checkout, consent and opt-out without relying solely on visual inspection.
3. Measure real or lab page responsiveness with documented limitations; isolate slow third-party scripts and analytics tags.
4. Verify conversion events once per business transaction and reconcile client-side tracking with server-side order truth.
5. Provide defect severity, reproduction steps, owner, release block and rollback criteria.

## Operational failure and recovery
- Failure: Landing page generates duplicate purchase events or hides a critical checkout error behind healthy click-through.
- Containment: stop or quarantine the affected campaign, audience, conversion uploads or spend pathway as appropriate; identify the authorised incident owner.
- Recovery: fix the source issue, replay/reconcile against a frozen ledger or sample, verify that late events or previous recipients are not double-counted, then resume by approved staged release.
- Do not modify remote platforms, send messages, spend budget, export personal data, or claim account access without explicit authorization.

## Independent falsification
- Negative/adversarial case: Pageview works while payment completion fails on mobile; block scale-up.
- Independent acceptance oracle: Representative user journeys complete successfully and event count reconciles against unique transaction IDs.
- Record actual observed evidence, test environment, sample coverage, expected outcome and uncertainty; a proposed test is not an executed test.

## Official source starting points
- https://web.dev/articles/vitals
- https://support.google.com/analytics/answer/9267735/
Check the exact published/current version, effective date, API eligibility and local rules at execution; source URLs are not operational certification.

## Output contract
Produce a scoped artifact, decision criteria, evidence/source ledger, assumptions, failure thresholds, test cases, owner, rollback trigger and unresolved risks. Separate observed facts, hypotheses and recommendations. Do not fabricate audience sizes, conversion rates, ROAS or impact estimates.

## Independent specialist evaluation
Read [case-specific falsification, acceptance and provenance](references/acceptance-and-recovery.md) on demand for production-impacting work. Passing static registry checks does not prove correctness or authorize any action.
