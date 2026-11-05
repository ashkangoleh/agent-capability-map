# observability-stack-logs-traces-metrics: specialist evaluation and negative controls

Domain `infrastructure/observability/stack`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Define user-visible SLIs, SLOs, error budgets and actionable burn-rate windows.
2. Model dependencies, saturation, capacity, failure domains and recovery objectives.
3. Instrument correlated metrics/logs/traces with controlled cardinality, sampling and retention.
4. Run controlled failure or restore exercises with blast-radius and abort criteria.

## Challenge / acceptance
- **Challenge:** Generate false positive and silent failure in instrumentation. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Burn rates and actionable alerts agree with user-impact SLOs. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - Start with read-only evidence collection and confirm the exact environment/cluster/account before mutation.
- Treat credentials, production data, network reachability and state backends as security boundaries.
- Define blast radius, abort criteria, rollback limits and post-change verification before execution.
- **Stop/review:** No destructive, credential or production control-plane changes without authorization. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://opentelemetry.io/docs/
- https://prometheus.io/docs/introduction/overview/

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
