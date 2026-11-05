---
name: ds-optuna-search
description: Use when designing reproducible hyperparameter optimization studies with Optuna, pruning, constraints, or multi-objective trade-offs.
metadata:
  version: "1.1.1"
---

# ds-optuna-search

## Activation boundary

Use for controlled hyperparameter and model-selection experiments. It does not replace a leakage-safe validation design or justify tuning against the final test set.

## Required context

Prediction target, split strategy, metric, compute budget, search space, constraints, reproducibility requirements and deployment objective.

## Workflow

1. Freeze the data split and metric before search. Use nested cross-validation or a separate final holdout when model selection itself is part of the evaluation.
2. Define a search space from model semantics and plausible scales. Prefer log distributions for scale parameters and conditional branches for incompatible model families.
3. Build an objective that fits preprocessing inside each training fold and returns a metric aggregated across the correct validation folds.
4. Select a sampler based on the search structure and budget. Use random search as a baseline; use TPE or another adaptive sampler only when its added complexity is justified.
5. Add pruning only when intermediate metrics are comparable across trials and early stopping does not systematically favor fast-learning configurations.
6. Persist studies to a durable storage backend for resume and collaboration. Set study direction, sampler seed, trial identity and artifact retention explicitly.
7. For constrained or multi-objective problems, preserve the Pareto frontier and report trade-offs rather than collapsing all objectives into an undocumented weighted score.
8. Inspect parameter importance cautiously, verify top configurations across additional seeds/folds and compare with a simple baseline.
9. Refit only after selection is frozen; evaluate the untouched test set once and store the study, environment, split IDs and model artifact.

## Failure modes and abstention

- Do not tune repeatedly against the same holdout.
- Do not parallelize with uncontrolled shared random state and then claim bitwise reproducibility.
- Do not compare trials that used different data, feature availability or evaluation rules.
- If the search budget is too small to distinguish candidates, report uncertainty and prefer the simpler baseline.

## Validation checklist

- [ ] Search does not leak validation/test information into preprocessing.
- [ ] Objective and constraints are deterministic or their stochasticity is measured.
- [ ] Pruning does not bias comparisons.
- [ ] Study storage and resume behavior are verified.
- [ ] Final evaluation uses untouched data.

## Authoritative reference

- https://optuna.readthedocs.io/en/stable/

## Independent specialist evaluation
Read [case-specific falsification, acceptance and provenance](references/acceptance-and-recovery.md) on demand for production-impacting or high-stakes work. Unexecuted tests and unsupported claims remain unverified; this reference cannot authorize actions.
