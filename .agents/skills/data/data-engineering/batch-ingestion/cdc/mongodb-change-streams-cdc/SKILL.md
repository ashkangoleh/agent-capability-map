---
name: mongodb-change-streams-cdc
description: Build MongoDB Change Streams ingestion with durable resume-token handling, oplog-window recovery and event-time correctness.
metadata:
  version: "1.0.0"
---

# MongoDB Change Streams CDC Engineering

## Activation boundary

Use for MongoDB change streams, change-event ingestion, resume-token recovery and collection/database/cluster-level CDC. Do not activate for standalone MongoDB polling, ordinary aggregation queries or a generic MongoDB schema review.

## Required context

Collect MongoDB server and driver versions, replica-set or sharded-cluster topology, watch scope, read preference, event filters, oplog window, pre/post-image configuration and retention, source throughput, sink commit model, consumer checkpoint store and recovery objective.

## Production procedure

1. Verify the deployment supports change streams. Change streams require a replica set or sharded cluster using WiredTiger and replica set protocol v1; a standalone server is not a valid production CDC source.
2. Select watch scope deliberately: collection, database or deployment-wide. For sharded clusters, connect through mongos. Estimate event volume and privileges before choosing a broader scope.
3. Use the driver Watch API when automatic resumability is required; MongoDB documents different resume behavior for a raw aggregate call. The $changeStream stage must be the first aggregation stage. Preserve the event document _id as the resume token and never modify or remove it in the pipeline.
4. Persist the resume token only after the corresponding sink effect is durable. If source token state and sink commit are not atomic, make the sink idempotent using document identity plus event identity and accept replay duplicates.
5. Resume with the same pipeline and options used to create the token. Use resumeAfter for normal continuation; use startAfter when restarting after an invalidate event. startAtOperationTime is an alternative starting point and is mutually exclusive with resumeAfter and startAfter.
6. Monitor the oplog history window. A resume token cannot recover an event whose associated operation has fallen out of the available oplog history; define a controlled snapshot/reconciliation path for that case.
7. Handle insert, update, replace, delete, invalidate and supported DDL/index events explicitly. Collection drop/rename can invalidate a stream and require a new watch boundary.
8. Understand update payload semantics. By default, update events provide changed-field deltas. fullDocument: updateLookup returns the current majority-committed document at lookup time and may include later interleaving writes; it is not guaranteed to be the exact post-image at the original event time.
9. If event-time pre/post images are required, verify server version support, enable changeStreamPreAndPostImages on the collection, configure whenAvailable or required semantics, and size retention/storage. Pre-images are unavailable for inserts; post-images are unavailable for deletes.
10. Account for sharded deployments, transaction metadata, event size limits, read preference changes, cursor getMore behavior, max await time and driver-specific automatic resumability. Each open stream holds a connection while waiting for events; size the connection pool for concurrent streams and monitor notification latency.
11. Reconcile source and target using resume-token progress, document keys, operation type and known source timestamps. Treat a full snapshot plus resume-token handoff as a consistency protocol, not two independent jobs.

## Failure modes and recovery

- Oplog history no longer contains the resume point: stop incremental replay and perform a documented resnapshot/reconciliation.
- Resume pipeline or options changed: do not reuse the old token with a different stream definition.
- Collection drop/rename emits invalidate: use the appropriate new stream start procedure; resumeAfter is not interchangeable with startAfter.
- updateLookup returns a later document version or null: use event deltas or configured pre/post images when event-time state is required. A pipeline that filters on fullDocument can also make resume-token lookup fail when updateLookup returns null after a delete; validate this interaction before production.
- Sink commit succeeds but token persistence fails: expect replay and deduplicate idempotently.
- Token persists before sink commit: data loss is possible; reverse the ordering or introduce a transactional outbox/checkpoint protocol.
- Broad database/cluster watches create excessive event volume or exceed operational budgets: narrow scope and filters without mutating the resume-token _id.

## Validation and acceptance

- Test insert/update/delete, multiple updates to one document, transaction events, collection invalidate, rename/drop, primary election, network interruption and driver resume.
- Test oplog-window expiry and prove the resnapshot/reconciliation procedure.
- Verify that the same stream pipeline/options are used after restart.
- Test pre/post-image availability, retention expiry and event-size limits where enabled.
- Reconcile sink state against a source snapshot and verify duplicate replay is harmless.
- Do not claim exactly-once across MongoDB and an external sink without an atomic cross-system protocol.

## Official references

- MongoDB Change Streams: https://www.mongodb.com/docs/manual/changestreams/
- Change-stream resume options and event behavior: https://www.mongodb.com/docs/manual/reference/operator/aggregation/changestream/
- Availability, connection pools, sharded behavior and resume-token handling: https://www.mongodb.com/docs/manual/changestreams/
- Update event and updateLookup semantics: https://www.mongodb.com/docs/manual/reference/change-events/update/

## Output contract

Deliver the topology and watch scope, event schema, resume-token persistence protocol, oplog and image retention requirements, sink idempotency, invalidate/re-snapshot recovery, monitoring and reproducible failure tests. Mark unverified server/driver compatibility explicitly.
