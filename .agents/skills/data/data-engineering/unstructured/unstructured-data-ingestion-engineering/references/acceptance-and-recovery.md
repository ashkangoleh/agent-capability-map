# unstructured-data-ingestion-engineering — independent acceptance and recovery

## Capability and observed inputs
Binary/text extraction and source traceability. Required context from the existing specialist: Source protocols; file types/sizes; volume; identity; metadata schema; privacy; retention; extraction requirements.

## Specialist falsification matrix
| Scenario | Action in isolated authorized test | Acceptance oracle |
|---|---|---|
| Baseline | Pin exact build, source and sink revisions, business grain and identity context; measure before/after counts, hashes, runtime and cost. | Explicitly compare a trustworthy control; unknown measurements are not PASS. |
| Fault injection | Ingest corrupt encodings, oversized documents and revoked content. | Extracted records retain provenance, access permissions and deterministic reprocessing. |
| Replay/restore | Crash after a durable handoff but before a checkpoint; resume using the same source window and verify duplicates and deletes. | Quarantine bad inputs and revoke derived outputs when source deleted. |
| Compatibility | Change one dependency/schema while holding a fixed representative fixture. | Reject silent behavior changes, unsupported APIs and lost authorization. |

## Existing risk signals requiring review
- Partial upload: reject until checksum and size match. - Parser crash: isolate per file and quarantine repeated failures. - Duplicate delivery: deduplicate by object identity/version and checksum. - Parser upgrade: reprocess raw originals into a new output version. - Sensitive data in logs: redact payloads.

## Release evidence ledger
- [ ] Installed engine, connector and catalog releases and configuration inspected; no `latest` assumption.
- [ ] Exact source revision, dataset/fixture and commands recorded if executed; mark unexecuted tests as proposed.
- [ ] Business keys, null/delete/late-event semantics and source-to-sink reconciliation verified where applicable.
- [ ] Measured fault recovery, bounded retries, capacity and cost compared with explicitly agreed SLOs.
- [ ] Rollback prerequisites, operator approval and monitoring owner assigned before any live change.
- [ ] Negative permission and untrusted-input tests done when external data/actions are in scope.

## Primary reference starting points (verify version)
- https://tika.apache.org/
- https://docs.unstructured.io/

This is a review protocol, not executed evidence or production authorization. Standalone clients do not execute scripts automatically.
