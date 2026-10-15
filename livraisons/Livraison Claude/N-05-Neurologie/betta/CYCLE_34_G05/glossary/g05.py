"""Abréviations G05 (Encéphalite, myélite et encéphalomyélite au cours d’affections classées ailleurs) ; ajouts conditionnels, sans mutation des glossaires existants."""
from pathlib import Path
import importlib
_existing = {}
for _path in sorted(Path(__file__).parent.glob('*.py')):
    if _path.stem in {'g05', '__init__'}:
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

add_if_absent('HSV', [('H', 'Herpes'), ('S', 'Simplex'), ('V', 'Virus')],
              'Virus de l’herpès simplex',
              'HSV-1 provoque chez l’adulte une encéphalite nécrosante focale, temporale médio-basale, traitée sans délai par l’aciclovir ; HSV-2 donne chez le nouveau-né une encéphalite hémorragique nécrosante diffuse.', 'g05-hsve')
add_if_absent('EBV', [('E', 'Epstein'), ('B', 'Barr'), ('V', 'Virus')],
              'Virus d’Epstein-Barr',
              'Ce virus provoque une encéphalite surtout chez l’immunodéprimé, notamment le transplanté ; la PCR du LCR peut être faussement positive en cas de pléiocytose.', 'g05-cmv')
add_if_absent('JCV', [('JC', 'nom d’usage du virus JC, non développé lettre à lettre dans les sources lues'), ('V', 'Virus')],
              'Virus JC',
              'Ce virus figure parmi les agents à rechercher chez l’immunodéprimé et au palier 3 de la recherche virale.', 'g05-pcr')
add_if_absent('HHV-6', [('H', 'Human'), ('H', 'Herpes'), ('V', 'Virus'), ('6', 'type 6')],
              'Virus herpès humain de type 6',
              'Il figure parmi les agents à rechercher chez l’immunodéprimé et au palier 3 de la recherche virale.', 'g05-pcr')
add_if_absent('LCMV', [('L', 'Lymphocytic'), ('C', 'Choriomeningitis'), ('M', 'Mammarenavirus (nom d’usage)'), ('V', 'Virus')],
              'Virus de la chorioméningite lymphocytaire',
              'Ce virus figure au palier 4 de la recherche virale, avec les situations spéciales.', 'g05-pcr')
add_if_absent('NGS', [('N', 'Next'), ('G', 'Generation'), ('S', 'Sequencing')],
              'Séquençage de nouvelle génération',
              'Avec les panels PCR multiplex, il est réservé aux cas où l’étiologie reste inconnue après le bilan standard.', 'g05-pcr')
add_if_absent('ADEM', [('A', 'Acute'), ('D', 'Disseminated'), ('E', 'Encephalo'), ('M', 'Myelitis')],
              'Encéphalomyélite aiguë disséminée',
              'Processus immunitaire post- ou para-infectieux, cité dans le diagnostic différentiel de l’encéphalite.', 'g05-graus')
add_if_absent('DGN', [('D', 'Deutsche'), ('G', 'Gesellschaft'), ('N', 'für Neurologie')],
              'Deutsche Gesellschaft für Neurologie (Société allemande de neurologie)',
              'Cette société savante allemande publie, avec l’AWMF, la ligne directrice 030/100 sur la méningo-encéphalite virale (2025), élaborée avec un représentant de la Société suisse de neurologie. Elle fonde ce cours.', 'g05-criteres')
add_if_absent('SNG', [('S', 'Schweizerische'), ('N', 'Neurologische'), ('G', 'Gesellschaft')],
              'Schweizerische Neurologische Gesellschaft (Société suisse de neurologie)',
              'Un de ses représentants a participé à la ligne directrice de 2025 et la société a approuvé la ligne directrice allemande de la neurosyphilis (2020).', 'g05-criteres')
add_if_absent('MONALISA', [('MONALISA', 'nom de la cohorte nationale prospective française de listériose ; la publication lue ne fournit aucun développement littéral')],
              'Cohorte MONALISA',
              'Cette cohorte (Lancet Infectious Diseases, 2017) compte 252 neurolistérioses ; elle montre une atteinte du tronc cérébral dans 17 % des cas et une mortalité plus élevée sous dexaméthasone adjuvante.', 'g05-dexa')
add_if_absent('GACHE', [('GACHE', 'nom d’un essai, non développé lettre à lettre dans la source lue')],
              'Essai GACHE',
              'Cet essai sur les corticoïdes dans l’encéphalite herpétique a été arrêté faute de recrutement.', 'g05-hsve')
add_if_absent('DexEnceph', [('DexEnceph', 'nom d’un essai, non développé lettre à lettre dans la source lue')],
              'Essai DexEnceph',
              'Ses résultats ne sont pas publiés selon la ligne directrice allemande de 2025.', 'g05-hsve')
add_if_absent('FTA-ABS', [('FTA', 'Fluorescent Treponemal Antibody'), ('ABS', 'Absorption')],
              'Test d’absorption des anticorps tréponémiques fluorescents',
              'Test de confirmation de la sérologie tréponémique de la neurosyphilis ; il reste positif à vie et ne sert pas au suivi.', 'g05-neurosyphilis')
add_if_absent('TPLA', [('TP', 'Treponema Pallidum'), ('LA', 'Latex Agglutination')],
              'Agglutination de particules de latex de Treponema pallidum',
              'Test tréponémique de la sérologie syphilitique, avec TPPA et TPHA.', 'g05-neurosyphilis')
add_if_absent('ROR', [('R', 'Rougeole'), ('O', 'Oreillons'), ('R', 'Rubéole')],
              'Vaccin rougeole, oreillons, rubéole',
              'En Suisse, deux doses sont données à 9 et 12 mois, avec rattrapage à tout âge chez la personne non immune.', 'g05-fsme')
add_if_absent('ROR-V', [('R', 'Rougeole'), ('O', 'Oreillons'), ('R', 'Rubéole'), ('V', 'Varicelle')],
              'Vaccin rougeole, oreillons, rubéole, varicelle',
              'Il est préféré depuis 2023 selon l’OFSP.', 'g05-fsme')
add_if_absent('FSME', [('F', 'Früh'), ('S', 'Sommer'), ('M', 'Meningo'), ('E', 'Enzephalitis')],
              'Encéphalite à tiques (Frühsommer-Meningoenzephalitis)',
              'Maladie à déclaration obligatoire en Suisse ; elle se code A84 sans lien avec G05.1*.', 'g05-fsme')
add_if_absent('PLED', [('P', 'Periodic'), ('L', 'Lateralized'), ('E', 'Epileptiform'), ('D', 'Discharges')],
              'Décharges épileptiformes latéralisées périodiques',
              'Aspect de l’EEG décrit dans l’encéphalite herpétique.', 'g05-eeg')
add_if_absent('GCS', [('G', 'Glasgow'), ('C', 'Coma'), ('S', 'Scale')],
              'Échelle de coma de Glasgow',
              'Un score inférieur à 12 est associé à une mortalité plus élevée à 6 mois dans la cohorte danoise.', 'g05-hsve')
add_if_absent('anti-NMDAR', [('anti', 'dirigé contre'), ('N', 'N-'), ('M', 'Méthyl-'), ('D', 'D-'), ('A', 'Aspartate'), ('R', 'Receptor (récepteur)')],
              'Anticorps anti-récepteur NMDA',
              'Ces anticorps caractérisent une encéphalite auto-immune qui peut suivre une encéphalite herpétique de semaines à mois.', 'g05-antinmda')
add_if_absent('EAN', [('E', 'European'), ('A', 'Academy of'), ('N', 'Neurology')],
              'Académie européenne de neurologie',
              'Elle est citée par la ligne directrice allemande pour des recommandations non lues directement.', 'g05-lacunes')
add_if_absent('EFNS', [('E', 'European'), ('F', 'Federation of'), ('N', 'Neurological'), ('S', 'Societies')],
              'Fédération européenne des sociétés neurologiques',
              'Elle est citée par la ligne directrice allemande pour la recommandation européenne de l’encéphalite, non lue directement.', 'g05-lacunes')
for _k, _t, _w in [
    ('G04.8', 'encéphalite auto-immune (hors G05)', 'g05-graus'),
    ('G05.0', 'au cours d’infections bactériennes classées ailleurs', 'g05-codage'),
    ('G05.1', 'au cours d’infections virales classées ailleurs', 'g05-codage'),
    ('G05.2', 'au cours d’autres maladies infectieuses et parasitaires classées ailleurs', 'g05-codage'),
    ('G05.8', 'au cours d’autres maladies classées ailleurs', 'g05-codage'),
    ('G31.2', 'encéphalopathie alcoolique', 'g05-codage'),
    ('G37.3', 'myélite transverse aiguë', 'g05-codage'),
    ('G37.4', 'syndrome de Foix-Alajouanine', 'g05-codage'),
    ('G93.4', 'encéphalopathie sans précision', 'g05-codage'),
    ('A17.8', 'tuberculose', 'g05-codage'),
    ('A32.1', 'Listeria', 'g05-codage'),
    ('A39.8', 'méningocoque', 'g05-codage'),
    ('A50.4', 'syphilis congénitale', 'g05-codage'),
    ('A52.1', 'syphilis tardive', 'g05-codage'),
    ('A85.0', 'entérovirus', 'g05-codage'),
    ('A85.1', 'adénovirus', 'g05-codage'),
    ('B00.4', 'herpès simplex', 'g05-codage'),
    ('B01.1', 'varicelle', 'g05-codage'),
    ('B02.0', 'zona', 'g05-codage'),
    ('B05.0', 'rougeole', 'g05-codage'),
    ('B06.0', 'rubéole', 'g05-codage'),
    ('B26.2', 'oreillons', 'g05-codage'),
    ('B25.88', 'cytomégalovirus', 'g05-codage'),
    ('B57.4', 'maladie de Chagas chronique', 'g05-codage'),
    ('B58.2', 'toxoplasmose', 'g05-codage'),
    ('B60.2', 'Naegleria', 'g05-codage'),
    ('B83.2', 'méningo-encéphalite à éosinophiles', 'g05-codage'),
    ('J10.8', 'grippe', 'g05-codage'),
    ('J11.8', 'grippe', 'g05-codage'),
    ('M32.1', 'encéphalopathie du lupus érythémateux systémique', 'g05-lupus'),
]:
    add_if_absent(_k, [(_k, 'code de la CIM-10-GM 2024, non une abréviation')], _t,
                  'Code de la CIM-10-GM 2024 cité dans ce cours, associé à : ' + _t + '.', _w)
add_if_absent('Foix-Alajouanine', [('Foix-Alajouanine', 'nom propre de deux médecins, non une abréviation')], 'Syndrome de Foix-Alajouanine', 'Myélite nécrosante subaiguë, exclue de G04 par la CIM-10-GM 2024.', 'g05-codage')
