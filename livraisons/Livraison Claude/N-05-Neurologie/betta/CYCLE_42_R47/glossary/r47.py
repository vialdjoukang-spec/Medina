"""Abréviations R47 ; ajouts conditionnels, sans mutation des glossaires existants."""
from pathlib import Path
import importlib
_existing = {}
for _path in sorted(Path(__file__).parent.glob('*.py')):
    if _path.stem in {'r47', '__init__'}:
        continue
    _existing.update(getattr(importlib.import_module(_path.stem), 'G', {}))
G = {}
def add_if_absent(key, letters, full, definition, window):
    if key not in _existing:
        G[key] = {'lit': [list(x) for x in letters], 'full': full,
                  'def': '<p>' + definition + '</p>', 'ref': window}

add_if_absent('LAST', [('LA', 'LAnguage (langage)'), ('S', 'Screening (dépistage)'), ('T', 'Test (test)')],
              'Language Screening Test (test de dépistage du langage)',
              'Outil de dépistage de l’aphasie en urgence : cinq sous-tests, 15 items, environ deux minutes, sans logopédiste. Il a été validé en français et en allemand en Suisse.', 'r47-last')
add_if_absent('CIAT', [('CIAT', 'sigle employé tel quel par la revue suisse lue ; développement usuel : Constraint-Induced Aphasia Therapy, thérapie de l’aphasie par contrainte')],
              'CIAT, méthode de rééducation de l’aphasie',
              'La revue suisse de 2013 la dit efficace surtout par son intensité. Le dossier de la leçon n’en détaille pas le protocole.', 'r47-rehab-suisse')
add_if_absent('MIT', [('MIT', 'sigle employé tel quel par la revue suisse lue ; développement usuel : Melodic Intonation Therapy, thérapie par intonation mélodique')],
              'MIT, méthode de rééducation de l’aphasie',
              'La revue suisse de 2013 la dit efficace par la parole rythmée. Le dossier de la leçon n’en détaille pas le protocole.', 'r47-rehab-suisse')
add_if_absent('ICHD-3', [('ICHD', 'International Classification of Headache Disorders (classification internationale des céphalées)'), ('3', 'troisième édition')],
              'Classification internationale des céphalées, troisième édition',
              'Publiée par l’International Headache Society. Le point 1.2, migraine avec aura, fournit les critères de l’aura du langage.', 'r47-aura')
add_if_absent('MSD', [('MSD', 'nom de l’édition du manuel de référence ; le dossier ne fournit pas de développement littéral')],
              'Manuel MSD, édition professionnelle',
              'Manuel nord-américain de référence, utilisé dans cette leçon pour la sémiologie et l’anatomie seulement, jamais comme fondement d’une conduite.', 'r47-aphasie-def')
for _n in ['Bâle-Ville', 'Flamand-Roze', 'Gorno-Tempini', 'Koenig-Bruhin', 'Pitié-Salpêtrière']:
    add_if_absent(_n, [(_n, 'nom propre de lieu ou d’auteur, non une abréviation')], _n,
                  'Nom propre cité dans les références de la leçon sur les troubles du langage.', 'r47-bale')

_codes = {
    'R47.0': ('Dysphasie et aphasie', 'r47-cim'),
    'R47.1': ('Dysarthrie et anarthrie', 'r47-cim'),
    'R47.8': ('Troubles du langage, autres et non précisés', 'r47-cim'),
    'R48.0': ('Dyslexie et alexie', 'r47-cim'),
    'R48.1': ('Agnosie', 'r47-cim'),
    'R48.2': ('Apraxie', 'r47-cim'),
    'R48.8': ('Autres troubles de la fonction symbolique, dont l’agraphie et l’acalculie', 'r47-cim'),
    'R49.0': ('Dysphonie, dont l’enrouement', 'r47-cim'),
    'R49.1': ('Aphonie', 'r47-cim'),
    'R49.2': ('Hyper- et hyponasalité', 'r47-cim'),
    'F44.4': ('Trouble psychogène de la voix', 'r47-cim'),
    'F84.0': ('Autisme (premier code exclu de R47)', 'r47-cim'),
    'F84.1': ('Autisme (second code exclu de R47)', 'r47-cim'),
    'F98.5': ('Bégaiement', 'r47-cim'),
    'F98.6': ('Bredouillement', 'r47-cim'),
    'G31.0': ('Aphasie progressive isolée, exclue de R47.0', 'r47-app'),
}
for _c, (_label, _ref) in _codes.items():
    add_if_absent(_c, [(_c, 'code de la CIM-10-GM 2024 : lettre de chapitre, numéro de catégorie, puis numéro de sous-catégorie')], _c + ', ' + _label,
                  'Code de la classification CIM-10-GM 2024 cité dans la leçon sur les troubles du langage : ' + _label.lower() + '.', _ref)
