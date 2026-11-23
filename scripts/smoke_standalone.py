"""Smoke an extracted standalone package with no external Python/Node on PATH."""

import argparse
import json
import os
import platform
import stat
import subprocess
import tempfile
import zipfile
from pathlib import Path


def invoke(executable, argv, *, cwd, env):
    completed = subprocess.run(
        [str(executable), *argv],
        capture_output=True, encoding="utf-8", text=True, cwd=cwd, env=env,
        check=False, timeout=120,
    )
    if completed.returncode:
        raise AssertionError(
            f"standalone {argv!r} exited {completed.returncode}: "
            f"{completed.stderr[-2500:]} {completed.stdout[-1000:]}"
        )
    try:
        return json.loads(completed.stdout)
    except json.JSONDecodeError as exc:
        raise AssertionError(f"Non-JSON standalone output: {completed.stdout[:1500]}") from exc


def smoke(archive):
    with tempfile.TemporaryDirectory(prefix="capability map standalone test ") as work:
        work = Path(work).resolve()
        with zipfile.ZipFile(archive) as source:
            source.extractall(work)
        folders = [p for p in work.iterdir() if p.is_dir() and p.name.startswith("capability-map-")]
        if len(folders) != 1:
            raise AssertionError(f"Expected one unpacked bundle, found: {folders}")
        bundle = folders[0]
        manifest = json.loads((bundle / "BUNDLE_MANIFEST.json").read_text(encoding="utf-8"))
        executable = bundle / manifest["executable"]
        if not executable.is_file():
            raise AssertionError(f"Missing binary: {executable}")
        if os.name != "nt":
            executable.chmod(executable.stat().st_mode | stat.S_IXUSR)
        import hashlib
        for relpath, expected in manifest["files_sha256"].items():
            candidate = bundle / relpath
            if not candidate.is_file() or hashlib.sha256(candidate.read_bytes()).hexdigest() != expected:
                raise AssertionError(f"Bundle checksum mismatch: {relpath}")

        # Preserve OS dependencies (System32 on Windows) but remove the build toolchains.
        env = os.environ.copy()
        env.pop("PYTHONPATH", None)
        env.pop("PYTHONHOME", None)
        env.pop("CAPABILITY_MAP_HOME", None)
        env.pop("CAPABILITY_MAP_PYTHON", None)
        env["PATH"] = str(bundle)
        if os.name == "nt":
            # Windows environment key spelling is not guaranteed by CI runners.
            # System DLL loading does not require a Python or Node interpreter.
            system_root = next(
                (value for key, value in env.items()
                 if key.casefold() in ("systemroot", "windir") and value),
                None,
            )
            if system_root:
                env["PATH"] += os.pathsep + os.path.join(system_root, "System32")
        outside = work / "outside checkout with spaces"
        outside.mkdir()
        status = invoke(executable, ["validate"], cwd=outside, env=env)
        assert status["status"] == "valid", status
        match = invoke(executable, [
            "resolve", "--request", "Infrastructure: falco runtime security detection"
        ], cwd=outside, env=env)
        assert match["status"] == "matched" and match["selected_skill"] == "runtime-security-falco", match
        assert match["skill_path"].startswith(str(bundle)), match
        assert all(path.startswith(str(bundle)) for path in match["role_paths"]), match

        home = work / "isolated user home"
        home.mkdir()
        preview = invoke(executable, [
            "domains", "apply", "--domains", "infrastructure", "data/data-engineering",
            "--home", str(home)
        ], cwd=outside, env=env)
        assert preview["status"] == "dry_run", preview
        assert not (home / ".config/agent-capability-map/domains.yaml").exists()
        applied = invoke(executable, [
            "domains", "apply", "--domains", "infrastructure", "data/data-engineering",
            "--home", str(home), "--apply"
        ], cwd=outside, env=env)
        assert applied["status"] == "applied", applied
        blocked = invoke(executable, [
            "resolve", "--request", "Audit technical SEO canonical tags", "--home", str(home)
        ], cwd=outside, env=env)
        assert blocked["status"] == "domain_not_enabled", blocked
        assert "role_paths" not in blocked and "role_path" not in blocked, blocked

        installed = invoke(executable, [
            "install", "--hosts", "codex", "claude", "opencode", "copilot", "cursor",
            "--home", str(home), "--apply"
        ], cwd=outside, env=env)
        assert installed["status"] == "applied", installed
        text = (home / ".codex/AGENTS.md").read_text(encoding="utf-8")
        assert str(executable) in text and str(bundle) in text, text
        assert "-m capability_map" not in text, text
        assert "role_paths" in text, text
        if os.name == "nt":
            assert "& '" in text and f"'{bundle}'" in text, text
        second = invoke(executable, [
            "install", "--hosts", "codex", "claude", "opencode", "copilot", "cursor",
            "--home", str(home), "--apply"
        ], cwd=outside, env=env)
        assert all(not host["changed"] for host in second["hosts"]), second
        print(json.dumps({
            "result": "PASS",
            "platform": platform.system(),
            "archive": str(archive),
            "bundle": str(bundle),
            "checked_assets": len(manifest["files_sha256"]),
            "isolated_path": True,
            "no_python_or_node_on_path": True,
            "host_install_idempotent": True,
        }, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--archive", type=Path, required=True)
    args = parser.parse_args()
    smoke(args.archive.expanduser().resolve())
