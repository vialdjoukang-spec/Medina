# Glossaire MEDINA — chapitre I83 Varices des membres inférieurs et maladie veineuse chronique
# Glossaire initial de l'architecte (7 octobre 2026). Les rédacteurs ajoutent leurs sigles dans
# glossary_i83_<onglet>.py ; le vérificateur fusionne. Ne pas redéfinir une clé déjà présente dans glossary/.
#
# Règle CEAP (voir PLAN.md, § 8.3) : les clés C1 à C9 existent déjà (fractions du complément, glossary/d84.py
# et glossary/i33.py). Les classes cliniques CEAP s'écrivent donc C&#8288;0 … C&#8288;6, C&#8288;4a, C&#8288;2r
# (gluon de mots U+2060 entre la lettre et le chiffre) afin de ne jamais ouvrir la définition du complément.
from cardio_1 import a, G

L = [
('CEAP', [('C', 'Clinical (clinique)'), ('E', 'Etiological (étiologique)'), ('A', 'Anatomical (anatomique)'), ('P', 'Pathophysiological (physiopathologique)')],
 'Classification clinique, étiologique, anatomique et physiopathologique des troubles veineux chroniques',
 '<p>Description d’un membre à un moment donné selon quatre domaines. Clinique : classes 0 à 6 (0 aucun signe ; 1 télangiectasies ou veines réticulaires ; 2 varices ; 3 œdème ; 4 altérations cutanées, 4a pigmentation ou eczéma, 4b lipodermatosclérose ou atrophie blanche, 4c corona phlebectatica ; 5 ulcère cicatrisé ; 6 ulcère actif), avec l’indice S (symptomatique) ou A (asymptomatique) et le suffixe r pour une récidive (2r, 6r). Étiologie : Ep primaire, Es secondaire (Esi intraveineuse, Ese extraveineuse), Ec congénitale, En non identifiée. Anatomie : As superficiel, Ad profond, Ap perforantes, An aucun site. Physiopathologie : Pr reflux, Po obstruction, Pr,o les deux, Pn aucune. Révision de 2020 (Lurie et al.) ; descriptive, elle ne mesure pas l’évolution.</p>', 'i83-ceap'),
('VCSS', [('V', 'Venous (veineux)'), ('C', 'Clinical (clinique)'), ('S', 'Severity (de gravité)'), ('S', 'Score')],
 'Score de gravité clinique veineuse (version révisée)',
 '<p>Score continu de 10 items cotés de 0 à 3 (douleur, varices, œdème, pigmentation, inflammation, induration, nombre, durée et taille des ulcères actifs, compression), soit 0 à 30 points. Il suit l’évolution d’un membre après traitement, ce que la classification CEAP ne permet pas (ESVS 2022, tableau 5).</p>', 'i83-vcss'),
('IPS', [('I', 'Index'), ('P', 'de Pression'), ('S', 'Systolique')],
 'Index de pression systolique cheville-bras',
 '<p>Rapport entre la pression systolique mesurée à la cheville par Doppler et la pression systolique brachiale la plus élevée. Avant toute compression, il recherche une artériopathie associée : l’ESVS 2022 déconseille une compression soutenue si l’index est inférieur à 0,6, si la pression de cheville est inférieure à 60 mmHg ou si la pression d’orteil est inférieure à 30 mmHg. Une artère calcifiée (diabète, insuffisance rénale) donne une valeur faussement élevée.</p>', 'i83-ips'),
('EHIT', [('E', 'Endothermal (endothermique)'), ('H', 'Heat (par la chaleur)'), ('I', 'Induced (induite)'), ('T', 'Thrombosis (thrombose)')],
 'Thrombose induite par la chaleur après ablation thermique endoveineuse',
 '<p>Thrombus qui prolonge la veine saphène traitée jusqu’à la jonction ou dans la veine profonde. Classification de l’American Venous Forum en quatre classes, de l’absence de propagation dans la veine profonde (classe I) au thrombus profond occlusif (classe IV). Fréquence d’environ 1,7 % après ablation de la grande saphène (méta-analyse citée par l’ESVS 2022) ; la classe IV relève d’une anticoagulation curative.</p>', 'i83-thermique'),
('EVRA', [('E', 'Early (précoce)'), ('V', 'Venous (veineux)'), ('R', 'Reflux'), ('A', 'Ablation')],
 'Essai EVRA (2018)',
 '<p>Essai randomisé britannique de 450 patients porteurs d’un ulcère veineux : l’ablation endoveineuse du reflux superficiel dans les deux semaines, ajoutée à la compression, raccourcit le délai médian de cicatrisation de 82 à 56 jours (Gohel et al., N Engl J Med 2018).</p>', 'i83-evra'),
('ESCHAR', [('E', 'Effect (effet)'), ('S', 'of Surgery (de la chirurgie)'), ('C', 'and Compression (et de la compression)'), ('H', 'on Healing (sur la cicatrisation)'), ('A', 'And'), ('R', 'Recurrence (et la récidive)')],
 'Essai ESCHAR (2004-2007)',
 '<p>Essai randomisé de 500 patients porteurs d’un ulcère veineux : la chirurgie du reflux superficiel ajoutée à la compression ne modifie pas la cicatrisation mais réduit la récidive à quatre ans de 56 % à 31 % (Gohel et al., British Medical Journal 2007).</p>', 'i83-evra'),
('CLASS', [('CLASS', 'Comparison of LAser, Surgery and foam Sclerotherapy (comparaison du laser, de la chirurgie et de la sclérothérapie à la mousse) ; nom d’essai, non strictement lettre à lettre')],
 'Essai CLASS (2014-2019)',
 '<p>Essai randomisé britannique de 798 patients porteurs de varices primitives : à cinq ans, la qualité de vie propre à la maladie est meilleure après laser endoveineux ou chirurgie qu’après sclérothérapie à la mousse (Brittenden et al., N Engl J Med 2019).</p>', 'i83-thermique'),
('CHIVA', [('C', 'Cure'), ('H', 'Hémodynamique'), ('I', 'de l’Insuffisance'), ('V', 'Veineuse'), ('A', 'en Ambulatoire')],
 'Cure conservatrice et hémodynamique de l’insuffisance veineuse en ambulatoire',
 '<p>Stratégie qui conserve la veine saphène et interrompt seulement les points de fuite du reflux, sous anesthésie locale, après une cartographie échographique détaillée. Recommandation ESVS 2022 de classe IIb, réservée aux équipes expérimentées.</p>', 'i83-chirurgie'),
('ASVAL', [('A', 'Ablation'), ('S', 'Sélective des'), ('V', 'Varices'), ('A', 'sous Anesthésie'), ('L', 'Locale')],
 'Ablation sélective des varices sous anesthésie locale',
 '<p>Phlébectomies des seules varices collatérales en conservant le tronc saphène, dans l’espoir que le reflux du tronc régresse. Recommandation ESVS 2022 de classe IIb pour les varices non compliquées.</p>', 'i83-chirurgie'),
('LiMA', [('Li', 'Liste'), ('M', 'des Moyens'), ('A', 'et Appareils')],
 'Liste des moyens et appareils (Suisse)',
 '<p>Annexe 2 de l’ordonnance sur les prestations de l’assurance des soins, publiée par l’Office fédéral de la santé publique ; nom allemand : MiGeL. Son chapitre 17 fixe les conditions de remboursement des bas et bandages de compression (édition du 1er janvier 2026).</p>', 'i83-suisse'),
('MiGeL', [('Mi', 'Mittel- (moyens)'), ('Ge', 'und Gegenstände- (et appareils)'), ('L', 'Liste')],
 'Mittel- und Gegenständeliste (liste des moyens et appareils, Suisse)',
 '<p>Nom allemand de la liste des moyens et appareils remboursés par l’assurance obligatoire des soins.</p>', 'i83-suisse'),
('OPAS', [('O', 'Ordonnance'), ('P', 'sur les Prestations'), ('A', 'de l’Assurance'), ('S', 'des Soins')],
 'Ordonnance du Département fédéral de l’intérieur sur les prestations de l’assurance obligatoire des soins',
 '<p>Nom allemand : Krankenpflege-Leistungsverordnung. Son annexe 1 (édition du 1er juillet 2026) admet l’ablation thermique endoveineuse des troncs saphènes par radiofréquence ou laser, réalisée par un médecin titulaire de l’attestation de formation complémentaire correspondante, et exclut l’ablation mécanochimique de type ClariVein.</p>', 'i83-suisse'),
('LAMal', [('L', 'Loi fédérale sur'), ('A', 'l’Assurance-'), ('Mal', 'Maladie')],
 'Loi fédérale sur l’assurance-maladie (Suisse)',
 '<p>Loi qui définit l’assurance obligatoire des soins et les critères d’efficacité, d’adéquation et d’économicité des prestations remboursées.</p>', 'i83-suisse'),
('MMP', [('M', 'Matrix (matricielles)'), ('M', 'Metallo-'), ('P', 'Proteinases (protéinases)')],
 'Métalloprotéinases matricielles',
 '<p>Enzymes dépendantes du zinc qui dégradent le collagène et l’élastine de la paroi. Leur activité accrue dans la paroi variqueuse participe au remodelage et à la dilatation ; elle est démontrée par des études d’expression, sans preuve qu’un inhibiteur modifie l’évolution clinique.</p>'),
('FOXC2', [('FOX', 'Forkhead bOX (boîte en fourche)'), ('C2', 'sous-famille C, membre 2')],
 'Gène du facteur de transcription Forkhead box C2',
 '<p>Facteur de transcription du développement des valvules veineuses et lymphatiques. Ses variants perte de fonction causent le syndrome lymphœdème-distichiasis, où l’incompétence valvulaire veineuse est fréquente.</p>', 'i83-gen'),
('Klippel-Trénaunay', [('Klippel-Trénaunay', 'nom propre : Maurice Klippel et Paul Trénaunay')],
 'Syndrome de Klippel-Trénaunay',
 '<p>Malformation vasculaire congénitale à flux lent associant malformation capillaire cutanée, malformation veineuse ou varices atypiques souvent latérales et hypertrophie d’un membre. Étiologie congénitale (Ec) dans la classification CEAP.</p>'),
]
for x in L:
    a(*x)

# Codes CIM-10-GM 2024 du périmètre (libellés du catalogue medora-data de shell/medina_front.html)
for c, tt in [
    ('I83.0', 'Varices ulcérées des membres inférieurs'),
    ('I83.1', 'Varices des membres inférieurs, avec inflammation (dermite de stase)'),
    ('I83.2', 'Varices des membres inférieurs, avec ulcère et inflammation'),
    ('I83.9', 'Varices des membres inférieurs sans ulcère ou inflammation'),
    ('I86.1', 'Varices scrotales (varicocèle)'),
    ('I86.2', 'Varices pelviennes'),
    ('I86.3', 'Varices vulvaires'),
    ('I87.0', 'Syndrome post-phlébitique'),
    ('I87.00', 'Syndrome post-thrombotique sans ulcération'),
    ('I87.01', 'Syndrome post-thrombotique avec ulcération'),
    ('I87.1', 'Compression veineuse'),
    ('I87.2', 'Insuffisance veineuse (chronique) (périphérique)'),
    ('I87.20', 'Insuffisance veineuse (chronique) (périphérique) sans ulcération'),
    ('I87.21', 'Insuffisance veineuse (chronique) (périphérique) avec ulcération'),
    ('I87.8', 'Autres atteintes veineuses précisées'),
    ('I87.9', 'Atteinte veineuse, sans précision'),
]:
    a(c, [(c, 'code de la Classification internationale des maladies, 10e révision, modification allemande')], tt,
      '<p>Code CIM-10-GM 2024.</p>', 'i83-codage')
