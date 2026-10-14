# N18 — Maladie rénale chronique : rapport de l’auteur correcteur C02-R-NEPH (Cycle 2)

Ce rapport date du 14 octobre 2026. Il couvre la reprise, par Claude et sur instruction de Vial, de la remise Codex `livraisons/Livraison Codex/N-07-Néphrologie/travail/CYCLE_02_N18/`. Il s’agit d’une revue par intelligence artificielle : **aucune validation médicale humaine** n’a eu lieu. L’auteur n’a fait ni commit ni push.

## Réserves bloquantes de la passe 1 : 3 sur 3 traitées

- **R01, Kerendia et inhibiteurs modérés du CYP3A4.** La FI suisse de novembre 2025, relue le 14.10.2026, prévoit une dose initiale de 10 mg chez tout patient qui reçoit déjà un inhibiteur modéré du CYP3A4. La fenêtre `n18-kerendia` contient désormais :
  - la ligne de tableau correspondante ;
  - le mécanisme pharmacocinétique : 90 % de l’élimination passe par le CYP3A4, et l’aire sous la courbe est multipliée par 3,48 avec l’érythromycine, par 2,70 avec le vérapamil et par 1,57 avec la fluvoxamine ;
  - la surveillance du potassium à l’instauration et à chaque changement de dose ;
  - un exemple chiffré ;
  - des contre-indications complétées.

  La concordance a été vérifiée en P01-4, P02-1, P02-3, dans les Pareto et en A07-3, où figurent aussi les critères SSN de la finérénone.
- **R02, appariement entre affirmations et sources.** Un nouveau registre `preuves/source_ledger_claude.json` couvre 45 décisions. Chaque décision est reliée au passage pertinent :
  - chronicité : KDIGO, points de pratique 1.1.3.1 et 1.1.3.2, page S149 ;
  - catégories G et A : tables 2 et 3, page S137 ;
  - conversions : page S127 ;
  - hémoglobine sous Aranesp : FI Aranesp ;
  - équation de risque KFRE : KDIGO 2.2, page S156, et Schulz 2022.

  Chaque entrée porte la section, la population, les limites et le SHA-256 du document téléchargé.
- **R03, référence échographique normale.** L’image IMG-N18-E02-1 est désormais un montage de deux figures réelles, sous licence CC BY 4.0, tirées de Hansen et al. (2016) : un rein normal (figure 1) et une maladie rénale chronique (figure 22).
  - Le texte de E02-5 enseigne les repères normaux et la lecture comparée A/B.
  - Un tableau compare le rein normal et le rein atteint de maladie rénale chronique.
  - La fenêtre consacrée à la morphologie a été réécrite.

## Autres corrections

- **Réserves non bloquantes R04 à R07 :**
  - R04 : le compte de produits a été corrigé.
  - R05 : le contrôle à une semaine prévu par le consensus suisse figure dans le tableau de surveillance.
  - R06 : chacun des 21 Pareto contient un piège concret.
  - R07 : les dimensions réelles des images figurent dans le manifeste.
- **Encadrés « À retenir » :** les 21 encadrés sont réécrits en phrases complètes.
- **Dernier îlot :** il contient les critères formels KDIGO complets dans un `div.alert`, puis les paramètres clés chiffrés dans un `div.key`.
- **Fenêtres E03 :** leurs titres sont mis en accord avec leur contenu.
- **Libellé G5 :** il reprend le terme KDIGO « kidney failure ».
- **Glossaire :** les sous-codes N18.x et les mentions DualDose et FixDose y sont déclarés. La remise d’entrée échouait à l’audit des abréviations ; cet audit passe désormais.
- **Image n18_05 :** son poids passe de 8,6 Mo à 1,2 Mo.

## Enrichissements

- **Raisonnement de type SSP de l’Examen fédéral (A06-6) :**
  - un tableau des diagnostics différentiels classés par gravité, avec l’élément discriminant et l’examen décisif ;
  - les urgences néphrologiques selon la stratégie HUG 2017 ;
  - un quiz corrigé.
- **Fenêtre `n18-drapeaux` :** elle présente les drapeaux rouges du consensus SSED/SSN et les seuils de DFGe selon l’âge.
- **Fenêtre `n18-acidose-seuils` :** elle expose la divergence suisse sur le bicarbonate (18 ou 22 mmol/L) et la manière dont elle est résolue.

## Contrôles

- **`python3 test_v7.py --static N18` :** OK, exécuté sur un clone jetable (44 581 mots, 108 fenêtres, 4 quiz, 21 Pareto).
- **Aperçu isolé (`tools/night_preview.py`) :** la construction aboutit.
- **Contrôle navigateur Chromium, à 1440 px et à 390 px :**
  - aucune erreur JavaScript et aucun débordement horizontal ;
  - la figure 3 se charge ;
  - quatre fenêtres modifiées ont été ouvertes.
- **Nettoyage :** le worktree a été supprimé.

## Réserves ouvertes, non bloquantes

- **Figure A06 :** elle reste un parcours australien, dont la portée est annoncée dans le cours. Aucune alternative sous licence ouverte n’a été trouvée.
- **Fenêtres « -fenetre-1/2 » :** la plupart recopient encore des paragraphes du corps du cours.
- **Registre Codex :** ses 858 entrées n’ont pas été revues une à une.
- **Suite de la chaîne :** la passe 2 de l’auditeur croisé et la validation médicale humaine restent à faire.

## Preuves

- `docs/collaboration/reviews/2026-10-14/CYCLE_02_CLAUDE/N18/auteur/{entree.json, sortie.json, auteur.json, rapport.md}`
- `livraisons/Livraison Codex/N-07-Néphrologie/travail/CYCLE_02_N18/preuves/{source_ledger_claude.json, images_claude.json}`

## Passe 2 — réponse au pass1 croisé de C02-R-ENDO (14.10.2026)

- **X01 (fenêtres recopiées)** : les 42 fenêtres prescrites sont réécrites avec un approfondissement propre (tableaux de preuves, mécanismes, calculs nouveaux, limites) ; 0 % de phrases reprises du corps. Nouvelles fenêtres **n18-creatinine** et **n18-cystatine** ; 64 mots verts repointés.
- **X02 (consensus SSED/SSN 2024)** : potassium sous bloqueur (> 5,5 réduire, > 6 arrêter, chélateur), cibles tensionnelles (> 130/80, > 140/90 chez l’âgé fragile, MAPA, paliers de 8 semaines), hypolipémiants et objectifs LDL (< 1,8 et −50 %, < 1,4), fer et érythropoïétine, bandelette puis sédiment ; tableaux commentés et comparés à SSN 2025 et KDIGO ; matrice `preuves/couverture_suisse_claude.json`.
- **X03 (borne A2/A3)** : fenêtre de contentieux **n18-a3-borne**, piège Pareto A03 reformulé, tableaux A03-3, E02-4 et n18-acr harmonisés.
- Observations : KDIGO PP 2.2.2 ajouté ; infinitifs « Exercice : … » reformulés ; coquilles corrigées.
- Contrôles : `test_v7.py --static N18` OK (45 295 mots, 111 fenêtres, 4 quiz, 21 Pareto) ; aperçu Playwright 1440/390 px sans erreur ni débordement.
- Réserves ouvertes : image A06 australienne ; registre Codex non revu entrée par entrée (276 identifiants d’anciennes fenêtres retirés) ; aucune validation médicale humaine.
