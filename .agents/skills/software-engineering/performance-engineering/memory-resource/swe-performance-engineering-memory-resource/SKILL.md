---
name: swe-performance-engineering-memory-resource
description: Use for application memory leak resource lifecycle tasks in Application Performance and Capacity; verify diagnose memory leaks, resource exhaustion and lifecycle ownership. and reject unsupported release or safety claims.
license: Proprietary
metadata:
  version: "1.0.0"
---

# Application Performance and Capacity: memory resource

## Purpose and activation boundary
Diagnose memory leaks, resource exhaustion and lifecycle ownership. Activate only when the request concerns this precise software-engineering workflow; do not substitute it for data pipelines, infrastructure operations or unrelated security authorization.

## Inputs and prerequisites
Heap snapshots, allocation profiles, GC events, file descriptors and job lifetime. Confirm the current repository revision, versioned runtime and user permissions before writing changes. Unknown versions or unprovided logs are unknown, not inferred.

## Production procedure
1. Establish the current behavior, failure impact, caller/consumer boundaries and measurable acceptance criteria in the actual codebase.
2. Capture versioned evidence: Heap snapshots, allocation profiles, GC events, file descriptors and job lifetime. Identify missing data and the smallest falsifiable diagnosis or design hypothesis.
3. Plan the narrowest change compatible with current contracts, dependency graph and deployment constraints. Evaluate one simpler alternative and its operational cost.
4. Implement or specify the corrective mechanism: Diagnose memory leaks, resource exhaustion and lifecycle ownership. Handle negative paths, timeouts, authorization, concurrency and resource limits where applicable.
5. Validate failure and recovery cases, explicitly including: Assuming cache equals leak, OOM hidden by retries and unbounded queues. Design retries, rollback or safe degradation where relevant, without assuming exactly-once effects.
6. Test against real runtime/library versions and peer interfaces; do not claim a build, benchmark, rollout or production behavior was observed unless actually executed.
7. Document changes, user-facing behavior, operational ownership, rollback feasibility and post-change monitoring.

## Evidence and authoritative sources
Use repository source, build configuration, lockfiles, test outputs, traces, threat models and published version-specific vendor documentation. General coverage reference: https://www.computer.org/education/bodies-of-knowledge/software-engineering/topics . Do not derive API compatibility solely from a general knowledge-area overview.

## Output contract
Validate steady-state memory, cleanup and failure recovery. State implementation/diff or exact proposed design, tests actually run, tradeoffs, unresolved conditions and safe rollout/rollback steps.

## Failure modes and abstention
Reject assumptions that conceal Assuming cache equals leak, OOM hidden by retries and unbounded queues. If required evidence is unavailable, provide an explicit validation plan rather than inventing passing results. Do not perform destructive migrations, exploit actions or unauthorized production changes.

## Validation checklist
- [ ] Actual project source/version and caller contracts inspected.
- [ ] Positive, negative, concurrency and boundary behavior assessed as relevant.
- [ ] Measurable tests or reason for not executing tests recorded.
- [ ] Dependency changes, security posture, observability and rollback checked.
- [ ] No unrelated domain, role or skill was loaded.
