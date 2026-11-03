# Data Domain Router

Use for data platforms, pipelines, distributed processing, storage, modeling, analytics engineering, BI, data quality, and governance.

1. Read domains/data/skills.json only.
2. Pipeline implementation, batch/stream processing, SQL engines, warehouse/lakehouse, orchestration, and data reliability route to data-engineering-implementation.
3. LLM retrieval or embedding pipeline architecture routes to ai-ml unless the core task is ordinary data movement or modeling.
4. Distinguish query correctness, data correctness, and operational correctness.
5. For production pipelines, inspect source and sink semantics, idempotency, replay, backfill, late data, schema evolution, data quality, observability, and recovery.
6. Never claim exactly-once semantics without proving the end-to-end contract.

## Progressive specialization (do not preload ancestors)

- Entire PySpark read/transform/write job -> pyspark-pipelines.
- Isolated Spark join correctness, join type, plan or hint -> pyspark-joins.
- Evidence of hot keys, straggler tasks, uneven shuffle partitions -> pyspark-skew-diagnostics. If evidence is absent, call skew a hypothesis and ask for plan/metrics.
- Generic non-Spark data pipeline -> data-engineering-implementation.
- Spark cluster or Kubernetes deployment without a data pipeline deliverable -> technology/platform-operations, not a PySpark leaf skill.
- Each leaf is self-contained; parent_skill is a navigation edge, not an instruction to load all ancestors. Related skills are pointers only, never implicit activations.
