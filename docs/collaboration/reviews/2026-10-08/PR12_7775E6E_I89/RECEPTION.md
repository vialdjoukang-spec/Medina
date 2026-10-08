# Réception Claude — I89 à la tête 7775e6e

Date : 8 octobre 2026  
Dépôt : `vialdjoukang-spec/Medina`  
PR : [#12](https://github.com/vialdjoukang-spec/Medina/pull/12)  
Branche : `claude/loving-shannon-spwrhc`  
Tête reçue : `7775e6e1544ca7753946921d3ec61a7dd45d1c65`  
Baseline déclarée et `main` contrôlé : `918ef69a8526bf0be38ffdf4f88438ad61d9a8a7`

## Décision

| Stade | État |
| --- | --- |
| Repéré | Oui |
| Reçu | Oui |
| Originaux archivés | Oui — 24 blobs inchangés |
| Intégré | Non |
| Contrôlé techniquement de manière indépendante | Non |
| Publié dans les sources canoniques / le site | Non |
| Publication de cette itération | Documentation de réception uniquement |

Le paquet est complet, sa provenance Claude est établie par la branche, le signal, le manifeste et le rapport. L’empreinte Git agrégée des 24 originaux est `cc9f0b6739915a1207d98c20b1939ef33c7fd33a`; l’arbre d’archive avec `PROVENANCE.json` est `3f657b535917ee5008a11435735ff1641fc444f9`.

## Périmètre et intégrité

Le lot propose **I89 — Autres atteintes non infectieuses des vaisseaux et des ganglions lymphatiques** pour **C-01-Cardiologie / S01**, avec couverture déclarée I89/I97. Les 11 empreintes SHA-256 de proposition sont exactes. Les deux remplacements concordent avec leur baseline : `chapters.json` (`9458acf…`) et `tests/verify_s01_browser.cjs` (`dfcf619…`). Les neuf ajouts — huit HTML et `glossary/i89.py` — sont absents de la baseline, comme déclaré. Le diff porte exactement sur ces 11 cibles (+1053/−1).

Aucune attribution, aucun chapitre actif, aucune route canonique et aucune source canonique n’est modifié par cette réception. Les cadres restent distincts et inchangés : campagne historique de 30 cours (15/15), backlog cardiologique de 20 cours (10/10), 21 fragments (11 Claude / 10 Codex).

## Blocage de chaîne

La règle courante impose un seul chapitre actif par producteur et exige de terminer, relire, contrôler, intégrer et publier le chapitre avant le suivant. Or I83-HARMONISATION-5 est médicalement accepté mais reste en attente d’injection et de publication. Le passage à I89 n’est donc pas autorisé sans clôture effective d’I83 ou dérogation explicite du propriétaire. Ce blocage suffit à interdire l’injection I89.

## Contre-lecture médicale ciblée

Verdict : **non intégrable médicalement à ce stade**. Cette revue est ciblée et ne constitue pas une certification exhaustive.

Réserves bloquantes :

1. **Octréotide dans le chylothorax.** Les doses actionnables (50 µg SC toutes les 8 h, 0,5 µg/kg/h chez l’enfant, arrêt après 1–2 semaines sans réponse) reposent dans le lot sur une revue secondaire et un domaine sans consensus. [DailyMed](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=4e2c9856-1836-49f0-9472-4dbeeb408f39) confirme les indications, risques et interactions, mais pas ces posologies hors indication. Une source primaire ou un protocole spécialisé est requis, sinon la dose doit être retirée.
2. **Vert d’indocyanine / Verdye en Suisse.** Le texte combine SwissPAR 2023, notice australienne et AWMF 2017 pour le statut hors indication, la disponibilité, l’iodure, les contre-indications thyroïdiennes et le délai avant test thyroïdien. L’information professionnelle suisse actuelle et la disponibilité suisse 2026 n’ont pas été vérifiées : il faut les contrôler ou limiter explicitement la juridiction partout.
3. **Mécanismes présentés comme établis sans primaire contre-lue.** Myxœdème–glycosaminoglycanes, territoires du conduit lymphatique droit, rôle valvulaire FOXC2/PIEZO1, rétention sodée sous AINS/corticoïdes/minoxidil et mécanisme PBP/peptidoglycane de la pénicilline doivent être sourcés au niveau requis ou clairement qualifiés comme notions de manuel non contre-lues.

Points ciblés levés ou rectifiés :

- [Thomas et al., NEJM 2013](https://www.nejm.org/doi/full/10.1056/NEJMoa1206300) soutient pénicilline V 250 mg deux fois/jour pendant 12 mois pour la jambe ; l’extrapolation au bras reste explicitement une extrapolation.
- L’[information EMA de Rapamune](https://www.ema.europa.eu/en/documents/product-information/rapamune-epar-product-information_en.pdf) soutient 2 mg/j, une cible résiduelle de 5–15 ng/mL et un premier contrôle à 10–20 jours dans la lymphangioléiomyomatose.
- L’[information EMA de Lyrica](https://www.ema.europa.eu/en/documents/product-information/lyrica-epar-product-information_en.pdf) classe l’œdème périphérique comme fréquent ; aucune dose de prégabaline n’est proposée dans les sources I89. Le manifeste doit corriger cette formulation.

Les vérifications Claude conservent aussi des limites non levées : divergence ISL/AWMF sur le diagnostic précoce, seuils non sourcés des signaux d’alarme, plusieurs notions cliniques dites classiques sans primaire, nomenclature A46/B74/I88/R59 non arbitrée, doublons possibles de glossaire et dépassement des cibles de longueur.

## Contrôles techniques

Contrôles producteurs archivés, non attribués à Codex :

- construction annoncée de 22 fragments ;
- 118 tests unitaires annoncés réussis ;
- contrôle natif I89 : 2 595 assertions, zéro échec/erreur, Chromium ordinateur 1360×900 et mobile 390×844, 43 modèles, 94 déclencheurs directs et 17 imbriqués ;
- contrôle S01 : 73 réussites, zéro erreur ;
- audits statiques I89 et non-régression I83 annoncés réussis.

Contre-lecture technique indépendante : chemins, périmètre du diff, empreintes, opérations add/replace et baseline conformes. En revanche, le workspace de cette itération ne contient ni dépôt local, ni `tools/livraison.py`, ni runtime de construction/tests, ni navigateur. Aucun apply, test unitaire, audit statique du canonique, rebuild, parcours ordinateur/mobile, contrôle de console ou débordement n’a donc été exécuté indépendamment. La création I89 relève de la voie branche/PR et devra être adaptée sélectivement sur un `main` frais ; les deux fichiers partagés ne doivent jamais être écrasés aveuglément.

## Conditions avant une future intégration

1. Clore I83 par intégration et publication, ou consigner une dérogation explicite.
2. Lever les réserves médicales ci-dessus et corriger la mention prégabaline du manifeste.
3. Recontrôler la tête de `main`, les collisions, les chemins et les empreintes.
4. Appliquer les 11 changements sélectivement dans les sources canoniques consommées.
5. Reconstruire les plateformes affectées et exécuter tests, audits statiques et vérification navigateur ordinateur/mobile, y compris fenêtres, mots cliquables, navigation, débordements et console.
6. Émettre un reçu d’intégration distinct et vérifier CI puis déploiement avant toute annonce de publication.

Le catalogue demeure CIM-10 ; aucune complétude CIM-11 n’est certifiée.
