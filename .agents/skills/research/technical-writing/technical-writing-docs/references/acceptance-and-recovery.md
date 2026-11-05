# technical-writing-docs: specialist evaluation and negative controls

Domain `research/technical-writing`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Choose the document type: guide, reference, tutorial, explanation, runbook, RFC, ADR, or report.
2. Inspect actual implementation, configuration, API schema, and authoritative references.
3. Define prerequisites, scope, non-goals, and terminology.
4. Organize around the reader's task or decision, not the author's chronology.

## Challenge / acceptance
- **Challenge:** Alter sampling assumptions or introduce contradictory primary evidence. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Methods, uncertainty, independent replication and provenance are disclosed. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** Unknown evidence remains UNKNOWN.
- **Stop/review:** No fabricated citations, research result or significance claim. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

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
