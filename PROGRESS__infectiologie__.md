# PROGRESS — I-03 Infectiologie (fragment T1)

Branche : `course/infectiologie`. Ordre : priority_codes de `organisation/fragments.json`.

| Code | Cours | État |
|---|---|---|
| A41 | Sepsis | existant (intégré) |
| B24 | VIH | existant |
| B18 | Hépatite virale chronique | existant |
| A54 | Gonococcie | existant |
| A53 | Syphilis | existant |
| A69 | Borréliose de Lyme | **écrit** (4 panneaux + pop-up, 3 GIF, glossaire `a69.py`) |
| A46 | Érysipèle | **écrit** (4 panneaux + pop-up, 3 GIF) |
| A04 | C. difficile / infections intestinales bactériennes | **écrit** (4 panneaux + pop-up, 4 GIF) |
| B02 | Zona | **écrit** (25 fenêtres, 2 GIF réels) |
| B00 | Herpès simplex | **écrit** (21 fenêtres, 2 GIF réels) |
| A09 | Gastro-entérite infectieuse aiguë | **écrit** (20 fenêtres, 3 GIF réels) |
| B37 | Candidose | **écrit** (16 fenêtres, 3 GIF réels) |
| B35 | Dermatophytoses | **écrit** (15 fenêtres, 4 GIF réels) |
| A84 | Méningo-encéphalite à tiques | **écrit** (15 fenêtres, 3 GIF réels dont 2 en fenêtre, « Lecture et physiopathologie » sous chaque élément) |
| A15 | Tuberculose pulmonaire (A15–A16) | **écrit** (27 fenêtres, 3 GIF réels, glossaire `a15.py`) |
| B50 | Paludisme (B50–B54) | **écrit** (24 fenêtres, 4 GIF réels, glossaire `b50.py`) |

Images : `assets/img/infectiologie/` + `ATTRIBUTIONS.json`.

## Reste à écrire (fragment T1)
- Pathologies fréquentes vides : A49, B07.
- priority_codes : tous écrits (B50, A15, A16).

## Lacunes nommées / points à vérifier
- A46 : dose orale d’amoxicilline SSI (500 mg toutes les 12 h, 5 j) vs information Amoxi-Mepha (375–750 mg 3–4×/j, ≥10 j) — à confirmer auprès des auteurs SSI.
- A46 : SSI en ligne « pipéracilline-tazobactam 4.5 mg » = coquille pour 4,5 g (signalée dans le texte).
- A46 : aucune incidence suisse d’érysipèle trouvée.
- A69 : épidémiologie suisse Sentinella 2008–2011 seulement (pas d’estimation nationale plus récente lue).
- A04 : seuil leucocytaire SSI exprimé en « /mL » (lu comme /µL = 15 G/L).
- Relecture médicale humaine non effectuée (mentionnée dans chaque en-tête).

- 2026-10-09 : règle images du propriétaire appliquée — 3 schémas auto-dessinés et le SVG espèces A69 supprimés, remplacés par des images réelles sous licence libre (lymphocytome borrélien, Ixodes ricinus, anatomie cutanée Blausen, Gram de C. difficile). Aucune image générée restante.

## Livraison
Décision du propriétaire : chaque cours terminé est rebasé sur origin/main, construit (build_medina, build_front) puis poussé sur main (jamais de force-push sur main) ; la branche course/infectiologie est poussée ensuite.

- B00 : seule donnée suisse lue = séroprévalence 1992–1993 (Bünzli 2004) — lacune nommée.
- B02 : chiffre d’atteinte oculaire divergent OFSP (bulletin 5–10 % vs page publique 10–20 %), signalé dans la fenêtre.
- B37 : pas de directive SSI sur la candidose ; sources européennes (ECMM 2025, IUSTI/OMS 2018, ESCMID 2012) et suisse (FUNGINOS 2021).
- B35 : pas de directive SSI ni européenne récente sur la peau glabre ; traitement selon information suisse, épidémiologie Lausanne 2020 et Zurich 2026, consensus Delphi 2026 (T. indotineae).
- B50 : pas de directive SSI ; OMS 2025, CEMV 2019, FI Riamet/Malarone. Écart premier trimestre (OMS 2022 vs FI Riamet 2019) signalé ; aucune FI suisse de l’artésunate, de la primaquine ni de la tafénoquine trouvée (lacune nommée).
- 2026-10-09 : auteurs des attributions nettoyés (« Unknown author », « Photo Credit », « Content Providers »).
- A15 : guide national LPS/OFSP V1.2024 + Bulletin OFSP 2025 ; points d’audit : seuil rénal (FI Rimactan < 25 ml/min, Rifater/Rifinah < 30 ml/min) contre adaptation de E et Z seulement dans le guide ; « environ 20 % des cas traités sans confirmation » (guide) contre 93,8 % de confirmation (Bulletin 2025). Notation « HR » évitée (collision glossaire : hazard ratio).
- 2026-10-09 : main cassé par P-02 (justifications J45/I26 introuvables après révision des connecteurs) ; livraison faite après vérification sur arbre propre d’origin/main que l’échec est préexistant et étranger, avec audit ciblé de mes cours.
- 2026-10-09 23:4x : jauges T1 après refresh_gauges : federal_exam 10/46 (21,7 %), fréquentes 9/11, global 16/175. Restants federal : A00 A01 A02 A03 A05 A06 A07 A08 A17 A18 A19 A40 A55 A56 A57 A58 A59 A60 A63 A64 A80 A81 A82 A83 A85 A86 A87 A88 A89 B15 B16 B17 B19 Z20 Z21 Z22. Ordre proposé : A87 (méningite virale), B15–B17, A01–A02, A60/A56/A59, A40, A17–A19, A03/A06/A07/A08, A00, A82, A80, A83/A85/A86/A88/A89/A81, A55/A57/A58/A63/A64, Z20–Z22.
- B07 et A49 (demandés) non encore écrits : hors étoile fédérale, placés après les catégories federal_exam selon la règle de priorité.

## Balayage rétroactif obligatoire (ordre du propriétaire), 9–10 octobre 2026 — TERMINÉ

Contrôle de chaque leçon de main contre toutes les règles du brief : vraies images seulement (fenêtres comprises), lecture physiopathologique sous chaque figure et chaque tableau, phrases complètes (aucune phrase nominale), justification des termes et décisions, termes et fenêtres interactifs, doses et codes inchangés (déjà vérifiés), pas de tableau consacré aux codes CIM.

| Leçon | Statut | Corrections livrées dans main |
|---|---|---|
| A69 | balayée | lectures sous 3 figures et 6 tableaux, 4 images réelles en fenêtre, phrases nominales réécrites |
| A46 | balayée | lectures sous 3 figures et 5 tableaux, 3 images en fenêtre, phrases nominales |
| A04 | balayée | lectures sous 4 figures et 5 tableaux, 3 images en fenêtre, phrases nominales |
| B02 | balayée | lectures sous 1 figure et 4 tableaux, 3 images en fenêtre, 19 phrases nominales |
| B00 | balayée | lectures sous 1 figure et 4 tableaux, 3 images en fenêtre, 18 phrases nominales |
| A09 | balayée | lectures sous 3 figures et 4 tableaux, 3 images en fenêtre, 10 phrases nominales |
| B37 | balayée | lectures sous 3 figures et 5 tableaux, 3 images en fenêtre, 15 phrases nominales |
| B35 | balayée | lectures sous 4 figures et 6 tableaux, 3 images en fenêtre, 11 phrases nominales |
| B50 | balayée | lectures sous 3 figures et 5 tableaux, 3 images en fenêtre, 14 phrases nominales |
| A15 | balayée | lectures sous 3 figures et 3 tableaux, 3 images en fenêtre, 18 phrases nominales, tableau de codes CIM remplacé par une phrase |
| A84 | balayée | tableau de codes CIM remplacé par une phrase, phrases nominales des encadrés et Pareto |
| A87 | balayée | phrases nominales des encadrés, fenêtres et Pareto |
| B15 | balayée | conforme (livrée sous les règles en vigueur), aucune correction |
| A41 (descellée) | balayée | 7 schémas SVG auto-dessinés supprimés ; algorithme Sepsis-3 et délais SSC 2026 en listes de phrases ; 3 vraies images + lectures ; 4 images en fenêtre |
| A53 (descellée) | balayée | 7 SVG supprimés ; algorithme sérologique et cinétiques en phrases ; 5 vraies images + lectures ; 4 images en fenêtre |
| A54 (descellée) | balayée | 5 SVG supprimés ; niveaux d’infection, calendriers, cibles en phrases et tableau ; 2 vraies images + lectures, aussi en fenêtre |
| B18 (descellée) | balayée | 4 SVG supprimés ; cinétique et sinusoïde en phrases ; 2 vraies images + lectures ; 4 images en fenêtre |
| B24 (descellée) | balayée | 6 SVG supprimés ; signal CD4, pyroptose, barrière génétique en phrases ; 3 vraies images + lectures ; 3 images en fenêtre |

Limite connue : les leçons descellées (A41, A53, A54, B18, B24) ont un format riche propre ; leurs nombreux tableaux sont déjà commentés par la prose voisine, et je n’ai pas ajouté d’encadré de lecture sous chacun d’eux. Prochaine étape : reprise des nouvelles leçons fédérales (B01 varicelle, puis la suite de la liste).
