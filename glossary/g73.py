"""Abréviations G73 ; ajouts conditionnels, sans mutation des glossaires existants."""
from pathlib import Path
import importlib
_existing = {}
for _path in sorted(Path(__file__).parent.glob('*.py')):
    if _path.stem in {'g73', '__init__'}:
        continue
    _existing.update(getattr(importlib.import_module(_path.stem), 'G', {}))
G = {}
def add_if_absent(key, letters, full, definition, window=None):
    if key not in _existing:
        G[key] = {'lit': [list(x) for x in letters], 'full': full,
                  'def': '<p>' + definition + '</p>', 'ref': window}
def code(key, titre):
    add_if_absent(key, [(key, 'code CIM-10-GM 2024')], titre,
                  'Code cité dans le cours G73 (classification allemande, titres français de l’Office fédéral de la statistique). Le signe † désigne la maladie causale, le signe * sa manifestation neuromusculaire.', 'g73-codage')

code('G73.0', 'Syndrome myasthénique au cours de maladies endocriniennes')
code('G73.1', 'Syndrome de Lambert-Eaton')
code('G73.2', 'Autres syndromes myasthéniques au cours de maladies tumorales')
code('G73.3', 'Syndrome myasthénique au cours d’autres maladies classées ailleurs')
code('G73.4', 'Myopathie au cours de maladies infectieuses et parasitaires classées ailleurs')
code('G73.5', 'Myopathie au cours de maladies endocriniennes')
code('G73.6', 'Myopathie au cours de maladies métaboliques')
code('G73.7', 'Myopathie au cours d’autres maladies classées ailleurs')
code('E21.0', 'Hyperparathyroïdie, maladie causale (code †) citée sous G73.5 ; la plage citée va de E21.0 à E21.3')
code('E21.3', 'Hyperparathyroïdie, maladie causale (code †) citée sous G73.5 ; la plage citée va de E21.0 à E21.3')
code('E74.0', 'Glycogénose, maladie causale (code †) citée sous G73.6')
code('M35.0', 'Syndrome sec, maladie causale (code †) citée sous G73.7')
code('M34.8', 'Sclérodermie, maladie causale (code †) citée sous G73.7')
code('M32.1', 'Lupus érythémateux systémique, maladie causale (code †) citée sous G73.7')

add_if_absent('CIM', [('C','Classification'),('I','Internationale des'),('M','Maladies')], 'Classification internationale des maladies',
              'Ce cours emploie la version allemande CIM-10-GM 2024, dont les titres français viennent de l’Office fédéral de la statistique. La cartographie vers la CIM-11 reste à établir.', 'g73-codage')
add_if_absent('SMLE', [('S','Syndrome'),('M','Myasthénique de'),('LE','Lambert-Eaton')], 'Syndrome myasthénique de Lambert-Eaton',
              'Maladie auto-immune rare de la jonction neuromusculaire : faiblesse proximale, réflexes abolis, dysautonomie. Elle est classée G73.1*.', 'g73-smle')
add_if_absent('LEMS', [('LE','Lambert-Eaton'),('M','Myasthenic'),('S','Syndrome')], 'Lambert-Eaton myasthenic syndrome, nom anglais du SMLE',
              'Les sources anglaises emploient cette abréviation pour le syndrome myasthénique de Lambert-Eaton.', 'g73-smle')
add_if_absent('PNS-Care', [('PNS','Paraneoplastic Neurologic Syndrome'),('Care','nom du score, non développé dans le dossier lu')], 'Critères PNS-Care 2021 des syndromes neurologiques paranéoplasiques',
              'Ce consensus international (coordination à Lyon) classe le syndrome de Lambert-Eaton parmi les phénotypes à haut risque de syndrome paranéoplasique.', 'g73-smle')
add_if_absent('DELTA-P', [('D','Dutch'),('E','English'),('L','LEMS'),('T','Tumour'),('A','Association'),('P','Prediction')], 'Dutch-English LEMS Tumour Association Prediction',
              'Ce score calculé au diagnostic estime le risque de carcinome bronchique à petites cellules dans le syndrome de Lambert-Eaton. Il comporte six items.', 'g73-deltap')
add_if_absent('VGCC', [('V','Voltage'),('G','Gated'),('C','Calcium'),('C','Channel')], 'Voltage-gated calcium channel, canal calcique voltage-dépendant',
              'Les anticorps dirigés contre les canaux de type P/Q réduisent la libération d’acétylcholine dans le syndrome de Lambert-Eaton.', 'g73-vgcc')
add_if_absent('CK', [('C','Créatine'),('K','Kinase')], 'Créatine kinase',
              'Enzyme musculaire dosée dans le sang. Elle est normale ou peu élevée dans la myopathie cortisonique et très élevée dans les myopathies nécrosante et bénigne de l’enfant citées par le cours.', 'g73-cortisone')
add_if_absent('PAMC', [('P','Potentiel d’'),('A','Action'),('M','Musculaire'),('C','Composé')], 'Potentiel d’action musculaire composé',
              'Réponse électrique globale du muscle à la stimulation de son nerf ; son amplitude de repos est basse dans le syndrome de Lambert-Eaton.', 'g73-pamc')
add_if_absent('ROC', [('R','Receiver'),('O','Operating'),('C','Characteristic')], 'Receiver operating characteristic',
              'La courbe ROC résume la performance d’un score ; une aire de 82,5 % est rapportée pour DELTA-P.', 'g73-deltap')
add_if_absent('QMG', [('Q','Quantitative'),('M','Myasthenia'),('G','Gravis')], 'Quantitative Myasthenia Gravis, score de force',
              'Score utilisé dans les essais de l’amifampridine ; une baisse de 2,44 points est rapportée par la revue Cochrane.', 'g73-amifampridine')
add_if_absent('mV', [('m','milli'),('V','volt')], 'Millivolt',
              'Unité d’amplitude du potentiel d’action musculaire composé.', 'g73-increment')
add_if_absent('NAT2', [('NAT','N-Acétyltransférase'),('2','isoforme numéro 2')], 'N-acétyltransférase 2',
              'Enzyme qui acétyle l’amifampridine. Les acétyleurs lents ont une exposition plus forte et davantage d’effets indésirables.', 'g73-firdapse-pk')
add_if_absent('SOX1', [('SOX','SRY-related HMG-box, famille de gènes'),('1','numéro 1')], 'Anticorps SOX1 (anti-nucléaires gliaux)',
              'Fortement associés au carcinome bronchique à petites cellules ; les line-blots commerciaux donnent beaucoup de faux résultats.', 'g73-cbpc')
add_if_absent('SOX2', [('SOX','SRY-related HMG-box, famille de gènes'),('2','numéro 2')], 'Anticorps SOX2',
              'Détectés chez 61 % des syndromes de Lambert-Eaton avec carcinome bronchique à petites cellules, avec une spécificité supérieure à 90 %.', 'g73-cbpc')
add_if_absent('SRP', [('S','Signal'),('R','Recognition'),('P','Particle')], 'Signal recognition particle',
              'Les anticorps anti-SRP définissent une myopathie nécrosante auto-immune, citée comme erreur possible de diagnostic avec la myopathie hypothyroïdienne.', 'g73-srp')
add_if_absent('FcRn', [('Fc','Fragment cristallisable'),('R','Receptor'),('n','neonatal')], 'Récepteur néonatal du fragment Fc',
              'Cible de biologiques testés surtout dans la myasthénie ; aucune donnée lue ne les valide dans le syndrome de Lambert-Eaton.', 'g73-immuno')
add_if_absent('IGF-1', [('I','Insulin-like'),('G','Growth'),('F','Factor'),('1','numéro 1')], 'Insulin-like growth factor 1',
              'Voie de synthèse protéique inhibée par les glucocorticoïdes dans la myopathie cortisonique.', 'g73-cortisone')
add_if_absent('FOXO', [('F','Forkhead'),('O','box O')], 'Forkhead box O',
              'Facteurs qui activent la dégradation des protéines musculaires sous glucocorticoïdes.', 'g73-cortisone')
add_if_absent('MuRF-1', [('Mu','Muscle'),('RF','RING-Finger'),('1','numéro 1')], 'Muscle RING-finger 1',
              'Atrogène, c’est-à-dire gène de l’atrophie musculaire, activé dans la myopathie cortisonique.', 'g73-cortisone')
add_if_absent('A0', [('A','Amplitude'),('0','de repos')], 'Amplitude de repos du PAMC',
              'Variable de la formule de l’incrément ; A1 désigne l’amplitude après contraction maximale.', 'g73-increment')
add_if_absent('A1', [('A','Amplitude'),('1','après contraction maximale')], 'Amplitude du PAMC après contraction maximale',
              'Variable de la formule de l’incrément ; A0 désigne l’amplitude de repos.', 'g73-increment')
add_if_absent('AG', [('AG','Aktiengesellschaft, société anonyme')], 'Aktiengesellschaft',
              'Forme juridique du titulaire suisse de Firdapse®.', 'g73-firdapse-poso')
for _k, _t, _d in [
    ('DRAC', 'DRAC, titulaire suisse de Firdapse®', 'Nom de société, non une abréviation.'),
    ('MEDA', 'MEDA, titulaire suisse de Mestinon®', 'Nom de société, non une abréviation.'),
    ('Lambert-Eaton', 'Lambert-Eaton, noms propres des auteurs du syndrome', 'Noms de famille de deux auteurs, non une abréviation.'),
    ('Pays-Bas', 'Pays-Bas, nom d’un pays', 'Nom propre, non une abréviation.'),
    ('Dutch-English', 'Dutch-English, mots anglais', 'Mots anglais « néerlandais-anglais » du nom du score DELTA-P.'),
    ('Géfard-Gontier', 'Géfard-Gontier, premier auteur d’une revue', 'Nom de famille composé, non une abréviation.'),
    ('Remijn-Nelissen', 'Remijn-Nelissen, premier auteur d’un essai', 'Nom de famille composé, non une abréviation.')]:
    add_if_absent(_k, [(_k, 'nom propre, non une abréviation')], _t, _d, 'g73-lacunes')
