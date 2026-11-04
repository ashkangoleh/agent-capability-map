---
name: data-access-control-masking
description: "Enforce data classification and least-privilege access at query, catalog and object-storage layers."
metadata:
  version: "1.0.0"
---

# data-access-control-masking

## Activation boundary
Enforce data classification and least-privilege access at query, catalog and object-storage layers.

## Required context
Classification, identities, policy engine, query engines, object storage, service accounts and audit.

## Production procedure
1. Identify producer/consumer owners, data purpose, classification and metadata source of truth.
2. Define versioned contracts for schema, semantics, quality, freshness, access and lifecycle.
3. Enforce identity and row/column controls at query and storage boundaries.
4. Capture lineage and mark inferred/incomplete metadata honestly.
5. Test policy bypass, revoked access, retention expiry and deletion propagation.

## Failure modes and recovery
- Validate the complete source-to-sink or control-plane boundary; component-level success is not an end-to-end guarantee.
- Verify partial commits, duplicate/replay behavior, schema drift, concurrency and rollback limits.
- Do not disable security controls or claim unverified exactly-once, atomicity or performance.

## Validation and acceptance
- Verify deployed versions and exact connector/engine compatibility against primary documentation.
- Test representative success, duplicate/replay, schema evolution and partial-failure recovery.
- Record ownership, monitoring, rollback and unresolved assumptions.

## Official or primary references
- https://ranger.apache.org/
- https://trino.io/docs/current/security/file-system-access-control.html

## Output contract
Deliver the requested implementation or diagnosis with explicit assumptions, version constraints, failure semantics and reproducible validation. Do not fabricate benchmarks, APIs or test results.
