"""Structural evidence audit for all canonical skills; never a production-quality certificate."""
import argparse
import json
import re
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
BASE = Path(".agents/skills")
CONTRACT = Path("references/acceptance-and-recovery.md")
CANONICAL = "catalog/master-skill-ids.yaml"
DOMAINS = "catalog/root.yaml"
PROFILES = "catalog/cross-domain-verification-profiles.json"


def audit(root=ROOT):
    root = Path(root).resolve()
    profiles = json.loads((root / PROFILES).read_text(encoding="utf-8"))["profiles"]
    expected = set(yaml.safe_load((root / CANONICAL).read_text(encoding="utf-8"))["ids"])
    domains = {n["id"] for n in yaml.safe_load((root / DOMAINS).read_text(encoding="utf-8"))["children"]}
    paths = sorted((root / BASE).rglob("SKILL.md"))
    rows, problems = [], []
    by_domain = defaultdict(lambda: {"skills": 0, "references": 0, "source_urls_missing": 0})
    for file in paths:
        relative = file.relative_to(root / BASE)
        dom = relative.parts[0]
        skill_id = file.parent.name
        is_data_engineering = relative.parts[:2] == ("data", "data-engineering")
        text = file.read_text(encoding="utf-8")
        supplement = file.parent / CONTRACT
        doc = supplement.read_text(encoding="utf-8") if supplement.is_file() else ""
        errors = []
        if not text.startswith("---\n") or "\n---\n" not in text:
            errors.append("missing YAML frontmatter")
        else:
            try:
                metadata = yaml.safe_load(text.split("---", 2)[1])
                if not isinstance(metadata, dict) or metadata.get("name") != skill_id:
                    errors.append("canonical skill name mismatch")
                if not isinstance(metadata.get("description"), str) or not metadata["description"].strip():
                    errors.append("missing skill description")
            except yaml.YAMLError:
                errors.append("invalid YAML frontmatter")
        if dom not in domains:
            errors.append("skill domain not in master catalog")
        if not supplement.is_file():
            errors.append("missing acceptance-and-recovery reference")
        if str(CONTRACT).replace("\\", "/") not in text:
            errors.append("SKILL.md does not link reference")
        if not re.search(r"## (Independent specialist evaluation|Independent operational verification)", text):
            errors.append("missing explicit activation of evaluation contract")
        if len(text.splitlines()) > 500:
            errors.append("SKILL.md over 500 lines")
        if len(text.encode("utf-8")) > 65536 or len(doc.encode("utf-8")) > 65536:
            errors.append("main skill or supplemental contract exceeds 64 KiB")
        if not is_data_engineering:
            segment = "/".join(relative.parts[1:-2])
            options = [
                k for k in profiles if k == dom or
                (k.startswith(dom + "/") and
                 (segment == k[len(dom)+1:] or segment.startswith(k[len(dom)+1:] + "/")))
            ]
            key = max(options, key=len) if options else None
            if not key:
                errors.append("no matching domain review policy")
            else:
                for prop in ("challenge", "oracle", "stop"):
                    if profiles[key].get(prop, "") not in doc:
                        errors.append(f"supplement lacks profile {prop}")
            if not all(marker in doc for marker in ("## Acceptance evidence ledger", "## Starting sources")) and                not all(marker in doc for marker in ("## Evidence ledger", "## Original references")):
                errors.append("missing evidence and source provenance sections")
        elif not ("##" in doc and "acceptance" in doc.lower() and "recover" in doc.lower()):
            errors.append("Data Engineering supplement lacks acceptance/recovery detail")
        url_count = len(re.findall(r"https?://", text))
        by_domain[dom]["skills"] += 1
        by_domain[dom]["references"] += int(supplement.is_file())
        by_domain[dom]["source_urls_missing"] += int(url_count == 0)
        if errors:
            problems.append({"id": skill_id, "path": file.relative_to(root).as_posix(), "errors": errors})
        rows.append({"id": skill_id, "domain": dom, "path": file.relative_to(root).as_posix(),
                     "reference": supplement.relative_to(root).as_posix(), "problems": errors})
    ids = {row["id"] for row in rows}
    if ids != expected:
        problems.append({"id": "canonical-index", "errors": [
            f"missing canonical IDs: {sorted(expected - ids)[:12]}",
            f"unexpected IDs: {sorted(ids - expected)[:12]}",
        ]})
    if len(rows) != len(ids):
        problems.append({"id": "duplicate-file-ids", "errors": ["multiple skill files share a canonical name"]})
    roles = len(list((root / "domains").rglob("ROLE.md")))
    return {
        "scope": "STRUCTURAL_L1_ONLY",
        "domains": len(domains), "skills": len(rows), "roles": roles,
        "referenced_skills": sum(x["references"] for x in by_domain.values()),
        "canonical_ids": len(expected),
        "review_profiles": len(profiles),
        "per_domain": dict(sorted(by_domain.items())),
        "problems": problems,
        "host_task_quality": "NOT_VERIFIED",
        "all_release_specific_sources": "NOT_VERIFIED",
        "integration_and_regulatory_qualification": "NOT_VERIFIED",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--summary", action="store_true")
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    report = audit(args.root)
    if args.summary:
        report.pop("per_domain")
    print(json.dumps(report, indent=2))
    if args.strict and (report["domains"] != 41 or report["skills"] != 537 or
                        report["referenced_skills"] != 537 or report["problems"]):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
