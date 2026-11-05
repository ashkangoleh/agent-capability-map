---
name: virtualization-kvm-proxmox-vmware
description: "Operate KVM, Proxmox and VMware virtualization with capacity, networking, storage and HA controls."
metadata:
  version: "1.0.1"
---

# virtualization-kvm-proxmox-vmware

## Activation boundary
Operate KVM, Proxmox and VMware virtualization with capacity, networking, storage and HA controls.

## Required context
Hypervisor version, cluster topology, CPU/RAM overcommit, storage, networking and licensing.

## Production procedure
1. Map hypervisor/cluster topology, CPU/RAM overcommit, storage and virtual networking.
2. Check HA, quorum, migration compatibility, snapshots and backup integration.
3. Plan upgrades with capacity headroom and tested guest compatibility.
4. Measure noisy-neighbor and storage latency under representative workloads.
5. Test host loss, live migration, datastore outage and restore.

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
- https://www.kernel.org/doc/html/latest/virt/kvm/
- https://pve.proxmox.com/pve-docs/

## Output contract
Return the requested design or diagnosis with exact scope, assumptions, evidence, safe procedure, failure modes, validation and rollback. Never claim production changes or tests that were not performed.

## Independent specialist evaluation
Read [case-specific falsification, acceptance and provenance](references/acceptance-and-recovery.md) on demand for production-impacting or high-stakes work. Unexecuted tests and unsupported claims remain unverified; this reference cannot authorize actions.
