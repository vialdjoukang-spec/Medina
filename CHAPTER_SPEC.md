## Consigne active — reprise et fragments entiers, 8 octobre 2026

Vial demande de prendre connaissance de `Prompt_Codex.pdf` et de continuer. Cette reprise lève le STOP antérieur. Lire [COORDINATION.md](COORDINATION.md) et [le protocole par fragment](docs/collaboration/PROTOCOLE_FRAGMENTS_2026-10-08.md) avant les instructions historiques ci-dessous. **Fragment entier complet et auto-revu avant transmission ; audit croisé unique, correction et injection par l’autre IA ; fragment INJECTÉ immuable ; arrêt après les 22 ; HTML clair exclusivement.** Les règles de remise par chapitre, d’injection autonome avant audit, de renvois successifs et de correction après injection sont remplacées. Les travaux et leurs preuves restent conservés. Le mode multi-agent et un auteur par fichier restent applicables ; les veilles automatiques restent en pause.

# MEDINA — Cahier des charges d’un chapitre (contrat de rédaction)

Tu rédiges UN chapitre de MEDINA, plateforme de cours de médecine pour médecins assistants préparant l’examen fédéral suisse de médecine humaine. Le propriétaire est psychiatre-psychothérapeute en Suisse ; il exige une qualité pédagogique maximale et vise **20/20** à l’audit.

## 1. Modèle à imiter (structure, pas contenu)
Le chapitre de référence est **I50 Insuffisance cardiaque** : `/home/claude/medina/chapters/I50/*.html`. Lis-le intégralement AVANT d’écrire : il fixe le gabarit HTML, le ton, la densité, les types d’encadrés, les fenêtres, les quiz et les Pareto. Imite la **forme**. Ne clone aucune phrase : le plan, les exemples et les pièges doivent être propres à ta pathologie.

## 2. Fichiers à produire
Dossier : `/home/claude/medina/chapters/<CODE>/`
- `<CODE>_a.html`, `<CODE>_b.html` : onglet « Pathologie et prise en charge ».
  - Ouvre par `<template id="ch-<CODE>"><div class="chap">`, suivi de l’en-tête, des quatre onglets et du panneau `pA`.
  - Découpe en deux fichiers pour la taille.
- `<CODE>_c.html` : panneaux `pE` (Examens complémentaires) et `pS` (Sciences fondamentales spécialisées).
- `<CODE>_d.html` : panneau `pP` (Pharmacologie de la pathologie). Il se ferme par `</div></template>`.
- `<CODE>_pop1.html` … `<CODE>_popN.html` : fenêtres `<template data-pop="clé" data-title="Titre">…</template>`.
- `/home/claude/medina/glossary/<code_minuscule>.py` : nouvelles abréviations (voir § 5).

## 3. Classes et identifiants
- Utilise exactement les classes courtes du modèle I50 : `ilot`, `toc`, `chap-body`, `sci-body`, `sci`, `sci-bar`, `key`, `trap` (+ `span.k`), `alert`, `two`, `card`, `table.t`, `pareto-btn`, `src`, `pager` (boutons `prev` et `next`), `quiz`, `fb`, `status`, `chap-head`, `code`, `n`, `ui`.
  - Ne crée aucune autre classe.
  - Le script de construction convertit ces classes en `mc-…`.
- Mots verts : `<button class="w" data-k="clé">libellé (contenu de la fenêtre)</button>`.
  - Le libellé annonce la destination entre parenthèses.
  - Chaque clé doit exister comme `<template data-pop>`.
- Quiz : `<div class="quiz ui"><p>…</p><button data-ok="1">…</button><button data-ok="0">…</button><p class="fb" hidden>explication</p></div>`.
- Pareto : un `<button class="pareto-btn ui" data-k="pareto-<code>-xxx">▲ Loi de Pareto — …</button>` en fin de chaque grande partie volumineuse. Le template commence par `<p class="ratio" data-cover="id1,id2"></p>`, suivi d’une `<ul>` contractée. Le ratio est calculé automatiquement ; les ids doivent être ceux des `<section class="ilot" id="…">` couverts.
- **Préfixes obligatoires** (ils évitent les collisions entre chapitres) :
  - ids d’îlots : `<code_minuscule>-<n>` (ex. `i21-3`), `<code>-e-<n>`, `<code>-p-<n>` ;
  - sciences : `<code>-s-anat`… ;
  - nouvelles clés de fenêtres : `<code_minuscule>-…` (ex. `i21-killip`).
- Tu peux **réutiliser** une fenêtre existante (clés sans préfixe de I50 : `np`, `echo`, `irm`, `raas`, `d-bb`, `d-arm`, `d-sglt2`, `d-arni`, `crt`, `dai`, `carfer`, `amylose`, `champ`…) si son contenu convient exactement. Ne la modifie pas.
- Sommaires internes : `<a href="#id">` (convertis automatiquement).

## 4. Contenu exigé (Prompt Ultima + amendements du propriétaire + instructions du projet)

**Temps Alpha (onglet 1).** Chaque îlot se lit seul. Ordre :
0. question clinique et objectifs ;
1. définition et classifications (version, société savante) ;
2. épidémiologie (données suisses si elles existent, sinon européennes, datées ; lacune nommée) ;
3. physiopathologie (chaîne normal → perturbation → manifestation, mots verts à chaque charnière, figure SVG noir et blanc légendée si utile) ;
4. étiologies et facteurs de risque ;
5. anamnèse :
   - antécédents cliquables ;
   - symptômes par fréquence, cliquables (caractérisation et physiopathologie) ;
   - formes typique et atypiques en cartes deux colonnes ;
6. examen clinique : état général → vitaux → anthropométrie → signes ciblés, en deux colonnes, chaque signe cliquable (technique, valeur, pièges) ;
7. diagnostic (critères officiels, algorithme, différentiels hiérarchisés par gravité) ;
8. urgences et complications : **gravité d’abord**, dans un encadré `alert` ;
9. prise en charge hiérarchisée : objectifs → moyens → choix justifiés → surveillance → critères de modification ;
10. suivi, pronostic, prévention ;
11. situations particulières : grossesse, sujet âgé, insuffisance rénale ou hépatique, cas récapitulatif.

Ajoute les îlots propres à la pathologie ; supprime ceux qui ne s’appliquent pas.

**Temps Betta.**
- Onglet Examens :
  - hiérarchie question → examen → statut (indiqué, conditionnel, non systématique) ;
  - **gold standard nommé** ;
  - fiches d’interprétation profondes : valeurs normales avec unités et population, seuils pathologiques, lésions élémentaires, pièges, erreur fréquente ;
  - tableau diagnostics × associations biologiques si plusieurs configurations existent ;
  - au moins 3 quiz de cas cliniques.
- Onglet Sciences : barre d’icônes (Anatomie, Histologie, Physiologie, Biochimie ou autre discipline pertinente, Génétique si pertinente), avec un îlot par science, un schéma SVG noir et blanc légendé au minimum, et des **corrélations cliniques explicites** (encadré `key`).
- Onglet Pharmacologie : stratégie **propre à la pathologie** :
  - classification ;
  - place selon le phénotype ;
  - tableau des doses (initiale et cible, sourcées) ;
  - interactions dangereuses (encadré `alert`) ;
  - surveillance et gestion des effets indésirables ;
  - médicaments à éviter ;
  - monographies en fenêtres (mécanisme, preuves avec essais, posologie, effets indésirables, contre-indications, surveillance).

**Rubriques transversales.**
- « Piège » et « Erreur fréquente » partout où elles existent.
- Moyens mnémotechniques en fenêtre, avec la mention « aide pédagogique, non critère officiel ».
- Chaque grande partie volumineuse finit par un Pareto (fraction minimale du texte qui donne 100 % des notions utiles).
- Section `src` en fin de l’onglet 1, avec les références principales datées.

**Style.**
- Français médical soutenu, phrases complètes, une idée par paragraphe.
- **Aucune métaphore, aucune comparaison imagée, aucun jeu de mots, aucun remplissage.**
- Chaque concept est expliqué comme si le lecteur le découvrait, avec un exemple.
- Pas de liste de mots-clés à la place d’un cours.

**Exactitude.**
- Références : sociétés savantes suisses et européennes (ESC, ERS, EASL, ESH, KDIGO…), Swissmedic et compendium.ch pour les médicaments, OFSP.
- Vérifie par recherche web les recommandations **en vigueur en septembre 2026**. De nouvelles recommandations ESC ont paru en août 2026 ; vérifie si ta pathologie en a reçu.
- N’invente aucun chiffre, seuil, posologie ou classe de recommandation. Si une donnée n’est pas vérifiable, attribue-la explicitement à la dernière version vérifiée (ex. « ESC 2023 »), sans formule de chantier du type « à vérifier ».
- Limite-toi à environ 12 recherches web ciblées.

## 5. Règle absolue des abréviations
**Aucune abréviation ne doit subsister sans définition littérale lettre par lettre.** Le script de construction rend cliquable chaque occurrence de chaque clé du glossaire. Tu dois donc :
1. Vérifier les clés existantes : `python3 -c "import sys;sys.path.insert(0,'/home/claude/medina/glossary');import glob,importlib;G={};[G.update(importlib.import_module(f.split('/')[-1][:-3]).G) for f in glob.glob('/home/claude/medina/glossary/*.py')];print(sorted(G))"`.
2. Pour chaque abréviation nouvelle, l’ajouter dans `glossary/<code_minuscule>.py` :
   ```python
   from cardio_1 import a, G
   a('SCA',[('S','Syndrome'),('C','Coronarien'),('A','Aigu')],'Syndrome coronarien aigu','<p>Définition riche en 1 à 3 phrases.</p>','clé_fenêtre_optionnelle')
   ```
   - Le développement littéral suit **chaque lettre ou groupe de lettres**.
   - Pour un nom d’essai non développable lettre à lettre, l’écrire honnêtement (voir `glossary/cardio_2.py`, par exemple COPERNICUS).
   - Pour les gènes, les ions et les signes ECG, suivre les exemples existants.
3. Écrire en toutes lettres ce qui n’est pas une abréviation nécessaire :
   - « par voie intraveineuse » au lieu de « IV » (les chiffres romains restent réservés aux classes et stades) ;
   - « /jour » au lieu de « /j » ;
   - « angiotensine II » au lieu de « Ang II ».
4. Les symboles d’unités (mg, mL, mmHg, mmol/L…) ne sont pas des abréviations.
5. Aucune abréviation dans les libellés des onglets, des boutons Pareto et de la barre des sciences.

## 6. Contrôles obligatoires avant de rendre
1. `cd /home/claude/medina && python3 build_medina.py <CODE>` doit afficher `<CODE> non couvertes: 0` et aucune erreur Pareto.
2. `python3 test_preview.py <CODE>` doit afficher `OK` : chargement, fenêtres, onglets, mode livre, aucune erreur JavaScript.
3. Contrôle des clés : chaque `data-k` possède son `template data-pop`, et aucune clé nouvelle n’est sans préfixe.
4. Relis ton texte contre la grille /20 :

   | Critère | Points |
   |---|---|
   | Exactitude et actualité | 4 |
   | Complétude | 3 |
   | Pédagogie | 3 |
   | Corrélations vertes | 2 |
   | Sciences fondamentales et schémas | 2 |
   | Examens | 2 |
   | Pharmacologie spécifique | 1 |
   | Pareto | 1 |
   | Langue et anti-clonage | 1 |
   | Interface | 1 |

   Corrige tout ce qui ferait perdre un point.

## 7. Rapport final (court)
- Fichiers créés.
- Nombre de mots, de fenêtres et de quiz.
- Sources principales, avec date.
- Points non vérifiables et leur attribution.
- Résultat des contrôles.

Ne modifie **aucun** fichier hors de `chapters/<CODE>/` et `glossary/<code>.py`.
