from cardio_1 import a, G
# E42 — Kwashiorkor avec marasme (E-06-Endocrinologie et métabolisme). Entrées conditionnelles : aucun terme existant dans G n’est écrasé.
if 'PCIME' not in G:
    a('PCIME', [('P','Prise'),('C','en Charge'),('I','Intégrée des'),('M','Maladies de'),('E','l’Enfant')], 'Prise en charge intégrée des maladies de l’enfant', '<p>Stratégie de l’Organisation mondiale de la Santé dont les signes de danger (incapacité de boire ou de téter, vomissement de tout ce qui est ingéré, convulsions, léthargie ou inconscience) sont repris dans la directive 2023 sur la malnutrition aiguë.</p>', 'e42-pcime')
if 'ATPE' not in G:
    a('ATPE', [('A','Aliment'),('T','Thérapeutique'),('PE','Prêt à l’Emploi')], 'Aliment thérapeutique prêt à l’emploi', '<p>Aliment utilisé en traitement ambulatoire de la malnutrition aiguë sévère, à raison de 150 à 185 kcal/kg/jour selon la directive de l’OMS 2023.</p>', 'e42-d-atpe')
if 'ReSoMal' not in G:
    a('ReSoMal', [('Re','Rehydration (réhydratation)'),('So','Solution'),('Mal','for Malnutrition (pour la malnutrition)')], 'Solution de réhydratation pour la malnutrition', '<p>Solution de réhydratation orale préférée par l’OMS 2023, en l’absence de choc, chez l’enfant atteint de malnutrition aiguë sévère.</p>', 'e42-d-resomal')
if 'CIM' not in G:
    a('CIM', [('C','Classification'),('I','Internationale des'),('M','Maladies')], 'Classification internationale des maladies', '<p>Classification de l’Organisation mondiale de la Santé. Le catalogue de ce dépôt suit la CIM-10-GM 2024 ; la CIM-11 est citée à titre de repère, sa correspondance exacte pour E42 n’ayant pas été vérifiée.</p>', 'e42-nosologie')
if 'IGF-1' not in G:
    a('IGF-1', [('IGF','Insulin-like Growth Factor (facteur de croissance analogue à l’insuline)'),('1','type 1')], 'Facteur de croissance analogue à l’insuline de type 1', '<p>Hormone dont le taux est abaissé dans la malnutrition aiguë, avec l’insuline et la triiodothyronine, alors que l’hormone de croissance et le cortisol sont élevés (Dipasquale 2020).</p>')
if 'McLaren' not in G:
    a('McLaren', [('McLaren','nom propre d’un auteur de classification, non une abréviation')], 'McLaren, auteur d’une classification de la malnutrition', '<p>Gomez, Waterlow et McLaren sont cités comme critères de classement dans une étude turque ; leurs seuils n’ont pas été lus dans une source primaire.</p>', 'e42-wellcome')
if '5B51' not in G:
    a('5B51', [('5B51','code de la CIM-11 cité par l’OMS pour l’émaciation, non développable lettre à lettre')], 'Code CIM-11 5B51 (émaciation)', '<p>Code cité par l’OMS 2023. Sa correspondance exacte avec E42 n’a pas été vérifiée.</p>', 'e42-nosologie')
if '5B52' not in G:
    a('5B52', [('5B52','code de la CIM-11 cité par l’OMS pour la malnutrition aiguë, non développable lettre à lettre')], 'Code CIM-11 5B52 (malnutrition aiguë)', '<p>Code cité par l’OMS 2023. Sa correspondance exacte avec E42 n’a pas été vérifiée.</p>', 'e42-nosologie')
