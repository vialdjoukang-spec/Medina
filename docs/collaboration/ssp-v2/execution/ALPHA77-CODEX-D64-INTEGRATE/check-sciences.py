"""Run the unchanged shared assertions with the explicitly authorised trusted base."""
from pathlib import Path
import importlib.util,sys
spec=importlib.util.spec_from_file_location('original_sciences','tests/audit_sciences.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
m.BASE='3131a5cbf6cc003ead358e25152073959c53c4d9'
sys.argv=['audit_sciences.py','--codes','D64','--out',str(Path(__file__).parent/'audit-sciences-trusted-base.json')]
m.main()
