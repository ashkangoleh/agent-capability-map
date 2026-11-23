---
name: marketing-affiliate-payout-integrity
description: "Use for design affiliate commission attribution and reconciliation with fraud and refund controls. Activate only when the task concerns creators and partnerships; exclude unrelated SEO, general data engineering and generic product experiments."
metadata:
  version: "1.0.0"
---

# marketing-affiliate-payout-integrity

## Activation boundary
Design affiliate commission attribution and reconciliation with fraud and refund controls. Do not assume provider features, law, account eligibility, real campaign performance, or tool permissions.

## Required inputs
Partner contracts, attribution windows, commission rules, referral identifiers, orders, refunds, disputes and payment ledger. Determine actual platform/API release, market/jurisdiction, consent and business decision owner before execution.

## Specialist procedure
1. Document a versioned commission policy: qualifying action, window, exclusions, cookie/device limitations and contract precedence.
2. Join referral to unique qualifying order with event-time constraints, deterministic priority and recorded tie resolution.
3. Identify self-referrals, duplicate conversions, coupon abuse, refunds, chargebacks and late-arriving attribution updates.
4. Build an auditable payout ledger with reversible adjustment records and separation of approval from disbursement.
5. Report partner disputes with replayable evidence; avoid asserting intent or fraud guilt from a single heuristic.

## Operational failure and recovery
- Failure: Refunded or duplicated orders are paid twice, or legitimate partners are wrongly accused of fraud.
- Containment: stop or quarantine the affected campaign, audience, conversion uploads or spend pathway as appropriate; identify the authorised incident owner.
- Recovery: fix the source issue, replay/reconcile against a frozen ledger or sample, verify that late events or previous recipients are not double-counted, then resume by approved staged release.
- Do not modify remote platforms, send messages, spend budget, export personal data, or claim account access without explicit authorization.

## Independent falsification
- Negative/adversarial case: Multiple partners claim the same order; quarantine until contract priority resolves ownership.
- Independent acceptance oracle: Payout totals reconcile to eligible unique orders and adjustments, with signed finance approval.
- Record actual observed evidence, test environment, sample coverage, expected outcome and uncertainty; a proposed test is not an executed test.

## Official source starting points
- https://www.ftc.gov/business-guidance/resources/disclosures-101-social-media-influencers
Check the exact published/current version, effective date, API eligibility and local rules at execution; source URLs are not operational certification.

## Output contract
Produce a scoped artifact, decision criteria, evidence/source ledger, assumptions, failure thresholds, test cases, owner, rollback trigger and unresolved risks. Separate observed facts, hypotheses and recommendations. Do not fabricate audience sizes, conversion rates, ROAS or impact estimates.

## Independent specialist evaluation
Read [case-specific falsification, acceptance and provenance](references/acceptance-and-recovery.md) on demand for production-impacting work. Passing static registry checks does not prove correctness or authorize any action.
