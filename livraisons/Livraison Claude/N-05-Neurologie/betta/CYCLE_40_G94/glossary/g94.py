"""Abréviations G94 (cycle Betta 40) ; ajouts conditionnels, sans mutation des glossaires existants."""
from pathlib import Path
import importlib, sys
_existing = {}
def _root():
    for p in [Path(__file__).resolve().parent] + list(Path(__file__).resolve().parents):
        if (p / 'glossary' / 'cardio_1.py').exists():
            return p / 'glossary'
    return None
_g = _root()
if _g is not None:
    sys.path.insert(0, str(_g))
    for _path in sorted(_g.glob('*.py')):
        if _path.stem in {'g94', '__init__'}:
            continue
        try:
            _existing.update(getattr(importlib.import_module(_path.stem), 'G', {}))
        except Exception:
            pass
G = {}
def a(key, letters, full, definition, window=None):
    if key not in _existing:
        G[key] = {'lit': [list(x) for x in letters], 'full': full, 'def': '<p>' + definition + '</p>', 'ref': window}

a('EANO', [('E','European'),('A','Association of'),('N','Neuro-'),('O','Oncology')], 'European Association of Neuro-Oncology',
  'Association européenne de neuro-oncologie, coauteure de la recommandation 2023 sur les métastases leptoméningées des tumeurs solides.', 'g94-ml')
a('OUTCOMEREA', [('OUTCOMEREA','nom propre d’une base de données française de réanimation, non développé lettre à lettre dans ce cours')], 'OUTCOMEREA, base de données de réanimation',
  'Cohorte française de patients de soins intensifs dans laquelle l’association entre la non-correction précoce de paramètres systémiques et la mortalité a été étudiée.', 'g94-cibles')
a('EFNS', [('E','European'),('F','Federation of'),('N','Neurological'),('S','Societies')], 'European Federation of Neurological Societies',
  'Fédération européenne de sociétés de neurologie, aujourd’hui European Academy of Neurology ; auteure de la recommandation 2010 sur l’encéphalopathie de Wernicke.', 'g94-wernicke')
a('Shankar-Hari', [('Shankar-Hari','nom propre du premier auteur de la revue 2026, non une abréviation')], 'Shankar-Hari, premier auteur de la revue 2026',
  'Auteur principal de la revue sur l’encéphalopathie associée au sepsis publiée dans Intensive Care Medicine en 2026.', 'g94-sae-def')
a('kJ', [('k','kilo'),('J','joule')], 'kilojoule', 'Unité d’énergie ; le besoin en thiamine est rapporté à 4200 kJ de glucides.', 'g94-thiamine-meca')
a('S100B', [('S100','protéine liant le calcium de la famille S100'),('B','sous-unité B')], 'Protéine S100B',
  'Protéine d’origine cérébrale mesurée dans le sang ; son utilité diagnostique dans l’encéphalopathie septique est limitée.', 'g94-eeg')
a('DTPA', [('D','Diéthylène'),('T','Triamine'),('P','Penta-'),('A','Acétate')], 'Acide diéthylènetriaminepentaacétique',
  'Molécule qui lie un traceur radioactif (indium-111) pour l’étude du flux du liquide cérébrospinal.', 'g94-flux')
a('MAA', [('M','Macro-'),('A','Agrégats d’'),('A','Albumine')], 'Macroagrégats d’albumine',
  'Particules d’albumine marquées au technétium-99m, traceur alternatif pour l’étude du flux du liquide cérébrospinal.', 'g94-flux')
a('In-DTPA', [('In','Indium'),('DTPA','acide diéthylènetriaminepentaacétique')], 'Indium-111 lié au DTPA', 'Traceur de l’étude de flux du liquide cérébrospinal.', 'g94-flux')
a('Tc-MAA', [('Tc','Technétium'),('MAA','macroagrégats d’albumine')], 'Technétium-99m lié aux macroagrégats d’albumine', 'Traceur alternatif de l’étude de flux du liquide cérébrospinal.', 'g94-flux')
a('indium-111-DTPA', [('indium-111','isotope de l’indium'),('DTPA','acide diéthylènetriaminepentaacétique')], 'Indium-111 lié au DTPA', 'Traceur de l’étude de flux du liquide cérébrospinal.', 'g94-flux')
a('technétium-99m-MAA', [('technétium-99m','isotope du technétium'),('MAA','macroagrégats d’albumine')], 'Technétium-99m lié aux macroagrégats d’albumine', 'Traceur alternatif de l’étude de flux du liquide cérébrospinal.', 'g94-flux')
for _k, _t in [('G94.0','hydrocéphalie au cours de maladies infectieuses et parasitaires'),('G94.1','hydrocéphalie au cours de maladies tumorales'),
               ('G94.2','hydrocéphalie au cours d’autres maladies classées ailleurs'),('G94.3','encéphalopathie au cours d’autres maladies classées ailleurs'),
               ('G94.30','encéphalopathie au cours de maladies endocriniennes et métaboliques'),('G94.31','encéphalopathie au cours de maladies infectieuses et parasitaires'),
               ('G94.32','encéphalopathie septique'),('G94.39','encéphalopathie non précisée au cours d’autres maladies'),
               ('G94.8','autres affections précisées du cerveau au cours de maladies classées ailleurs')]:
    a(_k, [('G94','code CIM-10-GM de la catégorie astérisque'), (_k[3:], _t)], 'Code CIM-10-GM ' + _k + ', ' + _t, 'Sous-catégorie astérisque de G94 : ' + _t + '.', 'g94-cim')
for _k, _t in [('K72.7','encéphalopathie hépatique, exclue de G94.3'),('B48.80','mycose avec sepsis, renvoi croix de G94.32'),
               ('B60.80','protozoose avec sepsis, renvoi croix de G94.32'),('B34.80','infection virale avec sepsis, renvoi croix de G94.32')]:
    a(_k, [(_k[:3],'catégorie CIM-10-GM'), (_k[3:], _t)], 'Code CIM-10-GM ' + _k + ', ' + _t, 'Code cité dans le périmètre de G94 : ' + _t + '.', 'g94-cim')
