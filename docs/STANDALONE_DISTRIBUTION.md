# Standalone capability-map — Linux and Windows (no Python/Node install)

**Status:** Native x64 distribution built and tested by the `standalone-release` GitHub Actions job. Download only after checking the **current commit's** job success. Python, Node.js, Git Bash and WSL are **not needed on the end-user machine**.

## Distribution contract

PyInstaller **6.22.3** bundles the interpreter, the PyYAML dependency and the existing router into a platform-specific `--onefile` native executable. The final `capability-map-<platform>.zip` contains the executable **plus stable, external** `catalog/`, `domains/` and `.agents/skills/` trees. This is a self-contained **ZIP distribution**, not a single-file-only product. The adjacent sources are necessary: a selected `skill_path` or `role_paths` path may be consumed by an agent after the CLI process terminates. Placing them in PyInstaller's per-run temporary `sys._MEIPASS` would be incorrect.

- Linux package: `capability-map-linux-x64.zip`, containing `capability-map-linux-x64/capability-map`.
- Windows package: `capability-map-windows-x64.zip`, containing `capability-map-windows-x64/capability-map.exe`.
- No global install, package manager or interpreter required at runtime. The build environment still needs Python 3.12 and PyInstaller.
- Builds target **Linux x86_64 with glibc (Ubuntu 24.04)** and **Windows x64 (Windows Server 2022)**. Other Linux libc distributions, ARM, macOS and code-signing are **not certified**.
- Move/extract the complete folder once before running `install --apply`. If moved later, re-run `install --apply` to refresh absolute host instructions.
- This project's domain allowlist stays capped at five non-overlapping scopes; registered skills and domain role inheritance remain authoritative. No second routing engine.

## Linux (terminal)

Extract the Linux x64 ZIP in a directory of your choice, open the extracted `capability-map-linux-x64` directory, then:

~~~bash
chmod +x ./capability-map
./capability-map validate
./capability-map domains list --prefix infrastructure
./capability-map domains apply --domains infrastructure data/data-engineering --apply
./capability-map resolve --request "Infrastructure: falco runtime security detection"
./capability-map install --hosts codex claude opencode copilot cursor --apply
~~~

## Windows (PowerShell; no Bash/WSL)

Use File Explorer or `Expand-Archive` to extract the Windows x64 ZIP. Then navigate to the extracted `capability-map-windows-x64` directory:

~~~powershell
.\capability-map.exe validate
.\capability-map.exe domains list --prefix infrastructure
.\capability-map.exe domains apply --domains infrastructure data/data-engineering --apply
.\capability-map.exe resolve --request "Infrastructure: falco runtime security detection"
.\capability-map.exe install --hosts codex claude opencode copilot cursor --apply
~~~

The executable runs in CMD, too, using the native Windows .exe path. No `py -3`, `python`, `node`, `npm`, Bash or WSL is required. A supported agent host is still required if you want an agent to **consume** the resolved skill. `install` registers host instructions; it does not install those five host applications.

## Package contents and trust model

The archive includes `BUNDLE_MANIFEST.json` with platform name, build commit identifier and SHA-256 digests for every shipped binary/asset. The CI smoke test extracts the ZIP into a directory **containing spaces**, verifies those checksums and executes the native binary from outside the source checkout, with Python/Node removed from `PATH`. It checks `validate`, `resolve`, `domains apply` dry-run and persistence, `domain_not_enabled`, and five-host instruction installation + idempotency. It rejects a temporary unpack path in host instructions.

**Important:** a manifest inside an unsigned archive provides an integrity check against accidental corruption, not authenticity against a malicious distributor who can replace both the archive and manifest. Pin the trusted GitHub Actions run/commit, protect its artifact permissions and verify downloaded artifacts through a trusted channel. Distribution signing, notarization, antivirus reputation and automatic updates are not implemented.

## Developer build (not required by the end user)

The GitHub Actions job builds separately on `ubuntu-24.04` and `windows-2022` with Python 3.12 and PyInstaller 6.22.3:

~~~bash
python -m pip install -e . pyinstaller==6.22.3
python scripts/build_standalone.py --output dist/standalone
python scripts/smoke_standalone.py --archive dist/standalone/capability-map-linux-x64.zip
~~~

To check CI artifacts, open the latest successful `pre_release` workflow run, locate the `Standalone bundle (linux-x64)` and `Standalone bundle (windows-x64)` jobs and download the OS-specific ZIP artifact. The artifact contents are **not** a standalone NPM/Python package, and there is no claim of direct distribution through npm, pip or an auto-installer.

## Remaining acceptance gates

Run version-specific host-agent integration tests for Codex, Claude Code, OpenCode, Copilot and Cursor on real client machines. CI verifies the binary CLI and resulting instruction files, not actual consumption of roles/skills by those agents or measurable improvements to final LLM output. Linux glibc compatibility outside the build image, Windows SmartScreen reputation and signed release publishing require separate evidence.
