# Dossier d’injection finale I89-3 — tentative arrêtée

**I89 — Autres atteintes non infectieuses des vaisseaux et des ganglions lymphatiques (C-01-Cardiologie) reste non injecté : le contrôle obligatoire `check-claude` échoue réellement.** Les empreintes et la provenance sont conformes, mais ce résultat ne remplace pas une condition obligatoire. Aucun contournement, nouvelle production ni injection par ce poste.

## Lot exact et bases

Source Claude : `04cb95729d44648cc65339f28cf6631574babbb2`. Base du lot : `f204b06ac174d41632b742ec6b82097b1532b2c8`. Archive immuable sur main : commit `a3b8ac4060529aaf339f17851305c07abac25cc8`. Snapshot canonique demandé : `61a841b3c96b3bd4f3ad58ec5870d06945e63292` ; HEAD locale ultérieure `5f04f5d950f742ec8848795bc048822d566640c5`. Le delta entre ces deux derniers états est vide sur les sources applicatives sélectionnées et les deux cibles remplacées.

Racine exacte du lot :

```text
/workspace/Medina/livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_PR12_04CB957_I89_3/livraisons/Livraison Claude/C-01-Cardiologie/lots/2026-10-08-I89-3
```

Manifeste : `livraison.json`, SHA256 `7473feb52e8f3fd2e90ea36f01089f932363cfb8dd89693cb1fe30ff11d808ea`. Les chemins absolus et chaque SHA sont fournis dans [DOSSIER_INJECTION.json](DOSSIER_INJECTION.json), et ont été transmis à la sentinelle technique.

## Onze propositions et deux empreintes de base

| Cible canonique | Opération annoncée | Source relative au lot | Vérification |
| --- | --- | --- | --- |
| chapters.json | replace | sources/chapters.json | conforme |
| chapters/I89/I89_a.html | add | sources/chapters/I89/I89_a.html | conforme |
| chapters/I89/I89_b.html | add | sources/chapters/I89/I89_b.html | conforme |
| chapters/I89/I89_c.html | add | sources/chapters/I89/I89_c.html | conforme |
| chapters/I89/I89_d.html | add | sources/chapters/I89/I89_d.html | conforme |
| chapters/I89/I89_pop1.html | add | sources/chapters/I89/I89_pop1.html | conforme |
| chapters/I89/I89_pop2.html | add | sources/chapters/I89/I89_pop2.html | conforme |
| chapters/I89/I89_pop3.html | add | sources/chapters/I89/I89_pop3.html | conforme |
| chapters/I89/I89_pop4.html | add | sources/chapters/I89/I89_pop4.html | conforme |
| glossary/i89.py | add | sources/glossary/i89.py | conforme |
| tests/verify_s01_browser.cjs | replace | sources/tests/verify_s01_browser.cjs | conforme |

**11/11 propositions** sont conformes au manifeste et identiques aux octets du SHA source exact. **18/18 blobs** de l’archive correspondent à `PROVENANCE.json`. Les **neuf ajouts** sont absents sur la base producteur, le snapshot et HEAD locale. Les **deux remplacements** conservent leurs empreintes originales sur ces trois états : aucun conflit ni base de fichier périmée.

## Portée consommée

Le registre proposé ajoute uniquement un cours : I89, après I83, portant `covers: ["I89", "I97"]`. Toutes les autres entrées sont identiques. L’inventaire global passerait de **32 à 33 cours**, et le seul consommateur direct, **C-01-Cardiologie**, de **21 à 22 cours** selon le prédicat statique de `build_front.fragment_chapters`. Aucun transfert d’attribution. Le seul changement du test S01 est son attente de 21 à 22 ; aucune assertion spécifique supplémentaire pour les sous-catégories n’est ajoutée.

Les catégories restent sous leur fragment : I89 — Autres atteintes non infectieuses des vaisseaux et des ganglions lymphatiques (C-01-Cardiologie) est le cours primaire. Le rattachement déclaré concerne aussi I97 — Troubles de l’appareil circulatoire après des actes médicaux, non classés ailleurs (C-01-Cardiologie), en particulier les lymphœdèmes après actes médicaux ; il ne certifie pas toute cette catégorie. I88 — Lymphadénite non spécifique (C-01-Cardiologie) est seulement articulée, sans couverture annoncée. Aucune complétude CIM-11.

## Réception médicale et limites conservées

Le reçu I89-3 lève les deux blocages ciblés de la version précédente. Il reste une contrelecture du delta, sans validation exhaustive du cours. Les anciennes pièces de revue interne, plan, deux vérificateurs et rapport du lot initial existent dans le SHA source ; leurs chemins et empreintes sont conservés dans le JSON. Les changements v2/v3 sont documentés dans les rapports correspondants.

Le reçu historique indique que les informations médicamenteuses du delta sont américaines et que l’information suisse de Verdye et sa disponibilité 2026 n’y étaient pas vérifiées. La sentinelle médicale a depuis relu le SwissPAR et la FI suisse, sans établir la disponibilité commerciale : voir [l’audit final daté](AUDIT_MEDICAL_FINAL.md). Lund 1986 est une petite étude lue en résumé, mécanisme présenté comme hypothèse. Glitazones/ENaC et docétaxel n’ont pas été relus dans le delta. Ces limites ne deviennent pas des validations parce que le reçu ne porte plus de blocage médical ciblé.

## Blocage technique exécuté

La sentinelle technique a exécuté le checker de confiance sur une copie isolée de main `61a841b3c96b3bd4f3ad58ec5870d06945e63292`. Résultat : **code 2**, avant tout overlay :

```text
Livraison interrompue : Code ou titre de cours incohérent : {'code': 'I89', 'title': 'Autres atteintes non infectieuses des vaisseaux et des ganglions lymphatiques', 'covers': ['I89', 'I97'], 'owner_fragment': 'S01'}
```

Le catalogue du checker ne contient que les cours déjà intégrés : le nouveau code est rejeté avant validation des fichiers. Ce message générique ne démontre pas une erreur médicale de titre, une fausse empreinte ou une mauvaise attribution. Le code lu limiterait ensuite les chemins au contenu `chapters/<code>/<fichier>` ; registre, glossaire et test du lot sont hors de son contrat actuel. Ce second obstacle est une lecture de code, pas un autre contrôle exécuté.

Les [règles d’injection](../../../REGLES_INJECTION_CLAUDE.md) exigent `check-claude` conforme. La condition échouée interdit de qualifier le lot d’admissible maintenant. Aucun manifeste, catalogue ou checker n’est modifié pour contourner ce refus. Les annonces historiques du producteur (2 595 contrôles natifs, 73 S01, 118 tests) ne sont pas des contrôles actuels reproduits par ce poste. La tentative est arrêtée sans build ni injection ; voir [CONTROLE_TECHNIQUE.md](CONTROLE_TECHNIQUE.md).

J45 — Asthme (P-02-Pneumologie) est exclu pour J45-MED-03. A41 — Sepsis et choc septique de l’adulte (I-03-Infectiologie) est exclu pour ESP03 et contre-audit Claude ouverts. Aucune file d’audit modifiée pour une injection qui n’a pas eu lieu. Constat daté : 2026-10-08T13:48:17.067761+00:00 UTC.
