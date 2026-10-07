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
