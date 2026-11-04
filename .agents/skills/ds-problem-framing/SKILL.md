---
name: ds-problem-framing
description: Use when translating an ambiguous business or scientific question into a measurable data science problem, estimand, prediction target, and evaluation plan.
metadata:
  version: "1.1.0"
---

# ds-problem-framing

## Activation boundary

Use before choosing data, features, statistical tests or ML algorithms when the problem statement is underspecified. Do not start by selecting a model or metric.

## Required context

Decision owner, action available, target population, unit of analysis, decision time, outcome horizon, constraints, costs of errors and available data sources.

## Workflow

1. Rewrite the request as a decision: who will act, what action changes, for whom and when.
2. Classify the question:
   - descriptive: what happened and to whom;
   - diagnostic: which factors are associated with the outcome;
   - predictive: what will happen using information available at a defined time;
   - causal: what would change under an intervention;
   - prescriptive: which feasible action optimizes a stated objective.
3. Define the population, entity grain, inclusion/exclusion rules, treatment or prediction timestamp, outcome window and estimand/target.
4. Specify the unit of analysis and the unit at which decisions, labels and errors occur. Resolve repeated entities, aggregation and exposure windows.
5. Translate business success into measurable primary metrics, guardrails, error costs, latency and operating constraints. Identify unacceptable failure modes.
6. Audit whether data can support the question: coverage, label delay, missingness, selection bias, leakage, representativeness, sample size, permissions and retention.
7. Establish a simple baseline and a decision threshold before proposing complex methods.
8. Choose the smallest valid method family. Route data acquisition and pipelines to Data Engineering, classical statistical/predictive analysis here, and deep learning/LLM deployment to AI/ML when appropriate.
9. Define a validation design that mirrors deployment: temporal/group split, randomized evaluation, quasi-experimental identification or sensitivity analysis.
10. Record assumptions, non-goals, acceptance criteria, decision owner and a stop condition for insufficient evidence.

## Failure modes and abstention

- Do not confuse prediction accuracy with causal impact or business value.
- Do not use an aggregate metric when the decision is made at a different grain.
- Do not define success only after inspecting the final test set.
- If the action, target population or outcome cannot be defined, return a clarification request rather than a model proposal.

## Validation checklist

- [ ] Decision and user/action are explicit.
- [ ] Question type and estimand/target are identified.
- [ ] Unit, population, time and outcome are defined.
- [ ] Baseline, metrics, guardrails and costs are specified.
- [ ] Data feasibility and leakage risks are assessed.
- [ ] Validation design and acceptance criteria are written.

## Output contract

Return a concise problem statement, decision/estimand, data requirements, baseline, evaluation plan, constraints, assumptions, non-goals and open questions.

## Authoritative reference

- https://scikit-learn.org/stable/getting_started.html
