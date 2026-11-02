"""Abréviations G24 Dystonie ; ajouts conditionnels, sans mutation des glossaires existants."""
from pathlib import Path
import importlib, sys
_here = Path(__file__).resolve().parent
_root = next((p for p in _here.parents if (p / 'build_medina.py').exists()), None)
_dirs = [_here] + ([_root / 'glossary'] if _root else [])
_existing = {}
for _d in _dirs:
    if str(_d) not in sys.path:
        sys.path.append(str(_d))
    for _path in sorted(_d.glob('*.py')):
        if _path.stem in {'g24', '__init__'}:
            continue
        try:
            _existing.update(getattr(importlib.import_module(_path.stem), 'G', {}))
        except Exception:
            pass
G = {}
def add_if_absent(key, letters, full, definition, window):
    if key not in _existing:
        G[key] = {'lit': [list(x) for x in letters], 'full': full,
                  'def': '<p>' + definition + '</p>', 'ref': window}

add_if_absent('GCH1', [('GCH1', 'symbole du gène GTP cyclohydrolase 1')], 'GTP cyclohydrolase 1', 'Enzyme impliquée dans la voie de biosynthèse du cofacteur BH4 ; certaines variations du gène sont liées à une dystonie dopa-sensible. Ce n’est pas un protocole posologique.', 'g24-gch1')
add_if_absent('BH4', [('BH4', 'notation usuelle de la tétrahydrobioptérine')], 'Tétrahydrobioptérine', 'Cofacteur utilisé notamment par la tyrosinehydroxylase dans la synthèse de L-DOPA.', 'g24-gch1')
add_if_absent('SNAP-25', [('SNAP', 'synaptosomal-associated protein'), ('25', 'masse nominale de 25 kilodaltons')], 'Protéine synaptique SNAP-25', 'Cible de clivage de la toxine botulique A, impliquée dans la libération présynaptique du neurotransmetteur.', 'g24-toxin')
add_if_absent('TWSTRS', [('T', 'Toronto'), ('W', 'Western'), ('S', 'Spasmodic'), ('T', 'Torticollis'), ('R', 'Rating'), ('S', 'Scale')], 'Toronto Western Spasmodic Torticollis Rating Scale', 'Échelle cervicale, à choisir avec les objectifs fonctionnels et les autres mesures adaptées.', 'g24-scales')
add_if_absent('BFMDRS', [('B', 'Burke'), ('F', 'Fahn'), ('M', 'Marsden'), ('D', 'Dystonia'), ('R', 'Rating'), ('S', 'Scale')], 'Burke-Fahn-Marsden Dystonia Rating Scale', 'Outil de mesure de la dystonie, sans valeur de diagnostic étiologique ni seuil universel de guérison.', 'g24-scales')
add_if_absent('ESDE', [('E', 'Epidemiological'), ('S', 'Study of'), ('D', 'Dystonia in'), ('E', 'Europe')], 'Epidemiological Study of Dystonia in Europe', 'Groupe de l’étude européenne publiée en 2000 sur cas adultes diagnostiqués en 1996–1997 ; résumé primaire lu. À distinguer d’ESEMED.', 'g24-exp-2')
add_if_absent('GPi', [('GP', 'globus pallidus'), ('i', 'interne')], 'Segment interne du globus pallidus', 'Structure de référence et cible possible de stimulation dans certaines dystonies sélectionnées, sans bénéfice individuel garanti.', 'g24-dbs')
add_if_absent('BoNT-A', [('BoNT', 'botulinum neurotoxin'), ('A', 'type A')], 'Neurotoxine botulique de type A', 'Les préparations commerciales ont des unités, indications et intervalles propres, non interchangeables.', 'g24-units')
add_if_absent('EMG', [('É', 'électro'), ('M', 'myo'), ('G', 'graphie')], 'Électromyographie', 'Examen de l’activité électrique musculaire, parfois utile au diagnostic différentiel ou au guidage ; ne donne pas seule l’étiologie centrale.', 'g24-exam')
