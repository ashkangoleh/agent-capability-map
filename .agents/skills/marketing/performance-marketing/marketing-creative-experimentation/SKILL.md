---
name: marketing-creative-experimentation
description: "Use for design a defensible paid-creative experiment with explicit randomization and decision rules. Activate only when the task concerns performance marketing; exclude unrelated SEO, general data engineering and generic product experiments."
metadata:
  version: "1.0.0"
---

# marketing-creative-experimentation

## Activation boundary
Design a defensible paid-creative experiment with explicit randomization and decision rules. Do not assume provider features, law, account eligibility, real campaign performance, or tool permissions.

## Required inputs
Creative variants, audience overlap, assignment unit, campaign objectives, minimum detectable effect, conversion lag and allocation method. Determine actual platform/API release, market/jurisdiction, consent and business decision owner before execution.

## Specialist procedure
1. Freeze hypothesis, primary outcome, guardrail and statistical decision rule before exposure.
2. Choose a platform-supported split, user holdout or geographical design; document whether delivery optimization breaks balanced assignment.
3. Ensure variants share comparable audience, offer and landing conditions and that creative claims are reviewed.
4. Check sample-ratio mismatch, crossover, sequential peeking, unequal budget delivery and conversion delay before inference.
5. Report effects with uncertainty, not a winner from early CTR or attributed conversion counts.

## Operational failure and recovery
- Failure: Algorithmic delivery shifts audience composition, making apparent creative lift confounded.
- Containment: stop or quarantine the affected campaign, audience, conversion uploads or spend pathway as appropriate; identify the authorised incident owner.
- Recovery: fix the source issue, replay/reconcile against a frozen ledger or sample, verify that late events or previous recipients are not double-counted, then resume by approved staged release.
- Do not modify remote platforms, send messages, spend budget, export personal data, or claim account access without explicit authorization.

## Independent falsification
- Negative/adversarial case: Variant B receives only high-intent users; reject the causal comparison.
- Independent acceptance oracle: Assignment integrity and predeclared experiment outcomes pass independent checks before scaling the winner.
- Record actual observed evidence, test environment, sample coverage, expected outcome and uncertainty; a proposed test is not an executed test.

## Official source starting points
- https://support.google.com/google-ads/answer/12003020
Check the exact published/current version, effective date, API eligibility and local rules at execution; source URLs are not operational certification.

## Output contract
Produce a scoped artifact, decision criteria, evidence/source ledger, assumptions, failure thresholds, test cases, owner, rollback trigger and unresolved risks. Separate observed facts, hypotheses and recommendations. Do not fabricate audience sizes, conversion rates, ROAS or impact estimates.

## Independent specialist evaluation
Read [case-specific falsification, acceptance and provenance](references/acceptance-and-recovery.md) on demand for production-impacting work. Passing static registry checks does not prove correctness or authorize any action.
