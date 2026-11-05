"""Structural Data Engineering skill-depth audit; does not certify production behavior."""
import argparse
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = Path(".agents/skills/data/data-engineering")
POLICIES = "catalog/data-engineering-verification-profiles.json"
REFERENCE = "references/acceptance-and-recovery.md"
TITLE = "## Independent operational verification"
REQUIRED_REFERENCES = ("## Specialist falsification matrix", "## Release evidence ledger")


def audit(root=ROOT):
    root = Path(root)
    policy = json.loads((root / POLICIES).read_text(encoding="utf-8"))
    if policy.get("schema_version") != 1:
        raise ValueError("Unknown Data Engineering verification-policy version")
    profiles = policy["profiles"]
    paths = sorted((root / BASE).rglob("SKILL.md"))
    report = []
    families = Counter()
    for path in paths:
        directory = path.parent
        skill = directory.name
        relative = directory.relative_to(root / BASE).as_posix()
        candidates = [name for name in profiles if relative == name or relative.startswith(name + "/")]
        matched = max(candidates, key=len) if candidates else None
        content = path.read_text(encoding="utf-8")
        ref_path = directory / REFERENCE
        doc = ref_path.read_text(encoding="utf-8") if ref_path.is_file() else ""
        errors = []
        if matched is None:
            errors.append("no evidence policy for this specialist path")
        else:
            item = profiles[matched]
            for key in ("focus", "inject", "oracle", "recover"):
                if not isinstance(item.get(key), str) or not item[key].strip():
                    errors.append(f"missing specialized {key} requirement")
            for key in ("inject", "oracle", "recover"):
                if item.get(key) and item[key] not in doc:
                    errors.append(f"verification reference lacks profile-specific {key}")
        if content.count(TITLE) != 1 or REFERENCE not in content:
            errors.append("skill does not point to the on-demand verification contract")
        if not ref_path.is_file():
            errors.append("missing on-demand verification reference")
        else:
            for heading in REQUIRED_REFERENCES:
                if heading not in doc:
                    errors.append(f"reference missing section {heading}")
            if len(doc.encode("utf-8")) > 32768:
                errors.append("reference too large for targeted loading")
            if "not executed" not in doc.lower() and "not evidence" not in doc.lower():
                errors.append("missing boundary between planned and observed tests")
        if len(content.encode("utf-8")) > 65536:
            errors.append("SKILL.md violates 64 KiB router limit")
        if not re.search(r"(?m)^name:\\s*[\"']?" + re.escape(skill) + r"[\"']?\\s*$", content):
            errors.append("skill frontmatter name does not match canonical directory")
        if not re.search(r"https?://", content):
            errors.append("skill does not cite a primary URL")
        if not re.search(r"(?im)^## (?:Production procedure|Production workflow|Procedure|Workflow|Decision procedure|Specialist workflow)", content):
            errors.append("missing explicit task procedure heading — manual audit needed")
        references = len(re.findall(r"https?://", content))
        has_script = (directory / "scripts").is_dir()
        has_example = (directory / "examples").is_dir()
        family = relative.split("/", 1)[0]
        families[family] += 1
        report.append({
            "id": skill,
            "path": path.relative_to(root).as_posix(),
            "family": family,
            "evidence_profile": matched,
            "reference_urls": references,
            "has_local_script": has_script,
            "has_example": has_example,
            "status": "STRUCTURAL_GAPS" if errors else "STRUCTURAL_GATE_PRESENT",
            "errors": errors,
            "real_host_behavior": "NOT_VERIFIED",
            "real_engine_fault_drill": "NOT_VERIFIED",
        })
    return {
        "scope": "DATA_ENGINEERING_STRUCTURAL_EVIDENCE_ONLY",
        "total_skill_packages": len(paths),
        "profile_count": len(profiles),
        "family_counts": dict(sorted(families.items())),
        "verified_structural": sum(r["status"] == "STRUCTURAL_GATE_PRESENT" for r in report),
        "has_local_script": sum(r["has_local_script"] for r in report),
        "has_example": sum(r["has_example"] for r in report),
        "all_real_engine_tests": "NOT_VERIFIED",
        "all_host_quality_ab": "NOT_VERIFIED",
        "issues": [r for r in report if r["errors"]],
        "skills": report,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--strict", action="store_true", help="Require all known skill packages to have structural gates")
    parser.add_argument("--summary", action="store_true")
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    report = audit(args.root)
    if args.summary:
        report.pop("skills")
    print(json.dumps(report, indent=2, ensure_ascii=False))
    if args.strict and (report["total_skill_packages"] < 123 or report["issues"]):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
