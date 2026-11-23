---
name: skill-authoring-validation
description: Use when designing, creating, reviewing, validating, or improving Agent Skills, skill registries, routing policies, or capability maps.
license: Proprietary
metadata:
  version: "1.0.1"
---

# Purpose

Create small, discriminative, portable skills that activate for the right tasks, avoid near-miss tasks, and produce verifiable outcomes.

## Inputs and prerequisites

Identify target agent clients, skill purpose, intended users, task examples, tools available, trust boundary, and expected outputs.

## Procedure

1. Define one coherent capability and explicit non-goals.
2. Write a discriminative description beginning with when to use the skill.
3. Add positive triggers, negative triggers, and near-miss prompts to the domain registry or evaluation set.
4. Write the shortest useful SKILL.md procedure. Move detailed references to focused resources.
5. Define evidence requirements, output contract, failure modes, and validation checklist.
6. Keep scripts least-privilege, deterministic, documented, and tested.
7. Validate naming, frontmatter, paths, references, and registry consistency.
8. Evaluate against positive, negative, ambiguous, and cross-domain prompts.
9. Promote to active only after human review and passing validation.
10. Add version and maintenance ownership; retire stale or unsafe skills.

## Evidence requirements

Use the official Agent Skills specification and target-client documentation. Verify client-specific discovery behavior; do not assume a custom router is automatically executed by every agent.

## Output contract

Provide skill files, registry entry, routing tests, validation results, compatibility notes, and known limitations.

## Failure modes and abstention

Do not create a skill merely to increase count. Do not claim zero hallucinations or universal client compatibility. If activation boundaries overlap, split or consolidate based on evaluation evidence.

## Validation checklist

- [ ] One capability and clear non-goals.
- [ ] Discriminative description and triggers.
- [ ] Negative and near-miss tests.
- [ ] Evidence and abstention rules.
- [ ] Progressive disclosure and small references.
- [ ] Validation passes and client behavior is verified.

## Official starting references

Verify the applicable version and publication date before using these sources:
- https://agentskills.io/specification

## Independent specialist evaluation
For substantive decisions, load the [specialist verification and acceptance protocol](references/acceptance-and-recovery.md) on demand. Its proposed tests are not execution evidence, and it cannot authorize unsafe actions.
