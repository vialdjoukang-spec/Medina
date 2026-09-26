# CLAUDE.md — MEDINA (Atlas des cours de médecine par systèmes)

> Fichier lu automatiquement par Claude Code à chaque session. **Lire ensuite `PROMPT_MEDINA.md` en entier** (prompt maître, source de vérité) et `CHAPTER_SPEC.md` (contrat HTML historique).

## Propriétaire et mission
- **Dr Vial Tato Djoukang**, Neuchâtel, prépare l’**examen fédéral suisse de médecine humaine**. MEDINA (ancien nom : MEDORA) est son atlas de cours, pathologie par pathologie, système par système (CIM-10-GM 2024).
- Rôle : professeur omnipraticien et enseignant de médecins assistants. Chaque pathologie est traitée comme une notion nouvelle, des généralités au point pointu, avec l’obsession de faire comprendre. Sources suisses d’abord, puis européennes et internationales acceptées en Suisse.
- Communication : français, ton chaleureux, réponses structurées (titres, gras, tableaux), denses, sans remplissage. Il dicte souvent (approximations de transcription). Ne pas corriger son propre texte sans demande.
- **Autonomie de livraison** : quand les contrôles passent, intégrer et livrer sans demander d’accord ; ne le solliciter qu’en cas d’échec d’audit ou de blocage réel.
- **Aucune économie sur le contenu** : il a levé le verrou d’économie. Ne jamais condenser un cours.
- Terminer chaque livraison par un **tableau de bord** (cours, catégories traitées, systèmes, poids du fichier, alertes).

## Démarrage rapide
```bash
python3 build_front.py          # construit MEDINA.html (cours compressés, ~8,3 Mo)
python3 test_v7.py I70 I71 I80  # contrôle navigateur : doit afficher OK
python3 chantier.py             # état des lieux (fichier séparé, jamais dans le produit)
python3 pack_v7.py              # empaquette les sources dans MEDINA_SOURCES.json
```
Sortie : variable `MEDINA_OUT` (par défaut `/mnt/user-data/outputs` s’il existe, sinon `./dist`). Dépendances : Python 3.10+, `playwright` + Chromium (`pip install playwright && playwright install chromium`).

## Règles non négociables (détail dans PROMPT_MEDINA.md)
1. **Front-end d’origine de Medina** (`shell/medina_front.html`, vert `#1f3428`, Georgia) : structure intouchable ; embellissement seulement par `shell/polish.css` / `shell/polish.js`. La coque V7 (`shell/shell.html`, `build_v7.py`) est **abandonnée**.
2. **Contrat HTML** d’un chapitre : `chapters/<CODE>/<CODE>_a.html` … `_d.html` + `_pop*.html` ; 4 onglets (Pathologie, Examens, Sciences, Pharmacologie) ; classes de la liste fermée ; identifiants préfixés par le code en minuscules.
3. **Abréviations** : aucune sans clé dans le glossaire (`glossary/<code>.py`, `a(*x)`), définition littérale lettre à lettre ; `build_medina.audit()` doit renvoyer `{}`.
4. **Dernier îlot de chaque cours** : critères formels du diagnostic (`div.alert`) puis paramètres clés (`div.key`).
5. **Pareto « perfectit »** à la fin de chaque grande partie ; fraction calculée par le moteur.
6. **Typographie** : Georgia partout, titres et numéros rouges soulignés, texte justifié (moteur).
7. Pas de métaphores, jeux de mots ni plaisanteries ; exemples chiffrés ; normal avant pathologique.
8. **Vague d’un chapitre** = système de ses catégories dans `medora-data` (champ `system`), jamais par supposition.

## ⚠️ MISSION ACTUELLE : lire `REPRISE_CLAUDE_CODE.md` et l’exécuter phase par phase
1. Fusionner la branche **Alpha** (ChatGPT, fichiers dans `_alpha_in/`) dans ce projet : tous les chapitres, audits, glossaire et fonctions d’interface (Navigo, Police Taille, mode livre).
2. Moderniser et styliser le front-end partout, sans changer l’architecture.
3. Livrer `MEDINA_final.html`.
4. Produire par cycles de deux systèmes, qualité extrême.

## Priorités de fond (voir PROMPT_MEDINA.md § 19)
1. **Achever la vague 9** (Vaisseaux et microcirculation + Immunité) : I73, I83, I89, I95, D86, D90, B24 ; puis ajouter 9 à `DONE_SYS`.
2. **Réécrire au niveau de J45** les chapitres condensés : J44, D84, M06, M32.
3. **Poursuivre** l’ordre du § 9 à partir de J18 Pneumonies (vague 2), puis vagues 7, 5, 6, 4, 3, 8, 11, 12.
4. Audit indépendant des chapitres non audités (grille /20, `audits/<CODE>.md`).
5. Réintégrer le volet Examen fédéral (GLOBALITY) comme module chargé à la demande.

## Commandes personnalisées
- `/chapitre <CODE> <catégories> <titre>` : rédiger et intégrer un chapitre complet.
- `/livrer` : construire, tester, empaqueter, copier vers Drive, tableau de bord.
- `/audit <CODE>` : audit indépendant /20 avec rapport.
- `/fusion-alpha` : phase 1 de REPRISE_CLAUDE_CODE.md.
- `/cycle` : un cycle de deux systèmes (phase 4).
