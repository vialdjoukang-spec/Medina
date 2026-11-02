# Préparation Néphrologie — N04, sans rédaction de cours

Base lue : `8a512893acbab9caa0dcfdd0e8682a44ea72fda6`. Préparation du 2026-11-02T01:16:51.601917+00:00. Aucun cours, image, mission, registre, commit ni PR modifié.

**Premier chapitre : N04 — Syndrome néphrotique (N-07-Néphrologie).** Existant attribué à Codex ; aucune réservation active N04 dans le snapshot commun. N17 demeure réservé et non touché. Le choix suit l’ordre actuel de spécialités parallèles et une leçon à la fois, qui remplace les lots historiques sans annuler les réservations.

## Inventaire et limites

Le plan conservatoire S04 contient 33 cibles : 6 existantes et 27 nouvelles. Codex en possède 16 (3 existantes, 13 nouvelles) ; Claude 17 (3 existantes, 14 nouvelles). La campagne Alpha77 ne comprend que 9 cibles S04 Codex. Ce périmètre éditorial n’est ni une liste fédérale officielle ni une validation clinique.

N04 : 6 HTML (249809 octets), 1 glossaire, 5 ressources locales ; dossier hérité : 16 entrées sources, 22 entrées FI et 113 assertions enregistrées. Ces comptes décrivent les fichiers, pas une vérification actuelle des assertions. Tokens et coût réels : inconnus, valeurs JSON null.

## File propre

| Ordre | Leçon | Type | État |
|---|---|---|---|
| 1 | N04 — Syndrome néphrotique | existing_review | selected_pending_harness_gate |
| 2 | N29 — Autres affections du rein et de l’uretère au cours de maladies classées ailleurs | existing_review | queued_after_previous_closure |
| 3 | N17 — Insuffisance rénale aiguë | existing_review | reserved_do_not_touch |
| 4 | N00 — Syndrome néphritique aigu | new_lesson | queued_after_previous_closure |
| 5 | C64 — Tumeur maligne du rein, à l’exception du bassinet | new_lesson | queued_after_previous_closure |
| 6 | N02 — Hématurie récidivante et persistante | new_lesson | queued_after_previous_closure |
| 7 | N03 — Syndrome néphritique chronique | new_lesson | queued_after_previous_closure |
| 8 | N05 — Syndrome néphritique, sans précision | new_lesson | queued_after_previous_closure |
| 9 | N06 — Protéinurie isolée avec lésions morphologiques précisées | new_lesson | queued_after_previous_closure |
| 10 | N07 — Néphropathie héréditaire, non classée ailleurs | new_lesson | backlog_not_in_77_campaign |
| 11 | N10 — Néphrite tubulo-interstitielle aiguë | new_lesson | backlog_not_in_77_campaign |
| 12 | N11 — Néphrite tubulo-interstitielle chronique | new_lesson | backlog_not_in_77_campaign |
| 13 | N14 — Atteintes tubulo-interstitielles et tubulaires dues à des médicaments et des métaux lourds | new_lesson | backlog_not_in_77_campaign |
| 14 | Q60 — Agénésie rénale et autres défauts de développement rénal | new_lesson | backlog_not_in_77_campaign |
| 15 | Q61 — Maladies kystiques du rein | new_lesson | backlog_not_in_77_campaign |
| 16 | S37 — Lésion traumatique des organes pelviens et urinaires | new_lesson | backlog_not_in_77_campaign |

Les 7 productions Codex hors campagne77 restent en backlog, sans lancement implicite. Les 17 cibles Claude restent en lecture seule. La liste complète et leurs réservations sont dans brief.json.

## Mission et chemins

Manifeste : `.medina/missions/ALPHA77-CODEX-N04-INTEGRATE.json`, actif génération1, ancienne base `8712c3fe758f0c7e1f9fb85378def47b554edb53`. Branche prévue `codex/alpha77/n04-integrate-g1`. Aucune acquisition/start réalisée. Le parent fournit une mission/base/génération cohérentes et le worktree exclusif après la porte harness.

- `chapters/N04`
- `glossary/n04.py`
- `assets/img/n04/alpha/codex`
- `organisation/alpha-publications/Codex/N04`
- `docs/collaboration/ssp-v2/execution/ALPHA77-CODEX-N04-INTEGRATE`

## Constats préliminaires, non audit médical

- Sémiologie fondamentale absente : quatre sous-onglets scientifiques, aucun marqueur sémiologique. L’exigence du15octobre est MAJEURE et locale à N04.
- Figures1 et8 : schémas SVG de structures anatomiques. Vérifier la provenance avant qualification ; le format seul ne démontre pas une origine IA. Figures2/4/5/6/7 : images existantes ; chaque licence propre et attribution doivent être recontrôlées.
- Le codage CIM est placé dans A02 ; conserver la monographie clinique et déplacer les métadonnées au besoin sans perdre les sous-codes.
- Les affirmations héritées et anciennes déclarations « conforme » ne remplacent pas une relecture actuelle des passages ni un audit indépendant.

## Qualité minimale

- Aucun fait médical issu de la seule mémoire du modèle ; assertion reliée à un passage effectivement lu, daté, avec population et limites.
- Sources suisses applicables puis européennes ; KDIGO seulement avec applicabilité motivée ; aucune recommandation américaine décisionnelle.
- Chaque médicament : FI suisse produit exact, date, dose, voie, fréquence, durée, maximum, adaptations, contre-indications et interactions ; hors indication explicite.
- Matrice de complétude à 20 rubriques et porte betta_verite avant rédaction ; lacunes visibles sans validation fabriquée.
- Quatre onglets et plan monographique clinique ; sémiologie clinique dans pA, sous-onglet Sémiologie fondamentale et analytique en premier dans pS, neuf sections substantielles.
- Fondamentales : normal puis mécanisme, conséquence clinique et décision ; paramètres avec unité, population, méthode, intervalle suisse applicable ; calculs explicités et cliquables.
- Figures anatomiques originales humaines avec droits propres, attribution, provenance et revue visuelle ; aucun dessin anatomique IA, SVG inclus.
- Contrôle de toutes les surfaces, navigation réelle ordinateur/mobile390, fenêtres, Livre et police agrandie ; captures réelles.
- Audits et preuves liés aux empreintes finales ; distinguer relu, corrigé, testé, publié et validé médicalement.

## Plan monographique à conserver ou améliorer

1. Question clinique et objectifs
2. Définition, critères et classifications
3. Épidémiologie suisse puis européenne et pronostic
4. Physiopathologie depuis le fonctionnement normal
5. Étiologies et facteurs de risque
6. Anamnèse et sémiologie clinique analytique
7. Examen clinique : technique, interprétation, limites
8. Démarche diagnostique et différentiels
9. Urgences et complications
10. Prise en charge causale et traitement de soutien
11. Surveillance, récupération, prévention et suivi
12. Situations particulières : enfant, grossesse, âgé, comorbidités
13. Références, lacunes explicites et métadonnées CIM après la conclusion clinique

Les onglets Examens, Sciences fondamentales et Pharmacologie portent les développements ciblés ; les fenêtres approfondissent les mots cliquables sans isoler artificiellement les décisions du raisonnement clinique.

## Preuves à relire

- `livraisons/Livraison Claude/N-07-Néphrologie/travail/CYCLE_03_N04/preuves/dossier_sources.json`
- `livraisons/Livraison Claude/N-07-Néphrologie/travail/CYCLE_03_N04/preuves/source_ledger_claude.json`
- `livraisons/Livraison Claude/N-07-Néphrologie/travail/CYCLE_03_N04/preuves/contexte_suisse_claude.json`
- `livraisons/Livraison Claude/N-07-Néphrologie/travail/CYCLE_03_N04/preuves/contexte_suisse_controle.json`
- `livraisons/Livraison Claude/N-07-Néphrologie/travail/CYCLE_03_N04/preuves/images_claude.json`
- `livraisons/Livraison Claude/N-07-Néphrologie/travail/CYCLE_03_N04/assets/img/cycle3/n04/ATTRIBUTIONS.json`

Commencer par les passages suisses réutilisables du dossier, puis ouvrir les sources primaires ciblées. Les sources héritées ne sont pas toutes attestées comme relues dans cette préparation.

- https://catalogue.chuv.ch/analyses-examens/laboratoires/fiche/download/DLA_INV_01_00380?no_cache=1
- https://kdigo.org/wp-content/uploads/2017/02/KDIGO-Glomerular-Diseases-Guideline-2021-English.pdf
- https://kdigo.org/wp-content/uploads/2025/04/KDIGO-2025-Guideline-for-Nephrotic-Syndrome-in-Children.pdf
- https://www.bag.admin.ch/dam/fr/sd-web/Oj0BSN-w-Ggs/Plan%20de%20vaccination%20suisse_2026_FR_Web_final.pdf
- https://www.infovac.ch/docs/public/streptococcus/ofsp-cfv-prise-de-position-recommandation-des-pcv-par-groupe-cible-e--tat-au-01-07-26-fr.pdf
- https://www.revmed.ch/revue-medicale-suisse/2022/revue-medicale-suisse-771/syndrome-nephrotique-de-l-adulte-et-autres-proteinuries-de-fort-debit
- https://www.swissnephrology.ch/wp/wp-content/uploads/2025/03/Version-2025_Francais_V_17.03.2025_WZ.pdf

Pour les 21 URL FI du chapitre, relire le produit exact et la date actuelle ; contrôler chaque modalité présente, y compris le statut hors indication. Figures : consulter pages originales, auteur, licence propre, original visuel et légende ; ImageFinder ne certifie rien à lui seul.

## Outils et contrôles réutilisables

- `tools/betta_verite.py`
- `tools/swissmedic_fi.py`
- `tools/image_codex_finder.py`
- `tools/ai_session_guard.py`
- `tools/alpha_publication.py`
- `tests/audit_sciences.py`
- `test_v7.py`
- `tools/capture_lecon.py`
- `tools/starter_codex.py`
- `tests/test_starter_codex.py`
- `tests/test_image_codex_finder.py`
- `tests/test_audit_sciences.py`

Modèle de forme : `chapters/I50/`, cardiologie en lecture seule. Aucun fait médical ou schéma du modèle ne doit être copié comme preuve. Contrats : `docs/collaboration/betta/PROMPT_VERITE.md`, `docs/collaboration/instructions/SEMIOLOGIE_FONDAMENTALE_ANALYTIQUE_2026-10-15.yaml`, `docs/collaboration/instructions/IMAGE_CODEX_FINDER.md`.

## Porte avant cours

1. Harness et tests réussis et veille fonctionnelle prouvée par parent
2. Réservation vérifiée à nouveau, mission/base/génération alignées et worktree exclusif
3. Recherche N04 traçable et porte de vérité avant tout cours

Aucun test clinique, navigateur ou contrôle de publication N04 exécuté par cet agent à ce stade ; aucune note ni clôture annoncée.
