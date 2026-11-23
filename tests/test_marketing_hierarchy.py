"""Marketing specialist catalog structure and controlled activation checks."""
import unittest
from pathlib import Path

from capability_map import Router
from capability_map.router import load_yaml

ROOT = Path(__file__).resolve().parents[1]


class MarketingHierarchyTests(unittest.TestCase):
    def test_domain_hierarchy_and_source_ids(self):
        root = load_yaml(ROOT, "domains/marketing/map.yaml")
        self.assertEqual(len(root["children"]), 7)
        actual = []
        for group in root["children"]:
            self.assertEqual(group["status"], "active")
            sub = load_yaml(ROOT, group["map"])
            self.assertEqual(sub["id"], group["id"])
            self.assertTrue((ROOT / "domains" / "marketing" / group["id"] / "ROLE.md").is_file())
            for leaf in sub["children"]:
                self.assertEqual(leaf["status"], "active")
                role = ROOT / "domains" / "marketing" / group["id"] / leaf["id"] / "ROLE.md"
                self.assertTrue(role.is_file(), role)
                registry = load_yaml(ROOT, leaf["skills"])
                self.assertEqual(len(registry["skills"]), 1)
                skill = registry["skills"][0]
                actual.append(skill["id"])
                self.assertTrue((ROOT / skill["path"]).is_file())
        self.assertEqual(len(actual), 17)
        self.assertEqual(len(set(actual)), 17)
        self.assertIn("marketing-strategy-campaign", actual)
        self.assertIn("marketing-measurement-attribution", actual)

    def test_exact_specialist_routes(self):
        cases = [
        [
                "marketing launch readiness dependency gate",
                "marketing-launch-readiness"
        ],
        [
                "marketing paid media spend pacing budget guardrails",
                "marketing-spend-pacing"
        ],
        [
                "marketing creative randomized experiment contamination",
                "marketing-creative-experimentation"
        ],
        [
                "marketing landing page conversion qa checkout funnel",
                "marketing-landing-page-conversion-qa"
        ],
        [
                "marketing audience research sampling bias segmentation",
                "marketing-audience-research-evidence"
        ],
        [
                "marketing brand positioning claim substantiation message test",
                "marketing-brand-message-validation"
        ],
        [
                "marketing crm consent suppression unsubscribe preference audit",
                "marketing-consent-suppression"
        ],
        [
                "marketing lifecycle journey holdout retention experiment",
                "marketing-lifecycle-journey-holdouts"
        ],
        [
                "marketing email sender reputation spf dkim dmarc unsubscribe",
                "marketing-email-deliverability"
        ],
        [
                "marketing geo lift incrementality holdout design",
                "marketing-incrementality-geo-lift"
        ],
        [
                "marketing offline conversion upload dedup reconciliation",
                "marketing-offline-conversion-reconciliation"
        ],
        [
                "marketing influencer paid endorsement disclosure review",
                "marketing-creator-disclosure-review"
        ],
        [
                "marketing affiliate payout attribution fraud reconciliation",
                "marketing-affiliate-payout-integrity"
        ],
        [
                "marketing campaign taxonomy utm governance audit",
                "marketing-campaign-taxonomy-utm"
        ],
        [
                "marketing campaign release preflight checklist approvals",
                "marketing-campaign-release-controls"
        ]
]
        router = Router(ROOT)
        for request, skill_id in cases:
            with self.subTest(skill=skill_id):
                result = router.resolve(request)
                self.assertEqual(result["status"], "matched", result)
                self.assertEqual(result.get("selected_skill"), skill_id, result)
                self.assertEqual(result["route"][0], "marketing")
                self.assertEqual(len(result["role_paths"]), len(result["route"]), result)

    def test_historical_skills_and_seo_boundary(self):
        cases = [
            ("Create marketing campaign strategy", "marketing-strategy-campaign"),
            ("Implement GA4 event tracking for marketing conversions", "marketing-measurement-attribution"),
            ("Audit technical SEO canonical tags", "seo-audit-strategy"),
            ("Write a product PRD", "product-discovery-prd"),
        ]
        router = Router(ROOT)
        for request, expected in cases:
            with self.subTest(request=request):
                result = router.resolve(request)
                self.assertEqual(result.get("selected_skill"), expected, result)


if __name__ == "__main__":
    unittest.main()
