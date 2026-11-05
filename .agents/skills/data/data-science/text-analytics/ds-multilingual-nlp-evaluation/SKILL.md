---
name: ds-multilingual-nlp-evaluation
description: Use when evaluating classical NLP or text classifiers across multiple languages, scripts, dialects, or code-switched content.
metadata:
  version: "1.0.1"
---

# ds-multilingual-nlp-evaluation

## Activation boundary

Use for language-stratified evaluation and error analysis of classical NLP systems. For LLM, multilingual embedding or foundation-model evaluation, route to AI/ML and compose with this skill only when classical text metrics are also required.

## Required context

Language/script distribution, dialects, code-switching, text source, annotation policy, target labels, model/tokenizer, privacy constraints and deployment population.

## Workflow

1. Inventory languages, scripts, dialects, code-switching, transliteration, spelling variation and source-specific text conventions. Do not infer language solely from geography or user profile.
2. Audit annotation quality and label definitions per language. Translate or harmonize label guidelines only after checking semantic equivalence and cultural ambiguity.
3. Build splits that prevent user, author, document-family, translation-pair and temporal leakage. Preserve the deployment language mix for one evaluation view and use balanced language slices for diagnosis.
4. Compare language-appropriate tokenization and normalization. Preserve script distinctions, diacritics, negation, named entities and code-switch boundaries when they affect meaning.
5. Establish word/character n-gram baselines and language-aware feature pipelines. Fit vocabularies and normalization statistics only on training data.
6. Report macro and per-language precision, recall, F1, calibration, coverage and confusion patterns. Include sample counts and uncertainty; do not let high-volume languages hide failure in low-resource groups.
7. Inspect error slices by script, dialect, code-switching, text length, source, label and time. Review false positives/negatives with native or qualified annotators when feasible.
8. Test transliteration, spelling normalization and translation augmentation as separate interventions. Check for translation leakage and distribution mismatch.
9. Document unsupported languages and abstention behavior. Define monitoring for language mix, vocabulary drift, annotation changes and performance degradation.

## Failure modes and abstention

- Do not report only micro-averaged performance when language representation is imbalanced.
- Do not assume a translated test set represents native-language deployment.
- Do not treat language identification as a reliable proxy for dialect or code-switching.
- Do not claim parity for languages with too few labels or wide uncertainty intervals.
- If annotation equivalence or tokenizer support is inadequate, report language-specific limitations rather than one global score.

## Validation checklist

- [ ] Language/script inventory and annotation quality are documented.
- [ ] Splits prevent user, source and translation leakage.
- [ ] Metrics are reported per language with sample counts.
- [ ] Code-switching, dialect and low-resource errors are reviewed.
- [ ] Unsupported languages have explicit abstention behavior.

## Authoritative references

- https://spacy.io/usage/models
- https://scikit-learn.org/stable/tutorial/text_analytics/

## Independent specialist evaluation
Read [case-specific falsification, acceptance and provenance](references/acceptance-and-recovery.md) on demand for production-impacting or high-stakes work. Unexecuted tests and unsupported claims remain unverified; this reference cannot authorize actions.
