---
name: marketing-audience-research-evidence
description: "Use for separate observed customer evidence from invented personas and biased convenience samples. Activate only when the task concerns brand and audience research; exclude unrelated SEO, general data engineering and generic product experiments."
metadata:
  version: "1.0.0"
---

# marketing-audience-research-evidence

## Activation boundary
Separate observed customer evidence from invented personas and biased convenience samples. Do not assume provider features, law, account eligibility, real campaign performance, or tool permissions.

## Required inputs
Business question, population frame, research method, sample design, consent, response rates and relevant segmentation fields. Determine actual platform/API release, market/jurisdiction, consent and business decision owner before execution.

## Specialist procedure
1. Specify population, decision, sampling frame, collection period and limitations before choosing interview or survey methods.
2. Separate behavioural segment evidence from sensitive-proxy targeting and prohibited audience inference.
3. Assess coverage, nonresponse, self-selection, weighting and duplicate respondents with an appropriate uncertainty description.
4. Triangulate qualitative claims with observable product/customer evidence; clearly label inferred personas as hypotheses.
5. Provide falsifiable segment hypotheses and an additional sample or experiment needed before media investment.

## Operational failure and recovery
- Failure: Self-selected survey participants are presented as representative of the full market.
- Containment: stop or quarantine the affected campaign, audience, conversion uploads or spend pathway as appropriate; identify the authorised incident owner.
- Recovery: fix the source issue, replay/reconcile against a frozen ledger or sample, verify that late events or previous recipients are not double-counted, then resume by approved staged release.
- Do not modify remote platforms, send messages, spend budget, export personal data, or claim account access without explicit authorization.

## Independent falsification
- Negative/adversarial case: Only engaged newsletter subscribers respond; withhold national market-size claims.
- Independent acceptance oracle: Segment statements trace to observed denominators, sampling method, uncertainty and permitted processing.
- Record actual observed evidence, test environment, sample coverage, expected outcome and uncertainty; a proposed test is not an executed test.

## Official source starting points
- https://aapor.org/standards-and-ethics/best-practices/
Check the exact published/current version, effective date, API eligibility and local rules at execution; source URLs are not operational certification.

## Output contract
Produce a scoped artifact, decision criteria, evidence/source ledger, assumptions, failure thresholds, test cases, owner, rollback trigger and unresolved risks. Separate observed facts, hypotheses and recommendations. Do not fabricate audience sizes, conversion rates, ROAS or impact estimates.

## Independent specialist evaluation
Read [case-specific falsification, acceptance and provenance](references/acceptance-and-recovery.md) on demand for production-impacting work. Passing static registry checks does not prove correctness or authorize any action.
