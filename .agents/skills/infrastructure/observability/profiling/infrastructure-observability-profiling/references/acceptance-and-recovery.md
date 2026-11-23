# infrastructure-observability-profiling: specialist evaluation and negative controls

Domain `infrastructure/observability/profiling`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Define operational questions and SLOs; map each signal to owner, source, retention and action.
2. Standardize resource attributes and correlation without unbounded identifiers.
3. Set cardinality budgets, trace sampling, log filtering, profile aggregation and retention tiers.
4. Use eBPF/profilers only where needed; validate overhead, permissions and kernel compatibility.

## Challenge / acceptance
- **Challenge:** Generate false positive and silent failure in instrumentation. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Burn rates and actionable alerts agree with user-impact SLOs. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - High-cardinality labels exhaust TSDB memory and cost.
- Sampling can remove rare failures; preserve error/latency evidence.
- Agents can add overhead or require privilege.
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
- https://grafana.com/docs/

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
