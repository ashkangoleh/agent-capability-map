-- Apache Iceberg Spark SQL inspection and example procedures.
-- IMPORTANT: this file contains only read-only executable statements.
-- Replace prod.analytics.events with your **observed** catalog table.
-- Verify engine/catalog syntax and permissions before execution.

SELECT snapshot_id, committed_at, operation
FROM prod.analytics.events.snapshots
ORDER BY committed_at DESC;

SELECT name, type, snapshot_id
FROM prod.analytics.events.refs;

SELECT content, COUNT(*) AS file_count,
       MIN(file_size_in_bytes) AS minimum_file_bytes,
       MAX(file_size_in_bytes) AS maximum_file_bytes,
       AVG(file_size_in_bytes) AS average_file_bytes
FROM prod.analytics.events.files
GROUP BY content;

SELECT *
FROM prod.analytics.events.partitions
LIMIT 100;

-- MUTATIONS BELOW ARE COMMENTS ONLY. NEVER RUN AS A BATCH.
-- After approval and version-specific verification, choose exactly one.
--
-- File compaction (mutates table):
-- CALL prod.system.rewrite_data_files(
--   table => 'analytics.events',
--   strategy => 'binpack',
--   where => 'event_date = DATE ''2026-01-01''',  -- illustrative; verify real partition/filter
--   options => map('target-file-size-bytes', '536870912')
-- );
--
-- Manifest rewrite (mutates metadata):
-- CALL prod.system.rewrite_manifests(table => 'analytics.events');
--
-- Snapshot expiration (potential physical data deletion):
-- CALL prod.system.expire_snapshots(
--   table => 'analytics.events',
--   older_than => TIMESTAMP '2026-01-01 00:00:00',
--   retain_last => 30
-- );
--
-- Orphan discovery is read-only WITH dry_run => true, but requires
-- age and path-equivalence review before submitting any real CALL:
-- CALL prod.system.remove_orphan_files(
--   table => 'analytics.events',
--   older_than => TIMESTAMP '2026-01-01 00:00:00',
--   dry_run => true
-- );
--
-- Do not uncomment an operation without a separate change review.
