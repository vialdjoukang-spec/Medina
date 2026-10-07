# MEDINA — dernière passation

Mise à jour : 7 octobre 2026. Le [tableau de bord commun](../../organisation/MEDINA_Organisation.html) fixe les noms, catégories et rangs théoriques. Sa [version publiée](https://vialdjoukang-spec.github.io/Medina/organisation.html) se reconstruit depuis les sources à chaque publication.

## Dossiers de livraison

Les 22 fragments ont un dossier sous [Livraison Codex](../../livraisons/Livraison%20Codex/) et [Livraison Claude](../../livraisons/Livraison%20Claude/). Les 30 cours intégrés sont remis avec leurs 251 sources HTML et JSON ; les fragments sans cours sont explicitement à produire.

Lire [le protocole](DELIVERY_PROTOCOL.md). Claude dispose des sources et dépose sa copie corrigée, son rapport et son manifeste sur sa branche. Codex contrôle les empreintes, le routage, le contenu, la reconstruction et les interactions avant de publier. Aucune livraison ancienne n’est ignorée à cause de son emplacement.

## Livraisons Claude reçues

| Livraison | État |
| --- | --- |
| Alpha, PR #1 | Fusionnée ; cours, glossaire et interface historiques conservés. |
| Relecture fibrillation atriale et CS, PR #8 | Intégrée avec contrelecture ; [reçu](receipts/CLAUDE_I48_CS_2026-10-07.json). |
| Audit global, lot 1, PR #9 | Huit cours, 17 sources ; intégré au commit `7fa06329b3369f54ef0831ae9f6cdf90fce5f605`, 583 contrôles navigateur réussis ; [reçu](receipts/CLAUDE_GLOBAL_LOT1_2026-10-07.json). |
| Audit global, lot 2 — I48 — Fibrillation et flutter auriculaires | **Livré, en attente d’injection** : copies corrigées de 7 fichiers dans [C-01-Cardiologie](../../livraisons/Livraison%20Claude/C-01-Cardiologie/), [rapport](../../livraisons/Livraison%20Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT2_I48/rapport.md) et [journal](../../livraisons/Livraison%20Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT2_I48/journal.json). Relecture intégrale des 8 fichiers ; `check-claude` conforme ; 583 et 71 contrôles navigateur réussis sur application temporaire. |
| Audit global, lot 3 — gabarits clonés de l’onglet Sciences (20 cours) | **Livré, en attente d’injection** : 20 fichiers `_c.html` dans [C-01-Cardiologie](../../livraisons/Livraison%20Claude/C-01-Cardiologie/) (16 cours) et [P-02-Pneumologie](../../livraisons/Livraison%20Claude/P-02-Pneumologie/) (I26, J18, J44, J45) ; 103 sites, 265 éditions ; [rapport](../../livraisons/Livraison%20Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT3_SCIENCES/rapport.md) avec 81 réserves médicales. Contrôles et `check-claude` réussis. |
| Audit global, lot 4 — I48 — Fibrillation et flutter auriculaires : justification systématique (cours pilote) | **Livré, en attente d’injection après les lots 2 et 3** : branche `claude/loving-shannon-spwrhc`, 8 sources corrigées dont `I48_d.html`, 5 entrées de `glossary/i48.py` ; 505 affirmations traitées, 360 compléments intégrés au texte, 133 mots verts, 12 fenêtres créées, 41 complétées, 12 erreurs du cours corrigées contre l’ESC 2024 ; [rapport](../../livraisons/Livraison%20Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT4_I48_JUSTIFICATION/rapport.md), [fenêtres types](../../livraisons/Livraison%20Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT4_I48_JUSTIFICATION/fenetres_types.html). Contrôles et `check-claude` réussis. Volume d’I48 : 25 494 → 66 107 mots, à valider par le propriétaire. |

Les originaux du lot 1 sont conservés dans les dossiers Claude des cinq fragments concernés et dans [ses archives](../../livraisons/Livraison%20Claude/Archives/2026-10-07-GLOBAL_LOT1/). Les adaptations médicales et les rectifications de son journal sont consignées dans la [contrelecture](reviews/2026-10-07/GLOBAL_LOT1/INTEGRATION_CODEX.md). La branche Claude conserve ses commits.

## Cours disponibles à relire intégralement

La mission demeure une relecture de l’ensemble : quatre onglets, fenêtres, figures, quiz, glossaires et Sémiologie CS. Employer un français médical professionnel, fluide et concis. Une correction ciblée ne valide pas toutes les sections du cours.

### C-01-Cardiologie

- I50 — Insuffisance cardiaque
- I21 — Syndromes coronariens aigus et infarctus du myocarde
- I25 — Syndromes coronariens chroniques et angor
- I48 — Fibrillation et flutter auriculaires
- I10 — Hypertension artérielle
- I30 — Péricardites, épanchement péricardique, tamponnade et constriction
- I33 — Endocardite infectieuse
- I35 — Valvulopathies aortiques
- I34 — Valvulopathies mitrales, tricuspides et pulmonaires
- I00 — Rhumatisme articulaire aigu
- I40 — Myocardites
- I42 — Cardiomyopathies
- I44 — Troubles de la conduction et bradycardies
- I47 — Tachycardies paroxystiques supraventriculaires et ventriculaires
- I49 — Extrasystoles et autres arythmies
- I46 — Arrêt cardiaque
- Q21 — Cardiopathies congénitales de l’adulte
- I71 — Anévrismes et dissections artérielles
- I80 — Thrombose veineuse profonde et thromboses veineuses
- I70 — Athérosclérose périphérique, artériopathie des membres inférieurs et ischémie aiguë

### P-02-Pneumologie

- J45 — Asthme
- J44 — Bronchopneumopathie chronique obstructive
- J18 — Pneumonies de l’adulte
- I26 — Embolie pulmonaire aiguë

### I-03-Infectiologie

- A41 — Sepsis et choc septique de l’adulte

### I-13-Immunologie et allergologie

- D84 — Déficits immunitaires
- M32 — Lupus érythémateux systémique
- T78 — Anaphylaxie et allergies
- M31 — Vascularites systémiques

### R-14-Rhumatologie et orthopédie

- M06 — Polyarthrite rhumatoïde

## Travail restant

- Injecter les lots 2 et 3 de Claude avec `apply-claude` (C-01-Cardiologie et P-02-Pneumologie), puis reconstruire S01 et S02.
- Mission commune de justification systématique : voir `MISSION_JUSTIFICATION_2026-10-07.md` (PR #11) pour la répartition 15/15. Claude commence par I48 comme cours pilote.
- **Lot 4 de Claude (I48, justification systématique) terminé** : rapport et réserves dans `livraisons/Livraison Claude/C-01-Cardiologie/archives/2026-10-07-GLOBAL_LOT4_I48_JUSTIFICATION/`. Injecter après les lots 2 et 3 (même fichiers). Extension aux 14 autres cours de Claude après validation des fenêtres types et du volume par le propriétaire ; méthode et script réutilisables dans `travail/lot4_I48_justification/`.
- Poursuivre la relecture intégrale des 30 cours et de CS ; les réserves médicales du lot 3 sont à reprendre cours par cours.
- Réserves de la PR #8 : la fenêtre des épisodes auriculaires rapides (R08) est corrigée par le lot 2 ; le complément vasculaire de CS (C10) reste ouvert.
- Constituer l’inventaire CIM-11 par fragment : aucun fragment n’est actuellement certifié complet. Le catalogue local historique contient 1 636 catégories CIM-10-GM 2024.
- PR #6 : accueil et QCM, travail Codex distinct encore en attente.

Avant chaque reprise, lire [l’inventaire des branches et PR](DELIVERIES_LATEST.md), les nouveaux dossiers Claude et les [reçus](receipts/). Après publication, vérifier séparément le déploiement du site.
