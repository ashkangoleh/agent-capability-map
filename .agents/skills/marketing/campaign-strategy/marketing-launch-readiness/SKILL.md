---
name: marketing-launch-readiness
description: "Use for evaluate cross-functional go-to-market launch readiness before spend or customer exposure. Activate only when the task concerns campaign strategy; exclude unrelated SEO, general data engineering and generic product experiments."
metadata:
  version: "1.0.0"
---

# marketing-launch-readiness

## Activation boundary
Evaluate cross-functional go-to-market launch readiness before spend or customer exposure. Do not assume provider features, law, account eligibility, real campaign performance, or tool permissions.

## Required inputs
Offer, target customers, geography, product availability, landing destination, budget owner, consent status, event schema, campaign calendar and escalation owner. Determine actual platform/API release, market/jurisdiction, consent and business decision owner before execution.

## Specialist procedure
1. Draw a launch dependency graph: product entitlement, inventory, pricing, creative claims, legal approvals, landing page and tracking.
2. Define go/no-go gates with owner, observed evidence, hard-block criteria and a rehearsed rollback or pause action.
3. Validate channel-to-landing-page URL paths, offers, locale/currency, audience eligibility and event-level conversion trace.
4. Stage a controlled smoke test before spend; predefine anomaly thresholds and a post-launch stop decision.
5. Report any unresolved launch dependency explicitly instead of substituting assumptions.

## Operational failure and recovery
- Failure: An offer goes live before inventory or tracking and produces irreversible spend or misleading claims.
- Containment: stop or quarantine the affected campaign, audience, conversion uploads or spend pathway as appropriate; identify the authorised incident owner.
- Recovery: fix the source issue, replay/reconcile against a frozen ledger or sample, verify that late events or previous recipients are not double-counted, then resume by approved staged release.
- Do not modify remote platforms, send messages, spend budget, export personal data, or claim account access without explicit authorization.

## Independent falsification
- Negative/adversarial case: Tracking reports conversions but backend order ledger records none; block go-live rather than assert campaign success.
- Independent acceptance oracle: Signed launch evidence ledger: every critical dependency has verified owner, source, status and pause/rollback owner.
- Record actual observed evidence, test environment, sample coverage, expected outcome and uncertainty; a proposed test is not an executed test.

## Official source starting points
- https://support.google.com/analytics/answer/9267735/
- https://support.google.com/google-ads/answer/12003020
Check the exact published/current version, effective date, API eligibility and local rules at execution; source URLs are not operational certification.

## Output contract
Produce a scoped artifact, decision criteria, evidence/source ledger, assumptions, failure thresholds, test cases, owner, rollback trigger and unresolved risks. Separate observed facts, hypotheses and recommendations. Do not fabricate audience sizes, conversion rates, ROAS or impact estimates.

## Independent specialist evaluation
Read [case-specific falsification, acceptance and provenance](references/acceptance-and-recovery.md) on demand for production-impacting work. Passing static registry checks does not prove correctness or authorize any action.
