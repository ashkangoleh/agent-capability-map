---
name: marketing-campaign-release-controls
description: "Use for treat marketing campaign deployment as a controlled production change with measurable abort criteria. Activate only when the task concerns marketing operations; exclude unrelated SEO, general data engineering and generic product experiments."
metadata:
  version: "1.0.0"
---

# marketing-campaign-release-controls

## Activation boundary
Treat marketing campaign deployment as a controlled production change with measurable abort criteria. Do not assume provider features, law, account eligibility, real campaign performance, or tool permissions.

## Required inputs
Change scope, budget cap, active campaigns, account permissions, creative approvals, telemetry, vendors and incident contacts. Determine actual platform/API release, market/jurisdiction, consent and business decision owner before execution.

## Specialist procedure
1. Inventory affected ads, email journeys, landing pages, pixels and attribution settings as one release boundary.
2. Require approvals for legal claims, sensitive targeting, spend, privacy, production access and destination links.
3. Run limited exposure smoke tests with conversion event reconciliation, consent checks and known-good rollback state.
4. Define stop/rollback triggers for budget overrun, link breakage, data quality regression or erroneous recipients.
5. Capture the change log, incident owner, post-release watch metrics and documented restoration procedure.

## Operational failure and recovery
- Failure: A partial marketing release mixes new creative and old conversion tracking, leading to expensive, misleading optimization.
- Containment: stop or quarantine the affected campaign, audience, conversion uploads or spend pathway as appropriate; identify the authorised incident owner.
- Recovery: fix the source issue, replay/reconcile against a frozen ledger or sample, verify that late events or previous recipients are not double-counted, then resume by approved staged release.
- Do not modify remote platforms, send messages, spend budget, export personal data, or claim account access without explicit authorization.

## Independent falsification
- Negative/adversarial case: Missing campaign pause permission at launch time; hold release until an authorized owner is present.
- Independent acceptance oracle: Preflight artifacts, reversible change path, and post-release reconciliation pass independently before full exposure.
- Record actual observed evidence, test environment, sample coverage, expected outcome and uncertainty; a proposed test is not an executed test.

## Official source starting points
- https://support.google.com/analytics/answer/9267735/
- https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/direct-marketing-guidance/plan-direct-marketing/
Check the exact published/current version, effective date, API eligibility and local rules at execution; source URLs are not operational certification.

## Output contract
Produce a scoped artifact, decision criteria, evidence/source ledger, assumptions, failure thresholds, test cases, owner, rollback trigger and unresolved risks. Separate observed facts, hypotheses and recommendations. Do not fabricate audience sizes, conversion rates, ROAS or impact estimates.

## Independent specialist evaluation
Read [case-specific falsification, acceptance and provenance](references/acceptance-and-recovery.md) on demand for production-impacting work. Passing static registry checks does not prove correctness or authorize any action.
