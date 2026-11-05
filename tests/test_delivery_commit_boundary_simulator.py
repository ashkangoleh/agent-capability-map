"""Deterministic synthetic commit-boundary counterexample tests."""
import subprocess
import sys
import unittest
from pathlib import Path

from capability_map import Router

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/".agents/skills/data/data-engineering/streaming/end-to-end-delivery-semantics"


class CommitBoundarySimulatorTests(unittest.TestCase):
    def test_ack_before_sink_commit_loses_event(self):
        from importlib.util import spec_from_file_location, module_from_spec
        spec=spec_from_file_location("delivery_model", BASE/"scripts/commit_boundary_simulator.py")
        mod=module_from_spec(spec)
        spec.loader.exec_module(mod)
        r=mod.simulate("ack_before_write",False)
        self.assertTrue(r["lost"])
        self.assertEqual(r["sink_effect_count"],0)
        self.assertFalse(r["actual_end_to_end_exactly_once_verified"])

    def test_sink_before_ack_replay_duplicate_without_idempotency(self):
        from importlib.util import spec_from_file_location, module_from_spec
        spec=spec_from_file_location("delivery_model", BASE/"scripts/commit_boundary_simulator.py")
        mod=module_from_spec(spec)
        spec.loader.exec_module(mod)
        r=mod.simulate("write_before_ack",False)
        self.assertTrue(r["duplicate_effects"])
        self.assertEqual(r["sink_effect_count"],2)

    def test_idempotent_sink_only_models_one_effect(self):
        from importlib.util import spec_from_file_location, module_from_spec
        spec=spec_from_file_location("delivery_model", BASE/"scripts/commit_boundary_simulator.py")
        mod=module_from_spec(spec)
        spec.loader.exec_module(mod)
        r=mod.simulate("write_before_ack",True)
        self.assertEqual(r["sink_effect_count"],1)
        self.assertFalse(r["actual_end_to_end_exactly_once_verified"])

    def test_skill_route_canonical(self):
        r=Router(ROOT).resolve("Explain end to end exactly once semantics across a sink")
        self.assertEqual(r["selected_skill"],"end-to-end-delivery-semantics",r)


if __name__=="__main__":
    unittest.main()
