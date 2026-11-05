"""Offline static field-ID checks for Iceberg v1/v2 primitive schema plans."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from capability_map import Router

ROOT=Path(__file__).resolve().parents[1]
FOLDER=ROOT/".agents/skills/data/data-engineering/lakehouse/iceberg/iceberg-table-schema-partition-evolution"
SCRIPT=FOLDER/"scripts/check_schema_evolution.py"
BASE=json.loads((FOLDER/"examples/schema_evolution_plan.json").read_text(encoding="utf-8"))


class IcebergSchemaPreflightTests(unittest.TestCase):
    def run_case(self, patch=None):
        import copy
        plan=copy.deepcopy(BASE)
        if patch:
            patch(plan)
        with tempfile.TemporaryDirectory() as directory:
            path=Path(directory)/"plan.json"
            path.write_text(json.dumps(plan),encoding="utf-8")
            done=subprocess.run([sys.executable,str(SCRIPT),"--plan",str(path)],
                capture_output=True,text=True,timeout=15,check=False)
            return done.returncode,json.loads(done.stdout)

    def test_valid_example_never_authorizes_execution(self):
        code,r=self.run_case()
        self.assertEqual(code,0,r)
        self.assertEqual(r["status"],"manual_review_required")
        self.assertIs(r["can_execute"],False)

    def test_historical_id_reuse_rejected(self):
        code,r=self.run_case(lambda p:p["after"][-1].update(id=4))
        self.assertEqual(code,1)
        self.assertIn("historically"," ".join(r["issues"]))

    def test_unauthorized_rename_rejected(self):
        code,r=self.run_case(lambda p:p.update(approved_renames=[]))
        self.assertEqual(code,1)
        self.assertIn("not authorized"," ".join(r["issues"]))

    def test_type_narrowing_rejected(self):
        code,r=self.run_case(lambda p:p["after"][0].update(type="int"))
        self.assertEqual(code,1)
        self.assertIn("unsupported type change"," ".join(r["issues"]))

    def test_new_required_field_rejected(self):
        code,r=self.run_case(lambda p:p["after"][-1].update(required=True))
        self.assertEqual(code,1)
        self.assertIn("new required"," ".join(r["issues"]))

    def test_unsupported_format_version_fails_closed(self):
        code,r=self.run_case(lambda p:p.update(format_version=3))
        self.assertEqual(code,1)
        self.assertIn("v1/v2"," ".join(r["issues"]))

    def test_route_and_original_id_preserved(self):
        r=Router(ROOT).resolve("Plan Iceberg schema evolution and partition changes")
        self.assertEqual(r["status"],"matched",r)
        self.assertEqual(r["selected_skill"],"iceberg-table-schema-partition-evolution",r)


if __name__=="__main__":
    unittest.main()
