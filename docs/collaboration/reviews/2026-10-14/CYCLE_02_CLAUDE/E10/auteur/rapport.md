# E10 — Diabète sucré de type 1 : rapport de l’auteur correcteur C02-R-ENDO

Cycle 2 MEDINA, 14 octobre 2026. Agent : `claude-code/session_01NNsXRGeno3p5fi2QvuhRCM/C02-R-ENDO`. Aucune validation médicale humaine. Ni commit, ni push, ni injection.

## Relevés

- Entrée : `entree_empreintes.json` (sept sources et neuf images identiques à `pass1.json`) et `entree.json` (sept contrôles du Prompt de vérité).
- Sortie : `sortie.json`. Preuve auteur : `auteur.json`.
- Registre des sources : `livraisons/Livraison Codex/E-06-Endocrinologie et métabolisme/travail/CYCLE_02_E10/preuves/source_ledger_claude.json` (48 assertions, empreinte du texte téléchargé le 14.10.2026).
- Manifeste des images : `…/preuves/images_claude.json` ; preuve Commons : `…/preuves/commons_GangreneFoot_api_claude.json` et `…_wikitext_claude.txt`.

## Les huit réserves de la passe 1

| Réserve | Correction de l’auteur | Source relue aujourd’hui |
|---|---|---|
| R01 SSED technologie | Tableau des quatre métriques adultes ; interférences par modèle ; standard de soins, systèmes communautaires, remboursement, télémédecine et consentement ; objectifs enfant et personne âgée fragile ; tableau grossesse et adaptations | SSED 2025, pp. 7–37 |
| R02 Conduite | Tableau du premier groupe par risque ; grade III et capteur ou 6–8 mesures pendant un an ; HbA1c > 10 % ; discordance texte/tableau signalée ; second groupe en fenêtre | SGED/SGRM août 2025, §9 et tableaux 1–3 |
| R03 Baqsimi | Encadré des interactions indométacine, warfarine, bêtabloquants, synchronisé dans deux fenêtres | FI Baqsimi, mars 2026 |
| R04 Acidocétose | Remplissage, insuline, tableau potassium, tableau des critères horaires de réponse, relais ; légende de la figure 2 ; fenêtre de calcul | JBDS mars 2023 ; FI NovoRapid ; RMS 2019 |
| R05 Pied | Niveaux de risque, grades 1–3, suivi hebdomadaire, escalade < 10 %/semaine et < 50 % en 4 semaines, drapeaux rouges, décharge ; fenêtre de calcul | QualiCCare/SGED 2023 |
| R06 Figures | « du premier au quatrième orteil » ; GLUT4 absent de la figure 7 déclaré ; légende de la figure 6 corrigée ; licence Commons archivée ; huit licences recontrôlées | Commons, Europe PMC, Frontiers, LibreTexts |
| R07 Rapport de capteur | Lecture guidée en tableau de ce qui est visible ou absent sur les figures publiées, données à obtenir, fictif séparé | PMC10888350, figures inspectées |
| R08 Rédaction | Infinitifs injonctifs et phrases de fabrication réécrits ; 21 Pareto réécrites ; liens contextuels ; corrélations des sciences explicites | STYLE_REDACTION |

La levée formelle de ces réserves appartient à la passe 2 du relecteur croisé C02-R-NEPH.

## Autres corrections et enrichissements

- Glossaire `e10.py` reconstruit sur les vraies clés : la remise d’entrée échouait déjà à `test_v7.py --static` (abréviations non couvertes).
- Confirmation d’un résultat isolé : absente de la position SSED 2011 ; reformulée comme lacune.
- Deux tableaux de raisonnement de l’examen fédéral (hyperglycémie avec soif/polyurie ; trouble de conscience), hiérarchisés par gravité puis fréquence, avec élément discriminant et examen décisif.
- Quatre fenêtres nouvelles avec calculs refaisables ; 42 fenêtres prescrites et 21 parties conservées.

## Contrôles techniques

- `python3 test_v7.py --static E10` dans un worktree jetable : **OK** (31 572 mots, 106 fenêtres, 3 quiz, 21 Pareto). Worktree et aperçu supprimés.
- Aperçu `tools/night_preview.py` (build_exit 0) puis Playwright 1440 et 390 px : aucune erreur JavaScript, aucun débordement ; nouvelles fenêtres ouvertes (captures `ui_*.png`).

## Réserves ouvertes

- Sources non relues ce jour (catalogues Viollier et La Source, revues mécanistiques, OpenStax, carte Sick Day Rules, note SSED de retraits) : couvertes seulement par le registre Codex.
- FI suisse d’une insuline soluble humaine intraveineuse non trouvée par AmiKo : le cours ne la nomme pas.
- Page MDPI inaccessible ; licence de la figure 7 vérifiée par Europe PMC.
- Discordance interne du texte de conduite non tranchée.
- Aucune validation médicale humaine.
