# I50 — Insuffisance cardiaque : contrelecture indépendante ciblée

Date : 7 octobre 2026. Fragment : **C-01-Cardiologie**. Base : `3cbe0f52f799e27e0a2d9a65fd7d8093187af37d`.

La contrelecture porte sur le diff des sources `chapters/I50`, les endroits consommateurs et les fenêtres associées. Les retouches signalées pendant cette contrelecture ont été appliquées par l'intégrateur, puis vérifiées. Aucun fichier du cours n'a été modifié par le contrelecteur.

**Conclusion du lot ciblé : aucune correction supplémentaire nécessaire n'a été identifiée après ces retouches.** Ce résultat ne constitue pas une certification médicale exhaustive du cours.

| Point contrôlé | Résultat de la contrelecture |
|---|---|
| BNP sous sacubitril/valsartan : `I50_b.html`, `#i50-7` | La hausse est présentée comme possible. Le BNP conserve sa valeur pronostique ; l'attribution automatique au médicament est écartée. |
| Tableau biologique : `I50_c.html`, `#e-2` | Le NT-proBNP n'est plus décrit comme « inchangé ». Sodium et potassium ont des lignes distinctes, avec leurs rôles cliniques propres. Les cibles `Sodium` et `Potassium` restent natives. |
| Quiz BNP : `I50_c.html`, `#e-6` | La réponse et sa justification exigent une confrontation clinique. Elles ne déduisent automatiquement ni une décompensation ni un simple effet de l'ARNI. |
| Sciences et Pareto BNP : `#sb-i`, `pareto-sci`, `d-arni` | La concentration mesurée peut augmenter par modification de la dégradation. Le texte n'appelle plus cette modification un « effet analytique » systématique. Le Pareto conserve la valeur pronostique. |
| Créatinine : `I50_d.html`, `#p-4`, banque `i50-j-rein-traitement` | Le repère ESC 2021 emploie les deux conditions conjointes : hausse transitoire **< 50 % ET valeur < 266 µmol/L**. Le contexte KDIGO sous IEC/ARA II avec maladie rénale chronique reste distinct. |
| Diurétiques : `#p-4`, `pareto-pharma` | L'adaptation dépend de la déplétion et de la congestion. Le médecin « envisage » une réduction ; l'euvolémie seule n'entraîne plus mécaniquement une baisse de dose. L'hypoperfusion exige une évaluation urgente. |
| Référence rénale | Le renvoi a été corrigé en **ESC 2021, section 13.6**, conformément au texte primaire consulté. |
| Hyponatrémie : `#i50-11`, `pareto-suivi`, `i50-j-hyponatremie-conduite` | Dilution et pertes de sel sont distinguées. La restriction hydrique dépend de la volémie. Les symptômes neurologiques sévères exigent une prise en charge urgente ; aucun bénéfice de survie n'est inféré de la seule correction. |
| Digoxine : `d-dig`, `i50-j-digoxine-interactions` | L'exposition, la sensibilité liée au potassium et l'élimination rénale sont distinguées. La glycoprotéine P explique une partie des interactions. L'amiodarone et le vérapamil sont explicitement nommés pour l'effet sur la conduction ; ce dernier n'est pas attribué indistinctement à la clarithromycine. |
| Source moléculaire digoxine | Katz 2010 a été ajouté pour l'antagonisme potassium–liaison. Cette étude sur enzymes humaines recombinantes soutient l'étape moléculaire ; elle ne détermine pas une posologie ou un risque individuel. La notice reste l'appui clinique. |
| Échocardiographie : `#e-3`, quiz `#e-6`, `pareto-exam`, `i50-j-echo-remplissage` | Les indices sont qualifiés d'indirects. E et e′ sont distingués ; le rapport s'interprète avec les autres paramètres, le rythme et les valvulopathies. Il ne devient pas un diagnostic autonome. |
| Histologie : `#sh-i` | Le code SVG dessine désormais deux branches parallèles, mécanique et électrique, qui convergent. Il correspond à la description. Le substrat de réentrée est présenté comme possible ; la fibrose seule n'établit pas une arythmie active. |
| Anémie : `i50-j-anemie` | La limite nouvelle distingue hémodilution et réduction de masse globulaire. L'évolution sous décongestion ne remplace pas la recherche étiologique. |

## Sources utilisées

- [Myhre et coll., PARADIGM-HF, JACC 2019, PMID 30846338](https://pubmed.ncbi.nlm.nih.gov/30846338/) : résumé original consulté ; évolution et valeur pronostique des deux peptides.
- [ESC 2021, European Journal of Heart Failure, sections 13.6–13.7](https://onlinelibrary.wiley.com/doi/full/10.1002/ejhf.2333) : passages du texte intégral consultés ; contexte des repères rénaux et troubles électrolytiques.
- [KDIGO 2024, points 3.6.2–3.6.5 et 3.7.3](https://kdigo.org/wp-content/uploads/2024/03/KDIGO-2024-CKD-Guideline.pdf) : passages du PDF officiel consultés ; surveillance IEC/ARA II et baisse initiale du DFG sous iSGLT2.
- [DailyMed, information officielle digoxine, sections 5.3 et 7.1–7.3](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9ca08b66-55eb-4155-a8bd-6fa2282adab4) : sensibilité à la toxicité, interactions pharmacocinétiques et conduction.
- [Katz et coll., J Biol Chem 2010, PMID 20388710](https://pubmed.ncbi.nlm.nih.gov/20388710/) : résumé et description de la figure 4 consultés ; antagonisme du potassium sur la liaison de la digoxine aux isoformes humaines de la pompe.
- [ASE 2025, fonction diastolique et diagnostic d'ICFEp](https://www.asecho.org/wp-content/uploads/2025/07/Left-Ventricular-Diastolic-Function.pdf) : passages du PDF officiel consultés ; approche multiparamétrique et limites des indices.
- [Androne et coll., Circulation 2003, PMID 12538419](https://pubmed.ncbi.nlm.nih.gov/12538419/) : résumé original consulté ; distinction hémodilution/anémie réelle dans une population sélectionnée.

## Vérification technique et limites

La compilation indépendante par `load_course_justifications` retrouve **24 fenêtres et 24 cibles**, avec `exhaustive_review: False`. Les trois nouvelles cibles sont effectivement retrouvées : `I50_b.html` / `i50-11` / `restriction hydrique`, `I50_d.html` / `p-2` / `Digoxine`, et `I50_c.html` / `e-3` / `Rapport E/e′ moyen`. La nouvelle explication de digoxine vise un texte natif du tableau, pas un template bloqué par le compilateur. `git diff --check -- chapters/I50` ne signale pas d'erreur.

Les seuils rénaux ne constituent pas des règles universelles. L'analyse de biomarqueurs et les résultats expérimentaux ne remplacent pas le raisonnement clinique. La portée demeure limitée aux modifications examinées : les autres doses, indications, classes de recommandation, seuils et affirmations non modifiés n'ont pas été réaudités. La classification attribuée à ESC 2026 n'a pas été remplacée par le référentiel 2021 ; sa vérification officielle a été conduite séparément par l'intégrateur. La topologie SVG a été contrôlée dans le code ; la vérification visuelle et les essais d'interface relèvent du contrôle final de l'intégrateur.
