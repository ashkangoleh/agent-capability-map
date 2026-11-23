---
name: marketing-spend-pacing
description: "Use for set bounded spend controls without confusing platform-reported roas with incremental profit. Activate only when the task concerns performance marketing; exclude unrelated SEO, general data engineering and generic product experiments."
metadata:
  version: "1.0.0"
---

# marketing-spend-pacing

## Activation boundary
Set bounded spend controls without confusing platform-reported ROAS with incremental profit. Do not assume provider features, law, account eligibility, real campaign performance, or tool permissions.

## Required inputs
Approved budget, pacing periods, contractual minimums, campaign owner, channel limits, contribution margin, attribution caveats and reconciliation cutoffs. Determine actual platform/API release, market/jurisdiction, consent and business decision owner before execution.

## Specialist procedure
1. Separate committed budget, actual ledger spend, pending invoices and platform provisional spend by currency and timezone.
2. Calculate daily and cumulative pacing versus calendar and campaign delivery targets, explicitly handling partial days and late invoices.
3. Determine hard caps, approval thresholds, platform safety stop, reallocation conditions and account permissions.
4. Stress test a 2x spend spike, delayed invoice, underdelivery and data outage; never use stale dashboards as the only stop signal.
5. Reconcile exceptions with finance before presenting apparent ROAS or CAC gains as unit-economics improvements.

## Operational failure and recovery
- Failure: Spend continues after tracking failure or a dashboard underreports booked cost.
- Containment: stop or quarantine the affected campaign, audience, conversion uploads or spend pathway as appropriate; identify the authorised incident owner.
- Recovery: fix the source issue, replay/reconcile against a frozen ledger or sample, verify that late events or previous recipients are not double-counted, then resume by approved staged release.
- Do not modify remote platforms, send messages, spend budget, export personal data, or claim account access without explicit authorization.

## Independent falsification
- Negative/adversarial case: Platform cost feed is 24 hours late while campaigns are spending; stop automated increase.
- Independent acceptance oracle: Total booked plus committed spend remains within the approved limit, with documented delayed-cost reconciliation.
- Record actual observed evidence, test environment, sample coverage, expected outcome and uncertainty; a proposed test is not an executed test.

## Official source starting points
- https://developers.google.com/google-ads/api/docs/conversions/overview
Check the exact published/current version, effective date, API eligibility and local rules at execution; source URLs are not operational certification.

## Output contract
Produce a scoped artifact, decision criteria, evidence/source ledger, assumptions, failure thresholds, test cases, owner, rollback trigger and unresolved risks. Separate observed facts, hypotheses and recommendations. Do not fabricate audience sizes, conversion rates, ROAS or impact estimates.

## Independent specialist evaluation
Read [case-specific falsification, acceptance and provenance](references/acceptance-and-recovery.md) on demand for production-impacting work. Passing static registry checks does not prove correctness or authorize any action.
