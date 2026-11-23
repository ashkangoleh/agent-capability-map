# Skill source library

Skills are routed through the explicitly registered domain/subdomain/category YAML graph. The registry's `path` field is authoritative; **do not infer source locations from skill IDs or load the entire library eagerly**.

## Current structural status — 2026-11-05

- Total canonical skill manifests: **344**.
- Domain-nested canonical manifests: **344 (100%)**.
- Legacy flat manifests: **0 (0%)**.
- The Infrastructure / Storage Engineering / Advanced Storage category is complete: both `object-storage-infrastructure-operations` and `storage-san-nas-nvmeof` are in `infrastructure/storage-engineering/advanced-storage/<skill-id>/SKILL.md`.
- The Data Engineering / Batch Ingestion / Recovery skill now has one canonical nested manifest and a dedicated `domains/data/data-engineering/batch-ingestion/recovery/skills.yaml` registry; the later registry isolation changed routing visibility, not skill content.
- The final 16 flat skills were migrated into their domain/category directories with unchanged Git blob SHAs and updated YAML registry paths; this is source-layout completion, not host compatibility certification.
- Only move a skill with all bundled resources; update all referencing registries, ensure there is only one canonical physical manifest, and test the path before deleting the old one.
- Native nested-skill discovery is host-dependent. The YAML Router is the authoritative source selector, and host-specific packaging must be validated separately.

**Global Python/CI status:** the 16-skill migration CI run `42014842454` and recovery-registry isolation CI run `42015373146` both passed. New host bootstrap contract tests require a separate post-commit CI verification. See `docs/CONTINUATION_CHECKPOINT.md` for evidence and `docs/SKILL_LIBRARY_LAYOUT.md` for layout invariants.

Host-specific installation and limitations: `docs/HOST_COMPATIBILITY_ACCEPTANCE.md`.
