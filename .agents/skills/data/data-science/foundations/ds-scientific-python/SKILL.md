---
name: ds-scientific-python
description: Use when building reliable numerical and scientific-computing workflows with NumPy, SciPy, pandas, sparse arrays, and reproducible random simulation.
metadata:
  version: "1.1.1"
---

# ds-scientific-python

## Activation boundary

Use for numerical computation, scientific Python foundations, numerical stability, array performance and scientific reproducibility. Do not use for domain-specific statistical design when a more specific inference or modeling skill applies.

## Required context

Array shapes, units, dtypes, numerical ranges, expected precision, data size, sparsity, hardware and reproducibility requirements.

## Workflow

1. Define mathematical inputs, output shape, units and valid ranges before implementation.
2. Make array dimensions explicit. Check broadcasting, axis semantics, row/column orientation and alignment before relying on implicit NumPy behavior.
3. Choose dtypes deliberately. Inspect integer overflow, float precision, categorical encoding and missing-value representation.
4. Use vectorized operations where they improve clarity, but avoid materializing huge intermediate arrays. Use chunking, sparse matrices or streaming reductions when memory is the constraint.
5. Select stable numerical formulations: log-sum-exp for probabilities, stable variance algorithms, solve linear systems instead of explicit matrix inversion, and scale ill-conditioned problems.
6. Use SciPy algorithms with explicit tolerances, convergence criteria and method choices. Inspect warnings and optimizer/sparse-solver status.
7. Use numpy.random.Generator with an explicit seed policy. Separate random streams for independent components and record generator/seed metadata.
8. Benchmark with representative data and profile memory before optimizing. Compare numerical outputs against a trusted small reference implementation.
9. Package the workflow with pinned dependencies, deterministic input fixtures and unit tests for edge cases.

## Failure modes and abstention

- Do not compare floating-point values with exact equality unless the operation guarantees it.
- Do not use a global random seed as a substitute for reproducible random-stream design.
- Do not replace a numerically unstable method with a faster approximation without quantifying error.
- If precision, conditioning or error bounds are material and unknown, report the limitation.

## Validation checklist

- [ ] Shapes, units, dtypes and numeric ranges are checked.
- [ ] Numerical stability and conditioning are assessed.
- [ ] Memory and runtime are measured on representative inputs.
- [ ] Randomness is reproducible and documented.
- [ ] Results are compared with a small trusted reference.

## Authoritative references

- https://numpy.org/doc/stable/
- https://docs.scipy.org/doc/scipy/reference/

## Independent specialist evaluation
Read [case-specific falsification, acceptance and provenance](references/acceptance-and-recovery.md) on demand for production-impacting or high-stakes work. Unexecuted tests and unsupported claims remain unverified; this reference cannot authorize actions.
