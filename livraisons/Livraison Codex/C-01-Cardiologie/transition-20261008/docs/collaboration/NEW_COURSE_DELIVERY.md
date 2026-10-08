# Nouveaux cours — transfert en trois commandes

L’outil `tools/new_course_delivery.py` prépare un paquet complet, vérifie ses sources, puis enregistre un nouveau cours sans écraser les fichiers déjà présents. L’injection ne reconstruit pas le site et ne certifie pas la médecine.

| Responsable | Cours | Catégorie S01 |
|---|---|---|
| Claude | I83 — Varices des membres inférieurs | vaisseaux |
| Claude | I89 — Autres atteintes non infectieuses des vaisseaux et des ganglions lymphatiques | vaisseaux |
| Codex | I73 — Autres maladies vasculaires périphériques | vaisseaux |
| Codex | I95 — Hypotension | pression |

## Préparer la remise

Le producteur écrit dans sa branche les sources `chapters/<CODE>/<CODE>_a.html` à `_d.html`, les fenêtres `<CODE>_pop….html`, le glossaire `glossary/<code>.py` et un rapport Markdown. Le rapport précise les sections relues, les sources médicales, les contrôles réalisés et les réserves. Les quatre panneaux natifs sont `pA`, `pE`, `pS` et `pP` ; le gabarit principal est `ch-<CODE>`. Les fenêtres locales portent le préfixe du cours. Les références communes doivent exister dans les sources partagées.

Une commande crée le paquet I83 :

```bash
python3 tools/new_course_delivery.py package I83 --title "Varices des membres inférieurs" --report docs/collaboration/reviews/I83.md
```

La commande déduit `covers: [I83]`, le Fragment S01 et la catégorie. Pour un regroupement, préciser `--covers I89 I97`, après justification de son périmètre. `--source-commit <SHA>` peut fixer le commit parent réel ; par défaut, l’outil enregistre `git rev-parse HEAD`. Codex utilise `--author Codex`. I95 choisit automatiquement `pression`, les autres cours choisissent `vaisseaux`.

Le paquet se trouve sous `livraisons/Livraison Claude/C-01-Cardiologie/production/I83/` : manifeste `livraison.json`, `rapport.md` et sources complètes. Le manifeste contient code, titre, catégories couvertes, fragment, catégorie de navigation, commit parent, chemin original du rapport et empreintes SHA-256. Un paquet existant est conservé : préparer une révision sur une branche dédiée ou archiver explicitement la remise précédente avant une nouvelle préparation.

Le producteur publie sa branche et sa PR avec le paquet. L’intégrateur récupère le dossier `production/<CODE>` et conserve les originaux ; il ne recopie pas les fichiers communs du producteur.

## Vérifier et injecter

Après récupération du paquet sur la branche d’intégration :

```bash
python3 tools/new_course_delivery.py check "livraisons/Livraison Claude/C-01-Cardiologie/production/I83"
```

Le contrôle vérifie les chemins, les liens symboliques, l’UTF-8, les empreintes, la syntaxe JSON/Python, les quatre sources et panneaux, les ID natifs, les fenêtres et renvois locaux ou communs. Les références partagées sont limitées aux cours réellement sélectionnés pour S01 et à sa coque ; une fenêtre ou route disponible uniquement dans un autre fragment est refusée. Les ID d’un autre cours ne sont pas considérés comme des panneaux du cours actif. Le Python du glossaire n’est pas exécuté par le contrôle. Son exécution ultérieure par la construction exige une relecture du code remis. Les références de glossaire littérales sont contrôlées ; les expressions calculées restent à examiner lors de la relecture et de la construction.

L’intégrateur relit le rapport et le contenu, puis lance :

```bash
python3 tools/new_course_delivery.py apply "livraisons/Livraison Claude/C-01-Cardiologie/production/I83"
```

La commande revérifie le paquet, crée exclusivement `chapters/I83/` et `glossary/i83.py`, ajoute l’entrée à `chapters.json` puis le rattachement S01 et la catégorie dans `fragments.json`. Elle refuse toute collision de fichier ou d’enregistrement. En cas d’erreur, elle retire ses créations et restaure les catalogues modifiés. Le coordinateur exécute les applications successivement, pour éviter une édition concurrente des catalogues.

Le reçu `docs/collaboration/receipts/NEW_COURSE_<CODE>_<date>.json` porte **« injecté, reconstruction/contrôles à faire »**. L’intégrateur reconstruit ensuite MEDINA, exécute les contrôles statiques et navigateur, puis publie les sources et le reçu final. Les états reçu, injecté, contrôlé et publié restent distincts. L’existence du cours et de `covers` ne prouve pas la complétude CIM-11.

Les commandes acceptent `--root <dépôt>` avant `package`, `check` ou `apply` pour travailler sur un autre checkout. Les remises Codex utilisent le même protocole, sous `Livraison Codex`.
