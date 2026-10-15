# G73 — Affections musculaires et neuromusculaires au cours de maladies classées ailleurs (N-05-Neurologie) — dossier de recherche

Cycle Betta 39, leçon 1 (ligne `c39-G73`), agent C39-A3-NEUR (Opus 5.5), 15.10.2026. Chaque fait porte sa référence [Sx] (voir `sources.json`). Rien n'est écrit de mémoire. Quand seule l'analyse (abstract) a été lue, `sources.json` le précise : le rédacteur ne doit rien tirer de plus que ce qui est cité ici. Ce qui n'a pas été lu figure en « Lacunes ».

Contexte de recherche : le quota WebSearch de la session était épuisé (refus explicite de l'outil). La recherche s'est faite par PubMed (métadonnées, et textes intégraux PMC pour [S3] et [S4]), par WebFetch ciblé (BfArM) et par `tools/swissmedic_fi.py` (AIPS via AmiKo). Aucune source suisse de type Swiss Medical Forum ou Société suisse de neurologie n'a pu être atteinte par ces voies (voir Lacunes).

## 0. Question clinique et périmètre
- G73 est une **catégorie « astérisque » (*)** : elle code la manifestation neuromusculaire, tandis que la maladie causale est codée par un code « croix » (†) primaire [S1, S2]. Le cours doit donc être organisé autour de la question : « quelle maladie générale explique cette atteinte de la jonction neuromusculaire ou du muscle ? ».
- Sous-codes (CIM-10-GM 2024, titres OFS en français [S2] ; contenu détaillé BfArM [S1]) :
  - **G73.0*** Syndrome myasthénique au cours de maladies endocriniennes ; inclut l'amyotrophie diabétique (E10–E14†) et l'hyperthyroïdie (E05.-†) [S1].
  - **G73.1*** Syndrome de Lambert-Eaton (primaire C00–D48†) [S1].
  - **G73.2*** Autres syndromes myasthéniques au cours de maladies tumorales (C00–D48†) [S1].
  - **G73.3*** Syndrome myasthénique au cours d'autres maladies classées ailleurs [S1].
  - **G73.4*** Myopathie au cours de maladies infectieuses et parasitaires classées ailleurs [S1].
  - **G73.5*** Myopathie au cours de maladies endocriniennes ; inclut hyperparathyroïdie (E21.0–E21.3†), hypoparathyroïdie (E20.-†), myopathie thyréotoxique (E05.-†) [S1].
  - **G73.6*** Myopathie au cours de maladies métaboliques ; inclut glycogénose (E74.0†) et lipidoses (E75.-†) [S1].
  - **G73.7*** Myopathie au cours d'autres maladies classées ailleurs ; inclut polyarthrite rhumatoïde (M05–M06†), syndrome sec (M35.0†), sclérodermie (M34.8†), lupus érythémateux systémique (M32.1†) [S1].
- La page BfArM lue ne mentionne pas d'exclusion propre à G73 [S1]. Le résumé de l'outil n'a pas restitué tous les inclusions mot pour mot (limite notée dans `sources.json`).
- **Pivot didactique proposé** (choix pédagogique, pas un fait médical) : le syndrome de Lambert-Eaton (G73.1) est l'entité la mieux documentée et la plus testée ; les myopathies endocriniennes, infectieuses et systémiques (G73.4–G73.7) forment la seconde moitié du cours.

## 1. Syndrome myasthénique de Lambert-Eaton (SMLE, G73.1)

### 1.1 Définition et place parmi les syndromes paranéoplasiques
- Maladie auto-immune rare de la jonction neuromusculaire, caractérisée par une faiblesse musculaire proximale, une perte des réflexes ostéotendineux et une dysautonomie [S5].
- Les critères PNS-Care 2021 (panel international, coordination Lyon) classent le SMLE parmi les **« phénotypes à haut risque »** de syndrome neurologique paranéoplasique (anciennement « syndromes classiques ») [S3]. Ces phénotypes doivent faire rechercher un cancer sous-jacent [S3].
- Les syndromes neurologiques paranéoplasiques surviennent chez environ 1 patient cancéreux sur 300 ; l'incidence rapportée varie de 1,6 à 8,9 par million de personnes-années [S3].

### 1.2 Épidémiologie
- Prévalence moyenne d'environ 0,3/100 000 habitants selon une revue néerlandaise actualisée (Radboud) [S11].
- Cohorte de Leiden (70 patients, 1992–2023) : 66 % de femmes, âge médian au diagnostic 54 ans, forme non tumorale (NT-SMLE) 77 % [S8]. (Cohorte de centre tertiaire ; la proportion tumorale varie selon le recrutement.)
- Association à un carcinome bronchique à petites cellules (CBPC) chez 50–60 % des patients [S5] ; environ 60 % selon [S4] ; 51 % (44/87) dans la cohorte prospective Leiden–Nottingham [S4].
- Registre néerlando-belge : autres maladies auto-immunes rapportées chez 38 % des patients SMLE [S14].
- Formes pédiatriques : 19 cas recensés dans la littérature, taux de cancer et de dysautonomie plus bas que chez l'adulte [S27].

### 1.3 Physiologie normale puis mécanisme
- Normal : à la zone active présynaptique, la relation entre canaux calciques voltage-dépendants et vésicules arrimées gouverne la probabilité de libération d'acétylcholine à chaque potentiel d'action [S28].
- Pathologique : des anticorps dirigés contre les **canaux calciques voltage-dépendants de type P/Q (VGCC)** présynaptiques de la terminaison motrice et du système nerveux autonome réduisent la libération d'acétylcholine [S5, S4]. Ces anticorps sont responsables de la baisse de libération de neurotransmetteur provoquée par l'influx nerveux [S4].
- Forme paranéoplasique : on pense que les anticorps dirigés contre les VGCC exprimés à la surface de la tumeur réagissent de manière croisée avec les VGCC présynaptiques [S4]. Le déclencheur de la forme non tumorale est inconnu [S4].
- Des données expérimentales suggèrent aussi une désorganisation de la zone active et d'éventuels anticorps contre d'autres protéines présynaptiques (modèle murin, simulations) [S28] : hypothèse de recherche, pas un fait clinique établi.
- Pharmacologie du mécanisme (pont vers le traitement) : l'amifampridine bloque les canaux potassiques voltage-dépendants, prolonge la dépolarisation présynaptique, augmente l'entrée de calcium et facilite l'exocytose des vésicules d'acétylcholine [S16].

### 1.4 Clinique
- Faiblesse proximale progressive, débutant habituellement aux membres inférieurs, puis membres supérieurs, muscles distaux, enfin muscles oculaires et bulbaires [S3] ; atteinte respiratoire possible dans les formes sévères [S5].
- Dysautonomie chez environ 90 % des patients, marque du SMLE : bouche sèche, dysfonction érectile, constipation [S3].
- Réflexes diminués ou abolis, qui **réapparaissent ou s'améliorent après un effort répété ou une contraction volontaire maximale** (facilitation) [S3].
- Troubles urinaires : données très limitées (une seule étude SMLE dans une revue exploratoire) [S29].

### 1.5 Examens
- **Électrophysiologie obligatoire pour confirmer la suspicion clinique** [S3] : amplitude du potentiel d'action musculaire composé (PAMC) de repos basse aux muscles de la main, avec **incrément** après contraction volontaire maximale [S4] ; décrément et incrément à la stimulation nerveuse répétitive sont très sensibles [S5].
- Seuil d'incrément : à Leiden (156 patients, 63 SMLE), un seuil de 60 % donne une sensibilité de 77,8 % et une spécificité de 98,9 % ; le seuil de 100 % donne 58,7 % et 100 % [S7]. Les auteurs recommandent d'abaisser le seuil à 60 % [S7].
- **Anticorps anti-VGCC P/Q** : présents chez près de 90 % des patients, non indispensables au diagnostic, aussi fréquents dans les formes paranéoplasiques que non paranéoplasiques [S3] ; ils ne distinguent donc pas les deux formes [S3]. La détection se fait par radio-immunoprécipitation ; l'immunohistochimie cérébrale n'est pas utile pour cet anticorps [S3, S4].
- **Anticorps SOX1 (anti-nucléaires gliaux)** : fortement associés au CBPC ; leur présence dans un SMLE suggère fortement un CBPC sous-jacent [S3]. Les line-blots commerciaux ont beaucoup de faux positifs et faux négatifs pour SOX1 [S3].
- Anticorps SOX2 : détectés chez 61 % des SMLE-CBPC ; spécificité > 90 % pour le CBPC [S12].
- Les critères de diagnostic utilisés dans la cohorte prospective : clinique typique (faiblesse proximale, réflexes atténués, dysautonomie) **et** soit électrophysiologie typique (PAMC bas + incrément > 60 %), soit anticorps anti-VGCC P/Q positifs [S4].

### 1.6 Recherche du cancer : score DELTA-P et calendrier
- Le score **DELTA-P** (Dutch-English LEMS Tumour Association Prediction), calculé au diagnostic à partir des signes des trois premiers mois, comporte six items [S4]. Items cités dans [S4] : symptômes bulbaires, dysfonction érectile (homme), perte de poids ≥ 5 %, tabagisme au début, âge de début ≥ 50 ans, indice de Karnofsky. (Seuil exact du Karnofsky non lu : voir Lacunes.)
- Risque de CBPC selon le score dans la cohorte prospective : 0 → 0 % ; 1 → 18,8 % ; 2 → 45 % ; 3 → 55,5 % ; 4 → 85,7 % ; 5 → 87,5 % ; 6 → 100 % ; aire sous la courbe ROC 82,5 % [S4].
- Prédicteurs indépendants en multivarié : perte de poids ≥ 5 %, tabagisme au début, âge ≥ 50 ans [S4]. L'item « dysfonction érectile » est le moins performant ; sans lui, un score à 5 items garde une AUC de 84,5 % [S4].
- Calendrier de dépistage appliqué : TEP-TDM au diagnostic ; si DELTA-P 3–6, répéter à 3 mois puis tous les 6 mois pendant 2 ans ; si DELTA-P 0–1, répéter une fois à 6 mois ; si DELTA-P 2, tous les 6 mois pendant 2 ans [S4].
- Le CBPC est découvert dans les 6 mois chez 91 % et dans les 12 mois chez 98 % des SMLE-CBPC [S4]. Un patient à DELTA-P 1 a eu son CBPC 25 mois après le diagnostic : le score ne s'emploie pas isolément [S4].
- PNS-Care : en cas de dépistage initial négatif, répéter tous les 4–6 mois pendant 2 ans dans les phénotypes à haut risque avec anticorps à haut risque, et dans les phénotypes à haut risque avec anticorps à risque intermédiaire chez les patients âgés, fumeurs ou porteurs d'anticorps concomitants très associés au cancer (par exemple VGCC + SOX1 dans le SMLE) [S3].
- Score PNS-Care, exemple publié pour le SMLE : SMLE + anticorps VGCC sans cancer au diagnostic = 6 (probable) ; CBPC trouvé à 18 mois = 9 (défini) ; pas de cancer après > 2 ans = 5 (possible) [S3]. Le diagnostic « défini » exige la présence d'un cancer [S3].

### 1.7 Diagnostic différentiel
- Les troubles de la jonction neuromusculaire comprennent principalement la myasthénie, le SMLE, le botulisme et l'intoxication aux organophosphorés [S30] ; chez l'enfant s'y ajoutent les syndromes myasthéniques congénitaux, parfois confondus avec une myopathie, une neuropathie ou une dystrophie [S31].
- Le botulisme entre dans le différentiel du SMLE ; en cas de paralysie flasque aiguë avec signes du tronc cérébral, penser au botulisme et notifier les autorités sanitaires [S32].
- Syndromes myasthéniques congénitaux présynaptiques : une partie est appelée « SMLE congénital », par anomalie génétique de la libération vésiculaire [S33].
- Inhibiteurs de points de contrôle immunitaire : des cas de myasthénie et de SMLE sont décrits après leur administration, mais la preuve d'un lien causal reste faible (revue systématique, 94 articles) [S26] ; PNS-Care recommande de rechercher les anticorps neuronaux chez tout patient développant sous ces traitements un tableau évocateur de syndrome paranéoplasique [S3].

### 1.8 Prise en charge
- **Trois piliers** : traitement de la tumeur (le plus important dans la majorité des syndromes paranéoplasiques), immunothérapie, traitement symptomatique [S10b]. Le contrôle des symptômes est obtenu chez la majorité des patients par traitement de la tumeur, traitement symptomatique et immunosuppression [S5].
- **Amifampridine** (3,4-diaminopyridine) : traitement symptomatique de première ligne [S8, S15]. Cochrane : 4 essais contrôlés (54 participants) ; amélioration du score QMG de 2,44 points en moyenne (IC 95 % 1,22–3,6) entre 3 et 8 jours, et du PAMC de 1,36 mV (0,99–1,72) ; qualité de preuve modérée à élevée [S9]. Méta-analyse 2021 de 6 essais (115 patients) : QMG −2,76 points, PAMC +1,34 mV [S34].
- Données de vie réelle (Leiden, 70 patients) : tous ont reçu de l'amifampridine, 91 % dans les 6 mois ; amélioration du « leg score » chez 57 % ; effets indésirables chez 58 % (surtout paresthésies), arrêt rare (7 %) [S8]. Pyridostigmine utilisée chez 81 % ; immunosuppresseurs (prednisolone, azathioprine) chez 44 % à 5 ans ; arrêts fréquents pour effets indésirables (azathioprine 50 %, prednisolone 38 %, pyridostigmine 32 %) [S8].
- L'amifampridine n'est pas efficace en ajout à la pyridostigmine dans la myasthénie à anticorps anti-RACh (essai croisé randomisé, 20 patients) [S15] : elle reste un médicament du SMLE.
- **Immunoglobulines intraveineuses** : un essai croisé (9 participants) montre une amélioration de la force pendant jusqu'à 8 semaines [S9].
- La plupart des NT-SMLE nécessitent une immunosuppression au long cours, habituellement prednisolone et azathioprine ; le rituximab ne repose que sur des cas isolés [S10]. (Revue britannique 2012 ; la cohorte de Leiden 2026 montre une immunosuppression introduite plus progressivement [S8].)
- Les nouveaux biologiques (anti-complément, anti-FcRn, anti-lymphocytes B) ont été testés surtout dans la myasthénie [S13] ; aucune donnée lue ne les valide dans le SMLE.

### 1.9 Pronostic
- NT-SMLE : survie identique à la population générale néerlandaise (65 patients) [S6].
- SMLE-CBPC : survie tumorale plus longue que le CBPC sans SMLE (médiane 17 vs 7,0 mois), même après correction pour le stade [S6].
- Autonomie : 62 % indépendants au diagnostic, 85 % à 1 an ; qualité de vie physique abaissée (55,9 vs 76,3), mentale comparable à la population générale [S6].

## 2. Pharmacologie suisse (information professionnelle Swissmedic)

### 2.1 Firdapse® (amifampridine, DRAC AG) — FI mise à jour janvier 2022 [S16]
- Indication : traitement symptomatique du SMLE chez l'adulte ; instauration par un médecin expérimenté.
- Posologie : 15 mg/j au départ, en 3–4 prises avec les repas ; paliers de 5 mg tous les 4–5 jours jusqu'à 60 mg/j ; dose unique ≤ 20 mg ; exceptionnellement jusqu'à 80 mg/j (paliers de 5 mg tous les 7 jours) sous surveillance clinique et ECG ; 80 mg/j ne doit pas être dépassé.
- Insuffisance rénale ou hépatique modérée/sévère : 5 mg une fois par jour au départ ; légère : 10 mg/j (5 mg × 2) ; paliers de 5 mg tous les 7 jours.
- SMLE paranéoplasique : traiter la tumeur est essentiel.
- Contre-indications : épilepsie ; asthme non contrôlé ; sultopride ; médicaments à marge thérapeutique étroite ; médicaments allongeant le QTc ; QT long congénital ; hypersensibilité.
- Précautions : ECG à l'instauration et pendant la titration, puis annuellement si stable ; crises épileptiques dose-dépendantes (prudence avec antidépresseurs tricycliques, ISRS, neuroleptiques, méfloquine, bupropion, tramadol) ; schwannomes chez le rat (prudence en cas d'antécédent, de neurofibromatose de type 2 ou de schwannomatose) ; acétyleurs lents NAT2 : exposition plus forte et plus d'effets indésirables ; les anticholinergiques réduisent l'effet des deux substances.
- Effets indésirables : très fréquents vertiges, hypoesthésie, paresthésies (périphériques et péribuccales), nausées ; fréquents extrémités froides, douleurs abdominales ; fréquence inconnue convulsions, troubles du rythme, crise d'asthme. Intensité et incidence dose-dépendantes.
- Grossesse : ne pas utiliser ; contraception efficace chez la femme en âge de procréer.
- Cinétique : demi-vie ≈ 2,5 h (métabolite 3-N-acétylé ≈ 4 h) ; 93–100 % excrétés dans l'urine en 24 h ; clairance surtout par N-acétylation.
- Surdosage : vomissements, douleurs abdominales, faiblesse, paresthésies diffuses, convulsions, troubles du rythme.

### 2.2 Mestinon® / Mestinon retard® (pyridostigmine) — FI juin 2020 [S17]
- Indication suisse : atonie intestinale, constipation atonique, myasthénie grave ; le SMLE n'est **pas** une indication de la FI (usage hors indication, documenté à Leiden chez 81 % des patients [S8]).
- Contre-indications : obstruction mécanique digestive ou urinaire ; association aux myorelaxants dépolarisants (suxaméthonium) ; hypersensibilité.
- Prudence : asthme, BPCO, bradycardie, bloc AV, insuffisance cardiaque décompensée, hypotension, ulcère, épilepsie, parkinsonisme, hyperthyroïdie.
- Distinguer crise cholinergique (surdosage : arrêter, soutien respiratoire) et crise myasthénique (renforcer le traitement).
- Demi-vie moyenne ≈ 1,5 h ; élimination rénale inchangée 75–81 %.

## 3. Autres syndromes myasthéniques (G73.0, G73.2, G73.3)
- G73.0 inclut le syndrome myasthénique de l'hyperthyroïdie et de l'amyotrophie diabétique [S1]. Aucune source clinique spécifique n'a été lue (Lacune).
- G73.2 : autres syndromes myasthéniques tumoraux (C00–D48†) [S1]. Un cas de SMLE associé à un carcinome neuroendocrine laryngé est décrit (deuxième cas de la littérature) [S35] ; un adénocarcinome pulmonaire EGFR muté avec SMLE est rapporté [S36] : le CBPC n'est pas la seule tumeur possible.

## 4. Myopathies au cours de maladies générales (G73.4–G73.7)

### 4.1 Myopathies endocriniennes (G73.5)
- **Myopathie thyréotoxique** : fréquente chez l'adulte, elle s'améliore habituellement avec le traitement de l'hyperthyroïdie [S21]. Chez une enfant, faiblesse proximale améliorée en 3 mois avec la normalisation hormonale ; aggravation transitoire au début du traitement (méthimazole + métoprolol) [S21].
- **Paralysie périodique hypokaliémique thyréotoxique** (différentiel aigu, rattachement CIM non vérifié) : épisodes transitoires de faiblesse avec hypokaliémie au cours d'une hyperthyroïdie ; prédominance masculine, surtout asiatique ; mécanisme : hausse de la Na⁺/K⁺-ATPase induite par les hormones thyroïdiennes et sensibilité β-adrénergique accrue, transfert intracellulaire du potassium, aggravé par le pic d'insuline post-prandial ; l'hypokaliémie hyperpolarise la membrane musculaire et la rend inexcitable ; risques : arythmies, insuffisance respiratoire [S20].
- **Myopathie hypothyroïdienne** : peut simuler une myosite. Sous inhibiteur de point de contrôle, la myopathie hypothyroïdienne survient typiquement > 2 mois après le début ; elle se distingue de la myosite immunologique par le délai, la présence de myœdème et le traitement (permet de poursuivre l'immunothérapie) [S22]. Inversement, une myopathie nécrosante auto-immune anti-SRP peut être prise à tort pour une myopathie hypothyroïdienne : CK 6 106 U/L persistantes malgré l'hormonothérapie, biopsie et anticorps spécifiques ont corrigé le diagnostic [S23]. Leçon : une CK qui ne baisse pas sous lévothyroxine impose de chercher une autre cause [S23].
- Une rhabdomyolyse peut accompagner une insuffisance surrénalienne (cas avec revue) [S37] ; l'hypercorticisme (syndrome de Cushing) s'accompagne de myopathie [S38].
- **Myopathie cortisonique** (iatrogène ; rattachement CIM habituel non vérifié, voir Lacunes) : faiblesse proximale **non douloureuse**, amyotrophie prédominant aux membres inférieurs ; CK normales ou peu élevées ; biopsie : atrophie préférentielle des fibres de type II sans infiltrat inflammatoire [S19]. Mécanisme : inhibition de la synthèse protéique (voie mTOR/IGF-1) et activation de la dégradation (ubiquitine-protéasome, autophagie-lysosome) via les facteurs FOXO et les atrogènes MuRF-1 et atrogine-1 [S19]. Conduite : réduction progressive ou arrêt des glucocorticoïdes, rééducation (exercices de résistance et d'endurance) [S19, S18].

### 4.2 Myopathies infectieuses et parasitaires (G73.4)
- **Myosite aiguë bénigne de l'enfant** (série portugaise, 47 cas, 2016–2024) : garçons 66 %, âge médian 7 ans ; prodromes fébriles respiratoires ; douleur bilatérale des mollets ; CK médiane 4 986 U/L ; virus influenza B dans 63 % ; guérison complète de tous, séjour médian 3,2 jours ; aucun cas pendant la pandémie de COVID-19 [S24].
- **Trichinellose** : 65 818 cas et 42 décès rapportés de 1986 à 2009, dont 87 % dans la Région européenne de l'OMS ; viande de porc principale source, gibier fréquent ; principaux signes : myalgies, diarrhée, fièvre, œdème facial, céphalées [S25].

### 4.3 Myopathies métaboliques (G73.6) et des connectivites (G73.7)
- Inclusions CIM lues seulement [S1] (glycogénose E74.0, lipidoses E75.-, polyarthrite rhumatoïde, syndrome sec, sclérodermie, lupus). Aucune source clinique lue (Lacune).

## 5. Critères formels (pour l'îlot final `div.alert`)
- SMLE, critères opérationnels de la cohorte Leiden–Nottingham : faiblesse proximale + réflexes atténués + dysautonomie **et** [PAMC de repos bas avec incrément > 60 % après contraction maximale **ou** anticorps anti-VGCC P/Q] [S4].
- Seuil d'incrément recommandé : 60 % [S7].
- PNS-Care 2021 : SMLE = phénotype à haut risque ; diagnostic défini (score ≥ 8) seulement si cancer présent ; reclassement selon le suivi à 2 ans [S3].

## 6. Paramètres clés (pour `div.key`)
- Prévalence SMLE ≈ 0,3/100 000 [S11] ; CBPC associé 50–60 % [S5] ; anticorps anti-VGCC ≈ 90 % [S3] ; dysautonomie ≈ 90 % [S3].
- Incrément ≥ 60 % : sensibilité 77,8 %, spécificité 98,9 % [S7].
- CBPC découvert ≤ 6 mois chez 91 %, ≤ 12 mois chez 98 % [S4] ; DELTA-P 0 → 0 %, 6 → 100 % [S4].
- Amifampridine : départ 15 mg/j, maximum 60 mg/j (80 mg/j exceptionnellement), dose unique ≤ 20 mg, demi-vie ≈ 2,5 h [S16].
- Survie NT-SMLE normale ; SMLE-CBPC médiane 17 vs 7 mois [S6].
- Myosite aiguë bénigne de l'enfant : CK médiane ≈ 5 000 U/L, influenza B, guérison spontanée [S24].

## 7. Lacunes explicites
1. **Aucune source suisse lue** (Swiss Medical Forum, Société suisse de neurologie, Swiss Neuromuscular Society) : WebSearch indisponible. Aucune recommandation EAN spécifique au SMLE n'a été trouvée par PubMed ; les sources européennes de fond sont Leiden (Pays-Bas), Nottingham (Royaume-Uni) et le panel PNS-Care (Europe, coordination Lyon).
2. Article original du score DELTA-P (Titulaer, 2011) non lu : la pondération exacte et le seuil du Karnofsky ne sont pas documentés ici ; seuls les items et les risques de [S4] sont utilisables.
3. Tableaux 1 à 5 de PNS-Care (listes d'anticorps, grille de points) : non restitués dans le texte intégral lu ; seules les valeurs citées dans le texte sont utilisables [S3].
4. Posologie et schémas des immunoglobulines, de la prednisolone et de l'azathioprine dans le SMLE : non lus. FI Swissmedic des immunoglobulines et de l'azathioprine non consultées.
5. Disponibilité suisse et remboursement (liste des spécialités, OFSP) de Firdapse® : non vérifiés.
6. G73.0, G73.3, G73.6 et G73.7 : aucune source clinique lue en dehors des inclusions CIM.
7. Myopathies endocriniennes : prévalence, CK et électromyographie typiques des myopathies hypo- et hyperthyroïdiennes non sourcées ; hyper- et hypoparathyroïdie non documentées.
8. Codage CIM de la paralysie périodique thyréotoxique et de la myopathie cortisonique non vérifié (relèvent possiblement d'autres catégories que G73) : le rédacteur doit les présenter comme diagnostics différentiels sans leur attribuer de code.
9. Trichinellose : traitement (albendazole, mébendazole) et diagnostic sérologique non lus.
10. Aucune donnée épidémiologique suisse.
