"""Abréviations E01 — Affections thyroïdiennes liées à une carence en iode. Ajouts conditionnels : aucun terme existant n’est écrasé."""
from pathlib import Path
import importlib.util
_existing = set()
for _dir in (Path(__file__).resolve().parent, Path(__file__).resolve().parents[8] / 'glossary' if len(Path(__file__).resolve().parents) > 8 else None):
    if _dir is None or not _dir.is_dir():
        continue
    for _path in sorted(_dir.glob('*.py')):
        if _path.stem in {'e01', '__init__'}:
            continue
        try:
            _spec = importlib.util.spec_from_file_location('_g_' + _path.stem, _path)
            _mod = importlib.util.module_from_spec(_spec)
            _spec.loader.exec_module(_mod)
            _existing.update(getattr(_mod, 'G', {}))
        except Exception:
            pass
G = {}
def a(key, letters, full, definition, window=None):
    if key not in _existing:
        G[key] = {'lit': [list(x) for x in letters], 'full': full, 'def': '<p>' + definition + '</p>', 'ref': window}

a('ETA', [('E','European'),('T','Thyroid'),('A','Association')], 'European Thyroid Association (Association européenne de la thyroïde)',
  'Société savante européenne dont les recommandations de 2017 (échographie), 2021 (produits de contraste iodés) et 2023 (nodules thyroïdiens) fondent la conduite de cette leçon, faute de recommandation suisse de société savante lue.', 'e01-sources-guides')
a('EU-TIRADS', [('EU','European (européen)'),('TI','THYROID (de la thyroïde)'),('RADS','Imaging Reporting And Data System (système de compte rendu et de données d’imagerie)')], 'Système européen de compte rendu échographique des nodules thyroïdiens',
  'Classification de l’<i>European Thyroid Association</i> en cinq catégories selon l’aspect échographique, avec risque estimé de malignité et seuil de taille de ponction.', 'e01-eutirads')
a('UNICEF', [('U','United'),('N','Nations'),('I','International'),('C','Children’s'),('E','Emergency'),('F','Fund')], 'Fonds des Nations unies pour l’enfance',
  'Cet organisme a co-publié avec l’OMS et le conseil international de lutte contre les troubles dus à la carence iodée les besoins quotidiens en iode utilisés dans cette leçon. Le sigle conserve l’ancien nom anglais du fonds.', 'e01-nis')
a('ICCIDD', [('I','International'),('C','Council for the'),('C','Control of'),('I','Iodine'),('D','Deficiency'),('D','Disorders')], 'Conseil international de lutte contre les troubles dus à la carence iodée',
  'Ce conseil a co-publié avec l’OMS et l’UNICEF le guide d’évaluation des troubles dus à la carence iodée, 3e édition, 2007.', 'e01-nis')
a('LISA', [('LISA','nom de l’essai allemand lévothyroxine et iode ; aucun développement littéral fourni par la source')], 'Essai LISA (lévothyroxine et iode)',
  'Essai randomisé contre placebo, 1024 patients euthyroïdiens porteurs de nodules, sur un an : lévothyroxine, iode ou association.', 'e01-levothyroxine')
a('TRH', [('T','Thyrotropin'),('R','Releasing'),('H','Hormone')], 'Hormone de libération de la thyrotropine',
  'Peptide hypothalamique qui stimule la sécrétion de TSH. Un test à la TRH, ou une scintigraphie de suppression, est cité par l’information professionnelle suisse d’Euthyrox® pour exclure une autonomie avant le traitement.', 'e01-levothyroxine')
a('Jod-Basedow', [('Jod','iode en allemand'),('Basedow','Carl von Basedow, médecin allemand')], 'Phénomène de Jod-Basedow',
  'Hyperthyroïdie déclenchée par une charge d’iode sur un tissu thyroïdien autonome, qui produit des hormones sans contrôle régulateur.', 'e01-wolff')
a('Wolff-Chaikoff', [('Wolff','Jan Wolff'),('Chaikoff','Israel Lyon Chaikoff')], 'Effet Wolff-Chaikoff',
  'Inhibition transitoire de l’organification de l’iodure et de la sécrétion hormonale par un excès pharmacologique d’iode, suivie d’un échappement de la thyroïde normale.', 'e01-wolff')
a('OSAV', [('O','Office fédéral de la'),('S','Sécurité'),('A','Alimentaire et des'),('V','Affaires Vétérinaires')], 'Office fédéral de la sécurité alimentaire et des affaires vétérinaires',
  'Autorité fédérale suisse qui surveille l’iodation du sel et publie les recommandations d’apport en iode.', 'e01-prophylaxie')
a('BLV', [('B','Bundesamt für'),('L','Lebensmittelsicherheit und'),('V','Veterinärwesen')], 'Office fédéral de la sécurité alimentaire et des affaires vétérinaires (nom allemand)',
  'Équivalent allemand de l’OSAV.', 'e01-prophylaxie')
for _code, _txt in (('E01.0', 'goitre diffus (endémique) lié à une carence en iode'), ('E01.1', 'goitre multinodulaire (endémique) lié à une carence en iode, goitre nodulaire inclus'),
                    ('E01.2', 'goitre (endémique) lié à une carence en iode, sans précision'), ('E01.8', 'autres affections thyroïdiennes liées à une carence en iode, hypothyroïdie acquise par carence iodée incluse')):
    a(_code, [(_code, 'sous-code de la CIM-10-GM 2024 : ' + _txt)], _txt[0].upper() + _txt[1:], 'Sous-code de la catégorie E01 de la classification statistique suisse CIM-10-GM 2024 : ' + _txt + '.')
