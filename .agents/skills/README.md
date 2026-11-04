# Registered skill source library

Skills are selected from the domain/subdomain YAML graph, not by listing and injecting every `SKILL.md` into a prompt.

The source layout is migrating incrementally to domain/category directories. **The registered `path` field is authoritative.** Skills not yet migrated remain in their existing flat folders. Do not infer paths from IDs, create duplicate `SKILL.md` copies or rely on automatic native discovery of arbitrary nested folders.

Current migrated family: `data/data-science/statistics-advanced` (six skills). All other active skills retain their existing registered locations.

See `docs/SKILL_LIBRARY_LAYOUT.md` for the migration contract, native-host compatibility limitations and required validation.
