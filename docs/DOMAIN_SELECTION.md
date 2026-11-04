# User-Selected Domain Scopes

## Purpose

The master graph can contain many disciplines, but a user should only expose the domain scopes they need to their resolver. Selection is a user-level policy, not a repository fork and not a copy of the skill files.

The default remains backward compatible: **if no selection profile exists, all active domain scopes are eligible**.

## Selectable scopes

A selectable scope is an active YAML map node reachable from `catalog/root.yaml`. Routes are canonical slash-separated IDs:

- `infrastructure`: one top-level domain and all descendants.
- `data/data-engineering`: only the Data Engineering branch.
- `data/data-science`: only the Data Science branch under Data & Analytics.
- `data`: all Data subdomains, including Data Engineering, Data Science, Data Analysis, BI and Governance.

Use `capability-map domains list` to see all selectable scopes and their active-skill/mapped-node counts. Use `--prefix data` to inspect the Data tree.

## Limit and overlap policy

- Maximum: **five** domain scopes per profile or Apply operation.
- Scopes must be active map nodes in the current graph.
- Duplicate routes are rejected.
- Parent/child overlap is rejected because the parent already includes the child. For example, `data` plus `data/data-engineering` is invalid.
- Five is a limit on selected domain roots, not on the number of skills inside a selected domain.
- A selected scope makes its full descendant tree eligible; skill loading remains progressive and task-specific.

This is a conservative product limit to keep domain selection deliberate. It is not a limit imposed by the Agent Skills file format or a host.

## CLI lifecycle

### Inspect

~~~sh
capability-map domains list
capability-map domains list --prefix data
capability-map domains status
~~~

### Replace selection

Preview first; no write occurs without `--apply`.

~~~sh
capability-map domains apply --domains data/data-engineering data/data-science infrastructure
capability-map domains apply --domains data/data-engineering data/data-science infrastructure --apply
~~~

### Incremental changes

~~~sh
capability-map domains add --domains infrastructure --apply
capability-map domains remove --domains data/data-science --apply
~~~

### Restore unrestricted routing

~~~sh
capability-map domains clear
capability-map domains clear --apply
~~~

`apply` replaces the complete selection. `add` is idempotent for already registered routes. `remove` only removes currently registered routes and refuses to leave an empty restricted profile; use `clear` to deliberately restore unrestricted routing.

## Storage and transaction semantics

The profile is stored at:

~~~text
~/.config/agent-capability-map/domains.yaml
~~~

Example:

~~~yaml
schema_version: 1
domains:
  - data/data-engineering
  - data/data-science
  - infrastructure
~~~

- The file is local to the current user and shared by host adapters that invoke this installation of the CLI.
- It is not committed to the master repository and does not alter another user's profile.
- The update is validated before writing and persisted through a same-directory temporary file plus atomic replace.
- The profile and configuration directory must not be symlinks; unsafe paths fail closed.
- File mode is restricted to the user on POSIX systems.
- Invalid schema, unknown routes, duplicate routes, overlaps and more than five scopes fail before mutation.
- `clear --apply` removes the profile; it does not delete or alter any master skill.

## Resolver behavior

When the profile exists, every resolver traversal step filters children to the selected route prefixes. A selected nested scope permits its ancestors to be traversed only to reach that scope, and then permits only its descendants.

If a request matches an existing but unselected branch, the resolver returns `domain_not_enabled` and the matching route candidates. The host must not search the repository manually to bypass the allowlist. The user can inspect the route and explicitly add/apply it.

If no active route matches the request at all, normal unmatched/clarification behavior remains unchanged.

The allowlist controls availability, not semantic correctness. It does not authorize execution, install the referenced software, or guarantee that a host invokes the resolver. Host compatibility must still be tested independently.

## Acceptance criteria

- A user can apply one through five valid scopes.
- Dry-run does not create, modify or delete the profile.
- Invalid or overlapping selections fail without changing the existing profile.
- Repeated Apply is idempotent.
- Add/remove/clear preserve the declared lifecycle semantics.
- A selected route resolves normally; an unselected matching route returns `domain_not_enabled`.
- No profile preserves the pre-existing unrestricted behavior.
- Symlinked profile/config paths and invalid YAML fail closed.
