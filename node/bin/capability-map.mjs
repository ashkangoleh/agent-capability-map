#!/usr/bin/env node
import { spawnSync } from 'node:child_process';
import { existsSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

function isRepo(dir) {
  return existsSync(join(dir, 'catalog', 'root.yaml')) &&
    existsSync(join(dir, 'capability_map', 'cli.py'));
}
function findRepo(start) {
  let directory = resolve(start);
  while (true) {
    if (isRepo(directory)) return directory;
    const parent = dirname(directory);
    if (parent === directory) return null;
    directory = parent;
  }
}
function pythonCandidates() {
  const configured = process.env.CAPABILITY_MAP_PYTHON;
  if (configured !== undefined) {
    if (!configured.trim()) throw new Error('CAPABILITY_MAP_PYTHON cannot be blank');
    return [[configured, []]];
  }
  return process.platform === 'win32'
    ? [['py', ['-3']], ['python', []]]
    : [['python3', []], ['python', []]];
}
function run() {
  const userArgs = process.argv.slice(2);
  if (userArgs[0] === '--root' && (!userArgs[1] || userArgs[1].startsWith('--'))) {
    throw new Error('--root needs a repository directory');
  }
  const root = userArgs[0] === '--root'
    ? resolve(userArgs[1])
    : process.env.CAPABILITY_MAP_HOME
      ? resolve(process.env.CAPABILITY_MAP_HOME)
      : findRepo(dirname(fileURLToPath(import.meta.url)));
  if (!root || !isRepo(root)) {
    throw new Error('Repository not found; clone pre_release and set CAPABILITY_MAP_HOME or pass --root <directory>');
  }
  const args = userArgs[0] === '--root' ? userArgs : ['--root', root, ...userArgs];
  for (const [python, prefix] of pythonCandidates()) {
    const child = spawnSync(python, [...prefix, '-m', 'capability_map', ...args], {
      shell: false, stdio: 'inherit', windowsHide: true,
      env: process.env, cwd: process.cwd(),
    });
    if (child.error?.code === 'ENOENT') continue;
    if (child.error) throw child.error;
    if (child.signal) return child.signal === 'SIGINT' ? 130 : 129;
    return child.status ?? 2;
  }
  throw new Error('Python executable not found; install Python >=3.10 or set CAPABILITY_MAP_PYTHON');
}
try {
  process.exitCode = run();
} catch (err) {
  process.stderr.write('capability-map-node: ' + err.message + '\n');
  process.exitCode = 2;
}
