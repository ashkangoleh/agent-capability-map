# aiml-recommender-systems-ranking: specialist evaluation and negative controls

Domain `ai-ml/recommender-systems/ranking`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Capture current model, data, baseline, runtime and deployment contract; define falsifiable acceptance tests and affected consumers.
2. Inspect labeling/split chronology and access provenance; block leakage, untrusted instructions, test-set contamination and unauthorized input.
3. Design the specialist solution around these explicit variables: exposure logging, rank labels and guardrail metrics. Compare a simpler existing baseline before expanding infrastructure.
4. Exercise the risk cases: position bias and clickbait objective. Include shift, missing inputs, outliers, retries, partial artifacts and rollback wherever relevant.

## Challenge / acceptance
- **Challenge:** Remove eligible items and perturb position propensities. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Validate recall@k, propensity support and online/offline ranking guardrails. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** Unknown evidence remains UNKNOWN.
- **Stop/review:** No model-quality or security claim based on a route fixture or demonstration. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://www.nist.gov/itl/ai-risk-management-framework
- https://github.com/GenAI-Security-Project/GenAI-LLM-Top10/tree/main/2026/final
- https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
