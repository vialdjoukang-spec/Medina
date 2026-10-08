# J45 — Asthme (P-02-Pneumologie) : corrections 1b (information professionnelle suisse)

L'information suisse a été lue avec `tools/compendium_fi.cjs`, le 08.10.2026. Toutes les URL ont la forme `compendium.ch/fr/product/<id>/mpro`.

| Produit (id) | Contenu suisse lu | Passages modifiés |
|---|---|---|
| Symbicort 100/6 Turbuhaler (93068), juin 2023 | MART dès 6 ans avec le 100/6 ; maximum transitoire de 12 inhalations par jour chez l'adulte, 8 chez l'enfant ; au plus 6 inhalations à la fois (4 chez l'enfant) ; AIR non décrit | d 3.2, pop3 `j45-d-icsf`, nouvelle fenêtre `j45-d-mart-ch` |
| Foster 100/6 (1384292), février 2026 | Dès 18 ans ; MART limité à 8 inhalations par jour ; le 200/6 sert à l'entretien seul | b (piège MART), d 3.2, fenêtre |
| Spiromax 160/4,5 (1680407) | MART dès 12 ans, au plus 6 à la fois, 8 par jour en général, 12 au maximum | fenêtre |
| Vannair 100/6 (1098353) | Entretien seul | fenêtre |
| Atrovent sol. 250 µg/2 mL (2600), octobre 2024 | Dans l'asthme, seulement associé à d'autres bronchodilatateurs pour la crise ; aucune dose propre à la crise d'asthme ; 100 à 250 µg de 6 à 12 ans ; 2 mg par jour au plus (paragraphe BPCO) | b (ipratropium, lien vers la fiche), pop3 `j45-d-ipra` |
| Singulair (99446), octobre 2023 | Mêmes doses que l'étiquetage américain, plus 4 mg en granulés de 6 mois à 2 ans | d tableau 3.3, pop3 `j45-d-ltra` |
| Trimbow 172/5/9 (1514226), mai 2025 | Asthme de l'adulte non contrôlé par l'association bêta-2 de longue durée et corticostéroïde inhalé ; 2 inhalations deux fois par jour, qui sont aussi la dose maximale | d 3.3, pop3 `j45-d-lama` |
| Spiriva Respimat (1413224), mars 2020 | BPCO seule ; non étudié avant 18 ans | d 3.3, pop3 |
| Xolair, Nucala, Fasenra, Cinqaero, Dupixent, Tezspire | Prescription réservée à des médecins expérimentés (pas pour Xolair) ; Xolair : IgE < 76 UI/mL implique une sensibilisation perannuelle ; mention « LS (LIM) » pour Xolair, Nucala, Fasenra, Dupixent et Tezspire | b, d 6.2, pop3 `j45-d-bio` |

**Règle du contentieux.** Le texte principal garde GINA 2026, le référentiel le plus récent, et donne en une phrase la contrainte suisse qui diverge : Foster, 8 par jour dès 18 ans. Le détail par produit et l'étiquetage britannique passent dans la nouvelle fenêtre `j45-d-mart-ch` (pop3), ouverte par des boutons dans b et d. La dose d'ipratropium de GINA reste celle du texte ; l'information suisse est placée dans la fiche.

**Mannitol.** La recherche « Aridol » renvoie Meridol, et « mannitol inhalation » renvoie Nasobol : aucune information suisse sur ce test n'a été trouvée. La baisse de 10 % entre deux doses et la dose cumulée de 635 mg sont retirées (c, tableau 3.2 ; pop2). Seul le seuil GINA de 15 % reste (encadré 1-2).

**Remboursement.** Le texte de la limitation ne figure pas dans l'information professionnelle. Le cours renvoie donc à la liste des spécialités de l'OFSP en vigueur, et signale la mention de limitation vue sur compendium.ch.

**Contrôles.** Sigles : `{}`. Le nom commercial « DuoResp » était refusé comme sigle : il est devenu « budésonide-formotérol Spiromax ». Contrôle statique : OK, avec 38 410 mots, 47 fenêtres, 8 quiz et 8 Pareto. Justifications : 15/15. Plus aucune occurrence de « à vérifier dans l'information professionnelle », de « non consultée », de « 635 » ni de « 10 % entre ».

**Hors périmètre.** Le reslizumab porte la mention « hc 03/26 », probablement hors commerce, mais ce n'est pas confirmé. Le glossaire `PD20` reste inutilisé.
