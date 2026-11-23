---
name: marketing-consent-suppression
description: "Use for define enforceable eligibility and suppression rules for direct marketing at send time. Activate only when the task concerns lifecycle and crm; exclude unrelated SEO, general data engineering and generic product experiments."
metadata:
  version: "1.0.0"
---

# marketing-consent-suppression

## Activation boundary
Define enforceable eligibility and suppression rules for direct marketing at send time. Do not assume provider features, law, account eligibility, real campaign performance, or tool permissions.

## Required inputs
Jurisdiction, channel, contact provenance, lawful-basis assessment, subscription timestamp, withdrawal records and audience snapshot. Determine actual platform/API release, market/jurisdiction, consent and business decision owner before execution.

## Specialist procedure
1. Identify the applicable jurisdiction and channel-specific rules; distinguish lawful-basis questions from product preference settings.
2. Model contact permission by purpose, channel, source and time with a fail-closed unknown-consent policy where required.
3. Enforce suppression before audience export, scheduling, retries and vendor dispatch; propagate opt-out and deletion changes.
4. Reconcile sample records across CRM, warehouse and send vendor; inspect stale snapshots and concurrent unsubscribe races.
5. Escalate legal interpretation to qualified reviewers; never invent consent or exempt a recipient based only on engagement.

## Operational failure and recovery
- Failure: An unsubscribe after audience export is ignored and an unlawful follow-up is sent.
- Containment: stop or quarantine the affected campaign, audience, conversion uploads or spend pathway as appropriate; identify the authorised incident owner.
- Recovery: fix the source issue, replay/reconcile against a frozen ledger or sample, verify that late events or previous recipients are not double-counted, then resume by approved staged release.
- Do not modify remote platforms, send messages, spend budget, export personal data, or claim account access without explicit authorization.

## Independent falsification
- Negative/adversarial case: Missing consent provenance or recent unsubscribe; exclude recipient pending verified authority.
- Independent acceptance oracle: All dispatched recipients pass a documented effective-time eligibility check; suppressed records receive zero sends.
- Record actual observed evidence, test environment, sample coverage, expected outcome and uncertainty; a proposed test is not an executed test.

## Official source starting points
- https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guidance-on-direct-marketing-using-electronic-mail/
- https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/direct-marketing-guidance/plan-direct-marketing/
Check the exact published/current version, effective date, API eligibility and local rules at execution; source URLs are not operational certification.

## Output contract
Produce a scoped artifact, decision criteria, evidence/source ledger, assumptions, failure thresholds, test cases, owner, rollback trigger and unresolved risks. Separate observed facts, hypotheses and recommendations. Do not fabricate audience sizes, conversion rates, ROAS or impact estimates.

## Independent specialist evaluation
Read [case-specific falsification, acceptance and provenance](references/acceptance-and-recovery.md) on demand for production-impacting work. Passing static registry checks does not prove correctness or authorize any action.
