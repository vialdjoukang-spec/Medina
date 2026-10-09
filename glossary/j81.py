from cardio_1 import a, G
# Glossaire du cours J81 — Œdème pulmonaire non cardiogénique (P-02-Pneumologie).
# TRALI et TACO peuvent déjà être définis par glossary/j80.py (chargé avant ce fichier) : ils ne sont ajoutés
# que s’ils manquent, afin de ne jamais écraser une entrée existante. OPHA, ISBT, UIAA et HNA sont nouveaux
# (vérification de l’absence de collision le 09.10.2026). Revue IA ; ne vaut pas validation médicale.

def _a(k, *args):
    if k not in G:
        a(k, *args)

_a('OPHA', [('O', 'Œdème'), ('P', 'Pulmonaire'), ('H', 'de Haute'), ('A', 'Altitude')], 'Œdème pulmonaire de haute altitude', '<p>Œdème pulmonaire non cardiogénique du sujet sain qui monte trop vite au-dessus d’environ 2500 à 3000 m. Il naît d’une vasoconstriction pulmonaire hypoxique exagérée et inégale, qui élève la pression capillaire, avec un cœur gauche normal.</p>', 'j81-opha')
_a('TRALI', [('T', 'Transfusion-'), ('R', 'Related (lié à la transfusion)'), ('A', 'Acute (aigu)'), ('L', 'Lung (pulmonaire)'), ('I', 'Injury (lésion)')], 'Lésion pulmonaire aiguë post-transfusionnelle', '<p>Œdème pulmonaire lésionnel survenant pendant une transfusion ou dans les 6 heures, avec hypoxémie et sans hypertension de l’oreillette gauche déterminante. Le consensus de 2019 distingue les types I et II selon la présence d’un facteur de risque de syndrome de détresse respiratoire aiguë.</p>', 'j81-trali')
_a('TACO', [('T', 'Transfusion-'), ('A', 'Associated (associée à la transfusion)'), ('C', 'Circulatory (circulatoire)'), ('O', 'Overload (surcharge)')], 'Surcharge circulatoire associée à la transfusion', '<p>Œdème pulmonaire hydrostatique par surcharge volémique, survenant pendant une transfusion ou dans les 12 heures. Il se reconnaît selon la définition de surveillance ISBT 2018.</p>', 'j81-taco')
_a('ISBT', [('I', 'International'), ('S', 'Society of'), ('B', 'Blood'), ('T', 'Transfusion')], 'Société internationale de transfusion sanguine', '<p>Société savante dont le groupe de travail d’hémovigilance a publié, avec le réseau international d’hémovigilance, la définition de surveillance du TACO de 2018, à laquelle se réfère Swissmedic.</p>', 'j81-taco')
_a('UIAA', [('U', 'Union'), ('I', 'Internationale des'), ('A', 'Associations d’'), ('A', 'Alpinisme')], 'Fédération internationale d’alpinisme et d’escalade', '<p>Fédération dont le siège est à Berne. Sa commission médicale publie des déclarations de consensus sur les maladies de l’altitude, dont la conduite d’urgence devant le mal aigu des montagnes, l’œdème pulmonaire et l’œdème cérébral de haute altitude.</p>', 'j81-opha')
_a('HNA', [('H', 'Human (humain)'), ('N', 'Neutrophil (des polynucléaires neutrophiles)'), ('A', 'Antigen (antigène)')], 'Antigène des polynucléaires neutrophiles humains', '<p>Antigène de surface des polynucléaires neutrophiles. Les anticorps anti-HNA d’un donneur peuvent déclencher un TRALI chez un receveur porteur de l’antigène correspondant.</p>', 'j81-trali')
