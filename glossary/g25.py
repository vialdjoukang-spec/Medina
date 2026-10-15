"""Abréviations G25 — ajouts conditionnels, sans écraser un terme déjà défini ailleurs."""
from pathlib import Path
import importlib
_existing = {}
for _path in sorted(Path(__file__).parent.glob('*.py')):
    if _path.stem in {'g25', '__init__'}:
        continue
    try:
        _existing.update(getattr(importlib.import_module(_path.stem), 'G', {}))
    except Exception:
        pass
G = {}
def a(key, lit, full, definition, ref=None):
    if key not in _existing:
        G[key] = {'lit': [list(x) for x in lit], 'full': full, 'def': '<p>' + definition + '</p>', 'ref': ref}

def code(key, label, ref='g25-codage'):
    a(key, [(key[0], 'Lettre du chapitre de la CIM-10-GM'), (key[1:], 'numéro de catégorie et de sous-code')], 'Code CIM-10-GM ' + key,
      'Code de la classification CIM-10-GM 2024 : ' + label + '.', ref)

a('CIM', [('C','Classification'),('I','Internationale des'),('M','Maladies')], 'Classification internationale des maladies',
  'Classification de l’Organisation mondiale de la santé. Le catalogue du dépôt suit la CIM-10-GM 2024 ; la correspondance avec la CIM-11 n’est pas établie.', 'g25-codage')
a('XX', [('XX', 'chapitre vingt de la CIM-10-GM : causes externes de morbidité et de mortalité')], 'Chapitre XX de la CIM-10-GM',
  'Les codes G25.1 et G25.4 demandent un code supplémentaire de ce chapitre pour identifier la substance responsable du tremblement ou de la chorée.', 'g25-codage')
code('F95.2', 'syndrome de Gilles de la Tourette, exclu de G25')
code('F95.9', 'tic non précisé, exclu de G25.6')
code('R25.1', 'tremblement non précisé, exclu de G25.0')
code('G51.4', 'myokymie faciale, exclue de G25.3')
for k, lab in [('G25.0','tremblement essentiel, y compris familial'),('G25.1','tremblement dû à des médicaments'),
               ('G25.2','autres formes précisées de tremblement, y compris intentionnel'),('G25.3','myoclonie, y compris médicamenteuse'),
               ('G25.4','chorée médicamenteuse'),('G25.5','autres chorées'),
               ('G25.6','tics médicamenteux et autres tics d’origine organique'),
               ('G25.80','mouvements périodiques des jambes au cours du sommeil'),('G25.81','syndrome des jambes sans repos'),
               ('G25.88','autres syndromes extrapyramidaux précisés, y compris akathisie et syndrome de l’homme raide'),
               ('G25.9','syndrome extrapyramidal et trouble de la motricité, sans précision')]:
    code(k, lab)
a('DGN', [('D','Deutsche'),('G','Gesellschaft'),('N','für Neurologie')], 'Société allemande de neurologie',
  'Cette société publie, avec les sociétés autrichienne et suisse de neurologie, les lignes directrices S2k sur le tremblement, le syndrome des jambes sans repos et la chorée.', 'g25-div-psg')
a('DGSM', [('D','Deutsche'),('G','Gesellschaft'),('S','für Schlafforschung'),('M','und Schlafmedizin')], 'Société allemande de recherche sur le sommeil et de médecine du sommeil',
  'Cette société cosigne la ligne directrice 2024 sur le syndrome des jambes sans repos.', 'g25-div-psg')
a('GABAergique', [('GABA','acide gamma-aminobutyrique'),('ergique','qui agit par ce neuromédiateur')], 'Qui agit par l’acide gamma-aminobutyrique',
  'Adjectif désignant les neurones ou les transmissions qui utilisent le GABA, neuromédiateur inhibiteur. Ils sont altérés dans la myoclonie corticale et le syndrome de l’homme raide.', 'g25-stiffperson')
a('GABAergiques', [('GABA','acide gamma-aminobutyrique'),('ergiques','qui agissent par ce neuromédiateur')], 'Qui agissent par l’acide gamma-aminobutyrique',
  'Pluriel de GABAergique : interneurones inhibiteurs dont la dysfonction est invoquée dans la myoclonie corticale.', 'g25-myoclonie-class')
for k, n in [('MEIS1','MEIS homeobox 1'),('BTBD9','BTB domain containing 9'),('MAP2K4','Mitogen-activated protein kinase kinase 4'),
             ('PTPRD','Protein tyrosine phosphatase receptor type D'),('TOX3','TOX high mobility group box family member 3')]:
    a(k, [(k, 'symbole de gène ; le développement littéral n’est pas fourni par les sources lues')], 'Gène ' + k,
      'Ce gène figure parmi les loci associés au syndrome des jambes sans repos dans la méta-analyse pangénomique 2024.', 'g25-sjsr-criteres')
a('anti-GAD65', [('anti','contre'),('GAD','acide Glutamique Décarboxylase'),('65','isoforme de 65 kilodaltons')], 'Anticorps dirigés contre la décarboxylase de l’acide glutamique 65',
  'Anticorps présents à titre élevé chez la plupart des patients avec syndrome de l’homme raide ; la GAD65 est l’enzyme de synthèse du GABA.', 'g25-stiffperson')
a('anti-TPO', [('anti','contre'),('T','Thyréo'),('P','Peroxydase'),('O','—')], 'Anticorps dirigés contre la thyréopéroxydase',
  'Dosage inscrit dans le bilan de la chorée sporadique.', 'g25-bilan-choree')
a('CAG', [('C','Cytosine'),('A','Adénine'),('G','Guanine')], 'Triplet cytosine-adénine-guanine',
  'Les répétitions de ce triplet définissent la maladie de Huntington ; le dossier cite des allèles intermédiaires de 27 à 35 répétitions.', 'g25-huntington')
a('Stiff-Person', [('Stiff-Person','nom anglais du syndrome de l’homme raide, non une abréviation')], 'Stiff-person syndrome', 'Nom anglais du syndrome de l’homme raide.', 'g25-stiffperson')
a('Creutzfeldt-Jakob', [('Creutzfeldt-Jakob','noms propres de deux médecins, non une abréviation')], 'Maladie de Creutzfeldt-Jakob', 'Maladie à évoquer devant des myoclonies avec démence rapidement progressive.', 'g25-urgence-myoclonie')
a('DaT-SPECT', [('DaT','DopAmine Transporter (transporteur de la dopamine)'),('SPECT','Single Photon Emission Computed Tomography (tomographie d’émission monophotonique)')], 'Scintigraphie du transporteur de la dopamine',
  'Examen à l’ioflupane marqué à l’iode 123 qui montre un déficit dopaminergique présynaptique.', 'g25-datscan')
a('DaT', [('DaT','DopAmine Transporter (transporteur de la dopamine)')], 'Transporteur de la dopamine', 'Cible de l’ioflupane dans le DaT-SPECT.', 'g25-datscan')
a('EMG', [('E','Électro'),('M','Myo'),('G','Gramme')], 'Électromyogramme', 'Enregistrement de l’activité électrique des muscles ; il distingue l’activité rythmique du tremblement des bouffées irrégulières de la myoclonie.', 'g25-emg')
a('5-HT2A', [('5-HT','5-HydroxyTryptamine (sérotonine)'),('2A','sous-type 2A du récepteur')], 'Récepteur 2A de la sérotonine',
  'Les antagonistes de ce récepteur (cyproheptadine, mirtazapine, miansérine, trazodone) sont cités dans l’akathisie ; la mirtazapine aggrave toutefois les jambes sans repos.', 'g25-d-akathisie')
a('CK', [('C','Créatine'),('K','Kinase')], 'Créatine kinase', 'Enzyme musculaire dosée dans le bilan de la chorée sporadique.', 'g25-bilan-choree')
a('PTH', [('P','Para'),('T','Thyroid (thyroïdienne)'),('H','Hormone')], 'Parathormone', 'Dosage inscrit dans le bilan de la chorée sporadique (hypoparathyroïdie).', 'g25-bilan-choree')
a('AAN', [('A','Anticorps'),('A','Anti'),('N','Nucléaires')], 'Anticorps antinucléaires', 'Dosage inscrit dans le bilan de la chorée sporadique pour rechercher un lupus.', 'g25-bilan-choree')
a('TRAK', [('TR','TSH-Rezeptor (récepteur de la TSH)'),('A','Auto'),('K','Körper (anticorps)')], 'Anticorps anti-récepteur de la TSH', 'Dosage inscrit dans le bilan de la chorée sporadique (hyperthyroïdie auto-immune).', 'g25-bilan-choree')
a('VIM', [('V','Ventral'),('IM','Intermédiaire (noyau ventral intermédiaire du thalamus)')], 'Noyau ventral intermédiaire du thalamus', 'Cible de la stimulation cérébrale profonde dans le tremblement essentiel sévère.', 'g25-d-toxine')
a('GPi', [('G','Globus'),('P','Pallidus'),('i','interne')], 'Globus pallidus interne', 'Cible alternative de la stimulation cérébrale profonde lorsque le tremblement est dystonique.', 'g25-d-toxine')
a('DDT', [('D','Dichloro'),('D','Diphényl'),('T','Trichloroéthane')], 'Dichlorodiphényltrichloroéthane', 'Insecticide figurant parmi les toxiques tremorigènes du consensus 2018.', 'g25-tremorigenes')
a('LGI1', [('LGI1','symbole de protéine ; développement non fourni par les sources lues')], 'Anticorps anti-LGI1', 'Cible d’une encéphalite auto-immune pouvant causer une chorée.', 'g25-chorees-causes')
a('CASPR2', [('CASPR2','symbole de protéine ; développement non fourni par les sources lues')], 'Anticorps anti-CASPR2', 'Cible d’une encéphalite auto-immune pouvant causer une chorée.', 'g25-chorees-causes')
a('IgLON5', [('IgLON5','symbole de protéine ; développement non fourni par les sources lues')], 'Anticorps anti-IgLON5', 'Cible d’une encéphalite auto-immune pouvant causer une chorée.', 'g25-chorees-causes')
a('PERM', [('P','Progressive'),('E','Encephalomyelitis'),('R','with Rigidity'),('M','and Myoclonus')], 'Encéphalomyélite progressive avec rigidité et myoclonies', 'Forme du syndrome de l’homme raide.', 'g25-stiffperson')
a('IRLSSG', [('I','International'),('R','Restless'),('L','Legs'),('S','Syndrome'),('S','Study'),('G','Group')], 'Groupe international d’étude du syndrome des jambes sans repos', 'Ce groupe a défini en 2014 les cinq critères diagnostiques.', 'g25-sjsr-criteres')
a('IRLS', [('I','International'),('R','Restless'),('L','Legs'),('S','Scale')], 'Échelle internationale du syndrome des jambes sans repos', 'Échelle de suivi d’un diagnostic établi.', 'g25-sjsr-criteres')
a('RLS-6', [('RLS','Restless Legs Syndrome'),('6','six items')], 'Échelle RLS-6', 'Échelle de suivi d’un diagnostic établi ; le détail de l’échelle n’est pas fourni par les sources lues.', 'g25-sjsr-criteres')
a('ASRS', [('ASRS','sigle d’échelle ; développement non fourni par les sources lues')], 'Échelle ASRS', 'Échelle de suivi d’un diagnostic établi de syndrome des jambes sans repos.', 'g25-sjsr-criteres')
a('Requip-Modutab', [('Requip-Modutab','noms commerciaux suisses du ropinirole, non une abréviation')], 'Requip-Modutab', 'Information suisse du ropinirole ne mentionnant que la maladie de Parkinson.', 'g25-d-ropinirole')
a('Ropinirol-Mepha', [('Ropinirol-Mepha','nom commercial suisse du ropinirole, non une abréviation')], 'Ropinirol-Mepha', 'Information suisse du ropinirole ne mentionnant que la maladie de Parkinson.', 'g25-d-ropinirole')
