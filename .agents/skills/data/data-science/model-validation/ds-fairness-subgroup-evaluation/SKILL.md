---
name: ds-fairness-subgroup-evaluation
description: Use when measuring statistical performance disparities, calibration, or error trade-offs across protected or operationally important subgroups.
metadata:
  version: "1.0.1"
---

# ds-fairness-subgroup-evaluation

## Activation boundary

Use for quantitative subgroup evaluation of predictive models and decision thresholds. This skill is not a legal compliance determination or a complete responsible-AI governance review.

## Required context

Decision context, affected populations, sensitive/group attributes, target and label provenance, prediction threshold, sample sizes, error costs and applicable policy constraints.

## Workflow

1. Identify the potential harms and affected groups with domain and policy owners. Define intersections and the unit at which harm occurs.
2. Audit group representation, missing sensitive attributes, label quality, selection mechanisms and sample sizes. Do not assume observed labels are unbiased ground truth.
3. Select metrics from the harm model rather than choosing one generic fairness score:
   - selection-rate or demographic-parity differences;
   - true/false-positive rates and equalized-odds gaps;
   - calibration and predictive-value differences;
   - error, abstention and allocation disparities.
4. Compute group and intersectional metrics with uncertainty intervals. Use bootstrap or other valid inference that respects entity/time/cluster dependence.
5. Examine base rates, threshold choice, prevalence, feature availability and measurement error. Explain why metrics can conflict and why no single parity metric establishes fairness.
6. Compare threshold and mitigation alternatives on a documented utility/fairness trade-off. Separate measurement from intervention; do not claim a mitigation is universally optimal.
7. Evaluate temporal stability, small-group uncertainty, intersectional slices and downstream human review/appeal paths.
8. Report unresolved harms, unsupported groups and monitoring requirements. Escalate policy or legal questions to the appropriate owner.

## Failure modes and abstention

- Do not publish unstable metrics for very small groups as precise facts.
- Do not infer absence of bias from one parity metric.
- Do not use sensitive attributes in mitigation or decisioning without authorization and legal/policy review.
- Do not assume demographic parity and equalized odds can always be achieved simultaneously.
- If labels are historically biased or group membership is unreliable, state that the measured disparity is not a complete fairness assessment.

## Validation checklist

- [ ] Harm model and affected groups are explicit.
- [ ] Group sample sizes and label quality are audited.
- [ ] Multiple relevant metrics and uncertainty are reported.
- [ ] Threshold and base-rate effects are explained.
- [ ] Policy/legal review and monitoring owners are identified.

## Authoritative references

- https://fairlearn.org/main/
- https://fairlearn.org/main/user_guide/fairness_in_machine_learning.html

## Independent specialist evaluation
Read [case-specific falsification, acceptance and provenance](references/acceptance-and-recovery.md) on demand for production-impacting or high-stakes work. Unexecuted tests and unsupported claims remain unverified; this reference cannot authorize actions.
