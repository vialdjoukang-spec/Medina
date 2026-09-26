# Prompt de reprise MEDINA, à donner tel quel à l’IA suivante

Tu reprends le projet **MEDINA**, un atlas de cours de médecine en français. Il prépare le Dr Vial Tato Djoukang à l’examen fédéral suisse de médecine humaine. Le dépôt GitHub est `vialdjoukang-spec/medina`. Tu travailles sur la branche `claude/medina-alpha-integration-7dul4i`. Tu fais un commit et un push à chaque étape validée. Tu ne crées aucune demande de fusion sans accord explicite.

## 1. Lis d’abord, dans cet ordre

1. `PASSATION_REECRITURE_2026-09-26.md` : il donne l’état exact et le travail restant.
2. `docs/STYLE_REDACTION.md` : ce guide de rédaction est obligatoire, et il prime sur tes habitudes.
3. `CLAUDE.md`, puis `PROMPT_MEDINA.md` : § 4 pour le contrat HTML, § 5 pour le glossaire, § 10 à § 14 pour le contenu, § 19 pour l’état du projet.
4. `audits/<CODE>.md` pour chaque cours que tu touches. Les données vérifiées en texte intégral y figurent ; tu les conserves exactement.

## 2. La règle d’or du propriétaire

**Le lecteur comprend, il ne devine pas.** Tu appliques cette règle à chaque phrase :
- **Phrases.** Tu écris des phrases courtes et complètes, avec un sujet et un verbe conjugué. Tu n’écris jamais de phrase nominale ni d’infinitif injonctif.
- **Parties.** Chaque partie s’ouvre par une annonce de deux à quatre phrases. Elle se développe ensuite, du normal au pathologique et du mécanisme à la décision. Elle se ferme par un encadré « À retenir ».
- **Explications.** Chaque affirmation dit quoi, puis pourquoi, puis ce que cela change pour le patient. Tu supprimes toute phrase qui n’explique rien.
- **Tableaux.** Avant chaque tableau, tu expliques la question posée et la logique des colonnes. Après, tu montres comment le lire, sur un exemple de patient.
- **Termes cliquables.** Chaque antécédent, symptôme, signe, examen, score, critère, médicament et essai important devient un mot vert. Ce mot ouvre une fenêtre réelle, rédigée selon les mêmes règles.
- **Sciences fondamentales.** Tu les traites au niveau universitaire. Chaque discipline part de la question clinique, décrit le normal, puis sa perturbation. Elle se termine par ses liens avec la clinique, les examens et le traitement.
- **Interdits.** Tu n’écris ni métaphore, ni jeu de mots, ni formule de chantier. Tu ne condenses jamais un cours.

## 3. Projet 1 : achever la réécriture de J44, J18, I26 et A41 (priorité absolue)

1. **I26 et A41, onglet 1.** Relis l’onglet 1 et complète ce que le rédacteur n’a pas terminé.
2. **Onglets 2 à 4 des quatre cours.**
   - Réécris l’onglet Examens complémentaires : pour chaque examen, donne la question qu’il tranche, son principe, ses valeurs normales, ses seuils de décision, ses limites et ses pièges. Garde au moins trois quiz.
   - Réécris l’onglet Sciences fondamentales, que le propriétaire juge le plus faible.
   - Réécris l’onglet Pharmacologie, avec le tableau des doses introduit et commenté, et des monographies complètes.
   - Le générateur `docs/passation/consignes_gen.py` produit une consigne par onglet. Tu peux confier ces trois onglets à trois rédacteurs en parallèle, à condition que chacun ait ses propres fichiers.
3. **Contre-lecture adverse.** Deux relecteurs indépendants vérifient chaque cours :
   - le premier contrôle le style et la profondeur ;
   - le second contrôle l’exactitude, avec au moins douze données nouvelles vérifiées à la source primaire, puis la cohérence et le contrat HTML.
   Tu corriges ensuite chaque écart fondé. Le script est `docs/passation/wf_contre_lecture.js`, et la version de référence est le commit `0a57926`.
4. **Livraison.** Reconstruis le fichier, teste les 30 cours au navigateur, empaquette les sources, puis livre `dist/MEDINA_final.html`. Les commandes figurent au § 5 de la passation. Termine par le tableau de bord.

## 4. Projets d’amélioration, une fois le projet 1 terminé

| Ordre | Projet | Ce qui est attendu |
|---|---|---|
| 2 | **Achever la vague 9** (vaisseaux, microcirculation, immunité) | Rédige I73, I83, I89, I95, D86, D90 et B24 au niveau de J45, selon le guide, puis ajoute 9 à `DONE_SYS`. |
| 3 | **Réécrire les chapitres condensés** | Porte D84, M06 et M32 au niveau de J45, avec le guide de rédaction. |
| 4 | **Appliquer le guide aux cours plus anciens** | Seulement si le propriétaire le demande, fais passer les cours de cardiologie, J45, T78, M31, I71, I80 et I70 au même style. |
| 5 | **Poursuivre le programme** | Suis l’ordre du § 9 de `PROMPT_MEDINA.md` : vague 2 (respiratoire), puis vagues 7, 5, 6, 4, 3, 8, 11 et 12, par cycles de deux systèmes (`/cycle`). |
| 6 | **Auditer les cours non audités** | Fais un audit indépendant noté sur 20, avec un rapport dans `audits/<CODE>.md` (`/audit <CODE>`). |
| 7 | **Réintégrer le volet Examen fédéral** | Ajoute le module GLOBALITY, chargé à la demande pour ne pas alourdir le fichier. |
| 8 | **Contrôle automatique du style** | Ajoute à `test_v7.py --static` un détecteur des phrases nominales, des infinitifs injonctifs et des tableaux sans paragraphe avant et après, pour qu’aucun cours ne régresse. |

## 5. Contrôles à chaque livraison

- `python3 test_v7.py --static <CODES>` doit afficher OK : ce test couvre le glossaire, les fenêtres, les préfixes, les classes et les styles en ligne.
- `python3 test_v7.py <CODES>` doit afficher OK au navigateur, sur PC et sur mobile.
- `build_medina.audit()` ne doit trouver aucune abréviation sans clé.
- Chaque donnée nouvelle est sourcée, avec son URL et sa date, dans `audits/<CODE>.md`.
- Tu termines chaque livraison par un tableau de bord : cours traités, mots, fenêtres, quiz, poids du fichier, alertes.

## 6. Façon de travailler avec le propriétaire

Tu lui réponds en français, avec un ton chaleureux, structuré et dense, en phrases complètes. Tu livres sans lui demander d’accord tant que les contrôles passent. Tu ne le sollicites qu’en cas de blocage réel.
