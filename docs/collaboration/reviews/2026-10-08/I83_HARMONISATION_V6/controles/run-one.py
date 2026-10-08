import datetime as dt
import json
import os
from pathlib import Path
import shlex
import subprocess
import sys
from zoneinfo import ZoneInfo

root = Path('/workspace/medina-env/reprise-i83/v6-candidate/source')
base = Path('/workspace/medina-env/reprise-i83/v6-candidate')
controls = base / 'controls'
name = sys.argv[1]
commands = {
    'gloss-sigles': ['python3', str(controls / 'gloss-sigles.py')],
    's01-browser': ['node', '-r', str(controls / 'http-preload.cjs'), str(root / 'tests/verify_s01_browser.cjs')],
    'build-global': ['python3', str(root / 'build_front.py')],
    'build-s01': ['python3', str(root / 'build_front.py'), '--fragment', 'S01'],
    'static-i83': ['python3', str(root / 'test_v7.py'), '--static', 'I83'],
    'global-browser': ['python3', str(controls / 'global-http.py')],
    'native-i83': ['node', '-r', str(controls / 'http-preload.cjs'), str(root / 'tests/verify_course_native.cjs')],
    'routes-i83-i87': ['node', '-r', str(controls / 'http-preload.cjs'), str(controls / 'routes-i83-i87.cjs')],
}
env = os.environ.copy()
overrides = {
    'PYTHONDONTWRITEBYTECODE': '1', 'TMPDIR': str(controls / 'tmp'),
    'I83_CONTROL_ROOT': str(root), 'I83_CONTROL_OUT': str(base), 'I83_CONTROL_REPORTS': str(controls),
    'MEDINA_ROOT': str(root), 'MEDINA_OUT': str(base / ('s01' if name == 'build-s01' else 'global')),
    'MEDINA_CHROMIUM': '/usr/bin/chromium', 'MEDINA_CHROMIUM_PATH': '/usr/bin/chromium',
    'MEDINA_FRAGMENTS': str(base / 's01/fragments'), 'MEDINA_NATIVE_CODE': 'I83',
    'MEDINA_QA_OUT': str(controls / name),
    'MEDINA_S01_FILE': str(base / 's01/fragments/MEDINA_S01_cardiovasculaire.html'),
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
    'transport': 'HTTP local with external destinations blocked' if name in {'global-browser', 'native-i83', 'routes-i83-i87'} else None,
}
(controls / (name + '-command.json')).write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record), flush=True)
raise SystemExit(result.returncode)
