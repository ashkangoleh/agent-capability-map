# ds-sequential-experimentation: specialist evaluation and negative controls

Domain `data/data-science/experimentation`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Decide whether the design is fixed-horizon or sequential before launch. Specify the monitoring cadence, maximum sample/duration and stopping rules.
2. Select a valid sequential procedure: group-sequential alpha spending, always-valid p-values/confidence sequences, mixture sequential probability ratio tests or another method with documented guarantees.
3. Distinguish interim monitoring from adaptive treatment assignment. Adaptive allocation changes the data-generating design and requires design-specific inference.
4. Predeclare efficacy, futility and safety boundaries. Define whether stopping can occur for primary outcomes, guardrails or operational failures.

## Challenge / acceptance
- **Challenge:** Shift sampling frame, intervention timing or held-out cohort. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Evaluate uncertainty intervals, leakage diagnostics and falsifiable baselines. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - Do not repeatedly inspect ordinary fixed-horizon p-values and stop when one crosses a threshold.
- Do not treat a Bayesian posterior probability as automatically equivalent to frequentist sequential error control.
- Do not change stopping boundaries after seeing outcomes.
- **Stop/review:** No accuracy or causal claim based on a dashboard or pipeline-success status alone. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://pubsonline.informs.org/doi/abs/10.1287/opre.2021.2135
- https://arxiv.org/abs/1512.04922
- https://www.statsig.com/perspectives/ab-testing-statistics
- https://online.stat.psu.edu/stat509/Lesson10

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
