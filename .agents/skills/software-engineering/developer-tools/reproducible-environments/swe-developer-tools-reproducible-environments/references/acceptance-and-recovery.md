# swe-developer-tools-reproducible-environments: specialist evaluation and negative controls

Domain `software-engineering/developer-tools/reproducible-environments`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Establish the current behavior, failure impact, caller/consumer boundaries and measurable acceptance criteria in the actual codebase.
2. Capture versioned evidence: Lockfiles, runtime images, platform/architecture, secrets sourcing and build cache. Identify missing data and the smallest falsifiable diagnosis or design hypothesis.
3. Plan the narrowest change compatible with current contracts, dependency graph and deployment constraints. Evaluate one simpler alternative and its operational cost.
4. Implement or specify the corrective mechanism: Make toolchains and dependency resolution deterministic and secure. Handle negative paths, timeouts, authorization, concurrency and resource limits where applicable.

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
- https://www.computer.org/education/bodies-of-knowledge/software-engineering/topics

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
