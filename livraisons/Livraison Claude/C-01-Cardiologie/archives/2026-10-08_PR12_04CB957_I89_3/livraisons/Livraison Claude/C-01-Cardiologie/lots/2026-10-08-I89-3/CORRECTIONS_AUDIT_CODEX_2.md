# I89 — Corrections après la réception Codex du lot I89-2 (C-01-Cardiologie), 08.10.2026

Fichiers modifiés : `chapters/I89/I89_c.html`, `I89_d.html`, `I89_pop2.html`, `I89_pop4.html`. Le glossaire n'a pas changé. Aucune opération Git.

## Sources officielles lues le 08.10.2026
Base DailyMed de la Bibliothèque nationale de médecine des États-Unis, notice complète de chaque produit (`https://dailymed.nlm.nih.gov/dailymed/services/v2/spls/<setid>.xml`) :
- minoxidil comprimés, setid 0b4fc036-9497-442b-b629-c4b386932789, version du 25.08.2026 ;
- hydralazine comprimés, 7dc89d53-ade0-40de-b7e3-d14f7151958d, version du 14.09.2026 ;
- ibuprofène comprimés sur ordonnance, 7c7b815b-d6f5-4ce6-b37f-f35d5c9f3254, version du 29.07.2026 ;
- prednisone comprimés, fec09050-5ac2-451b-a2b9-5a21b2def212, version du 15.09.2026 ;
- pénicilline V potassique, a0f02ee0-2f7e-449a-a742-be7a98cefec5, version du 29.09.2026.

Source PubMed : Lund et al., Acta Endocrinol 1986, PMID 3094309, doi:10.1530/acta.0.1130056. Seul le résumé a été lu.

## Passages modifiés
1. **`I89_d`, tableau des œdèmes médicamenteux, ligne « Rétention rénale ».** Avant : « baisse de la pression de perfusion rénale pour le minoxidil (Cohn) ; prostaglandines (Kim et Joo) ; minéralocorticoïde (Liu) ». Après : sous minoxidil, la baisse de la pression artérielle déclenche des mécanismes rénaux, dont une hausse de la rénine. Les anti-inflammatoires non stéroïdiens peuvent provoquer une rétention hydrique et un œdème. Les corticoïdes peuvent provoquer une rétention sodée avec œdème et une perte de potassium. La ligne cite les informations professionnelles américaines.
2. **`pop4` `i89-d-oedeme-medic`.** Le mécanisme commun « vasodilatateurs directs → baisse de la perfusion rénale » est retiré. Le minoxidil reprend son étiquetage : rénine, rétention de plusieurs centaines de milliéquivalents de sel sans diurétique, diurétique de l'anse presque toujours nécessaire. L'hydralazine reprend aussi son étiquetage : rénine, angiotensine II, aldostérone et réabsorption de sodium, œdème « moins fréquent », débit sanguin rénal maintenu ou augmenté. Le lien avec les prostaglandines est réduit à ce que dit l'étiquetage de l'ibuprofène : baisse de l'effet natriurétique du furosémide et des thiazides. Pour la prednisone, la mention de la dexaméthasone et le terme « minéralocorticoïde » sont retirés. « Le diurétique agit » devient « peut agir ». La ligne Source remplace Cohn, Kim et Joo et Liu par les quatre étiquetages.
3. **`pop4` `i89-d-penicilline`.** Avant : liaison covalente aux protéines liant la pénicilline, blocage de la réticulation et lyse (Kong). Après : inhibition de la biosynthèse du mucopeptide de la paroi, ou peptidoglycane, et effet bactéricide en phase de multiplication active. Les streptocoques des groupes A, C et G y sont « très sensibles ». Kong est retiré.
4. **`I89_c`, tableau des diagnostics différentiels, et `pop2` `i89-oed-systemique`.** Safer 2011 est remplacé par Lund 1986. L'étude a mesuré l'acide hyaluronique dans la peau de dix patients atteints de myxœdème primaire non traité. Il était plus élevé que chez les témoins et la thyroxine l'a fait baisser ; les autres glycosaminoglycanes n'étaient pas augmentés. Les auteurs proposent seulement qu'il « contribue » à l'œdème, qui ne prend pas le godet.

## Contrôles
- `verifier_sigles.py I89` → `{}`. « DailyMed » a été réécrit en toutes lettres dans le cours.
- `test_v7.py --static I89` → **OK** (36 953 mots, 43 fenêtres, 8 quiz, 5 Pareto).

## Réserves restantes
- Les étiquetages lus sont américains. L'information professionnelle suisse n'a pas été consultée.
- La rétention par les anti-inflammatoires non stéroïdiens est décrite par l'étiquetage de classe. Le rôle des prostaglandines n'y figure que pour l'interaction de l'ibuprofène avec les diurétiques.
- Lund 1986 est une petite étude, lue en résumé seulement ; le mécanisme y reste une hypothèse.
- Les glitazones et ENaC (travaux chez la souris) ainsi que le docétaxel ne relevaient pas de ce mandat et n'ont pas été vérifiés.
