# Conservative Iceberg schema-evolution preflight

**Scope:** flat top-level schema fields, primitive types, Iceberg v1/v2 promotion checks and explicitly approved renames only. This is a preflight exercise, NOT the Apache Iceberg schema validator or a replacement for a catalog commit API. Nested structs/maps/lists, field defaults, v3+ promotions, partition-spec updates, equality-delete schemas, concurrent commits and full reader compatibility are intentionally excluded.

Run only when Python 3.10+ is available:

```bash
python scripts/check_schema_evolution.py --plan examples/schema_evolution_plan.json
```

A successful result is always `manual_review_required`, `can_execute=false`. Confirm every writer/reader version, current field-ID history, active partition specs and snapshot refs in the real catalog before authorizing DDL; the sample JSON numbers are illustrative, not environment facts.

Reference: https://iceberg.apache.org/spec/
