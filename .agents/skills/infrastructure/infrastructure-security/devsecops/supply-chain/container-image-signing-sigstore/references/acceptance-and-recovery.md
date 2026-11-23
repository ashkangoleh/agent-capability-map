# container-image-signing-sigstore: specialist evaluation and negative controls

Domain `infrastructure/infrastructure-security/devsecops/supply-chain`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Map threats, trust boundaries, assets and required security gates before selecting scanners.
2. Integrate SAST/DAST/SCA, secrets, IaC, image, SBOM and provenance checks with severity policy.
3. Use policy-as-code in audit mode before enforce; define narrow exceptions and expiry.
4. Verify identity, signing, attestation and admission at deployment time.

## Challenge / acceptance
- **Challenge:** Inject compromised dependency, stale token and policy bypass. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Prevent unauthorized actions, preserve audit trail and verify remediation. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
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
- https://docs.sigstore.dev/

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
