# FUSION_ALPHA — intégration de la branche Alpha (ChatGPT) dans la branche Claude

**Date** : 26 septembre 2026. **Exécutant** : Claude Code, intégrateur unique (REPRISE_CLAUDE_CODE.md, phase 1).
**Sources** : `_alpha_in/MEDINA_Alpha_TRANSPORT_26-09-2026.zip` (6 empreintes SHA-256 conformes), restauré par `RESTAURER_MEDINA_Alpha.py` dans `../_alpha` (252 fichiers) ; `_alpha_in/MEDINA_Alpha_PASSATION_2026-09-26.md`.

## 1. Authenticité et version retenue

| Pièce | Constat | Décision |
|---|---|---|
| `MEDINA_Alpha_SOURCES.json.gz` | Reconstruit par `build_front.py` en un HTML **identique octet pour octet** au HTML du zip (11 953 435 o, 1 743 gabarits) | Source de vérité de la branche Alpha |
| `MEDINA_Alpha_26-09-2026.html` téléversé seul (11 788 946 o) | État **antérieur strict** : 20 cours, sans A41 ni I26, sans Navigo ni Police Taille ; aucun gabarit absent du zip, aucun gabarit différent | Conservé dans `_alpha_in/` pour mémoire ; non utilisé |
| Passation envoyée en cours de session | Identique (SHA-256) à celle de `_alpha_in/` | Aucune action |

## 2. Inventaire différentiel (`diff -rq`, avant fusion)

- **Identiques dans les deux branches** : les 17 chapitres cardiologiques, **J45**, 31 fichiers de glossaire communs sauf `j44.py`, `modules/ecg.py`, `modules/ecg.json`, `CHAPTER_SPEC.md`, `build_v7.py`, `restore.py`, `test_preview.py`, `test_medina.py`, `pack.py`.
- **Seulement Alpha** : chapitres **J18, I26, A41** (+ `j18.py`, `i26.py`, `a41.py`), `J44_pop3.html`, `audits/` (8 rapports), `IDENTITE_MEDINA_Alpha.md`, `create_cycle_pdf.py`, `create_status_pdf.py`, `recover_polish.py`.
- **Seulement Claude** : chapitres D84, I70, I71, I80, M06, M31, M32, T78 (+ glossaires), `modules/p2.html`, `p3.html`, `prev.html`, `CLAUDE.md`, `REPRISE_CLAUDE_CODE.md`, `.claude/commands/`.
- **Divergents** : `chapters.json`, J44 (6 fichiers) et `j44.py`, `engine/medina_course.js` et `.css`, `shell/polish.css` et `.js`, `shell/data.py`, `shell/medina_front.html` (seulement le nom « MEDINA_Alpha » dans `<title>` et `application-name`), `build_front.py`, `build_medina.py`, `chantier.py`, `pack_v7.py`, `test_v7.py`, `PROMPT_MEDINA.md`.

Après fusion, tout fichier Alpha est présent dans le dépôt ou remplacé à dessein (tableau § 4).

## 3. Chapitres

| Chapitre | Décision | Détail |
|---|---|---|
| J18 Pneumonies de l’adulte | **Repris** (vague 2, vérifiée dans `medora-data`) | `covers` restreint à **J13, J14, J15, J18** : le cours traite la pneumonie communautaire bactérienne de l’adulte ; J12 (virales → futur J09), J16, J17 non traités (contrôle de contrat, § 6) |
| I26 Embolie pulmonaire aiguë | **Repris** (vague 2) | `covers` = I26 |
| A41 Sepsis et choc septique de l’adulte | **Repris** (vague 7) | `covers` = A41 ; A40 et R57.2 non développés (signalés dans le cours) |
| J44 BPCO | **Fusionné** section par section | Base Alpha (évolution stricte de Claude : aucune section propre à Claude) ; restaurations Claude vérifiées ; journal détaillé : `audits/FUSION_J44.md` ; 10 256 mots, 50 fenêtres, 4 quiz, 7 Pareto |
| J45 et 17 cours cardiologiques | Identiques | Aucune action |
| D84, I70, I71, I80, M06, M31, M32, T78 | Conservés (propres à Claude) | M31 : sigle « PRES » corrigé en « PReS » (collision de sens, § 5) |

## 4. Code et interface

| Élément | Origine | Décision |
|---|---|---|
| **Navigo** (plan flottant, onglets, recherche, sauts en lecture verticale et en mode livre) | Alpha | Porté (`engine/medina_course.js`, `shell/polish.css`) ; libellés corrigés (espace entre numéro et titre) |
| **Police Taille** (14–24 px, curseur, A−/A+, réinitialisation, mémorisation par cours, transmise aux fenêtres) | Alpha | Porté |
| **Mode livre** : pas de page calculé sur la largeur réelle et l’espacement ; sciences masquées respectées ; flèches du clavier inactives dans les champs | Alpha | Porté |
| Numéros de sous-parties `mc-subn` | Alpha | Porté (`build_medina.transform`) |
| `DONE_COURSES` : insigne « 100 % rédigé » réservé aux chapitres audités, distinct de l’intégration | Alpha | **Adopté** : 17 cours cardiologiques ; `MEDINA_COMPLETE` injecté par `build_front.py` |
| Directeur des systèmes intégré à l’accueil (cartes, jauges, pastilles de cours) | Alpha | Porté ; ajouté **à côté** du bouton directeur Claude, relié à sa fenêtre (« Plan de rédaction ») |
| Accueil : phrase périmée « Aucun cours n’est déclaré complet » | Alpha | Remplacée à la construction |
| Style des cours (en-tête, onglets, îlots, encadrés, quiz, tableaux, fenêtres) | Alpha | Porté, **adapté à la typographie retenue** : titres et numéros rouges soulignés (l’ocre `#ad8242` n’est pas retenu) ; en-tête de cours et en-tête des fenêtres en version claire pour garder le contraste du titre rouge |
| `pack_v7.py` : empaquette `shell/*.css`, `shell/*.js`, `audits/*.md` | Alpha | Adopté (les couches `polish` n’étaient pas empaquetées dans la branche Claude) ; ajout de `docs/`, `.claude/commands/`, `modules/*.html` |
| `test_v7.py` : code de sortie non nul en cas d’échec | Alpha | Adopté |
| `create_cycle_pdf.py`, `create_status_pdf.py`, `recover_polish.py` | Alpha | Copiés à la racine (outils) |
| `IDENTITE_MEDINA_Alpha.md`, `PROMPT_MEDINA.md` d’Alpha (version 3.0 antérieure) | Alpha | Archivés dans `docs/alpha/` (le prompt Claude est un sur-ensemble) |
| Nom « MEDINA_Alpha » dans `medina_front.html` | Alpha | Non repris : le produit s’appelle Medina |
| Compression des cours, bouton directeur, atlas ECG, notification, insignes, typographie Georgia | Claude | **Conservés** |
| Notification « Nouveaux cours livrés » | Claude | Conservée ; chaque cours non achevé y porte « en révision » |

### Défauts découverts et corrigés pendant la fusion

1. **Cours inaccessibles** : la coque d’origine redirige `#/entry/I30`, `K35`, `A41`, `I63` vers d’anciens modules pilotes `#/pathology/…` introuvables dans le fichier autonome (« Chargement impossible »). Le cours **I30** (Péricardites) était donc inaccessible dans les deux branches, et **A41** l’aurait été. Correctif de construction (`build_medina.build`, remplacements assertés) : la redirection n’a lieu que si aucun cours MEDINA n’existe, et `#/pathology/<code>` renvoie vers le cours quand il existe ; `MEDINA_ALIAS` est désormais injecté dans `<head>`, avant les scripts de la coque.
2. **Doublons de fonctions** apparus au portage (`toast`, `ecgButton`) : supprimés.
3. `test_v7.py` : Chromium local (`MEDINA_CHROMIUM` ou `/opt/pw-browsers/chromium`) ; mode `--static` ; contrôles ajoutés pour Navigo (ouverture, contenu, saut), Police Taille (réglage, réinitialisation) et mode livre ; I50, chapitre modèle antérieur à la règle des préfixes, est exempté de ce seul contrôle.

## 5. Glossaire

- Union des deux branches : 1 231 clés (Claude) et 1 011 clés effectives (Alpha), soit 1 256 ; après fusion, corrections et ajouts : **1 276 clés**.
- **53 clés arbitrées** dans `glossary/zz_fusion.py` (chargé en dernier) : définitions riches écrasées par des fichiers chargés plus tard (souvent avec leur fenêtre d’approfondissement), définitions trop propres à un chapitre, dates d’essai divergentes (COMPASS 2017). Chaque fenêtre `ref` conservée existe et convient à tous les emplois. Détail : `audits/FUSION_GLOSSAIRE.md`.
- **Collisions de sens résolues** : PRES (encéphalopathie, I10) / **PReS** (société pédiatrique, M31) ; REDUCE (BPCO, J44) / **Gore REDUCE** (Q21) ; ABCDE et HOPE (sens minoritaires écrits en toutes lettres dans I10 et I25) ; **SSC** employé ~32 fois dans A41 au sens de *Surviving Sepsis Campaign* (écrit en toutes lettres) ; **V1** (récepteur V1a de la vasopressine, nouvelle clé) ; **ALAT** (Asociación Latinoamericana de Tórax écrite en toutes lettres, clé retirée pour réserver ALAT à l’alanine aminotransférase des futurs cours d’hépatologie).
- `build_medina.audit()` = `{}` sur les 30 chapitres.

## 6. Contrôle de conformité, corrections et vérification en texte intégral des chapitres repris

Un contrôle indépendant du contrat (§ 4, 10, 13, 14, 15 du prompt) a relevé dans J18, I26 et A41 des défauts bloquants (J18 sans critères formels dans le dernier îlot ; figures d’I26 hors contrat ; collision SSC dans A41 ; posologies manquantes du dabigatran et de l’édoxaban ; fiche ESCAPe décrivant REMAP-CAP), des défauts majeurs (tableaux des doses incomplets, pager des Sciences inerte, Pareto mal placés ou hors cible, formules de chantier, version « CIM-10-GM 2026 ») et un `covers` surdéclaré pour J18. Chaque chapitre a été corrigé, contre-lu par un agent indépendant, puis repris.

L’accès réseau ayant été ouvert par le propriétaire en cours de session, chaque réserve « vérifiée par extraits » a ensuite été **levée en texte intégral** (informations professionnelles suisses sur swissmedicinfo.ch et compendium.ch, recommandations GOLD 2026, SSI, ERS/ESICM/ESCMID 2023, ATS/IDSA, BTS, Surviving Sepsis Campaign 2021 et 2026, ESC/ERS 2019, AHA/ACC 2026, Plan de vaccination suisse 2026, PubMed), avec contre-lecture adverse d’au moins douze points par chapitre.

| Chapitre | Mots Alpha → livrés | Fenêtres | Quiz | Pareto | Vérification en texte intégral |
|---|---|---|---|---|---|
| J44 | 9 675 (Claude 7 591) → **14 740** | 51 | 4 | 7 | 80 points : 41 confirmés, 35 corrigés (dont PaCO₂ > 53 mmHg selon GOLD 2023–2026, antibiothérapie 5 jours, Daxas, trithérapies suisses) |
| J18 | 6 510 → **15 020** | 35 | 3 | 5 | 48 points (dont CAPE COD 4 ou 7 jours, amoxicilline 4–6 g/j, vaccination pneumococcique dès 2 ans, corticoïdes selon la SSI) |
| I26 | 6 769 → **12 465** | 41 | 4 | 7 | Anticoagulants et altéplase selon les textes suisses ; PEITHO (ténectéplase) |
| A41 | 6 851 → **11 819** | 30 | 4 | 7 | 58 points (dont noradrénaline, hydrocortisone non recommandée en routine selon le texte suisse, pipéracilline/tazobactam, SSC 2026) |

Tableaux détaillés (point, URL de la source primaire, verdict, correction) : sections « Vérification en texte intégral — 26.09.2026 » de `audits/J44.md`, `J18.md`, `I26.md`, `A41.md`.

## 7. Réserves reportées

- **Aucun des quatre chapitres n’est déclaré achevé** : `DONE_COURSES` reste limité aux 17 cours cardiologiques ; J44, J18, I26 et A41 portent la pastille « cours · en révision » jusqu’à leur audit indépendant /20 (grille § 16) et une revue humaine.
- Textes intégraux réellement inaccessibles (protections anti-robots ou abonnement) : NEJM, JAMA, ATS Journals, ERJ, Springer, LWW ; données correspondantes vérifiées sur les résumés MEDLINE, Europe PMC ou les publications conjointes, et signalées dans chaque audit.
- **J18** : `covers` restreint à J13, J14, J15, J18 ; J12 (pneumonies virales) appartient au périmètre du cours selon le § 9.3 et sera développé lors de la réécriture ; J16 et J17 à traiter ou à renvoyer.
- **A41** : A40 (sepsis à streptocoques) et R57.2 non développés.
- **I26** : pédiatrie, syndrome des antiphospholipides, grossesse compliquée, embolie sous-segmentaire isolée non développés (réserves Alpha).
- Chapitres propres à Claude non audités : T78, M31, I71, I80, I70 ; trop condensés : D84, M06, M32 (phase 4).
- Contrôles navigateur (Chromium, PC 1300 px et mobile 390 px) : voir § 8.

## 8. Contrôles de la livraison de phase 1

- Construction : `build_front.py` à partir du code de phase 1 (commit `38b7b56` pour `shell/polish.css`, `shell/polish.js`, `build_medina.py`) et du contenu final ; **30 cours**, 1 873 gabarits compressés, **8 481 859 octets** (12,8 Mo avant compression).
- `python3 test_v7.py` sur les **30 chapitres** (Chromium 141, PC 1300 × 900 et mobile 390 × 844) : **OK**. Le test contrôle les abréviations non couvertes (`audit()` vide), les fenêtres manquantes, les clés préfixées, l’affichage de chaque cours, le clic sur chaque mot vert, les quatre onglets, Navigo (ouverture, contenu, saut), Police Taille (réglage et réinitialisation), le mode livre, l’absence d’erreur JavaScript et l’absence de débordement horizontal sur mobile.
- Livrables : `dist/MEDINA_Claude.html`, `dist/MEDINA_SOURCES.json`, `dist/MEDINA_Etat_des_lieux.html`.
