# datahub-metadata-catalog-governance: specialist evaluation and negative controls

Domain `data/governance/catalog`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Define dataset identities and owners from authoritative source metadata rather than inferred naming.
2. Configure connector ingestion with scoped permissions, schedules, profiling limits and sensitive-field redaction.
3. Distinguish discovered datasets from live/healthy datasets and manual vs emitted lineage edges.
4. Validate schema versions, glossary terms, policies and data-product boundaries against actual consumers.

## Challenge / acceptance
- **Challenge:** Revoke sensitive dataset access and mutate lineage metadata. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Policy propagation and provenance are independently auditable. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** Unknown evidence remains UNKNOWN.
- **Stop/review:** No accuracy or causal claim based on a dashboard or pipeline-success status alone. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://docs.datahub.com/docs/
- https://openlineage.io/

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
