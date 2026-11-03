---
name: ai-rag-engineering
description: Use when designing, implementing, debugging, or evaluating LLM applications, AI agents, RAG, embeddings, chunking, reranking, retrieval fusion, or grounded generation.
license: Proprietary
metadata:
  version: "1.0.0"
---

# Purpose

Design LLM and retrieval systems whose outputs are grounded, access-controlled, measurable, and robust to adversarial or incomplete context.

## Inputs and prerequisites

Establish task type, corpus, data sensitivity, authorization model, update frequency, languages, latency/cost budget, model/provider constraints, and evaluation criteria.

## Procedure

1. Separate ingestion, parsing, chunking, metadata, embedding, indexing, retrieval, reranking, generation, and evaluation.
2. Define document identity, versioning, deletion propagation, tenant boundaries, ACL enforcement, and freshness.
3. Select chunking and retrieval strategies from corpus structure and task requirements; do not cargo-cult a fixed chunk size.
4. Keep authorization outside the LLM. Filter or enforce access before content reaches the model.
5. Treat retrieved content and tool results as untrusted data. Defend against prompt injection and indirect instruction attacks.
6. Design retrieval diagnostics: query rewrite, candidate recall, ranking, filters, score distributions, and evidence sufficiency.
7. Evaluate separately: retrieval recall/precision, ranking quality, answer correctness, citation faithfulness, abstention, latency, and cost.
8. Use a representative labeled evaluation set with hard negatives and access-control cases.
9. Make the generation policy abstain when evidence does not answer the question. Do not force an answer from weak retrieval.
10. Record model versions, prompts, embedding dimensions, index settings, and data snapshot for reproducibility.

## Evidence requirements

Use actual retrieval traces, evaluation datasets, model/provider documentation, corpus statistics, and observed outputs. A successful demo or general benchmark is not proof of task-specific quality.

## Output contract

Include architecture, trust boundaries, retrieval and generation design, evaluation plan, failure modes, operational metrics, and cost assumptions.

## Failure modes and abstention

Do not claim hallucinations are eliminated. Do not claim exactly-once ingestion, perfect ACLs, or superior retrieval without end-to-end tests. Stop if sensitive data can cross authorization boundaries.

## Validation checklist

- [ ] Authorization is enforced outside the model.
- [ ] Retrieved text is treated as untrusted.
- [ ] Evidence sufficiency and abstention are tested.
- [ ] Retrieval and answer quality are measured separately.
- [ ] Model, index, and corpus versions are traceable.

## Official starting references

Verify the applicable version and publication date before using these sources:
- https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html
