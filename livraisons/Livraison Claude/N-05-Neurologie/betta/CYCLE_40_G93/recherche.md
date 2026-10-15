# G93 — Autres affections du cerveau (N-05-Neurologie) — dossier de recherche

Cycle Betta 40, leçon 1 · agent C40-A4-NEUR (Opus 5.5) · 15.10.2026
Statut : recherche brute pour l'agent de rédaction. Audit différé — revue IA, distincte d'une validation médicale humaine.
Règle : chaque fait porte sa référence [Sx] (voir `sources.json`). Ce qui n'a pas été lu figure dans « Lacunes ». Aucune donnée de mémoire.
Note de méthode : le quota WebSearch de la session était épuisé ; recherche faite par PubMed (métadonnées et résumés), Europe PMC, WebFetch de textes PMC en libre accès et `tools/swissmedic_fi.py`. Les textes intégraux ERC-ESICM 2025 et EAN 2020 (troubles de la conscience) sont restés inaccessibles (403).

## 0. Question clinique et logique de la leçon
G93 est une catégorie « résiduelle » qui regroupe des affections cérébrales hétérogènes [S1]. Pour l'examen fédéral, quatre entités portent l'essentiel : l'hypertension intracrânienne idiopathique (G93.2), la lésion cérébrale anoxique après arrêt cardiaque (G93.1), l'œdème et la compression cérébrale avec engagement (G93.6, G93.5) et le syndrome de fatigue chronique / encéphalomyélite myalgique (G93.3). Les kystes arachnoïdiens (G93.0), le syndrome de Reye (G93.7) et le syndrome apallique (G93.80) complètent la catégorie. Proposition de plan : une partie commune (pression intracrânienne, Monro-Kellie, œdème) puis une monographie courte par sous-code, la HII et l'encéphalopathie post-anoxique étant les plus développées.

## 1. Définition et périmètre CIM-10-GM 2024 [S1]
- G93.0 Kystes cérébraux : inclut kyste porencéphalique et kyste arachnoïdien ; exclut kystes cérébraux congénitaux (Q04.6) et kystes périventriculaires acquis du nouveau-né (P91.1).
- G93.1 Lésion cérébrale anoxique NCA : exclut les complications d'avortement/grossesse extra-utérine/môle (O00–O07, O08.8), de chirurgie et de soins (T80–T88), de grossesse/travail/post-partum (O29.2, O74.3, O89.2) et l'asphyxie néonatale (P21.9).
- G93.2 Hypertension intracrânienne bénigne [pseudotumor cerebri] ; exclut l'encéphalopathie hypertensive (I67.4). Libellé OFS : « hypertension intracrânienne idiopathique ».
- G93.3 Syndrome de fatigue chronique : inclut SFC avec dysfonction immunitaire, encéphalomyélite myalgique, syndrome de fatigue (chronique) post-viral.
- G93.4 Encéphalopathie SAI : exclut encéphalopathie alcoolique (G31.2) et toxique (G92.-).
- G93.5 Compression du cerveau : inclut hernie (engagement) et compression du cerveau (tronc cérébral) ; exclut la compression traumatique diffuse (S06.28) et circonscrite (S06.38).
- G93.6 Œdème cérébral : exclut œdème par traumatisme obstétrical (P11.0) et traumatique (S06.1).
- G93.7 Syndrome de Reye : code supplémentaire (chapitre XX) pour la cause externe.
- G93.8- Autres affections précisées : G93.80 syndrome apallique ; G93.88 autres (inclut l'encéphalopathie post-radique) ; code du chapitre XX pour la cause externe.
- G93.9 Affection du cerveau SAI.
- Message didactique : le code G93 est choisi lorsqu'aucun code étiologique plus précis n'existe ; un œdème ou une compression d'origine traumatique relève de S06 [S1].

## 2. Socle commun : pression intracrânienne, œdème, engagement (G93.5, G93.6)
### 2.1 Physiologie normale → pathologique [S7]
- Doctrine de Monro-Kellie : la pression intracrânienne (PIC) dépend de la somme des volumes de sang, de cerveau et de LCS contenus dans une boîte crânienne rigide ; tout gonflement (œdème, hématome) augmente la PIC.
- Compliance : indice pression-volume normal ≈ 20–25 mL.
- Cascade : HTIC → baisse de la pression de perfusion cérébrale et du débit sanguin cérébral → lésion irréversible, engagement, décès.
- Seuil de traitement admis dans les recommandations de TCC : PIC 20–22 mmHg ; HTIC > 20–22 mmHg chez 45–80 % des TCC, association dose-dépendante avec le pronostic.
### 2.2 Classification de l'œdème cérébral [S7]
- Cytotoxique (cellulaire) : défaillance des pompes (Na+/K+-ATPase) ou activation de canaux → eau dans les cellules ; redistribue l'eau sans augmenter l'eau cérébrale totale ; dès ~1 h après un TCC.
- Ionique : flux net d'eau capillaire → interstitium par transport ionique endothélial, sans rupture de la barrière hémato-encéphalique (BHE).
- Vasogénique : rupture de la BHE → passage d'eau et de protéines dans l'interstitium ; pic 6–24 h ; perméabilité maximale les premières heures, persistant 3–4 jours, second pic possible vers J5.
- Osmotique/contusionnel : le noyau nécrotique hyperosmolaire d'une contusion attire l'eau.
- Continuum cytotoxique → vasogénique → hémorragie secondaire progressive.
- Acteurs moléculaires : NKCC1 (activé par K+ extracellulaire, surexprimé dès 1 h), canal SUR1-TRPM4 (non exprimé normalement, ouvert par la déplétion en ATP), aquaporine-4 (entrée d'eau dans l'œdème cytotoxique, clairance dans l'œdème vasogénique), MMP-2/MMP-9, VEGF-A, cytokines.
- Œdème présent chez > 60 % des patients avec lésion expansive et ≈ 15 % avec scanner initial normal (TCC).
- Imagerie : la diffusion (ADC) distingue composantes cellulaire et vasogénique ; la déviation de la ligne médiane sert de mesure de l'œdème dans les essais d'AVC.
### 2.3 Traitements de l'œdème / de l'HTIC
- Osmothérapie (mannitol, sérum salé hypertonique) : abaisse la PIC, effet incertain sur le pronostic [S7].
- Mannitol 20 % (FI suisse) [S12] : indications incluant le traitement de l'hypertension intracrânienne et l'« osmothérapie et prévention d'un œdème cérébral » ; dose HTIC 1–2 g/kg en 30–60 min (p. ex. 500 mL de Mannitol 20 % en 1 h) ; pas plus de 500 mL/24 h (contexte oligurie) ; voie i.v. seulement. Mécanisme : filtré, non réabsorbé → diurèse osmotique ; « abaissement de la pression intraoculaire et diminution de l'œdème cérébral ». Contre-indications : insuffisance cardiaque, congestion/œdème pulmonaire, déshydratation importante, hémorragie cérébrale (sauf craniotomie), anurie ne répondant pas à une dose-test, hyperosmolarité plasmatique préexistante, troubles de la barrière hémato-méningée. Surveillance : PVC, fonction rénale, électrolytes, trou osmotique ; peut abaisser la natrémie (transfert d'eau intracellulaire) et masquer une hypovolémie ; risque d'insuffisance rénale accru si néphropathie ou néphrotoxiques.
- Craniectomie décompressive : baisse de la PIC et de la mortalité dans de grands essais (TCC), bénéfice fonctionnel incertain [S7].
- Hypothermie : baisse la PIC, bénéfice clinique incertain [S7].
- Glibenclamide (inhibiteur SUR1) : réduction de l'expansion des contusions sans changement du devenir dans un essai de 66 sujets ; essai d'AVC de phase II : moins de déviation de ligne médiane [S7]. Ne pas présenter comme traitement établi.
- Corticoïdes : non traités par S7 → lacune (voir §9).
- Acétazolamide (FI suisse) : « œdèmes cérébraux » figure parmi les indications [S11].

## 3. G93.2 — Hypertension intracrânienne idiopathique (HII) [S2 sauf mention]
### 3.1 Définition et nomenclature
- HII = élévation de la PIC sans cause identifiable. « Pseudotumor cerebri » est désormais un terme parapluie pour toute HTIC chronique, primaire (HII) ou secondaire.
### 3.2 Épidémiologie
- Prévalence estimée 0,5–2/100 000 dans la population générale ; femmes obèses en âge de procréer surtout ; > 90–95 % obèses ; survenue décrite après prise de 5–15 % du poids ; probablement sous-diagnostiquée et en hausse avec l'obésité.
### 3.3 Physiopathologie
- Étiologie largement inconnue ; traitements visant la sécrétion de LCS (plexus choroïdes). Pistes : peptides intestinaux (GLP-1), activité locale du cortisol via 11β-HSD1. Sténose des sinus transverses possiblement conséquence plutôt que cause de l'HTIC (débattu). Troubles cognitifs (temps de réaction, vitesse de traitement) pouvant persister après normalisation de la PIC.
### 3.4 Clinique
- Céphalées jusqu'à 90 % (pression/« explosives », frontales ou rétro-orbitaires, souvent migraineuses) ; abus médicamenteux > 1/3 (37 %).
- Obscurcissements visuels transitoires, flou, diplopie (paralysie du VI uni- ou bilatérale) ; acouphène pulsatile fréquent ; troubles olfactifs jusqu'à 80 % (inutiles au diagnostic).
- Signe cardinal : œdème papillaire bilatéral, asymétrique dans ≈ 4 %.
- Erreur diagnostique ≈ 40 %, surtout par examen ophtalmologique incorrect.
### 3.5 Critères diagnostiques
- Syndrome défini par les critères de Friedman 2013 (figure non lue → lacune), y compris une version sans œdème papillaire.
- Pression d'ouverture (décubitus latéral, jambes étendues, sans sédation) : normale ≤ 25 cmH2O chez l'adulte, ≤ 28 cmH2O chez l'enfant ; zone grise 25–30 cmH2O ; PIC parfois intermittente → répéter ou monitorer si mesure normale.
- HII sans œdème papillaire : certaine si paralysie du VI uni/bilatérale ; possible sans VI si ≥ 3 des 4 signes IRM : selle turcique vide, aplatissement postérieur du globe, élargissement de l'espace périoptique, sténose des sinus transverses.
- Céphalée attribuée à l'HII (ICHD-3) : céphalée nouvelle ou nettement aggravée ; HII diagnostiquée avec pression du LCS > 250 mm (280 mm chez l'enfant obèse) ; lien temporel ou acouphène pulsatile ou œdème papillaire ; pas mieux expliquée. L'ICHD-3 a retiré l'exigence d'amélioration après baisse de pression ; ≈ 2/3 gardent des céphalées malgré une PIC normale.
### 3.6 Examens
- IRM : examen de référence pour exclure une cause secondaire ; signes de soutien : selle vide, aplatissement du globe, gaine du nerf optique élargie, tortuosité du nerf optique ; ventricules de taille normale ; aucun signe pathognomonique.
- Veinographie (ARM ou angio-CT veineux) toujours, pour exclure une thrombose veineuse cérébrale ; sténose transverse jusqu'à 90 % des HII mais asymétrie aussi chez 50 % des sujets sains.
- Ponction lombaire obligatoire (mesure de pression, conditions ci-dessus).
- Bilan sanguin individualisé selon causes secondaires.
- Ophtalmologie : acuité, pupilles, périmétrie formelle, fond d'œil dilaté ; exclure un pseudo-œdème papillaire ; déficits typiques : élargissement de la tache aveugle, rétrécissement périphérique, ressaut nasal inférieur, déficit arciforme partiel. Œdème papillaire de haut grade et baisse d'acuité initiale prédisent une perte de champ visuel.
- OCT : quantifie l'œdème papillaire et suit son évolution ; ne distingue pas, par la seule épaisseur RNFL, la résolution de l'œdème d'une atrophie optique.
### 3.7 Diagnostic différentiel — causes secondaires (tableau 4 de S2)
- Obstruction veineuse : thrombophilie, lupus, otite/mastoïdite, infection du SNC, hypertension pulmonaire, BPCO, syndrome cave supérieur, fistule artérioveineuse, tumeur glomique, tumeur compressive.
- Médicaments : fluoroquinolones, tétracyclines, vitamine A et rétinoïdes, stéroïdes anabolisants, sevrage de corticoïdes, hormone de croissance, lithium, acide nalidixique, contraceptifs oraux, implant de lévonorgestrel, amiodarone, ciclosporine, cytarabine.
- Autres : VIH, syphilis, borréliose, varicelle, maladie d'Addison, hypoparathyroïdie, apnées du sommeil, urémie, anémie ferriprive sévère, insuffisance rénale, syndromes de Turner et de Down.
### 3.8 Prise en charge
- Perte de poids : seule thérapie modificatrice établie ; à aborder avec tact avec chaque patient [S2]. Chirurgie bariatrique : −27,2 à −27,8 kg à 24 mois et plus forte baisse de PIC (−11,9 cmH2O) ; intervention multicomposante + acétazolamide : −11,2 cmH2O à 6 mois ; perte de poids fortement corrélée à la baisse de PIC ; bariatrique à considérer si IMC ≥ 35 kg/m² (grade A), intervention de mode de vie multicomposante si IMC < 35 (grade B) [S3]. Mortalité bariatrique 0,05–0,14 % ; résolution de l'œdème papillaire 100 % et amélioration des céphalées 90 % dans une revue systématique [S2].
- Acétazolamide (première ligne) : seul médicament évalué en essais randomisés ; Cochrane 2015 : bénéfice modeste, preuves insuffisantes ; IIHTT : bénéfice sur le champ visuel en cas de perte visuelle légère ; > 40 % des patients IIHTT à 4 g/j (souvent mal toléré) ; 48 % d'arrêts à 1500 mg dans des études antérieures ; effets : paresthésies, dysgueusie, vomissements, diarrhée, malaise, fatigue, dépression ; pas d'effet sur le HIT-6 [S2].
- Acétazolamide, FI suisse Diamox® [S11] : l'HII n'est pas une indication nommée (indication « œdèmes cérébraux ») ; comprimés 250 mg ; contre-indications : hyponatrémie/hypokaliémie, insuffisance rénale ou hépatique grave (dont cirrhose), insuffisance surrénalienne, acidose hyperchlorémique, hypersensibilité aux sulfamides ; mises en garde : réactions cutanées graves (SJS/NET, PEAG), agranulocytose, anémie aplasique, hyponatrémie, hypokaliémie, acidose métabolique, lithiase rénale, œdème pulmonaire non cardiogénique, idées suicidaires, épanchement choroïdien ; contrôle formule sanguine et électrolytes avant et pendant ; grossesse : ne pas utiliser, surtout au 1er trimestre, sauf nécessité absolue ; allaitement : passage dans le lait.
- Topiramate : étude ouverte (n = 40) d'équivalence avec l'acétazolamide ; favorise la perte de poids ; contre-indiqué pendant la grossesse selon S2. Furosémide, bumétanide, amiloride : preuves animales ou séries minimes ; octréotide : étude ouverte n = 26 [S2].
- Chirurgie si baisse visuelle rapide : dérivation du LCS (ventriculo-péritonéale préférée à lombo-péritonéale : 1,8 vs 4,3 révisions/patient ; 51 % de révision, 30 % multiples) ; fenestration de la gaine du nerf optique (26 % de révision) ; stenting des sinus veineux (débattu ; resténose adjacente, 1/3 retraités ; rarement perforation, hématome sous-dural, décès). « Pas de dérivation pour une céphalée isolée » ; céphalée persistante après dérivation 68 % à 6 mois, 79 % à 2 ans [S2].
- HII fulminante : PL itératives temporaires pour préserver la vision en attendant la dérivation [S2].
- PL thérapeutique au long cours non recommandée : effet bref (−1 point/10 sur la céphalée), aggravation de la céphalée la semaine suivante chez 64 % [S2].
- Céphalées : sevrage de l'abus médicamenteux ; rechercher une migraine associée ; prophylaxie possible (topiramate, candésartan, toxine onabotulinique) ; éviter les médicaments faisant prendre du poids [S2].
### 3.9 Situations particulières et suivi
- Grossesse : décisions au cas par cas ; conseil sur la prise de poids gestationnelle ; acétazolamide controversé ; topiramate à proscrire ; PL itératives, fenestration ou dérivation si vision menacée ; pas de changement du mode d'accouchement sur un antécédent seul [S2].
- HII sans œdème papillaire : morbidité céphalalgique ; pas de risque visuel décrit ; pas de surveillance visuelle au long cours ; chirurgie non recommandée en routine [S2].
- Suivi : surveillance ophtalmologique rapprochée (fonction visuelle, périmétrie) tant que l'œdème papillaire est actif ; prise en charge neurologique des céphalées ; conseil pondéral [S2].

## 4. G93.1 — Lésion cérébrale anoxique (hypoxique-ischémique) après arrêt cardiaque [S4 ; S5 version 2025 non lue]
### 4.1 Mécanismes
- Le syndrome post-arrêt cardiaque comprend la lésion cérébrale hypoxique-ischémique, la dysfonction myocardique, la réponse systémique d'ischémie-reperfusion et la pathologie déclenchante.
- Facteurs aggravants associés : hypotension, hypoxémie, hyperoxémie, fièvre, hypo- et hyperglycémie, convulsions ; l'hypocapnie vasoconstricte (baisse du débit cérébral) ; l'hypercapnie augmente débit et PIC.
### 4.2 Réanimation post-arrêt (objectifs chiffrés)
- SpO2 94–98 % (PaO2 10–13 kPa / 75–100 mmHg) ; éviter hypoxémie et hyperoxémie.
- Normocapnie : PaCO2 4,5–6,0 kPa (35–45 mmHg).
- Éviter PAM < 65 mmHg ; viser une PAM assurant diurèse > 0,5 mL/kg/h et lactate normal ou décroissant.
- Température : cible constante 32–36 °C pendant ≥ 24 h ; éviter la fièvre (> 37,7 °C) pendant ≥ 72 h chez le patient resté comateux ; pas de solutés froids préhospitaliers.
- Convulsions : EEG pour diagnostiquer et suivre ; lévétiracétam ou valproate de sodium en première ligne avec sédatifs ; pas de prophylaxie systématique.
- La version ERC-ESICM 2025 [S5] couvre les mêmes thèmes ; ses éventuelles modifications chiffrées n'ont pas été lues → la rédaction doit dater ces valeurs « ERC-ESICM 2021 » et signaler la mise à jour 2025.
### 4.3 Pronostic neurologique (algorithme multimodal)
- Exclure d'abord les facteurs confondants : sédation résiduelle, curarisation, hypothermie, hypotension sévère, hypoglycémie, sepsis, troubles métaboliques ou respiratoires.
- Patient comateux avec réponse motrice M ≤ 3 à ≥ 72 h du retour à une circulation spontanée (RACS).
- Pronostic défavorable probable si ≥ 2 des prédicteurs : absence des réflexes pupillaires et cornéens à ≥ 72 h ; absence bilatérale de l'onde N20 des PES à ≥ 24 h ; EEG hautement malin > 24 h (fond supprimé ± décharges périodiques, ou suppression-bouffées) ; NSE > 60 µg/L à 48 h et/ou 72 h ; état de mal myoclonique ≤ 72 h ; lésion anoxique diffuse et étendue au scanner/IRM (perte du rapport substance grise/blanche ; restriction de diffusion étendue).
- Aucun prédicteur n'est exact à 100 % ; risque de prophétie autoréalisatrice. Syndrome de Lance-Adams : myoclonies généralisées avec décharges épileptiformes chez des patients qui se réveillent.
- La décision de limitation thérapeutique est discutée séparément du pronostic neurologique et intègre âge, comorbidités, fonctions d'organes et volontés du patient.
### 4.4 Suites
- Évaluation fonctionnelle (déficits physiques et non physiques) avant la sortie, orientation en réadaptation ; suivi de tous les survivants dans les 3 mois : dépistage des troubles cognitifs, émotionnels et de la fatigue.
- Don d'organes : envisager chez les patients remplissant les critères neurologiques de décès, ou un don après arrêt circulatoire en cas de décision de limitation ; observation de 24 h après réchauffement à 36 °C avant les tests de mort cérébrale (algorithme S4) ; cadre légal local (en Suisse : directives ASSM non lues → lacune).
### 4.5 Troubles chroniques de la conscience (G93.80 syndrome apallique) [S8]
- EAN 2020 (panel de 10 pays, dont CHUV Lausanne ; méthode GRADE) : examen neurologique complet ; rechercher des mouvements oculaires volontaires au miroir ; répéter les évaluations cliniques en phase subaiguë et chronique avec la Coma Recovery Scale-Revised ; préférer le score FOUR au Glasgow en aigu ; EEG standard ; rechercher sommeil paradoxal et lent à l'EEG ; si possible TEP, IRMf de repos ou active, EEG haute densité quantitatif chez les patients sans réponse à la commande ; classer l'état de conscience selon le niveau le plus élevé révélé par l'une des trois approches.

## 5. G93.3 — Encéphalomyélite myalgique / syndrome de fatigue chronique (EM/SFC) [S6]
- Définition : intolérance à l'effort avec malaise post-effort (MPE) comme trait central ; aussi sommeil non réparateur, troubles cognitifs, intolérance orthostatique, douleurs. Diagnostic clinique, sans biomarqueur.
- Épidémiologie : prévalence 0,1–0,7 % ; incidence 0,015/1000 personnes-années ; ≈ 3 millions de cas en Europe (1 à > 5 millions) ; ≥ 2/3 de femmes ; coût ≈ 40 milliards €/an (extrapolé du Royaume-Uni).
- Critères adultes : IOM 2015 (≥ 6 mois) adaptés aux soins primaires ; critères canadiens (CCC) pour la confirmation, les sous-groupes et la recherche ; Fukuda/CDC-1994 utilisables en dépistage mais le MPE est exigé pour le diagnostic clinique. CCC : fatigue pathologique, MPE, troubles du sommeil, douleur, symptômes cognitifs, plus ≥ 2 catégories parmi autonome, neuroendocrine, immunitaire.
- Enfants : critères de Rowe 2017 ; CCC utilisables après 3 mois ; ≈ la moitié des formes post-infectieuses pédiatriques suivent une mononucléose à EBV ; implication de la famille et de l'école.
- Bilan de base : FSC, ferritine, enzymes hépatiques, fonction rénale, TSH/thyroïde, CRP ultrasensible ou VS, électrolytes (Na, K, Ca, phosphate), CK, glycémie à jeun ou HbA1c ; sérologies selon contexte (EBV, VHB, VHC, VIH, Lyme) ; tests spécialisés selon clinique (anti-CCP, anti-transglutaminase, cortisol matinal, B12, NT-proBNP, vitamine D).
- Exclusions si elles expliquent les symptômes : hypothyroïdie, cancer, SEP, insuffisance cardiaque, anémie sévère, insuffisance rénale, diabète, apnées du sommeil, abus de substances. Comorbidités compatibles : fibromyalgie, POTS, côlon irritable, anxiété/dépression légère, hypermobilité, migraine.
- Drapeaux rouges : perte de poids involontaire, fièvre prolongée ≥ 38 °C, marqueurs inflammatoires élevés persistants, anomalies d'examen significatives, idées suicidaires.
- Sévérité : sévère = quasi confiné au domicile ; très sévère = quasi alité.
- Prise en charge : gestion de l'énergie (pacing) centrale, règle pratique ≈ 2/3 de la durée et de l'intensité ayant déclenché les symptômes ; traitement des symptômes prioritaires (douleur, sommeil, intolérance orthostatique : bas de contention, apport de liquides et de sel ; doses initiales plus faibles par sensibilité) ; TCC : soutien possible, non curative, preuves limitées ; régimes d'exclusion non recommandés en général.
- Organisation : soins primaires pour le diagnostic initial, le suivi et la recherche d'autres diagnostics ; adresser au spécialiste pour confirmation, jeunes, formes sévères ou en aggravation ; 2–4 médecins spécialisés par million d'habitants.

## 6. G93.7 — Syndrome de Reye
- Maladie extrêmement rare mais grave ; décès 30–40 % par atteinte du tronc cérébral ; précédée d'une infection virale avec intervalle libre de 3–5 jours ; trouble généralisé du métabolisme mitochondrial → défaillance hépatique et d'autres tissus ; étiologie du Reye « classique » inconnue ; plusieurs maladies héréditaires du métabolisme et toxiques donnent un tableau « Reye-like » [S9]. L'auteur juge la causalité de l'aspirine insuffisamment établie (position à présenter comme débat, non comme consensus) [S9].
- FI suisse Aspirine® [S13] : chez les adolescents dès 12 ans avec fièvre et/ou infection virale, aspirine seulement sur prescription et en deuxième intention, en raison du risque de syndrome de Reye, « encéphalopathie potentiellement mortelle dont les principaux symptômes sont de forts vomissements ainsi que des troubles de la conscience et de la fonction hépatique » ; formes à croquer/granulé non indiquées avant 12 ans ; syndrome de Reye listé « très rare » parmi les effets indésirables.

## 7. G93.0 — Kystes cérébraux (arachnoïdiens, porencéphaliques)
- Prévalence des kystes arachnoïdiens 2,3 % (29/1235) dans une population suédoise ≥ 70 ans au scanner, sans différence de sexe ; pas plus de céphalées, vertiges, troubles cognitifs, dépression, épilepsie ni de mortalité qu'en l'absence de kyste → découverte fortuite généralement asymptomatique ; prudence avant de leur attribuer des symptômes et attitude thérapeutique restrictive [S10].
- Kyste porencéphalique : inclus dans G93.0 [S1] ; données cliniques non lues (lacune).

## 8. G93.4 / G93.88 / G93.9
- Encéphalopathie SAI et encéphalopathie post-radique : seule la nosologie est sourcée [S1] ; pas de données cliniques lues.

## 9. Lacunes explicites
- Aucune source suisse de recommandation (SNG/SSN, Swiss Medical Forum, ASSM) n'a pu être lue (quota WebSearch épuisé) : ni pour l'HII, ni pour l'EM/SFC, ni pour le diagnostic de mort cérébrale (directives ASSM).
- ERC-ESICM 2025 (S5) non lue en texte intégral ; valeurs chiffrées issues de la version 2021.
- EAN 2020 sur les troubles de la conscience : résumé seulement ; définitions SÉNR/ÉCM et taux d'erreur diagnostique non lus.
- Critères de Friedman 2013 (figure) non lus ; classification de Frisén de l'œdème papillaire non lue.
- Agonistes du GLP-1 dans l'HII (essais publiés après 2018) non lus.
- Types cliniques d'engagement cérébral (sous-falcoriel, temporal/uncal, amygdalien, triade de Cushing) : aucune source lue → ne pas rédiger de détail sans source.
- Corticoïdes dans l'œdème vasogénique tumoral, sérum salé hypertonique (doses) : non sourcés.
- Syndrome de Reye : critères diagnostiques, biologie (ammoniémie, transaminases), traitement, épidémiologie suisse non lus.
- Encéphalopathie post-radique, kystes porencéphaliques, G93.4 : données cliniques absentes.
- Topiramate FI suisse non lue (HII hors libellé).

## 10. Proposition pour les îlots finaux (à partir des seules sources lues)
- Critères formels : HII — pression d'ouverture > 25 cmH2O adulte / > 28 cmH2O enfant, imagerie excluant une cause secondaire (IRM + veinographie), HII sans œdème papillaire (VI ou ≥ 3/4 signes IRM) [S2] ; pronostic post-anoxique défavorable si ≥ 2 prédicteurs à ≥ 72 h, M ≤ 3, confondants exclus [S4] ; EM/SFC — MPE obligatoire, ≥ 6 mois adulte (IOM 2015), 3 mois chez l'enfant [S6].
- Paramètres clés : PIC seuil 20–22 mmHg [S7] ; mannitol 1–2 g/kg en 30–60 min [S12] ; SpO2 94–98 %, PaCO2 4,5–6,0 kPa, PAM ≥ 65 mmHg, pas de fièvre > 37,7 °C pendant 72 h [S4] ; NSE > 60 µg/L à 48–72 h [S4] ; prévalence kyste arachnoïdien 2,3 % chez les ≥ 70 ans [S10].
