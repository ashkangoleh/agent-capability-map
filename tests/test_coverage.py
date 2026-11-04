import unittest
from pathlib import Path

from scripts.report_coverage import compute_coverage
from capability_map.router import load_yaml

ROOT = Path(__file__).resolve().parents[1]


class CoverageReportTests(unittest.TestCase):
    def test_all_top_level_domains_have_a_real_linked_skill(self):
        report = compute_coverage(ROOT)
        self.assertEqual(report["domain_count"], 42)
        self.assertEqual(report["domains_with_active_skills"], 42)
        self.assertEqual(report["domains_without_active_skills"], [])
        self.assertGreaterEqual(report["unique_active_skills"], 59)
        self.assertEqual(report["unique_active_skills"], len(load_yaml(ROOT, "catalog/master-skill-ids.yaml")["ids"]))
        self.assertGreater(report["mapped_only_subdomain_nodes"], 0)
        self.assertEqual(len({item["id"] for item in report["domains"]}), 41)

    def test_all_reported_skills_are_unique_per_domain(self):
        report = compute_coverage(ROOT)
        for entry in report["domains"]:
            with self.subTest(domain=entry["id"]):
                self.assertEqual(
                    entry["active_skill_count"],
                    len(set(entry["active_skill_ids"])),
                )


if __name__ == "__main__":
    unittest.main()
