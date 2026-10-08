# Glossaire MEDINA — chapitre I44 Troubles de la conduction et bradycardies
from cardio_1 import a, G

# ---- troubles de la conduction
a('BAV',[('B','Bloc'),('A','Auriculo-'),('V','Ventriculaire')],'Bloc auriculoventriculaire',
 '<p>Retard ou interruption de la conduction entre les oreillettes et les ventricules. Premier degré (PR &gt; 200 ms), deuxième degré (Mobitz I, Mobitz II, 2:1, haut degré), troisième degré (complet). Son pronostic dépend du siège : nodal ou infranodal.</p>','i44-site')
a('BBD',[('B','Bloc de'),('B','Branche'),('D','Droit')],'Bloc de branche droit',
 '<p>QRS ≥ 120 ms, rsR′ en V1–V2, onde S large en DI et V6. Fréquent et souvent bénin isolé ; associé à un hémibloc, il forme un bloc bifasciculaire.</p>','i44-bbd')
a('HBAG',[('H','Hémi-'),('B','Bloc'),('A','Antérieur'),('G','Gauche')],'Hémibloc antérieur gauche',
 '<p>Bloc du fascicule antérieur de la branche gauche : axe entre −45° et −90°, qR en aVL, rS en DII, DIII et aVF, QRS &lt; 120 ms.</p>','i44-hbag')
a('HBPG',[('H','Hémi-'),('B','Bloc'),('P','Postérieur'),('G','Gauche')],'Hémibloc postérieur gauche',
 '<p>Bloc du fascicule postérieur de la branche gauche : axe entre +90° et +180°, rS en DI et aVL, qR en DIII et aVF ; diagnostic d’élimination.</p>','i44-hbpg')
a('PP',[('P','onde P'),('P','onde P suivante')],'Intervalle PP',
 '<p>Intervalle entre deux ondes P successives ; sa mesure au compas distingue un arrêt sinusal, un bloc sino-auriculaire et une onde P prématurée bloquée.</p>','i44-bsa')

# ---- stimulation
a('NBG',[('N','NASPE (North American Society of Pacing and Electrophysiology)'),('B','BPEG (British Pacing and Electrophysiology Group)'),('G','Generic (code générique)')],'Code générique NASPE/BPEG des modes de stimulation',
 '<p>Code à cinq positions : cavité stimulée, cavité détectée, réponse à la détection, asservissement de fréquence, stimulation multisite. Version révisée en 2002.</p>','i44-nbg')
a('NASPE',[('N','North'),('A','American'),('S','Society of'),('P','Pacing and'),('E','Electrophysiology')],'North American Society of Pacing and Electrophysiology',
 '<p>Société savante nord-américaine de stimulation et d’électrophysiologie, devenue la Heart Rhythm Society ; coautrice du code NBG.</p>','i44-nbg')
a('BPEG',[('B','British'),('P','Pacing and'),('E','Electrophysiology'),('G','Group')],'British Pacing and Electrophysiology Group',
 '<p>Groupe britannique de stimulation et d’électrophysiologie ; coauteur du code NBG.</p>','i44-nbg')
for k,lit,full,d in [
 ('AAI',[('A','stimulation Auriculaire'),('A','détection Auriculaire'),('I','Inhibition par une activité détectée')],'Mode de stimulation auriculaire inhibée','<p>Stimule l’oreillette si aucune onde P spontanée n’est détectée. Suppose une conduction auriculoventriculaire saine.</p>'),
 ('AAIR',[('A','stimulation Auriculaire'),('A','détection Auriculaire'),('I','Inhibition'),('R','Rate modulation (asservissement de fréquence)')],'Mode auriculaire inhibé avec asservissement de fréquence','<p>AAI dont la fréquence augmente avec l’activité physique ; exposé à l’apparition ultérieure d’un BAV (essai DANPACE).</p>'),
 ('VVI',[('V','stimulation Ventriculaire'),('V','détection Ventriculaire'),('I','Inhibition par une activité détectée')],'Mode de stimulation ventriculaire inhibée','<p>Stimule le ventricule si aucun QRS spontané n’est détecté, sans tenir compte de l’oreillette ; peut provoquer un syndrome du stimulateur en rythme sinusal.</p>'),
 ('VVIR',[('V','stimulation Ventriculaire'),('V','détection Ventriculaire'),('I','Inhibition'),('R','Rate modulation (asservissement de fréquence)')],'Mode ventriculaire inhibé avec asservissement de fréquence','<p>Mode de choix en fibrillation auriculaire permanente.</p>'),
 ('DDD',[('D','stimulation Double (oreillette et ventricule)'),('D','détection Double'),('D','réponse Double : inhibition et déclenchement')],'Mode de stimulation double chambre','<p>Une onde P détectée déclenche une stimulation ventriculaire après le délai auriculoventriculaire ; une activité spontanée inhibe. Maintient la synchronie auriculoventriculaire.</p>'),
 ('DDDR',[('D','stimulation Double'),('D','détection Double'),('D','réponse Double'),('R','Rate modulation (asservissement de fréquence)')],'Mode double chambre avec asservissement de fréquence','<p>DDD dont la fréquence de base augmente avec l’activité ; indiqué en cas d’incompétence chronotrope.</p>'),
 ('VDD',[('V','stimulation Ventriculaire'),('D','détection Double'),('D','réponse Double')],'Mode de stimulation ventriculaire synchronisée à l’oreillette','<p>Détecte l’oreillette et le ventricule, ne stimule que le ventricule ; possible avec une sonde unique.</p>'),
 ('DOO',[('D','stimulation Double'),('O','aucune détection'),('O','aucune réponse')],'Mode double chambre asynchrone','<p>Stimulation à fréquence fixe sans détection : réponse habituelle à l’aimant, mode utilisé pendant une IRM ou un bistouri électrique chez le patient dépendant.</p>'),
 ('VOO',[('V','stimulation Ventriculaire'),('O','aucune détection'),('O','aucune réponse')],'Mode ventriculaire asynchrone','<p>Stimulation ventriculaire à fréquence fixe sans détection.</p>')]:
    a(k,lit,full,d,'i44-nbg')

# ---- sociétés, référentiels
a('HRS',[('H','Heart'),('R','Rhythm'),('S','Society')],'Heart Rhythm Society (Société américaine du rythme cardiaque)',
 '<p>Société savante internationale de rythmologie basée aux États-Unis ; coautrice des recommandations de standardisation de l’électrocardiogramme (2009) et d’une recommandation sur la stimulation physiologique (2023).</p>')
a('ACCF',[('A','American'),('C','College of'),('C','Cardiology'),('F','Foundation')],'American College of Cardiology Foundation',
 '<p>Fondation de la société savante américaine de cardiologie ; coautrice des recommandations AHA/ACCF/HRS 2009 d’interprétation de l’électrocardiogramme.</p>')

# ---- aides pédagogiques
a('MILTHA',[('M','Médicaments'),('I','Ischémie'),('L','Lyme et inflammations'),('T','Thyroïde (hypothyroïdie)'),('H','Hyperkaliémie, Hypothermie'),('A','Apnées du sommeil, Athlète')],'Aide-mémoire des causes réversibles de bradycardie',
 '<p>Aide pédagogique créée pour ce cours, non critère officiel.</p>','i44-mnemo-miltha')
a('BRASH',[('B','Bradycardia (bradycardie)'),('R','Renal failure (insuffisance rénale)'),('A','Atrioventricular nodal blockade (médicament bloqueur du nœud)'),('S','Shock (choc)'),('H','Hyperkalaemia (hyperkaliémie)')],'Syndrome BRASH',
 '<p>Cercle auto-entretenu associant hyperkaliémie modérée, bradycardisant, bradycardie et insuffisance rénale (Farkas et collaborateurs, 2020). Acronyme descriptif, non critère officiel.</p>','i44-brash')
a('SILC',[('S','Suspicious'),('I','Index in'),('L','Lyme'),('C','Carditis')],'Score de suspicion de cardite de Lyme',
 '<p>Score de probabilité clinique d’une cardite de Lyme devant un BAV (équipe de Baranchuk, 2018) ; aide pédagogique, non critère officiel.</p>','i44-lyme')
a('COSTAR',[('C','Constitutional symptoms (signes généraux)'),('O','Outdoor activity (activité en plein air, zone d’endémie)'),('S','Sex (sexe masculin)'),('T','Tick bite (piqûre de tique)'),('A','Age (âge &lt; 50 ans)'),('R','Rash (érythème migrant)')],'Aide-mémoire des éléments du score SILC',
 '<p>Aide pédagogique, non critère officiel.</p>','i44-lyme')

# ---- essais
a('DANPACE',[('DAN','DANish (danois)'),('PACE','PACEmaker (nom de l’essai : single lead atrial pacing versus dual chamber pacing in sick sinus syndrome)')],'Essai danois de stimulation dans la maladie du sinus',
 '<p>Essai randomisé comparant AAIR et DDDR dans la dysfonction sinusale (2011) : mortalité identique, plus de fibrillation auriculaire paroxystique et deux fois plus de réinterventions avec l’AAIR.</p>','i44-modes')
a('BLOCK HF',[('BLOCK HF','nom de l’essai, non développable lettre à lettre (Biventricular versus Right Ventricular Pacing in Heart Failure Patients with Atrioventricular Block)')],'Essai BLOCK HF',
 '<p>Essai randomisé (2013) chez des patients en BAV avec fraction d’éjection ≤ 50 % : la resynchronisation a réduit le critère composite de décès, consultations urgentes pour insuffisance cardiaque et remodelage, par rapport à la stimulation ventriculaire droite.</p>','crt')
a('WRAP-IT',[('WRAP-IT','World-wide Randomized Antibiotic envelope Infection Prevention Trial')],'Essai WRAP-IT',
 '<p>Essai randomisé (2019) : l’enveloppe antibactérienne autour du boîtier a réduit les infections majeures de dispositif chez des patients à risque (remplacements, mises à niveau).</p>','i44-d-antibio')
a('PADIT',[('PADIT','Prevention of Arrhythmia Device Infection Trial')],'Essai PADIT',
 '<p>Essai randomisé en grappes et croisé (2018) : une prophylaxie renforcée (céfazoline et vancomycine avant l’intervention, lavage de la loge à la bacitracine, céphalexine orale pendant deux jours) n’a pas réduit significativement les hospitalisations pour infection par rapport à la céfazoline préopératoire seule.</p>','i44-d-antibio')
a('BRUISE CONTROL',[('BRUISE','Bridge or continue coumadin for device surgery randomized controlled trial'),('CONTROL','nom de l’essai, non une abréviation')],'Essai BRUISE CONTROL',
 '<p>Essai randomisé (2013) : poursuivre la warfarine plutôt qu’un relais par héparine réduit les hématomes de loge (3,5 % contre 16 %).</p>','i44-d-anticoag')
a('BRUISE CONTROL-2',[('BRUISE CONTROL','nom de l’essai (voir BRUISE CONTROL)'),('2','deuxième essai, consacré aux anticoagulants oraux directs')],'Essai BRUISE CONTROL-2',
 '<p>Essai randomisé (2018) : poursuite ou brève interruption d’un anticoagulant oral direct donnent un taux d’hématome identique et faible.</p>','i44-d-anticoag')
a('SPAIN',[('SPAIN','nom de l’essai espagnol, non une abréviation (Closed-loop stimulation in the prevention of vasovagal syncope)')],'Essai SPAIN',
 '<p>Essai randomisé croisé (2017) : la stimulation double chambre à boucle fermée a réduit les syncopes chez des patients avec syncope réflexe cardio-inhibitrice au test d’inclinaison.</p>','i44-reflexe')
a('BIOSync CLS',[('BIOSync','nom de l’essai, non développable lettre à lettre (Benefit Of dual-chamber pacing with closed loop stimulation in tilt-induced cardio-inhibitory reflex SYNCope)'),('CLS','Closed Loop Stimulation (stimulation à boucle fermée)')],'Essai BIOSync CLS',
 '<p>Essai randomisé en double aveugle (2021) : chez des patients de plus de 40 ans avec asystolie au test d’inclinaison, la stimulation à boucle fermée a réduit les récidives de syncope par rapport à une stimulation placebo.</p>','i44-reflexe')
a('ISSUE-3',[('ISSUE','International Study on Syncope of Uncertain Etiology'),('3','troisième étude de la série')],'Essai ISSUE-3',
 '<p>Essai randomisé en double aveugle (2012) : chez des patients de plus de 40 ans avec pauses asystoliques documentées par moniteur implantable, la stimulation double chambre a réduit environ de moitié les récidives de syncope.</p>','i44-reflexe')
a('PATCH',[('PATCH','Preventive Approach to Congenital Heart block with Hydroxychloroquine')],'Essai PATCH',
 '<p>Étude prospective (2020) : l’hydroxychloroquine chez des mères porteuses d’anticorps anti-Ro ayant eu un enfant atteint a réduit la récidive du BAV congénital par rapport aux données historiques.</p>','i44-congen')
a('ARIC',[('A','Atherosclerosis'),('R','Risk in'),('C','Communities (cohorte)')],'Cohorte ARIC',
 '<p>Cohorte prospective américaine ; elle a fourni une estimation de l’incidence de la dysfonction sinusale (environ 0,8 pour 1 000 personnes-années).</p>')

# ---- génétique
a('TRPM4',[('T','Transient'),('R','Receptor'),('P','Potential cation channel'),('M','subfamily M (mélastatine)'),('4','membre 4')],'Canal cationique TRPM4',
 '<p>Canal cationique activé par le calcium, exprimé dans le tissu de conduction ; ses variants causent des maladies progressives de la conduction familiales.</p>','i44-scn5a')
a('NKX2-5',[('NK','Nirenberg et Kim (découvreurs de la famille de gènes)'),('X','homéoboîte (homeoboX)'),('2','famille NK2'),('-5','membre 5')],'Facteur de transcription NKX2-5 (NK2 homeobox 5)',
 '<p>Facteur de transcription du développement cardiaque ; ses variants associent communication interauriculaire et BAV progressif.</p>')
a('TBX5',[('T','T (gène Brachyury, fondateur de la famille)'),('BX','BoX (domaine de liaison à l’ADN)'),('5','membre 5')],'Facteur de transcription TBX5',
 '<p>Facteur de transcription à boîte T ; ses variants causent le syndrome de Holt-Oram (anomalies des membres supérieurs, communication interauriculaire, troubles de conduction).</p>')
a('DMPK',[('D','Dystrophia'),('M','Myotonica'),('P','Protein'),('K','Kinase')],'Protéine kinase de la dystrophie myotonique',
 '<p>Gène dont l’expansion de triplets CTG cause la dystrophie myotonique de type 1 ; atteinte progressive du His-Purkinje.</p>','i44-neuromusc')
a('CTG',[('C','Cytosine'),('T','Thymine'),('G','Guanine')],'Triplet nucléotidique CTG',
 '<p>Triplet répété dans le gène <i>DMPK</i> ; au-delà d’environ 50 répétitions, dystrophie myotonique de type 1, plus sévère avec le nombre de répétitions.</p>','i44-neuromusc')
a('CYP1A2',[('CYP','CYtochrome P450'),('1','famille 1'),('A','sous-famille A'),('2','isoforme 2')],'Cytochrome P450 1A2',
 '<p>Enzyme hépatique qui métabolise la théophylline ; inhibée par la ciprofloxacine et la fluvoxamine.</p>','i44-d-theo')

# ---- noms propres composés
a('Stokes-Adams',[('Stokes-Adams','noms de deux médecins irlandais (William Stokes, Robert Adams), non une abréviation')],'Syncope de Stokes-Adams',
 '<p>Perte de connaissance brutale par asystolie, classiquement lors d’un BAV paroxystique.</p>','i44-s-syncope')
a('Lev-Lenègre',[('Lev-Lenègre','noms de deux auteurs (Maurice Lev, Jean Lenègre), non une abréviation')],'Maladie de Lev-Lenègre',
 '<p>Fibrose dégénérative progressive du tissu de conduction ; première cause de BAV complet du sujet âgé.</p>','i44-lev')
a('Kearns-Sayre',[('Kearns-Sayre','noms de deux médecins de la Mayo Clinic (Thomas P. Kearns, ophtalmologiste ; George P. Sayre, anatomopathologiste), non une abréviation')],'Syndrome de Kearns-Sayre',
 '<p>Maladie mitochondriale associant ophtalmoplégie externe, rétinopathie pigmentaire et troubles de conduction pouvant aller jusqu’au bloc complet.</p>','i44-neuromusc')
a('Holt-Oram',[('Holt-Oram','noms de deux médecins britanniques (Mary Holt, Samuel Oram), non une abréviation')],'Syndrome de Holt-Oram',
 '<p>Maladie autosomique dominante liée à <i>TBX5</i> : anomalies des membres supérieurs, communication interauriculaire, troubles de conduction.</p>')

# ---- notation électrocardiographique des morphologies du QRS
for k,lit,full in [
 ('rSR′',[('r','petite onde R initiale'),('S','onde S'),('R′','seconde onde R, ample (R prime)')],'Morphologie rSR′ du QRS'),
 ('rsr′',[('r','petite onde R initiale'),('s','petite onde S'),('r′','seconde petite onde R (r prime)')],'Morphologie rsr′ du QRS')]:
    a(k,lit,full,'<p>Notation des ondes du QRS : majuscule pour une onde ample, minuscule pour une onde de faible amplitude, prime pour une seconde onde de même nom. Les aspects à double onde R en V1–V2 caractérisent le retard droit.</p>','i44-bbd')
a('His-Purkinje',[('His-Purkinje','noms de deux anatomistes (Wilhelm His junior, Jan Evangelista Purkinje), non une abréviation')],'Système His-Purkinje',
 '<p>Faisceau de His, branches et réseau de Purkinje : partie infranodale et rapide du tissu de conduction, dépendante du courant sodique et peu sensible au système nerveux autonome.</p>','i44-site')
a('rS',[('r','petite onde R positive initiale'),('S','grande onde S négative')],'Morphologie rS du QRS',
 '<p>Petite onde R suivie d’une grande onde S : aspect normal en V1, et en DII, DIII et aVF dans l’hémibloc antérieur gauche.</p>','i44-hbag')
