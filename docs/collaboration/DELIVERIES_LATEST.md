# MEDINA — livraisons repérées

Branche d'intégration : `codex/sciences-cs-fragments-20261007`.
Commit cible : `f5c83957a239a27b836b838063e97835cd80f4d9`.

Scan : complet selon les données fournies.
Une livraison repérée ou reçue n'est pas présumée intégrée. Une intégration ne prouve pas une vérification.

| Branche / PR | Tête | Reçu | Intégré dans la cible | Vérifié | Routage |
| --- | --- | --- | --- | --- | --- |
| codex/accueil-qcm-20260929 · #6 | `871bb223564d` | Non confirmé | Non démontré | Non démontré | GLOBAL |
| claude/medina-alpha-integration-7dul4i · #1 | `303f95a66dd2` | Oui | Oui, preuve enregistrée | Non démontré | GLOBAL, S01, S02, S07, S10, SYSTEM, T1 |
| claude/review-i48-esc2024-20261007 | `c3770739b58c` | Non confirmé | Oui, preuve enregistrée | Non démontré | À préciser |
| claude/review-medina-global-20261007 · #8 | `f6e400df9e5d` | Oui | Oui, preuve enregistrée | Oui, contrôles enregistrés | CS, GLOBAL, S01 |
| codex/ajouter-options-de-generation-de-fragments · #3 | `1539f4e77171` | Non confirmé | Oui, preuve enregistrée | Non démontré | GLOBAL |
| codex/configurer-publication-github-pages-automatique · #4 | `8d0de9bcd572` | Non confirmé | Oui, preuve enregistrée | Non démontré | GLOBAL |
| codex/creer-fragments.json-et-corrige-des-chemins · #2 | `0f38d9aab4ef` | Non confirmé | Oui, preuve enregistrée | Non démontré | GLOBAL |
| codex/etancheite-complete-des-fragments · #5 | `7071e557cfc2` | Non confirmé | Oui, preuve enregistrée | Non démontré | GLOBAL |
| codex/fragment-s01-accueil-navigo-20261005 · #7 | `c50a28a23d7e` | Non confirmé | Oui, preuve enregistrée | Non démontré | GLOBAL, S01 |
| main | `92b1db11a594` | Non confirmé | Oui, preuve enregistrée | Non démontré | À préciser |

## codex/accueil-qcm-20260929

- PR #6 vise main ; comparaison à la cible MEDINA requise.

| Fichier | Nature | Routage | Diff |
| --- | --- | --- | --- |
| `.github/workflows/pages.yml` | integration_source | GLOBAL | integration_target |
| `CLAUDE.md` | documentation | GLOBAL | integration_target |
| `build_index.py` | integration_source | GLOBAL | integration_target |
| `docs/QCM_MEDINA.md` | documentation | GLOBAL | integration_target |
| `site/index_template.html` | consultation_source | GLOBAL | integration_target |
| `site/qcm.html` | consultation_source | GLOBAL | integration_target |

## claude/medina-alpha-integration-7dul4i

- Chemin sans route de build connue ; examen manuel requis.
- Sortie dérivée ; intégrer les sources puis reconstruire.
- Vérifier titres, covers, activation, rattachements et rubriques après intégration.
- Glossaire global : contrôler les collisions et la définition finale après zz_fusion.py.
- Tracés générés : vérifier modules/ecg.py et régénérer.
- Coque historique et ressources embarquées : contrôler SYSTEM et les fragments séparément.
- PR #1 vise main ; comparaison à la cible MEDINA requise.

| Fichier | Nature | Routage | Diff |
| --- | --- | --- | --- |
| `.claude/commands/audit.md` | documentation | GLOBAL | pull_request_base |
| `.claude/commands/chapitre.md` | documentation | GLOBAL | pull_request_base |
| `.claude/commands/cycle.md` | documentation | GLOBAL | pull_request_base |
| `.claude/commands/fusion-alpha.md` | documentation | GLOBAL | pull_request_base |
| `.claude/commands/livrer.md` | documentation | GLOBAL | pull_request_base |
| `.gitignore` | unknown |  | pull_request_base |
| `CHAPTER_SPEC.md` | documentation | GLOBAL | pull_request_base |
| `CLAUDE.md` | documentation | GLOBAL | pull_request_base |
| `MEDINA_ClaudeCode.zip` | derived |  | pull_request_base |
| `PASSATION_REECRITURE_2026-09-26.md` | documentation | GLOBAL | pull_request_base |
| `PROMPT_MEDINA.md` | documentation | GLOBAL | pull_request_base |
| `PROMPT_REPRISE_IA.md` | documentation | GLOBAL | pull_request_base |
| `README.md` | documentation | GLOBAL | pull_request_base |
| `REPRISE_CLAUDE_CODE.md` | documentation | GLOBAL | pull_request_base |
| `_alpha_in/LISEZMOI.txt` | unknown |  | pull_request_base |
| `_alpha_in/MEDINA_Alpha_26-09-2026.html` | unknown |  | pull_request_base |
| `_alpha_in/MEDINA_Alpha_PASSATION_2026-09-26.md` | documentation | GLOBAL | pull_request_base |
| `_alpha_in/MEDINA_Alpha_TRANSPORT_26-09-2026.zip` | unknown |  | pull_request_base |
| `audits/A41.md` | review_report | T1 | pull_request_base |
| `audits/DESIGN_2026-09-26.md` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_MODERNISATION.md` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/01_accueil_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/01_accueil_pc-sombre.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/01_accueil_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/02_accueil_directeur_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/02_accueil_directeur_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/03_bouton_directeur_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/03_bouton_directeur_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/04_notification_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/04_notification_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/05_specialite_cardiologie_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/05_specialite_cardiologie_pc-sombre.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/05_specialite_cardiologie_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/06_systeme_cardiologie_mobile.png` | review_report | SYSTEM | pull_request_base |
| `audits/FRONT_captures/apres/06_systeme_cardiologie_pc.png` | review_report | SYSTEM | pull_request_base |
| `audits/FRONT_captures/apres/07_entree_cim_plan_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/07_entree_cim_plan_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/08_cours_entete_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/08_cours_entete_pc-sombre.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/08_cours_entete_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/09_cours_ilot_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/09_cours_ilot_pc-sombre.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/09_cours_ilot_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/10_cours_fenetre_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/10_cours_fenetre_pc-sombre.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/10_cours_fenetre_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/11_cours_quiz_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/11_cours_quiz_pc-sombre.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/11_cours_quiz_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/12_cours_pareto_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/12_cours_pareto_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/13_cours_navigo_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/13_cours_navigo_pc-sombre.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/13_cours_navigo_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/14_cours_police_taille_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/14_cours_police_taille_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/15_cours_mode_livre_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/15_cours_mode_livre_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/16_cours_sciences_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/16_cours_sciences_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/17_examen_federal_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/17_examen_federal_pc-sombre.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/17_examen_federal_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/18_carnet_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/18_carnet_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/19_recherche_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/19_recherche_pc-sombre.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/19_recherche_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/20_methode_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/20_methode_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/21_atlas_ecg_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/21_atlas_ecg_pc-sombre.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/apres/21_atlas_ecg_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/01_accueil_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/01_accueil_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/02_accueil_directeur_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/02_accueil_directeur_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/03_bouton_directeur_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/03_bouton_directeur_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/04_notification_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/04_notification_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/05_specialite_cardiologie_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/05_specialite_cardiologie_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/06_systeme_cardiologie_mobile.png` | review_report | SYSTEM | pull_request_base |
| `audits/FRONT_captures/avant/06_systeme_cardiologie_pc.png` | review_report | SYSTEM | pull_request_base |
| `audits/FRONT_captures/avant/07_entree_cim_plan_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/07_entree_cim_plan_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/08_cours_entete_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/08_cours_entete_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/09_cours_ilot_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/09_cours_ilot_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/10_cours_fenetre_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/10_cours_fenetre_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/11_cours_quiz_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/11_cours_quiz_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/12_cours_pareto_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/12_cours_pareto_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/13_cours_navigo_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/13_cours_navigo_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/14_cours_police_taille_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/14_cours_police_taille_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/15_cours_mode_livre_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/15_cours_mode_livre_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/16_cours_sciences_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/16_cours_sciences_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/17_examen_federal_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/17_examen_federal_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/18_carnet_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/18_carnet_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/19_recherche_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/19_recherche_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/20_methode_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/20_methode_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/21_atlas_ecg_mobile.png` | review_report | GLOBAL | pull_request_base |
| `audits/FRONT_captures/avant/21_atlas_ecg_pc.png` | review_report | GLOBAL | pull_request_base |
| `audits/FUSION_ALPHA.md` | review_report | GLOBAL | pull_request_base |
| `audits/FUSION_GLOSSAIRE.md` | review_report | GLOBAL | pull_request_base |
| `audits/FUSION_J44.md` | review_report | S02 | pull_request_base |
| `audits/HOME_DIRECTEUR_2026-09-26.md` | review_report | GLOBAL | pull_request_base |
| `audits/I26.md` | review_report | S02 | pull_request_base |
| `audits/J18.md` | review_report | S02 | pull_request_base |
| `audits/J18_sources.md` | review_report | S02 | pull_request_base |
| `audits/J44.md` | review_report | S02 | pull_request_base |
| `audits/NAVIGO_2026-09-26.md` | review_report | GLOBAL | pull_request_base |
| `build_front.py` | integration_source | GLOBAL | pull_request_base |
| `build_medina.py` | integration_source | GLOBAL | pull_request_base |
| `build_v7.py` | unknown |  | pull_request_base |
| `captures_front.py` | unknown |  | pull_request_base |
| `chantier.py` | unknown |  | pull_request_base |
| `chapters.json` | registration_source | GLOBAL | pull_request_base |
| `chapters/A41/A41_a.html` | course_source | T1 | pull_request_base |
| `chapters/A41/A41_b.html` | course_source | T1 | pull_request_base |
| `chapters/A41/A41_c.html` | course_source | T1 | pull_request_base |
| `chapters/A41/A41_d.html` | course_source | T1 | pull_request_base |
| `chapters/A41/A41_pop1.html` | course_source | T1 | pull_request_base |
| `chapters/A41/A41_pop2.html` | course_source | T1 | pull_request_base |
| `chapters/A41/A41_pop_pa.html` | course_source | T1 | pull_request_base |
| `chapters/D84/D84_a.html` | course_source | S07 | pull_request_base |
| `chapters/D84/D84_b.html` | course_source | S07 | pull_request_base |
| `chapters/D84/D84_c.html` | course_source | S07 | pull_request_base |
| `chapters/D84/D84_d.html` | course_source | S07 | pull_request_base |
| `chapters/D84/D84_pop1.html` | course_source | S07 | pull_request_base |
| `chapters/D84/D84_pop2.html` | course_source | S07 | pull_request_base |
| `chapters/I00/I00_a.html` | course_source | S01 | pull_request_base |
| `chapters/I00/I00_b.html` | course_source | S01 | pull_request_base |
| `chapters/I00/I00_c.html` | course_source | S01 | pull_request_base |
| `chapters/I00/I00_d.html` | course_source | S01 | pull_request_base |
| `chapters/I00/I00_pop1.html` | course_source | S01 | pull_request_base |
| `chapters/I00/I00_pop2.html` | course_source | S01 | pull_request_base |
| `chapters/I00/I00_pop3.html` | course_source | S01 | pull_request_base |
| `chapters/I00/I00_pop4.html` | course_source | S01 | pull_request_base |
| `chapters/I00/I00_pop5.html` | course_source | S01 | pull_request_base |
| `chapters/I00/I00_pop6.html` | course_source | S01 | pull_request_base |
| `chapters/I10/I10_a.html` | course_source | S01 | pull_request_base |
| `chapters/I10/I10_b.html` | course_source | S01 | pull_request_base |
| `chapters/I10/I10_c.html` | course_source | S01 | pull_request_base |
| `chapters/I10/I10_d.html` | course_source | S01 | pull_request_base |
| `chapters/I10/I10_pop1.html` | course_source | S01 | pull_request_base |
| `chapters/I10/I10_pop2.html` | course_source | S01 | pull_request_base |
| `chapters/I10/I10_pop3.html` | course_source | S01 | pull_request_base |
| `chapters/I10/I10_pop4.html` | course_source | S01 | pull_request_base |
| `chapters/I10/I10_pop5.html` | course_source | S01 | pull_request_base |
| `chapters/I21/I21_a.html` | course_source | S01 | pull_request_base |
| `chapters/I21/I21_b.html` | course_source | S01 | pull_request_base |
| `chapters/I21/I21_c.html` | course_source | S01 | pull_request_base |
| `chapters/I21/I21_d.html` | course_source | S01 | pull_request_base |
| `chapters/I21/I21_pop1.html` | course_source | S01 | pull_request_base |
| `chapters/I21/I21_pop2.html` | course_source | S01 | pull_request_base |
| `chapters/I21/I21_pop3.html` | course_source | S01 | pull_request_base |
| `chapters/I21/I21_pop4.html` | course_source | S01 | pull_request_base |
| `chapters/I21/I21_pop5.html` | course_source | S01 | pull_request_base |
| `chapters/I21/I21_pop6.html` | course_source | S01 | pull_request_base |
| `chapters/I25/I25_a.html` | course_source | S01 | pull_request_base |
| `chapters/I25/I25_b.html` | course_source | S01 | pull_request_base |
| `chapters/I25/I25_c.html` | course_source | S01 | pull_request_base |
| `chapters/I25/I25_d.html` | course_source | S01 | pull_request_base |
| `chapters/I25/I25_pop1.html` | course_source | S01 | pull_request_base |
| `chapters/I25/I25_pop2.html` | course_source | S01 | pull_request_base |
| `chapters/I25/I25_pop3.html` | course_source | S01 | pull_request_base |
| `chapters/I25/I25_pop4.html` | course_source | S01 | pull_request_base |
| `chapters/I25/I25_pop5.html` | course_source | S01 | pull_request_base |
| `chapters/I25/I25_pop6.html` | course_source | S01 | pull_request_base |
| `chapters/I26/I26_a.html` | course_source | S02 | pull_request_base |
| `chapters/I26/I26_b.html` | course_source | S02 | pull_request_base |
| `chapters/I26/I26_c.html` | course_source | S02 | pull_request_base |
| `chapters/I26/I26_d.html` | course_source | S02 | pull_request_base |
| `chapters/I26/I26_pop1.html` | course_source | S02 | pull_request_base |
| `chapters/I26/I26_pop2.html` | course_source | S02 | pull_request_base |
| `chapters/I26/I26_pop_pa.html` | course_source | S02 | pull_request_base |
| `chapters/I30/I30_a.html` | course_source | S01 | pull_request_base |
| `chapters/I30/I30_b.html` | course_source | S01 | pull_request_base |
| `chapters/I30/I30_c.html` | course_source | S01 | pull_request_base |
| `chapters/I30/I30_d.html` | course_source | S01 | pull_request_base |
| `chapters/I30/I30_pop1.html` | course_source | S01 | pull_request_base |
| `chapters/I30/I30_pop2.html` | course_source | S01 | pull_request_base |
| `chapters/I30/I30_pop3.html` | course_source | S01 | pull_request_base |
| `chapters/I30/I30_pop4.html` | course_source | S01 | pull_request_base |
| `chapters/I30/I30_pop5.html` | course_source | S01 | pull_request_base |
| `chapters/I30/I30_pop6.html` | course_source | S01 | pull_request_base |
| `chapters/I33/I33_a.html` | course_source | S01 | pull_request_base |
| `chapters/I33/I33_b.html` | course_source | S01 | pull_request_base |
| `chapters/I33/I33_c.html` | course_source | S01 | pull_request_base |
| `chapters/I33/I33_d.html` | course_source | S01 | pull_request_base |
| `chapters/I33/I33_pop1.html` | course_source | S01 | pull_request_base |
| `chapters/I33/I33_pop2.html` | course_source | S01 | pull_request_base |
| `chapters/I33/I33_pop3.html` | course_source | S01 | pull_request_base |
| `chapters/I33/I33_pop4.html` | course_source | S01 | pull_request_base |
| `chapters/I34/I34_a.html` | course_source | S01 | pull_request_base |
| `chapters/I34/I34_b.html` | course_source | S01 | pull_request_base |
| `chapters/I34/I34_c.html` | course_source | S01 | pull_request_base |
| `chapters/I34/I34_d.html` | course_source | S01 | pull_request_base |
| `chapters/I34/I34_pop1.html` | course_source | S01 | pull_request_base |
| `chapters/I34/I34_pop2.html` | course_source | S01 | pull_request_base |
| `chapters/I34/I34_pop3.html` | course_source | S01 | pull_request_base |
| `chapters/I34/I34_pop4.html` | course_source | S01 | pull_request_base |
| `chapters/I34/I34_pop5.html` | course_source | S01 | pull_request_base |
| `chapters/I34/I34_pop6.html` | course_source | S01 | pull_request_base |
| `chapters/I35/I35_a.html` | course_source | S01 | pull_request_base |
| `chapters/I35/I35_b.html` | course_source | S01 | pull_request_base |
| `chapters/I35/I35_c.html` | course_source | S01 | pull_request_base |
| `chapters/I35/I35_d.html` | course_source | S01 | pull_request_base |
| `chapters/I35/I35_pop1.html` | course_source | S01 | pull_request_base |
| `chapters/I35/I35_pop2.html` | course_source | S01 | pull_request_base |
| `chapters/I35/I35_pop3.html` | course_source | S01 | pull_request_base |
| `chapters/I35/I35_pop4.html` | course_source | S01 | pull_request_base |
| `chapters/I35/I35_pop5.html` | course_source | S01 | pull_request_base |
| `chapters/I40/I40_a.html` | course_source | S01 | pull_request_base |
| `chapters/I40/I40_b.html` | course_source | S01 | pull_request_base |
| `chapters/I40/I40_c.html` | course_source | S01 | pull_request_base |
| `chapters/I40/I40_d.html` | course_source | S01 | pull_request_base |
| `chapters/I40/I40_pop1.html` | course_source | S01 | pull_request_base |
| `chapters/I40/I40_pop2.html` | course_source | S01 | pull_request_base |
| `chapters/I40/I40_pop3.html` | course_source | S01 | pull_request_base |
| `chapters/I40/I40_pop4.html` | course_source | S01 | pull_request_base |
| `chapters/I40/I40_pop5.html` | course_source | S01 | pull_request_base |
| `chapters/I40/I40_pop6.html` | course_source | S01 | pull_request_base |
| `chapters/I42/I42_a.html` | course_source | S01 | pull_request_base |
| `chapters/I42/I42_b.html` | course_source | S01 | pull_request_base |
| `chapters/I42/I42_c.html` | course_source | S01 | pull_request_base |
| `chapters/I42/I42_d.html` | course_source | S01 | pull_request_base |
| `chapters/I42/I42_pop1.html` | course_source | S01 | pull_request_base |
| `chapters/I42/I42_pop2.html` | course_source | S01 | pull_request_base |
| `chapters/I42/I42_pop3.html` | course_source | S01 | pull_request_base |
| `chapters/I42/I42_pop4.html` | course_source | S01 | pull_request_base |
| `chapters/I42/I42_pop5.html` | course_source | S01 | pull_request_base |
| `chapters/I42/I42_pop6.html` | course_source | S01 | pull_request_base |
| `chapters/I44/I44_a.html` | course_source | S01 | pull_request_base |
| `chapters/I44/I44_b.html` | course_source | S01 | pull_request_base |
| `chapters/I44/I44_c.html` | course_source | S01 | pull_request_base |
| `chapters/I44/I44_d.html` | course_source | S01 | pull_request_base |
| `chapters/I44/I44_pop1.html` | course_source | S01 | pull_request_base |
| `chapters/I44/I44_pop2.html` | course_source | S01 | pull_request_base |
| `chapters/I44/I44_pop3.html` | course_source | S01 | pull_request_base |
| `chapters/I44/I44_pop4.html` | course_source | S01 | pull_request_base |
| `chapters/I44/I44_pop5.html` | course_source | S01 | pull_request_base |
| `chapters/I44/I44_pop6.html` | course_source | S01 | pull_request_base |
| `chapters/I46/I46_a.html` | course_source | S01 | pull_request_base |
| `chapters/I46/I46_b.html` | course_source | S01 | pull_request_base |
| `chapters/I46/I46_c.html` | course_source | S01 | pull_request_base |
| `chapters/I46/I46_d.html` | course_source | S01 | pull_request_base |
| `chapters/I46/I46_pop1.html` | course_source | S01 | pull_request_base |
| `chapters/I46/I46_pop2.html` | course_source | S01 | pull_request_base |
| `chapters/I46/I46_pop3.html` | course_source | S01 | pull_request_base |
| `chapters/I46/I46_pop4.html` | course_source | S01 | pull_request_base |
| `chapters/I46/I46_pop5.html` | course_source | S01 | pull_request_base |
| `chapters/I47/I47_a.html` | course_source | S01 | pull_request_base |
| `chapters/I47/I47_b.html` | course_source | S01 | pull_request_base |
| `chapters/I47/I47_c.html` | course_source | S01 | pull_request_base |
| `chapters/I47/I47_d.html` | course_source | S01 | pull_request_base |
| `chapters/I47/I47_pop1.html` | course_source | S01 | pull_request_base |
| `chapters/I47/I47_pop2.html` | course_source | S01 | pull_request_base |
| `chapters/I47/I47_pop3.html` | course_source | S01 | pull_request_base |
| `chapters/I47/I47_pop4.html` | course_source | S01 | pull_request_base |
| `chapters/I47/I47_pop5.html` | course_source | S01 | pull_request_base |
| `chapters/I47/I47_pop6.html` | course_source | S01 | pull_request_base |
| `chapters/I48/I48_a.html` | course_source | S01 | pull_request_base |
| `chapters/I48/I48_b.html` | course_source | S01 | pull_request_base |
| `chapters/I48/I48_c.html` | course_source | S01 | pull_request_base |
| `chapters/I48/I48_d.html` | course_source | S01 | pull_request_base |
| `chapters/I48/I48_pop1.html` | course_source | S01 | pull_request_base |
| `chapters/I48/I48_pop2.html` | course_source | S01 | pull_request_base |
| `chapters/I48/I48_pop3.html` | course_source | S01 | pull_request_base |
| `chapters/I48/I48_pop4.html` | course_source | S01 | pull_request_base |
| `chapters/I49/I49_a.html` | course_source | S01 | pull_request_base |
| `chapters/I49/I49_b.html` | course_source | S01 | pull_request_base |
| `chapters/I49/I49_c.html` | course_source | S01 | pull_request_base |
| `chapters/I49/I49_d.html` | course_source | S01 | pull_request_base |
| `chapters/I49/I49_pop1.html` | course_source | S01 | pull_request_base |
| `chapters/I49/I49_pop2.html` | course_source | S01 | pull_request_base |
| `chapters/I49/I49_pop3.html` | course_source | S01 | pull_request_base |
| `chapters/I49/I49_pop4.html` | course_source | S01 | pull_request_base |
| `chapters/I49/I49_pop5.html` | course_source | S01 | pull_request_base |
| `chapters/I50/I50_a.html` | course_source | S01 | pull_request_base |
| `chapters/I50/I50_b.html` | course_source | S01 | pull_request_base |
| `chapters/I50/I50_c.html` | course_source | S01 | pull_request_base |
| `chapters/I50/I50_d.html` | course_source | S01 | pull_request_base |
| `chapters/I50/I50_pop1.html` | course_source | S01 | pull_request_base |
| `chapters/I50/I50_pop2.html` | course_source | S01 | pull_request_base |
| `chapters/I50/I50_pop3.html` | course_source | S01 | pull_request_base |
| `chapters/I50/I50_pop4.html` | course_source | S01 | pull_request_base |
| `chapters/I70/I70_a.html` | course_source | S01 | pull_request_base |
| `chapters/I70/I70_b.html` | course_source | S01 | pull_request_base |
| `chapters/I70/I70_c.html` | course_source | S01 | pull_request_base |
| `chapters/I70/I70_d.html` | course_source | S01 | pull_request_base |
| `chapters/I70/I70_pop.html` | course_source | S01 | pull_request_base |
| `chapters/I71/I71_a.html` | course_source | S01 | pull_request_base |
| `chapters/I71/I71_b.html` | course_source | S01 | pull_request_base |
| `chapters/I71/I71_c.html` | course_source | S01 | pull_request_base |
| `chapters/I71/I71_d.html` | course_source | S01 | pull_request_base |
| `chapters/I71/I71_pop.html` | course_source | S01 | pull_request_base |
| `chapters/I80/I80_a.html` | course_source | S01 | pull_request_base |
| `chapters/I80/I80_b.html` | course_source | S01 | pull_request_base |
| `chapters/I80/I80_c.html` | course_source | S01 | pull_request_base |
| `chapters/I80/I80_d.html` | course_source | S01 | pull_request_base |
| `chapters/I80/I80_pop.html` | course_source | S01 | pull_request_base |
| `chapters/J18/J18_a.html` | course_source | S02 | pull_request_base |
| `chapters/J18/J18_b.html` | course_source | S02 | pull_request_base |
| `chapters/J18/J18_c.html` | course_source | S02 | pull_request_base |
| `chapters/J18/J18_d.html` | course_source | S02 | pull_request_base |
| `chapters/J18/J18_pop1.html` | course_source | S02 | pull_request_base |
| `chapters/J18/J18_pop_pa.html` | course_source | S02 | pull_request_base |
| `chapters/J44/J44_a.html` | course_source | S02 | pull_request_base |
| `chapters/J44/J44_b.html` | course_source | S02 | pull_request_base |
| `chapters/J44/J44_c.html` | course_source | S02 | pull_request_base |
| `chapters/J44/J44_d.html` | course_source | S02 | pull_request_base |
| `chapters/J44/J44_pop1.html` | course_source | S02 | pull_request_base |
| `chapters/J44/J44_pop2.html` | course_source | S02 | pull_request_base |
| `chapters/J44/J44_pop3.html` | course_source | S02 | pull_request_base |
| `chapters/J44/J44_pop_pa.html` | course_source | S02 | pull_request_base |
| `chapters/J45/J45_a.html` | course_source | S02 | pull_request_base |
| `chapters/J45/J45_b.html` | course_source | S02 | pull_request_base |
| `chapters/J45/J45_c.html` | course_source | S02 | pull_request_base |
| `chapters/J45/J45_d.html` | course_source | S02 | pull_request_base |
| `chapters/J45/J45_pop1.html` | course_source | S02 | pull_request_base |
| `chapters/J45/J45_pop2.html` | course_source | S02 | pull_request_base |
| `chapters/J45/J45_pop3.html` | course_source | S02 | pull_request_base |
| `chapters/J45/J45_pop4.html` | course_source | S02 | pull_request_base |
| `chapters/M06/M06_a.html` | course_source | S10 | pull_request_base |
| `chapters/M06/M06_b.html` | course_source | S10 | pull_request_base |
| `chapters/M06/M06_c.html` | course_source | S10 | pull_request_base |
| `chapters/M06/M06_d.html` | course_source | S10 | pull_request_base |
| `chapters/M06/M06_pop.html` | course_source | S10 | pull_request_base |
| `chapters/M31/M31_a.html` | course_source | S07 | pull_request_base |
| `chapters/M31/M31_b.html` | course_source | S07 | pull_request_base |
| `chapters/M31/M31_c.html` | course_source | S07 | pull_request_base |
| `chapters/M31/M31_d.html` | course_source | S07 | pull_request_base |
| `chapters/M31/M31_pop.html` | course_source | S07 | pull_request_base |
| `chapters/M32/M32_a.html` | course_source | S07 | pull_request_base |
| `chapters/M32/M32_b.html` | course_source | S07 | pull_request_base |
| `chapters/M32/M32_c.html` | course_source | S07 | pull_request_base |
| `chapters/M32/M32_d.html` | course_source | S07 | pull_request_base |
| `chapters/M32/M32_pop.html` | course_source | S07 | pull_request_base |
| `chapters/Q21/Q21_a.html` | course_source | S01 | pull_request_base |
| `chapters/Q21/Q21_b.html` | course_source | S01 | pull_request_base |
| `chapters/Q21/Q21_c.html` | course_source | S01 | pull_request_base |
| `chapters/Q21/Q21_d.html` | course_source | S01 | pull_request_base |
| `chapters/Q21/Q21_pop1.html` | course_source | S01 | pull_request_base |
| `chapters/Q21/Q21_pop2.html` | course_source | S01 | pull_request_base |
| `chapters/Q21/Q21_pop3.html` | course_source | S01 | pull_request_base |
| `chapters/Q21/Q21_pop4.html` | course_source | S01 | pull_request_base |
| `chapters/Q21/Q21_pop5.html` | course_source | S01 | pull_request_base |
| `chapters/Q21/Q21_pop6.html` | course_source | S01 | pull_request_base |
| `chapters/Q21/Q21_pop7.html` | course_source | S01 | pull_request_base |
| `chapters/T78/T78_a.html` | course_source | S07 | pull_request_base |
| `chapters/T78/T78_b.html` | course_source | S07 | pull_request_base |
| `chapters/T78/T78_c.html` | course_source | S07 | pull_request_base |
| `chapters/T78/T78_d.html` | course_source | S07 | pull_request_base |
| `chapters/T78/T78_pop1.html` | course_source | S07 | pull_request_base |
| `chapters/T78/T78_pop2.html` | course_source | S07 | pull_request_base |
| `create_cycle_pdf.py` | unknown |  | pull_request_base |
| `create_status_pdf.py` | unknown |  | pull_request_base |
| `dist/MEDINA_Claude.html` | derived |  | pull_request_base |
| `dist/MEDINA_Etat_des_lieux.html` | derived |  | pull_request_base |
| `dist/MEDINA_SOURCES.json` | derived |  | pull_request_base |
| `dist/MEDINA_final.html` | derived |  | pull_request_base |
| `dist/MEDINA_final_SOURCES.json` | derived |  | pull_request_base |
| `docs/STYLE_REDACTION.md` | documentation | GLOBAL | pull_request_base |
| `docs/alpha/IDENTITE_MEDINA_Alpha.md` | documentation | GLOBAL | pull_request_base |
| `docs/alpha/PROMPT_MEDINA_Alpha.md` | documentation | GLOBAL | pull_request_base |
| `docs/passation/consignes_gen.py` | documentation | GLOBAL | pull_request_base |
| `docs/passation/mesure_texte.py` | documentation | GLOBAL | pull_request_base |
| `docs/passation/wf_contre_lecture.js` | documentation | GLOBAL | pull_request_base |
| `docs/passation/wf_reecriture_sequentielle.js` | documentation | GLOBAL | pull_request_base |
| `engine/medina_course.css` | integration_source | GLOBAL | pull_request_base |
| `engine/medina_course.js` | integration_source | GLOBAL | pull_request_base |
| `glossary/a41.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/cardio_1.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/cardio_2.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/cardio_3.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/d84.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/i00.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/i10.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/i21.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/i25.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/i26.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/i30.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/i33.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/i34.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/i35.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/i40.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/i42.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/i44.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/i46.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/i47.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/i48.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/i49.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/i70.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/i71.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/i80.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/j18.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/j44.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/j45.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/m06.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/m31.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/m32.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/q21.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/t78.py` | glossary_source | GLOBAL | pull_request_base |
| `glossary/zz_fusion.py` | glossary_source | GLOBAL | pull_request_base |
| `modules/ecg.json` | derived | S01 | pull_request_base |
| `modules/ecg.py` | unknown |  | pull_request_base |
| `modules/p2.html` | unknown |  | pull_request_base |
| `modules/p3.html` | unknown |  | pull_request_base |
| `modules/prev.html` | unknown |  | pull_request_base |
| `pack.py` | unknown |  | pull_request_base |
| `pack_v7.py` | integration_source | GLOBAL | pull_request_base |
| `recover_polish.py` | unknown |  | pull_request_base |
| `restore.py` | unknown |  | pull_request_base |
| `shell/data.py` | registration_source | GLOBAL | pull_request_base |
| `shell/medina_front.html` | integration_source | GLOBAL | pull_request_base |
| `shell/polish.css` | integration_source | GLOBAL | pull_request_base |
| `shell/polish.js` | integration_source | GLOBAL | pull_request_base |
| `shell/shell.html` | integration_source | GLOBAL | pull_request_base |
| `test_medina.py` | unknown |  | pull_request_base |
| `test_preview.py` | unknown |  | pull_request_base |
| `test_v7.py` | unknown |  | pull_request_base |

## claude/review-i48-esc2024-20261007


## claude/review-medina-global-20261007


| Fichier | Nature | Routage | Diff |
| --- | --- | --- | --- |
| `chapters/I48/I48_a.html` | course_source | S01 | pull_request_base |
| `chapters/I48/I48_c.html` | course_source | S01 | pull_request_base |
| `chapters/I48/I48_pop2.html` | course_source | S01 | pull_request_base |
| `chapters/I48/I48_pop4.html` | course_source | S01 | pull_request_base |
| `docs/collaboration/HANDOFF_LATEST.md` | documentation | GLOBAL | pull_request_base |
| `docs/collaboration/reviews/CLAUDE_CS_CARDIO_RAPPORT_2026-10-07.md` | review_report | S01, CS | pull_request_base |
| `docs/collaboration/reviews/CLAUDE_I48_ESC2024_RAPPORT.md` | review_report | S01 | pull_request_base |
| `modules/cardiovascular_cs.html` | clinical_skills_source | S01, CS | pull_request_base |
| `modules/cardiovascular_cs.js` | clinical_skills_source | S01, CS | pull_request_base |

## codex/ajouter-options-de-generation-de-fragments

- PR #3 vise main ; comparaison à la cible MEDINA requise.

| Fichier | Nature | Routage | Diff |
| --- | --- | --- | --- |
| `build_front.py` | integration_source | GLOBAL | pull_request_base |

## codex/configurer-publication-github-pages-automatique

- Chemin sans route de build connue ; examen manuel requis.
- PR #4 vise main ; comparaison à la cible MEDINA requise.

| Fichier | Nature | Routage | Diff |
| --- | --- | --- | --- |
| `.github/workflows/pages.yml` | integration_source | GLOBAL | pull_request_base |
| `.gitignore` | unknown |  | pull_request_base |
| `build_index.py` | integration_source | GLOBAL | pull_request_base |
| `tests/audit_fragments.py` | integration_source | GLOBAL | pull_request_base |

## codex/creer-fragments.json-et-corrige-des-chemins

- Chemin sans route de build connue ; examen manuel requis.
- Vérifier titres, covers, activation, rattachements et rubriques après intégration.
- PR #2 vise main ; comparaison à la cible MEDINA requise.

| Fichier | Nature | Routage | Diff |
| --- | --- | --- | --- |
| `.gitignore` | unknown |  | pull_request_base |
| `FRAGMENTS.md` | documentation | GLOBAL | pull_request_base |
| `build_medina.py` | integration_source | GLOBAL | pull_request_base |
| `fragments.json` | registration_source | GLOBAL | pull_request_base |
| `test_preview.py` | unknown |  | pull_request_base |

## codex/etancheite-complete-des-fragments

- PR #5 vise main ; comparaison à la cible MEDINA requise.

| Fichier | Nature | Routage | Diff |
| --- | --- | --- | --- |
| `FRAGMENTS.md` | documentation | GLOBAL | pull_request_base |
| `build_front.py` | integration_source | GLOBAL | pull_request_base |
| `tests/audit_fragments.py` | integration_source | GLOBAL | pull_request_base |

## codex/fragment-s01-accueil-navigo-20261005

- Vérifier titres, covers, activation, rattachements et rubriques après intégration.
- PR #7 vise main ; comparaison à la cible MEDINA requise.

| Fichier | Nature | Routage | Diff |
| --- | --- | --- | --- |
| `FRAGMENTS.md` | documentation | GLOBAL | pull_request_base |
| `audits/S01_2026-10-05/README.md` | review_report | S01 | pull_request_base |
| `audits/S01_2026-10-05/browser-results.json` | review_report | S01 | pull_request_base |
| `audits/S01_2026-10-05/captures/accueil_mobile.jpg` | review_report | S01 | pull_request_base |
| `audits/S01_2026-10-05/captures/accueil_pc.jpg` | review_report | S01 | pull_request_base |
| `audits/S01_2026-10-05/captures/cours_mobile.jpg` | review_report | S01 | pull_request_base |
| `audits/S01_2026-10-05/captures/cours_pc.jpg` | review_report | S01 | pull_request_base |
| `audits/S01_2026-10-05/captures/navigo_mobile.jpg` | review_report | S01 | pull_request_base |
| `build_front.py` | integration_source | GLOBAL | pull_request_base |
| `fragment_surface.py` | integration_source | GLOBAL | pull_request_base |
| `fragments.json` | registration_source | GLOBAL | pull_request_base |
| `shell/fragment.css` | integration_source | GLOBAL | pull_request_base |
| `shell/fragment.js` | integration_source | GLOBAL | pull_request_base |
| `tests/audit_fragments.py` | integration_source | GLOBAL | pull_request_base |
| `tests/verify_s01_browser.cjs` | integration_source | GLOBAL | pull_request_base |

## main


## Limites

- Les rapports et les tests déclarés ne constituent pas une vérification médicale indépendante.
- Le routage est contrôlé contre les sources locales de la cible, avant les changements proposés.
- Aucune branche n'est fusionnée, aucun reçu créé et aucun commit publié par ce scanner.
