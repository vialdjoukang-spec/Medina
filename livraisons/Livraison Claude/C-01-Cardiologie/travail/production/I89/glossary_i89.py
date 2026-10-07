# Glossaire MEDINA — chapitre I89 Autres atteintes non infectieuses des vaisseaux et des ganglions lymphatiques
# Glossaire initial de l’architecte (07.10.2026). Les rédacteurs ajoutent leurs sigles dans glossary_i89_<onglet>.py.
# Aucune clé ci-dessous n’écrase une clé existante du dépôt (contrôle fait le 07.10.2026).
# Attention : la clé PATCH existe déjà (essai d’hydroxychloroquine du bloc congénital, glossary/i44.py).
# Ne jamais écrire « PATCH » dans I89 : citer « l’essai de Thomas et al. (2013) ».
from cardio_1 import a, G

# ---- sociétés, réglementation suisse
a('ISL',[('I','International'),('S','Society of'),('L','Lymphology')],'International Society of Lymphology (Société internationale de lymphologie)',
 '<p>Société savante internationale qui publie le document de consensus sur le diagnostic et le traitement du lymphœdème périphérique. La version 2023 (Lymphology 2023;56:133-151) définit les stades 0 à III et la thérapie décongestive complexe en deux phases.</p>')
a('LAMal',[('L','Loi fédérale sur l’'),('A','Assurance-'),('Mal','MALadie')],'Loi fédérale sur l’assurance-maladie',
 '<p>Loi suisse qui définit l’assurance obligatoire des soins. Les prestations prises en charge sont précisées par l’OPAS et ses annexes.</p>')
a('OPAS',[('O','Ordonnance'),('P','sur les Prestations'),('A','de l’Assurance'),('S','des Soins')],'Ordonnance sur les prestations de l’assurance des soins',
 '<p>Ordonnance du Département fédéral de l’intérieur (RS 832.112.31). Son annexe 1 fixe les conditions de prise en charge de certaines prestations, dont les anastomoses lymphaticoveineuses et les transplantations de ganglions lymphatiques vascularisés (édition du 1.7.2026).</p>','i89-suisse')
a('LiMA',[('Li','LIste'),('M','des Moyens'),('A','et Appareils')],'Liste des moyens et appareils',
 '<p>Annexe 2 de l’OPAS. Son chapitre 17 fixe les indications, les quantités et les montants maximaux remboursés des bas et bandages de compression, des systèmes ajustables et des appareils de compression pneumatique.</p>','i89-suisse')

# ---- essais et techniques
a('AMAROS',[('A','After'),('MA','MApping of the axilla (après repérage de l’aisselle)'),('R','Radiotherapy'),('O','Or'),('S','Surgery')],'Essai AMAROS',
 '<p>Essai européen de phase 3 (Donker et al., Lancet Oncology 2014) chez des patientes avec ganglion sentinelle positif : curage axillaire ou radiothérapie axillaire. Le contrôle axillaire a été comparable. Des signes cliniques de lymphœdème étaient présents à 5 ans chez 23 % des patientes après curage et 11 % après radiothérapie.</p>')
a('PAL',[('P','Physical'),('A','Activity and'),('L','Lymphedema')],'Essai PAL (activité physique et lymphœdème)',
 '<p>Essai randomisé (Schmitz et al., New England Journal of Medicine 2009) de renforcement musculaire progressif, deux fois par semaine, chez 141 femmes avec lymphœdème stable du bras après cancer du sein. Le gonflement n’a pas augmenté et les poussées ont été moins fréquentes (14 % contre 29 %).</p>')
a('LYMPHA',[('LYMPHA','LYMPHatic microsurgical preventive healing Approach (approche microchirurgicale lymphatique préventive)')],'Technique LYMPHA',
 '<p>Anastomose lymphaticoveineuse réalisée pendant le curage ganglionnaire, chez un patient à haut risque, pour prévenir le lymphœdème. Plusieurs études suggèrent une baisse de l’incidence ; les données à long terme manquent (ISL 2023).</p>','i89-chir-micro')
a('ICG',[('I','Indo-'),('C','Cyanine'),('G','Green (vert)')],'Vert d’indocyanine',
 '<p>Colorant fluorescent injecté dans le derme. Une caméra proche infrarouge visualise en temps réel les vaisseaux lymphatiques superficiels (lymphographie au vert d’indocyanine), sans rayonnement ionisant.</p>','i89-e-icg')
a('BIS',[('B','Bio-'),('I','Impedance'),('S','Spectroscopy')],'Bioimpédance spectroscopique',
 '<p>Mesure de la résistance du membre à des courants de faible intensité et de fréquences multiples. Le liquide extracellulaire conduit le courant de basse fréquence : son augmentation abaisse la résistance et révèle un lymphœdème avant qu’il ne soit visible.</p>','i89-e-bis')
a('L-Dex',[('L','Lymphoedema'),('Dex','inDEX (indice)')],'Indice de lymphœdème mesuré par bioimpédance',
 '<p>Rapport des résistances entre le membre exposé et le membre sain, normalisé par l’appareil de bioimpédance spectroscopique. Son interprétation exige une mesure de référence avant le traitement du cancer.</p>','i89-e-bis')

# ---- gènes et marqueurs
a('VEGF-C',[('V','Vascular (vasculaire)'),('E','Endothelial (endothélial)'),('G','Growth (de croissance)'),('F','Factor (facteur)'),('C','type C')],'Facteur de croissance de l’endothélium vasculaire C',
 '<p>Principal facteur de croissance des vaisseaux lymphatiques. Il active le récepteur VEGFR-3 des cellules endothéliales lymphatiques. Certains variants pathogènes de son gène causent un lymphœdème héréditaire.</p>','i89-s-vegfc')
a('VEGF-D',[('V','Vascular (vasculaire)'),('E','Endothelial (endothélial)'),('G','Growth (de croissance)'),('F','Factor (facteur)'),('D','type D')],'Facteur de croissance de l’endothélium vasculaire D',
 '<p>Facteur lymphangiogénique apparenté au VEGF-C. Son taux sérique est élevé dans la lymphangioléiomyomatose et diminue sous sirolimus.</p>')
a('VEGFR-3',[('V','Vascular (vasculaire)'),('E','Endothelial (endothélial)'),('G','Growth (de croissance)'),('F','Factor (facteur)'),('R','Receptor (récepteur)'),('3','type 3')],'Récepteur 3 du facteur de croissance de l’endothélium vasculaire',
 '<p>Récepteur à activité tyrosine kinase des cellules endothéliales lymphatiques, codé par le gène FLT4. Une perte de fonction cause la maladie de Milroy.</p>','i89-s-vegfc')
a('FLT4',[('F','Fms- (apparenté au récepteur fms)'),('L','Like (similaire)'),('T','Tyrosine kinase'),('4','4')],'Gène FLT4',
 '<p>Gène du récepteur VEGFR-3. Ses variants pathogènes, souvent transmis sur un mode autosomique dominant, causent la maladie de Milroy : lymphœdème congénital des pieds et des jambes.</p>')
a('FOXC2',[('FOX','FOrkhead boX (domaine en tête de fourche)'),('C2','sous-famille C, membre 2')],'Gène FOXC2',
 '<p>Facteur de transcription nécessaire à la formation des valvules lymphatiques. Ses variants pathogènes causent le syndrome lymphœdème-distichiasis : lymphœdème d’apparition souvent tardive (puberté ou âge adulte) et double rangée de cils.</p>')
a('CCBE1',[('C','Collagen (collagène)'),('C','Calcium-'),('B','Binding (liant le calcium)'),('E','EGF domain (domaine de type facteur de croissance épidermique)'),('1','1')],'Gène CCBE1',
 '<p>Gène nécessaire à la maturation du VEGF-C. Ses variants pathogènes causent le syndrome de Hennekam, dysplasie lymphatique généralisée avec lymphangiectasies intestinales.</p>')
a('FAT4',[('FAT','FAT (nom du gène « fat » de la drosophile, non développable)'),('4','4')],'Gène FAT4',
 '<p>Gène d’une cadhérine atypique. Ses variants pathogènes sont une autre cause du syndrome de Hennekam.</p>')
a('GJC2',[('G','Gap'),('J','Junction (jonction communicante)'),('C','protein gamma (sous-famille C)'),('2','2')],'Gène GJC2',
 '<p>Gène de la connexine 47, protéine des jonctions communicantes. Ses variants pathogènes causent un lymphœdème héréditaire des membres.</p>')
a('PIEZO1',[('PIEZO','du grec « píesi », pression (canal ionique mécanosensible)'),('1','1')],'Gène PIEZO1',
 '<p>Gène d’un canal ionique activé par l’étirement, impliqué dans le développement des valvules lymphatiques. Ses variants pathogènes causent une forme de lymphœdème héréditaire (type III selon l’ISL 2023) et des dysplasies lymphatiques généralisées.</p>')
a('GATA2',[('GATA','facteur se liant à la séquence d’ADN G-A-T-A'),('2','2')],'Gène GATA2',
 '<p>Facteur de transcription hématopoïétique et lymphatique. Ses variants pathogènes causent le syndrome d’Emberger : lymphœdème primaire, infections et risque de myélodysplasie, ce qui impose un suivi hématologique.</p>')
a('SOX18',[('S','SRY (région du chromosome Y déterminant le sexe)'),('OX','-related HMG bOX (boîte HMG apparentée)'),('18','18')],'Gène SOX18',
 '<p>Facteur de transcription de la différenciation lymphatique. Ses variants pathogènes causent le syndrome hypotrichose-lymphœdème-télangiectasies.</p>')
a('PROX1',[('PRO','PROspero (gène homologue de la drosophile)'),('X','homeoboX (boîte homéotique)'),('1','1')],'Facteur de transcription PROX1',
 '<p>Facteur qui fixe l’identité des cellules endothéliales lymphatiques pendant le développement. Il sert aussi de marqueur immunohistochimique de ces cellules.</p>')
a('LYVE-1',[('LY','LYmphatic (lymphatique)'),('V','Vessel (vaisseau)'),('E','Endothelial hyaluronan receptor (récepteur endothélial de l’hyaluronane)'),('1','1')],'Récepteur endothélial lymphatique de l’hyaluronane 1',
 '<p>Récepteur de l’hyaluronane exprimé par les lymphatiques initiaux. Il sert de marqueur des capillaires lymphatiques en histologie.</p>')
a('PIK3CA',[('PI','PhosphatidylInositol'),('3K','3-Kinase'),('C','Catalytic subunit (sous-unité catalytique)'),('A','Alpha')],'Gène PIK3CA',
 '<p>Gène de la sous-unité catalytique alpha de la phosphatidylinositol 3-kinase. Ses variants somatiques activateurs causent des syndromes de croissance excessive avec malformations lymphatiques, dont le syndrome CLOVES et le syndrome de Klippel-Trénaunay.</p>')
a('RASA1',[('RAS','RAt Sarcoma (oncogène du sarcome du rat)'),('A','Activator (protéine activatrice de la GTPase)'),('1','1')],'Gène RASA1',
 '<p>Gène d’un régulateur négatif de la voie RAS. Ses variants pathogènes causent des malformations capillaires et artérioveineuses, dont certaines s’accompagnent d’une hypertrophie de membre.</p>')
a('TSC1',[('T','Tuberous (tubéreuse)'),('S','Sclerosis (sclérose)'),('C','Complex (complexe)'),('1','gène 1')],'Gène TSC1',
 '<p>Gène de l’hamartine, frein de la voie mTOR. Sa perte de fonction, comme celle de TSC2, active mTOR dans la sclérose tubéreuse et la lymphangioléiomyomatose.</p>')
a('TSC2',[('T','Tuberous (tubéreuse)'),('S','Sclerosis (sclérose)'),('C','Complex (complexe)'),('2','gène 2')],'Gène TSC2',
 '<p>Gène de la tubérine, frein de la voie mTOR. Ses variants pathogènes, comme ceux de TSC1, activent mTOR dans la lymphangioléiomyomatose ; le sirolimus inhibe mTOR.</p>')
a('CD31',[('CD','Cluster of Differentiation (classe de différenciation)'),('31','31')],'Antigène CD31',
 '<p>Molécule d’adhésion des cellules endothéliales (aussi appelée PECAM-1). Son expression par les cellules tumorales confirme la nature vasculaire d’un angiosarcome.</p>')
a('PECAM-1',[('P','Platelet (plaquettaire)'),('E','Endothelial (endothéliale)'),('C','Cell (cellulaire)'),('A','Adhesion (d’adhésion)'),('M','Molecule (molécule)'),('1','1')],'Molécule d’adhésion plaquettaire et endothéliale 1',
 '<p>Autre nom de l’antigène CD31.</p>')
a('ERG',[('E','ETS (famille de facteurs de transcription « E26 transformation-specific »)'),('R','-Related (apparenté)'),('G','Gene (gène)')],'Facteur de transcription ERG',
 '<p>Facteur nucléaire spécifique des cellules endothéliales. Sa détection immunohistochimique aide à confirmer un angiosarcome.</p>')
a('MYC',[('MYC','MYéloCytomatose (oncogène du virus de la myélocytomatose aviaire)')],'Oncogène MYC',
 '<p>Facteur de transcription de la prolifération cellulaire. Son amplification de haut niveau caractérise une partie des angiosarcomes secondaires à l’irradiation ou au lymphœdème chronique (Manner et al., 2010).</p>')
a('D2-40',[('D2-40','nom du clone d’anticorps monoclonal, non développable')],'Anticorps D2-40 (antipodoplanine)',
 '<p>Anticorps monoclonal qui reconnaît la podoplanine, glycoprotéine des cellules endothéliales lymphatiques. Il distingue en histologie un vaisseau lymphatique d’un capillaire sanguin.</p>')

# ---- classifications et éponymes
a('CEAP',[('C','Clinique'),('E','Étiologique'),('A','Anatomique'),('P','Physiopathologique')],'Classification CEAP de la maladie veineuse chronique',
 '<p>Classification internationale de la maladie veineuse chronique. La classe clinique va de C0 (aucun signe) à C6 (ulcère veineux actif). La LiMA s’y réfère pour la prise en charge des bas de compression.</p>')
a('CLOVES',[('C','Congenital (congénitale)'),('L','Lipomatous'),('O','Overgrowth'),('V','Vascular malformations (malformations vasculaires)'),('E','Epidermal nevi (nævus épidermiques)'),('S','Scoliosis, skeletal and spinal anomalies (anomalies rachidiennes et squelettiques)')],'Syndrome CLOVES',
 '<p>Syndrome de croissance excessive lié à des variants somatiques de PIK3CA, avec masses lipomateuses et malformations vasculaires, notamment lymphatiques.</p>')
a('Stewart-Treves',[('Stewart','Fred W. Stewart, pathologiste américain'),('Treves','Norman Treves, chirurgien américain')],'Syndrome de Stewart-Treves',
 '<p>Angiosarcome (lymphangiosarcome) développé sur un lymphœdème chronique, décrit en 1948 après mastectomie. Il se manifeste par des macules ou nodules violacés et a un pronostic sombre.</p>','i89-stewart')
a('Klippel-Trénaunay',[('Klippel','Maurice Klippel, neurologue français'),('Trénaunay','Paul Trénaunay, médecin français')],'Syndrome de Klippel-Trénaunay',
 '<p>Malformation vasculaire combinée (capillaire, veineuse, souvent lymphatique) avec hypertrophie d’un membre, liée à des variants somatiques de PIK3CA. Elle entre dans le diagnostic différentiel d’un gros membre de l’enfant.</p>')

# ---- codes CIM-10-GM 2024 hors chapitre I (les codes I.. décimaux sont déjà acceptés par le moteur)
# N’écrire jamais « CIM » seul : écrire « CIM-10-GM » ou « CIM-11 ».
for c,tt in [('Q82.0','Lymphœdème héréditaire'),
             ('E88.2','Lipomatose, non classée ailleurs (dont lipœdème)'),
             ('E88.20','Lipœdème, stade I'),('E88.21','Lipœdème, stade II'),('E88.22','Lipœdème, stade III'),
             ('J94.0','Épanchement chyleux'),
             ('L03.1','Phlegmon d’autres parties d’un membre'),
             ('L98.4','Ulcérations chroniques de la peau, non classées ailleurs'),
             ('B74.0','Filariose à Wuchereria bancrofti'),
             ('R59.0','Adénopathies localisées'),('R59.9','Adénopathie, sans précision')]:
    a(c,[(c,'code de la Classification internationale des maladies, 10e révision, modification allemande')],tt,'<p>Code CIM-10-GM 2024.</p>')
