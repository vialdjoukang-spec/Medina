# PLAN — I83 — Varices des membres inférieurs et maladie veineuse chronique

Fragment **C-01-Cardiologie**, vague 9, système « Vaisseaux et microcirculation » (libellé du catalogue : « Angiologie et autres affections circulatoires »).
Architecte : Claude, 7 octobre 2026. Ce plan est la référence commune des quatre rédacteurs et du vérificateur. Un rédacteur qui trouve une erreur dans ce plan ne le modifie pas : il écrit sa réserve dans `brouillon/RESERVES_<onglet>.md`, applique la source primaire et prévient le vérificateur.

Avant d'écrire, chaque rédacteur lit : `TACHE_NOUVEAU_COURS.md`, `CHAPTER_SPEC.md`, `docs/STYLE_REDACTION.md`, `docs/collaboration/FRAGMENT_01_PRIORITE.md`, `travail/justification/CONSIGNES.md`, puis le modèle de forme `chapters/I80/` (structure) et `chapters/I48/` (fenêtres justifiées). **Aucune phrase n'est copiée** d'I80 ni d'un autre cours.

---

## 1. Périmètre CIM et arbitrage

### 1.1 Décision

Le cours **I83** couvre **I83 et I87** ; il traite aussi, dans un îlot dédié, les varices pelviennes et vulvaires **I86.2 et I86.3** lorsqu'elles alimentent des varices des membres inférieurs. Déclaration proposée pour `chapters.json` (à faire par l'orchestrateur) :

```json
{"code": "I83", "covers": ["I83", "I87"], "title": "Varices des membres inférieurs et maladie veineuse chronique", "integrated": true, "wave": 9, "added": "2026-10-07"}
```

### 1.2 Justification

| Catégorie | Sous-codes (catalogue `shell/medina_front.html`) | Décision | Raison |
|---|---|---|---|
| **I83** Varices des membres inférieurs | I83.0 ulcérées ; I83.1 avec inflammation (dermite de stase) ; I83.2 avec ulcère et inflammation ; I83.9 sans ulcère ni inflammation | **Cœur du cours** | Objet principal ; les quatre sous-codes décrivent des stades de la même maladie (classes cliniques CEAP 2 à 6). |
| **I87** Autres atteintes veineuses | I87.0 syndrome post-thrombotique (I87.00 sans, I87.01 avec ulcération) ; I87.1 compression veineuse ; I87.2 insuffisance veineuse chronique (I87.20 sans, I87.21 avec ulcération) ; I87.8 ; I87.9 | **Couvert** | Même mécanisme final (hypertension veineuse ambulatoire), même examen (écho-Doppler debout), même traitement de base (compression), mêmes recommandations (ESVS 2022, chapitres 5 et 6). Séparer I87 produirait un cours redondant. |
| **I86** Varices d'autres localisations | I86.2 pelviennes ; I86.3 vulvaires | **Traité partiellement** (îlot i83-11) | ESVS 2022, chapitre 7 : varices d'origine pelvienne qui alimentent les membres inférieurs. |
| I86 (suite) | I86.0 sublinguales ; I86.1 scrotales (varicocèle) ; I86.4 gastriques ; I86.8 autres (grêliques, coliques, rectales) | **Non couvert** : renvoi | Autres organes, autres mécanismes (hypertension portale, urologie). I86 n'est donc **pas déclaré** dans `covers`. Proposition de renvoi documenté pour l'orchestrateur : « I86 — varices d'autres localisations : I86.2 et I86.3 traitées dans I83 ; I86.1 en urologie ; I86.4 et I86.8 avec l'hypertension portale (hépatologie) ». |

### 1.3 Frontières avec les cours voisins (ne pas recouper)

- **I80 — Thrombose veineuse profonde et thromboses veineuses** (existant, Codex) est propriétaire du **diagnostic et du traitement anticoagulant** de la thrombose veineuse profonde et de la **thrombose veineuse superficielle** (seuils de 5 cm et de 3 cm, fondaparinux, durée). I83 traite la thrombose superficielle **comme complication des varices** : reconnaissance, échographie de tout le membre, absence d'antibiotique et d'intervention aiguë, traitement du reflux au moins trois mois après (ESVS 2021, recommandations 43, 50 et 51). I83 rappelle la décision anticoagulante **en une phrase** et renvoie au cours I80 dans le texte (« voir le cours I80 — Thrombose veineuse profonde et thromboses veineuses »), sans redonner les doses.
- I80 cite le syndrome post-thrombotique comme complication tardive et le score de Villalta. **I83 est propriétaire** du syndrome post-thrombotique constitué (I87.0) : définition, évaluation, compression, obstruction iliaque, désobstruction veineuse. La prévention du syndrome post-thrombotique au moment de la thrombose aiguë (bas après thrombose, essai SOX, thrombolyse, essai ATTRACT) reste dans I80 ; I83 la mentionne sans la développer.
- Le **syndrome de May-Thurner** : I80 le cite comme cause de thrombose ilio-fémorale ; I83 traite la **compression veineuse non thrombotique** (I87.1) et l'obstruction iliaque post-thrombotique comme causes d'hypertension veineuse chronique, et leur traitement endovasculaire.
- **I70 — Artériopathie des membres inférieurs** : propriétaire de l'artériopathie. I83 utilise l'index de pression systolique cheville-bras **seulement comme condition de la compression et diagnostic de l'ulcère mixte**, dans sa propre fenêtre.
- **I89 — Lymphœdème** (futur, Claude) : I83 cite le phlébolymphœdème et le signe de Stemmer dans le diagnostic différentiel de l'œdème, sans développer le lymphœdème.
- **I50 — Insuffisance cardiaque** : cause d'œdème bilatéral et contre-indication relative de la compression (classe NYHA III et IV) ; renvoi.
- **Grossesse** (O22.0, O87.8, exclus d'I83 par la CIM) : I83 traite la conduite pratique des varices de la grossesse dans « Situations particulières », car l'ESVS 2022 la traite (recommandation 93).
- **CIM-11** : correspondance non établie. Ne citer **aucun code CIM-11** dans le cours.

### 1.4 Recommandations ESC 2026

Les recommandations ESC 2026 déjà intégrées au dépôt (insuffisance cardiaque ; maladie cardiovasculaire et rénale chronique ; réadaptation) **ne portent pas** sur la maladie veineuse chronique. **Aucune fenêtre comparative ESC 2026** n'est prévue. Seule incidence : la nouvelle définition de l'insuffisance cardiaque (ESC 2026) intervient dans le diagnostic différentiel de l'œdème ; renvoi au cours I50, sans chiffre. Le site de l'ESVS (consulté le 7 octobre 2026) indique que les recommandations sur les **thromboses veineuses sont en révision** ; l'ESVS 2022 sur la maladie veineuse chronique reste le référentiel en vigueur (aucune mise à jour 2025-2026 trouvée).

---

## 2. En-tête, statut et onglets (texte exact pour le rédacteur A)

```html
<template id="ch-I83"><div class="chap">
<div class="chap-head"><div class="code">I83 · couvre I83 et I87 · CIM-10-GM 2024 · Vaisseaux et microcirculation</div>
<h1>Varices des membres inférieurs et maladie veineuse chronique</h1>
<span class="status">Rédaction du 7.10.2026 · référentiels ESVS 2022 (maladie veineuse chronique des membres inférieurs), ESVS 2021 (thromboses veineuses), annexe 1 de l’OPAS (1.7.2026), LiMA (1.1.2026), informations professionnelles suisses · non validé par une revue humaine</span></div>
<div class="tabs ui" role="tablist">
<button role="tab" aria-controls="pA" data-p="pA" aria-selected="true">⚕ Pathologie et prise en charge</button>
<button role="tab" aria-controls="pE" data-p="pE" aria-selected="false">🔬 Examens complémentaires</button>
<button role="tab" aria-controls="pS" data-p="pS" aria-selected="false">⚛ Sciences fondamentales spécialisées</button>
<button role="tab" aria-controls="pP" data-p="pP" aria-selected="false">💊 Pharmacologie des veinotropes et des sclérosants</button></div>
<div class="panel" id="pA">
```

Puis `nav.toc` (plan des îlots i83-0 à i83-14, liens `<a href="#i83-n">`) et `<div class="chap-body">`. Le fichier **b** se ferme exactement comme `I80_b.html` : `</div><div class="pager ui"><button class="prev">← Îlot précédent</button><span></span><button class="next">Îlot suivant →</button></div></div>`. Le fichier **d** se ferme par `</div><div class="pager ui">…</div></div>` puis `</div></template>`, comme `I80_d.html`.

---

## 3. Cas fil rouge et cas d'entraînement (chiffres communs à tous les onglets)

### 3.1 Cas fil rouge — Mme R., 61 ans

Toutes les valeurs ci-dessous sont **fixées** : aucun rédacteur ne les modifie.

- **Terrain** : aide-soignante en établissement médico-social, debout 8 heures par jour ; trois grossesses ; mère opérée de varices ; IMC 31 kg/m² ; hypertension traitée par **amlodipine 10 mg par jour depuis un an** (piège de l'œdème médicamenteux) ; pas d'antécédent de thrombose ; non fumeuse.
- **Motif** : lourdeur des jambes le soir depuis dix ans, gonflement des chevilles en fin de journée ; depuis six mois, tache brune prurigineuse au-dessus de la malléole interne gauche. Il y a deux ans, « cordon rouge et douloureux » sur une varice de la jambe gauche, traité par une pommade sans échographie.
- **Examen debout** : varices du territoire de la grande saphène gauche (face interne de cuisse et de jambe), diamètre visible > 5 mm ; œdème prenant le godet de la cheville gauche, circonférence de cheville 26 cm à gauche contre 24 cm à droite ; pigmentation brune et eczéma sus-malléolaires internes gauches ; corona phlebectatica sous la malléole interne ; pas d'induration ; pas d'ulcère ; pouls pédieux et tibiaux postérieurs perçus. Membre droit : quelques veines réticulaires.
- **Index de pression systolique cheville-bras** : 1,08 à gauche, 1,10 à droite.
- **Écho-Doppler veineux debout (gauche)** : veines profondes perméables, compressibles, sans reflux ni séquelle post-thrombotique. Reflux de la jonction saphéno-fémorale et de la grande saphène jusqu'à mi-jambe, durée 2,8 s après manœuvre de Valsalva et compression-relâchement du mollet ; diamètre 7,5 mm à 15 cm de la jonction ; collatérale variqueuse de jambe ; perforante jambière incompétente de 4 mm (reflux 0,6 s) sous la zone pigmentée ; petite saphène continente. Ancienne thrombose superficielle : collatérale partiellement recanalisée, sans extension.
- **Classification** (membre gauche) : **C&#8288;2,3,4a,4c S, Ep, As,p, Pr** (à écrire avec le gluon de mots, § 8.3). Classe la plus élevée : C&#8288;4a. VCSS révisé : 8 points (douleur 2, varices de jambe et de cuisse 3, œdème limité à la cheville 1, pigmentation périmalléolaire 1, inflammation périmalléolaire 1, induration 0, ulcères 0, compression 0) — **valeur pédagogique** calculée par l'architecte selon le tableau 5 de l'ESVS 2022 ; le rédacteur A la recalcule et la corrige si nécessaire.
- **Décisions attendues** (îlots 8 à 10 et 14) : l'œdème bilatéral asymétrique fait d'abord rechercher une autre cause (recommandation 16) : l'amlodipine contribue probablement à l'œdème des deux chevilles ; discussion avec le médecin traitant d'un autre antihypertenseur. Compression médicale de classe 2 (23 à 32 mmHg) jusqu'au genou, remboursée par la LiMA (indications C&#8288;1 à C&#8288;6), mesurée et ajustée par un fournisseur ; contrôle de l'index de pression avant. **Traitement interventionnel indiqué** (classes C&#8288;4 à C&#8288;6, recommandation 17) : **ablation thermique endoveineuse** de la grande saphène (recommandation 28), sous anesthésie par tumescence, en ambulatoire, avec phlébectomies ou mousse des collatérales dans le même temps ou ensuite (recommandation 48) ; remboursée par l'assurance obligatoire si le médecin possède l'attestation de formation complémentaire requise (OPAS, annexe 1). La perforante n'est pas traitée d'emblée ; elle est réévaluée après le traitement du tronc. Évaluation individuelle du risque thromboembolique (recommandations 25 et 26). Écho-Doppler de contrôle entre une et quatre semaines (recommandation 27). Activité physique et perte de poids (recommandations 8 et 91). Un veinotrope peut soulager lourdeur et œdème en attendant l'intervention (recommandation 14), sans remplacer ni la compression ni le traitement du reflux.

### 3.2 Cas d'entraînement (quiz et situations particulières ; un seul propriétaire par cas)

| Cas | Données fixées | Propriétaire | Réponse attendue |
|---|---|---|---|
| **E1** M. B., 74 ans, ulcère de la face interne de jambe depuis 4 mois, diabétique | Index cheville-bras 0,55 ; pression de cheville 55 mmHg ; reflux de grande saphène | C (quiz) | Pas de compression soutenue (recommandation 72) ; bilan artériel et revascularisation à discuter (renvoi I70) ; ulcère mixte. |
| **E2** M. B. après revascularisation | Index 0,75 ; pression de cheville 85 mmHg ; pression d'orteil 45 mmHg | C (quiz) | Compression modifiée < 40 mmHg sous surveillance étroite (recommandation 74). |
| **E3** Mme K., 45 ans, ulcère veineux de 3 mois | Index 1,05 ; reflux de grande saphène ; veines profondes normales | B (îlot 11) et C (quiz) | Compression ≥ 40 mmHg et ablation endoveineuse précoce (recommandations 70 et 76 ; essai EVRA). |
| **E4** M. D., 52 ans, thrombose ilio-fémorale gauche il y a 3 ans | Villalta 12 ; claudication veineuse ; obstruction iliaque post-thrombotique | B (îlot 12) | Syndrome post-thrombotique modéré ; compression 20 à 40 mmHg ; discussion multidisciplinaire d'une recanalisation et d'un stent (recommandations 12, 58, 59, 63). |
| **E5** Mme T., 32 ans, 28 semaines de grossesse | Varices vulvaires et de cuisse, lourdeurs | B (îlot 13) | Bas de compression (recommandation 93) ; pas de traitement interventionnel pendant la grossesse ; réévaluation 3 à 6 mois après l'accouchement. |
| **E6** Mme F., 86 ans, sous apixaban | Saignement abondant d'une varice de cheville sous la douche | B (îlot 8) | Surélévation et compression immédiates ; orientation urgente (recommandation 89) ; sclérothérapie à la mousse locale (recommandation 90). |
| **E7** M. L., 58 ans | Cordon rouge de 8 cm sur la grande saphène, à 10 cm de la jonction, varices connues | C (quiz) | Écho-Doppler de tout le membre ; thrombose superficielle ≥ 5 cm à plus de 3 cm de la jonction : anticoagulation selon le cours I80 ; pas d'antibiotique ; ablation du reflux au moins 3 mois après. |
| **E8** Mme P., 39 ans | Télangiectasies de cuisse, demande esthétique | C (quiz) ou D | Écho-Doppler d'abord (recommandation 38) ; traiter d'abord un reflux associé (recommandation 39) ; puis sclérothérapie (recommandation 41) ; prise en charge esthétique non remboursée (à formuler sans chiffre). |

---

## 4. Faits clés sourcés (référence commune)

Règle : un chiffre absent de cette table doit être vérifié par le rédacteur dans une source primaire de `src/` ou sur PubMed, et noté dans `brouillon/SOURCES_<onglet>.md`. Classes et niveaux : voir `src/esvs2022_recommandations.txt` (94 recommandations extraites ; les recommandations mal découpées par l'extraction ont été corrigées à la main sur le texte en colonnes).

### 4.1 Définitions et classifications (ESVS 2022, chapitre 1)

| N° | Fait | Source |
|---|---|---|
| F1 | La maladie veineuse chronique désigne toute anomalie morphologique ou fonctionnelle durable du système veineux qui se manifeste par des symptômes ou des signes justifiant une évaluation ou des soins (consensus VEIN-TERM). Le terme « insuffisance veineuse chronique » est réservé aux formes avancées : classes C&#8288;3 à C&#8288;6. | ESVS 2022, § 1 |
| F2 | CEAP 2020 : classes cliniques C&#8288;0 à C&#8288;6 ; C&#8288;4a pigmentation ou eczéma ; C&#8288;4b lipodermatosclérose ou atrophie blanche ; **C&#8288;4c corona phlebectatica (nouveauté 2020)** ; C&#8288;2r et C&#8288;6r récidive (nouveauté 2020) ; indices S ou A ; étiologie Ep, Es (**Esi intraveineuse**, **Ese extraveineuse**, nouveauté 2020), Ec, En ; anatomie As, Ad, Ap, An ; physiopathologie Pr, Po, Pr,o, Pn ; abréviations anatomiques remplaçant les numéros. Recommandation 1 : CEAP pour l'audit et la recherche (I C). | ESVS 2022 tableau 3 ; Lurie et al. 2020 (PMID 32113854) |
| F3 | Veines réticulaires : 1 à 3 mm ; télangiectasies : ≤ 1 mm. Le seuil de 3 mm des varices « en position debout » vient de la définition CEAP ; **texte intégral de Lurie 2020 non accessible** : si le rédacteur ne le vérifie pas, il écrit « au-delà du calibre des veines réticulaires (1 à 3 mm, ESVS 2022) ». | ESVS 2022 § 4.5 |
| F4 | VCSS révisé : 10 items de 0 à 3 (douleur, varices, œdème, pigmentation, inflammation, induration, nombre, durée et taille des ulcères actifs, compression). La CEAP est descriptive et catégorielle ; elle ne suit pas l'évolution. Recommandation 2 (IIa C) : VCSS révisé et Villalta pour l'audit et la recherche. | ESVS 2022 § 1.5, tableau 5 |
| F5 | Villalta : 5 symptômes et 6 signes cotés 0 à 3 (maximum 33) ; < 5 pas de syndrome post-thrombotique ; 5 à 9 léger ; 10 à 14 modéré ; > 14 ou ulcère : sévère. Spécificité discutée, car ses signes existent aussi sans thrombose antérieure. | ESVS 2022 tableau 6 |
| F6 | Codage : I83.1 « avec inflammation » = **dermite de stase**, et non la thrombose superficielle. Une thrombophlébite sur varice se code **I80.0** (cours I80). I87.21 exclut l'ulcère variqueux (I83.0, I83.2). | Catalogue CIM-10-GM 2024, `shell/medina_front.html` |

### 4.2 Épidémiologie (aucune donnée suisse nationale vérifiée : **lacune à nommer**)

| N° | Fait | Source |
|---|---|---|
| F7 | Prévalences groupées (19 études, non ajustées) : C&#8288;0s 9 %, C&#8288;1 26 %, C&#8288;2 19 %, C&#8288;3 8 %, C&#8288;4 4 %, C&#8288;5 1 %, C&#8288;6 0,42 %. C&#8288;2 la plus fréquente en Europe occidentale (21 % en Europe selon l'ESVS). Forte hétérogénéité. | Salim et al., Ann Surg 2021 (PMID 33214466) ; ESVS 2022 § 1.1 |
| F8 | Facteurs **associés** : sexe féminin (rapport de cotes 2,26), âge, obésité, station debout prolongée, antécédents familiaux, parité. Association, non causalité démontrée pour chacun. | Salim 2021 |
| F9 | Edinburgh Vein Study : 880 sujets suivis 13 ans ; 0,9 % par an développent un reflux ; progression de la maladie chez 57,8 % (4,3 % par an) ; un tiers des varices non compliquées évoluent vers des altérations cutanées ; progression plus fréquente en cas de surpoids ou d'antécédent de thrombose. | ESVS 2022 § 1.1 |
| F10 | Les varices sont un facteur de risque **mineur** de thrombose veineuse profonde ; le caractère causal du lien (hors thrombose superficielle) est **incertain** : facteurs de risque communs possibles. | ESVS 2022 § 1.4.3 |
| F11 | **Ne pas utiliser** la phrase de l'ESVS « 22 % des C&#8288;2 développent un ulcère en six ans » sans vérification dans l'article source : formulation ambiguë. | Réserve de l'architecte |

### 4.3 Physiopathologie (ESVS 2022 § 1.3)

| N° | Fait | Source |
|---|---|---|
| F12 | Pression veineuse d'une veine dorsale du pied : 80 à 90 mmHg debout immobile ; 20 à 30 mmHg pendant la marche (pression veineuse ambulatoire). L'échec de cette baisse définit l'hypertension veineuse ambulatoire, associée surtout au reflux, moins souvent à l'obstruction proximale. | ESVS 2022 § 1.3 |
| F13 | Varices : altérations de la paroi et des valvules (inflammation endothéliale, perte d'élastine et de collagène, fibrose), progression ascendante ou descendante ; le reflux accélère le remplissage et rend la vidange moins efficace. | ESVS 2022 § 1.3 |
| F14 | Peau : l'hypertension veineuse atteint la microcirculation ; capillaires et veinules s'allongent, se dilatent ; dysfonction endothéliale, fuite liquidienne, médiateurs inflammatoires, migration cellulaire, manchons de fibrine, puis fibrose, pigmentation, calcification, ulcère. | ESVS 2022 § 1.3 |
| F15 | Atteinte profonde : souvent post-thrombotique (Esi). Recanalisation → destruction valvulaire → reflux ; recanalisation insuffisante → obstruction. Les deux réunis : évolution plus sévère. Causes extraveineuses (Ese) : compression extrinsèque (iliaque), insuffisance cardiaque droite, pompe musculaire déficiente, obésité. | ESVS 2022 § 1.3 |
| F16 | Obésité : augmentation de la pression intra-abdominale (mécanisme principal) et moindre utilisation de la pompe musculaire. | ESVS 2022 § 8.2.1 |

### 4.4 Clinique et examens (ESVS 2022 §§ 1.4, 2)

| N° | Fait | Source |
|---|---|---|
| F17 | Symptômes : lourdeur, fatigue, sensation de gonflement, prurit, crampes nocturnes, douleurs aggravées par la station debout ou assise prolongée. Ils ne sont pas corrélés à la gravité de l'hypertension veineuse ; ils existent sans signe (C&#8288;0s) et manquent parfois malgré des varices étendues. Fatigue, crampes et jambes sans repos sont **peu spécifiques**. | ESVS 2022 § 1.4.1 |
| F18 | Claudication veineuse : douleur croissante à l'effort par obstruction ilio-fémorale ou cave ; 15 % de 39 patients en ont présenté une au test de marche cinq ans après une thrombose ilio-fémorale. | ESVS 2022 § 1.4.1 |
| F19 | Signes hors CEAP : collatérales sus-pubiennes (obstruction iliaque unilatérale), collatérales abdominales (obstruction cave), varices vulvaires (troubles veineux pelviens). | ESVS 2022 § 1.4.2 |
| F20 | Examen **debout** ; recherche d'autres causes (artérielles, orthopédiques, rhumatologiques, neurologiques) ; mesure des circonférences ; photographies. Le Doppler continu de poche n'a **plus de place** dans le diagnostic du reflux ; il sert à mesurer la pression de cheville. | ESVS 2022 §§ 2.1-2.2 |
| F21 | **Écho-Doppler complet du membre** = examen de première intention (recommandation 3, I B) — examen de référence nommé du cours. Reflux recherché debout, genou légèrement fléchi, provoqué par Valsalva ou compression-relâchement. Seuils : **> 1 s** pour veines fémorale commune, fémorale et poplitée ; **> 0,5 s** pour veines superficielles ; perforantes : flux sortant > 0,35 s (ou > 0,5 s selon d'autres) et diamètre > 3,5 mm. Diamètre de la grande saphène mesuré debout à environ 15 cm de la jonction. Cartographie graphique indispensable avant traitement. | ESVS 2022 § 2.3.1 |
| F22 | Suspicion sus-inguinale : écho-Doppler abdominal (recommandation 4, IIa C) ; rapport de vitesses ≥ 2,5 = meilleur critère d'obstruction iliaque significative par rapport à l'échographie endovasculaire ; phlébo-IRM ou phlébo-TDM si une intervention est envisagée (recommandation 5, I C) ; phlébographie ou échographie endovasculaire si l'imagerie en coupe est insuffisante (recommandation 6, IIb B) ; pléthysmographie à air si discordance (recommandation 7, IIb C). | ESVS 2022 §§ 2.3.2-2.6 |
| F23 | Avant compression : mesure de la pression de cheville et de l'index de pression systolique ; chez le diabétique, pression d'orteil (médiacalcose). | ESVS 2022 § 3.2 |

### 4.5 Traitement conservateur (ESVS 2022 chapitre 3 ; Suisse)

| N° | Fait | Source |
|---|---|---|
| F24 | Exercice (recommandation 8, IIa B) ; conseils : marche, éviter la station debout prolongée et la chaleur, surélévation ; perte de poids si obésité (recommandation 91, IIa C). | ESVS 2022 § 3.1 |
| F25 | Bas élastiques ≥ 15 mmHg à la cheville pour les symptômes (recommandation 9, I B) ; 20 à 40 mmHg pour l'œdème C&#8288;3 (bas, bandages inélastiques ou dispositifs ajustables ; recommandation 10, I B) ; 20 à 40 mmHg pour l'induration C&#8288;4b (recommandation 11, I B) ; 20 à 40 mmHg dans le syndrome post-thrombotique (recommandation 12, IIa B) ; compression pneumatique intermittente d'appoint dans le syndrome post-thrombotique (recommandation 13, IIb B). | ESVS 2022 § 3.2 |
| F26 | La compression ne prévient **pas** de façon démontrée la progression ou la récidive des varices : ne pas la prescrire dans ce seul but. | ESVS 2022 § 3.2.1.1 |
| F27 | **Contre-indications à la compression soutenue** (tableau 7) : artériopathie sévère avec index < 0,6 et/ou pression de cheville < 60 mmHg ; pontage extra-anatomique ou superficiel sous la compression ; insuffisance cardiaque NYHA IV ; NYHA III sans surveillance clinique et hémodynamique ; allergie confirmée au matériau ; neuropathie diabétique sévère avec perte sensitive ou microangiopathie à risque de nécrose (peut ne pas s'appliquer à une compression inélastique modifiée). | ESVS 2022 tableau 7 |
| F28 | **LiMA, chapitre 17 (1.1.2026)** : bas de classe 2 (23 à 32 mmHg) remboursés pour les troubles veineux C&#8288;1 à C&#8288;3, l'insuffisance veineuse chronique C&#8288;3 à C&#8288;6, le lymphœdème de grade 1, la thrombose aiguë, les œdèmes internistes, d'inactivité, post-traumatiques et postopératoires ; classes 3 et 4 (≥ 34 mmHg) remboursées pour C&#8288;3 à C&#8288;6 et la thrombose aiguë ; **au plus deux paires par an** ; remboursement seulement si le fournisseur mesure, essaie, conseille et contrôle les mesures (un bas mesuré par le patient lui-même n'est pas remboursé) ; sur mesure seulement si un bas de série ne convient pas. **Non remboursés** : bas « anti-thrombose » et bas de soutien n'atteignant pas la classe 2, compression pour la performance sportive, la prévention de la thrombose du voyage et la prévention pure pendant la grossesse. Systèmes adaptatifs à velcro (17.06) : C&#8288;3 à C&#8288;5, un jeu par membre et par semestre. | `src/migel_2026-01.txt`, positions 17.02, 17.03, 17.06 |
| F29 | Veinotropes (recommandation 14, IIa A) : symptômes et œdème, chez les patients non opérés, en attente ou avec symptômes résiduels, selon les preuves propres à chaque molécule (tableau 8 de l'ESVS). Coût faible, effets indésirables rares. Ils ne remplacent ni la compression ni le traitement du reflux. | ESVS 2022 § 3.3 |

### 4.6 Traitements interventionnels (ESVS 2022 chapitre 4 ; Suisse)

| N° | Fait | Source |
|---|---|---|
| F30 | Indications : varices symptomatiques C&#8288;2s (recommandation 15, I B) ; altérations cutanées C&#8288;4 à C&#8288;6 (recommandation 17, I C) ; œdème C&#8288;3 : rechercher d'abord une autre cause (recommandation 16, IIa C). Un reflux isolé asymptomatique n'est pas une indication. | ESVS 2022 § 4.1.1 |
| F31 | Grande saphène : **ablation thermique endoveineuse en première intention**, de préférence à la crossectomie-stripping et à la mousse (recommandation 28, I A) ; choix laser ou radiofréquence laissé au médecin (recommandation 29, I B) ; colle cyanoacrylate si une technique non thermique sans tumescence est préférée (recommandation 30, IIa A) ; ablation mécanochimique (recommandation 34, IIb A) ; mousse dirigée par cathéter (recommandation 33, IIb B) ; mousse échoguidée pour troncs < 6 mm (recommandation 31, IIb B) ; crossectomie-stripping si l'ablation thermique n'est pas disponible (recommandation 35, IIa A). Petite saphène : ablation thermique de préférence (recommandation 43, I A) ; attention au nerf sural sous la mi-mollet (recommandation 45, I B). Grande saphène > 12 mm : ablation thermique possible (recommandation 53, IIa C). | ESVS 2022 §§ 4.2, 4.6 |
| F32 | Conditions : ambulatoire si possible (recommandation 18, I C) ; anesthésie par tumescence échoguidée (recommandation 19, I C), solutions tamponnées (recommandation 20, IIa B) ; compression après ablation ou mousse (recommandation 22, IIa A), après stripping ou phlébectomies étendues (recommandation 23, I A), durée individuelle (recommandation 24, I A) ; évaluation du risque thromboembolique (recommandation 25, I C) et prophylaxie individualisée (recommandation 26, IIa B) ; écho-Doppler à 1 à 4 semaines (recommandation 27, IIa C) ; **ne pas interrompre l'anticoagulation** pour une ablation thermique (recommandation 94, III C). | ESVS 2022 §§ 4.1, 8.2.3 |
| F33 | Résultats : ablation laser, succès global 92 % (méta-analyse de 28 essais) ; radiofréquence segmentaire, occlusion 92 % à 5 ans (cohorte de 295 membres) ; reflux récidivant à la jonction à 5 ans plus fréquent après laser qu'après crossectomie-stripping (22 % contre 12 %), mais récidive clinique et VCSS comparables. Mousse : occlusion moindre à long terme (essai CLASS : 64 % laser, 75,9 % chirurgie, 33,3 % mousse à 5 ans). | ESVS 2022 §§ 4.2.1-4.2.3 ; Brittenden 2019 (PMID 31483962) |
| F34 | Complications de l'ablation thermique : EHIT 1,7 % (classes II à IV 1,4 %), thrombose profonde 0,3 %, embolie pulmonaire 0,1 % ; classification EHIT I à IV de l'American Venous Forum ; EHIT IV (thrombus occlusif de la fémorale commune) → anticoagulation curative ; autres : thrombose superficielle, pigmentation, paresthésies (nerf saphène, nerf sural), hématome, brûlure exceptionnelle. | ESVS 2022 § 4.2.1.5, tableau 9 |
| F35 | Collatérales : phlébectomie ambulatoire, mousse échoguidée ou les deux (recommandation 36, I B) ; traitement concomitant à discuter (recommandation 48, IIa B). Perforantes : non traitées dans les varices sans altération cutanée (recommandation 49, III C) ; à discuter si C&#8288;4b à C&#8288;6 avec perforante significative isolée ou résiduelle (recommandation 50, IIb C). CHIVA (recommandation 51, IIb B) et ASVAL (recommandation 52, IIb C). Récidives : ablation ou mousse (recommandation 55, IIa B) ; pas de réintervention chirurgicale du pli de l'aine si une ablation endoveineuse est possible (recommandation 56, III B). | ESVS 2022 §§ 4.3-4.7 |
| F36 | Veines réticulaires : écho-Doppler avant traitement (recommandation 38, I C) ; traiter d'abord un reflux associé (recommandation 39, I C) ; sclérothérapie en première intention (recommandation 40, I A) ; télangiectasies : sclérothérapie (recommandation 41, IIa A) ou laser transcutané (recommandation 42, IIa B). Mousse et liquide d'efficacité comparable pour C&#8288;1 ; troubles visuels plus fréquents avec la mousse. | ESVS 2022 § 4.5 |
| F37 | **OPAS, annexe 1 (édition du 1.7.2026)** : ablation thermique endoveineuse des troncs saphènes par radiofréquence ou laser : **prise en charge obligatoire**, si le médecin possède une formation conforme au programme de formation complémentaire « Ablation thermique endoveineuse des troncs saphènes en cas de varices » (1.1.2016, révisé le 29.9.2016) ; ablation **mécanochimique de type ClariVein : non remboursée** (depuis le 1.7.2013). La colle cyanoacrylate n'est **pas mentionnée** : ne pas affirmer de statut ; écrire que la prise en charge est à clarifier avec l'assureur. | `src/klv_anhang1_2026-07.txt`, lignes 189-197 (copie hébergée par l'Hôpital universitaire de Zurich du texte officiel de l'Office fédéral de la santé publique) |

### 4.7 Ulcère veineux (ESVS 2022 chapitre 6)

| N° | Fait | Source |
|---|---|---|
| F38 | Pas d'antibiotique local ou systémique sans infection (recommandation 67, III B) ; **évaluation artérielle objective** de tout ulcère (recommandation 68, I C) ; index > 0,8 : compression complète possible ; 15 à 20 % des ulcères veineux ont aussi une artériopathie (index < 0,8). | ESVS 2022 §§ 6.2-6.3 |
| F39 | Compression : recommandée (recommandation 69, I A) ; bandages multicouches ou inélastiques ou dispositifs ajustables **≥ 40 mmHg** à la cheville (recommandation 70, I A) ; bas superposés jusqu'à 40 mmHg pour ulcères petits et récents (recommandation 71, IIa B ; corrigendum de la figure 13) ; **pas de compression soutenue** si pression de cheville < 60 mmHg, pression d'orteil < 30 mmHg ou index < 0,6 (recommandation 72, III C) ; compression pneumatique si les autres options échouent (recommandation 73, IIa B) ; ulcère mixte : compression modifiée < 40 mmHg si pression de cheville > 60 mmHg, sous surveillance étroite (recommandation 74, IIb C) ; compression au long cours après cicatrisation (recommandation 75, IIa B). | ESVS 2022 § 6.3 ; corrigendum 2022 |
| F40 | **EVRA** (Gohel, N Engl J Med 2018 ; 450 patients, ulcère de 6 semaines à 6 mois) : ablation endoveineuse dans les 2 semaines + compression contre ablation différée : délai médian de cicatrisation **56 contre 82 jours** ; rapport de risques 1,38 (1,13-1,68) ; cicatrisation à 24 semaines **85,6 % contre 76,3 %** ; temps sans ulcère la première année 306 contre 278 jours. **Piège** : l'ESVS écrit 75,4 % ; retenir la source primaire, 76,3 %. Recommandation 76 (I B). | PMID 29688123 |
| F41 | **ESCHAR** (Gohel, British Medical Journal 2007 ; 500 patients) : chirurgie superficielle + compression contre compression seule : cicatrisation à 3 ans 93 % contre 89 % (non significatif) ; **récidive à 4 ans 31 % contre 56 %**. Recommandation 77 (I A) ; traiter le reflux superficiel même si le réseau profond est incompétent (recommandation 79, I A). | PMID 17545185 |
| F42 | Mousse du plexus sous-ulcéreux (recommandation 78, IIa C) ; perforante proche de l'ulcère (recommandation 80, IIb C) ; stent si obstruction iliaque (recommandation 81, IIa B) ; adjuvants : fraction flavonoïque purifiée micronisée, hydroxyéthylrutosides, pentoxifylline ou sulodexide (recommandation 82, IIa A). | ESVS 2022 § 6.4-6.6 |

### 4.8 Atteinte profonde, pelvis, situations particulières

| N° | Fait | Source |
|---|---|---|
| F43 | Obstruction iliaque avec symptômes sévères : traitement endovasculaire en première intention (recommandation 58, IIa B), guidé par échographie endovasculaire (recommandation 59, IIa C) ; reconstruction chirurgicale ou hybride si échec (recommandation 60, IIb C) ; **aucune intervention sans symptômes sévères** (recommandation 61, III C) ; surveillance échographique à J1, J14 puis régulière (recommandation 62, I C) ; équipe multidisciplinaire (recommandation 63, I C) ; réparation valvulaire profonde en centre spécialisé (recommandation 64, IIb B) ; reflux superficiel et profond combinés : traiter le superficiel (recommandation 65, IIa C) — il corrige le reflux profond segmentaire dans jusqu'à 50 % des cas. | ESVS 2022 chapitre 5 |
| F44 | Pelvis : écho-Doppler des points de fuite pelviens si une origine pelvienne est possible (recommandation 84, I C) ; écho abdominale ou transvaginale (recommandation 85, IIa B) ; sans symptômes pelviens : traitement local d'abord (recommandation 86, IIa C) et **pas d'embolisation pelvienne en première intention** (recommandation 87, III C) ; avec symptômes pelviens : embolisation à considérer (recommandation 88, IIa B) ; exclure les autres causes de douleur pelvienne (recommandation 83, I C). Reflux non saphène dans 10 % de 835 membres, dont un tiers d'origine pelvienne (≈ 3,4 %). | ESVS 2022 chapitre 7 |
| F45 | Hémorragie : peau amincie sur veines réticulaires ou télangiectasies sous hypertension veineuse ; saignement souvent sous une douche chaude ou la nuit chez une personne âgée seule ; peut être fatal ; surélévation et pression externe ; orientation urgente (recommandation 89, I C) ; mousse locale (recommandation 90, IIa C). | ESVS 2022 § 8.1.2 |
| F46 | Grossesse : œdème jusqu'à 80 % des femmes (troisième trimestre) ; bas de compression (recommandation 93, I B) ; pas de traitement interventionnel pendant la grossesse (citation NICE par l'ESVS) ; régression partielle fréquente ; traitement différé de 3 à 6 mois après l'accouchement. Obésité : ablation endoveineuse à considérer (recommandation 92, IIa C) ; résultats moins bons si IMC ≥ 35 mais amélioration dans toutes les catégories. | ESVS 2022 § 8.2 |
| F47 | Thrombose superficielle (ESVS 2021) : environ 25 % des patients de l'étude POST avaient déjà une thrombose profonde ou une embolie au diagnostic ; erreur fréquente : diagnostic d'infection et antibiotiques injustifiés ; écho-Doppler de tout le membre, bilatéral si besoin (recommandation 43, I B) ; pas d'intervention superficielle aiguë (recommandation 50, III C) ; ablation des veines incompétentes **au moins trois mois** après l'épisode (recommandation 51, IIa C). Fondaparinux 2,5 mg **une fois par jour** 45 jours dans CALISTO (l'ESVS 2021 écrit à tort « b.d. » dans son texte). Doses : cours I80. Thrombus court (< 5 cm) d'une collatérale : l'évacuation par ponction soulage vite la douleur (ESVS 2022 § 8.1.1). | ESVS 2021 §§ 2.11 ; PMID 20860504 |

### 4.9 Médicaments disponibles en Suisse (Swissmedic, liste des médicaments autorisés au 30.09.2026 ; informations professionnelles dans `src/fi_*.txt`)

| N° | Fait | Source |
|---|---|---|
| F48 | Autorisés : **Daflon 500** (fraction flavonoïque purifiée micronisée, diosmine et hespéridine ; 2 comprimés par jour, midi et soir, aux repas ; indications : œdème et autres symptômes de l'insuffisance veineuse, maladie hémorroïdaire) ; **Daflon UNO 1000 mg** (1 comprimé à croquer le matin) ; génériques diosmine-hespéridine ; **Doxium** (dobésilate de calcium 500 à 2000 mg par jour ; agranulocytose très rare ; prudence en insuffisance rénale) ; **Venoruton** (oxérutines ; forte 1 comprimé 2 fois par jour ou 1000 mg 1 fois par jour) ; **Antistax forte** (extrait de feuilles de vigne rouge 360 mg par jour, jusqu'à 720 mg, pas plus de 3 mois sans avis) ; **Venostasin** (marronnier d'Inde ; information professionnelle non récupérée : à vérifier) ; sclérosants **Aethoxysklerol** (polidocanol 0,25 à 3 %) et **Sclerovein** (polidocanol 0,5 à 5 %). | `src/swissmedic_ham.xlsx` ; `src/fi_*.txt` |
| F49 | **Non trouvés** dans la liste Swissmedic (recherche par nom de produit) : pentoxifylline, sulodexide, extraits de Ruscus, tétradécylsulfate de sodium. Les recommandations ESVS qui les citent ne sont donc pas directement applicables en Suisse. | `src/swissmedic_ham.xlsx` |
| F50 | Polidocanol (information professionnelle Aethoxysklerol) : **≤ 2 mg/kg de poids corporel par jour** ; injection strictement intraveineuse ; 0,25-0,5 % pour veines réticulaires et télangiectasies, 1 % petites varices, 2-3 % varices moyennes ; une seule injection à la première séance chez un patient prédisposé à l'hypersensibilité ; compression après injection ; marche 30 minutes ; contre-indications : alitement, artériopathie oblitérante, thrombose profonde, infection fébrile, cardiopathie aiguë sévère, mobilité réduite, contre-indication à la compression ; **pas de sclérose au premier trimestre ni après 36 semaines** ; injection intra-artérielle accidentelle : nécrose, conduite décrite. Sclerovein : **foramen ovale perméable symptomatique connu = contre-indication de la mousse** ; troubles visuels transitoires et migraine plus fréquents avec la mousse ; accident vasculaire cérébral très rare. L'information suisse d'Aethoxysklerol ne mentionne pas la forme mousse : vérifier avant d'écrire qu'elle y est autorisée. | `src/fi_aethoxysklerol.txt`, `src/fi_sclerovein.txt` |
| F51 | Anesthésie par tumescence (ESVS 2022 § 4.1.3) : solution type 445 mL de cristalloïde, 50 mL de lidocaïne 1 % avec adrénaline 1:100 000, 5 mL de bicarbonate 8,4 % ; doses de lidocaïne jusqu'à 15 mg/kg associées à peu d'effets indésirables dans ces solutions diluées, toxicité chez 36 % à 35 mg/kg. **Données citées par l'ESVS, non posologie suisse** : les écrire comme telles. | ESVS 2022 § 4.1.3 |

---

## 5. Plan détaillé des quatre onglets

Conventions communes :
- Ids d'îlots : `i83-0` … `i83-14` (onglet 1), `i83-e-1` … `i83-e-6` (Examens), `i83-sa`, `i83-sh`, `i83-sp`, `i83-sb`, `i83-sg` (Sciences, dans `div.sci` d'ids `i83-s-anat`, `i83-s-histo`, `i83-s-physio`, `i83-s-bioch`, `i83-s-gen`), `i83-p-1` … `i83-p-5` (Pharmacologie).
- Chaque îlot : annonce directe du problème médical, développement normal → pathologique → décision, épilogue `div.key` « À retenir. ». Pas de métadiscours.
- Chaque tableau : question avant, lecture après (erreur fréquente, exemple de Mme R. ou d'un cas E).
- Mots verts : `<button class="w" data-k="i83-…">libellé (destination annoncée)</button>`, seulement vers les clés de la § 6.
- Renvois vers un autre cours : en texte, jamais par une clé d'un autre chapitre.
- Volume indicatif (sans objectif) : onglet 1 ≈ 6 000 mots (a ≈ 3 000, b ≈ 3 200), Examens ≈ 1 600, Sciences ≈ 1 500, Pharmacologie ≈ 1 300. Total visé 9 000 à 10 500 mots de texte principal ; fenêtres ≈ 7 000 à 8 000 mots.

### 5.1 Rédacteur A — `brouillon/I83_a.html` (en-tête, onglets, début de pA : îlots 0 à 7)

| Îlot | Titre | Contenu attendu | Mots verts (clés) |
|---|---|---|---|
| `i83-0` | Question clinique et objectifs | Présentation de Mme R. (§ 3.1, partie « Terrain » et « Motif » seulement). Question structurante : s'agit-il d'une maladie veineuse chronique, à quel stade, faut-il un examen, faut-il traiter le reflux, comment, et qu'est-ce que l'assurance rembourse ? Objectifs en phrases complètes. `div.key` Prérequis. | `i83-pav` (pression veineuse ambulatoire) |
| `i83-1` | Définitions, classifications et codage | Maladie veineuse chronique, insuffisance veineuse chronique (F1) ; varices, veines réticulaires, télangiectasies (F3) ; primitive, secondaire, congénitale ; syndrome post-thrombotique ; CEAP 2020 : **tableau** des classes cliniques (F2), lecture du membre de Mme R. ; VCSS et Villalta (F4, F5) ; **tableau de correspondance CIM-10-GM** I83.0/1/2/9, I87.0x/1/2x/8/9, I86.2/3 avec la classe CEAP et le piège I83.1 ≠ thrombophlébite (F6). | `i83-ceap`, `i83-vcss`, `i83-codage` |
| `i83-2` | Épidémiologie et histoire naturelle | F7 à F10 ; **lacune nommée** : aucune donnée suisse nationale vérifiée ; association et causalité distinguées (F8, F10). | `i83-fdr-hered` |
| `i83-3` | Physiopathologie : de la valvule à l'ulcère | Chaîne normal → reflux ou obstruction → hypertension veineuse ambulatoire → microcirculation → peau (F12-F16). **Figure 1 (SVG noir et blanc)** : schéma causal en colonnes « Normal » et « Maladie » : pompe du mollet et valvules continentes → pression du pied 80-90 mmHg debout, 20-30 mmHg à la marche / valvules incompétentes ou obstruction → pression ambulatoire élevée → dilatation capillaire, fuite, inflammation, manchons de fibrine → œdème, pigmentation, lipodermatosclérose, ulcère. Légende « Figure 1 — … Schéma pédagogique. » ; lecture expliquée avant et après. Ne pas dessiner de courbe de pression (réservée à la figure 3 de l'onglet Sciences). | `i83-pav`, `i83-microcirc` |
| `i83-4` | Étiologies et facteurs de risque | Primitives (paroi, valvules, hérédité) ; secondaires intraveineuses (post-thrombotiques) et extraveineuses (compression iliaque, insuffisance cardiaque droite, obésité, immobilité, ankylose de cheville) ; congénitales (Klippel-Trénaunay) ; tableau facteur → mécanisme → force de la preuve (association ou cause). | `i83-fdr-hered`, `i83-fdr-obesite` |
| `i83-5` | Anamnèse | Antécédents cliquables (thrombose, grossesses, chirurgie veineuse, médicaments œdématogènes dont l'amlodipine) ; symptômes par fréquence et spécificité (F17) ; claudication veineuse (F18) ; formes typique et atypiques en `div.two` + `div.card` (varices primitives typiques ; varices atypiques de face postérieure de cuisse ou vulvaires évoquant une origine pelvienne ; varices latérales congénitales ; œdème unilatéral sans varice évoquant une obstruction proximale). | `i83-s-lourdeur`, `i83-s-claud`, `i83-x-oedeme` |
| `i83-6` | Examen clinique | Debout, en deux colonnes : état général et poids → inspection (trajets, C&#8288;1 à C&#8288;6, collatérales sus-pubiennes) → palpation (œdème, induration, pouls) → mesure des circonférences → recherche d'une autre cause. Chaque signe cliquable. Tests manuels historiques (Trendelenburg, Perthes) : citer comme dépassés par l'écho-Doppler, sans les décrire longuement. Mme R. : données d'examen du § 3.1. | `i83-x-debout`, `i83-x-peau`, `i83-x-oedeme` |
| `i83-7` | Démarche diagnostique et diagnostics différentiels | Algorithme en phrases puis petit tableau : clinique debout → écho-Doppler complet (F21, examen de référence) → imagerie proximale si indices (F22) → index de pression avant compression (F23). Différentiels **hiérarchisés par gravité** : thrombose veineuse profonde, ischémie artérielle et ulcère artériel, érysipèle et dermohypodermite, insuffisance cardiaque, rénale, hépatique, œdème médicamenteux, lymphœdème et lipœdème, ulcères d'autre cause (vascularite, pyoderma gangrenosum, carcinome). Résultat de l'écho-Doppler de Mme R. (§ 3.1) et sa CEAP. | `i83-x-oedeme` (réutilisation), et renvoi en texte vers l'onglet Examens |
| — | Fin de A | `<button class="pareto-btn ui" data-k="pareto-i83-bases">▲ Loi de Pareto — Définitions, mécanismes et diagnostic</button>` à la fin de `i83-7` ; un quiz possible dans `i83-7` (cas E8). | — |

### 5.2 Rédacteur B — `brouillon/I83_b.html` (suite de pA : îlots 8 à 14 ; fermeture de pA)

| Îlot | Titre | Contenu attendu | Mots verts (clés) |
|---|---|---|---|
| `i83-8` | Complications aiguës et signes de gravité | **`div.alert` en tête**, gravité d'abord : hémorragie variqueuse (E6, F45) ; thrombose superficielle avec extension profonde ou embolie (F47) ; ulcère infecté, dermohypodermite ; thrombose veineuse profonde (renvoi I80) ; ischémie méconnue sous compression. Puis développement : thrombose superficielle sur varice (ce cours) et articulation avec I80 en une phrase sur le traitement. | `i83-tvs`, `i83-hemorragie` |
| `i83-9` | Prise en charge : objectifs et traitement conservateur | Objectifs (symptômes, œdème, peau, ulcère, récidive) → moyens → choix justifiés → surveillance. Mesures générales (F24), compression (F25-F27) avec **tableau** « situation → pression → dispositif → classe de recommandation », lecture avec Mme R. ; remboursement (F28) ; veinotropes en une phrase (F29), renvoi à l'onglet Pharmacologie. | `i83-compression`, `i83-ci-compression`, `i83-suisse` |
| `i83-10` | Traitements interventionnels : indications et choix | Qui traiter (F30) ; **tableau** des techniques (ablation thermique, colle, mécanochimique, mousse, crossectomie-stripping, phlébectomies, CHIVA et ASVAL) : principe, place ESVS, résultats, statut de remboursement suisse (F31-F37) ; conditions périprocédurales (F32) ; complications (F34) ; décision pour Mme R. | `i83-indication`, `i83-thermique`, `i83-nonthermique`, `i83-chirurgie`, `i83-mousse`, `i83-suisse` |
| `i83-11` | Ulcère veineux | Définition et diagnostic (ulcère de la face interne de cheville, contexte, index obligatoire F38) ; soins locaux ; compression (F39) ; traitement précoce du reflux (F40-F41) ; adjuvants et leur disponibilité en Suisse (F42, F49) ; ulcère mixte ; prévention de la récidive. Cas E3. | `i83-evra`, `i83-ulcere-local`, `i83-ci-compression` |
| `i83-12` | Syndrome post-thrombotique, obstruction iliaque et varices d'origine pelvienne | I87.0 : définition, Villalta, compression (F5, F25) ; I87.1 : compression non thrombotique, May-Thurner, syndrome de la veine cave ; stent (F43) ; I86.2 et I86.3 : points de fuite, embolisation (F44). Cas E4. | `i83-stent`, `i83-pelvien` |
| `i83-13` | Suivi, pronostic, prévention et situations particulières | Suivi (écho-Doppler 1-4 semaines, récidive) ; pronostic (F9) ; prévention (poids, activité, compression **sans** effet préventif démontré sur la progression, F26) ; grossesse (F46, cas E5) ; sujet âgé (enfilage, aides, peau fragile, hémorragie) ; obésité ; patient anticoagulé (F32) ; insuffisance rénale (dobésilate) ; **cas récapitulatif** : Mme R. à 3 mois de l'ablation (évolution décidée par B, cohérente avec F33-F34 ; pas de complication grave). | `i83-grossesse` |
| `i83-14` | Critères formels du diagnostic | **`div.alert`** : critères formels (varices ; insuffisance veineuse chronique C&#8288;3-C&#8288;6 ; reflux superficiel > 0,5 s, profond > 1 s ; perforante pathologique ; ulcère veineux = ulcère de jambe avec hypertension veineuse démontrée et index ≥ 0,8 ou explication de l'ulcère mixte ; syndrome post-thrombotique = Villalta ≥ 5 après thrombose documentée, ou ulcère) ; puis **`div.key`** paramètres clés à surveiller. Puis `pareto-i83-crit` puis `div.src` références principales datées. | — |
| — | Paretos | `pareto-i83-tt` à la fin de `i83-10` (couvre `i83-8,i83-9,i83-10`) ; `pareto-i83-crit` à la fin de `i83-14` (couvre `i83-11,i83-12,i83-13,i83-14`). | — |

Références principales (`div.src`, B) : De Maeseneer M. G. et al. ESVS 2022 (Eur J Vasc Endovasc Surg 2022;63:184-267) et corrigendum (2022;64:284-285) ; Kakkos S. K. et al. ESVS 2021 (Eur J Vasc Endovasc Surg 2021;61:9-82) ; Lurie F. et al. CEAP 2020 (J Vasc Surg Venous Lymphat Disord 2020;8:342-352) ; Salim S. et al. (Ann Surg 2021;274:971-976) ; Gohel M. S. et al. EVRA (N Engl J Med 2018;378:2105-2114) ; Gohel M. S. et al. ESCHAR (British Medical Journal 2007;335:83) ; Brittenden J. et al. CLASS (N Engl J Med 2019;381:912-922) ; Decousus H. et al. CALISTO (N Engl J Med 2010;363:1222-1232) ; annexe 1 de l'OPAS, édition du 1.7.2026 ; LiMA, édition du 1.1.2026 ; informations professionnelles suisses (Swissmedic, consultées le 7.10.2026).

### 5.3 Rédacteur C — `brouillon/I83_c.html` (pE et pS)

**pE — Examens complémentaires** (`nav.toc` puis `div.chap-body`)

| Îlot | Titre | Contenu | Mots verts |
|---|---|---|---|
| `i83-e-1` | Stratégie et hiérarchie | Tableau question → examen → statut (indiqué, conditionnel, non systématique) : écho-Doppler complet debout (**examen de référence**, indiqué) ; index de pression (indiqué avant compression, ulcère) ; pression d'orteil (conditionnel, diabète) ; écho abdominale (conditionnel) ; phlébo-IRM ou TDM, phlébographie, échographie endovasculaire (conditionnels) ; pléthysmographie (non systématique) ; biologie (non systématique). Lecture commentée. | `i83-ips`, `i83-imagerie-prox` |
| `i83-e-2` | A. Écho-Doppler veineux des membres inférieurs | Technique (position, manœuvres), **fiche d'interprétation profonde** : valeurs normales (absence de reflux ou reflux < seuils ; compressibilité), seuils pathologiques (F21), lésions élémentaires (reflux, obstruction, séquelles post-thrombotiques, néovascularisation après chirurgie, recanalisation après ablation), diamètre, cartographie ; pièges (examen couché, provocation insuffisante, reflux physiologique bref, reflux « de passage » d'une collatérale) ; erreur fréquente (prescrire sur la seule clinique). Résultat de Mme R. lu pas à pas. | `i83-duplex-reflux`, `i83-cartographie` |
| `i83-e-3` | B. Évaluation artérielle avant compression | Index de pression systolique, pression de cheville, pression d'orteil, seuils décisionnels (F27, F38, F39) ; médiacalcose ; **tableau** valeurs → décision de compression. | `i83-ips` |
| `i83-e-4` | C. Imagerie proximale et examens de seconde ligne | Écho abdominale et rapport de vitesses ≥ 2,5 ; IRM, TDM, phlébographie, échographie endovasculaire (avantages, irradiation, produit de contraste, indication avant stent) ; pléthysmographie ; pelvis (écho transvaginale). | `i83-imagerie-prox` |
| `i83-e-5` | D. Biologie et examens de l'ulcère | Pas de biologie pour poser le diagnostic de maladie veineuse ; examens **selon la question** : glycémie ou HbA1c (cicatrisation, diabète), hémogramme et CRP si infection clinique (prélèvement bactériologique seulement si infection, F38), bilan de l'œdème bilatéral (créatinine, albumine, NT-proBNP selon la clinique) ; biopsie d'un ulcère atypique ou résistant (chiffres de délai **seulement si vérifiés** dans l'ESVS 2022 § 6.2). Chaque dosage : pourquoi, interprétation, décision. Tableau diagnostics × examens (ulcère veineux, artériel, mixte, neuropathique, vascularite, carcinome). | — |
| `i83-e-6` | Entraînement | **Au moins quatre quiz** : E1, E2, E7, E8 (et E3 au choix). Format `div.quiz ui` ; rétroaction explicative en phrases complètes. Puis `pareto-i83-exam` (couvre `i83-e-1` à `i83-e-5`). | — |

**pS — Sciences fondamentales spécialisées** : `div.sci-bar ui` avec cinq boutons (Anatomie, Histologie, Physiologie, Biochimie et inflammation, Génétique), icônes SVG comme I48, sans abréviation ; puis `div.chap-body sci-body`.

| Discipline (div.sci / îlot) | Question clinique éclairée | Contenu | Figure / mots verts |
|---|---|---|---|
| Anatomie (`i83-s-anat` / `i83-sa`) | Pourquoi la grande saphène est-elle la cible de l'ablation, et où sont les pièges ? | Réseaux superficiel, profond, perforantes ; **compartiment saphène** entre fascias superficiel et musculaire ; jonctions saphéno-fémorale et saphéno-poplitée ; saphène accessoire antérieure ; veine de Giacomini ; nerfs saphène et sural (complications) ; veines pelviennes et points de fuite. **Ne pas répéter** l'anatomie générale d'I80 : centrer sur ce qui guide l'ablation. | **Figure 2 (SVG)** : coupe de cuisse montrant le compartiment saphène entre les deux fascias, et schéma des jonctions ; `i83-saphene` |
| Histologie (`i83-s-histo` / `i83-sh`) | Pourquoi une veine variqueuse ne redevient-elle pas normale ? | Paroi veineuse normale (intima, média pauvre, adventice), valvules ; remodelage variqueux (alternance hypertrophie et atrophie, perte d'élastine, collagène désorganisé, MMP) ; peau : dépôts d'hémosidérine, lipodermatosclérose, atrophie blanche. Corrélations. | `i83-microcirc` (réutilisation de la fenêtre de A) |
| Physiologie (`i83-s-physio` / `i83-sp`) | Pourquoi la marche protège-t-elle, et comment la compression agit-elle ? | Pression hydrostatique, pompe du mollet, pression veineuse ambulatoire et temps de remplissage (F12) ; filtration capillaire selon Starling ; loi de Laplace appliquée au bandage ; élastique contre inélastique (pression de repos et de travail). | **Figure 3 (SVG)** : courbes de pression veineuse du pied au repos, pendant 10 pas et à la récupération : normal, reflux, obstruction (allure qualitative, axes légendés, chiffres limités à F12) ; `i83-laplace`, `i83-pav` |
| Biochimie et inflammation (`i83-s-bioch` / `i83-sb`) | Comment l'hypertension veineuse abîme-t-elle la peau, et comment agissent les traitements ? | Contrainte de cisaillement anormale, activation endothéliale et leucocytaire, MMP, fer et stress oxydatif, manchons de fibrine (hypothèse historique de diffusion de l'oxygène, aujourd'hui discutée : le dire) ; mécanismes des sclérosants détergents (lyse endothéliale) et de l'ablation thermique (dénaturation du collagène, fibrose). | `i83-microcirc` |
| Génétique (`i83-s-gen` / `i83-sg`) | Les varices sont-elles héréditaires, et faut-il un test ? | Agrégation familiale ; formes monogéniques rares (FOXC2 et syndrome lymphœdème-distichiasis ; Klippel-Trénaunay, variants somatiques) ; études d'association pangénomiques : chaque variant explique peu ; **aucun test génétique utile** dans les varices communes. Chiffres seulement si vérifiés sur PubMed. | `i83-gen` |

Chaque discipline se termine par trois encadrés `div.key` de corrélation (science → clinique, science → examen, science → traitement) puis « À retenir ». `pareto-i83-sci` à la fin de la génétique (couvre `i83-sa,i83-sh,i83-sp,i83-sb,i83-sg`).

### 5.4 Rédacteur D — `brouillon/I83_d.html` (pP)

| Îlot | Titre | Contenu | Mots verts |
|---|---|---|---|
| `i83-p-1` | Stratégie médicamenteuse | Ce que les médicaments font et ne font pas (symptômes et œdème ; pas de prévention démontrée de la progression ; ne remplacent pas compression et traitement du reflux) ; classification : veinotropes naturels et synthétiques, sclérosants détergents, anesthésiques de tumescence, antithrombotiques (renvoi I80) ; place selon le phénotype (C&#8288;0s-C&#8288;3 symptomatique ; attente d'intervention ; symptômes résiduels ; ulcère : adjuvant). | `i83-d-mpff`, `i83-d-pentox` |
| `i83-p-2` | Veinotropes disponibles en Suisse : doses et preuves | **Tableau des doses** (F48) : molécule, spécialité suisse, dose initiale et usuelle, durée, effet démontré (tableau 8 de l'ESVS : symptômes et œdème, à reprendre molécule par molécule depuis `src/esvs2022_cvd_flux.txt` § 3.3), source ; tableau introduit et commenté. Statut de remboursement (liste des spécialités) : **non vérifié** par l'architecte ; le vérifier sur la liste des spécialités de l'Office fédéral de la santé publique ou ne rien affirmer. | `i83-d-mpff`, `i83-d-dobesilate`, `i83-d-oxerutines`, `i83-d-vigne` |
| `i83-p-3` | Sclérosants | Polidocanol : formes, concentrations par calibre, dose maximale, technique, mousse et ses contre-indications, grossesse (F50) ; tétradécylsulfate non autorisé en Suisse (F49). | `i83-d-polidocanol` |
| `i83-p-4` | Anesthésie, antithrombotiques et interactions | Tumescence (F51) ; prophylaxie individualisée et anticoagulants poursuivis (F32) ; thrombose superficielle : renvoi I80 pour les doses ; **`div.alert` interactions et sécurité** : anticoagulant + anti-inflammatoire non stéroïdien (saignement) ; dobésilate et agranulocytose (fièvre, angine → hémogramme) ; polidocanol : injection intra-artérielle, anaphylaxie (matériel de réanimation), mousse et foramen ovale perméable ; lidocaïne : toxicité dose-dépendante. | `i83-d-tumescence` |
| `i83-p-5` | Médicaments qui aggravent l'œdème ou gênent la décision | Antagonistes calciques dihydropyridiniques (amlodipine : vasodilatation artériolaire précapillaire → hausse de la pression capillaire → œdème non corrigé par diurétique), autres causes médicamenteuses **seulement si sourcées** (information professionnelle suisse) ; diurétiques : inefficaces sur l'œdème veineux pur et source d'hypovolémie et de troubles électrolytiques chez la personne âgée (formuler comme mécanisme et prudence, sans chiffre non vérifié) ; lien avec Mme R. Puis `pareto-i83-pharma` (couvre `i83-p-1` à `i83-p-5`). | `i83-d-pentox` |

---

## 6. Fenêtres : liste complète (41 fenêtres de contenu + 6 Pareto = 47)

Format de chaque fenêtre de contenu (gabarit commun, modèle I48) :

```html
<template data-pop="i83-…" data-title="Titre en clair, sans abréviation">
<p>Réponse directe en une à trois phrases.</p>
<div class="lab">Mécanisme</div><p>…</p>
<div class="lab">Conséquence clinique</div><p>…</p>
<div class="lab">Limites</div><p>… (association ou causalité ; recommandation ou résultat d'essai)</p>
<div class="lab">Source</div><p>Auteur et al., référence, section ou recommandation (classe, niveau).</p></template>
```

Les intitulés de `div.lab` peuvent varier (« Technique », « Valeur », « Piège », « Décision ») mais la réponse directe vient toujours en premier et la source en dernier. Longueur : **1 200 à 2 500 caractères** pour les fenêtres de signe ou de symptôme, **1 800 à 3 500** pour les fenêtres de décision et les monographies (au plus 4 000). Au plus deux renvois internes `<button class="w" data-k="…">` par fenêtre, vers une clé de cette liste. Pareto : `<template data-pop="pareto-i83-…" data-title="Pareto — …"><p class="ratio" data-cover="ids"></p><ul>…</ul></template>`, contracté, en phrases complètes.

| # | Clé | Titre | Fichier | Onglet propriétaire | Contenu attendu |
|---|---|---|---|---|---|
| 1 | `i83-ceap` | Classification CEAP 2020 : décrire un membre | pop1 | A | Quatre domaines, nouveautés 2020, règle de notation de toutes les classes présentes, exemple de Mme R., limites (descriptive). |
| 2 | `i83-vcss` | VCSS révisé et échelle de Villalta : mesurer la gravité | pop1 | A | Items, usage pour suivre l'évolution, seuils de Villalta, limite de spécificité. |
| 3 | `i83-codage` | Codage CIM-10-GM des varices et de l'insuffisance veineuse | pop1 | A | Correspondance, piège I83.1, I80.0 pour la thrombophlébite, I87.21 contre I83.0, CIM-11 non établie. |
| 4 | `i83-pav` | Pression veineuse ambulatoire : pourquoi la marche abaisse la pression du pied | pop1 | A | F12 ; rôle des valvules et de la pompe ; conséquence clinique (symptômes du soir) ; limites (mesure invasive, peu utilisée). |
| 5 | `i83-microcirc` | Microcirculation et inflammation : de l'hypertension veineuse à la dermite | pop1 | A | F14 ; leucocytes, fer, fibrine ; hypothèses discutées ; conséquence (compression précoce). |
| 6 | `i83-fdr-hered` | Hérédité, âge, sexe et grossesses : association ou cause ? | pop1 | A | F7-F8 ; mécanismes plausibles (hormones, volume, compression utérine) ; limites. |
| 7 | `i83-fdr-obesite` | Obésité et station debout prolongée | pop1 | A | F16 ; pression intra-abdominale ; pompe ; décision (poids, activité, recommandations 91-92). |
| 8 | `i83-s-lourdeur` | Lourdeur, douleur, crampes, prurit : valeur des symptômes veineux | pop1 | A | F17 ; caractérisation (soir, chaleur, soulagement par surélévation) ; non spécificité. |
| 9 | `i83-s-claud` | Claudication veineuse : penser à l'obstruction proximale | pop1 | A | F18 ; différence avec la claudication artérielle ; examen à demander. |
| 10 | `i83-x-debout` | Examen veineux debout : technique et signes | pop1 | A | Position, éclairage, trajets saphènes, palpation, tests historiques dépassés. |
| 11 | `i83-x-peau` | Signes cutanés de l'insuffisance veineuse chronique | pop1 | A | Pigmentation, eczéma, lipodermatosclérose, atrophie blanche, corona phlebectatica ; mécanisme de chacun ; pièges (dermite de contact aux topiques). |
| 12 | `i83-x-oedeme` | Œdème veineux et autres œdèmes des jambes | pop1 | A | Godet, horaire, unilatéralité ; diagnostics différentiels (cardiaque, rénal, hépatique, médicamenteux, lymphœdème et signe de Stemmer, lipœdème) ; amlodipine. |
| 13 | `i83-tvs` | Thrombose veineuse superficielle sur varice | pop2 | B | F47 ; frontière avec I80 ; écho de tout le membre ; pas d'antibiotique ; ablation à 3 mois ; ponction d'un thrombus court. |
| 14 | `i83-hemorragie` | Hémorragie d'une varice : geste immédiat et prévention | pop2 | B | F45 ; surélévation et compression ; orientation ; mousse ; patient âgé, anticoagulé. |
| 15 | `i83-compression` | Compression médicale : pressions, dispositifs et prescription | pop2 | B | F25 ; élastique et inélastique ; mesure ; observance ; prescription (taille, longueur, classe) ; remboursement résumé (renvoi `i83-suisse`). |
| 16 | `i83-ci-compression` | Contre-indications à la compression | pop2 | B | F27, F39 ; mécanisme (pression transmurale et perfusion cutanée) ; compression modifiée. |
| 17 | `i83-indication` | Qui traiter : indications de l'intervention sur le reflux | pop2 | B | F30 ; reflux sans symptômes ; décision partagée. |
| 18 | `i83-thermique` | Ablation thermique endoveineuse : laser et radiofréquence | pop2 | B | Principe, tumescence, résultats (F33), complications et EHIT (F34), essai CLASS. |
| 19 | `i83-nonthermique` | Colle cyanoacrylate et ablation mécanochimique | pop2 | B | Principe, place ESVS (F31), statut suisse (F37), implant permanent et réactions. |
| 20 | `i83-chirurgie` | Crossectomie-stripping, phlébectomies, CHIVA et ASVAL | pop2 | B | F31, F33, F35 ; néovascularisation ; place actuelle. |
| 21 | `i83-mousse` | Sclérothérapie à la mousse échoguidée : technique et place | pop2 | B | Technique, efficacité selon le diamètre (< 6 mm), récidives, ulcère ; **sans** répéter la monographie du polidocanol (fenêtre 37). |
| 22 | `i83-evra` | Essais EVRA et ESCHAR : ce qu'ils prouvent | pop2 | B | F40-F41 ; populations, critères, limites (observance, ulcères < 6 mois). |
| 23 | `i83-ulcere-local` | Soins locaux de l'ulcère veineux | pop2 | B | Nettoyage, détersion, pansement selon l'exsudat, peau périlésionnelle, pas d'antibiotique sans infection (F38), douleur. Chiffres seulement si vérifiés. |
| 24 | `i83-stent` | Obstruction iliaque et stent veineux | pop2 | B | F43 ; May-Thurner non thrombotique et post-thrombotique ; antithrombotiques après stent : seulement si vérifiés dans l'ESVS 2022 chapitre 5. |
| 25 | `i83-pelvien` | Varices d'origine pelvienne | pop2 | B | F44 ; points de fuite ; embolisation ; femme et homme. |
| 26 | `i83-grossesse` | Varices et grossesse | pop2 | B | F46 ; varices vulvaires ; sclérose contre-indiquée au 1er trimestre et après 36 semaines (F50) ; post-partum. |
| 27 | `i83-suisse` | Prise en charge en Suisse : remboursement et filière | pop2 | B | F28, F37 ; formation complémentaire ; bas de classe 1 non remboursés ; ClariVein exclu ; colle non mentionnée ; traitement esthétique ; filière médecin de famille → angiologue ou chirurgien vasculaire. |
| 28 | `i83-duplex-reflux` | Seuils de reflux et manœuvres de provocation | pop3 | C | F21 ; physiologie de la fermeture valvulaire ; pièges. |
| 29 | `i83-cartographie` | Cartographie veineuse avant traitement | pop3 | C | Éléments obligatoires du compte rendu ; exemple de Mme R. |
| 30 | `i83-ips` | Index de pression systolique cheville-bras et pression d'orteil avant compression | pop3 | C | Technique, seuils (F27, F38, F39), médiacalcose, décision. |
| 31 | `i83-imagerie-prox` | Imagerie de l'obstruction proximale | pop3 | C | F22 ; choix selon la question ; irradiation, contraste. |
| 32 | `i83-laplace` | Loi de Laplace et pression sous un bandage | pop3 | C | P = T × n / R (formule expliquée, sans constante non vérifiée) ; conséquence : cheville fine, tibia saillant, rembourrage. |
| 33 | `i83-saphene` | Compartiment saphène et jonctions : repères pour l'échographie et l'ablation | pop3 | C | Image du compartiment, accessoire antérieure, Giacomini, nerfs. |
| 34 | `i83-gen` | Hérédité des varices : ce que l'on sait | pop3 | C | FOXC2, formes syndromiques, études d'association ; pas de test. |
| 35 | `i83-d-mpff` | Fraction flavonoïque purifiée micronisée (diosmine-hespéridine) | pop4 | D | Monographie : mécanisme, preuves (méta-analyse citée par l'ESVS), posologie suisse, effets indésirables, contre-indications, surveillance. |
| 36 | `i83-d-dobesilate` | Dobésilate de calcium | pop4 | D | Monographie ; agranulocytose ; insuffisance rénale. |
| 37 | `i83-d-polidocanol` | Polidocanol | pop4 | D | Monographie du sclérosant (F50). |
| 38 | `i83-d-oxerutines` | Oxérutines (hydroxyéthylrutosides) | pop4 | D | Monographie ; grossesse à partir du 4e mois selon l'information suisse (vérifier dans `fi_venoruton.txt`). |
| 39 | `i83-d-vigne` | Extraits de feuilles de vigne rouge et de marronnier d'Inde | pop4 | D | Phytothérapie : preuves, posologie suisse (Antistax forte ; Venostasin à vérifier), limites. |
| 40 | `i83-d-tumescence` | Anesthésie par tumescence | pop4 | D | F51 ; lidocaïne diluée, adrénaline, bicarbonate ; toxicité ; pourquoi la tumescence protège les tissus. |
| — | `i83-d-pentox` | Pentoxifylline et sulodexide : recommandés par l'ESVS, absents en Suisse | pop4 | D | **41e fenêtre** ; F42, F49 ; mécanismes ; conséquence pratique en Suisse. |
| P1 | `pareto-i83-bases` | Pareto — Définitions, mécanismes et diagnostic | pop1 | A | `data-cover="i83-1,i83-2,i83-3,i83-4,i83-5,i83-6,i83-7"` |
| P2 | `pareto-i83-tt` | Pareto — Complications et traitement | pop2 | B | `data-cover="i83-8,i83-9,i83-10"` |
| P3 | `pareto-i83-crit` | Pareto — Ulcère, atteintes profondes et critères | pop2 | B | `data-cover="i83-11,i83-12,i83-13,i83-14"` |
| P4 | `pareto-i83-exam` | Pareto — Examens | pop3 | C | `data-cover="i83-e-1,i83-e-2,i83-e-3,i83-e-4,i83-e-5"` |
| P5 | `pareto-i83-sci` | Pareto — Sciences fondamentales | pop3 | C | `data-cover="i83-sa,i83-sh,i83-sp,i83-sb,i83-sg"` |
| P6 | `pareto-i83-pharma` | Pareto — Pharmacologie | pop4 | D | `data-cover="i83-p-1,i83-p-2,i83-p-3,i83-p-4,i83-p-5"` |

**Total : 41 fenêtres de contenu et 6 fenêtres Pareto, soit 47 fenêtres.** Répartition : A 12 + 1 Pareto ; B 15 + 2 Pareto ; C 7 + 2 Pareto ; D 7 + 1 Pareto. Aucune réutilisation de fenêtres d'autres cours (I70, I80, I26…) : leurs contenus sont plus courts, appartiennent à d'autres responsables et à d'autres fragments.

Le glossaire `glossary_i83.py` renvoie déjà vers `i83-ceap`, `i83-vcss`, `i83-ips`, `i83-thermique`, `i83-evra`, `i83-chirurgie`, `i83-suisse`, `i83-gen`, `i83-codage` : ces clés doivent exister.

---

## 7. Répartition des fichiers par rédacteur

| Rédacteur | Écrit seulement | Sigles nouveaux éventuels | Ne fait pas |
|---|---|---|---|
| **A** — Pathologie 1 | `brouillon/I83_a.html` ; `brouillon/I83_pop1.html` (12 fenêtres + `pareto-i83-bases`) | `glossary_i83_a.py` | Ne ferme pas `pA` ; ne traite pas la thérapeutique au-delà d'une phrase d'orientation. |
| **B** — Pathologie 2 | `brouillon/I83_b.html` ; `brouillon/I83_pop2.html` (15 fenêtres + `pareto-i83-tt`, `pareto-i83-crit`) | `glossary_i83_b.py` | Ne redonne pas les doses d'anticoagulants (I80) ni les monographies (D) ; ne décrit pas la technique d'écho-Doppler (C). |
| **C** — Examens et Sciences | `brouillon/I83_c.html` ; `brouillon/I83_pop3.html` (7 fenêtres + `pareto-i83-exam`, `pareto-i83-sci`) | `glossary_i83_c.py` | Ne refait pas l'anatomie générale d'I80 ; ne reprend pas la figure 1 de A. |
| **D** — Pharmacologie | `brouillon/I83_d.html` ; `brouillon/I83_pop4.html` (7 fenêtres + `pareto-i83-pharma`) | `glossary_i83_d.py` | Ne décrit pas la technique de la mousse (fenêtre `i83-mousse` de B) ; ne donne pas de dose d'anticoagulant. |
| **Vérificateur** | `verification.json` ; corrections en place dans `brouillon/` ; fusion des glossaires dans `glossary_i83.py` | — | — |

Interfaces à respecter (qui dit quoi) :
- La **décision** de compression et de traitement interventionnel est dans B ; la **mesure** (index, écho-Doppler) dans C ; la **molécule** dans D. Un rédacteur qui touche le domaine d'un autre écrit une phrase et ouvre la fenêtre du propriétaire.
- Les chiffres du § 4 sont repris **à l'identique** ; la formulation est libre.
- Mme R. : A la présente et la classe ; B décide et conclut (cas récapitulatif) ; C interprète ses examens ; D discute l'amlodipine et un éventuel veinotrope. Aucun rédacteur n'ajoute de donnée chiffrée à son dossier sans l'écrire dans `RESERVES_<onglet>.md` pour le vérificateur.

---

## 8. Sigles et glossaire

### 8.1 Glossaire initial (`glossary_i83.py`, vérifié sans collision avec `glossary/`)

CEAP, VCSS, IPS, EHIT, EVRA, ESCHAR, CLASS, CHIVA, ASVAL, LiMA, MiGeL, OPAS, LAMal, MMP, FOXC2, Klippel-Trénaunay, et les codes I83.0, I83.1, I83.2, I83.9, I86.1, I86.2, I86.3, I87.0, I87.00, I87.01, I87.1, I87.2, I87.20, I87.21, I87.8, I87.9.

### 8.2 Sigles déjà au glossaire, utilisables

ESVS, ESC, OFSP, FMH, AOD, HBPM, AINS, IMC, IRM, TDM, CRP, HbA1c, NT-proBNP, NYHA, AVC, CALISTO, SOX, ATTRACT, May-Thurner, Écho-Doppler, CIM-10-GM, CIM-11, NICE, S2k, AWMF, VCAM-1, TNF-α, IL-1, VEGF, TGF-β, MMP-9, NO, O₂, CO₂.

### 8.3 Règle des classes cliniques CEAP (obligatoire)

Les clés C1 à C9 désignent déjà les fractions du complément. Pour que « C3 » n'ouvre pas la définition du complément, **toute classe clinique CEAP s'écrit avec le gluon de mots** : `C&#8288;0`, `C&#8288;1`, `C&#8288;2`, `C&#8288;2r`, `C&#8288;3`, `C&#8288;4a`, `C&#8288;4b`, `C&#8288;4c`, `C&#8288;5`, `C&#8288;6`, `C&#8288;6r`, `C&#8288;0s` (rendu identique à l'écran, contrôlé : `verifier_sigles.py` renvoie `{}`). Cela vaut aussi dans les SVG, les tableaux, les quiz et les fenêtres. Contrôle du vérificateur : `grep -nP '(?<![A-Za-z&#0-9])C[0-6](?![0-9])' brouillon/*.html` ne doit rien renvoyer hors du code CIM. Les indices E, A, P (Ep, Es, Esi, Ese, Ec, En, As, Ad, Ap, An, Pr, Po, Pn) passent sans glossaire.

### 8.4 À écrire en toutes lettres (pas de sigle)

Thrombose veineuse profonde, thrombose veineuse superficielle, maladie veineuse chronique, insuffisance veineuse chronique, grande et petite saphène, jonction saphéno-fémorale, foramen ovale perméable, échographie endovasculaire, ablation thermique endoveineuse, laser endoveineux, radiofréquence, ablation mécanochimique, sclérothérapie à la mousse échoguidée, fraction flavonoïque purifiée micronisée, American Venous Forum, Society for Vascular Surgery, attestation de formation complémentaire, assurance obligatoire des soins, « VCSS révisé » (jamais « r-VCSS »), « British Medical Journal » (jamais « BMJ »), « N Engl J Med » et « Eur J Vasc Endovasc Surg » (pas de majuscules consécutives). Une nouvelle abréviation va dans `glossary_i83_<onglet>.py`, définie lettre à lettre, au format de `glossary/i80.py`.

### 8.5 Contrôle

```bash
cd /home/user/Medina
P="livraisons/Livraison Claude/C-01-Cardiologie/travail/production/I83"
MEDINA_GLOSSAIRE_EXTRA="$P/glossary_i83.py:$P/glossary_i83_a.py" \
  python3 "livraisons/Livraison Claude/C-01-Cardiologie/travail/justification/verifier_sigles.py" I83 "$P/brouillon/I83_a.html" "$P/brouillon/I83_pop1.html"
```

Le résultat doit être `{}`. Un fichier `glossary_i83_<onglet>.py` absent est simplement omis de la variable.

---

## 9. Contrôles avant remise (chaque rédacteur, puis le vérificateur)

1. Sigles : `{}` (§ 8.5) ; classes CEAP avec gluon (§ 8.3).
2. Clés : chaque `data-k` du fichier a son `template data-pop` dans la liste du § 6 ; aucune clé hors de cette liste sans accord du vérificateur.
3. Classes HTML de la liste fermée seulement (`CHAPTER_SPEC.md` § 3) ; ids préfixés `i83-` ; aucun style en ligne ; figures `figure > svg + figcaption`, noir et blanc (`#222`, `font-family="Georgia,serif"`).
4. Paretos : ids de `data-cover` existants dans le même onglet.
5. Phrases complètes, ni infinitif injonctif ni phrase nominale ; tableaux introduits et commentés ; aucun métadiscours.
6. Chaque chiffre : présent au § 4 ou noté avec sa source dans `brouillon/SOURCES_<onglet>.md`.
7. Comptage indicatif : `python3 -c "import re,sys;print(len(re.sub(r'<[^>]+>',' ',open(sys.argv[1]).read()).split()))" fichier`.
8. Le vérificateur assemble `I83_a` à `I83_d` + pops dans un dossier temporaire et lance, si l'orchestrateur l'autorise, `python3 build_medina.py I83` et `python3 test_v7.py I83` sur une copie, jamais dans `chapters/`.

---

## 10. Réserves ouvertes (à lever ou à respecter)

1. **Données suisses** : aucune recommandation nationale suisse spécifique (Société suisse de phlébologie, Société suisse d'angiologie) n'a été trouvée ; aucune donnée épidémiologique suisse nationale vérifiée. Le cours le dit explicitement. L'article d'Ars Medici 2024 (`src/arsmedici_2024_varikose.txt`) est une reprise d'auteurs allemands : ne pas le présenter comme une position suisse.
2. **Liste des spécialités** (remboursement des veinotropes) : non vérifiée. Ne rien affirmer sans consultation.
3. **Colle cyanoacrylate** : non mentionnée dans l'annexe 1 de l'OPAS ; statut de remboursement non établi.
4. **Définition du diamètre des varices (≥ 3 mm debout)** : texte intégral de Lurie 2020 inaccessible ; voir F3.
5. **Venostasin** (marronnier d'Inde) : information professionnelle non récupérée (requête Swissmedic vide) ; vérifier avant toute posologie.
6. **Forme mousse d'Aethoxysklerol** : non mentionnée dans l'information suisse ; Sclerovein la mentionne.
7. **Erreurs de l'ESVS repérées** : EVRA 75,4 % (source primaire : 76,3 %) ; CALISTO « b.d. » (source primaire : une fois par jour). Les signaler dans `verification.json`.
8. **Cohérence avec I80** : I80 (Codex) écrit « ≥ 5 cm et à plus de 3 cm de la jonction » pour le fondaparinux ; l'ESVS 2021 (recommandations 45 et 47) dit « ≥ 5 cm de long et ≥ 3 cm de la jonction ». Écart minime à signaler à Codex, sans modifier I80.
9. **Renvoi I86** à inscrire par l'orchestrateur (§ 1.2) ; `chapters.json` et `RENVOIS` ne sont pas modifiés par les rédacteurs.

---

## 11. Sources téléchargées (`src/`, non versionnées — `.gitignore` : `travail/production/*/src/`)

| Fichier | Contenu |
|---|---|
| `esvs2022_cvd.pdf`, `.txt` (colonnes), `_flux.txt` (ordre de lecture) | De Maeseneer et al., ESVS 2022, maladie veineuse chronique, texte intégral (dépôt ouvert de l'Université de Milan) |
| `esvs2022_corrigendum.pdf`, `.txt` | Corrigendum (figures 6 et 13) |
| `esvs2022_recommandations.txt` | 94 recommandations avec classe et niveau (extraction corrigée) |
| `esvs2021.pdf`, `.txt`, `_flux.txt` | Kakkos et al., ESVS 2021, thromboses veineuses (copie du dossier I80) |
| `klv_anhang1_2026-07.pdf`, `.txt` | Annexe 1 de l'OPAS, édition du 1.7.2026 |
| `migel_2026-01.pdf`, `.txt` | LiMA (MiGeL), édition du 1.1.2026, chapitre 17 |
| `swissmedic_ham.xlsx` | Médicaments autorisés en Suisse, état au 30.09.2026 |
| `fi_aethoxysklerol.txt`, `fi_sclerovein.txt`, `fi_daflon500.txt`, `fi_daflon_uno.txt`, `fi_doxium.txt`, `fi_venoruton.txt`, `fi_antistax_forte.txt` | Informations professionnelles suisses (AIPS, swissmedicinfo.ch, français) |
| `pubmed_verifies.txt` | Résumés PubMed vérifiés : EVRA, ESCHAR, CEAP 2020, Salim 2021, CALISTO, CLASS |
| `arsmedici_2024_varikose.pdf`, `.txt` | Bruning et Gerontopoulou, Ars Medici 2024 (source secondaire) |
