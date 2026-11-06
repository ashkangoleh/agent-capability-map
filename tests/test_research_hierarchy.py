"""Research & Communication hierarchical registry and routing contract checks."""
import tempfile
import unittest
from pathlib import Path
from capability_map import Router
from capability_map.router import load_yaml

ROOT = Path(__file__).resolve().parents[1]

class ResearchHierarchyTests(unittest.TestCase):
    def test_structure_preserves_two_original_skill_ids(self):
        graph=load_yaml(ROOT,"domains/research/map.yaml")
        self.assertEqual(len(graph["children"]),8)
        seen=[]
        for group in graph["children"]:
            self.assertEqual(group["status"],"active")
            self.assertTrue((ROOT/"domains"/"research"/group["id"]/"ROLE.md").is_file())
            sub=load_yaml(ROOT,group["map"])
            for leaf in sub["children"]:
                self.assertTrue((ROOT/"domains"/"research"/group["id"]/leaf["id"]/"ROLE.md").is_file())
                registry=load_yaml(ROOT,leaf["skills"])
                self.assertEqual(len(registry["skills"]),1)
                item=registry["skills"][0]
                self.assertTrue((ROOT/item["path"]).is_file())
                seen.append(item["id"])
        self.assertEqual(len(seen),22)
        self.assertEqual(len(set(seen)),22)
        self.assertIn("evidence-research",seen)
        self.assertIn("technical-writing-docs",seen)
        self.assertEqual(Router(ROOT).validate()["status"],"valid")

    def test_specialists_routing(self):
        cases=[
            ("research primary source triangulation independence review", "research-primary-source-triangulation"),
            ("research contradictory evidence adjudication primary studies", "research-conflicting-evidence-adjudication"),
            ("research evidence claim citation provenance ledger", "research-claim-to-source-traceability"),
            ("research systematic review prisma search screening reproducibility", "research-systematic-review-reporting"),
            ("research scholarly citation doi crossref retraction validation", "research-scholarly-doi-metadata-integrity"),
            ("research study protocol reproducibility artifact versioning", "research-protocol-reproducibility-review"),
            ("research technical api reference openapi code contract docs", "research-api-reference-documentation"),
            ("research technical operational runbook incident recovery procedure", "research-operational-runbook-recovery"),
            ("research technical docs version consistency link example checks", "research-documentation-version-qa"),
            ("research technical rfc proposal alternatives tradeoffs requirements", "research-rfc-proposal-tradeoff-review"),
            ("research technical adr decision rationale superseded architecture", "research-adr-decision-traceability"),
            ("research technical translation semantic fidelity glossary rtl", "research-technical-translation-fidelity"),
            ("research technical copyedit correctness terminology change control", "research-technical-copyedit-precision"),
            ("research executive evidence brief decisions confidence assumptions", "research-executive-evidence-brief"),
            ("research chart claim integrity denominator axes uncertainty audit", "research-visual-claim-integrity"),
            ("research technical presentation source trace slide narrative", "research-technical-presentation-evidence"),
            ("research contributor credit conflict interest authorship CRediT", "research-contributor-credit-coi"),
            ("research ai generated citation hallucination provenance audit", "research-ai-generated-citation-audit"),
            ("research knowledge base documentation source freshness ownership", "research-knowledge-base-source-curation"),
            ("research handoff evidence package reproducibility stakeholders", "research-handoff-reproducible-findings"),
        ]
        for prompt,skill in cases:
            with self.subTest(skill=skill):
                found=Router(ROOT).resolve(prompt)
                self.assertEqual(found["status"],"matched",found)
                self.assertEqual(found.get("selected_skill"),skill,found)
                self.assertEqual(found["route"][0],"research")
                self.assertEqual(len(found["role_paths"]),len(found["route"]))

    def test_old_and_cross_domain_regressions(self):
        cases=[
            ("Fact check this evidence claim","evidence-research"),
            ("Write documentation","technical-writing-docs"),
            ("Prepare a content strategy editorial brief for a product launch","content-editorial-brief"),
            ("Audit technical SEO canonical tags","seo-audit-strategy"),
            ("Create marketing campaign strategy","marketing-strategy-campaign"),
            ("Write a product PRD","product-discovery-prd"),
        ]
        for request,skill in cases:
            with self.subTest(skill=skill):
                self.assertEqual(Router(ROOT).resolve(request).get("selected_skill"),skill)

    def test_user_selection_denies_research(self):
        with tempfile.TemporaryDirectory() as temp:
            home=Path(temp)
            conf=home/".config"/"agent-capability-map"
            conf.mkdir(parents=True)
            (conf/"domains.yaml").write_text("schema_version: 1\ndomains:\n  - seo\n",encoding="utf-8")
            result=Router(ROOT,home=home).resolve("research scholarly citation doi crossref retraction validation")
            self.assertEqual(result["status"],"domain_not_enabled",result)
            self.assertNotIn("role_paths",result)

if __name__ == "__main__":
    unittest.main()
