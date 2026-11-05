# infrastructure-capacity-performance: specialist evaluation and negative controls

Domain `infrastructure/observability/profiling`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Build workload models from measured arrival rates, concurrency, payload and seasonality.
2. Find bottlenecks across CPU, memory, disk, network, pools, quotas and scheduler queues.
3. Calculate normal and failure-mode headroom including AZ loss, maintenance and rebuild traffic.
4. Run controlled load tests with production-like dependencies and explicit abort thresholds.

## Challenge / acceptance
- **Challenge:** Generate false positive and silent failure in instrumentation. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Burn rates and actionable alerts agree with user-impact SLOs. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - Average utilization hides tail saturation; use p95/p99 and queue age.
- Autoscaling can amplify downstream overload; cap scale rates and concurrency.
- Quotas can block scale-out despite available budget.
- **Stop/review:** No destructive, credential or production control-plane changes without authorization. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://sre.google/sre-book/handling-overload/
- https://sre.google/workbook/alerting-on-slos/
- https://sre.google/sre-book/service-level-objectives/

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
