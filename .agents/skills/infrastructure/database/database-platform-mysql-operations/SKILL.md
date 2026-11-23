---
name: database-platform-mysql-operations
description: "Operate MySQL infrastructure including replication, backups, failover, binlog retention and connection capacity."
metadata:
  version: "1.0.1"
---

# database-platform-mysql-operations

## Activation boundary
Operate MySQL infrastructure including replication, backups, failover, binlog retention and connection capacity.

## Required context
MySQL version, topology, GTID/binlog, backup method, failover, replication lag and proxies.

## Production procedure
1. Inspect version, topology, replication, WAL/binlog retention, backup and connection pools.
2. Define RPO/RTO, failover fencing, read/write routing and recovery sequencing.
3. Tune memory, storage, vacuum/maintenance and connection concurrency from measurements.
4. Test restore, replica lag, split-brain prevention, schema upgrades and rollback.
5. Verify application behavior after failover, not only database process health.

## Failure modes and recovery
- Start with read-only evidence collection and confirm the exact environment/cluster/account before mutation.
- Treat credentials, production data, network reachability and state backends as security boundaries.
- Define blast radius, abort criteria, rollback limits and post-change verification before execution.
- Do not claim availability, security or recovery guarantees without evidence from the deployed version and tested path.

## Validation
- Verify product/version compatibility against official documentation.
- Test failure, partial rollout, identity expiry, capacity exhaustion and recovery where applicable.
- Record ownership, monitoring, approval and rollback evidence.

## Official references
- https://dev.mysql.com/doc/refman/8.4/en/

## Output contract
Return the requested design or diagnosis with exact scope, assumptions, evidence, safe procedure, failure modes, validation and rollback. Never claim production changes or tests that were not performed.

## Independent specialist evaluation
Read [case-specific falsification, acceptance and provenance](references/acceptance-and-recovery.md) on demand for production-impacting or high-stakes work. Unexecuted tests and unsupported claims remain unverified; this reference cannot authorize actions.
