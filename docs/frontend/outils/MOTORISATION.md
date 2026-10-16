# Motorisation du contrôle et de l’amélioration du frontend

Question de Vial : « peux-tu motoriser ce processus à plusieurs niveaux pour réduire son coût ? » Oui. Le cycle « modifier → reconstruire → contrôler → corriger » est confié à un orchestrateur déterministe, `tools/front_pipeline.py`. Celui-ci ne fait appel à une IA qu’en dernier recours, avec un paquet minimal. Le dispositif ne touche à aucun contenu médical : il lance les constructeurs et les automates existants (`build_front.py`, `build_index.py`, `front_garde`, `front_poids`, `tests/verify_*.cjs`).

## Commande unique

```bash
python3 tools/front_pipeline.py                 # construire ce qui a changé depuis origin/main, contrôler, résumer
python3 tools/front_pipeline.py --dry-run       # plan N0–N2 seul : rien n’est construit ni lancé
python3 tools/front_pipeline.py --fichiers engine/atlas_v4.css   # liste explicite, sans git
python3 tools/front_pipeline.py --complet --jobs 3               # amorçage du cache (première fois)
```

La sortie tient en cinq lignes, puis le chemin du rapport JSON. Voici une sortie réelle, après une retouche d’une fenêtre de cours S07 :

```text
front_pipeline · liste explicite → arbre de travail · 1 fichiers modifiés (0 sans effet, 0 non classés)
N0 plan : 3 cibles touchées sur 27 (atlas, fragment:S07, index)
N1 construction : 1 à construire, 0 restaurées, 26 à jour · 5 s réalisés, ≈ 1152 s évités
N2 contrôles : 4/4 ok
N3 : aucune IA nécessaire
```

« Évités » additionne les dernières durées enregistrées des cibles sautées. Celles-ci ont été mesurées sous charge et en parallèle : c’est un ordre de grandeur, pas un chronométrage.

Code retour : 0 si tout passe ; 1 si une construction ou un contrôle échoue ; 2 si l’exécution est impossible (révision git introuvable). Le cache se trouve par défaut dans `~/.cache/medina-front-pipeline/` (ou `$MEDINA_PIPELINE_CACHE`). Le site construit est dans `<cache>/site`, avec la même disposition que `_site` dans `pages.yml`. Le dernier rapport est dans `<cache>/dernier/rapport.json`.

## Architecture à quatre niveaux

| Niveau | Rôle | Coût | Outil |
|---|---|---|---|
| **N0** | `git diff` depuis la base (merge-base avec `origin/main`, arbre de travail et fichiers non suivis) → cibles | < 1 s | règles de `front_pipeline.classer` |
| **N1** | Construction incrémentale : chaque cible porte une empreinte de ses entrées réelles ; si elle est inchangée, la cible est sautée ou restaurée | 0 à 560 s | `build_front.py`, `build_index.py` sous traçage |
| **N2** | Contrôles déterministes, du moins cher au plus cher, limités aux cibles touchées | 10 s à quelques min | tests Python liés, `front_poids`, `verify_*.cjs`, `front_garde` |
| **N3** | Rapport, résumé de cinq lignes ; IA **seulement en cas d’échec**, avec un modèle choisi selon la nature de l’échec | 0 jeton si tout passe | `paquet_agent.txt`, `--ia-commande` |

### N0 — cartographie fichiers → cibles

Il y a 27 cibles : `atlas` (`MEDINA.html`), les 23 `fragment:<ID>`, `index` (portail), `organisation` et `apercu` (Infectiologie). Les règles sont lues dans l’ordre, et la première qui correspond l’emporte. Chaque cible retenue est accompagnée de sa raison dans le rapport.

| Fichier modifié | Cibles | Raison |
|---|---|---|
| `chapters/<CODE>/…` | `atlas`, fragment propriétaire, `index` | propriétaire calculé par `fragment_surface.frontend_catalog` (attributions explicites, spécialité, couvertures) |
| onglet `chapters/<CODE>/<CODE>_[abcd].html` qui passe de vide à rempli (ou l’inverse) | + les 23 fragments | la jauge globale, incorporée dans chaque fragment, change |
| `chapters.json` | diff entrée par entrée : fragment de chaque cours modifié + `atlas` ; tous les fragments si `integrated`, `covers` ou `owner` changent, ou si un cours est ajouté ou retiré | renvois et jauge globale |
| `nosology/fragments/<ID>.json` | fragment `<ID>`, `index` ; tous les fragments si la liste des leçons change | jauge globale |
| `engine/*`, `shell/*`, `build_front.py`, `build_medina.py`, `fragment_surface.py`, `nosologyEngine.py`, `fragments.json`, `organisation/fragments.json`, chargeurs `tools/*` | tout | moteur commun |
| `shell/fragment.*` | fragments, `index` | coque des fragments |
| `glossary/*` | `atlas`, fragments, `index` | le glossaire est chargé globalement par `build_medina` |
| `modules/*` | `atlas`, `fragment:S01` | ECG et Sémiologie CS |
| `build_index.py` ; `tools/build_organisation.py` ; `tools/build_fragment_work_preview.py` | la seule page concernée | — |
| `assets/images/*`, `assets/img/*` | aucune construction ; copie incrémentale à l’assemblage | — |
| `tools/front_garde.py`, `tools/front_poids.py`, `tests/*` | aucune construction ; contrôle ou test concerné | — |
| `docs/*`, `*.md`, `audits/*`, `livraisons/*`, `organisation/execution-*`, `.github/*` | aucune | sans effet sur le site |
| autre fichier de code (`.py`, `.js`, `.css`, `.html`, `.json`) | dépendance relevée par traçage si elle est connue ; sinon tout, par prudence | signalé dans `conservateurs` |

Le portail `index` est ajouté dès qu’un fragment est touché, parce qu’il agrège les 23 fragments. Il exige donc leur présence : ils sont restaurés depuis le cache, ou construits si le cache est froid.

### N1 — construction incrémentale avec cache par empreinte

- **Traçage des entrées réelles.** Chaque cible est construite dans un sous-processus qui installe un *audit hook* Python (`sys.addaudithook`). Il relève chaque fichier ouvert en lecture et chaque dossier parcouru (`os.scandir`, donc `glob` et `Path.glob`). Les modules importés sont relevés par leur `.pyc` puis ramenés à leur source `.py`. On ne dépend donc pas d’une liste de dépendances tenue à la main, qui finit toujours par se périmer. Le fragment S07, par exemple, relève 1 096 lectures et 6 dossiers.
- **Empreinte.** SHA-256 des contenus lus, des listes des dossiers parcourus, du script, de ses arguments et de la version de Python. Un mémo (taille, `mtime_ns`, inode) évite de relire un fichier inchangé.
- **Exclusion des lectures de jauge.** Chaque fragment lit les onglets a–d des 207 cours et les 23 inventaires nosologiques, mais seulement pour la jauge globale. Ces lectures étrangères sont remplacées dans l’empreinte par deux valeurs dérivées : `cours_remplis` (`nosologyEngine.integrated_course_aliases`) et `jauge_globale`. Sans cette exclusion, toute retouche de leçon invaliderait les 23 fragments.
- **Décisions.** `a_jour` (empreinte et sortie conformes), `restaurer` (sortie absente, copie depuis `<cache>/objets/`), `construire`, `hors_plan`. N1 corrige N0 dans les deux sens. Une cible désignée par N0 mais dont l’empreinte est inchangée est sautée : c’est le cas de l’atlas après une modification de `engine/finition_premium.css`, qu’il ne lit pas. Une cible dont l’empreinte a changé sans règle N0 est reconstruite et signalée dans `ecarts_cartographie`.
- **Agrégats.** Le portail (`index`) lit les fragments construits. Si un fragment est reconstruit, l’empreinte du portail est réévaluée après la phase 1 : il n’est reconstruit que si ses entrées ont réellement changé.
- **Parallélisme.** `--jobs 2` par défaut (environ 0,4 Go de mémoire par construction). Les cibles les plus longues partent en premier ; le portail vient en second temps.
- **`--exclure atlas`.** Dans une boucle locale centrée sur un fragment, on peut ne pas reconstruire l’atlas (216 s). Sa sortie peut alors être périmée, et le rapport le dit.
- **Assemblage.** Les images sont copiées comme dans `pages.yml` (`images/`, `fragments/images/`, `assets/img/`), en mode incrémental (taille et date).

### N2 — contrôles ciblés

| Contrôle | Quand | Ciblage |
|---|---|---|
| `python -m unittest tests/test_<module>.py` | un `.py` modifié possède son test, ou un test est modifié | modules liés seulement |
| `front_poids --sans-navigateur --budget` | une page est reconstruite | budget de `POIDS.md`, filtré aux pages présentes ; `--poids-navigateur` ajoute les temps |
| `verify_fragment_bootstrap.cjs` | fragment reconstruit | `MEDINA_QA_FRAGMENTS=<IDs>` |
| `verify_category_progress.cjs` | fragment reconstruit | `MEDINA_CATEGORY_FRAGMENT_IDS=<IDs>`, `MEDINA_TEST_COMPACT=1` |
| `verify_categories.cjs` | seulement avec `--verify-categories` | `MEDINA_CATEGORY_FRAGMENT_IDS=<IDs>` ; ce test ne figure pas dans `pages.yml` et **échoue déjà sur `main` 9e1b1d4** (`.mcg-lesson-title` absent) |
| `verify_fragment_filters.cjs` | logique des filtres modifiée (`engine/category_organisation.*`, `nosology/frequency.json`, `nosologyEngine.py`, `fragment_surface.py`) | tous les fragments (le test ne se filtre pas) |
| `front_garde --fragment <ID> --lecon <CODE>` | fragment reconstruit, portail modifié ou `front_garde.py` modifié | au plus `--garde-max` fragments (2 par défaut), ceux dont une leçon est touchée d’abord, avec cette leçon ; S08 par défaut |

**Cache des contrôles réussis.** Un contrôle navigateur (`verify_*`, `front_garde`) réussi est mémorisé avec une clé : commande, empreinte des outils (script, `browser_runtime.cjs`) et SHA-256 exacts des pages contrôlées. Sur les mêmes octets, il n’est pas relancé ; `--sans-cache-controles` force la relance. Seuls les succès sont mémorisés.

Les prérequis reconstruits à froid pour le portail ne sont pas contrôlés. Un contrôle est marqué `indisponible` (sans échec) si Playwright, Node ou Chromium manque, ou avec `--sans-navigateur`. Les sorties QA vont dans `<cache>/dernier/qa/`, jamais dans le dépôt.

### N3 — rapport, résumé et IA économique

`rapport.json` contient les fichiers, le plan avec ses raisons, les décisions N1, les durées, les contrôles, les échecs et l’économie (`construction_realisee_s`, `construction_evitee_s`). En cas d’échec, l’outil écrit en plus :

- `paquet_agent.txt` : la mission, la liste minimale des échecs (pour `front_garde`, contrôle, page, largeur et deux exemples ; pour `front_poids`, la métrique dépassée et sa limite ; sinon les lignes d’erreur utiles), les fichiers suspects (fichiers modifiés qui ont produit une cible en échec) et l’interdiction de toucher au contenu médical ;
- `paquet_agent.json` : les mêmes données, structurées ;
- deux estimations : `jetons_estimes_paquet` (taille du paquet / 4) et `jetons_estimes_journaux_bruts` (taille des journaux et des rapports JSON que l’agent aurait lus sans tri).

Après un succès, les anciens paquets sont effacés : un agent ne peut donc pas lire un échec périmé. Le paquet demande aussi de vérifier qu’un échec inexpliqué n’existe pas déjà sur la base, avant de le corriger.

Le modèle conseillé dépend de la nature de l’échec :

| Échec | Niveau | Pourquoi |
|---|---|---|
| construction, tests Python, budget de poids, `transitions`, `mouvement-reduit`, `erreurs` (ressource 404), `police` | **léger** (Sonnet, ou Haiku pour le tri) | correction mécanique : une durée, un chemin, une valeur, une trace d’erreur explicite |
| `contraste`, `saturation`, `cartes`, `debordement`, `focus`, axe, `verify_*.cjs` | **Opus** | choix de design ou régression de comportement à diagnostiquer |
| échec léger non résolu en deux essais | **Opus** | escalade |

`--ia-commande` lance une commande seulement en cas d’échec, avec le paquet sur l’entrée standard ; `{modele}` y est remplacé par `leger` ou `opus`. Exemple : `--ia-commande 'claude -p --model {modele}'`, à adapter à l’alias de modèle du poste. Sans cette option, l’outil n’appelle aucune IA : il écrit le paquet, et c’est le coordinateur qui décide.

## Gains estimés, chiffrés

**Référence : construction complète actuelle** (`main` 9e1b1d4, 16 octobre 2026, 4 cœurs, séquentiel, sans traçage). L’atlas prend 216 s. Viennent ensuite S08 (56 s), S01 (54 s), S02 (41 s), S05 (32 s), T1 (25 s), S06 (22 s), S03 (21 s) et S04 (14 s) ; les quatorze autres fragments prennent entre 4 et 9 s. Au total : **560 s (9 min 20 s)** pour l’atlas et les 23 fragments, sans le portail, l’organisation ni l’aperçu. C’est le coût de la phase « Construire » de `pages.yml` à chaque publication et de toute vérification manuelle complète.

**Mesures du pipeline**, sur une copie jetable du dépôt (`git archive HEAD`), en modifiant réellement les entrées :

| Scénario | Mesure du pipeline | Aujourd’hui | Gain |
|---|---|---|---|
| Amorçage à froid (`--complet --jobs 3`, 27 cibles) | 517 s de durée réelle | 560 s + portail, organisation, aperçu | ≈ égal (coût unique) |
| Relance sans modification (CI rejouée, documentation, reçus) | **1,1 s**, rien n’est construit ni contrôlé | 560 s | ≈ 100 % |
| Fenêtre d’un cours S07 (`chapters/M31/M31_pop.html`) : construction | atlas 213 s + S07 9,5 s = 223 s | 560 s | −60 % |
| Même cas, contrôles compris (front_poids 28 s, bootstrap 9 s, jauges 5 s, front_garde S07 26 s) | **4 min 45 s** en tout (mesure prise avant la correction de la réévaluation du portail, qui ajoute environ 4 s) | 560 s de construction, puis les contrôles sur les 23 fragments | ≈ −50 % et plus |
| Relance après une correction qui ne change pas les pages contrôlées | 28 s (portail 5 s + front_poids 23 s ; trois contrôles navigateur repris du cache, 40 s évitées) | 560 s et plus | −95 % |
| CSS propre aux fragments (`engine/finition_premium.css`) | 23 fragments et portail en 355 s ; **atlas, organisation et aperçu sautés par N1** (leur trace ne lit pas ce fichier) | 560 s | −37 % |
| Fenêtre d’un cours S07 avec `--exclure atlas` (boucle locale d’un agent de fragment) | **13 s** mesurées pour S07, portail compris ; ≈ 65 s estimées pour S08 | 560 s | −88 à −98 % |
| Image seule (`assets/img/*`) | aucune construction, copie incrémentale (non chronométrée) | 560 s | ≈ 100 % |

Le traçage ajoute environ 35 % au temps d’une construction : S07 passe de 7,0 à 9,6 s quand il est construit seul. Ce surcoût ne porte que sur les cibles réellement reconstruites. Le parallélisme rapporte peu sur la machine de mesure, une machine partagée où chaque construction devenait 2,5 fois plus lente à trois en parallèle. Un exécuteur GitHub à 4 cœurs libres devrait mieux en profiter, mais cela n’a pas été mesuré.

**Jetons IA évités** (mesures du scénario S07). Les sorties brutes des contrôles totalisent 175 ko, soit environ **44 000 jetons** : 154 ko pour le rapport `front_poids.json`, 16,5 ko pour `front_garde_S07.json` et 4,7 ko de journaux. Un agent qui « vérifie le frontend » sans motorisation les lit, en plus des journaux de construction, puis décide quoi relancer. Avec le pipeline :

- **si tout passe, l’IA ne consomme aucun jeton**, et c’est le cas courant ; les cinq lignes du résumé suffisent (environ 120 jetons) ;
- **en cas d’échec**, le paquet minimal mesuré pèse 1 041 octets, soit environ **260 jetons**, à peu près **170 fois moins** que les sorties brutes ; il désigne en plus le niveau de modèle à employer ;
- **choix du modèle** : la plupart des échecs mécaniques (budget, durée, chemin, test) sont confiés au modèle léger, au lieu d’Opus.

Ces durées sont locales et indicatives ; elles varient selon le nombre de cœurs, le disque et la charge de la machine.

## Proposition CI (non appliquée)

`.github/workflows/*` est un fichier partagé : il n’est pas modifié ici. La proposition ajoute un job de **contrôle de PR** léger. La publication Pages reste inchangée et complète.

```yaml
# .github/workflows/front-pr.yml — proposition, à intégrer par une mission d’intégration
name: Contrôle frontend ciblé (PR)
on:
  pull_request:
    paths-ignore: ['docs/**', '**/*.md', 'audits/**', 'livraisons/**', 'organisation/execution-*/**']
permissions:
  contents: read
jobs:
  front:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v7
        with: { fetch-depth: 0 }
      - uses: actions/setup-python@v7
        with: { python-version: "3.12" }
      - uses: actions/setup-node@v7
        with: { node-version: "22" }
      - name: Restaurer le cache du pipeline (empreintes, objets, site)
        uses: actions/cache@v4
        with:
          path: ~/.cache/medina-front-pipeline
          key: front-pipeline-${{ runner.os }}-py312-${{ github.sha }}
          restore-keys: front-pipeline-${{ runner.os }}-py312-
      - name: Plan (aucune exécution)
        run: python3 tools/front_pipeline.py --base origin/${{ github.base_ref }} --dry-run
      - name: Installer Chromium seulement si des contrôles navigateur sont prévus
        run: |
          if python3 -c "import json,os,sys;r=json.load(open(os.path.expanduser('~/.cache/medina-front-pipeline/dernier/rapport.json')));sys.exit(0 if any(c['navigateur'] for c in r['controles_planifies']) else 1)"; then
            python -m pip install playwright==1.55.0
            python -m playwright install --with-deps chromium
            npm install --no-save --package-lock=false playwright@1.55.0
          fi
      - name: Construire ce qui a changé, contrôler, résumer
        run: python3 tools/front_pipeline.py --base origin/${{ github.base_ref }} --jobs 3 --rapport work/front_pipeline/rapport.json
      - name: Résumé dans la PR
        if: always()
        run: python3 -c "import json;print('\n'.join(json.load(open('work/front_pipeline/rapport.json'))['resume']))" >> "$GITHUB_STEP_SUMMARY"
      - uses: actions/upload-artifact@v4
        if: failure()
        with: { name: paquet-agent, path: work/front_pipeline }
```

Dans `pages.yml`, on pourrait aussi construire avec `python3 tools/front_pipeline.py --complet --jusqua construction --jobs 3 --out dist`, avec le même cache, au lieu de `build_front.py` puis `build_front.py --all-fragments`. Le cache rend alors la publication proportionnelle au changement. Cette étape doit d’abord être validée par une mission d’intégration, parce que la publication est le chemin critique.

## Hook local (proposition, non installé)

Fichier `.git/hooks/pre-push`, propre à chaque poste et jamais versionné :

```sh
#!/bin/sh
# Contrôle ciblé avant push : rien n'est construit si seuls des documents ont changé.
python3 tools/front_pipeline.py --base origin/main --garde-max 1 || {
  echo "front_pipeline : échec — voir ~/.cache/medina-front-pipeline/dernier/paquet_agent.txt"; exit 1; }
```

Pour un agent Claude Code, l’équivalent est un hook `Stop` qui lance `python3 tools/front_pipeline.py --sans-navigateur`. Ce hook est réglé dans les paramètres de l’agent, pas dans ce dépôt.

## Consignes aux agents

1. **Réutiliser les scripts, ne pas les réécrire.** Pour toute vérification du frontend, lancer `python3 tools/front_pipeline.py`. Ne pas recomposer à la main `build_front.py`, `build_index.py`, `front_garde` et `verify_*.cjs`, ni écrire un script ponctuel qui fait la même chose.
2. **Construire de façon ciblée.** Ne jamais lancer `build_front.py --all-fragments` pour vérifier une retouche : le pipeline construit ce que le diff impose. Utiliser `--dry-run` pour connaître le coût avant d’exécuter, et `--cibles fragment:S08` pour forcer une seule page. Dans une boucle locale sur un fragment, `--exclure atlas` évite 216 s quand l’atlas n’est pas l’objet du travail. Amorcer le cache une seule fois, avec `--complet`.
3. **Lire de façon ciblée.** Lire d’abord les cinq lignes du résumé. En cas d’échec, lire `paquet_agent.txt`, puis seulement les journaux et les fichiers suspects qu’il cite. Ne pas ouvrir les HTML construits (7 à 67 Mo), les rapports bruts complets ni les captures, sauf si le paquet le demande.
4. **IA seulement sur échec.** Si le code retour vaut 0, le travail de contrôle est terminé : on ne lance aucun agent de relecture du frontend.
5. **Modèle léger pour le mécanique.** Le niveau indiqué par le paquet s’applique : `leger` (Sonnet ou Haiku) pour un budget de poids, une durée de transition, un chemin 404, un test unitaire ou une trace de construction ; `opus` pour le contraste, la saturation, les cartes, le focus, le débordement et les `verify_*.cjs`, ou après deux échecs du modèle léger.
6. **Relancer après correction.** Après la correction, relancer la même commande. Le cache ne reconstruit que la cible corrigée. L’agent ne déclare la réussite que si le code retour vaut 0, et il cite les cinq lignes.
7. **Respecter le périmètre.** Le paquet rappelle les interdits (`chapters/`, `glossary/`, `nosology/`, `chapters.json`). Un échec qui exigerait d’y toucher est remonté au coordinateur ; l’agent ne le contourne pas.

## Limites honnêtes

- **Cache froid.** Sur un poste neuf, toute cible qui touche un fragment demande le portail, donc les 23 fragments : la première exécution coûte une construction complète. On peut aussi viser un site déjà construit (`--out dist`) : ses sorties non tracées sont alors acceptées comme « à jour (non vérifiées) » si N0 ne les désigne pas.
- **Lectures invisibles.** Le traçage voit les ouvertures de fichiers et les parcours de dossiers, pas les simples tests d’existence (`Path.exists`, `is_file`). Un fichier dont seule l’existence compte, et qui apparaît plus tard, n’est vu que par les règles N0. C’est le cas de `organisation/course_groups.json`, couvert explicitement.
- **Course pendant la construction.** L’empreinte est calculée juste après la construction, sur les fichiers lus. Un fichier modifié pendant la construction peut être attribué à tort à la sortie : il faut relancer.
- **Le glossaire est global.** `build_medina` charge tous les glossaires : une retouche de `glossary/<code>.py` reconstruit l’atlas et les 23 fragments. Affiner exigerait de modifier le moteur, ce qui est hors de cette mission.
- **L’atlas domine.** 216 s sur 560 s, et il dépend de tous les cours : toute retouche de cours le reconstruit. Le vrai gain viendra de la première recommandation de `POIDS.md` (paquets par cours), qui relève du moteur.
- **Contrôles partiels.** `verify_fragment_filters.cjs` ne se filtre pas ; `front_garde` ne regarde que deux fragments ; les captures et la régression visuelle ne sont pas couvertes. La publication Pages garde ses contrôles complets.
- **Échec préexistant constaté.** `tests/verify_categories.cjs` échoue sur `main` 9e1b1d4 non modifié (« Cannot read properties of null (reading 'textContent') », ligne 50 : `.mcg-lesson-title` absent des cartes). Il n’est pas lancé par `pages.yml` ; le pipeline ne le lance que sur demande. Sa correction relève d’une mission d’intégration, car le fichier est partagé.
- **Cache des contrôles.** La clé couvre les pages contrôlées et les scripts de contrôle, mais pas les images ni le navigateur. Après une mise à jour de Chromium ou des seuls fichiers d’images, il faut relancer avec `--sans-cache-controles`.
- **Taille du cache.** Environ 200 Mo d’objets et 300 Mo de site. L’action `actions/cache` le permet (10 Go par dépôt), mais il faut le purger de temps en temps (`rm -rf ~/.cache/medina-front-pipeline/objets`).
- **Ce que le pipeline ne valide pas.** Ni la médecine, ni la pédagogie, ni le jugement esthétique : seuls les seuils techniques documentés dans `README.md` et `POIDS.md` sont vérifiés.
- **Modèles.** Le niveau d’IA est une recommandation inscrite dans le paquet. Le pipeline n’appelle un modèle que si `--ia-commande` est fourni.
