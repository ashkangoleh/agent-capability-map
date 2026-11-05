# Bounded delivery-commit failure experiment

This small state machine models one event with one crash. It is **not** a broker emulator, a connector integration test, or proof of an end-to-end guarantee. Test cases are intended to falsify unsafe assumptions, not certify exactly-once delivery.

| Commit ordering | Sink idempotent? | Expected modeled result | Why |
|---|---|---|---|
| Source ack, crash, no sink write | Either | Lost event | Source position advanced before durable sink effect |
| Sink write, crash before source ack | No | Duplicate effect after replay | Two sink writes represent one source event |
| Sink write, crash before source ack | Yes | One effect | Modeled stable idempotency key suppresses duplicate effect |

Run from the skill directory with Python 3.10+ if available:

```bash
python scripts/commit_boundary_simulator.py --order ack_before_write
python scripts/commit_boundary_simulator.py --order write_before_ack
python scripts/commit_boundary_simulator.py --order write_before_ack --idempotent-sink
```

For a real pipeline, this is insufficient: verify source replay horizon, transaction coordinator, sink commit/label state, checkpoint persistence, event identity across partition/schema changes, consumer rebalance and external side effects. End-to-end exactly-once is a composite source+processor+sink contract, not a successful simulator output.

Official basis:
- https://kafka.apache.org/design/
- https://nightlies.apache.org/flink/flink-docs-stable/docs/learn-flink/fault_tolerance/
