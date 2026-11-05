"""One-skill production-depth regression for Iceberg maintenance (no live Spark)."""

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from capability_map import Router
from capability_map.router import load_yaml

ROOT = Path(__file__).resolve().parents[1]
FOLDER = ROOT / ".agents/skills/data/data-engineering/lakehouse/iceberg/iceberg-compaction-retention"
SCRIPT = FOLDER / "scripts/check_plan.py"


class IcebergMaintenanceSkillTests(unittest.TestCase):
    def run_plan(self, plan):
        with tempfile.TemporaryDirectory() as temp:
            p = Path(temp) / "plan.json"
            p.write_text(json.dumps(plan), encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(SCRIPT), "--plan", str(p)],
                capture_output=True, text=True, timeout=15, check=False
            )
            return result.returncode, json.loads(result.stdout)

    def plan(self):
        return json.loads((FOLDER / "examples/preflight_plan.json").read_text(encoding="utf-8"))

    def test_existing_route_and_skill_id_unchanged(self):
        registry = load_yaml(ROOT, "domains/data/data-engineering/lakehouse/iceberg/skills.yaml")
        item = next(s for s in registry["skills"] if s["id"] == "iceberg-compaction-retention")
        self.assertEqual(item["path"], (FOLDER / "SKILL.md").relative_to(ROOT).as_posix())
        r = Router(ROOT).resolve("Plan Iceberg compaction and snapshot expiration")
        self.assertEqual(r["status"], "matched", r)
        self.assertEqual(r["selected_skill"], "iceberg-compaction-retention", r)
        self.assertEqual(r["route"][:4], ["data", "data-engineering", "lakehouse", "iceberg"])

    def test_skill_uses_on_demand_resources_and_readonly_script(self):
        skill = (FOLDER / "SKILL.md").read_text(encoding="utf-8")
        for rel in (
            "references/operations.md", "references/failure-recovery.md",
            "examples/preflight_plan.json", "examples/spark_maintenance.sql",
            "scripts/check_plan.py",
        ):
            self.assertIn(rel, skill)
            self.assertTrue((FOLDER / rel).is_file())
        self.assertLess(len(skill.splitlines()), 500)
        script = SCRIPT.read_text(encoding="utf-8")
        self.assertNotIn("subprocess.", script)
        self.assertNotIn("os.system(", script)

    def test_valid_plan_never_returns_execution_permission(self):
        code, report = self.run_plan(self.plan())
        self.assertEqual(code, 0, report)
        self.assertEqual(report["status"], "manual_review_required")
        self.assertIs(report["can_execute"], False)

    def test_retention_floor_violation_is_rejected(self):
        plan = self.plan()
        plan["retention"]["planned_retention_days"] = 3
        code, report = self.run_plan(plan)
        self.assertEqual(code, 1, report)
        self.assertIn("planned_retention_days violates", " ".join(report["errors"]))

    def test_orphan_cleanup_must_be_dry_run_and_older_than_writers(self):
        plan = self.plan()
        plan["operation"] = "remove_orphan_files"
        plan["parameters"] = {
            "dry_run": False, "path_equivalence_reviewed": False,
            "older_than_hours": 24, "safety_margin_hours": 12,
        }
        code, report = self.run_plan(plan)
        self.assertEqual(code, 1, report)
        self.assertGreaterEqual(len(report["errors"]), 3)
        plan["parameters"].update(
            dry_run=True, path_equivalence_reviewed=True, older_than_hours=72
        )
        code, report = self.run_plan(plan)
        self.assertEqual(code, 0, report)
        self.assertIs(report["can_execute"], False)

    def test_snapshot_expiry_checks_age_refs_and_legal_hold(self):
        plan = self.plan()
        plan["operation"] = "expire_snapshots"
        plan["retention"]["legal_hold"] = True
        plan["retention"]["protected_refs_reviewed"] = False
        plan["parameters"] = {
            "retain_last": 1, "older_than_utc": "2099-01-01T00:00:00Z"
        }
        code, report = self.run_plan(plan)
        self.assertEqual(code, 1, report)
        self.assertGreaterEqual(len(report["errors"]), 3)

    def test_manifest_plan_requires_spec_and_planning_evidence(self):
        plan = self.plan()
        plan["operation"] = "rewrite_manifests"
        plan["parameters"] = {"spec_id": 0, "planning_baseline_reviewed": False}
        self.assertEqual(self.run_plan(plan)[0], 1)
        plan["parameters"]["planning_baseline_reviewed"] = True
        self.assertEqual(self.run_plan(plan)[0], 0)

    def test_version_placeholders_are_rejected(self):
        plan = self.plan()
        plan["iceberg_version"] = "latest"
        self.assertEqual(self.run_plan(plan)[0], 1)
        plan["iceberg_version"] = "1.12.0"
        plan["spark_version"] = "3.5.x"
        self.assertEqual(self.run_plan(plan)[0], 1)

    def test_missing_or_invalid_snapshot_rejected(self):
        plan = self.plan()
        plan["baseline_snapshot_id"] = True
        self.assertEqual(self.run_plan(plan)[0], 1)

    def test_invalid_plan_is_not_executable(self):
        with tempfile.TemporaryDirectory() as temp:
            plan_path = Path(temp) / "bad.json"
            plan_path.write_text('{"schema_version":1,"schema_version":1}', encoding="utf-8")
            done = subprocess.run(
                [sys.executable, str(SCRIPT), "--plan", str(plan_path)],
                capture_output=True, text=True, timeout=15, check=False,
            )
            self.assertEqual(done.returncode, 1)
            self.assertFalse(json.loads(done.stdout)["can_execute"])


if __name__ == "__main__":
    unittest.main()
