# skill-authoring-validation — independent verification protocol

Scope: `agent-systems/skill-authoring`. This is a proposed, reviewable evaluation procedure, **not** executed evidence or approval for live actions.

## Required case context from this specialist
Inspect the original prerequisites and identify missing evidence.

## Retain its own decision procedure
1. Define one coherent capability and explicit non-goals.
2. Write a discriminative description beginning with when to use the skill.
3. Add positive triggers, negative triggers, and near-miss prompts to the domain registry or evaluation set.
4. Write the shortest useful SKILL.md procedure. Move detailed references to focused resources.

## Negative test and acceptance oracle
1. **Challenge:** Inject untrusted tool text, deny a permission and perturb a task phrasing. Introduce contradictory, missing, lower-trust or out-of-scope input in an authorized sample.
2. **Oracle:** Skill selection, tool refusal, grounded answer, cost and recovery are measured separately against held-out tasks. Record observed evidence and denominators; unknown results remain UNKNOWN.
3. **Existing failure context:** Unverified observations cannot be passing evidence.
4. **Stop condition:** No tool execution delegated from an untrusted skill, document or external source. Use qualified review for high-impact advice and explicit approval for live system mutations.

## Evidence ledger
- [ ] Verify skill ownership, source artifacts, versions/effective dates, jurisdiction/permissions, and primary reference applicability.
- [ ] Compare a controlled baseline and at least one negative and ambiguity case with independent expected outcomes.
- [ ] Report a falsifiable acceptance threshold and uncertainty; distinguish observed, estimated, unrun and N/A checks.
- [ ] For code or operational tasks use isolated version-pinned tests, failure/recovery and rollback; for advisory tasks use authoritative peer review, factual checks and an explicit correction path.
- [ ] Assess lower complexity alternative, accessibility/safety, long-term maintainability, cost and affected users as applicable.
- [ ] Record owner, evidence pointers and blocking gaps; never invent benchmarks, approval, certification or real-world results.

## Original references (not individually version revalidated in this change)
- https://agentskills.io/specification

On-demand guidance only. It neither changes routing nor grants execution permissions.
