# Rapport de rédaction — G60 Neuropathie héréditaire et idiopathique (N-05-Neurologie)

Cycle Betta 38, leçon 2, agent C38-A3-NEUR (rédaction Sonnet 5.5). Source unique : `recherche.md` et `sources.json` du même dossier (S1–S26). Aucune donnée hors dossier.

## Fichiers (octets)
| Fichier | Contenu | Taille |
|---|---|---|
| chapters/G60/G60_a.html | en-tête, quatre onglets, Pathologie îlots 0–6 | 30 466 |
| chapters/G60/G60_b.html | Pathologie îlots 7–12 (figure 1, critères formels `div.alert`, paramètres clés `div.key`) | 22 887 |
| chapters/G60/G60_c.html | Examens (e-1 à e-4) et Sciences (anatomie, histologie, physiologie, biochimie et génétique) | 18 919 |
| chapters/G60/G60_d.html | Pharmacologie (p-1 à p-4) | 11 578 |
| chapters/G60/G60_pop1.html | 31 fenêtres cliniques | 37 887 |
| chapters/G60/G60_pop2.html | 5 fenêtres pharmacologiques et 14 Pareto | 12 818 |
| glossary/g60.py | 76 entrées, conditionnelles (`if not in G`) | — |

57 fenêtres au total (43 explicatives, 14 Pareto), 6 quiz, 1 figure SVG.

## Auto-contrôle
- HTML bien formé (pile de balises vide en a–d et pop1–pop2) ; identifiants uniques, préfixés `g60-` ; toutes les clés `data-k` ont leur fenêtre, aucune fenêtre orpheline ; couvertures Pareto et sommaire résolus.
- Audit d'abréviations `build_medina.audit()` exécuté sur une copie isolée avec `glossary/g60.py` : résultat `{}` après ajout de « Charcot-Marie-Tooth », ClCr, IMAO, LCR.
- Conventions du modèle N17/D50 respectées (classes de la liste fermée, quatre onglets, Pareto par grande partie). Le dernier îlot de la Pathologie est `div.alert` puis `div.key`.
- Contentieux C1 (génétique : guide espagnol 2024/2025 retenu comme source européenne la plus récente lue) et C2 (gabapentine/duloxétine hors indication suisse) présentés dans des fenêtres liées à un mot vert.

## Lacunes (reprises du dossier de recherche)
Aucune recommandation ni texte intégral suisse (S19–S22 en résumé) ; aucune épidémiologie suisse ; remboursement OKP des tests génétiques inconnu ; DGN/AWMF et EAN non lus ; rattachement CIM de la HNPP non établi ; Morvan, Nélaton, Roussy-Lévy et HSAN non décrits cliniquement ; pronostic non chiffré ; carbamazépine et capsaïcine (informations professionnelles suisses) non lues ; HNPP fondée sur une revue chinoise et un résumé. Volume plus modeste que N17 : l'épaisseur du dossier source (résumés) limite la profondeur sans extrapolation.

Audit différé — revue IA, distincte d'une validation médicale humaine.
