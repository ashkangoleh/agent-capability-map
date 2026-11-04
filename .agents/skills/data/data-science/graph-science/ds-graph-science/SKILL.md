---
name: ds-graph-science
description: "Analyze graph structure, centrality, communities and network effects without inferring causality."
metadata:
  version: "1.0.0"
---

# ds-graph-science

## Activation boundary
Analyze graph structure, centrality, communities and network effects without inferring causality.

## Required context
Node/edge grain, direction, weights, time, sampling and graph size.

## Analysis procedure
1. Define node/edge identity, direction, weight, time and sampling.
2. Choose algorithms based on graph size and topology assumptions.
3. Check disconnected components, hubs, sampling bias and temporal leakage.
4. Validate community/centrality stability under perturbation.
5. Separate structural association from causal influence.

## Failure modes and safeguards
- Do not infer causality from predictive association or treat a p-value as effect size.
- Protect temporal/group boundaries, label availability, sampling design and multiplicity assumptions.
- Report uncertainty, sensitivity, calibration and population limitations; do not fabricate performance.

## Validation
- Reproduce from a clean environment and immutable data/split definitions.
- Test leakage, missingness, subgroup stability, sensitivity and generalization.
- Record library versions, seeds, assumptions, metrics and limitations.

## Official reference
- https://networkx.org/documentation/stable/

## Output contract
Return the analysis/modeling result with estimand, assumptions, validation design, uncertainty, reproducibility and decision implications. Separate observed evidence from inference.
