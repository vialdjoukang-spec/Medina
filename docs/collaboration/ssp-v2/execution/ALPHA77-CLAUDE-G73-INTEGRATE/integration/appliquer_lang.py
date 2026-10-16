"""Applique les propositions LANG (ALPHA1-CLAUDE-G73-LANG, fond_inchange) sur la base, ancre unique vérifiée."""
import json, sys
from pathlib import Path
ROOT = Path(sys.argv[1]); props = json.loads(Path(sys.argv[2]).read_text(encoding='utf-8'))
res = []
for p in props:
    f = ROOT / p['fichier']; t = f.read_text(encoding='utf-8'); n = t.count(p['ancien'])
    if n == 1 and p['fond_inchange']:
        f.write_text(t.replace(p['ancien'], p['nouveau']), encoding='utf-8'); res.append((p['id'], 'applique'))
    else:
        res.append((p['id'], f'non_applique (occurrences={n})'))
print(json.dumps(res, ensure_ascii=False))
