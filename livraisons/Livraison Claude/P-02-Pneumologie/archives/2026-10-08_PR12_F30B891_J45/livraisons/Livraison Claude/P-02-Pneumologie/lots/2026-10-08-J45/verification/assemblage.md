# Rapport d’assemblage — J45 — Asthme (P-02-Pneumologie)

Copie : `scratchpad/wt_j45` (aucune opération Git). Fichiers modifiés par l’assembleur : `J45_b.html`, `J45_c.html` (panneau pE seulement), `J45_d.html`, `J45_pop1.html`, `J45_pop4.html`, `J45_justifications.json`. `glossary/j45.py` n’a pas été modifié, car aucun nouveau sigle n’était nécessaire.

## 1. Propositions appliquées, par rapport source
- **Pathologie (P1–P11)** : P1 à P8 sont appliquées mot pour mot dans `J45_b` (§ 9.1, 9.2, 11.3, 12.1 à 12.4, piège MART). P9 et P11 sont appliquées dans les Pareto `clin` et `urg`. P10 est appliquée dans pE (réversibilité VEMS ou CVF, seuil de l’enfant, 200 à 400 µg et lecture à 10 à 15 minutes, heure de prélèvement des biomarqueurs, PaCO₂ > 45 mmHg).
- **Examens (rôle qui a révisé J45_b et pop2)** :
  - Les propositions 1 à 3 (`j45-eos`, `j45-gaz`, `j45-feno`) étaient déjà intégrées par le rôle Pathologie dans pop1. Je l’ai vérifié.
  - Les propositions 4 à 7 sont appliquées dans pE : gazométrie, délais de suspension, PD20 ERS 2017, test d’effort chez l’enfant, éosinophiles du matin et strongyloïdose, seuils FeNO de GINA.
  - La proposition 8 était déjà présente dans j45-sp, et la proposition 9 dans `j45-d-mg`.
  - La proposition 10 est appliquée dans les Pareto `urg`, `diag` et `crit`.
- **Sciences** :
  - La proposition 1 était déjà intégrée.
  - La proposition 2 est appliquée dans `j45-remod` : absence de régression démontrée, Grainge 2011 et lien observationnel. La référence a été ajoutée.
  - La proposition 3 est appliquée dans `J45_b` § 8.2 (Perrin 2011).
  - Pour la proposition 4, `J45_a` § 3.5 contenait déjà une formulation équivalente rédigée par le rôle Pathologie ; elle est conservée.
  - Les propositions 5 et 6 sont traitées aux sections 3 et 4 ci-dessous.
- **Pharmacologie** :
  - La proposition 1 est appliquée : le texte du Pareto `pharma` est repris mot pour mot, et `data-cover` couvre désormais `j45-p-1` à `j45-p-8`.
  - Les propositions 2 (ipratropium en Suisse) et 3 (magnésium chez l’enfant) sont appliquées dans `J45_b` § 8.2.

## 2. Arbitrages
- **Béclométasone-formotérol en MART.** Les rôles Examens et Pathologie (P8) divergeaient. J’ai retenu P8. GINA 2026 (rapport, p. 88 ; § « Box 4-8 » ; ligne « GINA suggests that the same advice should also apply ») applique le repère de 12 inhalations au total ; le mot « temporairement » n’y figure pas. La phrase sur la limite européenne de 8 inhalations est conservée.
- **Délais de suspension.** GINA 2026 indique « au moins 4 heures » pour le bêta-2 agoniste de courte durée, la norme ATS/ERS 2019 « 4 à 6 heures ». Les deux valeurs sont citées avec leur source.
- **Salbutamol dans la crise sévère.** `J45_d` indiquait « jusqu’à 3 fois ». J’ai aligné le texte sur l’algorithme de GINA 2026 (summary guide) : « à répéter si nécessaire toutes les 20 à 30 minutes », comme `J45_b`.
- **Pareto `clin`.** La ligne ajoutée par P9 sur le contrôle a été fusionnée avec la ligne existante, pour éviter de répéter « contrôle ≠ risque futur ».
- **P11.** J’ai gardé la formulation de GINA, « PaCO₂ normale ou élevée, surtout > 45 mmHg », plutôt que « PaCO₂ > 45 mmHg » seule.

## 3. Justifications
Dans `J45_a`, « limitation variable du débit expiratoire » apparaît une fois dans la définition et une fois dans l’encadré « À retenir ». La seconde occurrence est un résumé voulu, pas une redite. J’ai donc ajouté `"occurrence": 1` à l’entrée `j45-j-variabilite`. Les 15 justifications compilent, sur 15 cibles.

## 4. Pareto resynchronisés
- `clin`, `diag`, `urg`, `tt`, `crit`, `exam` et `pharma` ont été réécrits sur le contenu final des onglets.
- `sci` a été conservé tel que le rôle Sciences l’a établi, car il reste cohérent avec les onglets.
- `crit` contenait une erreur : il exigeait une obstruction inférieure à la limite inférieure de la normale. Il exige désormais la variabilité, et le rapport inférieur à cette limite renforce le diagnostic sans suffire. Le suivi après une exacerbation est fixé à 2 à 7 jours (2 à 5 chez l’enfant).

## 5. Divergences transversales corrigées
- **IgE totales de l’ABPA.** pE indiquait « > 1 000 UI/mL » ; la valeur est alignée sur `j45-abpa` : ≥ 500 UI/mL selon les critères ISHAM 2024.
- **ANCA dans l’EGPA.** pE indiquait « environ 40 % » ; le texte dit désormais « une minorité », comme `j45-abpa`.
- **Réduction du traitement.** Le délai est maintenant partout de 2 à 3 mois (`J45_b` § 9.2 et 11.3, Pareto `tt` et `crit`, `J45_d`).
- **Suva.** La formulation « annonce à l’assureur-accidents » est reprise dans le quiz de pE et le Pareto `crit`.
- **Variabilité du débit de pointe.** La référence est « ERS 2022 » au lieu de « ERS 2021 » dans le quiz 4 de pE.
- **Budésonide-formotérol dans la crise légère.** `J45_d` donne maintenant « 200/6 µg (160/4,5 µg délivrés) ».
- **Gazométrie.** pE la réserve désormais aux crises avec débit de pointe ou VEMS < 50 %, absence de réponse ou aggravation.
- **Biomarqueurs dans pE.** Ils servent à soutenir le diagnostic ; la mention « recommandé au diagnostic » a été retirée.
- **Contrôles par grep.** Plus aucune occurrence de 42 mmHg, 5,6 kPa ou des anciennes cibles de saturation 93–95 %, 94–98 % ou 90 % hors contexte. Les autres valeurs suivantes sont identiques partout :
  - saturation < 92 % et cible de 92 à 95 % ;
  - salbutamol 4, 4 à 6 ou 6 à 10 bouffées ;
  - MART 12/8 ;
  - FeNO > 50/> 35 ppb ;
  - éosinophiles plus élevés le matin et FeNO plus basse le matin ;
  - prednisone 40 à 50 mg pendant 5 à 7 jours.
- **Style.** La phrase infinitive de `J45_b` § 11.1 a été réécrite.

## 6. Contrôles (depuis la copie)
- `verifier_sigles.py J45 chapters/J45/*.html` → `{}`
- `test_v7.py --static J45` → `J45 mots 41401 fenêtres 46 quiz 8 pareto 8` puis **OK**
- `insert_justifications.py --course J45 --root .` → 15 fenêtres, 15 cibles, aucune erreur
- `build_front.py` → MEDINA.html de 16 739 424 octets, compressé à 9 927 382 octets ; `--all-fragments` → 22 fragments
- `audit_fragments.py` → « audit réussi : 22 fragments, JavaScript valide, build reproductible »
- `verify_course_native.cjs J45` → `{"result":"passed","checks":2282,"failures":0}`
- Les balises de chaque fichier ont le même décalage structurel qu’au commit HEAD (a +3, b −2, d −1 pour les `div`).

## 7. Problèmes restants
- Les catégories PD20 de l’ERS 2017 et les contre-indications de la méthacholine n’ont pas été lues en texte intégral (erreur 403).
- Les informations professionnelles suisses (Compendium) n’ont pas été consultées : limites MART, ipratropium, Trimbow.
- Les sources de l’OFSP et de la Société suisse de pneumologie n’ont pas été consultées.
- Le volume a fortement augmenté (41 401 mots) ; une passe de concision reste utile.
- Aucune nouvelle affirmation médicale n’a été créée hors des propositions. Les ajouts de pE reprennent des faits déjà présents dans `J45_b` et `j45-pop1` ou `j45-pop2`.
- La revue reste ciblée et non exhaustive : le cours n’est pas déclaré validé.
