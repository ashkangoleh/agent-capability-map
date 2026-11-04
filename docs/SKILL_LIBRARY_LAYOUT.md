# Canonical skill library layout — phased domain organization

**Branch:** `pre_release`  
**Phase:** Data Science / Advanced Statistics and Foundations  
**Scope:** Source-tree organization only; existing skill IDs, trigger phrases, YAML routing, and user-selected domain profile semantics are unchanged.

## Directory contract

The canonical source location for the ten migrated Data Science skills is:

```text
.agents/skills/
  data/
    data-science/
      statistics-advanced/
        <stable-skill-id>/
          SKILL.md
      foundations/
        <stable-skill-id>/
          SKILL.md
```

The source of truth is each registered `path` in the relevant `domains/data/data-science/<category>/skills.yaml` file. Do **not** infer a path solely from a skill ID or assume all other skill paths are already nested.

| Category | Migration status | Canonical path policy |
|---|---|---|
| `data/data-science/statistics-advanced` | **6/6 migrated** | `.agents/skills/data/data-science/statistics-advanced/<id>/SKILL.md` |
| `data/data-science/foundations` | **4/4 migrated** | `.agents/skills/data/data-science/foundations/<id>/SKILL.md` |
| Other `data/data-science` categories | **32 remaining** | Existing flat paths remain authoritative until explicitly migrated, tested and old copies retired |
| Other Data subdomains | Not migrated | Preserve existing registered paths |
| Other top-level domains | Not migrated | No changes in this increment |

Preserved Advanced Statistics skill identities: `ds-power-sample-size`, `ds-bayesian-pymc-stan`, `ds-missing-data`, `ds-robust-nonparametric-inference`, `ds-multiple-testing-control`, `ds-survey-sampling-design`.

Preserved Foundations skill identities: `ds-problem-framing`, `ds-scientific-python`, `ds-r-statistics`, `ds-jupyter-reproducibility`.

## Why the migration is phased

The **Agent Skills format** specifies a folder containing `SKILL.md`; it does not require a universal source-tree placement. But **native client discovery is implementation-specific**. In particular, some native integrations require skill folders to be immediate children of their configured skills root; deeply nested source libraries are not universally auto-discovered.

- The repository's **authoritative global router** reads a registered YAML `path` only after task-scoped route selection; it can resolve nested source paths without a global scan. This is the supported source-of-truth behavior for this repository.
- **Do not claim** Codex, Claude Code, GitHub Copilot, Cursor, or OpenCode will auto-discover nested source skills in every mode. Host discovery and packaging must be tested separately.
- **Do not duplicate `SKILL.md`** at both flat and nested paths as a permanent compatibility workaround: it creates multiple physical sources, risks duplicate activation and stale instructions.
- If a host requires immediate-child skill directories, use a separately tested *explicit host-specific export/installation step* that emits a **flat, uniquely named distribution**, without altering the canonical nested source. No such export is implemented or certified in this phase; routing via the custom resolver remains the supported path.
- Continue to apply **user domain selection / allowlist**, not indiscriminate loading or installing all skills. A selected domain does not imply eager-loading all its skills.

## Migration invariants

1. Stable `id`, frontmatter `name`, trigger/exclusion rules, and skill content; no stylistic edits to the moved skills.
2. Copy to the domain path, verify **identical Git blob SHA**, update the exact source registry entry, change tests referencing the old physical path, and delete the flat original. For both migrated families all ten new blobs matched their old blobs.
3. Within `statistics-advanced` and `foundations`, no duplicate canonical SKILL files remain in the original flat locations. The master ID index remains unchanged.
4. Do not replace links with symlinks: native scanners may follow them, duplicate activations can result, and secure root/path resolution needs deliberate review.
5. Validate with `Router.validate()`, the deterministic fixture suite, Data Science layout tests and all unit tests **on the live branch HEAD**.
6. Independently assess host native discovery on each target before migrating further families or calling the nested layout universally supported.
7. Audit any skill bundle containing relative assets/references/scripts **as a whole directory**, not by moving only `SKILL.md`. This phase moved instruction-only skills.

## Validation evidence and limitations

- Ten destination `SKILL.md` files were retrieved after copy; **all ten Git blob SHAs matched** their original contents byte-for-byte.
- Both `domains/data/data-science/statistics-advanced/skills.yaml` (six) and `domains/data/data-science/foundations/skills.yaml` (four) were updated, and all ten obsolete flat files were deleted.
- `tests/test_data_science_inference_routing.py` now reads the registry path instead of assuming a flat directory.
- `tests/test_data_science_skill_layout.py` checks ten canonical paths, absence of flat duplicates and ten explicit route cases, the complete Data Science set of 42 registered skills, unique ownership and folder/id consistency.
- **NOT VERIFIED:** actual execution of full Python validator, complete routing regression suite and push GitHub Actions, nor native discovery in target hosts. Do not report these as PASS.
- This refactor adds **no examples**, no new specialist IDs and no changes to user domain-selection semantics.

## Next controlled organization phase

First retrieve actual CI/runtime evidence for this move. Then migrate one additional **Data Science subcategory** at a time, preserving its full skill bundle and updating its registry, tests and docs. Prefer source layout:

```text
.agents/skills/<top-level-domain>/<subdomain>/<capability-category>/<skill-id>/SKILL.md
```

Keep domain IDs stable and paths explicit. Migrate other Data subdomains and top-level domains only as separate, reviewed steps. Do not combine a sweeping 344-skill move with behavior changes.

## Official references

- [Agent Skills specification](https://agentskills.io/specification)
- [OpenAI Codex skill locations and loading](https://learn.chatgpt.com/docs/build-skills)
- [Claude Platform one-level managed repository discovery](https://platform.claude.com/docs/en/managed-agents/skills)
- [OpenAI plugin manifest depth restrictions](https://developers.openai.com/plugins/deploy/submission-errors)
