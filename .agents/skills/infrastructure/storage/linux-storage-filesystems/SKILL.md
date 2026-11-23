---
name: linux-storage-filesystems
description: "Operate Linux block devices, filesystems, LVM, mounts and capacity with safe recovery planning."
metadata:
  version: "1.0.1"
---

# linux-storage-filesystems

## Activation boundary
Operate Linux block devices, filesystems, LVM, mounts and capacity with safe recovery planning.

## Required context
Device topology, filesystem, mount options, LVM/RAID, backups and kernel modules.

## Production procedure
1. Capture read-only host evidence: kernel, distribution, boot logs, units, devices and resource pressure.
2. Trace CPU, memory, I/O, filesystem, driver and service dependencies before remediation.
3. Check package/kernel compatibility, backups, mount state and maintenance constraints.
4. Apply reversible changes with explicit rollback and post-change health checks.
5. Test reboot, device loss, filesystem recovery and resource saturation.

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
- https://man7.org/linux/man-pages/
- https://docs.kernel.org/filesystems/

## Output contract
Return the requested design or diagnosis with exact scope, assumptions, evidence, safe procedure, failure modes, validation and rollback. Never claim production changes or tests that were not performed.

## Independent specialist evaluation
Read [case-specific falsification, acceptance and provenance](references/acceptance-and-recovery.md) on demand for production-impacting or high-stakes work. Unexecuted tests and unsupported claims remain unverified; this reference cannot authorize actions.
