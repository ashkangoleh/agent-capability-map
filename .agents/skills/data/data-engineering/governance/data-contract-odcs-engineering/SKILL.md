---
name: data-contract-odcs-engineering
description: "Define versioned Open Data Contract Standard contracts for schema, semantics, quality, SLA, ownership, security and producer-consumer compatibility."
license: Proprietary
metadata:
  version: "1.1.1"
---

# data-contract-odcs-engineering

## Activation boundary
Use for machine-readable data contracts. A YAML contract file is not enforcement until CI/runtime components validate it.

## Required context
Producer/consumer owners; dataset/event identity; schema; semantics; quality; freshness SLO; classification; access; compatibility/deprecation policy.

## Production procedure
1. Pin ODCS specification version and validate against its matching schema.
2. Define contract identity, version, domain, owner, team, terms and authoritative contact.
3. Define schema fields with physical type, logical meaning, nullability, constraints and examples.
4. Define quality rules for completeness, uniqueness, validity, referential integrity and freshness.
5. Define SLOs, support hours, update cadence, latency and incident notification.
6. Define access, privacy, retention, usage limits and data residency.
7. Define compatibility and lifecycle states for draft, active, deprecated and retired versions.
8. Attach enforcement to producer CI, registry, ingestion tests and runtime checks; assign failure owner.

## Failure modes and recovery
- Contract exists but is unenforced: do not report compliance; add executable gates.
- Semantic ambiguity: require business definitions and examples, not only SQL types.
- Breaking change: publish a new version and use expand-contract.
- SLO not measurable: define timestamp source and missing-data behavior.
- No accountable owner: block production activation.

## Validation and acceptance
- Validate ODCS schema/version.
- Run producer and consumer tests with valid, invalid and boundary payloads.
- Verify quality/freshness rules execute in the real pipeline.
- Record version, approvals, enforcement points and violation response.

## Output contract
Return contract, version policy, executable enforcement map, owners and measurable SLOs.

## Official or primary references
- https://bitol-io.github.io/open-data-contract-standard/
- https://docs.getdbt.com/docs/mesh/govern/model-contracts

## Independent operational verification
For deployable changes and incident response, consult the [specialist recovery and falsification protocol](references/acceptance-and-recovery.md) on demand. Preserve verified runtime evidence and refuse privileged mutations without authorization.
