# Registered skill source library

Skills are selected from the domain/subdomain YAML graph, not by listing and injecting every `SKILL.md` into a prompt.

The source layout is migrating incrementally to domain/category directories. **The registered `path` field is authoritative.** Skills not yet migrated remain in their existing flat folders. Do not infer paths from IDs, create duplicate `SKILL.md` copies or rely on automatic native discovery of arbitrary nested folders.

Migrated Data Science families: `statistics-advanced` (six skills) and `foundations` (four skills). The remaining 32 Data Science skills, and other domains, retain their existing registered paths.

See `docs/SKILL_LIBRARY_LAYOUT.md` for the migration contract, native-host compatibility limitations and required validation.
