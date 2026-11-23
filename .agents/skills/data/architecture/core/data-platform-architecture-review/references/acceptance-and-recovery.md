# data-platform-architecture-review: specialist evaluation and negative controls

Domain `data/architecture/core`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Define workload objectives, data product grain, availability, latency and recovery requirements before selecting engines.
2. Map ingestion, CDC, storage format, catalog, compute, orchestration, governance and serving separately; identify contracts at each boundary.
3. Challenge proposed components for overlapping responsibilities, unnecessary state/queues/catalogs and hidden cross-engine transaction gaps.
4. Compare a minimal baseline against serious alternatives, scoring scalability, operability, data quality, cost, portability and migration.

## Challenge / acceptance
- **Challenge:** Introduce temporal leakage, duplicate records or changed metric grain. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Independent reconciliation, versioned logic and explicit uncertainty preserve analytic correctness. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - Test one representative ingestion-transform-serving path through partial failure and replay.
- Collect evidence of query latency, operational burden and total cost rather than synthetic invented benchmarks.
- Include edge cases, timeouts and partial failures where material; do not claim tests executed without tool traces.
- **Stop/review:** No accuracy or causal claim based on a dashboard or pipeline-success status alone. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://iceberg.apache.org/docs/latest/
- https://trino.io/docs/current/
- https://spark.apache.org/documentation

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
