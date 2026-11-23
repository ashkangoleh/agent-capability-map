# ds-classical-nlp: specialist evaluation and negative controls

Domain `data/data-science/text-analytics`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Define the text unit, target label, language distribution, annotation source and intended decision. Audit duplicates, near-duplicates and label disagreement.
2. Split by user, document family, source or time before fitting tokenizers or vocabulary. Prevent author, template and near-duplicate leakage.
3. Normalize conservatively. Preserve negation, numbers, punctuation, named entities and script distinctions when they carry signal. Keep raw text and transformation provenance.
4. Compare word n-gram and character n-gram TF-IDF baselines with simple linear classifiers before more complex models. Fit vectorizers inside the training pipeline.

## Challenge / acceptance
- **Challenge:** Shift sampling frame, intervention timing or held-out cohort. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Evaluate uncertainty intervals, leakage diagnostics and falsifiable baselines. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - Do not use random row splits when the same user, source or template appears across splits.
- Do not translate test data into a dominant language and claim native-language quality.
- Do not use accuracy alone for imbalanced labels.
- **Stop/review:** No accuracy or causal claim based on a dashboard or pipeline-success status alone. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://scikit-learn.org/stable/tutorial/text_analytics/
- https://spacy.io/usage/models

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
