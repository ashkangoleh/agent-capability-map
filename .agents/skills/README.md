# Skill source library

Skills are routed through the explicitly registered domain/subdomain/category YAML graph. The registry's `path` field is authoritative; **do not infer source locations from skill IDs or load the entire library eagerly**.

## Current structural status — 2026-11-05

- Total canonical skill manifests: **344**.
- Domain-nested canonical manifests: **327 (95.06%)**.
- Legacy flat manifests: **17 (4.94%)**.
- The Infrastructure / Storage Engineering / Advanced Storage category is complete: both `object-storage-infrastructure-operations` and `storage-san-nas-nvmeof` are in `infrastructure/storage-engineering/advanced-storage/<skill-id>/SKILL.md`.
- Only move a skill with all bundled resources; update all referencing registries, ensure there is only one canonical physical manifest, and test the path before deleting the old one.
- Native nested-skill discovery is host-dependent. The YAML Router is the authoritative source selector, and host-specific packaging must be validated separately.

**Global Python/CI status:** the earlier generic registry path failures were repaired; legacy flat-path assumptions in three coverage tests were also corrected. Confirm the latest GitHub Actions run before declaring the full repository green. See `docs/CONTINUATION_CHECKPOINT.md` for evidence and `docs/SKILL_LIBRARY_LAYOUT.md` for layout invariants.
