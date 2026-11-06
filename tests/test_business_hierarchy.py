"""Business & Operations structural and routing regression tests.

The tests establish deterministic registry and evidence-contract validity,
not audited financial statements or real organizational decision outcomes.
"""
import tempfile
import unittest
from pathlib import Path

from capability_map import Router
from capability_map.router import load_yaml, role_paths_for_route

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "business-strategic-market-sizing",
    "business-portfolio-investment-allocation",
    "business-unit-economics-contribution",
    "business-pricing-discount-guardrails",
    "business-revenue-cohort-retention",
    "business-budget-forecast-variance",
    "business-cash-runway-liquidity",
    "business-capital-investment-appraisal",
    "business-bpmn-process-boundaries",
    "business-process-bottleneck-recovery",
    "business-decision-rules-dmn",
    "business-capacity-queue-staffing",
    "business-operating-kpi-scorecard",
    "business-continuity-response-drill",
    "business-risk-register-treatment",
    "business-control-assurance-three-lines",
    "business-procurement-supplier-selection",
    "business-supplier-performance-resilience",
    "business-partnership-viability-economics",
    "business-commercial-contract-obligations",
    "business-sensitivity-scenario-comparison",
    "business-policy-rule-approval-trace",
    "business-change-rollout-adoption",
    "business-operating-review-cadence",
}


class BusinessHierarchyTests(unittest.TestCase):
    def test_hierarchy_and_route_integrity(self):
        root = load_yaml(ROOT, "domains/business/map.yaml")
        self.assertEqual(len(root["children"]), 10)
        seen = set()
        for group in root["children"]:
            self.assertEqual(group["status"], "active")
            g = group["id"]
            self.assertTrue((ROOT / "domains" / "business" / g / "ROLE.md").is_file())
            sub = load_yaml(ROOT, group["map"])
            for leaf in sub["children"]:
                self.assertEqual(leaf["status"], "active")
                lid = leaf["id"]
                self.assertTrue((ROOT / "domains" / "business" / g / lid / "ROLE.md").is_file())
                doc = load_yaml(ROOT, leaf["skills"])
                self.assertEqual(len(doc["skills"]), 1)
                skill = doc["skills"][0]
                self.assertNotIn(skill["id"], seen, "duplicate skill ID")
                seen.add(skill["id"])
                self.assertTrue((ROOT / skill["path"]).is_file())
                route = ["business", g, lid]
                paths = role_paths_for_route(ROOT, route)
                self.assertEqual(len(paths), 3)
                self.assertTrue(paths[-1].endswith(f"/{lid}/ROLE.md"))
        self.assertEqual(len(seen), 25)
        self.assertEqual(seen - {"business-strategy-analysis"}, EXPECTED)
        self.assertEqual(Router(ROOT).validate()["status"], "valid")

    def test_all_specialists_have_exact_positive_route(self):
        root = load_yaml(ROOT, "domains/business/map.yaml")
        cases = []
        for group in root["children"]:
            sub = load_yaml(ROOT, group["map"])
            for leaf in sub["children"]:
                skill = load_yaml(ROOT, leaf["skills"])["skills"][0]
                if skill["id"] == "business-strategy-analysis":
                    continue
                cases.append((skill["triggers"][0], skill["id"], group["id"], leaf["id"]))
        self.assertEqual(len(cases), 24)
        router = Router(ROOT)
        for request, skill, group, leaf in cases:
            with self.subTest(skill=skill):
                result = router.resolve(request)
                self.assertEqual(result["status"], "matched", result)
                self.assertEqual(result.get("selected_skill"), skill, result)
                self.assertEqual(result["route"], ["business", group, leaf], result)
                self.assertEqual(len(result.get("role_paths", [])), 3, result)

    def test_legacy_business_and_cross_domain_regressions(self):
        cases = [
            ("Compare a business case with unit economics", "business-strategy-analysis"),
            ("Create marketing campaign strategy", "marketing-strategy-campaign"),
            ("Audit technical SEO canonical tags", "seo-audit-strategy"),
            ("Prepare a content strategy editorial brief for a product launch", "content-editorial-brief"),
            ("Fact check this evidence claim", "evidence-research"),
            ("Write a product PRD", "product-discovery-prd"),
        ]
        router = Router(ROOT)
        for prompt, skill in cases:
            with self.subTest(prompt=prompt):
                result = router.resolve(prompt)
                self.assertEqual(result.get("selected_skill"), skill, result)

    def test_domain_selection_fail_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp)
            conf = home / ".config" / "agent-capability-map"
            conf.mkdir(parents=True)
            (conf / "domains.yaml").write_text(
                "schema_version: 1\ndomains:\n  - seo\n",
                encoding="utf-8",
            )
            result = Router(ROOT, home=home).resolve(
                "business operations procurement supplier total cost bid evaluation"
            )
            self.assertEqual(result["status"], "domain_not_enabled", result)
            self.assertNotIn("role_paths", result)

    def test_unmatched_business_does_not_invent_a_skill(self):
        output = Router(ROOT).resolve("unrelated blue moon widget event")
        self.assertIn(output["status"], ("unmatched", "needs_clarification"))
        self.assertNotIn("selected_skill", output)


if __name__ == "__main__":
    unittest.main()
