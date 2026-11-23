# security-threat-model-review: specialist evaluation and negative controls

Domain `security/core`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Inspect real architecture and data-flow artifacts; list unknown trust boundaries instead of assuming a conventional stack.
2. Identify assets, entry points, identities, sensitive data paths, external dependencies and privilege transitions. Draw a minimal DFD only when it adds clarity.
3. Apply appropriate threat prompts (for example STRIDE) to each boundary and misuse case; map threats to real attacker capabilities rather than theoretical slogans.
4. Rank risks using explicit impact, preconditions, likelihood evidence and affected users; never claim a numerical risk probability without data.

## Challenge / acceptance
- **Challenge:** Inject privilege escalation, invalid identity or hostile untrusted input. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Attack paths, prevention, detection and residual-risk owner are explicitly validated. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** Unknown evidence remains UNKNOWN.
- **Stop/review:** No offensive access, bypass or false security certification. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html
- https://www.nist.gov/cyberframework

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
