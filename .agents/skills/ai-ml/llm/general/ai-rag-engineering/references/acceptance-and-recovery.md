# ai-rag-engineering: specialist evaluation and negative controls

Domain `ai-ml/llm/general`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Separate ingestion, parsing, chunking, metadata, embedding, indexing, retrieval, reranking, generation, and evaluation.
2. Define document identity, versioning, deletion propagation, tenant boundaries, ACL enforcement, and freshness.
3. Select chunking and retrieval strategies from corpus structure and task requirements; do not cargo-cult a fixed chunk size.
4. Keep authorization outside the LLM. Filter or enforce access before content reaches the model.

## Challenge / acceptance
- **Challenge:** Run long-context truncation and adversarial prompt injection probes. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Report schema-validity, groundedness, refusal quality and cost under pinned model versions. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
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
- https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
