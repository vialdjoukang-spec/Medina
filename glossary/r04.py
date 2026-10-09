from cardio_1 import a, G
# R04 — Hémoptysie (P-02-Pneumologie). Revue IA ; ne vaut pas validation médicale.
# Ajouts conditionnels : une clé déjà définie par un autre glossaire (par exemple FFP2 dans J67) n'est jamais écrasée.
# Vérification de l'absence de collision dans glossary/*.py le 09.10.2026.

def _a(k, *args):
    if k not in G:
        a(k, *args)

_a('CIRSE', [('C', 'Cardiovascular (cardiovasculaire)'), ('I', 'and Interventional (et interventionnelle)'), ('R', 'Radiological (de radiologie)'), ('S', 'Society of (Société)'), ('E', 'Europe (d’Europe)')], 'Société européenne de radiologie cardiovasculaire et interventionnelle', '<p>Société savante européenne de radiologie interventionnelle. Ses « Standards of Practice » de 2022 sur l’embolisation des artères bronchiques fixent les indications, la technique, les résultats attendus et les complications de ce geste.</p>', 'r04-eab')
_a('FFP2', [('F', 'Filtering (filtrante)'), ('F', 'Face (faciale)'), ('P', 'Piece (pièce)'), ('2', 'classe de protection 2')], 'Demi-masque filtrant contre les particules, classe 2', '<p>Masque de protection respiratoire conforme à la norme européenne EN 149. Le guide suisse de la tuberculose le recommande au personnel et aux visiteurs qui entrent dans la chambre d’un patient isolé pour suspicion de tuberculose pulmonaire.</p>', 'r04-tuberculose')
_a('MM', [('M', 'Mixed (mixtes)'), ('M', 'Micelles (micelles)')], 'Micelles mixtes', '<p>Forme galénique de la vitamine K<sub>1</sub> (Konakion® MM) : la phytoménadione est dissoute dans une solution limpide de micelles mixtes, administrable par voie orale ou parentérale selon l’information professionnelle suisse.</p>', 'r04-d-pcc')
