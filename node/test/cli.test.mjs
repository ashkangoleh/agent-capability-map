import test from 'node:test';
import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import { mkdtempSync, existsSync, readFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { resolve, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const repo = resolve(fileURLToPath(new URL('../../', import.meta.url)));
const script = join(repo, 'node/bin/capability-map.mjs');
const python = process.env.CAPABILITY_MAP_PYTHON || 'python';

function invoke(args, extra = {}) {
  return spawnSync(process.execPath, [script, ...args], {
    cwd: repo, shell: false, encoding: 'utf8',
    env: {...process.env, CAPABILITY_MAP_PYTHON: python, ...extra},
  });
}
function result(args) {
  const child = invoke(args);
  assert.equal(child.status, 0, child.stderr || child.stdout);
  return JSON.parse(child.stdout);
}
test('resolve returns canonical Infrastructure route and inherited roles', () => {
  const response = result(['resolve', '--request', 'Infrastructure: falco runtime security detection']);
  assert.equal(response.status, 'matched');
  assert.equal(response.selected_skill, 'runtime-security-falco');
  assert.equal(response.role_paths[0], join(repo, 'domains/infrastructure/ROLE.md'));
  assert.ok(response.role_paths.length >= 4);
  assert.ok(response.role_paths.at(-1).endsWith(join('devsecops', 'runtime-security', 'ROLE.md')));
});
test('domain apply persists and blocks unselected domains', () => {
  const home = mkdtempSync(join(tmpdir(), 'cap-map-js-'));
  const applied = result(['domains', 'apply', '--domains',
    'infrastructure/containers-orchestration/kubernetes', 'data/data-engineering',
    '--home', home, '--apply']);
  assert.equal(applied.status, 'applied');
  const profile = join(home, '.config/agent-capability-map/domains.yaml');
  assert.ok(readFileSync(profile, 'utf8').includes('infrastructure/containers-orchestration/kubernetes'));
  const yes = result(['resolve', '--request', 'Infrastructure: kubernetes operator crd lifecycle', '--home', home]);
  assert.equal(yes.status, 'matched');
  const no = result(['resolve', '--request', 'Audit technical SEO canonical tags', '--home', home]);
  assert.equal(no.status, 'domain_not_enabled');
  assert.equal(no.role_paths, undefined);
});
test('explicit root works from a reusable CLI', () => {
  const list = result(['--root', repo, 'domains', 'list', '--prefix', 'infrastructure']);
  assert.equal(list.status, 'ok');
  assert.ok(list.domains.length > 0);
});
test('untrusted request never reaches a command shell', () => {
  const home = mkdtempSync(join(tmpdir(), 'cap-map-js-'));
  const marker = join(home, 'unwanted-execution');
  const r = result(['resolve', '--request',
    'Audit technical SEO canonical tags; touch ' + marker, '--home', home]);
  assert.ok(r.status);
  assert.equal(existsSync(marker), false);
});
test('missing repository and interpreter fail explicitly', () => {
  let child = invoke(['--root', join(tmpdir(), 'no-repository'), 'validate']);
  assert.equal(child.status, 2);
  assert.match(child.stderr, /Repository not found/);
  child = invoke(['validate'], { CAPABILITY_MAP_PYTHON: join(tmpdir(), 'missing-python') });
  assert.equal(child.status, 2);
  assert.match(child.stderr, /Python executable not found/);
});
