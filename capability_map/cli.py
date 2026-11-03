"""Command-line interface for the global capability router."""

import argparse
import json
import os
import sys
from pathlib import Path

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

    installing = subs.add_parser("install", help="Preview or install global agent instructions")
    installing.add_argument("--hosts", nargs="+", choices=sorted([*HOST_FILES, "cursor"]), required=True)
    installing.add_argument("--home", type=Path, default=Path.home())
    installing.add_argument("--apply", action="store_true", help="Write instructions; preview by default")

    args = parser.parse_args(argv)
    try:
        if args.command == "install":
            result = {
                "status": "applied" if args.apply else "dry_run",
                "hosts": install(args.hosts, args.home, apply=args.apply),
                "message": "Existing file text outside managed blocks remains unchanged.",
            }
        else:
            router = Router(args.root, project=args.project, home=args.home)
            result = router.resolve(args.request) if args.command == "resolve" else router.validate()
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except (RouterError, OSError, UnicodeError) as exc:
        print(json.dumps({"status": "error", "message": str(exc)}, ensure_ascii=False), file=sys.stderr)
        raise SystemExit(2) from exc


if __name__ == "__main__":
    main()
