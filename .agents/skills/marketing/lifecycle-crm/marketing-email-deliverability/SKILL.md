---
name: marketing-email-deliverability
description: "Use for investigate email delivery failures without weakening authentication or bypassing suppression. Activate only when the task concerns lifecycle and crm; exclude unrelated SEO, general data engineering and generic product experiments."
metadata:
  version: "1.0.0"
---

# marketing-email-deliverability

## Activation boundary
Investigate email delivery failures without weakening authentication or bypassing suppression. Do not assume provider features, law, account eligibility, real campaign performance, or tool permissions.

## Required inputs
Domain identity, sending service, DNS records, authentication results, bounce samples, complaint rates, reputation history and consent records. Determine actual platform/API release, market/jurisdiction, consent and business decision owner before execution.

## Specialist procedure
1. Verify the actual sending domain, envelope-from, SPF, DKIM alignment, DMARC policy and sending platform configuration.
2. Separate acceptance, delivery, spam placement, opens and recipient actions; do not infer inbox placement from provider acceptance.
3. Inspect hard/soft bounces, complaint trends, list acquisition and unsubscribe processing against current provider rules.
4. Use reversible staged volume changes only after confirming permission, infrastructure ownership and policy compliance.
5. Record recipient-domain-specific failures and a sender-owner rollback plan; never evade abuse controls.

## Operational failure and recovery
- Failure: Authentication passes but recipients are spam-filtered, or sender reputation is damaged by recycled addresses.
- Containment: stop or quarantine the affected campaign, audience, conversion uploads or spend pathway as appropriate; identify the authorised incident owner.
- Recovery: fix the source issue, replay/reconcile against a frozen ledger or sample, verify that late events or previous recipients are not double-counted, then resume by approved staged release.
- Do not modify remote platforms, send messages, spend budget, export personal data, or claim account access without explicit authorization.

## Independent falsification
- Negative/adversarial case: Request to remove unsubscribe or weaken DMARC to improve delivery; reject.
- Independent acceptance oracle: Authentication and bounce/complaint diagnostics improve without increasing unsolicited sends.
- Record actual observed evidence, test environment, sample coverage, expected outcome and uncertainty; a proposed test is not an executed test.

## Official source starting points
- https://support.google.com/mail/answer/81126?hl=en-GB
Check the exact published/current version, effective date, API eligibility and local rules at execution; source URLs are not operational certification.

## Output contract
Produce a scoped artifact, decision criteria, evidence/source ledger, assumptions, failure thresholds, test cases, owner, rollback trigger and unresolved risks. Separate observed facts, hypotheses and recommendations. Do not fabricate audience sizes, conversion rates, ROAS or impact estimates.

## Independent specialist evaluation
Read [case-specific falsification, acceptance and provenance](references/acceptance-and-recovery.md) on demand for production-impacting work. Passing static registry checks does not prove correctness or authorize any action.
