# Skill Authoring Standard

## Scope

A skill is one reusable capability with a clear activation boundary and a verifiable output. Do not create a skill for every tool, technology keyword, or one-off prompt.

## Required metadata

Every skill must use the Agent Skills folder format:
- directory name equals the skill name;
- SKILL.md begins with YAML frontmatter;
- name is lowercase kebab-case;
- description says what the skill does and when to use it;
- body defines a repeatable workflow, not a generic persona.

## Required body sections

1. Purpose and activation boundary.
2. Inputs and prerequisites.
3. Procedure with ordered steps.
4. Evidence and source requirements.
5. Output contract.
6. Failure modes and abstention conditions.
7. Validation checklist.
8. References loaded only when needed.

## Design constraints

- One coherent unit of work per skill.
- Prefer a useful default, not a long menu of alternatives.
- Keep SKILL.md below 500 lines and preferably below 5,000 tokens.
- Move deep material to focused reference files.
- Keep references one level deep where practical.
- Do not duplicate canonical documentation between skills.
- Include positive triggers, negative triggers, and near-miss tests in the domain registry or evaluation fixtures.
- Optional parent_skill must refer to an active skill in the same domain, and parent links must be acyclic. related_skills may cross domains but never trigger automatic loading. Every child SKILL.md must be independently useful without reading ancestor bodies.
- Before adding a child, demonstrate a different workflow and discriminating triggers from its parent. If the difference is merely deeper documentation, create a focused reference instead.
- Scripts must be deterministic where possible, documented, tested, and least-privilege.
- Never embed secrets, personal data, or unlicensed third-party material.
- Do not state that the skill prevents hallucination; state what evidence and validation controls it applies.

## Promotion lifecycle

Draft → metadata validation → human review → positive/negative routing tests → task evaluation → active → periodic maintenance.

A skill with stale references, broken paths, weak routing metadata, or unreviewed executable scripts must not be treated as trusted active capability.
