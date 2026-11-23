---
name: marketing-incrementality-geo-lift
description: "Use for estimate incremental marketing impact with explicit identification assumptions and uncertainty. Activate only when the task concerns marketing analytics; exclude unrelated SEO, general data engineering and generic product experiments."
metadata:
  version: "1.0.0"
---

# marketing-incrementality-geo-lift

## Activation boundary
Estimate incremental marketing impact with explicit identification assumptions and uncertainty. Do not assume provider features, law, account eligibility, real campaign performance, or tool permissions.

## Required inputs
Treatment and comparison units, geography/time windows, spend changes, holdout eligibility, conversion lag, baseline variance, seasonality and interference. Determine actual platform/API release, market/jurisdiction, consent and business decision owner before execution.

## Specialist procedure
1. Define the counterfactual and estimand before using attribution, geo lift, conversion lift or marketing-mix modelling.
2. Select randomized holdout where possible; otherwise assess parallel trends, spillover, contamination and seasonality.
3. Power the experiment or state its expected imprecision and predefine unit, primary outcome and exclusions.
4. For MMM, document temporal aggregation, spend collinearity, controls, priors, validation and any experimental calibration.
5. Report absolute incremental outcomes, intervals, cost per incremental outcome and sensitivity to identification choices.

## Operational failure and recovery
- Failure: A last-click channel's attributed conversions are presented as incremental new revenue.
- Containment: stop or quarantine the affected campaign, audience, conversion uploads or spend pathway as appropriate; identify the authorised incident owner.
- Recovery: fix the source issue, replay/reconcile against a frozen ledger or sample, verify that late events or previous recipients are not double-counted, then resume by approved staged release.
- Do not modify remote platforms, send messages, spend budget, export personal data, or claim account access without explicit authorization.

## Independent falsification
- Negative/adversarial case: Geo tests have cross-border media spillover and no reliable control; refuse causal lift claim.
- Independent acceptance oracle: An independent evaluator reproduces treatment/control assignment, estimand, uncertainty and diagnostic failures.
- Record actual observed evidence, test environment, sample coverage, expected outcome and uncertainty; a proposed test is not an executed test.

## Official source starting points
- https://support.google.com/google-ads/answer/12003020
- https://developers.google.com/meridian/docs/advanced-modeling/roi-priors-and-calibration
Check the exact published/current version, effective date, API eligibility and local rules at execution; source URLs are not operational certification.

## Output contract
Produce a scoped artifact, decision criteria, evidence/source ledger, assumptions, failure thresholds, test cases, owner, rollback trigger and unresolved risks. Separate observed facts, hypotheses and recommendations. Do not fabricate audience sizes, conversion rates, ROAS or impact estimates.

## Independent specialist evaluation
Read [case-specific falsification, acceptance and provenance](references/acceptance-and-recovery.md) on demand for production-impacting work. Passing static registry checks does not prove correctness or authorize any action.
