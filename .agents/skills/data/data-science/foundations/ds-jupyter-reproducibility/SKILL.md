---
name: ds-jupyter-reproducibility
description: Use when making analytical notebooks reproducible, reviewable, parameterized, and safe to rerun outside an interactive session.
metadata:
  version: "1.1.0"
---

# ds-jupyter-reproducibility

## Activation boundary

Use when a notebook is a deliverable, analysis artifact or recurring research workflow. Do not treat a notebook that runs only in the author's current kernel as reproducible.

## Required context

Notebook paths, data dependencies, environment, credentials, execution time, expected outputs, parameter inputs and target runtime.

## Workflow

1. Restart the kernel and run all cells in order. Record failures caused by hidden state, execution order or stale variables.
2. Remove machine-specific paths, embedded credentials, personal data and undeclared local dependencies.
3. Pin the environment and document system-level dependencies. Use a lockfile or reproducible environment definition.
4. Parameterize dates, input paths and experiment settings rather than editing cells manually between runs.
5. Make external data dependencies explicit: source, snapshot/version, extraction timestamp, checksum and access permissions.
6. Separate exploration from the final analytical path. Move reusable logic into tested modules and keep notebook cells focused on explanation and results.
7. Validate outputs against deterministic fixtures or tolerances. Use notebook execution tooling in CI when runtime and licensing permit.
8. Control notebook diffs: clear irrelevant output, preserve meaningful charts/tables and avoid huge embedded data payloads.
9. Provide a clean-run command, expected artifacts and known limitations.

## Failure modes and abstention

- Do not commit tokens, customer records or private extracts in notebook metadata or outputs.
- Do not rely on widgets, environment variables or mounted drives without documenting them.
- Do not silently suppress execution errors or stale output.
- If a notebook cannot run without inaccessible data or proprietary credentials, mark the dependency and provide a safe mock fixture.

## Validation checklist

- [ ] Restart-and-run-all succeeds.
- [ ] Environment and data dependencies are declared.
- [ ] Parameters and paths are portable.
- [ ] Outputs are reproducible or have stated tolerances.
- [ ] Secrets and sensitive data are absent.
- [ ] Clean execution is tested where feasible.

## Authoritative reference

- https://docs.jupyter.org/en/latest/
