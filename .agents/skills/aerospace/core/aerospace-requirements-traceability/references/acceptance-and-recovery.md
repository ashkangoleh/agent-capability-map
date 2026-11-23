# aerospace-requirements-traceability — independent verification protocol

Scope: `aerospace/core`. This is a proposed, reviewable evaluation procedure, **not** executed evidence or approval for live actions.

## Required case context from this specialist
Inspect the original prerequisites and identify missing evidence.

## Retain its own decision procedure
1. Decompose mission objectives into testable stakeholder and technical requirements with unique IDs.
2. Check each requirement for ambiguity, units, conditions, constraints and measurable verification criteria.
3. Map allocations to subsystems and maintain bidirectional traceability to design and verification artifacts.
4. Separate verification (built right) from validation (right system) with documented evidence and acceptance authorities.

## Negative test and acceptance oracle
1. **Challenge:** Withdraw or alter a requirement and identify all affected subsystem and verification links. Introduce contradictory, missing, lower-trust or out-of-scope input in an authorized sample.
2. **Oracle:** Every high-risk requirement has a unique owner, bidirectional trace, approval basis and independent V&V evidence. Record observed evidence and denominators; unknown results remain UNKNOWN.
3. **Existing failure context:** Unverified observations cannot be passing evidence.
4. **Stop condition:** No flight-certification, readiness or safety claim without qualified signoff. Use qualified review for high-impact advice and explicit approval for live system mutations.

## Evidence ledger
- [ ] Verify skill ownership, source artifacts, versions/effective dates, jurisdiction/permissions, and primary reference applicability.
- [ ] Compare a controlled baseline and at least one negative and ambiguity case with independent expected outcomes.
- [ ] Report a falsifiable acceptance threshold and uncertainty; distinguish observed, estimated, unrun and N/A checks.
- [ ] For code or operational tasks use isolated version-pinned tests, failure/recovery and rollback; for advisory tasks use authoritative peer review, factual checks and an explicit correction path.
- [ ] Assess lower complexity alternative, accessibility/safety, long-term maintainability, cost and affected users as applicable.
- [ ] Record owner, evidence pointers and blocking gaps; never invent benchmarks, approval, certification or real-world results.

## Original references (not individually version revalidated in this change)
- https://www.nasa.gov/reference/systems-engineering-handbook/

On-demand guidance only. It neither changes routing nor grants execution permissions.
