# Rapport C38-A4-NEUR — G63, Polynévrite au cours de maladies classées ailleurs (N-05-Neurologie)

Audit différé — revue IA, distincte d’une validation médicale humaine.

## Fichiers livrés (cycle Betta 38, leçon 1)

| Fichier | Octets | Empreinte SHA-256 (16 premiers caractères) |
|---|---|---|
| chapters/G63/G63_a.html | 25980 | 82947f41b70256a0 |
| chapters/G63/G63_b.html | 32009 | 0764b4e3f495f377 |
| chapters/G63/G63_c.html | 33882 | 1721d42e03ee2466 |
| chapters/G63/G63_d.html | 12085 | 9455938e0c123895 |
| chapters/G63/G63_pop1.html | 24197 | 72f33f6f6bebb818 |
| chapters/G63/G63_pop2.html | 23131 | d86e6392e8a33720 |
| glossary/g63.py | 11669 | 6ee9cabc547337e2 |
| recherche.md, sources.json | fournis (entrée) | — |

Total rédigé : 162953 octets.

## Contenu
- Monographie en quatre onglets : Pathologie (îlots 0 à 12, références, dernier îlot = critères formels `alert` puis paramètres clés `key`), Examens (e-1 à e-5), Sciences (Anatomie, Histologie, Physiologie, Biochimie et génétique), Pharmacologie (p-1 à p-4).
- 49 fenêtres (35 explicatives, 14 Pareto), 7 quiz de cas (2 dans l’onglet Pathologie, 5 dans l’onglet Examens), 6 figures SVG noir et blanc légendées, environ 16 700 mots au total.
- Glossaire `glossary/g63.py` : entrées conditionnelles (codes G63.x et G62.0, anticorps, gènes, sociétés savantes, formes juridiques, kJ, noms propres non développables signalés honnêtement).

## Sources utilisées
Uniquement celles de `sources.json` (S1 à S27) : CIM-10-GM 2024 (BfArM) et libellés OFS, Sommer 2018, Feldman 2019, trois documents SGED/QualiCCare (2013-2014, 2016, 2023), Julian 2019, de Greef 2018, Graus 2021, Adams 2016 (ATTReuNET), Arnold 2016, Finnerup 2015, Tran 2015, résumés EAN/PNS 2021, PNS 2010, EFNS 2010 (douleur et Lyme), et sept informations professionnelles Swissmedic lues via AmiKo (prégabaline, gabapentine, duloxétine, amitriptyline, Qutenza, hydroxocobalamine, thiamine).

## Lacunes reprises du dossier et traitées honnêtement
- Aucune recommandation de la Société suisse de neurologie ni article du Swiss Medical Forum ; aucune donnée suisse d’épidémiologie (dit dans l’îlot 2) ; Blanquet et Humm 2025 connu par son résumé.
- ESMO-EONS-EANO 2020 non lue : aucune prévention ni traitement de la neuropathie de la chimiothérapie n’est rédigé ; rattachement G62.0 / G63.1 non vérifié (signalé dans l’îlot 1, la fenêtre de la neuropathie anticancéreuse et le glossaire).
- EAN/PNS 2021, PNS 2010, EFNS 2010, NeuPSIG 2015, EFNS Lyme : résumés seulement (signalé dans les fenêtres).
- G63.0 hors Lyme, G63.3 hors amylose à transthyrétine, G63.6 : aucune source clinique lue (dit dans l’îlot 4 et la pharmacologie). Amylose à transthyrétine : consensus de 2016, thérapies actuelles non vérifiées.
- Sciences fondamentales limitées aux données du dossier : aucun trajet nerveux, aucune histologie du nerf normal (dit dans les fenêtres et les îlots de sciences).
- Point à vérifier lors de l’audit : la prégabaline est notée « emploi non prévu sous 30 mL/min » d’après le dossier ; relire la monographie en vigueur.
- Aucune valeur de référence chiffrée de laboratoire (vitamine B12, etc.), le dossier n’en fournissant pas.

## Auto-contrôle (cahier W)
- `build_medina.audit()` sur une copie isolée de la racine (glossaire racine + `g63.py`) : `G63 non couvertes: 0`, aucune erreur Pareto.
- HTML bien formé (pile vide), 49 fenêtres, aucune clé `data-k` sans `template data-pop`, aucune fenêtre orpheline, identifiants uniques et préfixés `g63-`.
- Contrôle navigateur `test_preview.py` non abouti dans la copie isolée (module `lesson-core.js` généré par la construction du frontend, absent de la copie) ; à relancer à l’injection.
- Aucun fichier modifié hors du dossier du cycle ; ni `chapters/` racine, ni `glossary/` racine, ni `chapters.json`, ni git.
