---
name: storage-ceph-zfs-lvm
description: "Design and troubleshoot Ceph, ZFS and LVM storage with durability, replication and recovery constraints."
metadata:
  version: "1.0.1"
---

# storage-ceph-zfs-lvm

## Activation boundary
Design and troubleshoot Ceph, ZFS and LVM storage with durability, replication and recovery constraints.

## Required context
Storage topology, failure domains, pool/RAID layout, checksums, snapshots and rebuild limits.

## Production procedure
1. Define durability, failure domains, replication, consistency and recovery requirements.
2. Inspect device health, pool/volume layout, filesystem, snapshots and capacity.
3. Plan rebuild/resilver/compaction with I/O headroom and backup validation.
4. Protect encryption keys, credentials and deletion boundaries.
5. Test disk/node failure, corruption, degraded mode and restore.

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
- https://docs.ceph.com/en/latest/
- https://openzfs.github.io/openzfs-docs/

## Output contract
Return the requested design or diagnosis with exact scope, assumptions, evidence, safe procedure, failure modes, validation and rollback. Never claim production changes or tests that were not performed.

## Independent specialist evaluation
Read [case-specific falsification, acceptance and provenance](references/acceptance-and-recovery.md) on demand for production-impacting or high-stakes work. Unexecuted tests and unsupported claims remain unverified; this reference cannot authorize actions.
