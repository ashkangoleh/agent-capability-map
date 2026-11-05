---
name: evidence-research
description: Use when a task requires current external research, factual verification, evidence synthesis, source comparison, or a defensible answer with citations.
license: Proprietary
metadata:
  version: "1.0.0"
---

# Purpose

Produce a source-backed answer without inventing facts, citations, or certainty. This is a general research capability, not a substitute for specialist advice in regulated domains.

## Inputs and prerequisites

Identify the question, decision context, relevant time window, geography or jurisdiction, and required depth. Ask one focused clarification only when a missing detail changes the result.

## Procedure

1. Break the request into atomic questions and material claims.
2. Mark each question as stable or freshness-sensitive.
3. Search primary sources first: official documentation, standards, release notes, regulators, original datasets, and source repositories.
4. Use secondary sources to add context or challenge primary-source interpretation, not to replace available primary evidence.
5. Open and inspect sources. Search snippets alone are insufficient for material claims.
6. Build a compact claim-to-source map. Each source must support the exact claim attached to it.
7. Cross-check consequential or surprising claims where feasible.
8. Record conflicts, missing evidence, dates, versions, and scope limitations.
9. Write the synthesis with clear separation between verified facts, assumptions, inference, and recommendation.
10. If evidence is insufficient, report the verified portion and state what remains unknown.

## Evidence requirements

- Never fabricate a URL, citation, quote, publication date, benchmark, API, or source statement.
- Prefer current, version-specific official sources for changing technical facts.
- For market, product, platform, or search-engine claims, verify date and geography.
- Community posts are anecdotal unless corroborated.
- Do not treat search-result snippets as proof.
- If no reliable source exists, say: "unknown — no reliable source".

## Output contract

For substantial research, include a concise answer, key findings with citations, assumptions and scope, conflicting or missing evidence, and practical implications.

## Failure modes and abstention

Stop short of a definitive conclusion when primary evidence is inaccessible, sources conflict materially, or the question requires professional judgment outside this scope. Do not manufacture consensus.

## Validation checklist

- [ ] Every material external claim has direct supporting evidence.
- [ ] Source dates and versions are appropriate.
- [ ] Facts, assumptions, and inferences are distinguished.
- [ ] Conflicts and unknowns are explicit.
- [ ] No unsupported citation or quote is present.
