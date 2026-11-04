"""Command-line interface for the global capability router."""

import argparse
import json
import os
import sys
from pathlib import Path

from .domain_selection import MAX_SELECTED_DOMAINS, discover_domains, domain_status, update_domain_selection
from .install import HOST_FILES, install
from .router import Router, RouterError


def root_location():
    return Path(os.environ.get("CAPABILITY_MAP_HOME", Path(__file__).resolve().parents[1]))


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="capability-map", description="Global-first YAML capability graph resolver"
    )
    parser.add_argument("--root", type=Path, default=root_location(), help="Master repository path")
    subs = parser.add_subparsers(dest="command", required=True)

    resolving = subs.add_parser("resolve", help="Resolve task without loading the skill body")
    resolving.add_argument("--request", required=True, help="Short user task intent without secrets")
    resolving.add_argument("--project", type=Path, default=None, help="Project root with AGENTS.md")
    resolving.add_argument("--home", type=Path, default=None, help="Home containing personal skills")

    validating = subs.add_parser("validate", help="Validate all YAML maps, registries, and skill paths")
    validating.add_argument("--project", type=Path, default=None)
    validating.add_argument("--home", type=Path, default=None)

    related = subs.add_parser("related", help="Inspect typed cross-domain relationships on demand")
    related.add_argument("--route", required=True, help="Slash-separated capability path")

    installing = subs.add_parser("install", help="Preview or install global instructions and host access settings")
    installing.add_argument("--hosts", nargs="+", choices=sorted([*HOST_FILES, "cursor"]), required=True)
    installing.add_argument("--home", type=Path, default=Path.home())
    installing.add_argument("--apply", action="store_true", help="Write instructions; preview by default")

    domains = subs.add_parser("domains", help="List and manage user-selected domain scopes")
    domain_actions = domains.add_subparsers(dest="domain_action", required=True)

    domain_list = domain_actions.add_parser("list", help="List selectable domain and subdomain scopes")
    domain_list.add_argument("--prefix", default=None, help="Limit results to a route prefix such as data")
    domain_list.add_argument("--home", type=Path, default=Path.home())

    domain_state = domain_actions.add_parser("status", help="Show the current user domain selection")
    domain_state.add_argument("--home", type=Path, default=Path.home())

    for action_name, action_help in (
        ("apply", "Replace the current selection with up to five domain scopes"),
        ("add", "Add domain scopes to the current selection"),
        ("remove", "Remove domain scopes from the current selection"),
    ):
        action = domain_actions.add_parser(action_name, help=action_help)
        action.add_argument("--domains", nargs="+", required=True, help="Canonical routes, e.g. data/data-engineering infrastructure")
        action.add_argument("--home", type=Path, default=Path.home())
        action.add_argument("--apply", action="store_true", help="Persist atomically; preview by default")

    domain_clear = domain_actions.add_parser("clear", help="Remove the allowlist and restore all domains")
    domain_clear.add_argument("--home", type=Path, default=Path.home())
    domain_clear.add_argument("--apply", action="store_true", help="Persist the change; preview by default")

    args = parser.parse_args(argv)
    try:
        if args.command == "install":
            result = {
                "status": "applied" if args.apply else "dry_run",
                "hosts": install(args.hosts, args.home, apply=args.apply, root=args.root),
                "message": "Existing file text outside managed blocks remains unchanged.",
            }
        elif args.command == "domains":
            if args.domain_action == "list":
                result = {
                    "status": "ok",
                    "max_domains_per_apply": MAX_SELECTED_DOMAINS,
                    "domains": discover_domains(args.root, prefix=args.prefix),
                }
            elif args.domain_action == "status":
                result = domain_status(args.root, args.home)
            else:
                operation = "replace" if args.domain_action == "apply" else args.domain_action
                if args.domain_action == "clear":
                    operation = "clear"
                result = update_domain_selection(
                    args.root,
                    args.home,
                    getattr(args, "domains", None),
                    operation=operation,
                    apply=args.apply,
                )
        elif args.command == "related":
            result = Router(args.root).related(args.route)
        else:
            router = Router(args.root, project=args.project, home=args.home)
            result = router.resolve(args.request) if args.command == "resolve" else router.validate()
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except (RouterError, OSError, UnicodeError) as exc:
        print(json.dumps({"status": "error", "message": str(exc)}, ensure_ascii=False), file=sys.stderr)
        raise SystemExit(2) from exc


if __name__ == "__main__":
    main()
