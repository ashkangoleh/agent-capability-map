"""Offline single-event commit boundary simulator; NOT a Kafka/Flink guarantee tester."""
import argparse
import json


def simulate(order, idempotent_sink):
    if order not in {"ack_before_write", "write_before_ack"}:
        raise ValueError("order must be ack_before_write or write_before_ack")
    if type(idempotent_sink) is not bool:
        raise ValueError("idempotent_sink must be a boolean")
    acknowledged = False
    sink_effects = []
    trace = []
    if order == "ack_before_write":
        acknowledged = True
        trace.append("ack source offset before sink write")
        trace.append("crash before sink commit")
    else:
        sink_effects.append("event-001")
        trace.append("durable sink effect written")
        trace.append("crash before source acknowledgement")
    if not acknowledged:
        trace.append("replay event-001 from source")
        if not idempotent_sink or "event-001" not in sink_effects:
            sink_effects.append("event-001")
        acknowledged = True
        trace.append("source offset acknowledged")
    expected = 1
    actual = len(sink_effects)
    return {
        "order": order, "idempotent_sink": idempotent_sink, "trace": trace,
        "sink_effect_count": actual, "expected_effect_count": expected,
        "lost": actual < expected, "duplicate_effects": actual > expected,
        "modeled_single_event_consistent": actual == expected,
        "actual_end_to_end_exactly_once_verified": False,
        "warning": "Modeled one-event example only. Real connectors, caches, commits and external side effects are NOT tested.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--order", required=True, choices=["ack_before_write","write_before_ack"])
    parser.add_argument("--idempotent-sink", action="store_true")
    args = parser.parse_args()
    print(json.dumps(simulate(args.order, args.idempotent_sink), indent=2))


if __name__ == "__main__":
    main()
