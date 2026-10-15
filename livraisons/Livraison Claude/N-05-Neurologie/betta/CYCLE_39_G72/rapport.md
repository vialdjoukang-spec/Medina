# Rapport C39-A1-NEUR — G72, Autres myopathies (N-05-Neurologie)

Audit différé — revue IA, distincte d’une validation médicale humaine.

## Fichiers livrés (cycle Betta 39, leçon 2)

| Fichier | Octets | Empreinte SHA-256 (16 premiers caractères) |
|---|---|---|
| chapters/G72/G72_a.html | 29725 | ecea94c73bbd7840 |
| chapters/G72/G72_b.html | 26023 | 9caa050090a7f738 |
| chapters/G72/G72_c.html | 30131 | 7f6c7f913bda9780 |
| chapters/G72/G72_d.html | 10012 | b1baecd57d9b7c06 |
| chapters/G72/G72_pop1.html | 36425 | 45439842d5b7fff8 |
| chapters/G72/G72_pop2.html | 14881 | 57ad293c83c6fc29 |
| glossary/g72.py | 10532 | c860d1c96290c8c0 |
| recherche.md, sources.json | fournis (entrée) | — |

Total rédigé : 157729 octets (environ 15 400 mots).

## Contenu
- Monographie en quatre onglets : Pathologie (îlots 0 à 12, références, dernier îlot = critères formels `alert` puis paramètres clés `key`), Examens (e-1 à e-5), Sciences (Anatomie, Histologie, Physiologie, Biochimie et génétique), Pharmacologie (p-1 à p-4). Plan monographique par mécanisme, sans îlot ni tableau consacré au code CIM (les sous-codes G72.0 à G72.9 sont cités dans le texte et dans la fenêtre `g72-cim`).
- 55 fenêtres (40 explicatives dont 8 monographies de médicaments, 15 Pareto), 6 quiz de cas (2 dans l’onglet Pathologie, 4 dans l’onglet Examens), 4 figures SVG noir et blanc légendées, 12 tableaux.
- Glossaire `glossary/g72.py` : 45 entrées conditionnelles (codes, gènes, essais, sociétés savantes, noms propres non développables signalés honnêtement).

## Sources utilisées
Uniquement celles de `sources.json` (S1 à S25 ; S22 non exploitée) : CIM-10-GM 2024 (BfArM), Praxis (Schubert 2023, Hunziker 2022, Giezendanner 2024, Bosma 2026), Rodriguez 2022 (Inselspital), Latronico 2023 et 2011, Piva 2019, consensus de la Société européenne d’athérosclérose 2015, Statland 2018, Allenbach 2020, Pasnoor 2018, Le Quang 2024, Solé 2026, Simon 2017, Gente 2026, Lundberg 2017 (EULAR/ACR), Lilleker 2024 (résumé), et deux informations professionnelles Swissmedic via AmiKo (Atorvastatin-Mepha, Diamox).
Notions de base non sourcées, signalées « notion de base » dans le texte : cible enzymatique des statines (HMG-CoA réductase) et voie du mévalonate, échelle 0–5 du score du Medical Research Council, hyperpolarisation de la fibre normale quand le potassium extracellulaire baisse. Aucun chiffre n’est tiré de ces notions.

## Lacunes reprises du dossier et traitées honnêtement
- Aucune recommandation de la Société suisse de neurologie ni de la DGN ; aucune donnée d’incidence suisse (dit dans l’îlot 2).
- Recommandation ESMO 2022, critères ENMC 2016 et 2024 non lus : aucune dose ni conduite chiffrée de la myosite sous inhibiteur de point de contrôle ; aucune dose d’immunoglobulines ou de rituximab.
- Codage de la myosite à inclusions, de la myopathie nécrosante et de la myosite sous inhibiteur entre G72.4 et M33/M60 non vérifié (dit dans l’îlot 1 et la fenêtre `g72-cim`).
- Colchicine, chloroquine, zidovudine et toxiques non médicamenteux de G72.2 : mentionnés sans développement.
- Paralysie périodique thyrotoxique, dichlorphénamide, posologie de l’atorvastatine, intervalles de référence suisses de la créatine kinase : non lus (dit dans le texte).
- Acétazolamide : hors étiquette en Suisse (information professionnelle Diamox) ; contradiction avec la contre-indication « hypokaliémie » signalée dans l’îlot p-3.

## Contrôles
- HTML bien formé (pile de balises vide), identifiants uniques et préfixés `g72-`, 55 clés `data-k` toutes définies, aucune fenêtre orpheline, couvertures de Pareto valides.
- Build `build_medina.py G72` sur copie temporaire (hors dépôt) : « G72 non couvertes: 0 », aucune erreur Pareto.
- `test_preview.py` non exécutable : l’actif `lesson-core.js` est absent du dépôt (échec indépendant du cours). Aucune injection, aucun git, aucun fichier hors du dossier de livraison.
