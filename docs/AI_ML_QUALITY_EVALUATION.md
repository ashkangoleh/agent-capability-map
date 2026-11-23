# AI/ML specialist quality gates and routing regression audit

Updated: 2026-11-05. Branch: `pre_release`.

## What is verified by this suite

- There are 43 new distinct alternative **registered lexical phrases**, one per specialist, checked through the root, first-level, leaf map, and skill registry. This does not mean that unknown synonyms or semantic paraphrases can be understood.
- Each of the 43 new specialist SKILL.md files has a distinct measured acceptance test and explicit failure/rejection gate, including sample-count and version provenance. This is a quality *contract*, not evidence that any real ML model was tested.
- The regression corpus includes 43 positive natural phrasings, 12 cross-domain/negative cases (including original owner preservation and mapped-only handling) and one user-scope denial test. All are deterministic; full CI must pass on the current SHA.
- Canonical inventory unchanged: 41 top-level domains, 438 active skill IDs, 408 ROLE.md files, and 66 active AI/ML leaves. The five non-overlapping user selections remain the maximum.

## Blinded real-agent A/B (NOT EXECUTED)

1. Build a frozen, de-identified and license-approved dataset of independently reviewed tasks across all 12 AI/ML branches. Include unanswerable, outdated, multilingual, cross-tenant and incident-recovery tasks.
2. Pin agent host/version, baseline model, system prompt, tools, token budget, evaluation data and task order. Baseline: no specialist role/skill. Treatment: matched skill plus role inheritance. Randomize output order.
3. Conduct blind primary and secondary reviews with adjudication. Measure task correctness, grounded citations, unsupported claims, failure-handling completeness, access-policy violations, refusal quality, tokens, p95 latency and cost per successful task.
4. Compare paired results per subdomain, show denominators, confidence intervals and regressions. Do not average away critical policy breaches; agree minimum practical improvement and cost cap before the experiment.
5. A promotion requires no critical access-control bypass, no unexpected privileged action and a measured quality gain on held-out tasks. A passing YAML/CI suite does not satisfy this criterion.

## Known gaps

- The alternate phrases are handwritten, not mined from real user prompts; this is lexical regression coverage, not semantic routing capability.
- Existing ML validation remains mapped-only.
- There are no A/B results from Codex, Claude Code, OpenCode, Copilot, or Cursor, so effectiveness and token savings remain unverified.

## References

- NIST AI RMF: https://www.nist.gov/itl/ai-risk-management-framework
- OWASP LLM Top 10 2026: https://github.com/GenAI-Security-Project/GenAI-LLM-Top10/tree/main/2026/final
- MLflow GenAI evaluation documentation: https://www.mlflow.org/docs/latest/genai/eval-monitor/quickstart/
- Agent Skills specification: https://agentskills.io/specification
