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
