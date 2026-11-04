---
name: data-access-control-masking
description: "Enforce data classification and least-privilege access across catalog, warehouse, query, pipeline and object-storage layers."
license: Proprietary
metadata:
  version: "1.1.0"
---

# data-access-control-masking

## Activation boundary
Use for data platform authorization and masking. Catalog permissions do not automatically protect direct object-store access or copied extracts.

## Required context
Classification; identities/workload principals; systems; groups; row/column policy; encryption/KMS; object storage; audit and emergency access.

## Production procedure
1. Inventory every access path: SQL, direct storage, APIs, exports, notebooks, service accounts and catalog APIs.
2. Classify sensitive fields/datasets and assign owners and approved purposes.
3. Define federation and workload identities; avoid shared long-lived credentials.
4. Apply least-privilege RBAC/ABAC at each enforcement layer, including row filters, masking, tokenization and object policy.
5. Separate pipeline write privileges from analyst read and admin privileges.
6. Protect secrets/keys; define rotation, revocation, break-glass and audit retention.
7. Propagate classification to derived datasets and extracts.
8. Test access using real non-admin identities and verify denied paths.

## Failure modes and recovery
- Direct object-store bypass: restrict bucket/prefix access or use credential vending.
- Overbroad service account: scope roles and rotate credentials.
- Masking inconsistency: test every query engine/export path.
- Revocation lag: measure token/session lifetime and terminate sessions where required.
- Sensitive values in logs: redact payloads.

## Validation and acceptance
- Run positive/negative access tests for user, analyst, engineer and pipeline identities.
- Test row/column policy, export, API, object store, expiry and revocation.
- Verify audit events contain principal, asset, action and timestamp.
- Confirm derived outputs preserve classification and retention.

## Output contract
Return access matrix, enforcement map, masking policy, key/secret lifecycle, audit evidence and bypass risks.

## Official or primary references
- https://ranger.apache.org/
- https://trino.io/docs/current/security/file-system-access-control.html
