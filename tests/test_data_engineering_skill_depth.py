"""Regression guard for 123 canonical Data Engineering specialist evidence contracts."""
import unittest
from pathlib import Path
from scripts.audit_data_engineering_skills import audit

ROOT = Path(__file__).resolve().parents[1]


class DataEngineeringSkillDepthTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = audit(ROOT)

    def test_all_123_skills_have_independent_evidence_contracts(self):
        self.assertEqual(self.report["total_skill_packages"], 123)
        self.assertEqual(self.report["verified_structural"], 123, self.report["issues"][:12])
        self.assertEqual(self.report["issues"], [])

    def test_references_match_specific_family_profile(self):
        by_id = {x["id"]: x for x in self.report["skills"]}
        for id_ in (
            "flink-checkpoint-savepoint-recovery",
            "kafka-streaming-reliability",
            "trino-federated-query-optimization",
            "starrocks-olap-warehouse-engineering",
            "iceberg-compaction-retention",
            "oracle-goldengate-cdc-operations",
        ):
            with self.subTest(id=id_):
                item = by_id[id_]
                self.assertIsNotNone(item["evidence_profile"])
                self.assertEqual(item["status"], "STRUCTURAL_GATE_PRESENT")

    def test_no_false_production_certification(self):
        self.assertEqual(self.report["all_real_engine_tests"], "NOT_VERIFIED")
        self.assertEqual(self.report["all_host_quality_ab"], "NOT_VERIFIED")
        self.assertTrue(all(item["real_engine_fault_drill"] == "NOT_VERIFIED" for item in self.report["skills"]))


if __name__ == "__main__":
    unittest.main()
