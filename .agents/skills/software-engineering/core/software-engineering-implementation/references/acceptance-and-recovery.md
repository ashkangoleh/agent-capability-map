# software-engineering-implementation: specialist evaluation and negative controls

Domain `software-engineering/core`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Inspect relevant files before proposing changes. Do not assume repository structure or framework version.
2. Trace current behavior and identify the smallest correct change.
3. Define the contract: inputs, outputs, errors, side effects, compatibility, and acceptance criteria.
4. Check security, authorization, validation, concurrency, resource limits, and failure behavior.

## Challenge / acceptance
- **Challenge:** Inject timeout, concurrency, dependency or schema break in a representative test. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Functional, security and operational regressions are tested in pinned build with rollback plan. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** Unknown evidence remains UNKNOWN.
- **Stop/review:** No claims of build, deployment or performance success without execution evidence. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- No primary URL in source SKILL.md; verify authoritative sources before any version-sensitive claim.

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
