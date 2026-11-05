# database-nosql-cache-operations: specialist evaluation and negative controls

Domain `infrastructure/database-infrastructure/ha-nosql`. This is a **proposed** evidence plan, never a real-system test result or execution permission.

## Specialist required inputs
Verify specialist prerequisites against real artifacts.

## Preserve skill-specific method
1. Document consistency, durability, write acknowledgement, quorum, read preference, TTL and eviction semantics.
2. Design replica/shard placement across failure domains and validate rebalancing/repair.
3. Set persistence, snapshots and backup policy; classify cache-only data explicitly.
4. Monitor replication lag, fragmentation, evictions, compaction, tombstones, hot partitions and connections.

## Challenge / acceptance
- **Challenge:** Lose a node, permission or control plane while applying a scoped change. Exercise an authorized contradictory, missing or adversarial test input.
- **Independent oracle:** Actual target identity, SLO, rollback prerequisites and failure isolation are independently checked. Reconcile observed outcomes against a fixed control; do not use the generated answer as its own oracle.
- **Existing failure risks:** - Redis eviction/persistence may lose data if cache is treated as durable.
- Elections/quorum changes affect availability and consistency; validate retries.
- Hot keys and compaction debt cause tail latency.
- **Stop/review:** No destructive, credential or production control-plane changes without authorization. Stop at incomplete authorizations, uncertain authoritative sources and irreversible changes.

## Acceptance evidence ledger
- [ ] Real source artifacts, version/effective date, scope, owner, permissions and lower-trust input boundary recorded.
- [ ] At least one baseline, negative control, ambiguity/near miss and recovery/retraction test documented with falsifiable expected outcomes.
- [ ] Domain-specific result, affected population, uncertainty, metrics and policy constraints independently verified.
- [ ] For implementation: isolated executable compatibility/failure tests, side effects and rollback. For advisory work: qualified independent review and citation audit instead.
- [ ] Simpler alternative, operational cost, incident/escalation owner and explicitly unresolved uncertainties stated.
- [ ] Separate proposed test from executed evidence; never claim production, legal, medical, security or regulatory certification from CI.

## Starting sources already listed by the skill (release applicability not independently validated)
- https://www.mongodb.com/docs/manual/replication/
- https://redis.io/docs/latest/operate/oss_and_stack/management/replication/
- https://cassandra.apache.org/doc/latest/

This reference is lazy-loaded only when appropriate and cannot override higher-priority safety instructions.
