# PROGRESS — G-04-Gastroentérologie et hépatologie (fragment S03)

Branche : `course/gastro-hepatologie`. Générateur et sources : `livraisons/Livraison Grok/G-04-Gastroenterologie-hepatologie/`.
Statut des cours : rédigés et contrôlés techniquement (abréviations, fenêtres, Pareto) ; **non audités** (audit Claude/Codex et validation médicale à faire).

## Leçons rédigées
| Code | Leçon | Images .gif | Sources principales |
|---|---|---|---|
| K92 | Hémorragies digestives | 3 (Commons) | ESGE 2021, ESGE 2022, Baveno VII, BSG 2019, FI suisses |
| K25 (couvre K26, K27) | Ulcère gastroduodénal | 4 (Commons) | SSI H. pylori 2026, S2k DGVS 2023, ESGE 2021, WSES 2020, FI Nexium® et Pylera® |
| K21 (traite aussi K22.7 Barrett) | Reflux gastro-œsophagien et œsophage de Barrett | 4 (Commons) | S2k DGVS 2023, Lyon 2.0 (2024), ESGE Barrett 2023, FI Nexium®, Pantozol®, Gaviscon® |

## Amendements du propriétaire appliqués (09.10.2026)
- Règle linguistique : connecteurs et transitions (`liaisons.py`, plans `chapitres/K92_liaisons.py`, `K25_liaisons.py` ; rédaction native dès K21).
- Règle de précision et d’interactivité : termes interactifs systématiques (`C.termes`, `liaisons.termes`) ; K92 36 → 54 fenêtres, K25 29 → 51, K21 41.
- Règle d’image : schémas générés supprimés (K92 Forrest, K25 profondeur, K21 Los Angeles) et remplacés par des images réelles Commons ; `Schema` désactivé dans `images.py`.

## Restantes (ordre des codes prioritaires du registre)
K85, K80, K74, K70, K50, K51, K52, C18, K35, K57, K56, K90, K58 ; puis les autres catégories de `nosology/fragments/S03.json`.

## Points ouverts
- K25 : divergence FI suisses (trithérapie 7 j, IPP 20 mg 2×/j ; Pylera® 10 j) vs SSI 2026 (IPP 40 mg 2×/j, 14 j) : signalée dans le cours, à valider par l’audit.
- K21 : grade B de Los Angeles concluant (Lyon 2.0) vs non concluant (S2k 2023) ; chimioprévention IPP du Barrett (ESGE 2023 oui, S2k non) ; aucune spécialité orale d’anti-H2 trouvée dans AmiKo : signalés dans le cours.
- `preview/lesson-core.js` absent : erreur JS préexistante des aperçus (aussi sur J40), hors périmètre G-04.
