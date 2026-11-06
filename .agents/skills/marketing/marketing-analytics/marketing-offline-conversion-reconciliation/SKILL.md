---
name: marketing-offline-conversion-reconciliation
description: "Use for reconcile ads-system conversions with order or lead truth before importing or adjusting offline events. Activate only when the task concerns marketing analytics; exclude unrelated SEO, general data engineering and generic product experiments."
metadata:
  version: "1.0.0"
---

# marketing-offline-conversion-reconciliation

## Activation boundary
Reconcile ads-system conversions with order or lead truth before importing or adjusting offline events. Do not assume provider features, law, account eligibility, real campaign performance, or tool permissions.

## Required inputs
Account/conversion action ownership, API release, click identifiers, orders, timestamps/timezones, values, currencies, consent, retries and attribution window. Determine actual platform/API release, market/jurisdiction, consent and business decision owner before execution.

## Specialist procedure
1. Choose the provider-supported workflow for the deployed API and account rather than assuming an old upload endpoint remains available.
2. Build a canonical event contract with stable order ID, event time, change type, currency, click identity and provenance.
3. Deduplicate and order conversion/retraction/restate events; handle refunds, late data, partial responses and retry idempotency.
4. Distinguish accepted API uploads from eventual attribution; reconcile downstream diagnostics to source-of-truth orders.
5. Require approvals, dry-run samples, staged rollouts, reconciliation thresholds and replay/rollback paths before write operations.

## Operational failure and recovery
- Failure: Successful upload response is treated as proof of correct attributed conversions, while duplicate orders inflate results.
- Containment: stop or quarantine the affected campaign, audience, conversion uploads or spend pathway as appropriate; identify the authorised incident owner.
- Recovery: fix the source issue, replay/reconcile against a frozen ledger or sample, verify that late events or previous recipients are not double-counted, then resume by approved staged release.
- Do not modify remote platforms, send messages, spend budget, export personal data, or claim account access without explicit authorization.

## Independent falsification
- Negative/adversarial case: Unknown consent or missing conversion action ownership; do not export customer identifiers.
- Independent acceptance oracle: Unique valid order/conversion IDs and total values reconcile across source and destination, with acknowledged delays.
- Record actual observed evidence, test environment, sample coverage, expected outcome and uncertainty; a proposed test is not an executed test.

## Official source starting points
- https://developers.google.com/google-ads/api/docs/conversions/overview
- https://developers.google.com/google-ads/api/docs/conversions/upload-offline
Check the exact published/current version, effective date, API eligibility and local rules at execution; source URLs are not operational certification.

## Output contract
Produce a scoped artifact, decision criteria, evidence/source ledger, assumptions, failure thresholds, test cases, owner, rollback trigger and unresolved risks. Separate observed facts, hypotheses and recommendations. Do not fabricate audience sizes, conversion rates, ROAS or impact estimates.

## Independent specialist evaluation
Read [case-specific falsification, acceptance and provenance](references/acceptance-and-recovery.md) on demand for production-impacting work. Passing static registry checks does not prove correctness or authorize any action.
