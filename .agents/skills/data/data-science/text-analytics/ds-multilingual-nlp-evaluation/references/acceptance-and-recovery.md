# ds-multilingual-nlp-evaluation: specialist evaluation and negative controls

Domain `data/data-science/text-analytics`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Inventory languages, scripts, dialects, code-switching, transliteration, spelling variation and source-specific text conventions. Do not infer language solely from geography or user profile.
2. Audit annotation quality and label definitions per language. Translate or harmonize label guidelines only after checking semantic equivalence and cultural ambiguity.
3. Build splits that prevent user, author, document-family, translation-pair and temporal leakage. Preserve the deployment language mix for one evaluation view and use balanced language slices for diagnosis.
4. Compare language-appropriate tokenization and normalization. Preserve script distinctions, diacritics, negation, named entities and code-switch boundaries when they affect meaning.

## Challenge / acceptance
- **Challenge:** Shift sampling frame, intervention timing or held-out cohort. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Evaluate uncertainty intervals, leakage diagnostics and falsifiable baselines. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - Do not report only micro-averaged performance when language representation is imbalanced.
- Do not assume a translated test set represents native-language deployment.
- Do not treat language identification as a reliable proxy for dialect or code-switching.
- **Stop/review:** No accuracy or causal claim based on a dashboard or pipeline-success status alone. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://spacy.io/usage/models
- https://scikit-learn.org/stable/tutorial/text_analytics/

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
