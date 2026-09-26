# Passation MEDINA : réécriture pédagogique (26.09.2026, 20 h UTC)

> Ce document permet à une autre IA de reprendre le travail sans rien deviner. Lisez ensuite `CLAUDE.md`, `PROMPT_MEDINA.md` et **`docs/STYLE_REDACTION.md`** (obligatoire).

## 1. Où trouver le travail

- **Dépôt** : `vialdjoukang-spec/medina`.
- **Branche** : `claude/medina-alpha-integration-7dul4i`. Tout le travail est sur cette branche ; il n’y a pas de demande de fusion (PR).
- **Livrable validé** : `dist/MEDINA_final.html` (phase 3, commit `0a57926`). Il contient 30 cours, tous testés au navigateur. **Il ne contient pas encore la réécriture pédagogique** décrite ci-dessous.
- **Sources empaquetées** : `dist/MEDINA_final_SOURCES.json`.

## 2. Ce qui est terminé depuis la phase 3

| Commit | Contenu | État |
|---|---|---|
| `3b9b1e1` | Guide de rédaction `docs/STYLE_REDACTION.md`, référencé dans PROMPT § 11, CLAUDE.md et `/chapitre`. Le test statique contrôle aussi les classes hors liste et les styles en ligne. | Terminé |
| `82171ea` | Espace et justification : césure française (native, sinon module de secours dans `shell/polish.js`), colonne élargie sur téléphone, interligne resserré. Mesures dans `audits/FRONT_MODERNISATION.md` § 6. | Terminé, testé au navigateur (J45, I50, T78, I21) |
| `a524aad` et suivants | Onglet 1 (Pathologie) réécrit selon le guide pour J44, J18, I26 et A41. | Rédigé, test statique OK, **contre-lecture non faite** |

## 3. Demande du propriétaire (à respecter)

Le propriétaire a demandé de réécrire **les cours produits par Claude Code**, c’est-à-dire **J18, I26, A41 et J44**. Les cours déjà présents avant (cardiologie, J45, D84, M06, M32, T78, M31, I71, I80, I70) ne doivent pas être touchés. Ses critiques étaient les suivantes :
- trop de phrases nominales ; il veut des phrases courtes et complètes ;
- des parties sans annonce ni conclusion ; il veut, pour chaque partie, une annonce, un développement, puis un épilogue « À retenir » ;
- des tableaux sans introduction ; il veut une introduction avant chaque tableau et une lecture après ;
- des sciences fondamentales trop superficielles ; il les veut au niveau universitaire, reliées à la clinique ;
- une densité trop faible ; il faut expliquer le pourquoi partout, avec des termes cliquables sur chaque notion clinique.

Sa règle d’or : **« le lecteur comprend, il ne devine pas »**.

## 4. État exact de chaque cours

| Cours | Onglet 1 Pathologie | Onglet 2 Examens (`_c.html`, panneau pE) | Onglet 3 Sciences (`_c.html`, panneau pS) | Onglet 4 Pharmacologie (`_d.html`) | Contre-lecture |
|---|---|---|---|---|---|
| J44 BPCO | Réécrit (45 712 mots au total) | À réécrire | À réécrire | À réécrire | À faire |
| J18 Pneumonies | Réécrit (51 376 mots) | À réécrire | À réécrire | À réécrire | À faire |
| I26 Embolie pulmonaire | Réécrit, mais le rédacteur a été arrêté juste avant sa fin : il faut vérifier que tout l’onglet 1 est traité (43 027 mots) | À réécrire | À réécrire | À réécrire | À faire |
| A41 Sepsis | Même situation que I26 (40 806 mots) | À réécrire | À réécrire | À réécrire | À faire |

Les quatre cours passent `python3 test_v7.py --static J44 J18 I26 A41` (OK).
Les données nouvelles de l’onglet 1 sont sourcées dans `audits/<CODE>.md`, section « Réécriture pédagogique — 26.09.2026 ».
Les nouvelles fenêtres de l’onglet 1 sont dans `chapters/<CODE>/<CODE>_pop_pa.html`.

## 5. Ce qu’il reste à faire, dans l’ordre

1. **I26 et A41, onglet 1** : relire l’onglet 1 et compléter ce qui manque (annonces, épilogues, fenêtres). Les rédacteurs ont été arrêtés juste avant la fin.
2. **Onglets 2, 3 et 4 des quatre cours** : les réécrire selon le guide. Une consigne prête à l’emploi existe pour chaque onglet. Pour la générer :
   `python3 docs/passation/consignes_gen.py J44 J18 I26 A41`
   Le script écrit les consignes dans le dossier de travail indiqué par sa variable `S` ; modifiez-la au besoin. Il attend les fichiers `_c.html` (examens) et `_c2.html` (sciences) : pour rédiger en parallèle, coupez `_c.html` à la ligne `<div class="panel" id="pS"`, puis recollez les deux fichiers à la fin, car le contrat HTML prévoit seulement `_a` à `_d`.
3. **Contre-lecture adverse** de chaque cours, par deux angles : style et profondeur, puis exactitude et contrat. Le script de flux de travail se trouve dans `docs/passation/wf_contre_lecture.js` (argument `{"code":"J44"}`). La comparaison se fait avec le commit `0a57926`.
4. **Construire, tester et livrer** :
   ```bash
   MEDINA_OUT=dist python3 build_front.py && cp dist/MEDINA.html dist/MEDINA_final.html
   MEDINA_OUT=dist python3 test_v7.py J44 J18 I26 A41   # puis les 30 cours
   MEDINA_OUT=dist MEDINA_SOURCES_NAME=MEDINA_final_SOURCES.json python3 pack_v7.py
   python3 chantier.py
   ```
   Mettez ensuite à jour `audits/<CODE>.md` et `PROMPT_MEDINA.md` § 19, faites le commit et le push, puis terminez par le tableau de bord.

## 6. Règles pour ne rien casser

- Les données déjà vérifiées en texte intégral (`audits/<CODE>.md`) doivent être conservées exactement.
- Toute donnée nouvelle doit être vérifiée à la source primaire et consignée avec son URL et sa date.
- Les abréviations doivent toutes avoir une clé du glossaire. N’ajoutez jamais une clé qui existe déjà : la dernière définition chargée l’emporte dans tout l’atlas.
- Les classes doivent appartenir à la liste fermée, sans aucun attribut `style` ; le test statique le vérifie.
- Si plusieurs agents travaillent en parallèle, chacun reçoit ses propres fichiers. Les fichiers partagés se modifient par remplacement exact, jamais par réécriture complète. Aucun agent ne lance de commande git qui modifie l’état.

## 7. Outils de passation

`docs/passation/` contient :
- `consignes_gen.py` : le générateur de consignes par onglet ;
- `wf_contre_lecture.js` : la contre-lecture et la reprise ;
- `wf_reecriture_sequentielle.js` : l’ancien flux, lent, à ne pas réutiliser tel quel ;
- `mesure_texte.py` : les mesures de justification et d’espace.
