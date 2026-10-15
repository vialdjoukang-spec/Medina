# Rapport de rédaction G71 — cycle Betta 39, leçon 1 (agent C39-A1-NEUR, Sonnet 5.5)

Audit différé — revue IA, distincte d'une validation médicale humaine.

## Fichiers (sous `livraisons/Livraison Claude/N-05-Neurologie/betta/CYCLE_39_G71/`)
| Fichier | Octets |
|---|---|
| chapters/G71/G71_a.html | 31 805 |
| chapters/G71/G71_b.html | 30 486 |
| chapters/G71/G71_c.html | 28 353 |
| chapters/G71/G71_d.html | 10 547 |
| chapters/G71/G71_pop1.html | 44 091 |
| chapters/G71/G71_pop2.html | 28 318 |
| glossary/g71.py | 12 280 |

Contenu : environ 17 560 mots, 72 fenêtres (dont 20 Pareto), 7 quiz de cas, 6 figures SVG, 4 onglets (Pathologie îlots 0–12, Examens e-1 à e-7, Sciences : Anatomie, Histologie, Physiologie, Biochimie, Génétique, Pharmacologie p-1 à p-5).

## Sources utilisées
37 des 38 sources du dossier sont mobilisées (S8, cardiologues américains, volontairement écartée comme fondement) par l'attribut `data-src` de chaque paragraphe, tableau, encadré et quiz ; les fenêtres citent leurs références en pied (`p.src`). Pivot : classification CIM-10-GM 2024 (S1, S2), consensus Duchenne parties 1 et 2 (S3, S4), information professionnelle suisse AGAMREE (S5), consensus DM1 (S6, S7), EFNS hyperCKémie (S9), Cochrane myotonie (S19), consensus MELAS (S23), cohortes Becker, FSHD et mitochondriale (S16, S24, S32), EMHG (S28). Source suisse effectivement lue : S5 uniquement.

## Contrôles (auto-contrôle du cahier W)
- HTML bien formé (pile de balises vide, chapitre et fenêtres) ; identifiants uniques et préfixés `g71-` ; aucune classe hors liste fermée ; aucun paragraphe sans `data-src`.
- Toutes les clés `data-k` résolues par un `template data-pop` ; aucune fenêtre orpheline ; clés préfixées `g71-` / `pareto-g71-` ; `data-cover` valides.
- Build dans une racine temporaire (`MEDINA_ROOT`, N17 + G71) : `G71 non couvertes: 0` (audit des abréviations de `build_medina.audit()` vide). Contrôle navigateur `test_preview.py` : seule l'erreur d'environnement `lesson-core.js` (module absent de la racine temporaire, identique pour N17 et G01) ; affichage, fenêtres et onglets sans autre erreur.
- Abréviations : 53 entrées lettre à lettre dans `glossary/g71.py` (DMD, DM1, DM2, CK, hyperCKémie, SpO2, MELAS, FSHD, DUX4, MLPA, CGH-array, EMG, OEPC, NSAA, LGMD, ENMC, EFNS, EMHG, ERN, EURO-NMD, ACMG, NHLBI, gènes, codes G71.x, etc.) ; entrées conditionnelles, aucune entrée existante écrasée. Pour les noms propres, noms commerciaux et désignations de locus sans développement dans le dossier (AGAMREE, EPIDYS, D4Z4, éponymes), l'entrée le dit explicitement.
- Aucun fichier modifié hors du dossier de livraison (ni chapters/ racine, ni glossary/ racine, ni chapters.json, ni git).

## Lacunes et limites (héritées du dossier de recherche)
1. Aucune recommandation suisse lue (Swiss Medical Forum, société suisse de neurologie, centres neuromusculaires, registre) ; épidémiologie suisse absente. Les consensus DMD (2018) et DM1 (2018) sont internationaux à forte participation américaine ; S8, S14, S15, S22, S24 (nord-américaines) ne servent que de données descriptives.
2. Tableau ESC 2022 sur les maladies neuromusculaires non extrait ; ESC 2021 de stimulation cardiaque non lues ; nomenclature LGMD (ENMC 2017) et guide EMHG 2024 non lus.
3. Statut suisse de givinostat, mexilétine, déflazacort, ataluren, exon-skipping et thérapie génique non trouvé dans l'AIPS ; le texte ne les présente pas comme autorisés. Statut européen de l'ataluren non vérifié. Posologies de mexilétine, lamotrigine, modafinil, givinostat non rapportées.
4. Myopathies congénitales, myotonies non dystrophiques, paramyotonie, neuromyotonie, dystrophie oculopharyngée, Emery-Dreifuss, dystrophies distales, DM2 et DM1 congénitale : couverture partielle ; aucune conduite détaillée avancée.
5. Lien RYR1–hyperthermie maligne non énoncé explicitement dans les textes lus (signalé dans la fenêtre dédiée) ; transmission de la FSHD, de la DM2 et héritabilité mitochondriale non lues (indiquées « non précisée dans les textes lus »).
6. Éléments non issus du dossier, marqués comme tels : vignettes cliniques fictives (valeurs pédagogiques), glose lexicale de « signe de Gowers » et de « myotonie de préhension », schémas SVG qualitatifs (capacité vitale forcée sans valeurs, topographies), aide mémoire pédagogique non officiel. Intervalles de référence de la CK et des explorations respiratoires non rapportés.
7. Seuls les abstracts de nombreuses sources ont été lus (voir sources.json) ; le niveau de preuve des affirmations correspondantes est limité.
