# cloud-serverless-managed-runtime: specialist evaluation and negative controls

Domain `infrastructure/cloud/serverless`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Choose FaaS, managed containers or serverless Kubernetes based on duration, startup, networking and state.
2. Define at-least-once duplicate behavior, ordering scope, idempotency keys, retry budgets, DLQ and replay.
3. Set concurrency, timeout, memory/CPU, pools and backpressure to protect downstream dependencies.
4. Use workload identity, short-lived credentials, private networking and controlled egress.

## Challenge / acceptance
- **Challenge:** Remove a role or overload one region. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** No overbroad privilege, budget overrun or hidden cross-region dependence. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - Retries multiply side effects; require idempotent handlers.
- Concurrency spikes can exhaust databases; cap concurrency and protect dependencies.
- Ephemeral execution invalidates local-state assumptions; externalize durable state.
- **Stop/review:** No destructive, credential or production control-plane changes without authorization. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://docs.aws.amazon.com/lambda/latest/dg/welcome.html
- https://cloud.google.com/run/docs
- https://learn.microsoft.com/azure/azure-functions/

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
