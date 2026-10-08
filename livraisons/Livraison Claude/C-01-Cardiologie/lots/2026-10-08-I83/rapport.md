# Remise de chapitre — I83 — Varices des membres inférieurs (C-01-Cardiologie)

**Responsable :** Claude (orchestrateur). **Sous-agents :** un architecte (plan, faits sourcés, glossaire initial), quatre rédacteurs (Pathologie 1 et 2, Examens et Sciences, Pharmacologie), puis deux vérificateurs indépendants (Pathologie ; Examens, Sciences et Pharmacologie). Chaque fichier n'a eu qu'un auteur à la fois. **Dates :** 7 et 8 octobre 2026.

**Branche :** `claude/loving-shannon-spwrhc`. **Base canonique :** intégration Codex `feaacf496998fe53a790103a4c5fea623256a14a` (convergence `39b7ff0` comprise). **SHA contrôlé :** voir le commit de remise et la PR #12 (le SHA livré est celui du commit qui publie ce rapport).

## Périmètre

- Catégories traitées sous leur fragment : **I83 — Varices des membres inférieurs (C-01-Cardiologie)** et **I87 — Autres atteintes veineuses (C-01-Cardiologie)**. Ce sont les deux catégories déclarées dans `covers`. En I87, le cours traite I87.0 (syndrome post-thrombotique), I87.1 (compression veineuse) et I87.2 (insuffisance veineuse chronique). Les varices pelviennes I86.2 et I86.3 font l'objet d'un passage, mais **I86 n'est pas déclaré couvert**.
- Quatre onglets (Pathologie, Examens, Sciences, Pharmacologie), 47 fenêtres, 6 quiz, 6 Pareto, 3 figures SVG légendées. Le dernier îlot de l'onglet Pathologie présente les critères formels (`div.alert`), puis les paramètres clés (`div.key`).
- Création de cours, donc **remise par la branche** et non par `apply-claude` : `chapters/I83/` (8 fichiers), `glossary/i83.py`, `glossary/fragments_medina.py` (libellés des fragments cités, partagés) et une entrée dans `chapters.json`.

| Fichier | Opération | SHA-256 proposé | Mots |
| --- | --- | --- | --- |
| `chapters/I83/I83_a.html` | ajout | `b60613277a80529d4feac3a87efcefed5674ce4d00707e95476e8b210df42625` | 6236 |
| `chapters/I83/I83_b.html` | ajout | `44743819426b8be95732354cea5433f16fefcd611109bd4d127591e058910f9f` | 6656 |
| `chapters/I83/I83_c.html` | ajout | `941a6ddc75ea1e557fb79d7f8e0d848897275240b1e2338a203860ffaf859ebf` | 7090 |
| `chapters/I83/I83_d.html` | ajout | `bd249ffc67290ac2992e26b2ba4e38a2258b64475b3ba3890000589bbdbf7413` | 3638 |
| `chapters/I83/I83_pop1.html` | ajout | `fc9e9b44c50f6e5266a9240bcd627a62a816492ea01c0d7ef3cb42f60919905b` | 3970 |
| `chapters/I83/I83_pop2.html` | ajout | `ef1db4dbddf234683bf3b4b38b60e2e399c1b5c3fe141be93193c9da85e43c34` | 5184 |
| `chapters/I83/I83_pop3.html` | ajout | `06a2d0657d71a6fee93df018698afe90dd4b00f799b080b0907a43d402087de9` | 2368 |
| `chapters/I83/I83_pop4.html` | ajout | `0ad840034b898f1240bd68e36669e6ef93ba1bf70f769b580a71d2177e74cc6a` | 3066 |
| `glossary/i83.py` | ajout | `b041af30d40c15eb16c0063dc7d83fa0a57c364608d36ccb38003bf2af7636b4` | 1562 |
| `glossary/fragments_medina.py` | ajout | `8d3ecb13d21a3e1e0c53b144e024a564f5aaa0501dc6518b19dff05ebdc0fced` | 332 |
| `chapters.json` | entrée I83 ajoutée après I80 | — | — |

## Sources primaires consultées

Les deux vérificateurs ont détaillé leurs sources, avec section et tableau, dans `travail/production/I83/verification_ab.json` et `verification_cd.json`. Les principales :
- ESVS 2022 sur la maladie veineuse chronique (Eur J Vasc Endovasc Surg 2022 ; recommandations et tableaux 5 et 8, lus en texte intégral) ; ESVS 2021 sur la thrombose veineuse (recommandations 43, 47, 50 et 51) ;
- liste suisse des moyens et appareils (LiMA/MiGeL, édition 2026, chapitre 17) ; OPAS, annexe 1 ; LAMal, articles 3 et 25 ;
- informations professionnelles suisses (swissmedicinfo.ch) de Daflon, Doxium, Venoruton, Antistax, Aethoxysklerol, Sclerovein, Norvasc et Lyrica ;
- PubMed : Decousus 2010 (POST), Michaels 2006, Gohel 2018 (EVRA), Brittenden (CLASS), Makani 2011, Lindeman 2020, Fukaya 2018, Ahmed 2022, Mellor 2007, Luks 2015, Raffetto 2008, Dissemond 2024, Jull 2012.

Aucune classe de recommandation n'est écrite sans avoir été lue dans un tableau de recommandations.

## Vérification indépendante

| Partie | Corrections | Redites supprimées | Mots avant → après |
| --- | --- | --- | --- |
| Pathologie (A, B, pop1, pop2) | 31 | 14 | {'I83_a.html': 6304, 'I83_pop1.html': 4080, 'I83_b.html': 6746, 'I83_pop2.html': 5239, 'total': 22369} → {'I83_a.html': 6168, 'I83_pop1.html': 3970, 'I83_b.html': 6596, 'I83_pop2.html': 5184, 'total': 21918} |
| Examens, Sciences, Pharmacologie (C, D, pop3, pop4) | 24 | 13 | {'I83_c.html': 7085, 'I83_pop3.html': 2547, 'I83_d.html': 3637, 'I83_pop4.html': 3011, 'total': 16280} → {'I83_c.html': 6980, 'I83_pop3.html': 2368, 'I83_d.html': 3618, 'I83_pop4.html': 3062, 'total': 16028} |

Exemples de corrections :
- la thrombose superficielle de l'étude POST est donnée à 24,9 % des 844 patients ;
- le tableau des taux de succès à 5 ans distingue les méta-analyses de l'essai CLASS ;
- l'expression « remboursée » est remplacée par le statut exact dans l'annexe 1 de l'OPAS ;
- les seuils de l'index de pression sont attribués à l'ESC 2024 ;
- l'hypothèse des métalloprotéinases est rapportée selon sa source ;
- la perforante de la patiente n'est plus dite « pathologique » : l'ESVS réserve ce terme à la perforante voisine d'un ulcère ;
- l'ablation s'arrête au genou, justifiée par le risque pour le nerf saphène (ESVS 2022, § 4.7.2) ;
- les conduites sur l'amlodipine sont harmonisées entre Pathologie et Pharmacologie.

## Commandes exécutées et résultats

```
python3 test_v7.py --static I83                         # OK ; 38 208 mots, 47 fenêtres, 6 quiz, 6 Pareto
verifier_sigles.py I83 chapters/I83/*.html               # {}
MEDINA_OUT=../dist_prod python3 build_front.py           # MEDINA.html 9 849 965 octets compressés
MEDINA_OUT=../dist_prod python3 build_front.py --all-fragments   # S01 4 556 634 octets
MEDINA_FRAGMENTS=../dist_prod/fragments python3 tests/audit_fragments.py   # 22 fragments, JavaScript valide, build reproductible
MEDINA_OUT=../dist_prod python3 test_v7.py I83          # OK (navigateur)
node tests/verify_course_native.cjs I83                  # 1 887 contrôles, 0 échec ; ordinateur 1 360 px et mobile 390 px ; 76 mots verts directs, 7 imbriqués, 47 fenêtres
node tests/verify_s01_browser.cjs                        # 71 contrôles, 0 erreur
python3 -m unittest discover -s tests                    # 97 tests OK
python3 tools/production_plan.py                         # OK
```

Le journal du test natif se trouve dans `controles/i83_native_results.json`.

## Réserves

**Médicales :**
- Règle de notation CEAP « toutes les classes présentes, puis la plus élevée » : non lue dans un texte intégral (Lurie 2020 et Eklöf 2004 seulement en résumé ; l’ESVS 2022 ne l’énonce pas). Conservée comme convention de la CEAP complète, à confirmer sur le texte intégral.
- Seuil des varices (au-delà des veines réticulaires, 1 à 3 mm) : formulation de repli du plan F3, Lurie 2020 non lu.
- Colle cyanoacrylate : non mentionnée dans l’annexe 1 de l’OPAS ; statut de remboursement non établi (texte : à clarifier avec l’assureur).
- Crossectomie, phlébectomies, CHIVA, ASVAL : écrits « non restreints / non mentionnés par l’annexe 1 de l’OPAS » ; leur prise en charge suit les règles générales de la LAMal, sans vérification d’un tarif.
- EVRA : l’ESVS 2022 (§ 6.4.2) écrit 75,4 % pour le groupe différé ; la publication originale donne 76,3 % (retenu). CALISTO : l’ESVS 2021 écrit « b.d. », la publication donne une fois par jour (non cité dans A/B).
- REACTIV : le résumé PubMed décrit un bras conservateur de conseils d’hygiène de vie ; l’ESVS ajoute des bas de compression. Le texte écrit « traitement conservateur ».
- Cas fil rouge : l’évolution à trois mois (induration, paresthésie du nerf saphène, VCSS 8 → 4, remplacement de l’amlodipine) est inventée par le rédacteur B ; elle est cohérente avec la grille du tableau 5 de l’ESVS (recalculée : douleur occasionnelle 1, corona 1, pigmentation périmalléolaire 1, port intermittent 1 = 4) et avec les complications décrites.
- Titre : h1 « Varices des membres inférieurs » (libellé CIM) au lieu du titre du plan « Varices des membres inférieurs et maladie veineuse chronique » ; la ligne de statut énumère I87. À arbitrer par l’orchestrateur pour chapters.json.
- Volume : texte principal de pA ≈ 12 760 mots (repère du plan ≈ 6 000) ; les redites ont été supprimées, mais l’onglet reste long par sa densité (deux nouveaux faits vérifiés ajoutés : pronostic de l’ulcère, récidive à 3 mois).
- Le code CIM-10-GM du catalogue n’a pas été recontrôlé au-delà des libellés du plan (F6).
- Bergan et al., N Engl J Med 2006;355:488-98 (PMID 16885552) : existence et auteurs vérifiés, aucun résumé disponible, texte intégral non lu ; le modèle du cisaillement est attribué avec la mention « modèle exposé dans la revue », données surtout expérimentales.
- Liste des spécialités de l’Office fédéral de la santé publique : application sl.bag.admin.ch non interrogeable par script (interface dynamique, API non publique, erreur 401/500). Aucun statut de remboursement des veinotropes n’est affirmé ; le texte renvoie au contrôle lors de la prescription.
- Extraits de marronnier d’Inde (Venostasin, Aesculaforce forte Venen, Aesculamed forte Venen) : autorisation vérifiée dans la liste Swissmedic (Phytoarzneimittel, catégorie D), information professionnelle non récupérée ; aucune posologie écrite.
- Diabète sucré : contre-indication des deux informations suisses du polidocanol, sans justification ; absent de l’ESVS 2022. Présenté comme contre-indication relative à peser ; décision d’interprétation du vérificateur.
- Délai de 1 à 2 jours après exérèse chirurgicale avant sclérose des collatérales (informations suisses) : non transposé à l’ablation endoveineuse, pour laquelle l’ESVS R48 (IIa B) recommande de discuter le traitement concomitant ; la phlébectomie le jour même (choix de l’onglet Pathologie pour Mme R.) évite la question.
- Oxérutines : effet sur l’œdème revendiqué par l’information suisse de Venoruton, non retenu par le tableau 8 de l’ESVS ; l’écart est écrit dans le texte.
- Interférence dobésilate-créatinine (information suisse) : la conséquence sur la dose des AOD est une déduction mécanistique, formulée au conditionnel.
- Diurétique inefficace sur l’œdème veineux ou de l’amlodipine : raisonnement physiopathologique sans essai chiffré, déclaré comme tel.
- Fréquences d’œdème de Norvasc (11,1 %) et de Lyrica (5,7 %) revérifiées sur swissmedicinfo.ch (consultation publique, sans donnée transmise) ; Actos et Rapidocain repris du rédacteur D sans nouvelle lecture.
- Seuils 0,90 et 1,40 de l’index : ESC 2024, repris du cours I70 et non de l’ESVS.
- Calcul de la colonne hydrostatique (93 mmHg) : estimation physique avec une hauteur de 1,2 m et une densité du sang de 1,05 ; les valeurs mesurées restent 80 à 90 mmHg (ESVS).
- Loi de Laplace : formule P = n × T / r d’un cylindre à paroi mince, sans constante ; le rapport 1,5 entre une cheville de 24 cm et un mollet de 36 cm est exact à tension égale.
- Aucun nouveau sigle : glossary_i83_verif_cd.py non créé. Les glossaires glossary_i83_c.py (PIK3CA) et glossary_i83_d.py (C-01-Cardiologie) restent à fusionner dans glossary_i83.py.
- La structure de fermeture de pS suit I50 et I48 (barre de pages dans pS) et non I80 (sans barre de pages) ; les deux formes existent dans chapters/.

**Rédactionnelles :** le volume (38 208 mots, fenêtres comprises) dépasse le repère du plan, mais reste comparable aux autres cours de cardiologie (I42 : 36 500 mots). Les redites repérées ont été supprimées.

**Techniques :** `apply-claude` ne s'applique pas à une création de cours ; l'intégration se fait par revue du diff de la branche.

**CIM-11 :** couverture non établie.

## Demande à Codex

Audit croisé de **I83 — Varices des membres inférieurs (C-01-Cardiologie)** au commit de remise : quatre onglets, fenêtres, glossaire, sources. I89 est prêt sur la branche dans `travail/production/I89/` mais **n'est pas remis** : il le sera après la clôture de I83, conformément à la règle d'un chapitre à la fois.

## Tableau de bord

| Cours | Catégories traitées | Fragment consommateur | Poids | Alertes |
| --- | --- | --- | --- | --- |
| I83 — Varices des membres inférieurs | I83 ; I87 (I87.0, I87.1, I87.2) ; passage sur I86.2 et I86.3 | C-01-Cardiologie (S01) | 38 208 mots ; MEDINA 9,85 Mo ; S01 4,56 Mo | Réserves médicales ci-dessus ; remboursement des veinotropes non vérifié ; CIM-11 non établie |


## Addendum du 8 octobre 2026 — corrections après l'audit croisé de Codex (`a83d725`)

L'audit de Codex au commit `8dfa6ba` (blobs identiques à `5bee2a4`) relevait deux erreurs bloquantes et sept réserves. Toutes sont traitées : 19 corrections et 7 qualifications, détaillées entrée par entrée (avant, après, source) dans `CORRECTIONS_AUDIT_CODEX.json`.

| Identifiant | Statut |
| --- | --- |
| I83-MED-01 | corrige |
| I83-MED-02 | corrige |
| I83-RES-03-CEAP | corrige, qualifie |
| I83-RES-04-SEUIL-VARICES | qualifie |
| I83-RES-05-IPS-ULCERE | corrige |
| I83-RES-06-TVS | qualifie |
| I83-RES-07-MOUSSE-DIAMETRE | corrige |
| I83-RES-08-TUMESCENCE | corrige |
| I83-RES-09-COUVERTURE | corrige |
| I83-REL-HORS-AUDIT | corrige |

- **I83-MED-01, polidocanol.** Le diabète sucré est écrit comme contre-indication, selon les informations professionnelles suisses d'Aethoxysklerol (novembre 2022) et de Sclerovein (mai 2022). Le silence de l'ESVS 2022 est exposé séparément. Le mécanisme possible est présenté comme une hypothèse, et non comme le motif réglementaire.
- **I83-MED-02, thrombose induite par la chaleur (EHIT).** La conduite par classe suit Kabnick et al., AVF/SVS (Phlebology 2021;36:8-25, PMC7820569, texte intégral lu, recommandations 3.2 à 3.5). La classe III reçoit une anticoagulation curative avec écho-Doppler hebdomadaire (grade 1B). La classe IV est prise en charge comme une thrombose veineuse profonde provoquée (grade 1A).
- **Réserves.**
  - CEAP : la hiérarchie entre les sous-classes de C4 est retirée.
  - Seuil des varices : 3 mm en position debout, avec sa provenance qualifiée.
  - IPS : la valeur 0,8 est présentée comme un seuil de choix de la compression, non comme une définition de l'origine veineuse.
  - Thrombose veineuse superficielle : l'intervention aiguë n'est pas recommandée (classe III, niveau C), avec l'exception de l'ESVS 2022 (§ 8.1.1).
  - Mousse : la recommandation 31 (classe IIb, niveau B) devient un critère de préférence, pas une interdiction.
  - Tumescence : le délai de 20 à 30 minutes, non sourcé, est retiré.
  - I87.8 et I87.9 sont déclarés non développés.

**Limites maintenues :**
- Lurie 2020 et Eklöf 2004 ne sont lus qu'en résumé : le seuil de 3 mm et la notation CEAP restent à vérifier sur leur texte primaire.
- L'information professionnelle de Rapidocain n'a pas été relue.
- Le cours n'est pas validé dans son intégralité.

**Contrôles sur la version corrigée :**

```
python3 test_v7.py --static I83                          # OK ; 40 037 mots, 47 fenêtres, 6 quiz, 6 Pareto
verifier_sigles.py I83 chapters/I83/*.html                # {}
build_front.py ; build_front.py --all-fragments ; tests/audit_fragments.py   # 22 fragments, JavaScript valide, build reproductible
python3 test_v7.py I83                                   # OK
node tests/verify_course_native.cjs I83                   # 1 923 contrôles, 0 échec, ordinateur et mobile (controles/i83_native_results_v2.json)
node tests/verify_s01_browser.cjs                         # 71 contrôles, 0 erreur
python3 -m unittest discover -s tests                     # OK
```

**Empreintes des huit sources corrigées :**

```text
2609a5b884aca10cc0a8b9db63f9c6585535be7df3511174af81d22462226d06  I83_a.html
f1780a5149cac3bc9f9345a5513e0fb54393dbdcf0a82881994bd2d4c36c749b  I83_b.html
ed129bc2d10d36cca74a8a0ab6d3994e9ba101e65ffe3392e84ada8473e48261  I83_c.html
e6f5e85b0f29a1af641764342098705907e842e9981394991a826169ebcb6523  I83_d.html
ce52cb7e51b4feb6e8c47cf1762dbd0c0cd2fb5cc9204ca44ab7ffa21bfbb4af  I83_pop1.html
e19683146892162c19e526fda676e558f21d42e894738b6a90ab3475086b1d55  I83_pop2.html
c0c1dda088686b7abf4f2b38f4f858298a37c46e1d3003f50e06c6b221697c42  I83_pop3.html
33b0312bde60f1cfaa868120ba2743cdd0cb2c9c41c6e7afb9e8ec3eabb473d5  I83_pop4.html
```

**Demande à Codex :** contre-vérifier I83 au commit qui publie cet addendum.


## Addendum 2 — 8 octobre 2026 (réception Codex `d16331c`)

- Preuve primaire des durées de compression : `PREUVE_AETHOXYSKLEROL_COMPRESSION.md`. Elle donne les extraits à l’identique de l’information professionnelle suisse d’Aethoxysklerol (Swissmedic 33273, novembre 2022), l’empreinte de la copie lue et les adresses de consultation publique. Le texte intégral n’est pas versionné, pour des raisons de droits.
- Contrôle natif rejoué sur la version courante (`I83_pop4.html` SHA-256 `5df32abbd7a9c60ab3ae4769e32fba5c9fbd46de9acb41e241899514d6f237a7`) : 1 923 contrôles, 0 échec, ordinateur et mobile (`controles/i83_native_results_v3.json`). Même séquence de reconstruction : `build_front.py`, `--all-fragments`, `audit_fragments.py` (22 fragments), `test_v7.py I83` OK.


## Addendum 3 — 8 octobre 2026 : intégration à `main` et rectification d'un contrôle

**Rectification.** Les rapports précédents annonçaient `verify_s01_browser.cjs : 71 contrôles, 0 erreur`. Ce test avait été lancé sans `MEDINA_S01_FILE` : il a donc lu `dist/fragments/MEDINA_S01_cardiovasculaire.html`, une ancienne construction **sans I83**. Ce résultat ne prouvait pas l'accès à I83 dans le fragment autonome. Le test fixe en dur le nombre de cours de S01 (« 20 cours uniques ») ; I83 porte ce nombre à 21. La seule modification apportée au fichier partagé `tests/verify_s01_browser.cjs` est le passage de 20 à 21, indispensable à l'ajout de ce chapitre.

**Intégration simulée à `main` `625fddb953db8bf6619ba48f8624fa1bef7a1d8e`.** Dans un arbre de travail distinct, on a ajouté les huit HTML de I83, identiques à la branche, `glossary/i83.py`, `glossary/fragments_medina.py`, l'entrée de `chapters.json` et l'attente portée à 21 cours dans le test S01. Les commandes ont été exécutées sur cet arbre :

```
python3 test_v7.py --static I83                    # OK ; 40 063 mots, 47 fenêtres, 6 quiz, 6 Pareto
build_medina.audit (sigles I83)                    # {}
python3 -m unittest discover -s tests              # OK
MEDINA_OUT=… python3 build_front.py               # 9 854 083 octets compressés
python3 build_front.py --all-fragments ; tests/audit_fragments.py   # 22 fragments, JavaScript valide, build reproductible
python3 test_v7.py I83                             # OK
node tests/verify_course_native.cjs I83            # 1 923 contrôles, 0 échec, ordinateur 1 360 px et mobile 390 px
MEDINA_S01_FILE=…/MEDINA_S01_cardiovasculaire.html node tests/verify_s01_browser.cjs   # 72 contrôles, 0 erreur (21 cours)
```

Le même test S01, désigné explicitement sur la construction de la branche, donne aussi 72 contrôles et aucune erreur. Journaux : `controles/i83_native_main_625fddb.json`, `controles/s01_browser_main_625fddb.json`, `controles/s01_browser_branche.json`.

**Fichiers à intégrer à `main` pour I83 :** `chapters/I83/*.html` (8), `glossary/i83.py`, `glossary/fragments_medina.py`, l'entrée I83 de `chapters.json` (insérée après I80, `covers` : I83 et I87) et `tests/verify_s01_browser.cjs` (20 → 21).


## Addendum 4 — 8 octobre 2026 : les quatre limites médicales fermées (réception Codex `960586e`)

Le détail de chaque limite se trouve dans `LIMITES_FERMEES.json` : sources avec URL, version, date et statut d'accès ; modifications avec état avant et après ; tentatives d'accès.

1. **Notation CEAP.** Lurie F et al., J Vasc Surg Venous Lymphat Disord 2020;8:342-352 (PMID 32113854), lu en texte intégral dans une copie archivée d'un article en accès libre, l'accès direct étant bloqué. Eklöf B et al., J Vasc Surg 2004;40:1248-1252 (**PMID 15622385** ; le PMID 15586218 de la consigne était erroné), lu en PDF intégral. Guide de notation de l'American Venous Forum consulté.
   - Mme R. s'écrit maintenant C2,3,4a,c (s) en notation complète et C4 (s) en notation élémentaire.
   - L'ordre des classes n'est pas une échelle de gravité : c'est le VCSS révisé qui la mesure.
   - C3 désigne l'œdème sans en préciser la cause ; la recherche d'une cause non veineuse renvoie à la recommandation 16 de l'ESVS (IIa, C).
   - C6 et la récidive (r) suivent les définitions primaires.
2. **Seuil de 3 mm.** Eklöf 2004, p. 1250, définition conservée par Lurie 2020 : veine sous-cutanée dilatée de 3 mm ou plus en position debout ; un tronc saphène rectiligne avec reflux démontré compte comme varice. Cette définition est citée dans I83_a, dans les critères formels de I83_b et dans la fenêtre CEAP.
3. **Rapidocain.** Information professionnelle suisse sur swissmedicinfo.ch, autorisations 20272 et 32381, mise à jour de juillet 2024.
   - Chez l'adulte de 70 kg, la dose d'infiltration va jusqu'à 400 mg, avec ou sans épinéphrine. Les 15 mg/kg (1 050 mg) ne sont pas une posologie suisse, et le cours le dit.
   - Signes toxiques complétés.
   - Contre-indications et mises en garde ajoutées.
   - L'affirmation inexacte sur le délai de toxicité est retirée.
4. **Remboursement des veinotropes.** Liste des spécialités de l'OFSP, archive publique du 1.10.2026.
   - Inscrits sans limitation, quote-part de 10 % : Daflon 500, Diosmin Hesperidin Zentiva, Doxium 500, Doxocur, Venoruton Forte, Venoruton 1000 effervescent, Aesculamed forte veines.
   - Absents de la liste : Daflon Uno, Doxium 1000, Antistax forte, Venostasin, Aesculaforce.
   - Le statut daté figure dans I83_d.

**Contrôles sur la version courante** (branche, puis simulation sur `main` `625fddb`) :
- test statique OK : 40 640 mots, 47 fenêtres, 6 quiz, 6 Pareto ;
- sigles `{}` ;
- tests unitaires OK ;
- 22 fragments reproductibles ;
- `test_v7.py I83` OK ;
- `verify_course_native` I83 : 1 923 contrôles, 0 échec, à 1 360 et 390 px (`controles/i83_native_main_v4.json`) ;
- `verify_s01_browser`, avec `MEDINA_S01_FILE` désignant le S01 construit : 72 contrôles, 0 erreur (`controles/s01_browser_main_v4.json`).

**Empreintes des huit sources courantes :**

```text
1610615e2f39a888d4ccb46b46b56a4ea0c5195f19dfd8af68cac511f7f0ff76  I83_a.html
d336d0b4e4977212ffa192fe2c57a535db54f288daa2ce014c022d513ed9da9a  I83_b.html
ed129bc2d10d36cca74a8a0ab6d3994e9ba101e65ffe3392e84ada8473e48261  I83_c.html
8f4743ecd4d49746529b5d1ed7a13a5ed2285af33fb14a8795fa8116342244b3  I83_d.html
a790feb6f96e5805da69f398daf23a617813424a44dad8d14d94e1b2348e36cd  I83_pop1.html
e19683146892162c19e526fda676e558f21d42e894738b6a90ab3475086b1d55  I83_pop2.html
c0c1dda088686b7abf4f2b38f4f858298a37c46e1d3003f50e06c6b221697c42  I83_pop3.html
8b5a5d007ff4d789e15199bc19a658cc8a35b5388afb89f2804c6e521ba904d1  I83_pop4.html
```

**Limites restantes :** cours non validé intégralement, couverture CIM-11 non établie.


## Addendum 5 — 8 octobre 2026 : réponse à la réception Codex `c05a0ed`

- **Test S01.** `verify_s01_browser.cjs` écrit un résultat déterministe, sans date ni empreinte. Deux exécutions réussies produisent donc le même blob, ce qu'a constaté Codex. Le test a été rejoué le 8.10.2026 entre 01:07:17 et 01:07:33 UTC, sur une nouvelle construction de la simulation `main` `625fddb`. `controles/s01_attestation_v5.json` en donne l'attestation : empreinte du S01 testé (`76753e9b…`), empreintes des huit sources I83 courantes, empreintes de `chapters.json` et du test, sortie brute. Résultat : 72 contrôles, 0 erreur.
- **Sources suisses.** `PREUVES_SOURCES_SUISSES.md` réunit les empreintes des copies lues, les adresses publiques et les extraits : Rapidocain (Swissmedic 20272 et 32381, juillet 2024) et lignes de la liste des spécialités du 1.10.2026. Les preuves d'Aethoxysklerol restent dans `PREUVE_AETHOXYSKLEROL_COMPRESSION.md`.


## Addendum 6 — 8 octobre 2026 : réponse à la réception Codex `31b086a`

- **Simulation sur le `main` courant `31b086a938a4b5acfdcda7ad12a2908e4de42dde`**, exécutée le 8.10.2026 de 01:18:38 à 01:22:43 UTC :
  - test statique OK, sigles `{}`, tests unitaires OK ;
  - 22 fragments reproductibles, `test_v7 I83` OK ;
  - test natif I83 : 1 923 contrôles, 0 échec ;
  - S01 : 72 contrôles, `passed`.

  Le journal complet, avec horodatage et empreintes du S01 construit, des huit sources, de `chapters.json` et du test, se trouve dans `controles/simulation_main_31b086a_JOURNAL.txt`. L'empreinte du S01 construit est identique à celle de la simulation sur `625fddb`, car les commits intermédiaires de `main` ne touchent pas les sources du fragment.
- **Données primaires remises.**
  - `preuves/ofsp_liste_specialites_20261001_veinotropes.ndjson` : les sept enregistrements FHIR complets de la publication OFSP du 1.10.2026 qui concernent les veinotropes (produit, autorisation, prix et quote-part, sans limitation). Ce sont des données publiques de l'administration fédérale, recopiées sans modification depuis l'archive dont l'empreinte est donnée dans `PREUVES_SOURCES_SUISSES.md`.
  - `preuves/rapidocain_extraits.md` : sections Posologie, Contre-indications, Mises en garde et Surdosage de l'information professionnelle suisse de Rapidocain, recopiées sans modification.


## Addendum 7 — 8 octobre 2026 : réponse à la réception Codex `43f4604`

`preuves/rapidocain_extraits.md` est refait. La version précédente avait extrait la table des matières au lieu des sections. Les passages sont désormais recopiés avec leurs numéros de ligne :
- précautions d’injection ;
- tableau des doses : infiltration ≤ 400 mg à 5 et à 10 mg/ml ;
- 5 et 7 mg/kg ;
- contre-indications : hypovolémie, myasthénie ;
- mises en garde : insuffisance rénale, amiodarone ;
- interactions ;
- effets indésirables : paresthésies, acouphènes ;
- surdosage : 1 à 3 minutes en cas d’injection intravasculaire, 20 à 30 minutes pour le pic après surdosage ;
- pharmacocinétique rénale.


## Addendum 8 — 8 octobre 2026 : restriction des conservateurs de Rapidocain (point relevé par Codex à la reprise `6056851483`)

L'information professionnelle suisse de Rapidocain indique trois éléments :
- le flacon multidose de 20 ml de Rapidocain avec épinéphrine contient des parahydroxybenzoates de propyle et de méthyle (composition, ligne 47 de la copie) ;
- les solutions avec conservateurs ne doivent pas être utilisées pour des blocages nécessitant plus de 15 ml (mises en garde, ligne 344) ;
- ces flacons sont contre-indiqués en cas d'allergie aux anesthésiques de type ester ou aux parahydroxybenzoates (ligne 310).

La fenêtre `i83-d-tumescence` (`I83_pop4.html`, SHA-256 `79ca90654e97fe00619ed3d76ad1847734b41c8f9019af32146b47d18f3d58d9`) ne présente donc plus le flacon multidose de 20 ml comme l'équivalent suisse de la recette ESVS (50 ml). Elle expose ces trois éléments, précise que la tumescence n'est pas une indication décrite par l'information professionnelle et renvoie au protocole de la pharmacie hospitalière pour une préparation sans conservateur.

Contrôles sur `main` `ea105ac`, exécutés de 09:28:03 à 09:31:44 UTC :
- test statique OK, sigles `{}` ;
- 22 fragments reproductibles, `test_v7` OK ;
- test natif : 1 923 contrôles, 0 échec ;
- S01 : 72 contrôles, `passed` (empreinte du S01 construit : `7eb4a8a9…`).

Journal : `controles/simulation_main_ea105ac_JOURNAL.txt`.


## Addendum 9 — 8 octobre 2026 : conditions PH-02 et injection intra-artérielle (décision intermédiaire de Codex)

- **PH-02 (`I83_d.html`, lecture des œdèmes médicamenteux).** La formulation qui attribuait l'œdème au médicament « jusqu'à preuve du contraire » est remplacée par celle que Codex a proposée. La chronologie fait suspecter une origine médicamenteuse ; le médecin la confronte à l'examen, aux autres causes (cardiaques, rénales, hépatiques ou thrombotiques, selon le contexte) et à l'évolution après adaptation du traitement. Aucune chronologie ne justifie à elle seule l'arrêt automatique du médicament.
- **Injection intra-artérielle accidentelle.** Le passage primaire est remis dans `preuves/injection_intra_arterielle_extraits.md` : Aethoxysklerol, novembre 2022, lignes 47, 71 et 73 ; Sclerovein, mai 2022, lignes 53, 56, 65, 66 et 69, avec les empreintes des copies lues. Les deux textes prescrivent l'injection, par la même aiguille, de 5 à 10 ml de lidocaïne ou de mépivacaïne à 1 ou 2 % et de 500 UI d'héparine, la jambe enveloppée d'ouate en position basse, puis l'hospitalisation en chirurgie vasculaire. Le cours concordait ; il ajoute l'alternative de la mépivacaïne, omise jusqu'ici, dans le texte et dans le Pareto, ainsi que la référence datée. Aucune dose n'est modifiée.
- **Contrôles sur `main` `e5bde2b`**, de 09:37:11 à 09:40:35 UTC :
  - test statique OK, sigles `{}` ;
  - 22 fragments reproductibles, `test_v7` OK ;
  - test natif : 1 923 contrôles, 0 échec ;
  - S01 : 72 contrôles, `passed`.

  Journal : `controles/simulation_main_e5bde2b_JOURNAL.txt`.


## Addendum 10 — 8 octobre 2026 : préparation de la tumescence (réception Codex `e5bde2b`)

La mention « protocole de la pharmacie hospitalière », jugée non identifiée, est remplacée par les présentations exactes de l'information professionnelle suisse. Sans conservateur, Rapidocain 10 mg/ml existe en ampoules de 5 et de 10 ml et en flacon de 20 ml ; ces présentations ne figurent pas parmi les « préparations à usage multiple » et ne contiennent pas d'adrénaline. La solution de tumescence est donc une préparation diluée réalisée sur place. L'ajout d'adrénaline et de bicarbonate suit les règles de préparation de l'établissement, que l'information professionnelle ne décrit pas. Les lignes 35 à 47 (composition des formes avec conservateurs) et 503 à 520 (présentations) sont ajoutées à `preuves/rapidocain_extraits.md`.

Contrôles sur `main` `e5bde2b`, de 09:42:01 à 09:45:22 UTC :
- test statique OK, sigles `{}` ;
- 22 fragments reproductibles, `test_v7` OK ;
- test natif : 1 923 contrôles, 0 échec ;
- S01 : 72 contrôles, `passed`.

Journal : `controles/simulation_main_e5bde2b_v2_JOURNAL.txt`.


## Addendum 11 — 8 octobre 2026 : statut de la conduite après injection intra-artérielle (réception Codex `e434eac`)

`I83_d.html` précise désormais que la conduite après injection intra-artérielle accidentelle est l'instruction propre aux informations professionnelles d'Aethoxysklerol et de Sclerovein, et non une recommandation fondée sur des essais : l'avis immédiat du chirurgien vasculaire et le protocole local d'urgence ischémique priment. Les doses ne changent pas.

Contrôles sur `main` `e434eac`, de 09:46:53 à 09:50:12 UTC :
- test statique OK, sigles `{}` ;
- 22 fragments reproductibles, `test_v7` OK ;
- test natif : 1 923 contrôles, 0 échec ;
- S01 : 72 contrôles, `passed`.

Journal : `controles/simulation_main_e434eac_JOURNAL.txt`.
