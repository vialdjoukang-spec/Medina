"""Abréviations G58 ; ajouts conditionnels, sans mutation des glossaires existants."""
from pathlib import Path
import importlib
_existing = {}
for _path in sorted(Path(__file__).parent.glob('*.py')):
    if _path.stem in {'g58', '__init__'}:
        continue
    _existing.update(getattr(importlib.import_module(_path.stem), 'G', {}))
G = {}
def add_if_absent(key, letters, full, definition, window):
    if key not in _existing:
        G[key] = {'lit': [list(x) for x in letters], 'full': full,
                  'def': '<p>' + definition + '</p>', 'ref': window}
add_if_absent('NSVN', [('N', 'Non'), ('S', 'Systemic'), ('V', 'Vasculitic'), ('N', 'Neuropathy')],
              'Neuropathie vasculitique non systémique',
              'Vascularite limitée aux vaisseaux du nerf, sans atteinte d’un autre organe. La Peripheral Nerve Society en a publié les critères en 2010.', 'g58-pns')
add_if_absent('PAN', [('P', 'Périartérite'), ('A', 'Artérite'), ('N', 'Noueuse')],
              'Périartérite noueuse',
              'Vascularite primaire systémique des artères de moyen calibre ; la neuropathie y atteint 65 à 85 % des cas selon une revue de 2015.', 'g58-vasculites')
add_if_absent('GPA', [('G', 'Granulomatose'), ('P', 'avec Poly-'), ('A', 'angéite')],
              'Granulomatose avec polyangéite',
              'Vascularite associée aux ANCA, le plus souvent de type anti-PR3 ; la neuropathie y varie de 5 à 50 % selon les séries.', 'g58-vasculites')
add_if_absent('MPA', [('M', 'Microscopic'), ('P', 'Poly-'), ('A', 'angiitis')],
              'Polyangéite microscopique',
              'Vascularite associée aux ANCA, le plus souvent de type anti-MPO ; la neuropathie y varie de 6 à 75 % selon les séries.', 'g58-vasculites')
add_if_absent('ACNES', [('A', 'Anterior'), ('C', 'Cutaneous'), ('N', 'Nerve'), ('E', 'Entrapment'), ('S', 'Syndrome')],
              'Syndrome de piégeage des nerfs cutanés antérieurs',
              'Piégeage de branches des nerfs intercostaux T7 à T12 dans les muscles grands droits, à l’origine d’une douleur pariétale abdominale.', 'g58-acnes')
add_if_absent('VS', [('V', 'Vitesse'), ('S', 'de Sédimentation')],
              'Vitesse de sédimentation',
              'Mesure de l’inflammation. Une valeur d’au moins 100 mm/h plaide contre une neuropathie vasculitique non systémique (Peripheral Nerve Society 2010).', 'g58-pns')
add_if_absent('IgIV', [('Ig', 'Immunoglobulines'), ('IV', 'IntraVeineuses')],
              'Immunoglobulines intraveineuses',
              'Leur usage dans les vascularites à ANCA réfractaires repose sur des séries de cas et reste hors indication.', 'g58-ritux')
add_if_absent('EFNS', [('E', 'European'), ('F', 'Federation of'), ('N', 'Neurological'), ('S', 'Societies')],
              'Fédération européenne des sociétés de neurologie',
              'Elle a publié en 2010 les lignes directrices sur le traitement de la douleur neuropathique et sur la neuroborréliose. Elle est devenue l’Académie européenne de neurologie.', 'g58-neurontin')
add_if_absent('EMG', [('É', 'Électro'), ('M', 'Myo'), ('G', 'Gramme')],
              'Électromyogramme',
              'Examen de l’activité électrique du muscle ; il montre ici des signes neurogènes.', 'g58-ncs')
add_if_absent('ANA', [('A', 'Anti'), ('N', 'Nuclear'), ('A', 'Antibodies')],
              'Anticorps antinucléaires',
              'Auto-anticorps recherchés dans le bilan d’une vascularite suspectée.', 'g58-anca')
add_if_absent('pANCA', [('p', 'périnucléaire'), ('ANCA', 'Anticorps anti-cytoplasme des polynucléaires neutrophiles')],
              'ANCA de type périnucléaire',
              'Les pANCA sont retrouvés dans 40 à 70 % des EGPA selon une revue de 2015.', 'g58-anca')
add_if_absent('PNS', [('P', 'Peripheral'), ('N', 'Nerve'), ('S', 'Society')],
              'Peripheral Nerve Society',
              'Société internationale qui a publié en 2010 la ligne directrice sur la neuropathie vasculitique non systémique.', 'g58-pns')
add_if_absent('CMAP', [('C', 'Compound'), ('M', 'Muscle'), ('A', 'Action'), ('P', 'Potential')],
              'Potentiel d’action musculaire composé',
              'Amplitude du potentiel moteur recueilli à la neurographie ; elle diminue en cas de perte axonale.', 'g58-ncs')
add_if_absent('T7', [('T', 'Thoracique'), ('7', 'septième segment')],
              'Septième segment thoracique',
              'Niveau supérieur des branches des nerfs intercostaux concernées par l’ACNES.', 'g58-acnes')
add_if_absent('T12', [('T', 'Thoracique'), ('12', 'douzième segment')],
              'Douzième segment thoracique',
              'Niveau inférieur des branches des nerfs intercostaux concernées par l’ACNES.', 'g58-acnes')
add_if_absent('O-A-C-V', [('O', 'Organe'), ('A', 'ANCA'), ('C', 'Cryoglobulines'), ('V', 'VS ≥ 100 mm/h')],
              'Aide mémoire O-A-C-V',
              'Aide pédagogique, non critère officiel : quatre arguments en faveur d’une vascularite systémique plutôt que d’une NSVN.', 'g58-mnemo')
add_if_absent('G58.0', [('G58.0', 'code de la CIM-10-GM 2024 : névrite intercostale ; identifiant de classification, non une abréviation lettre à lettre')],
              'Névrite intercostale',
              'Code de la classification CIM-10-GM 2024 utilisé pour situer la catégorie.', 'g58-cim')
add_if_absent('G58.7', [('G58.7', 'code de la CIM-10-GM 2024 : mononévrite de sièges multiples ; identifiant de classification, non une abréviation lettre à lettre')],
              'Mononévrite de sièges multiples',
              'Code de la classification CIM-10-GM 2024 utilisé pour situer la catégorie.', 'g58-cim')
add_if_absent('G58.8', [('G58.8', 'code de la CIM-10-GM 2024 : autres mononévrites précisées ; identifiant de classification, non une abréviation lettre à lettre')],
              'Autres mononévrites précisées',
              'Code de la classification CIM-10-GM 2024 utilisé pour situer la catégorie.', 'g58-cim')
add_if_absent('G58.9', [('G58.9', 'code de la CIM-10-GM 2024 : mononévrite sans précision ; identifiant de classification, non une abréviation lettre à lettre')],
              'Mononévrite sans précision',
              'Code de la classification CIM-10-GM 2024 utilisé pour situer la catégorie.', 'g58-cim')
add_if_absent('M79.2', [('M79.2', 'code de la CIM-10-GM 2024 : névralgie et névrite sans précision ; identifiant de classification, non une abréviation lettre à lettre')],
              'Névralgie et névrite sans précision',
              'Code de la classification CIM-10-GM 2024 utilisé pour situer la catégorie.', 'g58-cim')
add_if_absent('O26.83', [('O26.83', 'code de la CIM-10-GM 2024 : névrite périphérique de la grossesse ; identifiant de classification, non une abréviation lettre à lettre')],
              'Névrite périphérique de la grossesse',
              'Code de la classification CIM-10-GM 2024 utilisé pour situer la catégorie.', 'g58-cim')
add_if_absent('M54.1', [('M54.1', 'code de la CIM-10-GM 2024 : radiculite sans précision ; identifiant de classification, non une abréviation lettre à lettre')],
              'Radiculite sans précision',
              'Code de la classification CIM-10-GM 2024 utilisé pour situer la catégorie.', 'g58-cim')
add_if_absent('G59.0', [('G59.0', 'code de la CIM-10-GM 2024 : mononeuropathie diabétique ; identifiant de classification, non une abréviation lettre à lettre')],
              'Mononeuropathie diabétique',
              'Code de la classification CIM-10-GM 2024 utilisé pour situer la catégorie.', 'g58-cim')
add_if_absent('G59.8', [('G59.8', 'code de la CIM-10-GM 2024 : autres mononeuropathies au cours de maladies classées ailleurs ; identifiant de classification, non une abréviation lettre à lettre')],
              'Autres mononeuropathies au cours de maladies classées ailleurs',
              'Code de la classification CIM-10-GM 2024 utilisé pour situer la catégorie.', 'g58-cim')
add_if_absent('G53.0', [('G53.0', 'code de la CIM-10-GM 2024 : névralgie post-zostérienne, nerfs crâniens ; identifiant de classification, non une abréviation lettre à lettre')],
              'Névralgie post-zostérienne, nerfs crâniens',
              'Code de la classification CIM-10-GM 2024 utilisé pour situer la catégorie.', 'g58-cim')
add_if_absent('B02.2', [('B02.2', 'code de la CIM-10-GM 2024 : zona avec atteinte du système nerveux ; identifiant de classification, non une abréviation lettre à lettre')],
              'Zona avec atteinte du système nerveux',
              'Code de la classification CIM-10-GM 2024 utilisé pour situer la catégorie.', 'g58-cim')
