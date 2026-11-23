---
name: ds-monte-carlo
description: "Quantify uncertainty with Monte Carlo simulation, convergence checks and scenario analysis."
metadata:
  version: "1.0.1"
---

# ds-monte-carlo

## Activation boundary
Quantify uncertainty with Monte Carlo simulation, convergence checks and scenario analysis.

## Required context
Input distributions, dependence, seeds, tail risk, draw count and decision threshold.

## Analysis procedure
1. Specify model assumptions, input distributions, dependence and decision outputs.
2. Choose random generators, seed policy and draw count for target precision.
3. Use variance reduction only when justified.
4. Check convergence, tail behavior and sensitivity to inputs.
5. Report uncertainty intervals, not false precision.

## Failure modes and safeguards
- Do not infer causality from predictive association or treat a p-value as effect size.
- Protect temporal/group boundaries, label availability, sampling design and multiplicity assumptions.
- Report uncertainty, sensitivity, calibration and population limitations; do not fabricate performance.

## Validation
- Reproduce from a clean environment and immutable data/split definitions.
- Test leakage, missingness, subgroup stability, sensitivity and generalization.
- Record library versions, seeds, assumptions, metrics and limitations.

## Official reference
- https://docs.scipy.org/doc/scipy/reference/stats.qmc.html

## Output contract
Return the analysis/modeling result with estimand, assumptions, validation design, uncertainty, reproducibility and decision implications. Separate observed evidence from inference.

## Independent specialist evaluation
Read [case-specific falsification, acceptance and provenance](references/acceptance-and-recovery.md) on demand for production-impacting or high-stakes work. Unexecuted tests and unsupported claims remain unverified; this reference cannot authorize actions.
