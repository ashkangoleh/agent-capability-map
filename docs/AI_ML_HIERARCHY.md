# AI/ML hierarchy — 2026-11-05

Working branch: `pre_release`. All existing skill IDs and SKILL.md bodies are preserved, including the previous single-leaf registry paths for vision, speech and responsible AI. Current mapped-only machine learning validation is deliberately not activated without a reviewed validation skill.

| Subdomain | Active leaves | New specialists |
|---|---:|---:|
| `llm-engineering` | 10 | 4 |
| `rag-retrieval` | 8 | 4 |
| `machine-learning` | 8 | 4 |
| `deep-learning` | 6 | 4 |
| `mlops` | 8 | 4 |
| `computer-vision` | 4 | 3 |
| `speech-audio-ai` | 4 | 3 |
| `responsible-ai` | 4 | 3 |
| `natural-language-processing` | 4 | 4 |
| `recommender-systems` | 4 | 4 |
| `reinforcement-learning` | 3 | 3 |
| `multimodal-ai` | 3 | 3 |

**Inventory:** 12 subdomains, 66 active leaves, 79 independent role contracts, 43 added specialist SKILL.md files. Existing roles from other domains and the max-five independent domain-scope limit remain untouched.

**Boundaries:** AI/ML owns model construction, evaluation and inference. Data owns ETL and statistical inference; Security owns general threat modeling; Agent Systems owns agent runtime, tool protocols and skill routing. AI-specific security reviews must not override security policies.

**Sources:** [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework), [OWASP GenAI 2026](https://github.com/GenAI-Security-Project/GenAI-LLM-Top10/tree/main/2026/final), [Google MLOps](https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning), [Agent Skills](https://agentskills.io/specification).

**Unverified:** Real-agent host integration, blinded quality A/B, model-task benchmark outcomes and production readiness. Full CI must pass against the exact new SHA; schema/fixture passes alone do not prove model effectiveness.
