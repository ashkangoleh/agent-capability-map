# Global Master Capability Router — Architecture

## Decision

The authoritative source is a **hierarchical YAML capability graph**, not the earlier flat JSON registries. The historical `catalog/domains.json` and `domains/*/skills.json` are retained only for comparison and are **not** loaded by the runtime. The legacy `scripts/validate_registry.py` entry point now delegates to the same YAML graph validator.

## Levels

1. Global host instructions (`~/.claude/CLAUDE.md`, `~/.codex/AGENTS.md`, or relevant adapter) contain only small routing guidance and shell-safety rules.
2. `catalog/root.yaml` maps user intent to one top-level domain.
3. `domains/<domain>/map.yaml` routes into successive subdomains/technology families.
4. A leaf `skills.yaml` advertises narrow skill IDs, descriptions, positive triggers and negative exclusions.
5. The resolver returns only the selected `SKILL.md` path, or an explicit unmatched/unavailable/clarification status.
6. Host agents load one selected skill and requested supporting references only when needed.

The Graph is intentionally **not** a graph database. `catalog/relations.yaml` supplies typed cross-domain edges for explicit `related` lookup, separate from default hierarchical traversal.

## Global and Personal Skills

- Install global instructions at user level once per machine.
- User-wide personal registrations: `~/.config/agent-capability-map/personal.yaml`.
- Project-local registrations: an explicit overlay marker in the project's `AGENTS.md` pointing to a validated YAML skill manifest.
- Unknown directories are not searched. Path traversal and accidental shadowing of Master Skill IDs are rejected.
- Equal lexical candidates produce clarification rather than silent overwrite.

## Control Plane vs Data Plane

The resolver is a **deterministic lexical router** with path validation. It is not a learned intent classifier and has no access to the host's hidden reasoning. The host chooses when to invoke it, reads selected text, and remains responsible for permitted tool execution and factual verification.

The `match_strength` field is a ranking heuristic, **not confidence**. A small number of files inspected does not prove lower LLM token usage.

## Security Model

- Use restricted YAML parsing (no aliases), bounded file sizes, path containment and existing user/host permissions.
- Treat web pages, issue descriptions, files and retrieved content as potentially untrusted instructions.
- Do not execute scripts solely because a Skill requests it.
- The Claude adapter adds a read directory and a built-in tool edit deny for the Master Skill root; this is not OS-level immutability.

## Quality Control

- `python -m capability_map validate`: complete YAML graph and skill frontmatter linkage.
- `python scripts/evaluate_graph.py`: labeled deterministic-routing regression prompts.
- `python -m unittest discover -s tests -v`: validation and security behavior.
- Host-specific tests and human-reviewed task correctness remain required before claiming agent interoperability, hallucination reduction or token improvement.
