# public-health-evidence-review: specialist evaluation and negative controls

Domain `health/core`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Frame population, exposure/intervention, comparison and measurable outcomes before collecting studies.
2. Prioritize WHO, national public-health authorities, systematic reviews and primary research when appropriate.
3. Record study design, sample, bias risk, confounding, limitations, certainty and applicability to target population.
4. Keep association, causality, effect size, confidence interval and absolute/relative risk distinct.

## Challenge / acceptance
- **Challenge:** Change guideline version or patient-specific contraindication in a clinical scenario. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Evidence provenance, clinically meaningful exclusions and safety escalation are explicit. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** Unknown evidence remains UNKNOWN.
- **Stop/review:** No diagnosis, treatment, or medical-device certification without qualified review. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://www.who.int/publications/i/item/9789240029200
- https://www.who.int/health-topics

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
