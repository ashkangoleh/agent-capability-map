# openlineage-metadata-instrumentation: specialist evaluation and negative controls

Domain `data/governance/lineage`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Define stable namespace/job/dataset identifiers and their ownership; avoid inferring lineage from similarly named tables.
2. Verify installed OpenLineage integration/version and applicable event schema before adding facets.
3. Capture run START/COMPLETE/FAIL and input/output datasets at the correct execution boundary; distinguish declared lineage from observed successful writes.
4. Use standard facets where supported and prefix custom facets to avoid collisions; redact secrets and sensitive fields.

## Challenge / acceptance
- **Challenge:** Revoke sensitive dataset access and mutate lineage metadata. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Policy propagation and provenance are independently auditable. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - Verify event UUID/run IDs, schema validity and facet compatibility.
- Measure emission failure rate, input/output coverage and link accuracy against traces.
- Do not assert a test, benchmark, compatibility or rollout succeeded without actual tool evidence.
- **Stop/review:** No accuracy or causal claim based on a dashboard or pipeline-success status alone. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://openlineage.io/docs/spec/facets/
- https://openlineage.io/

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
