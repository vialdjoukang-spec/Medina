# J45 — Asthme (P-02-Pneumologie) : corrections après réception Codex no 1 (J45-MED-01, J45-MED-02)

## Tentatives d'accès
- **ERS 2017 (Coates, DOI 10.1183/13993003.01526-2016)** : Europe PMC renvoie PMID 28461290, sans PMCID et sans accès ouvert (le texte intégral XML renvoie 404). PubMed `convert_article_ids` ne donne pas de PMCID. Le site ERJ, publications.ersnet.org et doi.org renvoient 403 (blocage Cloudflare). **Texte intégral non lu.**
- **Suisse** : swissmedicinfo.ch et la liste des spécialités (spezialitaetenliste.ch, redirigée vers sl.bag.admin.ch) ne servent qu'une coquille JavaScript, et l'export XML ne renvoie que du HTML. Sur compendium.ch, l'information professionnelle exige une connexion. **Aucune information professionnelle ni limitation consultée.**

## Méthacholine (retrait faute de texte intégral)
- `J45_c.html`, tableau 3.2 : « PD20 < 400 µg ; 100–400 µg zone limite (ERS 2017) » devient « chute du VEMS ≥ 20 % aux doses standard (GINA 2026, encadré 1-2) ; catégories de dose : norme ERS 2017, non relue ici ».
- `J45_pop2.html` `j45-metha` : la phrase sur la PD20 et les cinq catégories est supprimée. Le texte garde le critère GINA (encadré 1-2, p. 28) et renvoie à l'ERS 2017, non relue. Les contre-indications (VEMS < 60 %/1,5 L, infarctus/AVC < 3 mois, HTA, anévrisme) sont retirées : il reste la grossesse, que GINA 2026 contre-indique (p. 37), et un renvoi à l'ERS 2017.
- `J45_pop4.html` (Pareto examens) : « PD20 < 400 µg ; 100–400 µg » devient « positive si le VEMS chute d'au moins 20 % aux doses standard ».
- `J45_b.html` : « GINA déconseille » devient « contre-indique (p. 37) », conformément au texte. `J45_pop1.html` : l'ERS 2017 porte désormais la mention « citée, texte intégral non relu ».
- Le grep ne trouve plus aucune occurrence de PD20, de catégorie de dose ni de l'ancienne liste de contre-indications.

## Affirmations suisses
Chaque affirmation sur une autorisation est maintenant attribuée à la « liste Swissmedic des conditionnements autorisés (état au 30 septembre 2026) » : ipratropium et Berodual N (b, d, pop3), budésonide-salbutamol, Symbicort 200/6 contre 160/4,5, Spiriva Respimat, Trimbow, aminophylline et dépémokimab. Cette source a aussi été ajoutée aux références de b et de pop3 (biothérapies).

Les limites MART, la posologie de l'ipratropium et celle du montélukast sont reformulées : « à vérifier dans l'information professionnelle suisse en vigueur ». Les affirmations sur le remboursement des biothérapies et la prescription par un pneumologue (b:129, d:155) deviennent « à vérifier dans l'information professionnelle suisse et la liste des spécialités de l'OFSP en vigueur ».

## Contrôles
- `verifier_sigles.py J45` : `{}`
- `test_v7.py --static J45` : OK (37 503 mots, 46 fenêtres, 8 quiz, 8 Pareto)
- `insert_justifications.py` : 15/15
- J45_a.html et J45_justifications.json non modifiés.

## Réserves restantes (hors périmètre)
- Le glossaire `glossary/j45.py` garde l'entrée PD20, définie comme « dose cumulée », alors que l'ancien texte parlait de dose non cumulée. Cette entrée n'est plus employée dans le HTML et le fichier n'est pas modifiable ici.
- Dans `j45-metha` et `J45_c.html`, deux critères du mannitol ne viennent pas de GINA, qui ne donne que ≥ 15 % : la baisse de 10 % entre deux doses et la dose cumulée de 635 mg. Leur source, l'ERS 2018 (Hallstrand), n'a pas été relue.
- La Suva et la LAA (art. 9) ne sont pas touchées : elles restent citées par leur texte légal.
