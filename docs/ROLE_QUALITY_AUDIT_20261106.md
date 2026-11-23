# Four-domain Role Quality Audit — 2026-11-06

## Decision
Strengthen the 120 existing reviewer contracts without changing skill IDs, canonical SKILL.md bodies, router scoring, active graph, dispatch permissions or host adapters.

## Verified structural scope
| Domain | Root roles | Subdomain roles | Leaf roles | Total |
| --- | ---: | ---: | ---: | ---: |
| Marketing | 1 | 7 | 17 | 25 |
| SEO | 1 | 9 | 22 | 32 |
| Content | 1 | 9 | 22 | 32 |
| Research | 1 | 8 | 22 | 31 |
| **Total** | **4** | **33** | **83** | **120** |

All roles now carry a short, level-specific, domain-grounded acceptance block:
- Root: cross-domain governance, ownership and stop conditions.
- Subdomain: scoped reviewer delegation, evidence and escalation.
- Leaf: concrete input evidence, independent acceptance criterion and failure stop.

### Representative falsifiable gates
- Marketing conversion: reconcile deduplicated conversion event with source order, **not** attributed clicks as causal gain.
- SEO canonical/indexing: distinguish HTTP crawlability, Google-selected canonical, indexed status and observed ranking.
- Content publishing: check commercial licensing, actual publication approval and corrective release path.
- Research citations: inspect original material and use DOI metadata only for identity, not claim support.

### Tests and limits
The new test \`tests/test_expanded_domain_role_quality.py\` validates 4/33/83 files, exact matching role IDs, three named decision controls, unique leaf contracts, active graph structure, inherited role order and the existing 8-KiB/8-file chain limits. Exact-commit full CI must pass before structural certification.

This is evidence of an **L1 role contract**, not expert-judged correctness, model adherence, absence of hallucinations or real host injection. Separately evaluate task output accuracy, false activation/abstention, compliance stop behavior and token/latency in each supported host.

### Host model limitations
\`ROLE.md\` is a repository-specific overlay resolved by \`role_paths_for_route\`. Codex discovers scoped \`AGENTS.md\`; Copilot supports repository/path-specific instructions; Claude Code distinguishes \`CLAUDE.md\`, skills and subagents. None of these external host conventions automatically installs or guarantees this custom overlay. An integration must explicitly consume and apply returned \`role_paths\` in the specified order. Do not add duplicate host instructions solely to increase nominal coverage.

Official starting points:
- https://developers.openai.com/cookbook/examples/gpt-5/codex_prompting_guide
- https://docs.github.com/en/copilot/concepts/prompting-and-context/custom-instructions
- https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more
