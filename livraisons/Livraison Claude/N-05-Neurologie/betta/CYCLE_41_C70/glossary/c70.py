from cardio_1 import a, G
# C70 — Tumeur maligne des méninges (N-05-Neurologie). Entrées conditionnelles : aucun terme existant n'est écrasé.
def _add(*args):
    if args[0] not in G:
        a(*args)
_add('EANO', [('E','European'),('A','Association'),('N','of Neuro-'),('O','Oncology')], 'Association européenne de neuro-oncologie', '<p>Société savante qui a publié en 2021 la recommandation européenne sur le diagnostic et la prise en charge des méningiomes de l’adulte.</p>', 'c70-eano')
_add('RANO', [('R','Response'),('A','Assessment in'),('N','Neuro-'),('O','Oncology')], 'Évaluation de la réponse en neuro-oncologie', '<p>Critères d’imagerie, tridimensionnels et injectés, qui définissent la réponse d’une tumeur cérébrale ; la réponse complète suppose l’absence de lésion rehaussée pendant au moins 8 semaines.</p>', 'c70-rano')
_add('NF2', [('N','Neuro-'),('F','Fibromatose'),('2','de type 2')], 'Neurofibromatose de type 2 (et gène NF2)', '<p>Maladie génétique, et gène du même nom, première association génétique du méningiome ; elle favorise les grades 2 et 3 et les tumeurs multiples.</p>', 'c70-nf2')
_add('NAB2', [('NAB2','nom de gène, non une abréviation à développer lettre à lettre')], 'Gène NAB2', '<p>Gène dont la fusion avec STAT6 caractérise la tumeur fibreuse solitaire dans la classification de l’OMS 2021.</p>', 'c70-autres')
_add('STAT6', [('STAT6','nom de gène, non une abréviation à développer lettre à lettre')], 'Gène STAT6', '<p>Gène dont la fusion avec NAB2 caractérise la tumeur fibreuse solitaire.</p>', 'c70-autres')
_add('CDKN2B', [('CDKN2B','nom de gène voisin de CDKN2A, non une abréviation à développer lettre à lettre')], 'Gène CDKN2B', '<p>Gène voisin de CDKN2A ; leur délétion homozygote commune est un critère moléculaire de grade 3.</p>', 'c70-moleculaire')
_add('H3K27me3', [('H3','histone H3'),('K27','lysine en position 27'),('me3','triméthylation')], 'Triméthylation de la lysine 27 de l’histone H3', '<p>Marque épigénétique dont la perte touche 10 à 20 % des méningiomes ; son pronostic est débattu et elle n’est pas un critère de grade.</p>', 'c70-h3k27')
_add('EORTC', [('E','European'),('O','Organisation for'),('R','Research and'),('T','Treatment of'),('C','Cancer')], 'Organisation européenne pour la recherche et le traitement du cancer', '<p>Organisation qui a conduit l’essai 22042-26042 sur la radiothérapie du méningiome.</p>', 'c70-radiotherapie')
_add('RTOG', [('R','Radiation'),('T','Therapy'),('O','Oncology'),('G','Group')], 'Groupe d’oncologie par radiothérapie', '<p>Groupe d’essais cliniques à l’origine de l’essai 0539 sur les méningiomes à haut risque.</p>', 'c70-radiotherapie')
_add('mTOR', [('m','mammalian'),('TOR','Target Of Rapamycin')], 'Cible de la rapamycine chez les mammifères', '<p>Voie de signalisation cellulaire inhibée par l’évérolimus.</p>')
_add('DOTATATE', [('DOTATATE','nom de molécule, non une abréviation à développer lettre à lettre')], 'DOTATATE', '<p>Analogue de la somatostatine marqué au gallium 68 pour la tomographie par émission de positons.</p>', 'c70-tep')
_add('DOTATOC', [('DOTATOC','nom de molécule, non une abréviation à développer lettre à lettre')], 'DOTATOC', '<p>Autre analogue de la somatostatine marqué, utilisé pour le même examen.</p>', 'c70-tep')
_add('AVF3708g', [('AVF3708g','identifiant d’étude, non une abréviation à développer lettre à lettre')], 'Étude AVF3708g', '<p>Étude citée dans l’information professionnelle suisse d’Avastin® pour la fréquence des complications de cicatrisation en monothérapie.</p>', 'c70-avastin')
_add('C228T', [('C228T','variant du promoteur de TERT, notation génétique')], 'Variant C228T', '<p>Un des deux points chauds de mutation du promoteur de TERT (avec C250T).</p>', 'c70-moleculaire')
_add('C250T', [('C250T','variant du promoteur de TERT, notation génétique')], 'Variant C250T', '<p>Second point chaud de mutation du promoteur de TERT.</p>', 'c70-moleculaire')
