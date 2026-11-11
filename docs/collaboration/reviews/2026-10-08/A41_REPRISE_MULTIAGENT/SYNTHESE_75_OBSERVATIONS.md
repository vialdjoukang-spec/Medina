# Synthèse des 75 observations — A41 — Sepsis et choc septique de l’adulte (I-03-Infectiologie)

Capture : 2026-10-08T13:19:01.208600+00:00. Base auditée : 39b7ff0cc585c59ffbb99fb448940daa1950b34d ; reprise : db06b1fae3c27e93050850df44c3eb23fcd60164.

**75 IDs uniques : 68 propositions complètes, 2 partielles, 5 déléguées ; aucun ID sans disposition.** Priorités d’origine conservées : **10 majeures, 46 mineures, 19 éditoriales**. Les dispositions décrivent les propositions d’auteur et ne constituent aucune clôture externe, validation médicale ou injection.

**Claude externe : 0 observation clôturée sur ce nouveau candidat.** Les contrelectures internes Codex gardent leurs périmètres, exclusions et empreintes.

| Priorité d’origine | Complètes | Partielles | Déléguées | Sans disposition | Total |
|---|---:|---:|---:|---:|---:|
| majeure | 9 | 1 | 0 | 0 | 10 |
| mineure | 41 | 1 | 4 | 0 | 46 |
| éditoriale | 18 | 0 | 1 | 0 | 19 |

ESP-03 reste **majeure et partielle** : les plages artérielles suisses réellement lues sont attribuées à leur matrice ; le bicarbonate standard ne remplace pas le bicarbonate actuel/calculé. L’intervalle actuel et l’applicabilité des profils anioniques au calcul artériel/mixte restent à établir. ESP-07 reste **mineure et partielle** : drainage et limites échographiques documentés ; source spécifique accessible de pesée bénéfice/risque du contraste encore manquante.

P1-22 à P1-25 sont déléguées à test_allocation, P1-27 à claude_spec. **ESP-16 apparaît dans deux rapports auteurs** (figures C et pager D), compté une seule fois. Les sept dépendances P1 de P2 et les remarques nouvelles des contrelecteurs ne créent aucun nouvel ID.

## Portée des contrelectures internes

| Preuve | Périmètre | Limite |
|---|---|---|
| [CONTRELECTURE_PATHOLOGIE1](CONTRELECTURE_PATHOLOGIE1.json) | a/pop1, Pareto def/physio/diag ; 27 IDs parcourus ; extension ESP-02 cultures | 20 dispositions indépendantes entières, 3 composants partiels, 4 composants écrits par le lecteur exclus. pop_pa relu dans P2 ; empreinte pop2 historique conservée. |
| [CONTRELECTURE_PATHOLOGIE2](CONTRELECTURE_PATHOLOGIE2.json) | 16 observations P2 + 7 composants P1 ; b/pop_pa et quatre remarques ciblées résolues | Trois monographies pop2 de P2-08 exclues, revue pharmacologique complémentaire. Aucun nouvel audit de chaque fait inchangé. |
| [CONTRELECTURE_EXAMENS_SCIENCES](CONTRELECTURE_EXAMENS_SCIENCES.json) | C, quatre fenêtres, calculs, figures 4–7, delta Viollier/Medics | ESP-03/07 restent ouvertes. claude_spec auteur des Pareto pop2 : aucune auto-certification de ces composants. Lectures de caches/extraits selon modes déclarés. |
| [CONTRELECTURE_PHARMACOLOGIE](CONTRELECTURE_PHARMACOLOGIE.json) | D, huit monographies, sept Pareto ; ESP-16 à ESP-26 et deltas relus | Pareto Examens/Sciences : review_plan vérifie intégration/cohérence de ses propres données C, sans deuxième certification médicale indépendante. Deltas techniques limités à leur preuve exacte. |
| [CONTRELECTURE_GLOSSAIRE_BANQUE](CONTRELECTURE_GLOSSAIRE_BANQUE.json) | ESP-27 à ESP-32, glossaire/banque aux empreintes de la revue | Ajouts ultérieurs limités aux deltas effectivement relus ; unicité des cibles à rapprocher des HTML finaux. |

Les anciens états « en attente » restent archivés dans les rapports auteurs. Les preuves complémentaires reçues documentent leur progression réelle, dans chaque périmètre. Le JSON contient les fiches initiales, dispositions, dépendances, preuves et SHA des rapports utilisés.

## Matrice des 75 IDs

P1 = audit_pathologie_1 ; P2 = audit_pathologie_2 ; ESP = audit_examens_sciences_pharmacologie. Fichiers concernés = sources du lot candidat.

| ID d’origine | Index | Priorité | Auteur principal | Disposition | Fichiers concernés | Preuves |
|---|---:|---|---|---|---|---|
| audit_examens_sciences_pharmacologie-01 | 1 | majeure | review_plan | complète | A41_c.html, A41_pop_sciences_revision.html | [EXAMENS_SCIENCES](EXAMENS_SCIENCES.json) ; [CONTRELECTURE_EXAMENS_SCIENCES](CONTRELECTURE_EXAMENS_SCIENCES.json) |
| audit_examens_sciences_pharmacologie-02 | 2 | majeure | review_plan | complète | A41_c.html, A41_pop1.html | [EXAMENS_SCIENCES](EXAMENS_SCIENCES.json) ; [PATHOLOGIE1](PATHOLOGIE1.json) ; [CONTRELECTURE_EXAMENS_SCIENCES](CONTRELECTURE_EXAMENS_SCIENCES.json) ; [CONTRELECTURE_PATHOLOGIE1](CONTRELECTURE_PATHOLOGIE1.json) |
| audit_examens_sciences_pharmacologie-03 | 3 | majeure | review_plan | partielle | A41_c.html, A41_pop_sciences_revision.html | [EXAMENS_SCIENCES](EXAMENS_SCIENCES.json) ; [CONTRELECTURE_EXAMENS_SCIENCES](CONTRELECTURE_EXAMENS_SCIENCES.json) |
| audit_examens_sciences_pharmacologie-04 | 4 | mineure | review_plan | complète | A41_c.html | [EXAMENS_SCIENCES](EXAMENS_SCIENCES.json) ; [CONTRELECTURE_EXAMENS_SCIENCES](CONTRELECTURE_EXAMENS_SCIENCES.json) |
| audit_examens_sciences_pharmacologie-05 | 5 | mineure | review_plan | complète | A41_c.html | [EXAMENS_SCIENCES](EXAMENS_SCIENCES.json) ; [CONTRELECTURE_EXAMENS_SCIENCES](CONTRELECTURE_EXAMENS_SCIENCES.json) |
| audit_examens_sciences_pharmacologie-06 | 6 | éditoriale | review_plan | complète | A41_c.html | [EXAMENS_SCIENCES](EXAMENS_SCIENCES.json) ; [CONTRELECTURE_EXAMENS_SCIENCES](CONTRELECTURE_EXAMENS_SCIENCES.json) |
| audit_examens_sciences_pharmacologie-07 | 7 | mineure | review_plan | partielle | A41_c.html | [EXAMENS_SCIENCES](EXAMENS_SCIENCES.json) ; [CONTRELECTURE_EXAMENS_SCIENCES](CONTRELECTURE_EXAMENS_SCIENCES.json) |
| audit_examens_sciences_pharmacologie-08 | 8 | mineure | review_plan | complète | A41_c.html | [EXAMENS_SCIENCES](EXAMENS_SCIENCES.json) ; [CONTRELECTURE_EXAMENS_SCIENCES](CONTRELECTURE_EXAMENS_SCIENCES.json) |
| audit_examens_sciences_pharmacologie-09 | 9 | mineure | review_plan | complète | A41_c.html | [EXAMENS_SCIENCES](EXAMENS_SCIENCES.json) ; [CONTRELECTURE_EXAMENS_SCIENCES](CONTRELECTURE_EXAMENS_SCIENCES.json) |
| audit_examens_sciences_pharmacologie-10 | 10 | mineure | review_plan | complète | A41_c.html | [EXAMENS_SCIENCES](EXAMENS_SCIENCES.json) ; [CONTRELECTURE_EXAMENS_SCIENCES](CONTRELECTURE_EXAMENS_SCIENCES.json) |
| audit_examens_sciences_pharmacologie-11 | 11 | majeure | review_plan | complète | A41_c.html | [EXAMENS_SCIENCES](EXAMENS_SCIENCES.json) ; [CONTRELECTURE_EXAMENS_SCIENCES](CONTRELECTURE_EXAMENS_SCIENCES.json) |
| audit_examens_sciences_pharmacologie-12 | 12 | mineure | review_plan | complète | A41_c.html | [EXAMENS_SCIENCES](EXAMENS_SCIENCES.json) ; [CONTRELECTURE_EXAMENS_SCIENCES](CONTRELECTURE_EXAMENS_SCIENCES.json) |
| audit_examens_sciences_pharmacologie-13 | 13 | mineure | review_plan | complète | A41_c.html, A41_pop_sciences_revision.html | [EXAMENS_SCIENCES](EXAMENS_SCIENCES.json) ; [CONTRELECTURE_EXAMENS_SCIENCES](CONTRELECTURE_EXAMENS_SCIENCES.json) |
| audit_examens_sciences_pharmacologie-14 | 14 | mineure | review_plan | complète | A41_c.html | [EXAMENS_SCIENCES](EXAMENS_SCIENCES.json) ; [CONTRELECTURE_EXAMENS_SCIENCES](CONTRELECTURE_EXAMENS_SCIENCES.json) |
| audit_examens_sciences_pharmacologie-15 | 15 | éditoriale | review_plan | complète | A41_c.html | [EXAMENS_SCIENCES](EXAMENS_SCIENCES.json) ; [CONTRELECTURE_EXAMENS_SCIENCES](CONTRELECTURE_EXAMENS_SCIENCES.json) |
| audit_examens_sciences_pharmacologie-16 | 16 | éditoriale | review_plan | complète | A41_c.html, A41_d.html | [EXAMENS_SCIENCES](EXAMENS_SCIENCES.json) ; [PHARMACOLOGIE](PHARMACOLOGIE.json) ; [CONTRELECTURE_EXAMENS_SCIENCES](CONTRELECTURE_EXAMENS_SCIENCES.json) ; [CONTRELECTURE_PHARMACOLOGIE](CONTRELECTURE_PHARMACOLOGIE.json) |
| audit_examens_sciences_pharmacologie-17 | 17 | majeure | claude_spec | complète | A41_d.html, A41_pop2.html | [PHARMACOLOGIE](PHARMACOLOGIE.json) ; [CONTRELECTURE_PHARMACOLOGIE](CONTRELECTURE_PHARMACOLOGIE.json) |
| audit_examens_sciences_pharmacologie-18 | 18 | majeure | claude_spec | complète | A41_d.html, A41_pop2.html | [PHARMACOLOGIE](PHARMACOLOGIE.json) ; [CONTRELECTURE_PHARMACOLOGIE](CONTRELECTURE_PHARMACOLOGIE.json) |
| audit_examens_sciences_pharmacologie-19 | 19 | majeure | claude_spec | complète | A41_d.html, A41_pop2.html | [PHARMACOLOGIE](PHARMACOLOGIE.json) ; [CONTRELECTURE_PHARMACOLOGIE](CONTRELECTURE_PHARMACOLOGIE.json) |
| audit_examens_sciences_pharmacologie-20 | 20 | majeure | claude_spec | complète | A41_d.html, A41_pop2.html | [PHARMACOLOGIE](PHARMACOLOGIE.json) ; [CONTRELECTURE_PHARMACOLOGIE](CONTRELECTURE_PHARMACOLOGIE.json) |
| audit_examens_sciences_pharmacologie-21 | 21 | mineure | claude_spec | complète | A41_d.html, A41_pop2.html | [PHARMACOLOGIE](PHARMACOLOGIE.json) ; [CONTRELECTURE_PHARMACOLOGIE](CONTRELECTURE_PHARMACOLOGIE.json) |
| audit_examens_sciences_pharmacologie-22 | 22 | mineure | claude_spec | complète | A41_d.html, A41_pop2.html | [PHARMACOLOGIE](PHARMACOLOGIE.json) ; [CONTRELECTURE_PHARMACOLOGIE](CONTRELECTURE_PHARMACOLOGIE.json) |
| audit_examens_sciences_pharmacologie-23 | 23 | mineure | claude_spec | complète | A41_d.html, A41_pop2.html | [PHARMACOLOGIE](PHARMACOLOGIE.json) ; [CONTRELECTURE_PHARMACOLOGIE](CONTRELECTURE_PHARMACOLOGIE.json) |
| audit_examens_sciences_pharmacologie-24 | 24 | mineure | claude_spec | complète | A41_d.html, A41_pop2.html | [PHARMACOLOGIE](PHARMACOLOGIE.json) ; [CONTRELECTURE_PHARMACOLOGIE](CONTRELECTURE_PHARMACOLOGIE.json) |
| audit_examens_sciences_pharmacologie-25 | 25 | mineure | claude_spec | complète | A41_d.html, A41_pop2.html | [PHARMACOLOGIE](PHARMACOLOGIE.json) ; [CONTRELECTURE_PHARMACOLOGIE](CONTRELECTURE_PHARMACOLOGIE.json) |
| audit_examens_sciences_pharmacologie-26 | 26 | éditoriale | claude_spec | complète | A41_d.html, A41_pop2.html | [PHARMACOLOGIE](PHARMACOLOGIE.json) ; [CONTRELECTURE_PHARMACOLOGIE](CONTRELECTURE_PHARMACOLOGIE.json) |
| audit_examens_sciences_pharmacologie-27 | 27 | mineure | root | complète | A41_justifications.json | [GLOSSAIRE_BANQUE](GLOSSAIRE_BANQUE.json) ; [CONTRELECTURE_GLOSSAIRE_BANQUE](CONTRELECTURE_GLOSSAIRE_BANQUE.json) |
| audit_examens_sciences_pharmacologie-28 | 28 | mineure | root | complète | A41_justifications.json | [GLOSSAIRE_BANQUE](GLOSSAIRE_BANQUE.json) ; [CONTRELECTURE_GLOSSAIRE_BANQUE](CONTRELECTURE_GLOSSAIRE_BANQUE.json) |
| audit_examens_sciences_pharmacologie-29 | 29 | mineure | root | complète | A41_justifications.json | [GLOSSAIRE_BANQUE](GLOSSAIRE_BANQUE.json) ; [CONTRELECTURE_GLOSSAIRE_BANQUE](CONTRELECTURE_GLOSSAIRE_BANQUE.json) |
| audit_examens_sciences_pharmacologie-30 | 30 | mineure | root | complète | A41_justifications.json | [GLOSSAIRE_BANQUE](GLOSSAIRE_BANQUE.json) ; [CONTRELECTURE_GLOSSAIRE_BANQUE](CONTRELECTURE_GLOSSAIRE_BANQUE.json) |
| audit_examens_sciences_pharmacologie-31 | 31 | éditoriale | root | complète | a41.py | [GLOSSAIRE_BANQUE](GLOSSAIRE_BANQUE.json) ; [CONTRELECTURE_GLOSSAIRE_BANQUE](CONTRELECTURE_GLOSSAIRE_BANQUE.json) |
| audit_examens_sciences_pharmacologie-32 | 32 | éditoriale | root | complète | a41.py | [GLOSSAIRE_BANQUE](GLOSSAIRE_BANQUE.json) ; [CONTRELECTURE_GLOSSAIRE_BANQUE](CONTRELECTURE_GLOSSAIRE_BANQUE.json) |
| audit_pathologie_1-01 | 1 | mineure | sentinelle_medicale | complète | A41_a.html, A41_pop1.html | [PATHOLOGIE1](PATHOLOGIE1.json) ; [CONTRELECTURE_PATHOLOGIE1](CONTRELECTURE_PATHOLOGIE1.json) |
| audit_pathologie_1-02 | 2 | mineure | sentinelle_medicale | complète | A41_a.html | [PATHOLOGIE1](PATHOLOGIE1.json) ; [CONTRELECTURE_PATHOLOGIE1](CONTRELECTURE_PATHOLOGIE1.json) |
| audit_pathologie_1-03 | 3 | mineure | sentinelle_medicale | complète | A41_a.html | [PATHOLOGIE1](PATHOLOGIE1.json) ; [CONTRELECTURE_PATHOLOGIE1](CONTRELECTURE_PATHOLOGIE1.json) |
| audit_pathologie_1-04 | 4 | mineure | sentinelle_medicale | complète | A41_a.html, A41_pop2.html | [PATHOLOGIE1](PATHOLOGIE1.json) ; [CONTRELECTURE_PATHOLOGIE1](CONTRELECTURE_PATHOLOGIE1.json) |
| audit_pathologie_1-05 | 5 | éditoriale | sentinelle_medicale | complète | A41_a.html | [PATHOLOGIE1](PATHOLOGIE1.json) ; [CONTRELECTURE_PATHOLOGIE1](CONTRELECTURE_PATHOLOGIE1.json) |
| audit_pathologie_1-06 | 6 | éditoriale | sentinelle_medicale | complète | A41_a.html, A41_pop1.html, A41_pop_pa.html | [PATHOLOGIE1](PATHOLOGIE1.json) ; [PATHOLOGIE2](PATHOLOGIE2.json) ; [CONTRELECTURE_PATHOLOGIE1](CONTRELECTURE_PATHOLOGIE1.json) ; [CONTRELECTURE_PATHOLOGIE2](CONTRELECTURE_PATHOLOGIE2.json) |
| audit_pathologie_1-07 | 7 | éditoriale | sentinelle_medicale | complète | A41_a.html | [PATHOLOGIE1](PATHOLOGIE1.json) ; [CONTRELECTURE_PATHOLOGIE1](CONTRELECTURE_PATHOLOGIE1.json) |
| audit_pathologie_1-08 | 8 | mineure | sentinelle_medicale | complète | A41_a.html | [PATHOLOGIE1](PATHOLOGIE1.json) ; [CONTRELECTURE_PATHOLOGIE1](CONTRELECTURE_PATHOLOGIE1.json) |
| audit_pathologie_1-09 | 9 | mineure | sentinelle_medicale | complète | A41_a.html, A41_pop2.html, A41_pop_pa.html | [PATHOLOGIE1](PATHOLOGIE1.json) ; [PATHOLOGIE2](PATHOLOGIE2.json) ; [CONTRELECTURE_PATHOLOGIE1](CONTRELECTURE_PATHOLOGIE1.json) ; [CONTRELECTURE_PATHOLOGIE2](CONTRELECTURE_PATHOLOGIE2.json) |
| audit_pathologie_1-10 | 10 | mineure | sentinelle_medicale | complète | A41_a.html, A41_pop1.html, A41_pop2.html, A41_pop_pa.html | [PATHOLOGIE1](PATHOLOGIE1.json) ; [PATHOLOGIE2](PATHOLOGIE2.json) ; [CONTRELECTURE_PATHOLOGIE1](CONTRELECTURE_PATHOLOGIE1.json) ; [CONTRELECTURE_PATHOLOGIE2](CONTRELECTURE_PATHOLOGIE2.json) |
| audit_pathologie_1-11 | 11 | mineure | sentinelle_medicale | complète | A41_a.html | [PATHOLOGIE1](PATHOLOGIE1.json) ; [CONTRELECTURE_PATHOLOGIE1](CONTRELECTURE_PATHOLOGIE1.json) |
| audit_pathologie_1-12 | 12 | mineure | sentinelle_medicale | complète | A41_a.html | [PATHOLOGIE1](PATHOLOGIE1.json) ; [CONTRELECTURE_PATHOLOGIE1](CONTRELECTURE_PATHOLOGIE1.json) |
| audit_pathologie_1-13 | 13 | mineure | sentinelle_medicale | complète | A41_a.html, A41_pop2.html | [PATHOLOGIE1](PATHOLOGIE1.json) ; [CONTRELECTURE_PATHOLOGIE1](CONTRELECTURE_PATHOLOGIE1.json) |
| audit_pathologie_1-14 | 14 | mineure | sentinelle_medicale | complète | A41_a.html, A41_pop1.html, A41_pop2.html | [PATHOLOGIE1](PATHOLOGIE1.json) ; [CONTRELECTURE_PATHOLOGIE1](CONTRELECTURE_PATHOLOGIE1.json) |
| audit_pathologie_1-15 | 15 | mineure | sentinelle_medicale | complète | A41_a.html, A41_pop1.html, A41_pop2.html | [PATHOLOGIE1](PATHOLOGIE1.json) ; [CONTRELECTURE_PATHOLOGIE1](CONTRELECTURE_PATHOLOGIE1.json) |
| audit_pathologie_1-16 | 16 | mineure | sentinelle_medicale | complète | A41_a.html | [PATHOLOGIE1](PATHOLOGIE1.json) ; [CONTRELECTURE_PATHOLOGIE1](CONTRELECTURE_PATHOLOGIE1.json) |
| audit_pathologie_1-17 | 17 | éditoriale | sentinelle_medicale | complète | A41_a.html, A41_pop2.html | [PATHOLOGIE1](PATHOLOGIE1.json) ; [CONTRELECTURE_PATHOLOGIE1](CONTRELECTURE_PATHOLOGIE1.json) |
| audit_pathologie_1-18 | 18 | éditoriale | sentinelle_medicale | complète | A41_a.html, A41_pop1.html | [PATHOLOGIE1](PATHOLOGIE1.json) ; [CONTRELECTURE_PATHOLOGIE1](CONTRELECTURE_PATHOLOGIE1.json) |
| audit_pathologie_1-19 | 19 | éditoriale | sentinelle_medicale | complète | A41_a.html | [PATHOLOGIE1](PATHOLOGIE1.json) ; [CONTRELECTURE_PATHOLOGIE1](CONTRELECTURE_PATHOLOGIE1.json) |
| audit_pathologie_1-20 | 20 | éditoriale | sentinelle_medicale | complète | A41_a.html | [PATHOLOGIE1](PATHOLOGIE1.json) ; [CONTRELECTURE_PATHOLOGIE1](CONTRELECTURE_PATHOLOGIE1.json) |
| audit_pathologie_1-21 | 21 | éditoriale | sentinelle_medicale | complète | A41_a.html | [PATHOLOGIE1](PATHOLOGIE1.json) ; [CONTRELECTURE_PATHOLOGIE1](CONTRELECTURE_PATHOLOGIE1.json) |
| audit_pathologie_1-22 | 22 | mineure | test_allocation | déléguée | A41_pop_pa.html | [PATHOLOGIE1](PATHOLOGIE1.json) ; [PATHOLOGIE2](PATHOLOGIE2.json) ; [CONTRELECTURE_PATHOLOGIE1](CONTRELECTURE_PATHOLOGIE1.json) ; [CONTRELECTURE_PATHOLOGIE2](CONTRELECTURE_PATHOLOGIE2.json) |
| audit_pathologie_1-23 | 23 | mineure | test_allocation | déléguée | A41_pop_pa.html | [PATHOLOGIE1](PATHOLOGIE1.json) ; [PATHOLOGIE2](PATHOLOGIE2.json) ; [CONTRELECTURE_PATHOLOGIE1](CONTRELECTURE_PATHOLOGIE1.json) ; [CONTRELECTURE_PATHOLOGIE2](CONTRELECTURE_PATHOLOGIE2.json) |
| audit_pathologie_1-24 | 24 | mineure | test_allocation | déléguée | A41_pop_pa.html | [PATHOLOGIE1](PATHOLOGIE1.json) ; [PATHOLOGIE2](PATHOLOGIE2.json) ; [CONTRELECTURE_PATHOLOGIE1](CONTRELECTURE_PATHOLOGIE1.json) ; [CONTRELECTURE_PATHOLOGIE2](CONTRELECTURE_PATHOLOGIE2.json) |
| audit_pathologie_1-25 | 25 | mineure | test_allocation | déléguée | A41_pop_pa.html | [PATHOLOGIE1](PATHOLOGIE1.json) ; [PATHOLOGIE2](PATHOLOGIE2.json) ; [CONTRELECTURE_PATHOLOGIE1](CONTRELECTURE_PATHOLOGIE1.json) ; [CONTRELECTURE_PATHOLOGIE2](CONTRELECTURE_PATHOLOGIE2.json) |
| audit_pathologie_1-26 | 26 | mineure | sentinelle_medicale | complète | A41_pop1.html | [PATHOLOGIE1](PATHOLOGIE1.json) ; [CONTRELECTURE_PATHOLOGIE1](CONTRELECTURE_PATHOLOGIE1.json) |
| audit_pathologie_1-27 | 27 | éditoriale | claude_spec | déléguée | A41_pop2.html | [PATHOLOGIE1](PATHOLOGIE1.json) ; [CONTRELECTURE_PATHOLOGIE1](CONTRELECTURE_PATHOLOGIE1.json) |
| audit_pathologie_2-01 | 1 | majeure | test_allocation | complète | A41_b.html | [PATHOLOGIE2](PATHOLOGIE2.json) ; [CONTRELECTURE_PATHOLOGIE2](CONTRELECTURE_PATHOLOGIE2.json) |
| audit_pathologie_2-02 | 2 | majeure | test_allocation | complète | A41_b.html, A41_pop_pa.html | [PATHOLOGIE2](PATHOLOGIE2.json) ; [CONTRELECTURE_PATHOLOGIE2](CONTRELECTURE_PATHOLOGIE2.json) |
| audit_pathologie_2-03 | 3 | mineure | test_allocation | complète | A41_b.html | [PATHOLOGIE2](PATHOLOGIE2.json) ; [CONTRELECTURE_PATHOLOGIE2](CONTRELECTURE_PATHOLOGIE2.json) |
| audit_pathologie_2-04 | 4 | mineure | test_allocation | complète | A41_b.html | [PATHOLOGIE2](PATHOLOGIE2.json) ; [CONTRELECTURE_PATHOLOGIE2](CONTRELECTURE_PATHOLOGIE2.json) |
| audit_pathologie_2-05 | 5 | mineure | test_allocation | complète | A41_b.html | [PATHOLOGIE2](PATHOLOGIE2.json) ; [CONTRELECTURE_PATHOLOGIE2](CONTRELECTURE_PATHOLOGIE2.json) |
| audit_pathologie_2-06 | 6 | mineure | test_allocation | complète | A41_b.html | [PATHOLOGIE2](PATHOLOGIE2.json) ; [CONTRELECTURE_PATHOLOGIE2](CONTRELECTURE_PATHOLOGIE2.json) |
| audit_pathologie_2-07 | 7 | mineure | test_allocation | complète | A41_b.html | [PATHOLOGIE2](PATHOLOGIE2.json) ; [CONTRELECTURE_PATHOLOGIE2](CONTRELECTURE_PATHOLOGIE2.json) |
| audit_pathologie_2-08 | 8 | mineure | test_allocation | complète | A41_b.html, A41_pop2.html, A41_pop_pa.html | [PATHOLOGIE2](PATHOLOGIE2.json) ; [CONTRELECTURE_PATHOLOGIE2](CONTRELECTURE_PATHOLOGIE2.json) |
| audit_pathologie_2-09 | 9 | mineure | test_allocation | complète | A41_b.html | [PATHOLOGIE2](PATHOLOGIE2.json) ; [CONTRELECTURE_PATHOLOGIE2](CONTRELECTURE_PATHOLOGIE2.json) |
| audit_pathologie_2-10 | 10 | mineure | test_allocation | complète | A41_b.html | [PATHOLOGIE2](PATHOLOGIE2.json) ; [CONTRELECTURE_PATHOLOGIE2](CONTRELECTURE_PATHOLOGIE2.json) |
| audit_pathologie_2-11 | 11 | mineure | test_allocation | complète | A41_b.html, A41_pop_pa.html | [PATHOLOGIE2](PATHOLOGIE2.json) ; [CONTRELECTURE_PATHOLOGIE2](CONTRELECTURE_PATHOLOGIE2.json) |
| audit_pathologie_2-12 | 12 | mineure | test_allocation | complète | A41_b.html | [PATHOLOGIE2](PATHOLOGIE2.json) ; [CONTRELECTURE_PATHOLOGIE2](CONTRELECTURE_PATHOLOGIE2.json) |
| audit_pathologie_2-13 | 13 | éditoriale | test_allocation | complète | A41_b.html | [PATHOLOGIE2](PATHOLOGIE2.json) ; [CONTRELECTURE_PATHOLOGIE2](CONTRELECTURE_PATHOLOGIE2.json) |
| audit_pathologie_2-14 | 14 | éditoriale | test_allocation | complète | A41_b.html | [PATHOLOGIE2](PATHOLOGIE2.json) ; [CONTRELECTURE_PATHOLOGIE2](CONTRELECTURE_PATHOLOGIE2.json) |
| audit_pathologie_2-15 | 15 | éditoriale | test_allocation | complète | A41_b.html | [PATHOLOGIE2](PATHOLOGIE2.json) ; [CONTRELECTURE_PATHOLOGIE2](CONTRELECTURE_PATHOLOGIE2.json) |
| audit_pathologie_2-16 | 16 | éditoriale | test_allocation | complète | A41_b.html | [PATHOLOGIE2](PATHOLOGIE2.json) ; [CONTRELECTURE_PATHOLOGIE2](CONTRELECTURE_PATHOLOGIE2.json) |

## Empreintes et rapprochement des deltas

Une différence d’empreinte peut provenir d’un delta technique : elle ne signifie automatiquement ni nouvelle erreur médicale, ni revue complète des nouveaux octets. Le JSON conserve les SHA déclarés et capturés.

| Source candidate | SHA-256 capturé |
|---|---|
| A41_a.html | 34a54b45c140cfb352add0adf9feed32c39fc34359f03fff0f58221256e650d1 |
| A41_b.html | b3955084555b603f56f905cdaf54407f1c06603bde38dc80930776e5860c1ace |
| A41_c.html | fdf9991f19aa93552ca94f52cdb3487637e64c85b79040d7608bc8d39c0da2dc |
| A41_d.html | 85c0d9a2e122a11b485d50fd27437847d146ca4e2231cf2afda82a62a57c2756 |
| A41_pop1.html | cdb1671a68f9f87d78b468c57b958cf894ada46439cd05b29d2b3e2db2645cce |
| A41_pop2.html | e7093e7453ac0fbe9d63aee17094a8a25893e899ebdd8d5936b70ddc10fbedc0 |
| A41_pop_pa.html | f383ad214398215420af0474e35d53478a6688bbfea14721ff3c8c9bba1e560d |
| A41_pop_sciences_revision.html | dd5ceeba3e8a346f2da2b4ebbe5c9f7015cc7e819f941ddc475ae89e2a1d234e |
| A41_justifications.json | c47273d990cbbc4e68a1f0d0620e4f17c6be96f507a1747e1866699a56c18822 |
| a41.py | f7d9e45c7df4b04d4b746989fbf3b7808dfec9712415fef0de51533affc2d69a |

| Preuve avec empreinte différente | Fichier | SHA déclaré | SHA candidat capturé |
|---|---|---|---|
| PATHOLOGIE1 (owned_files.A41_a.html) | A41_a.html | 6d8a376ff807e05ae09837fa47e937a5cc83bc8e7db6471cb366a9bfdfc37743 | 34a54b45c140cfb352add0adf9feed32c39fc34359f03fff0f58221256e650d1 |
| PATHOLOGIE1 (owned_files.A41_pop1.html) | A41_pop1.html | cee042353cb59c71dae361e59eaefccd7c3fb089f7450757c166bc7bf146778e | cdb1671a68f9f87d78b468c57b958cf894ada46439cd05b29d2b3e2db2645cce |
| CONTRELECTURE_PATHOLOGIE1 (reviewed_file_inventory.A41_pop2.html) | A41_pop2.html | 2e11143b01de68f3628ca9630fe0c674cf123578cf588b94144a75895a2502b1 | e7093e7453ac0fbe9d63aee17094a8a25893e899ebdd8d5936b70ddc10fbedc0 |
| CONTRELECTURE_PATHOLOGIE1 (reviewed_file_inventory.A41_b.html) | A41_b.html | f984a8a7d5ec710460aa248823ae633f77e4f6a8876884982ccb53d6429f4c48 | b3955084555b603f56f905cdaf54407f1c06603bde38dc80930776e5860c1ace |
| CONTRELECTURE_PATHOLOGIE1 (reviewed_file_inventory.A41_pop_pa.html) | A41_pop_pa.html | e9b464ba7bf3f371e64cde359906ded7037165211cf8b5d77e9de533d241a13f | f383ad214398215420af0474e35d53478a6688bbfea14721ff3c8c9bba1e560d |
| CONTRELECTURE_PATHOLOGIE2 (final_sources_reviewed.A41_b.html) | A41_b.html | f984a8a7d5ec710460aa248823ae633f77e4f6a8876884982ccb53d6429f4c48 | b3955084555b603f56f905cdaf54407f1c06603bde38dc80930776e5860c1ace |
| CONTRELECTURE_PATHOLOGIE2 (final_sources_reviewed.A41_pop_pa.html) | A41_pop_pa.html | e9b464ba7bf3f371e64cde359906ded7037165211cf8b5d77e9de533d241a13f | f383ad214398215420af0474e35d53478a6688bbfea14721ff3c8c9bba1e560d |

Le rapport technique et les recherches complémentaires de normes sont référencés avec leur état à la capture ; ils ne ferment aucune réserve et ne créent aucun ID.

## Vérification documentaire

Contrôles : égalité exacte des 75 IDs avec BASE_ET_OBSERVATIONS ; unicité ; audit, index et gravité d’origine conservés ; 76 fiches auteurs ramenées à 75 IDs ; sept dépendances P1 non comptées comme nouveaux IDs ; auteur/fichiers/preuves présents par ligne ; totaux recomptés ; zéro clôture externe Claude. Aucun ID sans disposition.

Cette agrégation écrit seulement les deux fichiers SYNTHESE_75_OBSERVATIONS ; aucune source ni commande Git modifiée/exécutée par l’agrégation. Les deltas auteur et leurs contrelectures sont des opérations distinctes, conservées dans leurs rapports. Aucun nouveau test d’interface ni avis médical autonome revendiqué.
