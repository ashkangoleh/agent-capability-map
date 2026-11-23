---
name: ds-operations-research
description: "Formulate constrained optimization with explicit objectives, feasibility and sensitivity analysis."
metadata:
  version: "1.0.1"
---

# ds-operations-research

## Activation boundary
Formulate constrained optimization with explicit objectives, feasibility and sensitivity analysis.

## Required context
Decision variables, objective, constraints, units, integrality and solver limits.

## Analysis procedure
1. Define decision variables, objective, constraints, units and feasibility.
2. Choose LP, integer, nonlinear or heuristic solver from mathematical structure.
3. Validate solver status, feasibility, optimality gap and termination.
4. Run sensitivity analysis on costs, capacities and uncertain inputs.
5. Translate solutions into implementable actions.

## Failure modes and safeguards
- Do not infer causality from predictive association or treat a p-value as effect size.
- Protect temporal/group boundaries, label availability, sampling design and multiplicity assumptions.
- Report uncertainty, sensitivity, calibration and population limitations; do not fabricate performance.

## Validation
- Reproduce from a clean environment and immutable data/split definitions.
- Test leakage, missingness, subgroup stability, sensitivity and generalization.
- Record library versions, seeds, assumptions, metrics and limitations.

## Official reference
- https://developers.google.com/optimization

## Output contract
Return the analysis/modeling result with estimand, assumptions, validation design, uncertainty, reproducibility and decision implications. Separate observed evidence from inference.

## Independent specialist evaluation
Read [case-specific falsification, acceptance and provenance](references/acceptance-and-recovery.md) on demand for production-impacting or high-stakes work. Unexecuted tests and unsupported claims remain unverified; this reference cannot authorize actions.
