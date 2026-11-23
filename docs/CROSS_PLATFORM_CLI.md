# Cross-platform CLI: Linux, Windows, Node.js

**New:** Linux and Windows users can also run the native frozen CLI without installing either Python or Node.js. It is shipped as a self-contained ZIP (executable + permanent catalog/roles/skills), not a standalone script. See [Standalone distribution](STANDALONE_DISTRIBUTION.md) for download and setup. The instructions below describe the original source-installed Python/Node developer clients.

All entry points share **one authoritative Python router**. Node is a subprocess bridge, not a Python-free implementation. Requirements: Python 3.10+, PyYAML installed with the project, and Node.js 20+ for the Node frontend. The Git checkout containing catalog/, domains/, and .agents/skills/ must remain available. Neither the Python package nor this private Node package is claimed to be published to a public registry.

## Linux

~~~sh
git clone --branch pre_release https://github.com/ashkangoleh/agent-capability-map.git
cd agent-capability-map
python3 -m venv .venv
.venv/bin/python -m pip install -e .
.venv/bin/capability-map --root "$PWD" validate
.venv/bin/capability-map --root "$PWD" domains apply --domains infrastructure data/data-engineering --apply
.venv/bin/capability-map --root "$PWD" install --hosts codex claude opencode copilot cursor --apply
~~~

## Windows (PowerShell)

~~~powershell
git clone --branch pre_release https://github.com/ashkangoleh/agent-capability-map.git
Set-Location agent-capability-map
py -3 -m venv .venv
& .\.venv\Scripts\python.exe -m pip install -e .
& .\.venv\Scripts\capability-map.exe --root (Get-Location).Path validate
& .\.venv\Scripts\capability-map.exe --root (Get-Location).Path domains apply --domains infrastructure data/data-engineering --apply
& .\.venv\Scripts\capability-map.exe --root (Get-Location).Path install --hosts codex claude opencode copilot cursor --apply
~~~

For cmd.exe use: \`.\.venv\Scripts\capability-map.exe --root "%CD%" domains status\`. The PowerShell call operator \`&\` is not a CMD command.

## Node.js (Windows/Linux/macOS)

From the same checked-out repository (Node package is local/private):

~~~sh
npm link
capability-map-node domains list --prefix infrastructure
capability-map-node domains apply --domains infrastructure/containers-orchestration/kubernetes --apply
capability-map-node resolve --request "Infrastructure: kubernetes operator crd lifecycle"
~~~

Or execute directly: \`node node/bin/capability-map.mjs domains status\`. Set \`CAPABILITY_MAP_HOME\` for a checkout outside the Node package directory or pass \`--root <repo-directory>\` before the subcommand. Set \`CAPABILITY_MAP_PYTHON\` to the Python executable where this project is installed when more than one interpreter exists. The Windows default tries \`py -3\` then \`python\`; Unix defaults to \`python3\` then \`python\`. An interpreter that exists but lacks this package fails rather than silently falling back.

PowerShell interpreter selection:

~~~powershell
$env:CAPABILITY_MAP_PYTHON = (Resolve-Path .\.venv\Scripts\python.exe).Path
$env:CAPABILITY_MAP_HOME = (Get-Location).Path
node .\node\bin\capability-map.mjs domains status
~~~

All commands use a local user-scoped profile; dry-run is default, mutations require explicit \`--apply\`. Node passes argument arrays with \`shell: false\` to avoid command-string interpolation. Verify actual host read permissions and domain allowlist enforcement separately: a passing smoke test is not native-host runtime certification.

## Tests

- \`python -m unittest discover -s tests -p test_cross_platform_cli.py -v\`
- \`npm test\`
- GitHub Actions matrix \`ubuntu-latest\` and \`windows-latest\` with Python 3.12 + Node.js 22.
