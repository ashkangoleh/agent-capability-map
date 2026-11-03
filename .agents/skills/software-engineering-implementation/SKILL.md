---
name: software-engineering-implementation
description: Use when implementing, debugging, refactoring, or reviewing application code, APIs, libraries, or software architecture in an existing or new codebase.
license: Proprietary
metadata:
  version: "1.0.0"
---

# Purpose

Deliver correct, maintainable software changes grounded in the actual repository and runtime constraints.

## Inputs and prerequisites

Inspect repository structure, language and framework versions, existing conventions, tests, configuration, and requested behavior. Clarify only blockers that change the design.

## Procedure

1. Inspect relevant files before proposing changes. Do not assume repository structure or framework version.
2. Trace current behavior and identify the smallest correct change.
3. Define the contract: inputs, outputs, errors, side effects, compatibility, and acceptance criteria.
4. Check security, authorization, validation, concurrency, resource limits, and failure behavior.
5. Implement using existing project conventions. Avoid unnecessary abstractions and dependency additions.
6. Add or update tests for normal paths, boundary conditions, and failures.
7. Run relevant tests, linters, type checks, and build commands when available. Report commands and actual results.
8. Review the diff for unrelated changes, secrets, unsafe defaults, and accidental API changes.
9. For production-impacting changes, provide rollout, observability, and rollback steps.

## Evidence requirements

Use source code, tests, lockfiles, generated schemas, runtime output, and official version-specific documentation. Do not invent APIs or claim compatibility without checking.

## Output contract

Summarize changed behavior, files changed, tests actually run, compatibility considerations, risks, and rollout/rollback when relevant.

## Failure modes and abstention

Do not edit when target behavior is unclear and a wrong interpretation could cause data loss, security exposure, or breaking changes. Do not claim a test passed if it was not run. Do not hide incomplete work.

## Validation checklist

- [ ] Existing code and conventions were inspected.
- [ ] Scope is limited to requested behavior.
- [ ] Error and boundary cases are covered.
- [ ] Tests were run or the reason they could not run is stated.
- [ ] Security and operational consequences were reviewed.
