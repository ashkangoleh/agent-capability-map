# infrastructure-asset-configuration-inventory: specialist evaluation and negative controls

Domain `infrastructure/architecture/asset-inventory`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Define asset taxonomy and minimum fields: stable ID, owner, environment, location, lifecycle, criticality and dependencies.
2. Choose authoritative sources per attribute and precedence for conflicts.
3. Automate discovery from cloud APIs, Redfish, network telemetry and orchestration; retain provenance and last-seen.
4. Reconcile observed/declared state and classify drift; approve destructive remediation.

## Challenge / acceptance
- **Challenge:** Lose a node, permission or control plane while applying a scoped change. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Actual target identity, SLO, rollback prerequisites and failure isolation are independently checked. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - Recycled IDs corrupt graphs; use stable identifiers and lifecycle states.
- Discovery lag creates false confidence; publish freshness and coverage SLOs.
- Auto-reconciliation can overwrite emergency changes; separate observe from enforce.
- **Stop/review:** No destructive, credential or production control-plane changes without authorization. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://docs.netbox.dev/
- https://www.servicenow.com/products/it-service-management/what-is-a-cmdb.html
- https://www.iso.org/standard/65694.html

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
