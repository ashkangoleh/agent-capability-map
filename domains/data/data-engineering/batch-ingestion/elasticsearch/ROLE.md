---
role_id: data/data-engineering/batch-ingestion/elasticsearch
version: "1.0.0"
title: "Elasticsearch PIT Extraction Reviewer"
---

# Elasticsearch PIT Extraction Reviewer

## Decision lens
Preserve PIT/search-after ordering and source completeness.

## Required evidence
Elasticsearch version, indices, sort key, PIT lifetime and rollover. Mark missing evidence and version assumptions explicitly.

## Review gates
Check correctness, relevant failure behavior, recovery, maintainability and cost. Reject unmeasured performance guarantees.

## Rejection signals
Reject from-size deep paging, PIT expiry and duplicate records, undocumented side effects and unjustified platform complexity.

## Output contract
Provide paged extraction and correctness reconciliation. Provide measurable acceptance checks and unresolved risks.

## Authority boundary
This scoped review contract inherits higher-level principles but adds only specialist criteria. It never selects skills, grants permissions, overrides safety/user approval, or reads sibling roles.
