# ecommerce-product-catalog-audit: specialist evaluation and negative controls

Domain `ecommerce/core`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Define product/SPU/SKU identity, parent-variant relationships and stable keys; never merge distinct variants using titles.
2. Reconcile required listing fields, identifiers, category, stock, price, currency, shipping and returns against current channel specifications.
3. Detect missing attributes, inconsistent variants, duplicate identifiers, stale availability and invalid reference URLs.
4. Distinguish product feed quality from search ranking and conversion rate; avoid guaranteed channel acceptance.

## Challenge / acceptance
- **Challenge:** Fail an order or inventory transition after partial external side effects. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** State transitions reconcile, payments/refunds are idempotent and customer impact measured. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** Unknown evidence remains UNKNOWN.
- **Stop/review:** No unsafe payment mutation or unverified conversion lift. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://developers.google.com/search/docs/appearance/structured-data/product
- https://support.google.com/merchants/

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
