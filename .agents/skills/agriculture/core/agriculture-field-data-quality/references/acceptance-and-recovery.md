# agriculture-field-data-quality — independent verification protocol

Scope: `agriculture/core`. This is a proposed, reviewable evaluation procedure, **not** executed evidence or approval for live actions.

## Required case context from this specialist
Inspect the original prerequisites and identify missing evidence.

## Retain its own decision procedure
1. Define field, plot, season and observation identifiers and distinguish event time from reporting time.
2. Inspect geo-coordinate systems, sampling coverage, weather/soil sensor calibration and expected measurement ranges.
3. Identify impossible values, unit errors, duplicates, gaps and spatial overlap without labeling unusual observations as definitively wrong.
4. Record survey/sensor provenance, consent, data ownership and retention; minimize personally identifiable farmer data.

## Negative test and acceptance oracle
1. **Challenge:** Change soil, weather, growth stage or regulatory region in a proposed recommendation. Introduce contradictory, missing, lower-trust or out-of-scope input in an authorized sample.
2. **Oracle:** Recommendation is supported by relevant field measurements and locally applicable official agronomic guidance. Record observed evidence and denominators; unknown results remain UNKNOWN.
3. **Existing failure context:** Unverified observations cannot be passing evidence.
4. **Stop condition:** No pesticide, dosage, crop-safety or yield guarantee without current local authorization. Use qualified review for high-impact advice and explicit approval for live system mutations.

## Evidence ledger
- [ ] Verify skill ownership, source artifacts, versions/effective dates, jurisdiction/permissions, and primary reference applicability.
- [ ] Compare a controlled baseline and at least one negative and ambiguity case with independent expected outcomes.
- [ ] Report a falsifiable acceptance threshold and uncertainty; distinguish observed, estimated, unrun and N/A checks.
- [ ] For code or operational tasks use isolated version-pinned tests, failure/recovery and rollback; for advisory tasks use authoritative peer review, factual checks and an explicit correction path.
- [ ] Assess lower complexity alternative, accessibility/safety, long-term maintainability, cost and affected users as applicable.
- [ ] Record owner, evidence pointers and blocking gaps; never invent benchmarks, approval, certification or real-world results.

## Original references (not individually version revalidated in this change)
- https://www.fao.org/e-agriculture/
- https://www.fao.org/faostat/en/

On-demand guidance only. It neither changes routing nor grants execution permissions.
