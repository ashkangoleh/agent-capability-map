# ds-scientific-python: specialist evaluation and negative controls

Domain `data/data-science/foundations`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Define mathematical inputs, output shape, units and valid ranges before implementation.
2. Make array dimensions explicit. Check broadcasting, axis semantics, row/column orientation and alignment before relying on implicit NumPy behavior.
3. Choose dtypes deliberately. Inspect integer overflow, float precision, categorical encoding and missing-value representation.
4. Use vectorized operations where they improve clarity, but avoid materializing huge intermediate arrays. Use chunking, sparse matrices or streaming reductions when memory is the constraint.

## Challenge / acceptance
- **Challenge:** Shift sampling frame, intervention timing or held-out cohort. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Evaluate uncertainty intervals, leakage diagnostics and falsifiable baselines. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - Do not compare floating-point values with exact equality unless the operation guarantees it.
- Do not use a global random seed as a substitute for reproducible random-stream design.
- Do not replace a numerically unstable method with a faster approximation without quantifying error.
- **Stop/review:** No accuracy or causal claim based on a dashboard or pipeline-success status alone. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://numpy.org/doc/stable/
- https://docs.scipy.org/doc/scipy/reference/

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
