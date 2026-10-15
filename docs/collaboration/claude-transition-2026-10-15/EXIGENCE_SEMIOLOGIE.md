# Exigence « sémiologie fondamentale et analytique » par leçon — S08, S05, S04, S06

Diagnostic en lecture seule de `/home/user/Medina` (main, 15 octobre 2026). Aucun fichier du dépôt n’a été modifié. Ce document ne lance aucune production médicale. Chaque modification des sources exige une mission préapprouvée dans `main`, réservée avec `tools/ai_session_guard.py acquire`, puis un worktree, une branche exclusive et une PR (contrat SSP V2, `docs/collaboration/ssp-v2/2026-10-15/README-V2.txt` §§ 4, 6 et 8). L’ajout d’une sémiologie change le contenu médical. Il ne peut donc pas passer par le reçu de publication « en l’état ».

---

## 1. Ce que fait réellement la Cardiologie (S01 / C-01-Cardiologie)

### 1.1 La « Sémiologie CS » est un module de fragment, pas un onglet de leçon

| Élément | Emplacement exact | Portée |
|---|---|---|
| Contenu du parcours | `modules/cardiovascular_cs.html` (`<template id="medina-cs-page">`, 31 Ko), `modules/cardiovascular_cs.css`, `modules/cardiovascular_cs.js` (modèles 3D, quiz, liste de contrôle) | Fragment S01 seul |
| Injection dans le frontend | `fragment_surface.py` l. 433-439 : `if fragment['id'] == 'S01'` insère CSS, HTML et JS | S01 codé en dur |
| Lien de navigation « Sémiologie CS » | `fragment_surface.py` l. 416 (`#/clinical-skills`, S01 seul) | S01 |
| Route `#/clinical-skills`, passerelle en accueil et en bas de chaque cours, palette de commandes | `shell/fragment.js` l. 127-146 | Fragments `surface: courses-v1` uniquement |
| Passerelle « Pratique clinique · Sémiologie » de l’accueil | `engine/category_organisation.js` l. 159 (`F.id === 'S01'`) | S01 |
| Preuves et captures | `audits/SCIENCES_CS_2026-10-07/README.md`, `captures/cs_thorax_1360.jpg`, `captures/cs_neck_390.jpg`, `science-cs-browser-results.json` (569 contrôles) | Livraison du 7 octobre |
| Contrôle navigateur | `tests/verify_sciences_cs.cjs` | S01 |

Dans `fragments.json`, S04, S05, S06 et S08 n’ont **pas** de champ `surface`. `shell/fragment.js` ne leur est donc pas chargé. Ils ne disposent ni de la route `#/clinical-skills`, ni du bouton « Lire le schéma en grand » des figures de sciences (`shell/fragment.js` l. 125).

### 1.2 Dans les leçons cardiologiques, l’onglet Sciences ne contient pas de sémiologie

Mesure sur `chapters/<CODE>/<CODE>_c.html`, panneau `#pS` :

| Leçon | Disciplines (`div.sci`) | Occurrences de « sémiologie » dans `_c` |
|---|---|---|
| I10 | Anatomie, Histologie, Physiologie, Biochimie et endocrinologie, Génétique | 0 |
| I48 | Anatomie, Histologie, Électrophysiologie, Biochimie de la coagulation, Génétique | 0 |
| I50 (modèle du contrat) | Anatomie, Histologie, Physiologie, Biochimie et neurohormones, Génétique | 0 |

La sémiologie propre à chaque leçon cardiologique vit dans l’onglet 1. On la trouve aux îlots 5 « Anamnèse » et 6 « Examen clinique » : par exemple `i48-5` compte 15 mots verts et `i48-6` en compte 16. Chaque signe y ouvre une fenêtre (technique, valeur, piège), selon CHAPTER_SPEC § 4 item 6 et PROMPT_MEDINA § 10. L’examen systématique de l’appareil vit dans le module de fragment.

**Conclusion.** La Cardiologie combine deux niveaux : un parcours de sémiologie analytique **par fragment**, et des signes cliquables **par leçon** dans l’onglet 1. Vial demande davantage : une sémiologie fondamentale et analytique **par leçon**, rattachée aux sciences fondamentales. Le « modèle Cardiologie » à reproduire est donc l’exigence pédagogique du parcours CS, transposée dans le contrat HTML d’une leçon :

- étapes numérotées ;
- priorité clinique dans un `alert` ;
- encadrés « Science → clinique » ;
- tableau introduit puis commenté ;
- synthèse présentée ;
- trois cas corrigés ;
- liste d’étapes ;
- sources datées.

### 1.3 Ce que le parcours CS impose (à transposer)

1. **Dix étapes** ordonnées : préparation, état général, constantes, périphérie, cou, précordium, auscultation, congestion, synthèse, entraînement. Chaque étape est une `section.cs-section`, avec un titre `h2` numéroté et des sous-titres `h3`.
2. Chaque étape s’ouvre par **le problème clinique**. Elle décrit ensuite **la technique**, puis **le mécanisme du signe**, puis **ses limites**. Exemples : « une saturation conservée ne renseigne pas sur l’hémoglobine » ; « l’irrégularité oriente, l’ECG confirme ».
3. Chaque étape se ferme par un `cs-key` : « À retenir », « Science → clinique » ou « Science → décision ».
4. Une **priorité clinique** (`cs-alert`) précède l’examen d’entraînement lorsque la situation est instable.
5. Un **tableau introduit et commenté** relie chaque repère à une question clinique (les foyers d’auscultation).
6. Une **synthèse orale exemplaire** (`cs-case`) sépare constatations, interprétation et limites.
7. **Trois cas corrigés** (`cs-quiz`) vérifient l’interprétation d’un signe et la formulation honnête d’une limite.
8. Une **liste de neuf étapes** (`cs-checklist`) sert à la station clinique. Les cases restent dans le navigateur.
9. Des **sources datées** (UNIGE dc116, Stanford Medicine 25, ESC 2024) et une portée explicite : les modèles sont pédagogiques, pas anatomiquement exacts.

### 1.4 Règles déjà en vigueur qui s’appliquent

- **CHAPTER_SPEC.md § 3** : liste fermée de classes (`ilot toc chap-body sci-body sci sci-bar key trap k alert two card t pareto-btn src pager quiz fb status chap-head code n ui w`). Elle est contrôlée par `test_v7.py` l. 19 et l. 33-34, sans style en ligne. Les identifiants portent le préfixe du code ; les clés de fenêtres commencent par `<code>-`.
- **CHAPTER_SPEC § 4 « Temps Betta » et PROMPT_MEDINA § 10, onglet 3** : un îlot par science, au moins un schéma SVG légendé, et les corrélations science → clinique, examen et traitement en `key`.
- **`tests/audit_sciences.py`** vérifie chaque `div.sci` : au moins 280 mots ; au moins une `figure` avec `figcaption` et `svg[role="img"][aria-label]` ; les quatre libellés « Science → clinique. », « Science → examen. », « Science → traitement. » et « À retenir. ». Il vérifie aussi la correspondance exacte des boutons `data-s` avec les `id` des `div.sci`.
- **`docs/STYLE_REDACTION.md`** : § 2 phrases complètes, jamais nominales ; § 3 annonce, développement, épilogue `key` ; § 4 aucun tableau ni figure sans introduction et lecture ; § 5 chaque symptôme et chaque signe est un mot vert avec une vraie fenêtre ; § 6 normal → perturbation → corrélations.
- **`docs/collaboration/CONSIGNES_INTERACTION_DENSITE_SOURCES.md`** : précisions en fenêtre après clic ; tableaux à cellules courtes ; la source primaire applicable la plus récente l’emporte ; une revue IA n’est pas une validation médicale.
- **PROMPT_VERITE.md**, rubrique 8 « Examen clinique (signes, sensibilité/spécificité si disponibles) » et rubrique 7 « Anamnèse et symptômes (fréquences) ». La règle fondamentale s’applique : aucune affirmation de mémoire, sources suisses puis européennes, aucune recommandation américaine.
- **CLAUDE.md** : « Préserver les quatre onglets » ; abréviations définies dans `glossary/<code>.py` et `build_medina.audit()` = `{}` ; deux captures réelles par leçon (`tools/capture_lecon.py`).

---

## 2. Décision structurelle : où placer l’« onglet » sémiologie

### 2.1 Options examinées

| Option | Faisabilité technique | Contrats et tests touchés | Verdict |
|---|---|---|---|
| **A. Première discipline de l’onglet Sciences** : nouveau bouton `data-s="<code>-s-semio"` en tête de `div.sci-bar`, et nouveau `div.sci` en tête de `div.sci-body` dans `<CODE>_c.html` | Moteur générique : `engine/medina_course.js` l. 75-77 bascule toute paire `button[data-s]`/`div.mc-sci`. Le premier bouton s’ouvre par défaut (`sb[0].click()`), ce qui donne une visibilité immédiate. | Aucun fichier partagé. Compatible avec `audit_sciences.py`, `test_v7.py --static`, `test_preview.py` et `tests/verify_fragment_frontends.cjs` (quatre onglets maintenus). | **Retenue.** Elle répond littéralement à « pas de sémiologie dans les sciences fondamentales » et crée un véritable onglet (`role="tab"`) par leçon. |
| B. Cinquième onglet principal `pC` | Le moteur le supporterait (`medina_course.js` l. 73 est générique). | Casse `tests/verify_fragment_frontends.cjs` l. 138, 142 et 165 (`count()===4`). Contredit `tools/cycle_claude_control.py` l. 43 (`TABS`), CHAPTER_SPEC § 2, CLAUDE.md (« quatre onglets »), `engine/reading_v3.css` l. 2, `tools/refresh_gauges.py` l. 6, `test_v7.py` l. 60 et `test_preview.py` l. 27. | Rejetée pour ce chantier. Elle exigerait une mission d’intégration sur fichiers partagés et une décision de Vial sur la « structure intouchable ». |
| C. Module de fragment de type CS (`#/clinical-skills`) pour S08, S05, S04 et S06 | Possible, sur le modèle de S01. | `fragment_surface.py` l. 416 et 433-439, `shell/fragment.js`, `engine/category_organisation.js` l. 159, `fragments.json` (`surface`), nouveaux `modules/*_cs.*`, `tests/verify_sciences_cs.cjs`. | Complément ultérieur pour l’examen systématique d’appareil (neurologique, endocrinien, rénal, hématologique et ganglionnaire). Il exige une mission partagée et ne remplace pas A. |

### 2.2 Décisions

1. **DÉCISION VIAL (15.10.2026) — option A retenue après maquettes : onglet par leçon = discipline `div.sci` placée en tête de l’onglet Sciences, ouverte par défaut.**
   - Libellé du bouton, sans abréviation (CHAPTER_SPEC § 5 item 5) : « Sémiologie fondamentale et analytique ».
   - Titre `h2` du premier îlot, formule exacte de Vial : « Pour la leçon : quelle est la sémiologie fondamentale et analytique ? ».
   - Le libellé court protège la barre à 390 px. Si Vial exige l’intitulé long sur le bouton lui-même, une capture à 390 px avec police 24 px doit le valider.
2. Les îlots 5-6 de l’onglet 1 sont **conservés**. La nouvelle discipline approfondit les **mécanismes**, la **valeur** et le **raisonnement**. Elle ne recopie pas l’anamnèse : elle y renvoie par un texte explicite (« onglet Sciences, Sémiologie »). Il n’y a **pas de lien `href` inter-onglets** : le gestionnaire `data-go` (`medina_course.js` l. 99) fait seulement défiler la page et n’ouvre pas un panneau caché.
3. Pas de liste de contrôle à cases, pas de 3D et pas de zoom de figure dans la leçon : ces éléments exigent du JavaScript partagé (§ 5). La liste d’étapes devient un `<ol>` statique. Les modèles 3D ne sont **pas** remplacés par des dessins : toute figure anatomique est un **original réel sourcé** trouvé avec Image_Clo_finder (règle de Vial, `docs/collaboration/instructions/FIGURES_ANATOMIQUES_IA_2026-10-15.md`) ; seuls les schémas non anatomiques (arbres de raisonnement, frises) peuvent être des SVG, avec valeurs et flèches sourcées.

---

## 3. Diagnostic des sept leçons (état de `main`)

Mesures obtenues par analyse lxml des sources. « Mots verts » = `button.w` dans l’îlot. « Valeur » = mentions de sensibilité, spécificité, rapport de vraisemblance ou valeur prédictive.

| Leçon | Disciplines actuelles de `#pS` | Sémiologie dédiée dans les Sciences | Sémiologie existante ailleurs | Statut des rubriques 7 et 8 dans l’audit Alpha 1 (`docs/collaboration/ssp-v2/execution/ALPHA1-CLAUDE-<CODE>-MED/rapport.md`) |
|---|---|---|---|---|
| **I61** Hémorragie intracérébrale (S08) | Anatomie ; Histologie ; Physiologie et biochimie ; Génétique | **Aucune** | `i61-a05` « Topographie et formes cliniques » : 573 mots, 0 mot vert. La sémiologie y est « déduite de l’anatomie », la source ne chiffrant pas les fréquences. `i61-a08` « Anamnèse et examen clinique » : 596 mots, 7 mots verts (GCS, NIHSS, HTIC), 0 valeur. | 7 partiel (sans fréquences) ; 8 partiel (sans sensibilité ni spécificité) |
| **G45** AIT et syndromes apparentés (S08) | Anatomie et histologie ; Physiologie ; Biochimie ; Réseaux et génétique | **Aucune** | `g45-a04` « Territoires vasculaires et tableaux focaux » (symptômes négatifs et positifs, aphasie, dysarthrie) ; `g45-a05` amaurose fugace ; `g45-a06` amnésie globale transitoire ; `g45-a08` : 720 mots, 4 mots verts, 2 mentions de valeur, 1 quiz. | 7 partiel ; 8 couvert |
| **E11** Diabète de type 2 (S05) | Biologie cellulaire ; Physiologie ; Biochimie ; Physiologie rénale | **Aucune** | `e11-5` : 410 mots, 5 mots verts (symptômes osmotiques, vision floue, neuropathie). `e11-6` : 412 mots, 5 mots verts (monofilament, diapason, index cheville-bras, acanthosis), 2 mentions de valeur. | 7 partiel (sans fréquences) ; 8 couvert |
| **E12** Diabète de malnutrition (S05) | Anatomie ; Histologie ; Physiologie ; Biochimie ; Génétique | **Aucune** | `e12-5` : 424 mots, 2 mots verts, dont une fenêtre « sémiologie de la douleur pancréatique ». `e12-6` : 238 mots, 1 mot vert. La leçon reconnaît que « les sources lues n’attribuent pas de valeur diagnostique propre aux constantes ». | 7 partiel ; 8 partiel |
| **N18** Maladie rénale chronique (S04) | Anatomie et histologie du rein ; Physiologie de filtration et transports ; Biochimie, équilibre acido-basique et minéral ; Fonctions endocrines et progression tissulaire | **Aucune** | `n18-a05` : 698 mots, 19 mots verts (prurit, nycturie, œdème, volume extracellulaire, intolérance orthostatique…), 0 valeur, 0 mécanisme explicité dans l’îlot. | 7 et 8 non distingués dans le rapport (rubriques non signalées comme lacunes) |
| **D50** Carence martiale (S06) | Physiologie ; Biochimie ; Hématologie cellulaire ; Génétique | **Aucune** | `d50-5` : 308 mots, 9 mots verts (fatigue, jambes sans repos, pica). `d50-6` : 385 mots, 3 mots verts (pâleur avec sa valeur selon mediX 08/2025, koilonychie, chéilite). C’est la meilleure base mécaniste des sept. | 7 partiel ; 8 couvert |
| **C77** Métastase ganglionnaire (S06) | Anatomie ; Histologie ; Physiologie ; Biochimie et biologie moléculaire | **Aucune** | `c77-5` : 243 mots (durée de plus de deux semaines selon Swiss Medical Weekly 2024, signes d’alarme). `c77-6` : 297 mots, 3 mots verts (caractérisation ganglionnaire, examen ORL, fosse sus-claviculaire). | 7 couvert ; 8 partiel (seuils de taille, examen gynécologique) |

**Constat commun.** Aucune des sept leçons ne possède de discipline sémiologique dans les Sciences ; le mot « sémiologie » apparaît au plus une fois par fichier. Ce qui existe est une **anamnèse et un examen descriptifs** de l’onglet 1. Il leur manque systématiquement :

1. le **mécanisme physiopathologique de chaque signe** (sauf D50, en partie) ;
2. la **valeur sémiologique** chiffrée, ou l’absence de chiffre déclarée avec la source cherchée ;
3. le **regroupement syndromique** explicite ;
4. le **raisonnement du signe vers le diagnostic** ;
5. l’**examen systématique de l’appareil** en étapes ;
6. une **synthèse présentée** ;
7. les **cas corrigés** consacrés au signe ;
8. une **figure sémiologique**.

---

## 4. Le livrable exigé

### 4 (a) Définitions opérationnelles

**Sémiologie fondamentale.** C’est l’étude de chaque manifestation isolée de la maladie étudiée. Pour être acceptée, chaque entrée (symptôme ou signe physique) comporte six éléments :

1. **Définition** exacte du symptôme ou du signe, et sa distinction avec un terme voisin (par exemple « aphasie » ou « dysarthrie »).
2. **Normal d’abord.** L’entrée décrit le fonctionnement ou la valeur normale et ce que l’examen montre chez le sujet sain (STYLE_REDACTION § 6 ; CLAUDE.md, règle 7).
3. **Technique** de recherche, pour un signe : position, geste, matériel, seuil et unité. Pour un symptôme, ce sont les questions de caractérisation (installation, durée, chronologie, facteurs, signes associés).
4. **Mécanisme physiopathologique** du signe, en chaîne causale normal → perturbation → manifestation. Le mécanisme est relié à une science de la leçon (anatomie, physiologie, biochimie…).
5. **Valeur sémiologique.** L’entrée donne la fréquence dans la maladie et la sensibilité, la spécificité ou le rapport de vraisemblance, avec la population et la source datée. Si les sources lues ne chiffrent pas, la leçon l’écrit explicitement et `rapport.md` consigne la `LACUNE` (modèle : `i61-a05`, `e12-6`). Un chiffre inventé ou importé d’une autre population est interdit.
6. **Piège et limite** : faux positifs, faux négatifs, conditions qui dégradent la fiabilité (par exemple la pâleur cutanée peu fiable selon mediX, D50).

**Sémiologie analytique.** C’est l’analyse sémiologique qui transforme des constatations en hypothèse. Elle comporte trois volets :

1. **Regroupement syndromique.** Les signes sont réunis en syndromes nommés : constituants, mécanisme commun, orientation topographique ou étiologique. Exemples : syndrome d’hypertension intracrânienne, syndrome anémique, syndrome cardinal hyperglycémique, syndrome urémique, syndrome tumoral ganglionnaire.
2. **Raisonnement du signe vers le diagnostic.** Il suit cinq étapes :
   1. reconnaître d’abord la gravité (`alert`) ;
   2. qualifier le signe ;
   3. le localiser, c’est-à-dire dire quel organe ou quel niveau lésionnel il désigne ;
   4. le regrouper avec les autres signes ;
   5. hiérarchiser les hypothèses par gravité et par fréquence, puis désigner l’examen qui tranche.

   Chaque différentiel porte un discriminant sourcé (README-V2 § 7). La force d’un signe isolé et celle d’une association de signes sont distinguées.
3. **Examen clinique systématique de l’appareil.** C’est la séquence complète et reproductible de l’examen de l’appareil concerné, transposée du parcours CS en étapes numérotées. Elle va de la préparation et de l’état général aux constantes, puis aux gestes propres à l’appareil, et se termine par la synthèse. La synthèse sépare constatations, interprétation et limites, comme `cs-case`.

### 4 (b) Structure HTML exacte (dans `<CODE>_c.html`, contrat fermé)

Il faut insérer **en tête** de `div.sci-bar` et **en tête** de `div.sci-body` du panneau `#pS` (exemple avec `n18`) :

```html
<!-- barre : premier bouton -->
<button role="tab" aria-selected="true" aria-controls="n18-s-semio" data-s="n18-s-semio">Sémiologie fondamentale et analytique</button>
<!-- l’ancien premier bouton passe à aria-selected="false" -->

<!-- corps : première discipline -->
<div class="sci" id="n18-s-semio">

<section class="ilot" id="n18-sm-1"><h2><span class="n">1</span>Pour la leçon : quelle est la sémiologie fondamentale et analytique ?</h2>
<p>Annonce : le problème clinique, et les signes qui décident (sans « cet îlot présente »).</p>
<div class="alert"><b>Priorité clinique.</b> Signes de gravité, seuil, délai, action.</div>
<div class="key"><b>À retenir.</b> …</div></section>

<section class="ilot" id="n18-sm-2"><h2><span class="n">2</span>Sémiologie fondamentale : les symptômes</h2>
<p>Introduction du tableau (question clinique posée).</p>
<table class="t"><tr><th>Symptôme</th><th>Mécanisme</th><th>Fréquence ou valeur (source)</th><th>Piège</th></tr>
<tr><td><button class="w" data-k="n18-sm-prurit">Prurit (mécanisme et valeur)</button></td><td>…</td><td>… ou « non chiffré dans les sources lues »</td><td>…</td></tr></table>
<p>Lecture du tableau : ce qu’il faut regarder d’abord, l’erreur fréquente, un patient lu à travers le tableau.</p>
<div class="key"><b>À retenir.</b> …</div></section>

<section class="ilot" id="n18-sm-3"><h2><span class="n">3</span>Sémiologie fondamentale : les signes physiques</h2>
<h3>Signe A — technique, mécanisme, valeur, piège</h3><p>…</p>
<figure><svg role="img" aria-label="Description complète du schéma" viewBox="0 0 640 360">…</svg>
<figcaption>Figure — Du mécanisme au signe. Lecture : …  Schéma pédagogique, non à l’échelle.</figcaption></figure>
<p>Lecture de la figure.</p>
<div class="trap"><span class="k">Piège</span> …</div>
<div class="key"><b>À retenir.</b> …</div></section>

<section class="ilot" id="n18-sm-4"><h2><span class="n">4</span>Sémiologie analytique : regrouper en syndromes</h2>
<p>Introduction.</p>
<table class="t"><tr><th>Syndrome</th><th>Signes constitutifs</th><th>Mécanisme commun</th><th>Orientation</th></tr>…</table>
<p>Lecture.</p><div class="key"><b>À retenir.</b> …</div></section>

<section class="ilot" id="n18-sm-5"><h2><span class="n">5</span>Du signe au diagnostic</h2>
<ol><li>Je reconnais la gravité : …</li><li>Je qualifie le signe : …</li><li>Je le localise : …</li><li>Je regroupe : …</li><li>Je hiérarchise et je choisis l’examen qui tranche : …</li></ol>
<div class="two"><div class="card"><b>Oriente vers la maladie</b><p>…</p></div><div class="card"><b>Oriente ailleurs</b><p>Discriminant sourcé…</p></div></div>
<div class="key"><b>À retenir.</b> …</div></section>

<section class="ilot" id="n18-sm-6"><h2><span class="n">6</span>Examen clinique systématique de l’appareil</h2>
<ol><li>Préparation, accord, exposition, hygiène.</li><li>État général et signes d’instabilité.</li><li>Constantes avec technique.</li><li>… gestes propres à l’appareil …</li><li>Synthèse.</li></ol>
<div class="card"><b>Exemple de présentation.</b><p>« Constatations… Interprétation… Limites… Examens qui répondent à l’incertitude… »</p></div>
<div class="key"><b>Science → clinique.</b> …</div>
<div class="key"><b>Science → examen.</b> …</div>
<div class="key"><b>Science → traitement.</b> …</div>
<div class="key"><b>À retenir.</b> …</div></section>

<section class="ilot" id="n18-sm-7"><h2><span class="n">7</span>S’entraîner : trois cas corrigés</h2>
<div class="quiz ui"><p>Cas 1 — …</p><button data-ok="0">…</button><button data-ok="1">…</button><p class="fb" hidden>Correction raisonnée : mécanisme, valeur, limite.</p></div>
<!-- cas 2 et 3 ; au moins un cas porte sur la formulation honnête d’une limite -->
<div class="src"><b>Sources de la sémiologie</b> (consultées le JJ.MM.AAAA) : …</div>
</section>

</div>
```

Contraintes de forme :

- **Classes** : uniquement la liste fermée. `table.t`, `div.trap` + `span.k`, `div.two` + `div.card` et `div.src` en font partie. `<ol>` n’a pas de classe.
- **Identifiants et clés.** Le `div.sci` prend l’identifiant `<code>-s-semio` et les îlots `<code>-sm-1` à `-7`. Les fenêtres prennent les clés `<code>-sm-<signe>`, dans `<CODE>_pop3.html` (nouveau fichier) ou dans les fichiers pop existants.
- **Placement des libellés.** Les quatre libellés exigés par `audit_sciences.py` se trouvent dans le `div.sci` (îlot 6). Au moins une `figure` conforme est présente.
- **Abréviations** : chaque nouveau sigle (GCS, NIHSS, HTIC, DFGe, IMC…) a sa clé dans `glossary/<code>.py`.
- **Pareto.** Le Pareto des sciences reste en fin de dernière discipline. Son `data-cover` peut inclure les `<code>-sm-*`.
- Pas de style en ligne, pas de JavaScript.
- **Rédaction** : STYLE_REDACTION §§ 2-6. Chaque phrase est complète. Chaque tableau et chaque figure est introduit puis lu. Chaque symptôme et chaque signe est un mot vert relié à une fenêtre réelle (technique, mécanisme, valeur, piège, source).
- **Volume.** Aucun plafond. Le minimum mesurable est celui d’`audit_sciences.py` (280 mots par discipline). En pratique, sept îlots denses, sans redite de l’onglet 1.

### 4 (c) Grille d’audit binaire (à ajouter à chaque `ALPHA*-…-MED/rapport.md` comme rubrique « 21 — Sémiologie fondamentale et analytique »)

Chaque critère reçoit oui ou non, avec l’identifiant HTML comme preuve. Un « non » sur SEM-01 à SEM-04, SEM-08, SEM-13 ou SEM-19 est bloquant.

| N° | Critère vérifiable |
|---|---|
| SEM-01 | `#pS .sci-bar` contient en **première** position un bouton `data-s="<code>-s-semio"` intitulé « Sémiologie fondamentale et analytique ». Le `div.sci` homonyme existe. |
| SEM-02 | Le premier `h2` du `div.sci` reprend la formule « Pour la leçon : quelle est la sémiologie fondamentale et analytique ? ». |
| SEM-03 | Critères de `tests/audit_sciences.py` satisfaits : au moins 280 mots, figure accessible et légendée, quatre libellés. **Précision du coordinateur (15.10.2026)** : une figure faite uniquement d'images réelles avec `alt` + `figcaption` attribuée est accessible ; l'erreur « figure sans légende ou nom accessible » qu'elle seule déclenche est un faux positif connu du test (antérieur à la règle de Vial), consigné dans `integration/controles.json`, et ne rend pas SEM-03 bloquant. Tout SVG ajouté dans une telle figure pour satisfaire le test est interdit. Correction du test demandée en mission partagée. |
| SEM-04 | `python3 test_v7.py --static <CODE>` affiche OK : classes fermées, aucune fenêtre manquante, clés préfixées, glossaire `{}`. |
| SEM-05 | Un tableau des symptômes existe, avec les colonnes mécanisme, fréquence ou valeur et piège. Il est introduit et commenté. |
| SEM-06 | Chaque signe physique cité porte sa **technique** : geste, position, seuil et unité. |
| SEM-07 | Chaque symptôme et chaque signe porte un **mécanisme** causal en phrase complète, rattaché à une science de la leçon. |
| SEM-08 | Chaque valeur chiffrée (fréquence, sensibilité, spécificité, rapport de vraisemblance) a sa population et sa source datée dans `sources.json`. Les valeurs absentes sont écrites « non chiffrées dans les sources lues » et consignées en `LACUNE`. |
| SEM-09 | Le normal (signe absent, valeur normale) précède le pathologique pour chaque geste. |
| SEM-10 | Au moins un piège ou une limite figure par signe majeur (`trap` ou phrase explicite). |
| SEM-11 | Un tableau des syndromes existe (constituants, mécanisme commun, orientation). |
| SEM-12 | Le raisonnement du signe vers le diagnostic suit cinq étapes ordonnées (`<ol>`), dans l’ordre : gravité, qualification, localisation, regroupement, hiérarchie et examen qui tranche. |
| SEM-13 | Une priorité clinique (`div.alert`) donne seuil, délai et action, et reste cohérente avec l’`alert` de l’onglet 1. |
| SEM-14 | Chaque différentiel cité porte un discriminant sourcé. Il n’y a pas d’énumération sans critère. |
| SEM-15 | L’examen systématique de l’appareil est numéroté de la préparation à la synthèse. |
| SEM-16 | Une synthèse présentée (`div.card`) sépare constatations, interprétation et limites. |
| SEM-17 | Trois cas corrigés (`div.quiz`) sont présents, dont au moins un sur la valeur d’un signe et un sur la formulation d’une limite. |
| SEM-18 | Chaque mot vert sémiologique ouvre une fenêtre réelle (technique, mécanisme, valeur, piège, source). La vérification se fait au navigateur. |
| SEM-19 | Aucune affirmation sans source lue ; sources suisses puis européennes ; aucune recommandation américaine utilisée comme référence. Une ressource américaine de technique (comme Stanford 25 en S01) est signalée comme telle et ne fixe aucun seuil décisionnel. |
| SEM-20 | Chiffres, seuils et définitions identiques entre la sémiologie, l’onglet 1, les fenêtres et le Pareto. |
| SEM-21 | Pas de redite de l’onglet 1 : la discipline approfondit mécanisme, valeur et raisonnement. Les îlots 5-6 restent intacts ou y renvoient par texte. |
| SEM-22 | Le libellé de la barre est lisible à 390 px avec police 24 px, sans débordement horizontal (capture réelle). |
| SEM-23 | Deux captures réelles sont prises : sémiologie ouverte, et fenêtre d’un signe ouverte (`tools/capture_lecon.py`). |
| SEM-24 | Le statut reste « revue IA, aucune validation médicale humaine » ; aucune certification n’est revendiquée. |

### 4 (d) Plan d’application aux sept leçons

**Chemins modifiés par leçon.** Ce sont uniquement les chemins propres à la mission :

- `chapters/<CODE>/<CODE>_c.html` : bouton et `div.sci` en tête de `#pS` ;
- `chapters/<CODE>/<CODE>_pop3.html` (nouveau), ou `_popN` existant : fenêtres `<code>-sm-*` ;
- `glossary/<code>.py` : nouveaux sigles ;
- `docs/collaboration/ssp-v2/execution/<MISSION>/` : `recherche.md` avec matrice et rubrique 21, `sources.json`, `rapport.md`, captures.

Les fichiers `_a`, `_b` et `_d` ne sont pas touchés, sauf une phrase de renvoi éventuelle dans les îlots 5-6.

**Ordre recommandé**, de la base la plus réutilisable à la plus lacunaire : D50, E11, C77, G45, N18, I61, E12.

| Leçon | Sémiologie fondamentale à écrire (sources à lire) | Syndromes et raisonnement | Examen systématique de l’appareil |
|---|---|---|---|
| **D50** | Symptômes d’anémie et de carence tissulaire (`d50-5`). Pâleur avec sa valeur (mediX 08/2025, déjà lu). Koilonychie, chéilite, glossite, alopécie, jambes sans repos, pica et pagophagie, avec mécanisme (hémoglobine, enzymes ferriques). | Syndrome anémique et sa compensation ; carence martiale sans anémie ; orientation vers la perte (gynécologique, digestive). Discriminants contre l’anémie inflammatoire et la thalassémie. | Tolérance (fréquence cardiaque, pression, fréquence respiratoire, insuffisance cardiaque), téguments et phanères, cavité buccale, abdomen et toucher rectal selon l’indication, synthèse. |
| **E11** | Syndrome cardinal (`e11-5`) et mécanisme du seuil rénal. Vision floue. Acanthosis. Monofilament, diapason, pouls et index cheville-bras (`e11-6`). Signes de neuropathie autonome. Fond d’œil. Valeurs à lire (SSED). | Syndrome cardinal hyperglycémique ; signes d’insulinorésistance ; pied à risque ; signes de décompensation (déshydratation, cétose). Discriminants contre le type 1, le LADA et le diabète secondaire. | Examen annuel du diabétique : anthropométrie, pression couchée et debout, examen cardiovasculaire, pieds (inspection, pouls, monofilament, diapason), peau et sites d’injection, synthèse. |
| **C77** | Caractérisation ganglionnaire : taille, consistance, mobilité, sensibilité, siège. Durée de plus de deux semaines (Swiss Medical Weekly 2024, déjà lu). Ganglion sus-claviculaire. Signes d’alarme. | Adénopathie localisée ou généralisée ; territoires de drainage et primitif ; syndrome tumoral ; signes généraux. Discriminants contre une cause infectieuse ou un lymphome. | Palpation de toutes les aires ganglionnaires, examen ORL complet (`c77-6`), seins, testicules ou examen gynécologique (lacune signalée par l’audit), peau, foie et rate, synthèse. |
| **G45** | Symptômes négatifs et positifs (`g45-a04`), aphasie et dysarthrie, amaurose fugace (`g45-a05`), amnésie globale transitoire (`g45-a06`). Mécanisme ischémique et marche des symptômes. Valeur (2 mentions existantes à étendre). | Syndromes carotidien et vertébrobasilaire ; chronologie (installation brutale contre marche migraineuse ou crise) ; imitateurs, avec discriminants sourcés (hypoglycémie, aura, crise focale). | Examen neurologique focal systématique : conscience, langage, champ visuel, oculomotricité, face, force, sensibilité, coordination, marche. Auscultation cervicale et cardiaque. Synthèse. |
| **N18** | Syndrome urémique, prurit, nycturie, intolérance orthostatique, œdème et volume extracellulaire (`n18-a05`, 19 mots verts sans mécanisme). Mécanismes à rattacher aux disciplines S02 et S03 de la leçon. Valeur : sources SSN 2025 et KDIGO déjà lues, à vérifier. | Rétention hydrosodée ; syndrome urémique ; signes de maladie causale (systémique, polykystose) ; signes d’alerte (hyperkaliémie sans signe clinique fiable, à sourcer). | Pression avec technique, estimation de la volémie, œdèmes, auscultation, palpation des reins et souffle abdominal, peau, fond d’œil selon l’indication, bandelette urinaire comme geste au lit, synthèse. |
| **I61** | Signes déduits de la topographie (`i61-a05`) : capsulaire, thalamique, putaminal, cérébelleux, lobaire, tronc. Céphalée, vomissements, troubles de la vigilance. GCS et NIHSS. Valeur : `LACUNE` déjà constatée (rubrique 8 partielle), à rechercher. | Syndrome d’hypertension intracrânienne ; syndromes d’engagement ; syndromes topographiques ; hémorragie ou ischémie (aucun signe clinique ne tranche : l’imagerie tranche). | Examen neurologique d’urgence : vigilance (GCS), pupilles, déficit (NIHSS), signes méningés, signes d’engagement, constantes (pression). Synthèse et transmission. |
| **E12** | Dénutrition (IMC, signes carentiels), douleur pancréatique (fenêtre existante), stéatorrhée, absence de cétose. Valeur : `LACUNE` explicite déjà écrite dans `e12-6`. | Syndrome de malabsorption et de pancréatopathie ; phénotype de malnutrition ; discriminants contre le type 1 (cétose, anticorps), le MODY et la lipodystrophie. | Anthropométrie et courbes (enfant), état nutritionnel, signes carentiels, abdomen, signes de complications. Synthèse. |

**Pour chaque mission** :

1. recherche ciblée : sources suisses (SSED, SSN, SGH/SSH, enseignement facultaire suisse de sémiologie), puis européennes ;
2. matrice à 20 rubriques plus la rubrique 21 ; `tools/betta_verite.py` compte les lignes « au moins 20 » (l. 33) et accepte une 21ᵉ ;
3. rédaction ;
4. contrôles : `test_v7.py --static`, `tests/audit_sciences.py --codes`, `test_preview.py`, build du fragment, `tests/verify_fragment_frontends.cjs` ;
5. deux captures ;
6. PR.

Aucune source sémiologique propre à la neurologie, l’endocrinologie, la néphrologie ou l’hématologie n’est aujourd’hui citée dans le dépôt. Les seules sources sémiologiques présentes (UNIGE dc116, Stanford Medicine 25) concernent l’examen cardiovasculaire. Elles restent à identifier et à lire pour chaque leçon.

### 4 (e) Ce qui exige une mission d’intégration sur fichiers partagés

| Besoin | Fichiers partagés | Nécessaire à l’option A ? |
|---|---|---|
| Rendre l’exigence contrôlable automatiquement : discipline `-s-semio` obligatoire pour S04, S05, S06 et S08, présence de `ol`, `alert`, trois `quiz` et deux `table.t` | `tests/audit_sciences.py` (nouvelle règle par fragment) | Recommandé, non bloquant |
| Inscrire la règle dans les contrats | `CHAPTER_SPEC.md` § 4 Temps Betta, `PROMPT_MEDINA.md` § 10 onglet 3, `docs/STYLE_REDACTION.md` § 6, `docs/collaboration/betta/PROMPT_VERITE.md` § 3 (rubrique 21), `tools/betta_verite.py` (contrôle de la rubrique 21), prompt commun SSP V2 `docs/collaboration/ssp-v2/2026-10-15/prompt-commun-ia.yaml` | Oui, pour que l’exigence s’impose aux autres IA et aux 154 leçons à produire |
| Zoom « Lire le schéma en grand » pour S04, S05, S06 et S08 | `shell/fragment.js` l. 125 (S01 et autres `courses-v1` seulement) ou `engine/category_organisation.js` ; `fragments.json` (`surface`) | Non (confort) |
| Liste de contrôle à cases mémorisées, comme `cs-checklist` | JavaScript partagé (`engine/medina_course.js` ou module dédié) et nouvelle classe hors liste fermée (`test_v7.py` l. 19) | Non : un `<ol>` statique la remplace |
| Parcours d’examen systématique par fragment avec modèles 3D (neurologique, endocrinien, rénal, hématologique et ganglionnaire) | Nouveaux `modules/<appareil>_cs.{html,css,js}`, `fragment_surface.py` l. 416 et 433-439 (généraliser `== 'S01'`), `shell/fragment.js` l. 127-146, `engine/category_organisation.js` l. 159, `tests/verify_sciences_cs.cjs` | Non : complément de fragment |
| Cinquième onglet principal (option B) | `tests/verify_fragment_frontends.cjs` l. 138, 142 et 165 ; `tools/cycle_claude_control.py` l. 43 ; `test_v7.py` l. 60 ; `test_preview.py` l. 27 ; `tools/refresh_gauges.py` ; `engine/reading_v3.css` ; `CHAPTER_SPEC.md` ; CLAUDE.md | Rejeté. Il exigerait aussi une décision explicite de Vial sur la structure « intouchable ». |
| Liens directs de l’onglet 1 vers la sémiologie (ouvrir `#pS` puis la discipline) | `engine/medina_course.js` l. 99 (gestionnaire `data-go`) | Non : renvoi textuel |
| Clés de glossaire globales ou figures partagées entre leçons | `glossary/` commun, `assets/` partagés | Seulement si une figure ou un sigle est mutualisé |

**Gouvernance.** Les sept leçons sont attribuées à Claude dans le plan V2 (`attributions-audit.csv` : SSPV2-AUDIT-S08-G45, -I61, S05-E11, -E12, S04-N18, S06-D50, -C77, toutes `PLANIFIE_NON_LANCE`). Les missions ALPHA1-CLAUDE-<CODE>-MED existantes sont des audits : elles n’autorisent pas l’ajout d’une discipline. Il faut donc une mission d’enrichissement nouvelle, approuvée dans `main`, par leçon, avec ses chemins propres. Les fichiers partagés de § 4 (e) passent par une mission d’intégration distincte, un intégrateur à la fois.
