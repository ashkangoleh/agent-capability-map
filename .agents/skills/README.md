# Skill source library

Skills are routed through the explicitly registered domain/subdomain/category YAML graph. The registry's `path` field is authoritative; **do not infer source locations from skill IDs or load the entire library eagerly**.

## Current structural status — 2026-11-05

- Total canonical skill manifests: **344**.
- Domain-nested canonical manifests: **328 (95.35%)**.
- Legacy flat manifests: **16 (4.65%)**.
- The Infrastructure / Storage Engineering / Advanced Storage category is complete: both `object-storage-infrastructure-operations` and `storage-san-nas-nvmeof` are in `infrastructure/storage-engineering/advanced-storage/<skill-id>/SKILL.md`.
- The Data Engineering / Batch Ingestion / Recovery `pipeline-backfill-recovery` skill now has exactly one canonical nested manifest; its registered `path` in `domains/data/general-skills.yaml` has changed without altering routing triggers.
- Only move a skill with all bundled resources; update all referencing registries, ensure there is only one canonical physical manifest, and test the path before deleting the old one.
- Native nested-skill discovery is host-dependent. The YAML Router is the authoritative source selector, and host-specific packaging must be validated separately.

**Global Python/CI status:** pre-migration push run `42000161037` passed at `48e169c52421318ed5bd294bc4f23ff4e5dd2d3d`. Verify the push run on the migration commit separately. See `docs/CONTINUATION_CHECKPOINT.md` for evidence and `docs/SKILL_LIBRARY_LAYOUT.md` for layout invariants. See `docs/CONTINUATION_CHECKPOINT.md` for evidence and `docs/SKILL_LIBRARY_LAYOUT.md` for layout invariants.
