"""SEO hierarchical skills and backwards compatible routing."""
import unittest
from pathlib import Path
from capability_map import Router
from capability_map.router import load_yaml

ROOT=Path(__file__).resolve().parents[1]

class SEOHierarchyTests(unittest.TestCase):
    def test_paths_and_ids(self):
        top=load_yaml(ROOT,"domains/seo/map.yaml")
        self.assertEqual(len(top["children"]),9)
        collected=[]
        for group in top["children"]:
            self.assertTrue((ROOT/"domains"/"seo"/group["id"]/"ROLE.md").is_file())
            sub=load_yaml(ROOT,group["map"])
            for leaf in sub["children"]:
                self.assertTrue((ROOT/"domains"/"seo"/group["id"]/leaf["id"]/"ROLE.md").is_file())
                registry=load_yaml(ROOT,leaf["skills"])
                self.assertEqual(len(registry["skills"]),1)
                s=registry["skills"][0]
                self.assertTrue((ROOT/s["path"]).is_file())
                collected.append(s["id"])
        self.assertEqual(len(collected),22)
        self.assertEqual(len(set(collected)),22)
        self.assertEqual(Router(ROOT).validate()["status"],"valid")

    def test_new_specialists_route(self):
        cases=[
            ("seo javascript rendered html visibility inspection", "seo-javascript-rendering"),
            ("seo site migration redirects url mapping rollback", "seo-site-migration-redirects"),
            ("seo internal link architecture orphan page audit", "seo-internal-link-architecture"),
            ("seo faceted navigation infinite urls crawl budget", "seo-faceted-navigation-controls"),
            ("seo xml sitemap lastmod canonical validation", "seo-sitemap-canonical-integrity"),
            ("seo googlebot server log verification status analysis", "seo-crawler-log-diagnostics"),
            ("seo merchant listing product price availability schema audit", "seo-merchant-listing-schema"),
            ("seo localbusiness schema opening hours location consistency", "seo-local-business-schema-truth"),
            ("seo search intent keyword to page mapping", "seo-search-intent-page-mapping"),
            ("seo people first content spam scaled content audit", "seo-people-first-content-review"),
            ("seo content cannibalization duplicate query page refresh", "seo-content-refresh-overlap-audit"),
            ("seo hreflang reciprocal alternate canonical audit", "seo-hreflang-reciprocity"),
            ("seo locale adaptive ip redirect googlebot crawl", "seo-locale-adaptive-crawl"),
            ("seo business profile accurate name address hours verification", "seo-business-profile-integrity"),
            ("seo ecommerce product variant canonical productgroup", "seo-product-variant-canonical"),
            ("seo ai overviews ai mode visibility audit", "seo-ai-search-feature-visibility"),
            ("seo search console api sampling query page reconciliation", "seo-search-console-data-quality"),
            ("seo organic traffic regression incident diagnose", "seo-organic-regression-triage"),
            ("seo change impact matched control pages test", "seo-change-impact-evaluation"),
        ]
        for prompt,skill in cases:
            with self.subTest(skill=skill):
                result=Router(ROOT).resolve(prompt)
                self.assertEqual(result["status"],"matched",result)
                self.assertEqual(result.get("selected_skill"),skill,result)
                self.assertEqual(len(result["route"]),len(result["role_paths"]))

    def test_existing_regressions(self):
        cases=[
            ("Audit technical SEO canonical tags","seo-audit-strategy"),
            ("Diagnose canonical mismatch on indexed pages","seo-indexability-diagnostics"),
            ("Validate structured data validation for product pages","seo-structured-data-validation"),
            ("Create marketing campaign strategy","marketing-strategy-campaign"),
            ("Write a product PRD","product-discovery-prd"),
        ]
        for prompt,expected in cases:
            with self.subTest(prompt=prompt):
                self.assertEqual(Router(ROOT).resolve(prompt).get("selected_skill"),expected)

if __name__=="__main__":
    unittest.main()
