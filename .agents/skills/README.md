# Skill source library

Skills are routed through the explicitly registered domain/subdomain/category YAML graph. The registry's `path` field is authoritative; **do not infer source locations from skill IDs or load the entire library eagerly**.

## Current structural status — 2026-11-05

- Total canonical skill manifests: **344**.
- Domain-nested canonical manifests: **327 (95.06%)**.
- Legacy flat manifests: **17 (4.94%)**.
- The Infrastructure / Storage Engineering / Advanced Storage category is complete: both `object-storage-infrastructure-operations` and `storage-san-nas-nvmeof` are in `infrastructure/storage-engineering/advanced-storage/<skill-id>/SKILL.md`.
- Only move a skill with all bundled resources; update all referencing registries, ensure there is only one canonical physical manifest, and test the path before deleting the old one.
- Native nested-skill discovery is host-dependent. The YAML Router is the authoritative source selector, and host-specific packaging must be validated separately.

**Global Python/CI status:** not green as of the latest checked migration run; a stale `domains/data/general-skills.yaml` reference to the moved `data-engineering-implementation` skill blocks validation. See `docs/CONTINUATION_CHECKPOINT.md` for current evidence and `docs/SKILL_LIBRARY_LAYOUT.md` for the migration contract.
