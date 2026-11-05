# starrocks-stream-load-transaction: specialist evaluation and negative controls

Domain `data/database-engineering/starrocks`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Check actual StarRocks version and shared-data/shared-nothing topology; verify that transaction features used exist in that release.
2. Select Stream Load, transactional Stream Load, Broker Load or INSERT based on input location, size and consistency requirements.
3. Define unique deterministic label from source batch/window/run and consider label retention; a label is not a perpetual deduplication guarantee.
4. Parse response status, filtered-row counts and tracking identifiers. Distinguish publish timeout from failed/aborted write; do not blindly retry an uncertain commit.

## Challenge / acceptance
- **Challenge:** Fail a transaction after partial client timeout and replay a CDC change. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Commit outcome, isolation and data invariants reconcile without blind retry. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - Check label state and published row counts before replaying uncertain batches.
- Record error messages, job state and data reconciliation per batch.
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
- https://docs.starrocks.io/docs/loading/Stream_Load_transaction_interface/
- https://docs.starrocks.io/docs/sql-reference/sql-statements/loading_unloading/STREAM_LOAD/

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
