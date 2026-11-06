"""Content and Publishing hierarchy, canonical preservation and routing regression."""
import tempfile
import unittest
from pathlib import Path

from capability_map import Router
from capability_map.router import load_yaml

ROOT = Path(__file__).resolve().parents[1]

class ContentHierarchyTests(unittest.TestCase):
    def test_hierarchy_and_canonical_skills(self):
        graph=load_yaml(ROOT,"domains/content/map.yaml")
        self.assertEqual(len(graph["children"]),9)
        ids=[]
        for group in graph["children"]:
            self.assertEqual(group["status"],"active")
            self.assertTrue((ROOT/"domains"/"content"/group["id"]/"ROLE.md").is_file())
            sub=load_yaml(ROOT,group["map"])
            for leaf in sub["children"]:
                self.assertTrue((ROOT/"domains"/"content"/group["id"]/leaf["id"]/"ROLE.md").is_file())
                registry=load_yaml(ROOT,leaf["skills"])
                self.assertEqual(len(registry["skills"]),1)
                entry=registry["skills"][0]
                ids.append(entry["id"])
                self.assertTrue((ROOT/entry["path"]).is_file())
        self.assertEqual(len(ids),22)
        self.assertEqual(len(set(ids)),22)
        self.assertIn("content-editorial-brief",ids)
        self.assertEqual(Router(ROOT).validate()["status"],"valid")

    def test_new_content_specialist_activation(self):
        cases=[
            ("content publishing editorial calendar portfolio prioritization", "content-editorial-calendar-governance"),
            ("content publishing audience evidence research brief", "content-audience-research-brief"),
            ("content publishing audience first copywriting clarity", "content-audience-first-copywriting"),
            ("content publishing claims substantiation public copy", "content-claims-substantiation"),
            ("content publishing editorial fact check source ledger", "content-fact-check-source-ledger"),
            ("content publishing editorial correction retraction process", "content-corrections-retractions"),
            ("content publishing source attribution quotation integrity", "content-source-attribution-integrity"),
            ("content publishing social channel editorial adaptation", "content-social-platform-adaptation"),
            ("content publishing social community moderation escalation", "content-community-moderation-playbook"),
            ("content publishing podcast rss feed artwork episode validation", "content-podcast-rss-production"),
            ("content publishing video captions transcript accessibility review", "content-audio-video-caption-qa"),
            ("content publishing podcast measurement IAB downloads dedup", "content-podcast-metric-integrity"),
            ("content publishing multilingual translation localization QA", "content-translation-localization-qa"),
            ("content publishing cultural inclusion language sensitivity review", "content-cultural-inclusion-review"),
            ("content publishing cms release schedule rollback editorial", "content-cms-release-rollback"),
            ("content publishing article lifecycle archive update retire", "content-lifecycle-update-retire"),
            ("content publishing newsletter editorial issue qa", "content-newsletter-editorial-qa"),
            ("content publishing accessible article headings tables language", "content-article-structure-accessibility"),
            ("content publishing image alt text decorative chart accessibility", "content-image-alt-text-decisions"),
            ("content publishing media license attribution clearance", "content-media-license-clearance"),
            ("content publishing AI origin provenance human review", "content-ai-origin-disclosure"),
        ]
        for request,skill in cases:
            with self.subTest(skill=skill):
                result=Router(ROOT).resolve(request)
                self.assertEqual(result["status"],"matched",result)
                self.assertEqual(result.get("selected_skill"),skill,result)
                self.assertEqual(result["route"][0],"content")
                self.assertEqual(len(result["role_paths"]),len(result["route"]))

    def test_historical_and_cross_domain_regressions(self):
        cases=[
            ("Prepare a content strategy editorial brief for a product launch","content-editorial-brief"),
            ("Create marketing campaign strategy","marketing-strategy-campaign"),
            ("Audit technical SEO canonical tags","seo-audit-strategy"),
            ("Write a product PRD","product-discovery-prd"),
        ]
        for request,skill in cases:
            with self.subTest(skill=skill):
                self.assertEqual(Router(ROOT).resolve(request).get("selected_skill"),skill)

    def test_scope_denies_content_when_only_seo_enabled(self):
        with tempfile.TemporaryDirectory() as tmp:
            home=Path(tmp)
            config=home/".config"/"agent-capability-map"
            config.mkdir(parents=True)
            (config/"domains.yaml").write_text("schema_version: 1\ndomains:\n  - seo\n",encoding="utf-8")
            out=Router(ROOT,home=home).resolve("content publishing media license attribution clearance")
            self.assertEqual(out["status"],"domain_not_enabled",out)
            self.assertNotIn("role_paths",out)

if __name__ == "__main__":
    unittest.main()
