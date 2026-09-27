"""Restaure les deux couches d'interface embarquées dans le HTML livré."""
from pathlib import Path
import re

root = Path(__file__).resolve().parent
html = (root / 'delivered.html').read_text(encoding='utf-8')
css = re.search(r'<style id="medina-polish">(.*?)</style>', html, re.S)
scripts = re.findall(r'<script(?:\s[^>]*)?>(.*?)</script>', html, re.S)
js = [s for s in scripts if 'MEDINA — couche d\'embellissement et modules' in s]
if css is None or len(js) != 1:
    raise SystemExit('Couches introuvables ou ambiguës dans la version livrée')
(root / 'shell' / 'polish.css').write_text(css.group(1), encoding='utf-8')
(root / 'shell' / 'polish.js').write_text(js[0], encoding='utf-8')
print('Couches restaurées :', len(css.group(1)), 'caractères CSS,', len(js[0]), 'caractères JS')
