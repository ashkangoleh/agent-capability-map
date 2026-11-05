---
name: swe-programming-languages-typescript
description: Use for typescript strict type safety tasks in Programming Language Engineering; verify preserve runtime validation despite compile-time TypeScript types. and reject unsupported release or safety claims.
license: Proprietary
metadata:
  version: "1.0.1"
---

# Programming Language Engineering: typescript

## Purpose and activation boundary
Preserve runtime validation despite compile-time TypeScript types. Activate only when the request concerns this precise software-engineering workflow; do not substitute it for data pipelines, infrastructure operations or unrelated security authorization.

## Inputs and prerequisites
TS/Node version, tsconfig strictness, module resolution, build target and API schemas. Confirm the current repository revision, versioned runtime and user permissions before writing changes. Unknown versions or unprovided logs are unknown, not inferred.

## Production procedure
1. Establish the current behavior, failure impact, caller/consumer boundaries and measurable acceptance criteria in the actual codebase.
2. Capture versioned evidence: TS/Node version, tsconfig strictness, module resolution, build target and API schemas. Identify missing data and the smallest falsifiable diagnosis or design hypothesis.
3. Plan the narrowest change compatible with current contracts, dependency graph and deployment constraints. Evaluate one simpler alternative and its operational cost.
4. Implement or specify the corrective mechanism: Preserve runtime validation despite compile-time TypeScript types. Handle negative paths, timeouts, authorization, concurrency and resource limits where applicable.
5. Validate failure and recovery cases, explicitly including: Unchecked unknown values, structural type loopholes and ESM/CJS incompatibility. Design retries, rollback or safe degradation where relevant, without assuming exactly-once effects.
6. Test against real runtime/library versions and peer interfaces; do not claim a build, benchmark, rollout or production behavior was observed unless actually executed.
7. Document changes, user-facing behavior, operational ownership, rollback feasibility and post-change monitoring.

## Evidence and authoritative sources
Use repository source, build configuration, lockfiles, test outputs, traces, threat models and published version-specific vendor documentation. General coverage reference: https://www.computer.org/education/bodies-of-knowledge/software-engineering/topics . Do not derive API compatibility solely from a general knowledge-area overview.

## Output contract
Run tsc and tests for runtime input validation and module imports. State implementation/diff or exact proposed design, tests actually run, tradeoffs, unresolved conditions and safe rollout/rollback steps.

## Failure modes and abstention
Reject assumptions that conceal Unchecked unknown values, structural type loopholes and ESM/CJS incompatibility. If required evidence is unavailable, provide an explicit validation plan rather than inventing passing results. Do not perform destructive migrations, exploit actions or unauthorized production changes.

## Validation checklist
- [ ] Actual project source/version and caller contracts inspected.
- [ ] Positive, negative, concurrency and boundary behavior assessed as relevant.
- [ ] Measurable tests or reason for not executing tests recorded.
- [ ] Dependency changes, security posture, observability and rollback checked.
- [ ] No unrelated domain, role or skill was loaded.

## Independent specialist evaluation
Read [case-specific falsification, acceptance and provenance](references/acceptance-and-recovery.md) on demand for production-impacting or high-stakes work. Unexecuted tests and unsupported claims remain unverified; this reference cannot authorize actions.
