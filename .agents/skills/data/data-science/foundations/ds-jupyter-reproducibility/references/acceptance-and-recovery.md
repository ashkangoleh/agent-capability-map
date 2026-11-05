# ds-jupyter-reproducibility: specialist evaluation and negative controls

Domain `data/data-science/foundations`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Restart the kernel and run all cells in order. Record failures caused by hidden state, execution order or stale variables.
2. Remove machine-specific paths, embedded credentials, personal data and undeclared local dependencies.
3. Pin the environment and document system-level dependencies. Use a lockfile or reproducible environment definition.
4. Parameterize dates, input paths and experiment settings rather than editing cells manually between runs.

## Challenge / acceptance
- **Challenge:** Shift sampling frame, intervention timing or held-out cohort. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Evaluate uncertainty intervals, leakage diagnostics and falsifiable baselines. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - Do not commit tokens, customer records or private extracts in notebook metadata or outputs.
- Do not rely on widgets, environment variables or mounted drives without documenting them.
- Do not silently suppress execution errors or stale output.
- **Stop/review:** No accuracy or causal claim based on a dashboard or pipeline-success status alone. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://docs.jupyter.org/en/latest/

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
