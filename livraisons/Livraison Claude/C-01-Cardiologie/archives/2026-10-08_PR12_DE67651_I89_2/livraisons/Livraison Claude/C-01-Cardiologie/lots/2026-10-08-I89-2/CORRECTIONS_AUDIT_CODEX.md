# I89 — Corrections après l'audit Codex (C-01-Cardiologie), 08.10.2026

Fichiers modifiés : `chapters/I89/I89_c.html`, `I89_d.html`, `I89_pop2.html`, `I89_pop3.html`, `I89_pop4.html`, `glossary/i89.py`. Aucune opération Git.

## Réserve 1 — Octréotide (posologies retirées partout)
- `I89_d.html`, îlot p-4 : « Aucun consensus ne fixe sa dose. » → « …ni sa durée : le centre spécialisé les fixe selon son protocole. »
- `I89_d.html`, tableau des posologies : « Adulte : 50 µg/8 h… arrêt après 1 à 2 semaines » → « Aucune posologie consensuelle : usage hors indication, dose et durée fixées par le protocole du centre spécialisé ».
- `I89_d.html`, « À retenir » p-4 : la dose de 50 µg est retirée. Le texte dit maintenant « hors indication et sans consensus ; le centre spécialisé fixe la dose et la durée ».
- `I89_d.html`, surveillance p-6 : « arrête après une à deux semaines » → « durée de l'essai et critère d'arrêt selon le protocole du centre spécialisé ».
- `I89_pop4.html`, fenêtre `i89-d-octreotide` : la réponse directe ne donne plus de dose et précise l'usage hors indication, sans consensus. La dose pédiatrique de 0,5 µg/kg/h est supprimée. Les effets indésirables sont maintenant attribués à « l'information professionnelle américaine ».
- `I89_pop4.html`, Pareto Pharmacologie : la dose de 50 µg est retirée.
- Contrôle : aucune mention « µg » ni « 1 à 2 semaines » ne reste dans le cours. Les indications américaines, les risques et les interactions sont conservés.

## Réserve 2 — Vert d'indocyanine / Verdye
Sources consultées le 08.10.2026 :
- swissmedicinfo.ch et compendium.ch : **inaccessibles** (application vide ; connexion requise).
- Résumé public SwissPAR de Swissmedic (29.06.2023) : **lu**. Il confirme l'autorisation du 24.04.2023, les seules indications cardiaques et circulatoires, hépatiques et ophtalmologiques, et l'absence d'information professionnelle suisse à cette date.
- Avis Swissmedic « out of stock » du 10.07.2023 : **lu**. Il autorise pour une durée limitée la distribution d'une présentation allemande. Cette donnée n'a pas été ajoutée au cours.

Juridiction limitée partout :
- `pop4` (`i89-d-traceurs`) : SwissPAR avec ses dates. Phrase ajoutée : « le statut et la disponibilité suisses actuels se vérifient dans l'information professionnelle suisse en vigueur ». L'iodure, les contre-indications thyroïdiennes, le délai avant le test d'iode et la réinjection sont attribués à l'information australienne, l'érysipèle à l'AWMF 2017 allemande. Ligne Source complétée.
- `I89_d.html`, p-6 et « À retenir », `pop3` (`i89-e-icg`, Limites et Source), Pareto `pop4` : même attribution, au passé pour 2023.

## Réserve 3 — Mécanismes
| Mécanisme | Repère | Appui lu | Accès |
|---|---|---|---|
| Myxœdème et glycosaminoglycanes | `c` (tableau des diagnostics différentiels), `pop2` (`i89-oed-systemique`) | Safer 2011, PubMed 22110782 : dépôt de glycosaminoglycanes, surtout d'acide hyaluronique, et peau qui ne garde pas le godet. « Prend peu le godet » devient « ne garde habituellement pas le godet » ; « corrige cet œdème » devient « traite la cause ». | Texte intégral PMC |
| Conduit lymphatique droit | `c`, anatomie | Kammerer et al. 2016, PubMed 27037010 : la moitié droite du thorax, le bras droit et le côté droit de la tête et du cou se drainent dans le confluent veineux droit. « Plus court » est retiré ; la phrase est qualifiée « selon le schéma anatomique habituel ». | Texte intégral PMC |
| Valvules FOXC2 et PIEZO1 | `c` (Génétique), glossaire PIEZO1 | Petrova et al. 2004, PubMed 15322537 (absence de valvules chez la souris Foxc2−/−) ; Nonomura et al. 2018, PubMed 30482854 (valvules très réduites sans Piezo1 endothélial). La phrase précise maintenant « chez la souris ». | Résumés |
| Rétention sodée | `d` (tableau des œdèmes médicamenteux), `pop4` (`i89-d-oedeme-medic`) | AINS : Kim et Joo 2007, PubMed 24459510 (inhibition des prostaglandines rénales). Minoxidil et hydralazine : Cohn et al. 2011, PubMed 21896152 (baisse de la pression de perfusion rénale, énoncée pour l'hydralazine). Corticoïdes : Liu et al. 2013, PubMed 23947590 (activité minéralocorticoïde, rétention d'eau, minimale avec la dexaméthasone). | Résumés ; Liu en texte intégral, lu partiellement |
| Pénicilline, PBP et peptidoglycane | `pop4` (`i89-d-penicilline`) | Kong et al. 2010, PubMed 20041868 : liaison covalente au site actif, inhibition de la réticulation, lyse. | Texte intégral PMC, lu partiellement |

## Contrôles
- `verifier_sigles.py I89` → `{}`. Une première passe a signalé SwissPAR, APMIS et Dermato-Endocrinology. Ces termes sont maintenant écrits en toutes lettres ou réécrits.
- `test_v7.py --static I89` → **OK** (36 713 mots, 43 fenêtres, 8 quiz, 5 Pareto).
- `glossary/i89.py` : syntaxe Python valide.

## Réserves restantes
- L'information professionnelle suisse actuelle de Verdye et sa disponibilité en 2026 n'ont pas été vérifiées. Le texte est limité à la juridiction de chaque source, sans valider le statut suisse.
- L'information australienne de Verdye n'a pas été relue par moi : son attribution est conservée telle quelle.
- Cohn et al. 2011 énonce le mécanisme rénal pour l'hydralazine ; il est appliqué au minoxidil comme vasodilatateur artériolaire direct de la même revue. Liu et al. 2013 parle de rétention d'« eau » par effet minéralocorticoïde.
- Les autres réserves de Codex sont hors de ce mandat : blocage de chaîne I83, manifeste et prégabaline, ISL/AWMF, seuils d'alarme, nomenclature, longueur.
