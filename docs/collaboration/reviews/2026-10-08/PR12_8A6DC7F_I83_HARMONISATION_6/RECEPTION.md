# Réception PR #12 — I83-HARMONISATION-6 — tête 8a6dc7f

## Décision

- **Repéré : oui.** Origine Claude établie par la branche, le manifeste et le rapport du lot.
- **Reçu : oui.** Treize originaux sont archivés sans modification avec provenance et objets Git exacts.
- **Médicalement recevable : oui, pour le delta ciblé.**
- **Intégré : non.**
- **Contrôlé techniquement de manière indépendante : non.**
- **Publié : documentation de réception seulement.**

## Baseline, empreintes et delta

Le lot remplace `2026-10-08-I83-HARMONISATION-5` et déclare `main` `1c39691289c49cb701345026b5ab9334f5330225` comme baseline. Les sept SHA-256 de propositions de chapitre et leurs sept baselines sont exacts ; le complément `glossary/i83.py` et sa baseline sont exacts. Aucun conflit n'est relevé sur les huit cibles.

Le delta réel depuis HARMONISATION-5 est limité à `I83_c.html`, `I83_pop2.html` et `glossary/i83.py` ; les cinq autres fichiers HTML sont identiques. Les deux réserves mineures v5 sont corrigées : définition/portée des perforantes pathologiques, et rattachement des fréquences d'ARTE/TVP aux ablations thermiques de la grande saphène.

Archive : `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-08_PR12_8A6DC7F_I83_HARMONISATION_6`  
Arbre des originaux : `20a0ff769d7c456303aa6b92d4271d6e58f8ebe1`  
Arbre avec provenance : `a419c5a1d191abd8c03d2f7398dafe59b179a0c9`

## Relecture médicale ciblée

Avis favorable sur le delta : la qualification des perforantes concorde avec ESVS 2022 §§ 2.3.1.1 et 4.6.6 sans transformer cette qualification en indication thérapeutique ; les fréquences de 1,4 % et 1,7 % sont correctement rattachées aux ablations thermiques de la grande saphène. La contre-indication suisse du polidocanol et la conduite de l'ARTE III anticoagulée restent préservées. Aucune règle générale de suivi de toute TVP jusqu'à résolution n'est réintroduite.

Cette décision concerne le delta H5→H6 ; elle ne constitue pas une certification médicale exhaustive du chapitre ni des 30 cours. Restent hors de cette contrelecture : le chiffre de 212 participants pour le cadexomère, les affirmations négatives concernant l’OFSP et toute couverture CIM-11.

## Contrôles techniques et réserve d'intégration

Le contrôle indépendant de réception a recalculé les 16 SHA-256, appliqué le diff en mémoire sans conflit, vérifié 47 templates, 41 identifiants et 85 déclencheurs sans doublon ni référence absente, et validé l'AST du glossaire. Il n'a exécuté ni build ni navigateur.

Le producteur annonce : statique I83 réussi, reconstruction de 22 fragments, 118 tests, 1 923 contrôles natifs sans erreur et 72 contrôles S01. Le JSON natif porte les empreintes H6 et une nouvelle date ; le JSON S01 est byte-identique à H5 et ne lie pas explicitement son build à H6, ce qui en fait une preuve faible pour ce rerun.

Faute de dépôt local, `tools/livraison.py`, reconstruction et navigateur dans ce workspace, aucun de ces contrôles n'a été reproduit. L'intégration et la publication du site sont donc différées ; aucune source canonique n'est modifiée. Lors d'une future injection, il faudra appliquer le paquet cumulatif complet de huit cibles contre main, et non les seules trois différences H5→H6, car H5 a été reçu mais jamais intégré.

## Périmètre

Aucune attribution ni aucun chapitre actif n'est changé. I83 reste le chapitre actif Claude. Restent distincts : campagne historique 30 cours (15/15), backlog cardiologique 20 cours (10/10), 21 fragments (11 Claude / 10 Codex).

## Écart documentaire consigné

Le manifeste classe `glossary/i83.py` parmi les compléments « inchangés depuis HARMONISATION-2 », alors que H6 y ajoute effectivement le qualificatif « thermiques ». Le reçu retient le delta calculé, pas cette description inexacte ; aucune adaptation canonique n'est appliquée dans cette réception.
