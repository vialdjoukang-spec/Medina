# Rapport de rédaction — G26 (N-05-Neurologie), cycle Betta 36, agent C36-A4-NEUR

Audit différé — revue IA, distincte d'une validation médicale humaine.

## Fichiers livrés
| Fichier | Octets | SHA-256 (16 premiers) |
|---|---|---|
| chapters/G26/G26_a.html | 22380 | 7bcb08b755dabba0 |
| chapters/G26/G26_b.html | 19500 | b0aa79fc049affe3 |
| chapters/G26/G26_c.html | 20251 | 8bd91acde7e20970 |
| chapters/G26/G26_d.html | 8970 | 8246043032bd1e46 |
| chapters/G26/G26_pop1.html | 20307 | 98c65df4a1da491f |
| chapters/G26/G26_pop2.html | 11544 | 9844392a89dc38de |
| glossary/g26.py | 7155 | 06fcba4b03f1ccf0 |

## Contenu
- Monographie G26 en quatre onglets : Pathologie (14 îlots, vignette fictive, 2 figures, 3 cas à choix, critères formels puis paramètres clés), Examens (5 îlots), Sciences (anatomie, histologie, physiologie, biochimie), Pharmacologie (4 îlots).
- 41 fenêtres explicatives (29 cliniques et pharmacologiques, 12 Pareto), 271 repères d'évidence `data-evidence`, rattachés aux sources S1 à S18 par `data-src`.
- Glossaire : 20 entrées conditionnelles (`glossary/g26.py`), aucune mutation des glossaires existants.

## Auto-contrôle du cahier W
- HTML bien formé (analyse de balises sur a+b+c+d, pop1, pop2) : aucune balise non fermée.
- Identifiants uniques et préfixés `g26-` ; toutes les clés `data-k` ont une fenêtre, aucune fenêtre orpheline ; couvertures Pareto toutes résolues.
- `build_medina.audit()` sur l'ensemble avec le glossaire G26 fusionné : `{}`.
- Aucun fichier hors du dossier du cycle n'a été modifié ; aucun git.

## Sources utilisées
S1 à S18 du dossier `sources.json` (S19, page grand public, non utilisée). EASL-ERN 2025 (S5) uniquement par son résumé.

## Lacunes et points d'attention
1. Paires † / G26* officielles non lues ; frontière G22* / G26* déduite de la structure du bloc ; codage des chorées médicamenteuses non vérifié.
2. Aucune source suisse primaire spécifique ni épidémiologie suisse ; la seule attache suisse est l'approbation SNG de la directive chorée, la coordination suisse de la directive Wilson et les informations professionnelles Swissmedic.
3. Striatopathie diabétique, hyperthyroïdie, DHCA : séries de cas et résumés ; aucune recommandation européenne ; formes réfractaires sans conduite.
4. Chorée lupique et syndrome des antiphospholipides : traitement non lu, donc non écrit. Zinc et D-pénicillamine : informations professionnelles suisses non lues ; posologies reprises de la directive allemande.
5. Les médicaments antichoréiques sont présentés comme hors indication suisse dans une chorée secondaire (déduction des trois informations professionnelles).
6. Sciences fondamentales : le dossier ne contient aucune description du circuit des noyaux gris ; seules les structures citées par les sources sont retenues. Rédigé sans détail anatomique ou histologique hors dossier.
7. Ajout du rédacteur hors dossier : conversion mg/dl vers mmol/L (division par 18, fenêtre `g26-unites`), signalée comme calcul arithmétique à confirmer.
8. Valeurs de la vignette : fictives (moyennes des séries publiées), signalées comme telles.
