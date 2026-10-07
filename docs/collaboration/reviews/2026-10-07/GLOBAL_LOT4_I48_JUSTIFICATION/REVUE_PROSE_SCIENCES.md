# I48 — Fibrillation et flutter auriculaires : contrelecture ciblée de la prose et des sciences

**Fragment : C-01-Cardiologie. Date : 7 octobre 2026.**

La livraison contient un développement causal utile, particulièrement dans les fenêtres. Sa croissance ne suffit pas à démontrer du remplissage. Plusieurs explications étaient néanmoins trop absolues ou contredisaient une autre partie du cours. Les corrections décrites ci-dessous portent sur les sources canoniques `chapters/I48/I48_c.html` et `chapters/I48/I48_pop1.html`, après autorisation complémentaire du responsable d’intégration. Les copies de Livraison Claude et les SVG restent intacts.

## Provenance et portée réelle

- Livraison examinée : PR #12, commit `b1f19c3510c1a828650867da033ebe2fbf30142e`, huit HTML sous `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I48/`, matérialisés séparément avant lecture.
- Ancienne source canonique : commit `3cbe0f52f799e27e0a2d9a65fd7d8093187af37d`, arbre `78e000ce`, fixé pour éviter une comparaison avec les changements concurrents.
- Injection locale pour contrelecture : `45004e92f6a43be40dc2050f84ead0349e9b4a26`. Elle ne constitue pas une publication depuis `main`.
- Lecture des fichiers `I48_a.html`, `I48_c.html` et `I48_d.html`, des quatre quiz de `I48_c.html` et des figures de ces fichiers. Vérifications médicales ponctuelles, sans certification de chaque affirmation ou posologie.
- Lecture des 17 fenêtres de `I48_pop1.html`, avec contrelecture déléguée ciblée, puis vérification et adaptation des points ci-dessous. Les résultats anticoagulants de `i48-infraclin` ont été confrontés aux essais primaires en coordination avec la revue anticoagulation.
- `I48_b.html` : examen ciblé des mentions ESC 2026. `I48_pop2.html` : échantillon ECG du flutter ; `I48_pop3.html` et `I48_pop4.html` : inventaire et volume, sans lecture médicale intégrale dans cette revue. Les revues anticoagulation et rythme couvrent des périmètres distincts.

Les repères de lignes suivants désignent le **HTML livré**, avant adaptations canoniques. Ils ne doivent pas être appliqués aveuglément au fichier corrigé.

## Volume et valeur pédagogique

Comptage indicatif du texte HTML, après retrait des balises, commentaires, scripts et styles ; les mots des tableaux, quiz, figures et templates sont inclus.

| Fichier | Ancienne source | PR #12 |
| --- | ---: | ---: |
| I48_a.html | 3 015 | 4 061 |
| I48_b.html | 5 381 | 7 590 |
| I48_c.html | 4 967 | 7 291 |
| I48_d.html | 1 715 | 3 222 |
| I48_pop1.html | 1 672 | 10 181 |
| I48_pop2.html | 2 758 | 12 013 |
| I48_pop3.html | 3 090 | 11 975 |
| I48_pop4.html | 3 114 | 10 006 |
| **Total** | **25 712** | **66 339** |

Le lot augmente d’environ 158 %. Les 100 fenêtres réparties entre POP1–4 comptent parfois 900 à 1 170 mots. Les longues fenêtres de réentrée et remodelage distinguent mécanisme, modèles expérimentaux, limites et conséquence thérapeutique : cette profondeur répond à la consigne de justification. Les ajouts sur l’anémie, Ashman, la dépendance à l’usage des antiarythmiques et le décalage entre INR et effet antithrombotique donnent aussi un véritable raisonnement.

Une duplication précise a été supprimée dans `i48-saos` : les anciens blocs « Mécanismes » et « De l’apnée à l’accès de FA » décrivaient deux fois pression négative, étirement et décharges autonomes. Le mécanisme est conservé dans un seul bloc ; les limites des questionnaires restent expliquées une fois. Les autres fenêtres longues n’ont pas été raccourcies sur le seul critère de leur taille.

## Corrections effectuées

| Repère livré | Problème | Adaptation canonique et preuve |
| --- | --- | --- |
| `c`, l.144, anatomie | L’ETO était dite seule capable d’exclure un thrombus, alors que l.72 admettait le scanner tardif. | L’ETO reste l’examen de référence ; le scanner avec acquisition tardive est reconnu selon contexte et protocole, notamment avant ablation. ESC 2024, §7.2.6 [S1]. |
| `c`, l.149, histologie | Diminution globale des connexines 40/43 présentée comme constante ; l’ajout attribuait directement une résistance longitudinale accrue à cette diminution. La première généralisation préexistait à PR #12. | Expression et localisation variables selon connexine, région et cardiopathie. L’hétérogénéité du couplage et la fibrose peuvent créer conduction lente ou bloc local, sans baisse universelle des deux protéines. Deux études humaines sont citées localement [S2, S3]. |
| `c`, l.152, histologie | Succession électrique « heures à jours », puis structurale « semaines à mois », sans réserve humaine ; contradiction avec la prudence conservée dans `a`, §3.2. | Délais expérimentaux distingués de l’évolution humaine, variable avec terrain et arythmie, sans calendrier fixe. Le modèle de Wijffels ne constitue pas un seuil humain [S4]. |
| `c`, l.63, surface mitrale | Le seuil de sévérité ≤1,5 cm² pouvait être lu comme seul seuil du choix AVK/AOD. | Distinction entre sévérité du rétrécissement et choix de l’anticoagulant : FA + rétrécissement rhumatismal avec surface ≤2,0 cm² excluent les AOD selon ESC/EACTS 2025, §6.2, tableau 2 et §10.2.2 [S5]. Aucune nouvelle classification universelle des autres étiologies n’est introduite. |
| `c`, l.145, science → examen | Flutter atypique envoyé systématiquement à une cartographie gauche. | Cartographie du circuit dans l’oreillette droite ou gauche selon substrat ; les macroréentrées atypiques droites sont reconnues par le consensus EHRA [S6]. |
| `c`, l.175, science → traitement | Contrôle du rythme associé sans délai à une systole auriculaire rétablie. | Restauration électrique distinguée de récupération mécanique, parfois retardée après cardioversion ; cohérence avec le paragraphe sur la sidération l.186 [S1]. |
| `pop1`, l.23, `i48-noeudav` | Tout RR régulier devenait signal d’alarme, avec intoxication digitalique « premier suspect ». | Suspicion de bloc devant une fréquence lente et régulière hors stimulation ventriculaire. Recherche de toxicité digitalique conditionnée à la prise de digoxine ; pacing attendu et flutter distingués [S7]. |
| `pop1`, l.81–88, `i48-infraclin` | Association charge–AVC convertie en causalité simple. Bénéfice net déduit de nombres d’AVC et d’hémorragies sans pondérer leur gravité. | Association explicitement distinguée de causalité. ARTESiA : efficacité en intention de traiter et sécurité pendant l’exposition sont distinguées ; les taux ne sont pas soustraits pour trancher une balance individuelle. Recommandation ESC IIb et discussion individuelle conservées [S1, S8]. |
| `pop1`, l.99, `i48-colaus` | Sous-groupe Swiss-AF décrit sans AVC, oubliant l’AIT ; association lésions/cognition prolongée en causalité de la FA. | AVC **et AIT** exclus du sous-groupe concerné. Analyse transversale et absence de preuve causale rendues explicites. Dates 2014–2017 et effectifs conservés [S9]. |
| `pop1`, l.118, `i48-poids` | Perte moyenne sous sémaglutide transformée en atteinte garantie de la cible ; population et dose absentes. | STEP 1 : dose 2,4 mg/semaine, adultes sans diabète, mesures d’hygiène de vie, moyenne 14,9 % à 68 semaines. La réponse individuelle n’est pas garantie. Exemple corrigé : perdre au moins 11 kg depuis 110 kg signifie atteindre 99 kg **ou moins** [S10]. |
| `pop1`, l.124 et l.128, `i48-tachycm` | Toute hausse de FEVG faisait disparaître l’indication de défibrillateur ; le seuil de 35 % résumait toutes les indications. | Réévaluation selon FEVG finale, substrat et risque arythmique. Une hausse de 20 à 30 % laisse une FEVG ≤35 %. Distinction entre prévention primaire fondée sur FEVG et autres indications ; aucune dépose automatique d’un dispositif n’est suggérée [S11]. |
| `pop1`, l.41, `i48-vp` | Bouton « activité automatique et déclenchée » pointant vers sa propre fenêtre. | Renvoi circulaire retiré ; différence entre automatisme diastolique et activité déclenchée par une post-dépolarisation explicitée dans la même fenêtre. Aucun nouveau template n’a été ajouté. |

Le point sur le défibrillateur pouvait modifier une décision clinique et nécessitait correction avant validation. Les autres corrections empêchent surtout des exclusions injustifiées, des généralisations ou une démonstration causale excessive. Ce tableau n’est pas un audit exhaustif des décisions thérapeutiques I48.

## Corrections antérieures conservées

- `i48-infraclin`, l.79 : fréquence auriculaire ≥170/min, généralement plus de cinq minutes, inspection visuelle et artefacts. Cette formulation sourcée antérieure est préservée.
- `i48-colaus`, l.99 : recrutement Swiss-AF **2014–2017**, 2 415 patients et 14 centres. Les limites ajoutées ne remplacent pas ces données historiques.
- Les quatre quiz ont été lus. Le calcul de Cockcroft-Gault du cas 2 donne environ 28 mL/min ; les deux critères âge/poids et la clairance justifient la dose réduite présentée. Les explications ECG ajoutées enseignent un mécanisme utile. Cette lecture ne valide pas toutes les décisions cliniques possibles autour des cas.

## Mentions ESC 2026 : vérification et limites

Les références 2026 de `b`, l.121/l.167 et `d`, l.14, ne doivent pas être qualifiées d’inventées sur la base de leur année.

- Le communiqué **officiel ESC du 29 août 2026** indique bien le passage à deux phénotypes, HFrEF avec FEVG <50 % et HFpEF ≥50 %, et cite les recommandations DOI `10.1093/eurheartj/ehag100` [S12]. La nouvelle dénomination ne redéfinit pas à elle seule les conditions de prescription de l’ESC FA 2024 ou d’une monographie suisse.
- Le communiqué **officiel ESC du 30 août 2026** inclut la FA parmi les affections pouvant bénéficier de réadaptation ; les recommandations sont identifiées par DOI `10.1093/eurheartj/ehag099` [S13].
- Vérification personnelle du portail et des communiqués des auteurs, **pas lecture intégrale des recommandations 2026**. Les liens ont été transmis à la revue rythme pour localisation bibliographique dans `b/d`. Aucune classe ou indication plus précise n’est certifiée ici.

## Réserves résiduelles de rédaction et de figures

- `pop2`, `i48-ecg-flutter`, l.77 et l.84 : le premier passage explique positivement le signal V1 par un front latéral, tandis que le second dit que son origine reste discutée. La formulation prudente doit gouverner les deux passages. Signal transmis au propriétaire de POP2, sans modification concurrente de ce fichier.
- `a`, §2 : l’explication des AVC plus graves par un embole souvent volumineux, proximal et avant développement de collatérales mérite une source dédiée et une formulation probabiliste. Les cohortes d’imagerie n’établissent pas une cause unique ; ce point n’a pas été modifié dans ce périmètre.
- Figures héritées de `c`, l.186/l.192 : la prévention embolique apparaît après la coagulation dans une chaîne descendante, comme une conséquence plutôt qu’une intervention ; le schéma génétique place le substrat au-dessus des deux facteurs, alors que la légende parle de convergence vers lui. Ces SVG **préexistaient** à PR #12 et restent inchangés. Leur restructuration relève d’une correction graphique distincte.
- Plusieurs encadrés « Science → clinique/examen/traitement » reprennent une information proche du paragraphe qui les précède. Ils peuvent servir de synthèse ; une réécriture future doit fusionner seulement les doublons qui n’ajoutent ni mécanisme, ni limite, ni décision.

La livraison ne peut donc pas être déclarée « toutes les affirmations justifiées et entièrement épurées » à partir de cette seule contrelecture. Les améliorations causales constatées, les corrections effectuées et les réserves restantes sont séparées.

## Sources primaires et accès effectivement utilisés

Consultation le 7 octobre 2026. Les pages de résumés ou extraits indexés ne sont pas présentées comme du texte intégral relu.

| ID | Source et repère | Accès utilisé |
| --- | --- | --- |
| S1 | [Van Gelder et coll., ESC FA 2024](https://academic.oup.com/eurheartj/article/45/36/3314/7738779), DOI ehae176, §6.2.3/7.2.6 et cardioversion. | Extraits indexés de la publication ; ouverture OUP bloquée par redirection CDN. |
| S2 | [Polontchouk et coll., JACC 2001](https://pubmed.ncbi.nlm.nih.gov/11527649/), DOI 10.1016/S0735-1097(01)01443-7. | Résumé primaire PubMed et extraits de la publication. |
| S3 | [Wetzel et coll., Heart 2005](https://pubmed.ncbi.nlm.nih.gov/15657225/), DOI 10.1136/hrt.2003.024216. | Résumé primaire PubMed ouvert, résultats et DOI vérifiés. |
| S4 | [Wijffels et coll., Circulation 1995](https://pubmed.ncbi.nlm.nih.gov/7671380/), DOI 10.1161/01.CIR.92.7.1954. | Résumé primaire indexé ; modèle caprin. |
| S5 | [Praz et coll., ESC/EACTS 2025](https://academic.oup.com/eurheartj/article/46/44/4635/8234488), DOI ehaf194 ; §6.2/tableau 2 et §10.2.2. | [PDF primaire en miroir](https://inavalverhd.inaheart.org/wp-content/uploads/2025/09/2025-ESC-EACTS-Guidelines-for-the-Management-of-Valvular-Heart-Disease.pdf), texte lu aux pages article 23 et 46. |
| S6 | [Consensus EHRA sur les arythmies supraventriculaires](https://doi.org/10.1093/europace/euw301), section flutter atypique droit. | Extrait indexé de la publication du consensus. |
| S7 | [Glikson et coll., ESC stimulation 2021](https://academic.oup.com/eurheartj/article/42/35/3427/6358547), DOI ehab364, §5.2.2.2. | Extrait indexé du texte primaire et contrelecture déléguée. |
| S8 | [Healey et coll., ARTESiA](https://www.nejm.org/doi/full/10.1056/NEJMoa2310234). | Résumé et extraits primaires NEJM : méthodes d’analyse et taux vérifiés. |
| S9 | [Conen et coll., Swiss-AF, JACC 2019](https://pubmed.ncbi.nlm.nih.gov/30846109/), DOI 10.1016/j.jacc.2018.12.039. | Résumé primaire ouvert ; recrutement et limites confrontés au texte de publication par la contrelecture déléguée. |
| S10 | [Wilding et coll., STEP 1, NEJM 2021](https://www.nejm.org/doi/full/10.1056/NEJMoa2032183). | Résumé et extraits primaires : population, dose, moyenne et durée vérifiées. |
| S11 | [Zeppenfeld et coll., ESC arythmies ventriculaires 2022](https://academic.oup.com/eurheartj/article/43/40/3997/6675633), DOI ehac262, §7.1.3/figure 19. | Extraits indexés du texte primaire et contrelecture déléguée ; la formulation retenue impose une réévaluation et n’invente pas de nouveau seuil. |
| S12 | [ESC : recommandations IC 2026, communiqué du 29 août](https://www.escardio.org/news/news-room/congress-news/2026-esc-guidelines-for-the-management-of-heart-failure/). | Page officielle ouverte : phénotypes et référence ehag100 lus. |
| S13 | [ESC : réadaptation 2026, communiqué du 30 août](https://www.escardio.org/news/news-room/congress-news/2026-esc-guidelines-on-cardiac-rehabilitation/). | Page officielle ouverte : FA et référence ehag099 lues. |

## Contrôles réalisés et limites

- Comparaison des textes livrés et de la base canonique figée ; revue des adaptations locales.
- Décodage UTF-8 réussi pour les deux HTML corrigés.
- Identifiants et ordre des templates conservés ; SVG comparés textuellement et inchangés ; aucun nouveau `data-k` ajouté.
- Assertions de conservation de la formulation AHRE antérieure et de Swiss-AF 2014–2017 réussies.
- `git diff --check` exécuté avant commit.
- Aucun build, modification de `dist`, contrôle navigateur, publication ou déploiement effectué par cette sous-revue. Elle ne certifie ni le cours entier, ni les autres cours du fragment, ni la complétude CIM-11.
