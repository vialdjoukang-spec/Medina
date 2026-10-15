from cardio_1 import a, G
# E52 — Carence en acide nicotinique [pellagre] (E-06-Endocrinologie et métabolisme). Entrées conditionnelles : aucun terme existant dans G n’est écrasé.
def _add(key, lit, full, definition, ref=None):
    if key not in G:
        a(key, lit, full, '<p>' + definition + '</p>', ref)

_add('NAD', [('N', 'Nicotinamide'), ('A', 'Adénine'), ('D', 'Dinucléotide')], 'Nicotinamide adénine dinucléotide',
     'Coenzyme actif dérivé de la niacine. Plus de 400 enzymes en dépendent ; son déficit altère la production d’énergie, la synthèse lipidique, la réparation de l’ADN et la défense antioxydante (ESPEN 2022).', 'e52-nad')
_add('NADP', [('N', 'Nicotinamide'), ('A', 'Adénine'), ('D', 'Dinucléotide'), ('P', 'Phosphate')], 'Nicotinamide adénine dinucléotide phosphate',
     'Forme phosphorylée du NAD, également dérivée de la niacine. Elle fait partie des coenzymes dont la carence en niacine compromet la fonction (ESPEN 2022).', 'e52-nad')
_add('ESPEN', [('E', 'European'), ('S', 'Society for'), ('P', 'Parenteral'), ('E', 'and Enteral'), ('N', 'Nutrition')], 'Société européenne de nutrition clinique et de métabolisme (sigle issu de European Society for Parenteral and Enteral Nutrition)',
     'Société savante européenne dont la recommandation de 2022 sur les micronutriments (Berger et al.) fixe les repères de ce chapitre pour la niacine.', 'e52-sources')
_add('DGE', [('D', 'Deutsche'), ('G', 'Gesellschaft für'), ('E', 'Ernährung')], 'Société allemande de nutrition',
     'Elle publie les valeurs de référence pour la niacine, exprimées en équivalents niacine, avec l’ÖGE ; l’adoption par la Suisse de ces valeurs n’a pas été vérifiée dans ce dossier.', 'e52-apports')
_add('ÖGE', [('Ö', 'Österreichische'), ('G', 'Gesellschaft für'), ('E', 'Ernährung')], 'Société autrichienne de nutrition',
     'Elle publie avec la DGE les valeurs de référence pour la niacine.', 'e52-apports')
_add('EFSA', [('E', 'European'), ('F', 'Food'), ('S', 'Safety'), ('A', 'Authority')], 'Autorité européenne de sécurité des aliments',
     'Ses limites supérieures de sécurité pour la niacine (acide nicotinique libre 10 mg par jour ; nicotinamide 12,5 mg/kg/jour) sont citées de seconde main par l’ESPEN, le texte de l’EFSA n’ayant pas été accessible.', 'e52-niacine')
_add('SMOB', [('S', 'Swiss'), ('M', 'Morbid'), ('O', 'Obesity'), ('B', 'and Metabolic Disorders')], 'Société suisse pour l’étude de l’obésité morbide et des maladies métaboliques (Swiss Society for the Study of Morbid Obesity and Metabolic Disorders)',
     'Ses directives, en vigueur dès le 1.7.2023, prévoient des multivitamines à long terme après chirurgie bariatrique, à vie après chirurgie malabsorptive.', 'e52-bariatrique')
_add('UV', [('U', 'Ultra'), ('V', 'Violets')], 'Ultraviolets',
     'Rayonnement dont l’exposition aggrave la dermatite de la pellagre, car le déficit en NAD empêche la réparation de l’ADN et la récupération des kératinocytes.', 'e52-photosensibilite')
_add('PARP', [('P', 'Poly'), ('A', 'Adénosine diphosphate (ADP)'), ('R', 'Ribose'), ('P', 'Polymérase')], 'Poly(ADP-ribose) polymérase',
     'Enzyme décrite comme grande consommatrice de NAD ; elle figure parmi les cinq voies proposées pour la dégénérescence neuronale de la carence en niacine, en partie expérimentales.', 'e52-encephalopathie')
_add('BDNF', [('B', 'Brain'), ('D', 'Derived'), ('N', 'Neurotrophic'), ('F', 'Factor')], 'Facteur neurotrophique dérivé du cerveau',
     'Protéine de la survie neuronale ; son axe avec le récepteur TrkB figure parmi les cinq voies proposées pour la lésion neuronale de la carence en niacine.', 'e52-encephalopathie')
_add('TrkB', [('Trk', 'Tropomyosin receptor kinase'), ('B', 'type B')], 'Récepteur de type B à tyrosine kinase, lié à la tropomyosine',
     'Récepteur du BDNF ; l’axe BDNF–TrkB est une des cinq voies proposées pour la lésion neuronale de la carence en niacine.', 'e52-encephalopathie')
_add('B12', [('B', 'vitamine du groupe B'), ('12', 'douzième de la série')], 'Vitamine B12 (cobalamine)',
     'Vitamine dont le déficit est recherché devant une neuropathie qui persiste malgré la niacine, la pellagre étant une carence multiple.')
_add('CK', [('C', 'Créatine'), ('K', 'Kinase')], 'Créatine kinase',
     'Enzyme musculaire dosée, avec un panel myosite, pour écarter une dermatomyosite devant une éruption en châle corticorésistante.')
_add('5-HIAA', [('5', 'en position 5'), ('H', 'Hydroxy-'), ('I', 'Indole-'), ('AA', 'Acetic Acid (acide acétique)')], 'Acide 5-hydroxy-indole-acétique',
     'Métabolite urinaire de la sérotonine. Il renseigne la charge sérotoninergique d’une tumeur carcinoïde, non le statut en niacine.', 'e52-carcinoide')
_add('E64.8', [('E64', 'code CIM-10-GM des séquelles de carences nutritionnelles'), ('.8', 'autres séquelles')], 'Code CIM-10-GM des séquelles de carence en niacine',
     'La CIM-10-GM 2024 exclut de E52 les séquelles de carence en niacine et les classe sous ce code.')
_add('E72.0', [('E72', 'code CIM-10-GM des anomalies du métabolisme des acides aminés'), ('.0', 'troubles du transport des acides aminés')], 'Code CIM-10-GM de la maladie de Hartnup',
     'Maladie héréditaire du transport du tryptophane, cause possible de pellagre.', 'e52-hartnup')
_add('N1-méthylnicotinamide', [('N1', 'azote en position 1 du noyau pyridine'), ('méthyl', 'groupe méthyle'), ('nicotinamide', 'amide de l’acide nicotinique')], 'N1-méthylnicotinamide',
     'Principal métabolite urinaire de la niacine ; l’OMS propose, à titre provisoire, la valeur de moins de 0,5 mg/g de créatinine comme seuil de déficience de l’adulte.', 'e52-seuils-oms')
_add('Marchiafava-Bignami', [('Marchiafava', 'Ettore Marchiafava, pathologiste italien'), ('Bignami', 'Amico Bignami, pathologiste italien')], 'Maladie de Marchiafava-Bignami',
     'Atteinte cérébrale liée à l’alcoolisme chronique, souvent associée à la chromatolyse neuronale de la pellagre alcoolique dans les autopsies parisiennes de 22 buveurs excessifs (Serdaru et al. 1988).', 'e52-serdaru')
_add('Wernicke-Korsakoff', [('Wernicke', 'Carl Wernicke, neurologue allemand'), ('Korsakoff', 'Sergueï Korsakov, psychiatre russe')], 'Syndrome de Wernicke-Korsakoff',
     'Atteinte neurologique de la carence en thiamine, fréquente chez l’alcoolique ; elle coexiste souvent avec la pellagre alcoolique, d’où le recours à une polyvitaminothérapie et non à la thiamine seule.', 'e52-serdaru')
_add('Roux-en-Y', [('Roux', 'César Roux, chirurgien suisse'), ('en-Y', 'montage en forme de Y')], 'Dérivation gastrique de Roux-en-Y',
     'Technique de dérivation gastrique bariatrique, après laquelle des cas de pellagre ont été rapportés, parfois en association à l’alcool.', 'e52-bariatrique')
