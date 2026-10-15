"""Abréviations E07 — Autres affections de la thyroïde. Ajouts conditionnels : aucun terme existant n’est écrasé."""
from pathlib import Path
import importlib.util
_existing = set()
for _dir in (Path(__file__).resolve().parent, Path(__file__).resolve().parents[8] / 'glossary' if len(Path(__file__).resolve().parents) > 8 else None):
    if _dir is None or not _dir.is_dir():
        continue
    for _path in sorted(_dir.glob('*.py')):
        if _path.stem in {'e07', '__init__'}:
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
  'Société savante européenne dont les recommandations de 2012 (cancer médullaire et dépistage génétique) et de 2023 (nodules thyroïdiens) fondent plusieurs passages de cette leçon, faute de recommandation suisse lue.', 'e07-sources-guides')
a('ENDO-ERN', [('ENDO','ENDOcrine (endocrinien)'),('E','European'),('R','Reference'),('N','Network')], 'Réseau européen de référence sur les maladies endocriniennes rares',
  'Réseau européen qui a coordonné le consensus 2020-2021 sur l’hypothyroïdie congénitale, appuyé par la société européenne d’endocrinologie pédiatrique et la société européenne d’endocrinologie.', 'e07-sources-guides')
a('ESPE', [('E','European'),('S','Society for'),('P','Paediatric'),('E','Endocrinology')], 'Société européenne d’endocrinologie pédiatrique',
  'Société savante qui a endossé le consensus 2020-2021 sur l’hypothyroïdie congénitale.', 'e07-sources-guides')
a('NIS', [('N','sodium (Natrium)'),('I','Iodide (iodure)'),('S','Symporter')], 'Symporteur sodium-iodure',
  'Protéine de la membrane basolatérale de la cellule folliculaire qui capte l’iodure du sang ; son gène est SLC5A5.', 'e07-genes')
a('SLC5A5', [('SLC','Solute Carrier (transporteur de soluté), famille'),('5','5'),('A','membre'),('5','5')], 'Gène du symporteur sodium-iodure',
  'Gène de la famille 5, membre 5, des transporteurs de soluté ; ses mutations réduisent ou suppriment la captation de l’iodure.', 'e07-genes')
a('SLC26A4', [('SLC','Solute Carrier (transporteur de soluté), famille'),('26','26'),('A','membre'),('4','4')], 'Gène de la pendrine',
  'Gène de l’échangeur d’anions pendrine ; ses mutations biallèliques causent le syndrome de Pendred.', 'e07-pendred')
a('SLC26A7', [('SLC','Solute Carrier (transporteur de soluté), famille'),('26','26'),('A','membre'),('7','7')], 'Gène d’un transporteur d’anions',
  'Gène associé à un goitre avec hypothyroïdie variable et audition normale.', 'e07-genes')
a('TPO', [('T','Thyro-'),('P','Per-'),('O','Oxydase (peroxydase)')], 'Thyroperoxydase (peroxydase thyroïdienne)',
  'Enzyme de l’organification de l’iode et du couplage ; son déficit donne un défaut complet d’organification, avec hypothyroïdie sévère et goitre.', 'e07-genes')
a('TG', [('T','Thyro-'),('G','Globuline (thyroglobuline)')], 'Thyroglobuline (gène ou protéine)',
  'Précurseur protéique des hormones thyroïdiennes ; dans le consensus, le gène TG est suspecté quand la thyroglobuline sérique est basse.', 'e07-perchlorate')
a('DUOX1', [('DU','DUal'),('OX','OXidase'),('1','type 1')], 'Oxydase duale de type 1',
  'Enzyme productrice de peroxyde d’hydrogène nécessaire à l’hormonosynthèse thyroïdienne.', 'e07-genes')
a('DUOX2', [('DU','DUal'),('OX','OXidase'),('2','type 2')], 'Oxydase duale de type 2',
  'Enzyme productrice de peroxyde d’hydrogène ; ses défauts donnent une hypothyroïdie transitoire ou permanente.', 'e07-genes')
a('DUOXA2', [('DUOX','Dual Oxidase'),('A','Activator (activateur)'),('2','type 2')], 'Activateur de l’oxydase duale de type 2',
  'Chaperon de DUOX2 ; son déficit donne un phénotype proche de celui de DUOX2.', 'e07-genes')
a('IYD', [('IYD','symbole du gène de l’iodotyrosine désiodase (iodotyrosine deiodinase), aussi nommé DEHAL1')], 'Gène de l’iodotyrosine désiodase',
  'Gène du recyclage de l’iode par désiodation des mono- et diiodotyrosines ; son défaut laisse la captation préservée et le test au perchlorate négatif.', 'e07-genes')
a('SERPINA7', [('SERPIN','SERine Protease INhibitor (inhibiteur de sérine protéase), famille'),('A','clade A'),('7','membre 7')], 'Gène de la globuline liant la thyroxine',
  'Gène situé sur le chromosome X (Xq22.2) ; ses mutations causent le déficit en globuline liant la thyroxine.', 'e07-tbg')
a('M918T', [('M','Méthionine'),('918','position 918 de la protéine RET'),('T','Thréonine')], 'Mutation de substitution de la méthionine 918 par une thréonine',
  'Mutation du gène RET associée à la néoplasie endocrinienne multiple de type 2B, pour laquelle la thyroïdectomie est proposée dès que possible.', 'e07-ret')
for _code, _txt in (('E07.0', 'hypersécrétion de calcitonine, hyperplasie des cellules C incluse'), ('E07.1', 'goitre dû à un trouble de l’hormonosynthèse, syndrome de Pendred inclus'),
                    ('E07.8', 'autres affections précisées de la thyroïde'), ('E07.9', 'affection de la thyroïde, sans précision'),
                    ('E03.1', 'hypothyroïdie congénitale sans goitre'), ('P72.0', 'goitre congénital, non classé ailleurs (transitoire, à fonction normale)')):
    a(_code, [(_code, 'code de la CIM-10-GM 2024 : ' + _txt)], _txt[0].upper() + _txt[1:], 'Code de la classification statistique : ' + _txt + '.', 'e07-nosologie')
