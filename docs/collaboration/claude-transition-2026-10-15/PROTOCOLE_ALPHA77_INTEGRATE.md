# Protocole ALPHA77-CLAUDE-<CODE>-INTEGRATE — 2 agents par leçon (ordre Vial, 15.10.2026)

Mission déjà acquise et démarrée (garde `start` réussie). Worktree et branche exacts dans ta consigne ; tu n'en sors jamais. Base `abd681e5`.

## Lectures obligatoires (dans le worktree, état de main)
- `AGENTS.md` (sections Sémiologie obligatoire, Moteurs indépendants, Figures anatomiques) ; `.medina/missions/ALPHA77-CLAUDE-<CODE>-INTEGRATE.json` (chemins autorisés).
- `docs/collaboration/instructions/SEMIOLOGIE_FONDAMENTALE_ANALYTIQUE_2026-10-15.yaml` (contrat : 1er sous-onglet de `.sci-bar`, ouvert par défaut, 9 sections `data-semiology`, repère clinique `data-semiology-clinical` dans pA, preuves de clôture SEMIO).
- `docs/collaboration/instructions/FIGURES_ANATOMIQUES_IA_2026-10-15.md`, `docs/collaboration/instructions/IMAGE_CODEX_FINDER.md`, `.claude/skills/image-clo-finder/SKILL.md`.
- `docs/collaboration/instructions/MOTEURS_INDEPENDANTS_7_STARTER_2026-10-15.md`, `tools/alpha_publication.py` et `tests/test_alpha_publication.py` (format exact du reçu Alpha et des preuves).
- Rapports d'audit fusionnés : `docs/collaboration/ssp-v2/execution/ALPHA1-CLAUDE-<CODE>-MED/` et `…-LANG/`.
- `docs/collaboration/betta/PROMPT_VERITE.md`, `docs/STYLE_REDACTION.md`, `CHAPTER_SPEC.md`.
- Spécification d'appui (hors dépôt) : /tmp/claude-0/-home-user-Medina/32d77524-f01f-5b7e-92b4-188dd9e32b87/scratchpad/EXIGENCE_SEMIOLOGIE.md (§ 4 b structure HTML, § 4 c grille SEM-01…SEM-24).

## Interdits
Aucun fait médical de mémoire ; sources suisses puis européennes, jamais une recommandation américaine comme conduite ; médicaments = FI suisse (`tools/swissmedic_fi.py`, AmiKo/Compendium) datée. Aucune anatomie dessinée ou générée par IA (SVG compris) ; seuls des schémas non anatomiques sourcés. Aucun fichier hors des chemins de la mission. Pas de force-push, pas de `main`. Aucune validation médicale humaine prétendue. Aucun identifiant de modèle dans les fichiers.
Choix éditoriaux en attente, NE PAS appliquer : espaces insécables globales, « fibrillation atriale/auriculaire », groupe `LIENS` d'E11 ; les lister comme différés.

## Rôles (un seul auteur par fichier)
### Agent P — préparateur et contrôleur
Écrit seulement dans `docs/collaboration/ssp-v2/execution/ALPHA77-CLAUDE-<CODE>-INTEGRATE/prep/` (et plus tard `…/revue/`) et `assets/img/<code>/alpha/claude/`.
Phase 1 :
1. Images : inventaire (`python3 tools/image_clo_finder.py inventory <CODE>`) croisé avec la clé `figures` du rapport MED. Pour chaque figure `ANATOMIQUE_IA` (MAJEUR) ou `ORIGINE_INCONNUE`, et pour chaque figure utile à la sémiologie : candidats via `python3 tools/image_clo_finder.py candidates "<requête précise en anglais>" --direct` (cache commun ; une requête par besoin ; jamais de boucle ; erreur ⇒ autre fournisseur ou lacune). Ouvrir la page source, vérifier la licence PROPRE à la figure, l'auteur, la provenance humaine, puis un seul téléchargement ciblé de l'original retenu dans `assets/img/<code>/alpha/claude/` ; vérifier visuellement l'image (outil Read) : exactitude anatomique et adéquation à la légende. Produire `prep/figures.json` (pour chaque figure : figure remplacée, fichier, page, original_url, auteur, licence, licence_url, attribution, sha256, contrôle visuel, réserves) et `prep/figures.html` (blocs `<figure>` prêts, légende + attribution).
2. Sémiologie : recherche réellement lue (sémiologie universitaire et recommandations suisses puis européennes ; revues). Rédiger `prep/semiologie_sciences.html` : le sous-onglet complet conforme au contrat (bouton `<code>-tab-semio`, panneau `<code>-s-semio`, titre exact « Pour la leçon : quelle est la sémiologie fondamentale et analytique ? », 9 sections `data-semiology` normal/signs/mechanisms/examination/interpretation/differentials/urgency/limits/sources avec contenu substantiel propre à la leçon, cas corrigé). Il doit aussi passer `tests/audit_sciences.py` (≥ 280 mots, `figure`+`figcaption`+`svg[role=img][aria-label]` NON anatomique, encadrés « Science → clinique. », « Science → examen. », « Science → traitement. », « À retenir. »). Rédiger `prep/semiologie_clinique.html` (bloc pA `data-semiology-clinical="<CODE>"` : symptômes, anamnèse analytique, signes, examen, discrimination, urgences). `prep/sources_semiologie.json` au format `source_contract.each_claim` du contrat. Classes HTML de la liste fermée, identifiants préfixés par le code en minuscules, abréviations avec clé de glossaire proposée (`prep/glossaire_ajouts.json`).
3. Écrire `prep/READY.json` (liste des livrables, lacunes), commit « Préparation Alpha77 <CODE> : images et sémiologie », push sur la branche. Réponse finale courte.
Phase 2 (sur message du coordinateur, après intégration par W) : revue finale indépendante des fichiers finaux → `revue/MED.json`, `revue/LANG.json`, `revue/SEMIO.json` au format `closure_evidence` du contrat (empreintes réelles, `requirements_reviewed.fundamental_analytical_semiology: true`, `medical_human_validation: false`, `unresolved_blockers` vide seulement si c'est vrai), commit, push.

### Agent W — rédacteur et intégrateur (seul auteur de `chapters/<CODE>/` et `glossary/<code>.py`)
Phase 1 : corriger la leçon d'après les rapports fusionnés.
- Tous les MAJEUR traités (correction sourcée, ou justification écrite si non fondé), MINEUR clairement corrects appliqués, ENRICHISSEMENTS pertinents intégrés depuis `propositions/` ; les `renvois_medicaux` du LANG tranchés avec les sources du MED.
- Propositions LANG `fond_inchange` locales appliquées (vérifier unicité de `ancien` au moment d'appliquer), sauf choix différés ci-dessus.
- Contrôles : `python3 -c "import build_medina as B; print(B.audit())"` (doit être `{}` pour la leçon), `python3 test_v7.py --static <CODE>` si disponible, `python3 tests/audit_sciences.py` si applicable.
- Commit « Corrections Alpha77 <CODE> d'après les audits MED et LANG », push. Journal `docs/collaboration/ssp-v2/execution/ALPHA77-CLAUDE-<CODE>-INTEGRATE/integration/corrections.json` (constat → action → fichier/ancre → source). Réponse finale courte.
Phase 2 (sur message du coordinateur, quand `prep/READY.json` existe) : intégrer la sémiologie (1er bouton `.sci-bar` sélectionné, les autres `aria-selected="false"`), le bloc clinique dans pA, les figures validées (remplacement des anatomies IA), les clés de glossaire ; contrôles complets, construction `python3 build_front.py --fragment <Sxx>` (sortie `MEDINA_OUT` dans le scratchpad, jamais dans le dépôt), rendu Chromium (`executable_path=/opt/pw-browsers/chromium-1194/chrome-linux/chrome`) : ouverture, fenêtre, sous-onglet sémiologie, mobile 390 px ; aucune erreur JavaScript. Commit, push.
Phase 3 (après revue P) : reçu Alpha `organisation/alpha-publications/Claude/<CODE>/…` conforme à `tools/alpha_publication.py` (phase completed, audits MED/LANG/SEMIO = fichiers `revue/`), vérification `python3 tools/alpha_publication.py --before <base> --after HEAD` réussie, commit, push.

## Visibilité Codex
Chaque commit cite la mission. Les fichiers `prep/READY.json`, `integration/corrections.json`, `revue/*.json` et le reçu Alpha sont la trace lisible par Codex. Mention finale : « Revue IA, distincte d'une validation médicale humaine ».
Commits terminés par :
Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_012rLPEdW6E6hLqqjusnCoMF

## Cohabitation des deux agents dans le même worktree
- `git add` uniquement tes propres chemins, jamais `git add -A`.
- Si `.git/index.lock` existe, attendre quelques secondes puis réessayer (l'autre agent committe) ; ne jamais supprimer ce verrou.
- Avant chaque push : `git pull --rebase origin <ta branche>` (seuls vos deux commits y figurent), puis `git push -u origin <ta branche>`.
- Fragments : I61, G45 → S08 ; E11, E12 → S05 ; N18 → S04 ; D50, C77 → S06.
- Interdit dans le worktree partagé : git stash, git checkout -- ., git reset, git clean. Comparer à la base via `git show abd681e5:<chemin>` vers le scratchpad.

## Décision coordinateur — `tests/audit_sciences.py` et images réelles
Ce test (non branché sur la CI ni sur `tools/alpha_publication.py`) exige un `svg[role=img][aria-label]` dans CHAQUE figure des Sciences : il est antérieur à la règle de Vial et rejette à tort une micrographie ou photographie réelle. Règle : (1) chaque discipline garde au moins une figure SVG non anatomique sourcée, et le test doit passer pour tout le reste ; (2) une figure à image réelle porte `<img alt="…">` + `<figcaption>` avec attribution ; l'erreur « figure sans légende ou nom accessible » qu'elle seule déclenche est consignée comme faux positif connu dans `integration/controles.json` ; (3) interdiction absolue d'ajouter un SVG factice pour satisfaire le test. Une mission partagée est demandée pour accepter `img[alt]`.
- Précision : un SVG ajouté DANS une figure d'image réelle pour satisfaire le test est aussi un contournement, même s'il porte des données ; un schéma de données va dans sa propre figure, avec des valeurs tirées d'une source clinique lue (jamais d'une page Commons).
- FICHIERS ADMIS (tools/alpha_publication.py, core_paths) : <CODE>_a, _b, _c, _d, _pop1, _pop2 et glossary/<code>.py. Aucun _pop3 : les fenêtres de sémiologie vont dans _pop1 ou _pop2.
- Pas de Pareto (data-cover) sur une section data-semiology : pareto_ratios ne la trouve pas.
- User-Agent des requêtes : uniquement `MEDINA-ImageCloFinder/0.1 (+https://github.com/vialdjoukang-spec/Medina)` — jamais d'identifiant ou d'adresse personnelle.
