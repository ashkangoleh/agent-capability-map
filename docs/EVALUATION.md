# Routing and Skill Evaluation

A large skill count is not a quality metric. Evaluate whether the right skill is selected, irrelevant context is avoided, and the final work is correct and grounded.

## Required test sets

For every skill, maintain positive prompts, negative prompts, near-miss prompts that share keywords but require another skill, ambiguous prompts where the correct behavior is to ask or abstain, and cross-domain prompts where composition is justified or rejected.

The authoritative labeled set is tests/fixtures/yaml-routing-cases.yaml (the original JSON set is archived for historical comparison). It is a deterministic-router fixture set, not proof of model routing accuracy. Run it against each target agent client and record the actual selected domain, skill, loaded files, and token usage.

## Metrics

- Top-1 routing accuracy: correct primary skill / all labeled prompts.
- Top-2 recall: whether the needed skill appears in the first two candidates.
- False activation rate: unrelated skill loaded / prompts.
- Abstention precision: correct abstentions / all abstentions.
- Evidence coverage: externally factual claims with support / externally factual claims.
- Unsupported claim rate: material factual claims without adequate evidence / material factual claims.
- Context cost: tokens loaded for root policy, domain router, registry, skill, and references.
- Task success: human-reviewed correctness against an explicit rubric.
- Regression rate: previously passing prompts that fail after a change.

Do not report a metric without a defined denominator, labeled test set, and evaluation date.

## Initial acceptance gates

These are targets, not measured results:
- 100% of active skill paths and metadata pass structural validation.
- No active skill has an empty or generic description.
- Every skill has positive and negative routing examples.
- No routine prompt loads more than two skills.
- No unselected domain reference is loaded.
- High-impact factual recommendations identify evidence and uncertainty.
- Routing changes run against positive, negative, and near-miss fixtures before merge.

Set numeric quality targets only after a baseline run. Do not claim hallucination reduction until a controlled evaluation demonstrates it.
