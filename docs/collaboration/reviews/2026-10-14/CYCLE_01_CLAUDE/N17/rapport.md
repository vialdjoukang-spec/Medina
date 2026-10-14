# N17 — Insuffisance rénale aiguë : audit et correction Claude, Cycle 1 (14 octobre 2026)

Acteur : sous-agent Claude d'audit N17, branche `claude/great-cerf-uizsml`. Il s'agit d'une revue par intelligence artificielle, sans validation médicale humaine. Le détail se trouve dans `audit.json` : empreintes avant et après, sources avec passages exacts, corrections et réserves.

## Notes

| Critère (grille §16) | Passe 1 | Passe 2 |
|---|---|---|
| Exactitude et actualité (4) | 3,5 | 3,5 |
| Complétude (3) | 2,0 | 2,5 |
| Pédagogie (3) | 2,5 | 3,0 |
| Corrélations vertes (2) | 2,0 | 2,0 |
| Sciences et schémas (2) | 1,5 | 2,0 |
| Examens (2) | 1,5 | 2,0 |
| Pharmacologie (1) | 0,5 | 1,0 |
| Pareto (1) | 1,0 | 1,0 |
| Langue (1) | 0,5 | 0,5 |
| Interface (1) | 1,0 | 1,0 |
| **Total /20** | **16,0** | **18,5** |

## Passe 1 : constat

J'ai revérifié **23 chiffres clés** dans la source primaire, avec une consultation le 14.10.2026 :
- les critères et les stades KDIGO 2012, ainsi que la clause pédiatrique ;
- la page KDIGO, qui confirme que le texte de 2026 reste un projet ;
- les recommandations NICE NG148 sur les délais d'échographie (6 et 24 heures) et de dérivation (12 heures) ;
- l'ensemble des repères UKKA 2023 sur l'hyperkaliémie ;
- la figure 2 de l'ERC 2025, lue visuellement ;
- le Resuscitation Council UK 2025 ;
- le bundle des HUG, lu sur l'image ;
- la Revue médicale suisse 2017 ;
- le dépistage 2025 de la Société suisse de néphrologie ;
- les informations professionnelles suisses de Lasix, Noradrenalin Sintetica, Bicarbonate Bichsel, Glucose Fresenius et Actrapid HM.

Je n'ai trouvé **aucune posologie fausse, aucun seuil faux et aucune contre-indication omise**. L'attribution « recommandation britannique de réanimation 2025 » paraissait douteuse. Elle est en réalité confirmée par la page du RCUK.

Les écarts relevés sont les suivants :
- Il n'y avait aucun raisonnement par situations de départ SSP et aucun diagnostic différentiel hiérarchisé.
- L'étape d'élimination du potassium n'était pas décrite.
- Le syndrome de levée d'obstacle était absent.
- Le cours ne comportait aucune image réelle.
- Une formulation KDIGO sur les diurétiques était trop forte.
- Plusieurs phrases décrivaient la fabrication du cours (« Ce cours… », « Le cours retient… »).
- Certaines légendes de schémas SVG ne disaient pas qu'il s'agissait de schémas didactiques.

## Corrections

- **Médicale (précision)** : j'ai corrigé une phrase sur KDIGO 3.4.1–3.4.2. Le texte distingue maintenant « recommande de ne pas » pour la prévention et « suggère de ne pas » pour le traitement, hors surcharge.
- **Linguistiques** : j'ai supprimé neuf formules de fabrication dans l'onglet a, l'onglet d, pop1 et pop2, et corrigé une majuscule fautive.
- **Présentation** : toutes les figures SVG sont maintenant légendées « Schéma didactique ».

## Enrichissements

1. **Îlot 7.1 : raisonnement par situations de départ.**
   - Un tableau couvre les SSP PROFILES 63, 161, 164 et 173. Pour chacune, il donne les hypothèses, l'élément discriminant et l'examen décisif.
   - Un tableau classe **dix diagnostics différentiels par gravité**, de l'obstruction infectée à la fausse hausse de créatinine.
   - Le texte explique comment orienter le diagnostic à partir de la numération sanguine.
   - Un nouveau quiz porte sur une anurie due à un globe vésical.
2. **Hyperkaliémie.**
   - Délais d'action du calcium (3 minutes, durée de 30 à 60 minutes) et de l'insuline (15 minutes ; baisse de 0,65 à 1,0 mmol/L ; effet d'environ 2 heures).
   - Étape d'élimination : par les urines, par un chélateur ou par la dialyse.
   - Salbutamol en adjuvant.
   - Indications de dialyse selon l'ERC.
3. **Nouvelle fenêtre Lokelma**, fondée sur l'information professionnelle suisse exacte (autorisation 67851, janvier 2026). Elle explique la tension entre cette information professionnelle, qui exclut l'usage comme médicament d'urgence, et UKKA/ERC.
4. **Nouvelles fenêtres** :
   - syndrome de levée d'obstacle, d'après le Collège français d'urologie ;
   - distinction entre forme aiguë, maladie rénale aiguë et forme chronique, d'après les tableaux 11, 13 et 14 de KDIGO et l'AFU.
5. **Autres ajouts** :
   - cristalloïdes plutôt que colloïdes ;
   - repères nutritionnels de KDIGO ;
   - modes de dérivation ;
   - créatinine toutes les 24 à 48 heures ;
   - précaution Lasix en cas d'obstacle à l'écoulement de l'urine ;
   - surveillance tensionnelle sous noradrénaline ;
   - part obstructive de l'IRA : 2 à 5 % selon la revue suisse, environ 10 % selon l'AFU ;
   - Paretos complétés.

## Images réelles

J'ai ouvert et vérifié visuellement chaque image. Toutes sont commentées avec la physiopathologie correspondante.

| Fichier | Contenu | Licence |
|---|---|---|
| `n17_ecg_hyperkaliemie.jpg` | ECG avec kaliémie à 8,2 mmol/L | CC BY 4.0 (Agbayani et Gonzales) |
| `n17_sediment_cylindres.jpg` | Cylindres tubulaires, granuleux, leucocytaires et érythrocytaires | CC BY 4.0 (Mohsenin, J Intensive Care 2017) |
| `n17_echographie_hydronephrose.jpg` | Hydronéphrose modérée | CC BY-SA 4.0 (Cerevisae) |
| `n17_histologie_atteinte_tubulaire.jpg` | Biopsie : atteinte tubulaire aiguë et néphrite tubulo-interstitielle | CC BY 4.0 (Chávez-Iñiguez et al., BMC Nephrol 2018) ; légende vérifiée sur Europe PMC |

## Réserves ouvertes

- Aucune validation médicale humaine.
- La divergence sur le débit du calcium entre UKKA/ERC et les HUG reste à arbitrer localement.
- La tension entre l'information professionnelle de Lokelma et UKKA/ERC est exposée, mais pas tranchée.
- Aucune posologie suisse du salbutamol nébulisé n'a été vérifiée ; le cours n'enseigne donc aucune dose de prescription suisse.
- Les matrices de contexte et de couverture suisses ne sont pas régénérées.
- Je n'ai pas fait de contrôle dans un navigateur réel.
- La fréquence relative des causes n'est pas chiffrée dans les sources.
- Le texte antérieur n'a pas été réécrit intégralement.
- Deux images proviennent des vignettes officielles de Wikimedia, car l'original renvoyait une erreur HTTP 429.

## Contrôle technique

`python3 test_v7.py --static N17` → `N17 mots 25353 fenêtres 81 quiz 5 pareto 14` / **OK**.
