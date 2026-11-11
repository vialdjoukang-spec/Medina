import datetime as dt
import json
import os
from pathlib import Path
import shlex
import subprocess
import sys
from zoneinfo import ZoneInfo

root = Path('/workspace/medina-env/reprise-a41/candidate/source')
base = Path('/workspace/medina-env/reprise-a41/candidate')
controls = base / 'controls' / 'gel-densite-final-2026-10-08'
name = sys.argv[1]
commands = {
    'gloss-sigles': ['python3', str(controls / 'gloss-sigles.py')],
    'compiled-sigles': ['python3', str(controls / 'compiled-sigles.py')],
    'bank-a41': ['python3', str(controls / 'bank-a41.py')],
    't1-browser': ['node', '-r', str(controls / 'http-preload.cjs'), str(controls / 't1-browser.cjs')],
    'build-global': ['python3', str(root / 'build_front.py')],
    'build-t1': ['python3', str(root / 'build_front.py'), '--fragment', 'T1'],
    'static-a41': ['python3', str(root / 'test_v7.py'), '--static', 'A41'],
    'global-browser': ['python3', str(controls / 'global-http.py')],
    'native-a41': ['node', '-r', str(controls / 'http-preload.cjs'), str(root / 'tests/verify_course_native.cjs')],
}
env = os.environ.copy()
overrides = {
    'PYTHONDONTWRITEBYTECODE': '1', 'TMPDIR': str(controls / 'tmp'),
    'A41_CONTROL_ROOT': str(root), 'A41_CONTROL_OUT': str(base), 'A41_CONTROL_REPORTS': str(controls),
    'MEDINA_ROOT': str(root), 'MEDINA_OUT': str(base / ('t1' if name == 'build-t1' else 'global')),
    'MEDINA_CHROMIUM': '/usr/bin/chromium', 'MEDINA_CHROMIUM_PATH': '/usr/bin/chromium',
    'MEDINA_FRAGMENTS': str(base / 't1/fragments'), 'MEDINA_NATIVE_CODE': 'A41',
    'MEDINA_QA_OUT': str(controls / name),
}
env.update(overrides)
start = dt.datetime.now(dt.timezone.utc)
print(json.dumps({'job': name, 'started_utc': start.isoformat()}), flush=True)
with (controls / (name + '.log')).open('w') as log:
    result = subprocess.run(commands[name], cwd=root, env=env, stdout=log, stderr=subprocess.STDOUT)
end = dt.datetime.now(dt.timezone.utc)
record = {
    'job': name, 'argv': commands[name], 'command': shlex.join(commands[name]),
    'environment_overrides': overrides, 'cwd': str(root), 'exit_code': result.returncode,
    'started_utc': start.isoformat(), 'finished_utc': end.isoformat(),
    'started_zurich': start.astimezone(ZoneInfo('Europe/Zurich')).isoformat(),
    'finished_zurich': end.astimezone(ZoneInfo('Europe/Zurich')).isoformat(),
    'duration_seconds': (end - start).total_seconds(),
    'log': str(controls / (name + '.log')),
    'transport': 'HTTP local with external destinations blocked' if name in {'global-browser', 'native-a41', 't1-browser'} else None,
}
(controls / (name + '-command.json')).write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record), flush=True)
raise SystemExit(result.returncode)
