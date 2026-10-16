# Protocole Audit Alpha tour 1 — Claude (ordre de Vial, 15.10.2026)

Tu exécutes UNE mission déjà acquise et démarrée (`tools/ai_session_guard.py start` réussi). Ton worktree et ta branche sont fixés dans ta consigne ; tu ne travailles que là.

## Interdits absolus
- Ne jamais modifier `chapters/`, `glossary/`, ni aucun fichier hors de ton dossier réservé `docs/collaboration/ssp-v2/execution/<ID_MISSION>/`.
- Ne jamais pousser ailleurs que sur ta branche exacte ; jamais de force-push, jamais `main`.
- Rien de mémoire : un fait sans source lue est une LACUNE, pas une affirmation. Aucun audit, lecture ou vérification non réalisés ne sont présentés comme faits.
- Aucune recommandation américaine comme référence de conduite (sources suisses → européennes ; revues et synthèses ensuite).
- N'écris aucun identifiant de modèle dans les fichiers ni dans les commits (écris « conforme au manifeste » pour le modèle demandé).

## Lectures obligatoires d'entrée
1. Ton manifeste `.medina/missions/<ID_MISSION>.json` (sources figées et empreintes SHA-256).
2. `docs/collaboration/betta/PROMPT_VERITE.md` (cinq lois, matrice à 20 rubriques).
3. `docs/STYLE_REDACTION.md`.
4. Les **7 fichiers** de la leçon, en entier : onglets `_a` (Pathologie), `_b` (Examens), `_c` (Sciences), `_d` (Pharmacologie), fenêtres `_pop1`, `_pop2`, glossaire `glossary/<code>.py`. Toutes les surfaces : texte, tableaux, figures, quiz, fenêtres, Pareto, critères `div.alert`, paramètres `div.key`, glossaire.
Avant l'analyse, recalcule les SHA-256 des 7 fichiers et compare-les au manifeste ; consigne le résultat (`lecture.empreintes_conformes`).

## A. Audit MÉDICAL agressif avec enrichissement (missions `-MED`)
- Vérifier chaque affirmation médicale significative : définitions, chiffres, seuils, scores, classifications, critères diagnostiques, conduites, doses, contre-indications, interactions, pronostic, spécificités suisses.
- Sources dans l'ordre : suisses (SMF/RMS, sociétés suisses, OFSP, Swissmedic, Suva) → européennes (ESO/EAN, ESC, EASD/ESE, ERA/KDIGO, EHA, ESMO…) → revues. Médicaments : information professionnelle suisse (`python3 tools/swissmedic_fi.py` si fonctionnel, sinon compendium.ch / amiko.oddb.org), avec date de mise à jour de la FI.
- Outils : WebFetch ciblé, WebSearch, PubMed MCP (charger via ToolSearch si nécessaire). Lire la section utile, noter section/page.
- Gravité : `BLOQUANT` (erreur médicale démontrée ou dose/conduite dangereuse), `MAJEUR` (inexact, obsolète, non sourcé sur un point décisionnel), `MINEUR` (imprécision sans conséquence décisionnelle), `ENRICHISSEMENT` (rubrique absente ou insuffisante de la matrice des 20 rubriques, point d'examen fédéral manquant).
- Chaque constat : `id`, `gravite`, `fichier`, `ancre` (id HTML ou extrait exact ≤ 200 caractères, présent tel quel dans le fichier), `constat`, `preuve` (liste de `{source_id, section, citation_courte}`), `proposition` (texte de remplacement ou d'ajout en HTML conforme aux classes existantes du fichier), `justification` (mécanisme → conséquence → décision).
- Enrichissements : propositions rédigées prêtes à intégrer (`propositions/<fichier>_<n>.html`), en français soutenu, sourcées `[Sx]`.
- Matrice des 20 rubriques : pour la leçon telle qu'elle est, statut `couvert` / `partiel` / `absent` / `sans_objet`, avec l'onglet ou l'ancre.

## B. Audit LINGUISTIQUE agressif, formulation locale sans changer le fond (missions `-LANG`)
- Orthographe, grammaire, accords, conjugaison, ponctuation, typographie française (espaces insécables avant « ; : ! ? », guillemets « », majuscules, unités SI, nombres), phrases nominales, lourdeurs, répétitions, ambiguïtés, registre, cohérence terminologique, abréviations sans clé de glossaire, intitulés.
- Chaque proposition est **locale** : `ancien` (extrait exact, unique dans le fichier) → `nouveau`, avec `motif` et `fond_inchange: true`. Si une reformulation risque de changer un sens médical, ne pas la proposer : la marquer `renvoi_medical` avec explication.
- Ne jamais ajouter, retirer ou modifier un fait, un chiffre, une dose, une source.
- Vérifier mécaniquement que chaque `ancien` apparaît exactement une fois dans le fichier (script Python), et le consigner.
- Fichier `propositions.json` : liste `{id, fichier, ancien, nouveau, motif, categorie, fond_inchange}`.

## Livrables (dossier `docs/collaboration/ssp-v2/execution/<ID_MISSION>/`)
- `rapport.json` : `{mission, code, type_audit, base_sha, generation, branche, worktree, conversation, agent_executant: "sous-agent Claude Code (voir accusé issue 107)", modele_effort: "conforme au manifeste", date_debut, date_fin, lecture: {fichiers, empreintes_conformes}, premiere_source_lue (MED) ou premiere_verification (LANG), synthese: {BLOQUANT, MAJEUR, MINEUR, ENRICHISSEMENT} (MED) ou {nombre_propositions, renvois_medicaux} (LANG), constats: [...], matrice_20 (MED), lacunes: [...], mention: "Audit IA — revue distincte d'une validation médicale humaine ; aucune source canonique modifiée"}`.
- `rapport.md` : synthèse lisible pour Vial, en français soutenu, constats classés par gravité, tableau de bord final.
- MED : `sources.json` (`[{id, titre, organisme, url, date_publication, date_consultation, niveau_lecture: texte_integral|section|resume, sections_lues}]`) et `propositions/`.
- LANG : `propositions.json`.
- Valider le JSON (`python3 -m json.tool`).

## Publication
- `git add` uniquement ton dossier ; `git status` doit montrer que rien d'autre n'est modifié.
- Commit en français, message : `Audit Alpha tour1 <ID_MISSION> : <résumé chiffré>`, terminé par une ligne vide puis :
  `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`
  `Claude-Session: <lien de TA session Claude Code>`
- `git push -u origin <ta branche>` ; en cas d'échec réseau seulement, réessayer 4 fois (2 s, 4 s, 8 s, 16 s).
- Ne pas ouvrir de PR (le coordinateur Claude s'en charge).

## Réponse finale (courte)
SHA du commit poussé, compteurs de synthèse, 3 constats les plus graves en une ligne chacun, première source lue (URL + section), lacunes principales.

## C. Exigence Vial (15.10.2026, soir) — SÉMIOLOGIE OBLIGATOIRE (audits médicaux)
Chaque leçon doit présenter sa sémiologie et disposer d'une partie « Pour la leçon : sémiologie fondamentale et analytique », sur le modèle de la Cardiologie (parcours Sémiologie CS du fragment S01). L'audit médical vérifie et consigne dans `rapport.json` une clé `semiologie` :
- `fondamentale` : signes et symptômes de la leçon, mécanisme physiopathologique de chaque signe (normal → pathologique), fréquence, sensibilité/spécificité ou rapport de vraisemblance quand une source les donne, signes de gravité.
- `analytique` : examen clinique systématique de l'appareil concerné (étapes, gestes, interprétation), regroupement syndromique, raisonnement du signe vers le diagnostic et le différentiel, cas corrigés.
- statut `presente` / `partielle` / `absente`, ancres, et constat : **absence = MAJEUR** ; partielle = MAJEUR si un signe décisionnel manque, sinon MINEUR.
- proposition d'enrichissement rédigée et sourcée (sources de sémiologie universitaires suisses puis européennes), sans écrire dans les sources canoniques.
Grille binaire SEM-01 à SEM-24 et structure HTML : origin/medina/alpha77-chainage:EXIGENCE_SEMIOLOGIE.md (§ 4 b et 4 c) ; rubrique 21 « Sémiologie fondamentale et analytique » obligatoire dans rapport.md.
