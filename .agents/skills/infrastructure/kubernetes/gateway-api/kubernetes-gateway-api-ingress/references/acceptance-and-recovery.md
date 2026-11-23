# kubernetes-gateway-api-ingress: specialist evaluation and negative controls

Domain `infrastructure/kubernetes/gateway-api`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Identify installed API versions, CRDs and controller support; conformance does not guarantee every feature.
2. Model GatewayClass, Gateway, listeners, route attachment, hostname, TLS and backend policy.
3. Define DNS/certificate automation, cross-namespace grants, WAF, rate limits and source IP behavior.
4. Migrate from Ingress in parallel with canary traffic and rollback independent of application release.

## Challenge / acceptance
- **Challenge:** Inject unavailable node, admission denial and stale rollout. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Workload health and availability remain within verified SLO; rollback tested. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - CRD/controller mismatch can accept YAML but fail reconciliation.
- Cross-namespace references can be denied or over-granted.
- DNS/certificate propagation lags route deployment.
- **Stop/review:** No destructive, credential or production control-plane changes without authorization. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://gateway-api.sigs.k8s.io/
- https://kubernetes.io/docs/concepts/services-networking/ingress/
- https://kubernetes.io/docs/concepts/services-networking/gateway/

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
