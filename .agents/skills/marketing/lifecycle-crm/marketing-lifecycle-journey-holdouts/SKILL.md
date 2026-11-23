---
name: marketing-lifecycle-journey-holdouts
description: "Use for design lifecycle journeys with frequency caps, identity correctness and incremental retention measurement. Activate only when the task concerns lifecycle and crm; exclude unrelated SEO, general data engineering and generic product experiments."
metadata:
  version: "1.0.0"
---

# marketing-lifecycle-journey-holdouts

## Activation boundary
Design lifecycle journeys with frequency caps, identity correctness and incremental retention measurement. Do not assume provider features, law, account eligibility, real campaign performance, or tool permissions.

## Required inputs
Lifecycle states, entry/exit events, identity resolution, consent, message budget, experiment unit, renewal cadence and delayed outcomes. Determine actual platform/API release, market/jurisdiction, consent and business decision owner before execution.

## Specialist procedure
1. Define state transitions, eligibility, cooldowns, re-entry limits and journey termination on account changes or opt-outs.
2. Deduplicate event-driven entry against business identifiers and guard against out-of-order updates, replay and late events.
3. Design holdouts or controlled exposure to distinguish organic repeat purchases from message-attributed returns.
4. Track fatigue, complaints, churn and margin as guardrails; do not optimise open rate alone.
5. Specify pause, retry, compensation and replay tests for vendor outages and mismatched CRM state.

## Operational failure and recovery
- Failure: Out-of-order user events retrigger a cancelled journey, causing repeated contact and biased conversion counts.
- Containment: stop or quarantine the affected campaign, audience, conversion uploads or spend pathway as appropriate; identify the authorised incident owner.
- Recovery: fix the source issue, replay/reconcile against a frozen ledger or sample, verify that late events or previous recipients are not double-counted, then resume by approved staged release.
- Do not modify remote platforms, send messages, spend budget, export personal data, or claim account access without explicit authorization.

## Independent falsification
- Negative/adversarial case: A churned, opted-out user is replayed into onboarding; block the send.
- Independent acceptance oracle: For each test identity, state transitions produce at most intended messages while suppression and holdout are preserved.
- Record actual observed evidence, test environment, sample coverage, expected outcome and uncertainty; a proposed test is not an executed test.

## Official source starting points
- https://support.google.com/analytics/answer/9267735/
- https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guidance-on-direct-marketing-using-electronic-mail/
Check the exact published/current version, effective date, API eligibility and local rules at execution; source URLs are not operational certification.

## Output contract
Produce a scoped artifact, decision criteria, evidence/source ledger, assumptions, failure thresholds, test cases, owner, rollback trigger and unresolved risks. Separate observed facts, hypotheses and recommendations. Do not fabricate audience sizes, conversion rates, ROAS or impact estimates.

## Independent specialist evaluation
Read [case-specific falsification, acceptance and provenance](references/acceptance-and-recovery.md) on demand for production-impacting work. Passing static registry checks does not prove correctness or authorize any action.
