---
name: business-decision-rules-dmn
description: "Use for business operations dmn 1.6 decision table overlap hit policy; evidence-grounded business decision and operations review, with assumptions, guardrails, unit consistency, failure behavior and a reviewer-approved recovery path. Not for personal financial advice."
metadata:
  version: "1.0.0"
---

# business-decision-rules-dmn

## Activation boundary
Specialist scope: business operations dmn 1.6 decision table overlap hit policy. Business & Operations owns business decision framing and accountable process design. Do not substitute for accounting signoff, legal review, Data Engineering pipeline implementation, or Marketing paid media operations.

## Required inputs and authority
Collect scope, date range, region, owner, approved baseline, units, data quality, cost and service constraints, evidence and required permission. Never invent supplier contracts, financial statement classifications or operating measurements.

## Specialist procedure
1. Write business decision inputs, owner, eligibility and explicit domain of values.
2. Model decision table hit policies and conflicting/overlapping rows in formal DMN 1.6.
3. Test boundary inputs, blank values, conflicting matches and policy precedence.
4. Reject DMN 1.7 beta artifacts as if already stable in production.

## Operational failure and recovery
- Failure example: Two overlapping rules return different prices under unspecified hit policy.
- Before proposing irreversible change, establish affected process or finance cohort, freeze input assumptions and retain an authorized rollback or correction owner.
- For scenarios, recompute downside with uncertainty and reconcile accounting/economic and operational quantities independently.
- For process actions, verify exceptions, missed approvals, retries, fallback staffing, stakeholder communication and evidence of actual recovery.
- Do not purchase, commit budget, sign contracts, modify supplier accounts or claim regulatory certification.

## Independent falsification
- Negative/near-miss case: Two overlapping rules return different prices under unspecified hit policy.
- Independent acceptance oracle: All test cases map to one documented business outcome or explicit rejection.
- Before testing, define positive, contradictory, ambiguous and missing-evidence cases with measurable stop criteria.
- A static lint, diagram or hypothetical profit estimate is not a real-world pass or causal business result.

## Authoritative source starting points
- https://www.omg.org/spec/DMN/1.6/
- https://www.omg.org/spec/BPMN/2.0.2/
At use, confirm standard edition and publication/effective dates, local accounting policy and source scope. ISO 31000 is guidance and not certifiable. IFRS 18 is effective for annual reporting periods on or after 2027-01-01 unless early adopted. Do not treat a draft standard as mandatory.

## Output contract
Deliver business question, option/status quo, actual evidence, assumptions, formulas and units if relevant, downside cases, owner-approved decision gate, earliest falsification test, recovery and open limitations.

## Independent specialist evaluation
Read [the independent specialist acceptance and recovery plan](references/acceptance-and-recovery.md) when affecting important decisions. It does not itself authorize an action or certify live performance.
