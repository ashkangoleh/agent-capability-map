# aiml-computer-vision-detection-segmentation — independent verification protocol

Scope: `ai-ml/computer-vision/detection-segmentation`. This is a proposed, reviewable evaluation procedure, **not** executed evidence or approval for live actions.

## Required case context from this specialist
Inspect the original prerequisites and identify missing evidence.

## Retain its own decision procedure
1. Capture current model, data, baseline, runtime and deployment contract; define falsifiable acceptance tests and affected consumers.
2. Inspect labeling/split chronology and access provenance; block leakage, untrusted instructions, test-set contamination and unauthorized input.
3. Design the specialist solution around these explicit variables: object and mask labels, IoU and rare classes. Compare a simpler existing baseline before expanding infrastructure.
4. Exercise the risk cases: tiny-object miss and label shift. Include shift, missing inputs, outliers, retries, partial artifacts and rollback wherever relevant.

## Negative test and acceptance oracle
1. **Challenge:** Swap image device, occlusion and rare-class sample. Introduce contradictory, missing, lower-trust or out-of-scope input in an authorized sample.
2. **Oracle:** Report per-class errors, IoU and annotation provenance. Record observed evidence and denominators; unknown results remain UNKNOWN.
3. **Existing failure context:** Unverified observations cannot be passing evidence.
4. **Stop condition:** No model-quality or security claim based on a route fixture or demonstration. Use qualified review for high-impact advice and explicit approval for live system mutations.

## Evidence ledger
- [ ] Verify skill ownership, source artifacts, versions/effective dates, jurisdiction/permissions, and primary reference applicability.
- [ ] Compare a controlled baseline and at least one negative and ambiguity case with independent expected outcomes.
- [ ] Report a falsifiable acceptance threshold and uncertainty; distinguish observed, estimated, unrun and N/A checks.
- [ ] For code or operational tasks use isolated version-pinned tests, failure/recovery and rollback; for advisory tasks use authoritative peer review, factual checks and an explicit correction path.
- [ ] Assess lower complexity alternative, accessibility/safety, long-term maintainability, cost and affected users as applicable.
- [ ] Record owner, evidence pointers and blocking gaps; never invent benchmarks, approval, certification or real-world results.

## Original references (not individually version revalidated in this change)
- https://www.nist.gov/itl/ai-risk-management-framework
- https://github.com/GenAI-Security-Project/GenAI-LLM-Top10/tree/main/2026/final
- https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning

On-demand guidance only. It neither changes routing nor grants execution permissions.
