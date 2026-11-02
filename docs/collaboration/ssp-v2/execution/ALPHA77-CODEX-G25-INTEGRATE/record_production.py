from lesson_helpers import *
import hashlib,datetime
files={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in list(CH.glob('*.html'))+[ROOT/'glossary/g25.py']}
for p in (ROOT/'assets/img/g25/alpha/codex').glob('*'):files[str(p.relative_to(ROOT))]=hashlib.sha256(p.read_bytes()).hexdigest()
OUT.joinpath('production.json').write_text(json.dumps(dict(mission='ALPHA77-CODEX-G25-INTEGRATE',code='G25',complete=True,meaning='Production matérielle des six surfaces ; relectures et tests finaux distincts, sans certification médicale.',recorded_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),final_files=files,clinical_certification=False),ensure_ascii=False,indent=2)+'\n')
