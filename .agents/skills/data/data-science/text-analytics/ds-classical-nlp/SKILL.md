---
name: ds-classical-nlp
description: Use when building classical text analytics or NLP systems with tokenization, sparse features, interpretable baselines, and language-aware evaluation.
metadata:
  version: "1.1.0"
---

# ds-classical-nlp

## Activation boundary

Use for classical text classification, retrieval features, topic discovery, sentiment or document analysis with sparse/statistical methods. Route foundation-model, LLM or embedding-serving work to AI/ML.

## Required context

Language/script, text unit, labels, class prevalence, privacy constraints, annotation policy, vocabulary drift and prediction-time availability.

## Workflow

1. Define the text unit, target label, language distribution, annotation source and intended decision. Audit duplicates, near-duplicates and label disagreement.
2. Split by user, document family, source or time before fitting tokenizers or vocabulary. Prevent author, template and near-duplicate leakage.
3. Normalize conservatively. Preserve negation, numbers, punctuation, named entities and script distinctions when they carry signal. Keep raw text and transformation provenance.
4. Compare word n-gram and character n-gram TF-IDF baselines with simple linear classifiers before more complex models. Fit vectorizers inside the training pipeline.
5. Handle class imbalance with class weights or training-only resampling; preserve natural prevalence in validation and test data.
6. Evaluate macro and per-class precision/recall/F1, confusion matrices, calibration and threshold costs. Report language-stratified and time-stratified results.
7. Inspect false positives/negatives, annotation noise, sensitive text leakage, vocabulary drift and code-switching.
8. Test inference-time preprocessing parity and document model size, latency, vocabulary version and retraining triggers.

## Failure modes and abstention

- Do not use random row splits when the same user, source or template appears across splits.
- Do not translate test data into a dominant language and claim native-language quality.
- Do not use accuracy alone for imbalanced labels.
- If language coverage or annotation reliability is inadequate, report per-language abstention rather than one misleading aggregate score.

## Validation checklist

- [ ] Text unit, language and annotation policy are explicit.
- [ ] Duplicate/group/time leakage is checked.
- [ ] Preprocessing is fitted only on training data.
- [ ] Per-class and per-language metrics are reported.
- [ ] Privacy, drift and inference parity are checked.

## Authoritative references

- https://scikit-learn.org/stable/tutorial/text_analytics/
- https://spacy.io/usage/models
