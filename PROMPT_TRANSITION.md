# MEDINA — Prompt de transition (unité de vérité)

Version du 9 octobre 2026. Ce document prime sur toute passation antérieure. Toute IA qui reprend MEDINA le lit en entier, puis lit `CLAUDE.md`, `docs/collaboration/LEADERSHIP_CLAUDE_2026-10-08.md` (sections 7 à 13) et `docs/STYLE_REDACTION.md`. Elle agit ensuite comme si elle avait conduit le projet depuis le début.

## 1. Projet et propriétaire
- **MEDINA** est l'atlas de cours de médecine du Dr Vial Tato Djoukang (Neuchâtel), qui prépare l'examen fédéral suisse de médecine humaine.
- **Dépôt** : `vialdjoukang-spec/Medina`, branche par défaut `main`.
- **Site** : https://vialdjoukang-spec.github.io/Medina/ (22 frontends dans `fragments/`, plus l'accueil).
- **Langue et ton** : français, phrases complètes, densité sans remplissage. Vial dicte souvent : interpréter avec bienveillance.
- **Autorisations** : accord permanent pour les branches, commits, pushes, PR et fusions dans MEDINA, une fois les contrôles passés.

## 2. Règles non négociables (acceptées)
1. **Rien de mémoire.** Chaque affirmation médicale provient d'une source réellement lue.
2. **Sources** : suisses d'abord (SSI, OFSP, sociétés suisses, Swiss Medical Forum, Suva), puis européennes (ERS, ESC, ESCMID, EAACI, NICE, HAS, AWMF). **Aucune recommandation américaine** ne fonde une conduite ; les essais peuvent être cités comme données.
3. **Médicaments** : information professionnelle suisse via `tools/swissmedic_fi.py`. Signaler tout usage hors indication.
4. **Plan monographique classique**, sans îlot ni tableau consacré au code CIM (le code n'apparaît que dans l'en-tête).
5. **Chaîne de production** : un rédacteur, puis un **relecteur distinct** qui fait deux passes sur quatre dimensions (rédaction, exactitude médicale, exactitude des sources, frontend), corrige et injecte. Codex peut auditer ensuite.
6. **Contrat HTML d'un cours** :
   - fichiers `chapters/<CODE>/<CODE>_a.html` à `_d.html`, plus `_pop1.html` et `_pop2.html` ;
   - quatre onglets : Pathologie, Examens, Sciences, Pharmacologie ;
   - un Pareto à la fin de chaque partie ;
   - dernier îlot : critères formels (`div.alert`), puis paramètres clés (`div.key`) ;
   - aucune abréviation sans clé dans `glossary/<code>.py`.
7. **Contentieux entre sources** : la source primaire applicable la plus récente l'emporte, exposée dans une fenêtre liée à un mot vert.
8. **Honnêteté** : une revue par IA n'est jamais une validation médicale humaine, et le cours le dit.
9. **Efficacité avant le volume** : cible indicative de 11 000 à 15 000 mots par cours.
10. **Style visuel** (décision de Vial du 9 octobre 2026) : couleurs **vives et vivantes, rien de plus** ; fonds ivoire, beige et gris interdits.
    - Fondement : Carruthers 2010 (doi:10.1186/1471-2288-10-12), Valdez et Mehrabian 1994 (doi:10.1037//0096-3445.123.4.394) et Lankston 2010 (doi:10.1258/jrsm.2010.100256).
    - Fond ciel clair vers vert printanier ; couvertures en dégradé bleu, lagon, vert et soleil ; cartes blanches à rail coloré.
    - Pas de filigrane, de motif décoratif ni de fond marin.
    - Fichiers : `engine/atlas_v4.css`, `engine/harmonie_v5.css`, `engine/portal_v3.css`.

## 3. Architecture technique
- **Catalogue** : CIM-10-GM 2024 (source OFS), dans `shell/medina_front.html`. La nosologie complète importée par Codex se trouve dans `nosology/` (`fragments/<ID>.json`, `frequency.json`).
- **Construction** :
  - `MEDINA_OUT=$PWD/dist python3 build_front.py --all-fragments` construit les 22 frontends (couches `fragment_surface.py` et `engine/*`) ;
  - `python3 build_index.py --fragments-dir dist/fragments --output dist/index.html` construit l'accueil ;
  - la publication sur Pages part automatiquement à chaque push sur `main` (`.github/workflows/pages.yml`).
- **Enregistrer un cours** :
  - entrée dans `chapters.json` (`code`, `covers`, `title`, `integrated`) ;
  - entrée dans `organisation/course_groups.json` (`owner`, `scope`) ;
  - état dans `organisation/FILE_FRAGMENTS_CLAUDE.json` ;
  - code ajouté à la liste des nouvelles productions dans `tests/audit_sciences.py` ;
  - puis `python3 tools/sceller.py enregistrer`.
- **Contrôles avant toute fusion** :
  - `python3 build_medina.py <CODE>` doit donner 0 abréviation non couverte ;
  - `python3 -m unittest discover -s tests -p 'test_*.py'` (248 tests) ;
  - `python3 tests/audit_fragments.py` ;
  - `MEDINA_OUT=$PWD/dist node tests/verify_fragment_frontends.cjs` (873 contrôles).
- **Jauges** (accueil, fragments, barre latérale) : « Pathologies fréquentes », « Examen fédéral » et « Avancement global ».
  - Elles sont calculées sur les **catégories à trois caractères** (`nosologyEngine.gauges`), car les sous-codes sont traités dans le cours de leur catégorie.
  - Affichage : « Libellé (n / total) (x %) ».
- **Navigation** : chaque fragment porte le bouton « Accueil MEDINA » (`../index.html`).

## 4. Travail accompli et accepté
- **Fragment C-01 Cardiologie** : 22 cours (production historique, audits Codex et Claude).
- **Fragment P-02 Pneumologie**, 23 cours injectés et scellés :
  - J45, J44, J40, J18, I26, J09, J96, J90, J86, J93, J84 ;
  - I27, J47, J80, J81, J12, J21, R04, J82, J67, J95, R05 et J60, relus en deux passes ;
  - rapports dans `livraisons/Livraison Claude/P-02-Pneumologie/travail/<CODE>/`.
- **Autres cours intégrés** : D84, M06, M32, T78, M31, I71, I80, I83, I70, A41, I51, A53, A54, B24 et B18. Le total est de 55 cours.
- **Nosologie** : Codex a importé la CIM-10-GM complète dans les 22 fragments. Chaque chapitre est visible, vide, « En préparation », avec un plan.
- **Plans des pathologies fréquentes** : 138 plans spécifiques dans `organisation/PLANS_PATHOLOGIES_FREQUENTES.json`, dont 121 injectés dans les leçons vides.
- **Frontend** : style vif unifié, jauges exactes, bouton d'accueil (PR #34 à #38 et #65).

## 5. Travail en attente (priorités dans l'ordre)
1. **Relectures** : relancer le relecteur distinct pour **R06** (Dyspnée) et **J69** (Pneumopathies d'inhalation), dont les relectures ont été interrompues. Les brouillons sont dans `livraisons/Livraison Claude/P-02-Pneumologie/travail/`. P-02 sera alors complet.
2. **Brouillons achevés, pas encore relus** :
   - K21 — Reflux gastro-œsophagien (G-04) ;
   - E11 — Diabète de type 2 (E-06) ;
   - D50 — Anémie par carence en fer (H-08).
3. **Fragments à produire, dans l'ordre de `organisation/FILE_FRAGMENTS_CLAUDE.json`** : G-04, E-06, H-08, G-10, M-12, R-14, O-17, O-18, M-19 et E-22, puis les fragments Codex en ordre inverse (M-21 vers I-03). Dans chaque fragment, les pathologies fréquentes passent d'abord.
4. **Réserves ouvertes** :
   - la jauge « Examen fédéral » repose sur une correspondance PROFILES établie par chapitre, trop large (44 catégories sur 45 en pneumologie) ; elle est à affiner catégorie par catégorie ;
   - la liste des pathologies fréquentes n'est étayée par l'OFS que pour 7 codes ; les autres sont à valider par une source suisse de fréquence ;
   - la complétude en CIM-11 reste à établir ;
   - aucun cours n'a été validé par un médecin.

## 6. Définition de « pathologie fréquente »
- Aucune société savante suisse ou européenne ne fixe de seuil officiel de fréquence.
- Le seul seuil officiel est celui de la **maladie rare** : moins d'une personne sur 2 000 (Europe ; OFSP, Concept national maladies rares).
- Dans MEDINA, une pathologie fréquente est une catégorie non rare retenue dans `nosology/frequency.json`. Elle n'est confirmée que lorsqu'une source de fréquence suisse est citée : OFS, Sentinella ou statistique médicale des hôpitaux.

## 7. État par fragment (catégories rédigées / total, pathologies fréquentes, examen fédéral)
| Fragment | Avancement global | Fréquentes | Examen fédéral |
|---|---|---|---|
| C-01-Cardiologie | 22 / 47 (46.81 %) | 8 / 8 | 22 / 43 |
| P-02-Pneumologie | 23 / 45 (51.11 %) | 5 / 6 | 22 / 44 |
| G-04-Gastroentérologie et hépatologie | 0 / 91 (0.0 %) | 0 / 17 | 0 / 89 |
| N-07-Néphrologie | 0 / 33 (0.0 %) | 0 / 2 | 0 / 33 |
| E-06-Endocrinologie et métabolisme | 0 / 77 (0.0 %) | 0 / 6 | 0 / 68 |
| H-08-Hématologie | 0 / 44 (0.0 %) | 0 / 4 | 0 / 42 |
| I-13-Immunologie et allergologie | 4 / 10 (40.0 %) | 2 / 2 | 4 / 7 |
| N-05-Neurologie | 0 / 116 (0.0 %) | 0 / 9 | 0 / 104 |
| R-14-Rhumatologie et orthopédie | 1 / 117 (0.85 %) | 0 / 16 | 1 / 101 |
| D-16-Dermatologie | 0 / 104 (0.0 %) | 0 / 9 | 0 / 97 |
| O-17-Oto-rhino-laryngologie et médecine bucco-dentaire | 0 / 96 (0.0 %) | 0 / 11 | 0 / 96 |
| O-18-Ophtalmologie | 0 / 58 (0.0 %) | 0 / 6 | 0 / 53 |
| G-10-Gynécologie et sénologie | 0 / 53 (0.0 %) | 0 / 9 | 0 / 47 |
| U-15-Urologie et andrologie | 0 / 46 (0.0 %) | 0 / 8 | 0 / 44 |
| O-11-Obstétrique et néonatologie | 0 / 142 (0.0 %) | 0 / 7 | 0 / 141 |
| I-03-Infectiologie | 5 / 180 (2.78 %) | 2 / 11 | 5 / 51 |
| M-12-Médecine des âges de la vie | 0 / 5 (0.0 %) | 0 / 1 | 0 / 3 |
| M-19-Médecine d’urgence, traumatologie et toxicologie | 0 / 130 (0.0 %) | 0 / 4 | 0 / 95 |
| O-09-Oncologie, génétique médicale et soins palliatifs | 0 / 59 (0.0 %) | 0 / 0 | 0 / 24 |
| D-20-Diagnostic clinique et examens complémentaires | 0 / 26 (0.0 %) | 0 / 0 | 0 / 16 |
| M-21-Médecine de premier recours et santé publique | 0 / 77 (0.0 %) | 0 / 2 | 0 / 43 |
| E-22-Éthique médicale, droit et communication | 0 / 3 (0.0 %) | 0 / 0 | 0 / 3 |

## 8. Attentes d'adaptation par type de leçon non traitée
Chaque leçon vide suit le plan monographique de base. Les pathologies fréquentes ont en plus un plan spécifique, décrit ci-dessous et déposé dans `organisation/PLANS_PATHOLOGIES_FREQUENTES.json`.
- **Socle commun** :
  - au début : définition et classification, épidémiologie suisse puis européenne, physiopathologie ;
  - à la fin : complications et pronostic, prévention et suivi, situations particulières, critères formels du diagnostic, Pareto.
- **Ajouts selon le chapitre CIM** :

| Chapitre | Ajouts au plan | Difficulté | Exigence propre |
|---|---|---|---|
| I Infections | agent pathogène, diagnostic microbiologique, anti-infectieux, déclaration OFSP, vaccination | élevée | SSI, OFSP, plan de vaccination suisse |
| II Tumeurs | carcinogenèse, stadification TNM, traitement multimodal, dépistage suisse | très élevée | ESMO, guidelines suisses, colloque pluridisciplinaire |
| XV et XVI Grossesse, nouveau-né | physiologie, surveillance materno-fœtale, médicaments compatibles | élevée | gynécologie suisse, SSP |
| XVIII Symptômes (R) | physiologie du symptôme, drapeaux rouges, démarche étagée | moyenne | approche symptomatique, renvois aux cours de maladie |
| XIX Traumatismes | mécanisme, ABCDE, imagerie, LAA | élevée | Suva, ATLS seulement comme donnée |
| Autres chapitres (maladies d'organe) | facteurs de risque, anamnèse, examen, examens complémentaires, traitements, urgences | élevée | société suisse de la spécialité, puis européenne |

- **Niveau d'exigence** : chaque cours atteint le niveau des cours P-02 relus. Le modèle de rendu est `chapters/J81/`, et le modèle de rapport est `livraisons/Livraison Claude/P-02-Pneumologie/travail/J81/rapport_relecture.md`.

## 9. Méthode de reprise
- **Organisation du travail** :
  - travailler sur une branche `claude/*` à partir de `main` ;
  - faire travailler plusieurs rédacteurs en parallèle, un par leçon, chacun avec son relecteur distinct ;
  - enregistrer, sceller, ouvrir une PR, puis fusionner une fois les contrôles verts.
- **Limite hebdomadaire de Vial** : surveillée ; tout fusionner avant d'atteindre 95 %.
- **Fin de chaque livraison** : un tableau de bord (cours, catégories, fragments, contrôles, réserves).

## 10. Procédure pas à pas pour une leçon (à suivre à la lettre)
1. **Vérifier avant d'écrire**, pour ne pas faire un double :
   - le code ou un code qu'il couvre figure-t-il dans `chapters.json` (champ `covers`) ? exemple : J40 couvre J20, J40, J41 et J42 ;
   - un dossier `livraisons/Livraison Claude/*/travail/<CODE>/` existe-t-il déjà ?
   - la fiche correspondante de l'annexe porte-t-elle une ligne « Brouillon existant » ?
   - Si l'une de ces réponses est oui, ne rien réécrire : relire ou compléter.
2. **Rédaction** dans `livraisons/Livraison Claude/<fragment>/travail/<CODE>/`, jamais directement dans `chapters/`.
   - Suivre le plan de la fiche, et ne traiter qu'en renvoi les cours du même bloc.
   - Les sous-codes de la fiche sont traités dans le cours, sans leçon séparée.
3. **Relecture** par un agent distinct de l'auteur, en deux passes. C'est lui qui injecte dans `chapters/<CODE>/` et `glossary/<code>.py`, avec des ajouts de glossaire conditionnels (`_a`).
4. **Enregistrement** : suivre la section 3, puis faire une PR et fusionner une fois les contrôles verts.

## 11. Pièges connus (déjà rencontrés : ne pas les reproduire)
- **Clés de glossaire déjà prises.** Des clés génériques existent déjà :
  - `ADA` signifie adénosine désaminase : écrire `ADA/EASD` ;
  - `ALAT` signifie alanine aminotransférase : la recommandation sur la fibrose s'écrit `ATS/ERS/JRS/ALAT` ;
  - `RECOVERY` est l'essai de chirurgie aortique (i35) : écrire « Recovery » pour l'essai COVID ;
  - `S2k` et `AWMF` sont dans t78, `FFP2` dans r04, `CFV`, `mRESVIA` et `ISHAM` dans j12, `ESGE` dans le brouillon d50.
  - Toujours vérifier `glossary/*.py` ET les glossaires des dossiers `travail/`, puis utiliser des ajouts conditionnels.
- **Sortie des constructions.** Toujours définir `MEDINA_OUT=$PWD/dist`. Sans cette variable, `build_front.py` écrit dans `/mnt/user-data/outputs` et écrase les sorties d'un autre agent.
- **Erreurs d'environnement, sans rapport avec le cours** :
  - `test_preview.py` échoue sur `preview/lesson-core.js` absent ;
  - Playwright attend parfois un autre build de Chromium : lancer `/opt/pw-browsers/chromium-1194/*/chrome` par `executable_path` ;
  - PubMed répond 203 à travers le proxy : vérifier les PMID par `esummary`.
- **`tests/audit_sciences.py`** échoue sur I50 dans un clone superficiel : c'est connu. Il faut aussi ajouter chaque nouveau code à sa liste de nouvelles productions.
- **Recommandations américaines déguisées** : la recommandation de 2020 sur la pneumopathie d'hypersensibilité est ATS/JRS/ALAT, pas ERS. Vérifier les sociétés signataires avant de qualifier un texte d'« européen ».
- **Jauges** : elles comptent les catégories, jamais les sous-codes. La jauge Examen fédéral repose sur une correspondance PROFILES établie par chapitre, trop large : elle est à affiner, sans la présenter comme officielle.
- **Push et PR** : chaque push relance les contrôles de la PR. Grouper les instantanés de brouillons, et fusionner dès que tout est vert.
- **Style** : aucun fond ivoire, beige ou gris, aucun motif ni filigrane. Les titres des cours restent rouges, comme le prévoit la règle d'origine.
- **Validation** : jamais « validé » sans médecin. La mention « revue par IA » est obligatoire.

## 12. Annexes (la tâche centrale)
- **Objectif de MEDINA** : produire les **pathologies** qui, ensemble, permettent de satisfaire **toutes** les situations PROFILES 2017 (SSP), en commençant par les pathologies fréquentes. Les SSP sont un critère de couverture, pas une unité de cours.
- **Annexe A, `ANNEXE_PATHOLOGIES_SSP.md`** (régénérée par `python3 tools/pathologies_ssp.py`) :
  - 272 pathologies dans les 22 fragments et 16 entités du volet psychiatrique couvrent les **265 SSP sur 265** ;
  - les pathologies sont classées par spécialité, dans l'ordre de production ;
  - chaque fiche donne le motif d'inclusion, l'état, la difficulté, les SSP à satisfaire dans ce cours et un plan spécifique numéroté ;
  - une matrice SSP → pathologies termine l'annexe.
  - **C'est la feuille de route de production.**
- **La psychiatrie** (F00 à F99) est hors des 22 fragments, par décision du projet. Ses 16 entités sont listées dans l'annexe A et forment un volet propre, à produire.
- **Annexe B, `ANNEXE_FEUILLE_DE_ROUTE.md`** (`python3 tools/feuille_de_route.py`) : la liste exhaustive des 1 244 catégories marquées « Examen fédéral ». C'est une référence de complétude, à traiter après l'annexe A.
- **Réserve** : la correspondance SSP → pathologie est pédagogique et non officielle, car PROFILES ne publie aucune table vers la CIM. Elle est à valider, sans la présenter comme officielle.
- Régénérer les deux annexes après chaque injection.
