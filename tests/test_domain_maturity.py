"""Repository-wide domain maturity indicators without conflating structure and production proof."""
import unittest
from collections import Counter
from pathlib import Path
from scripts.audit_all_skill_evidence import audit

ROOT=Path(__file__).resolve().parents[1]


class DomainMaturityTests(unittest.TestCase):
    def test_every_domain_has_linked_l1_contract(self):
        report=audit(ROOT)
        self.assertEqual((report["domains"],report["skills"],report["referenced_skills"]),(41,513,513))
        self.assertEqual(report["problems"],[])

    def test_singleton_domains_are_explicit_breadth_gap(self):
        report=audit(ROOT)
        size={d:v["skills"] for d,v in report["per_domain"].items()}
        self.assertEqual(len([v for v in size.values() if v==1]),31)
        self.assertEqual(size["data"],186)
        self.assertEqual(size["infrastructure"],95)
        self.assertEqual(size["ai-ml"],61)
        self.assertEqual(size["software-engineering"],52)

    def test_no_structural_test_claims_host_or_regulatory_readiness(self):
        report=audit(ROOT)
        for field in ("host_task_quality","all_release_specific_sources","integration_and_regulatory_qualification"):
            self.assertEqual(report[field],"NOT_VERIFIED")


if __name__=="__main__":
    unittest.main()
