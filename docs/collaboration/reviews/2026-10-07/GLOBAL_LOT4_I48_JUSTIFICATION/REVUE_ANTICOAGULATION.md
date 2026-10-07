# Contrelecture ciblée — I48 — Fibrillation et flutter auriculaires

- Responsable : Codex, revue indépendante des ajouts concernant l’anticoagulation.
- Fragment : **C-01-Cardiologie**.
- Livraison examinée : Claude, PR #12, tête `b1f19c3510c1a828650867da033ebe2fbf30142e`.
- Base canonique après réception : `45004e92f6a43be40dc2050f84ead0349e9b4a26`.
- Date : 7 octobre 2026.
- Lecture ciblée : `I48_b.html`, fenêtres anticoagulation de `I48_pop3.html` et `I48_pop4.html`, ainsi que `i48-infraclin` de `I48_pop1.html` et `i48-preexc` de `I48_pop2.html`.
- Modification exclusive : `chapters/I48/I48_pop3.html`. Les huit originaux sous `livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I48/` sont conservés. Aucun fichier `dist/` modifié.
- État : corrections canoniques ciblées ; propositions concernant les autres propriétaires transmises à l’équipe. Cette revue ne valide pas tout le chapitre.

## Observations corrigées dans la source canonique

| ID | Repère dans `I48_pop3.html` | Défaut constaté dans la livraison Claude | Décision appliquée | Source et accès |
| --- | --- | --- | --- | --- |
| AC-01 | `i48-24h`, « Sidération et quatre semaines après » ; `i48-eto`, « Limites et risques » | Le nouveau développement réintroduisait une règle après « toute cardioversion » et annonçait que le cours suivait seulement le tableau de classe I. Son propre paragraphe « Application » conservait pourtant l’option précédente. | Harmonisation avec les arbitrages I48-09 à I48-11 : règle habituelle et exception limitée conservées ensemble. Une ETO négative ne constitue pas, seule, une exception. | ESC 2024, §7.2.1, figure 12 et tableau de recommandations 15 ; PDF intégral [S1]. |
| AC-02 | `i48-hasbled`, « Exposition excessive » et « Facteurs modifiables » | Le passage nouveau imposait un passage à un AOD sans condition d’éligibilité après un temps insuffisant dans la zone. Il appliquait également l’INR 2–3 et le seuil 3 à toutes les indications. | Éligibilité explicitée ; valve mécanique et rétrécissement mitral exclus du passage automatique. Cible individuelle distinguée de la cible habituelle de la FA. | ESC 2024, tableau de recommandations 7 [S1] ; ESC/EACTS 2025, tableau 10 [S2]. |
| AC-03 | `i48-inr`, « Cibles » et conduite devant un INR excessif | Défaut **hérité** : une zone mécanique unique 2,5–3,5, puis « INR entre 3 et 5 : sauter une prise ». Un INR 3,2 peut pourtant appartenir à la zone prescrite. Le seuil vague supérieur à 5 conduisait à la vitamine K automatique. | Comparaison préalable à la cible individuelle ; distinction du saignement et du degré réel de surdosage. La vitamine K orale n’est plus présentée comme systématique dans la zone 4,5–10 sans saignement. Le protocole local, le contrôle rapproché et le risque thrombotique restent explicites. | ESC/EACTS 2025, tableau 10 et §14.3.1.2 [S2]. |
| AC-04 | `i48-mitral`, « Seuil de surface » | L’ajout laissait la bande 1,5–2 cm² à une discussion indéterminée en se référant uniquement aux valvulopathies de 2021. Cela pouvait faire utiliser le seuil de sévérité de 1,5 cm² comme frontière d’éligibilité aux AOD. | Distinction entre sévérité valvulaire et choix de l’anticoagulant ; restriction concernant la FA avec rétrécissement rhumatismal et surface ≤2,0 cm² explicitée. | ESC/EACTS 2025, §6.2, tableau de recommandations 2, et §10.2.2 [S2]. |
| AC-05 | `i48-laao`, « Données récentes » et « Conséquences dans les essais » | Les chiffres composites validés avaient été conservés, mais un nouvel ajout prétendait que les mécanismes résiduels « expliquent probablement » l’absence de supériorité sur les AVC. Il suggérait aussi une protection de l’AOD contre toutes les autres sources emboliques. | Retrait du lien causal attribué à CHAMPION-AF ; conservation des résultats composites et de leur limite. La proportion anatomique de thrombi hors auricule est distinguée d’une incidence d’AVC. | CHAMPION-AF, résumé primaire reproduit par un auteur [S3] ; revue anatomique de Blackshear et Odell [S4]. |
| AC-06 | `i48-bilan`, « Coagulation de base » | Le nouveau texte enchaînait temps de céphaline allongé, anticoagulant lupique et préférence pour un AVK dans le syndrome triple positif, sans présenter la population effectivement étudiée. | Un test isolé ne diagnostique plus implicitement le syndrome. La comparaison est attribuée à 120 patients avec syndrome **thrombotique**, triple positivité et thrombose antérieure ; cette preuve n’est pas présentée comme un essai de FA ordinaire. | TRAPS, Pengo et coll. 2018, résumé original [S5]. |
| AC-07 | `i48-24h`, mêmes mécanismes | Les délais de récupération étaient présentés comme une propriété générale de l’oreillette et de l’auricule. Le chiffre 98 % semblait universel. | Attribution des délais au Doppler transmitral dans une cohorte de 60 patients ; absence de garantie individuelle pour l’auricule. Attribution de 98 % aux événements recensés dans des séries anciennes. | Manning et coll. 1994, résumé original reproduit par un auteur [S6] ; Berger et Schweitzer 1998, résumé original [S7]. |

Les restrictions de portée changent une décision concrète : un faible temps dans la zone ne rend pas éligible un porteur de valve mécanique ; un seuil de sévérité valvulaire n’est pas automatiquement un seuil de prescription ; une association anatomique ne démontre pas le mécanisme d’un résultat d’essai.

## Arbitrages Codex précédents

Le registre contrôlé est `audits/MECANISMES_2026-10-07/CODEX_ARBITRAGES.json`, revue PR #10, tête `be6a909059200711493064bd9c96a7437d71c019`.

| Arbitrage | Contrôle dans ce périmètre |
| --- | --- |
| I48-01 — Sepsis et cardioversion urgente | Le passage de `b` conserve l’indication urgente lorsque la FA provoque ou aggrave l’instabilité. |
| I48-04 — INR précoce et effet maximal | La formulation canonique de `c` était conservée. L’ajout de `pop4/i48-avk` sur la nécrose cutanée risquait néanmoins de réintroduire un chevauchement généralisé ; proposition transmise au propriétaire de ce fichier. |
| I48-05 — FA pré-excitée et différentiels | `pop2/i48-preexc` conserve la suspicion et les diagnostics différentiels. Les contre-indications nodales demeurent explicites. |
| I48-06 à I48-08 — CHAMPION-AF | Résultats composites conservés. Aucun taux isolé d’AVC 3,2 % contre 2,0 % réintroduit. Le lien causal ajouté dans `pop3` a été retiré. |
| I48-09 à I48-11 — Cardioversion | Les passages révisés antérieurs restent présents dans `b`, `pop3/Application` et le Pareto de `pop4`. AC-01 corrige leur contradiction avec le nouveau développement de `pop3`. Le schéma de `b` a été signalé à son propriétaire. |

Les arbitrages I48-02 et I48-03 relèvent de l’autre revue. La conservation sémantique d’un passage n’est pas assimilée à une identité octet pour octet, notamment après ajout de mots cliquables.

## Réserves et propositions hors du fichier modifié

- **FA infraclinique, `pop1/i48-infraclin`.** Les résultats ARTESiA cités sont cohérents avec le résumé primaire. En revanche, le bénéfice « net » ne peut pas être calculé par soustraction brute des AVC et hémorragies : les analyses d’efficacité et de sécurité diffèrent, et la gravité des événements compte. L’explication de la faible charge doit rester une association/hypothèse, conformément à la discussion « marqueur ou cause » déjà présente. Proposition transmise à la revue de prose ; source ARTESiA [S8].
- **Relais d’initiation, `pop4/i48-avk`.** La nécrose cutanée rare ne démontre pas une obligation d’héparine pour toute FA isolée. La réserve prolonge I48-04. Une cohorte primaire de FA non valvulaire soutient l’absence de relais systématique, sans constituer un essai randomisé ni une preuve pour toutes les valves ; proposition transmise à la revue du rythme [S9].
- **Pré-excitation, `b` et `pop2/i48-preexc`.** Aucune nouvelle inversion de conduite observée : freinateurs nodaux contre-indiqués, amiodarone évitée, cardioversion urgente si instabilité. La disponibilité suisse des alternatives n’a pas été confirmée dans une information professionnelle actuelle lors de cette revue. Cette réserve n’autorise pas à prétendre une indisponibilité absolue.
- Les modèles expérimentaux de coagulation sur prothèse sont explicitement présentés comme hypothétiques chez l’homme. Leur présence ne prouve pas le mécanisme clinique de l’échec des AOD. La réserve concerne surtout la portée de l’explication, sans contester les restrictions thérapeutiques établies.

## Sources consultées le 7 octobre 2026

| Réf. | Source primaire, version et accès réel |
| --- | --- |
| S1 | Van Gelder et coll., **ESC 2024 FA**, doi:10.1093/eurheartj/ehae176. [Article officiel](https://academic.oup.com/eurheartj/article/45/36/3314/7738779) bloqué par le relais CDN ; [PDF intégral accessible](https://forening.sls.se/media/kfyncecr/2024-esc-guidelines.pdf), §6.2.1–6.2.3, §7.2.1, §9.11, tableau de recommandations 7 et 15, figure 12. |
| S2 | Praz et coll., **ESC/EACTS 2025 valvulopathies**, doi:10.1093/eurheartj/ehaf194. [Article officiel](https://academic.oup.com/eurheartj/article/46/44/4635/8234488) et [PDF intégral reproduisant l’article](https://inavalverhd.inaheart.org/wp-content/uploads/2025/09/2025-ESC-EACTS-Guidelines-for-the-Management-of-Valvular-Heart-Disease.pdf). §6.2 p.23, §10.2.2 p.46, §14.3.1.2 et tableau 10 p.59, pagination de ce PDF. |
| S3 | Doshi et coll., **CHAMPION-AF**, N Engl Med 2026;394:2083–2094, doi:10.1056/NEJMoa2517213, PMID 41910347. NEJM direct refusé ; [dépôt institutionnel d’un auteur](https://pure.au.dk/portal/en/publications/left-atrial-appendage-closure-or-anticoagulation-for-atrial-fibri/) donnant le résumé original. Les résultats globaux sont vérifiés ; aucun sous-critère isolé non accessible n’est certifié. |
| S4 | Blackshear et Odell 1996, doi:10.1016/0003-4975(95)00887-X. [Résumé original](https://www.sciencedirect.com/science/article/pii/000349759500887X), revue de 23 séries ; localisation anatomique et anticoagulation non contrôlée. |
| S5 | Pengo et coll., **TRAPS**, Blood 2018;132:1365–1371, doi:10.1182/blood-2018-04-848333. [Résumé PubMed original](https://pubmed.ncbi.nlm.nih.gov/30002145/). |
| S6 | Manning et coll. 1994, doi:10.1016/0735-1097(94)90652-1. [Résumé original au dépôt Duke](https://scholars.duke.edu/publication/750275), étude observationnelle après cardioversion. |
| S7 | Berger et Schweitzer 1998, doi:10.1016/S0002-9149(98)00704-8. [Résumé PubMed original](https://pubmed.ncbi.nlm.nih.gov/9874066/), analyse rétrospective de 32 études. |
| S8 | Healey et coll., **ARTESiA**, doi:10.1056/NEJMoa2310234. [Résumé PubMed original](https://pubmed.ncbi.nlm.nih.gov/37952132/), distinguant intention de traiter et analyse pendant traitement. |
| S9 | Kim et coll. 2015, doi:10.1111/jth.12810. [Résumé PubMed original](https://pubmed.ncbi.nlm.nih.gov/25472735/), cohorte avec appariement par score de propension, initiation de warfarine dans la FA non valvulaire. |

## Contrôles exécutés et limites

- `git diff --check -- chapters/I48/I48_pop3.html` : réussi.
- Comparaison des clés `data-pop` avant/après la base `45004e9` : **29 fenêtres, mêmes clés et même ordre**.
- Original Claude `I48_pop3.html` inchangé, SHA-256 `8841493f7fe4acb32a984bbe818cf6d043cd6321385b91536358da3a52076fb3`.
- Canonique corrigé, SHA-256 `37499843c9b47ac193d90d8c7d77427b330c2235be5723b0204d97dcda94498a`.
- `python3 test_v7.py --static I48` : premier échec comportant deux nouveaux libellés de cette correction ; libellés corrigés. Deuxième exécution : échec limité à `S0735-1097`, `NEJMoa2032183`, `NEJM199103213241201`, dans les modifications concurrentes d’autres fichiers. Contrôle global final confié à l’intégration.
- Aucun rendu navigateur ni reconstruction effectué dans cette sous-tâche ; aucune modification `dist/`.

La revue ne couvre pas toutes les doses, tous les protocoles de saignement, toute la pharmacologie suisse, ni chaque nouvelle justification. Les détails individuels de CHAMPION-AF absents du résumé accessible restent non vérifiés. Aucun statut d’audit intégral, de validation des autres cours ou de complétude CIM-11 n’est attribué.
