"""Build a relocatable, no-Python-install standalone distribution for the host OS."""

import argparse
import hashlib
import json
import os
import platform
import shutil
import stat
import subprocess
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ASSET_DIRECTORIES = ("catalog", "domains", ".agents/skills")
ASSET_FILES = ("README.md", "docs/CROSS_PLATFORM_CLI.md")


def platform_slug():
    system = platform.system().lower()
    if system not in ("linux", "windows"):
        raise RuntimeError(f"Standalone CI supports Linux and Windows only: {system}")
    machine = platform.machine().lower()
    if machine not in ("x86_64", "amd64"):
        raise RuntimeError(f"Only verified x64 build architecture is supported: {machine}")
    return f"{system}-x64"


def require_safe_source(source):
    if not source.exists():
        raise RuntimeError(f"Required source asset missing: {source}")
    for entry in (source, *source.rglob("*")) if source.is_dir() else (source,):
        if entry.is_symlink():
            raise RuntimeError(f"Source asset symlink is not supported: {entry}")
        if entry.is_file() and not entry.resolve().is_relative_to(ROOT):
            raise RuntimeError(f"Source asset escapes checked-out repository: {entry}")


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as reader:
        for chunk in iter(lambda: reader.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def archive_folder(bundle, archive):
    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as writer:
        for path in sorted(bundle.rglob("*")):
            if not path.is_file():
                continue
            relpath = path.relative_to(bundle.parent).as_posix()
            info = zipfile.ZipInfo(relpath)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = path.stat().st_mode << 16
            info.create_system = 3
            writer.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED)


def build(output):
    slug = platform_slug()
    output = output.expanduser().resolve()
    output.mkdir(parents=True, exist_ok=True)
    workspace = ROOT / "build" / "standalone"
    frozen = workspace / "frozen"
    binary = "capability-map.exe" if os.name == "nt" else "capability-map"
    subprocess.run(
        [
            sys.executable, "-m", "PyInstaller",
            "--noconfirm", "--clean", "--onefile", "--console", "--noupx",
            "--name", "capability-map",
            "--paths", str(ROOT),
            "--distpath", str(frozen),
            "--workpath", str(workspace / "work"),
            "--specpath", str(workspace / "spec"),
            str(ROOT / "scripts" / "standalone_entry.py"),
        ],
        check=True,
        cwd=ROOT,
    )

    destination = output / f"capability-map-{slug}"
    if destination.exists():
        shutil.rmtree(destination)
    destination.mkdir(parents=True)
    executable = frozen / binary
    if not executable.is_file():
        raise RuntimeError(f"PyInstaller did not produce an executable: {executable}")
    shutil.copy2(executable, destination / binary)
    if os.name != "nt":
        (destination / binary).chmod((destination / binary).stat().st_mode | stat.S_IXUSR)

    for name in ASSET_DIRECTORIES:
        origin = ROOT / name
        require_safe_source(origin)
        shutil.copytree(origin, destination / name, symlinks=False)
    for name in ASSET_FILES:
        origin = ROOT / name
        require_safe_source(origin)
        target = destination / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(origin, target)

    files = {
        path.relative_to(destination).as_posix(): sha256(path)
        for path in sorted(destination.rglob("*"))
        if path.is_file()
    }
    manifest = {
        "format": 1,
        "platform": slug,
        "source_commit": os.environ.get("GITHUB_SHA", "local-unverified"),
        "executable": binary,
        "files_sha256": files,
    }
    (destination / "BUNDLE_MANIFEST.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    archive = output / f"capability-map-{slug}.zip"
    if archive.exists():
        archive.unlink()
    archive_folder(destination, archive)
    print(json.dumps({
        "bundle": str(destination),
        "archive": str(archive),
        "platform": slug,
        "files": len(files),
        "sha256_archive": sha256(archive),
    }, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=ROOT / "dist" / "standalone")
    args = parser.parse_args()
    build(args.output)
