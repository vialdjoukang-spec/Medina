# Rapport C33-A1-NEUR — I68, Troubles cérébrovasculaires au cours de maladies classées ailleurs (N-05-Neurologie)

Audit différé — revue IA, distincte d’une validation médicale humaine.

## Fichiers livrés (cycle Betta 33, leçon 2)

| Fichier | Octets | Empreinte SHA-256 (16 premiers caractères) |
|---|---|---|
| chapters/I68/I68_a.html | 24447 | f98b254a55009d14 |
| chapters/I68/I68_b.html | 32830 | e20f68c0e7cad307 |
| chapters/I68/I68_c.html | 31357 | 585ed3a8e89feed7 |
| chapters/I68/I68_d.html | 11324 | d04f20b7cfb2ec0e |
| chapters/I68/I68_pop1.html | 20222 | 172d5d728e6c54d9 |
| chapters/I68/I68_pop2.html | 23365 | a9010e8718d591dc |
| glossary/i68.py | 5990 | db0145331f92b463 |
| recherche.md, sources.json | fournis (entrée) | — |

Total rédigé : 149535 octets.

## Contenu
- Monographie en quatre onglets : Pathologie (îlots 0 à 12, références, dernier îlot = critères formels `alert` puis paramètres clés `key`), Examens (e-1 à e-6), Sciences (Anatomie, Histologie, Physiologie, Biochimie et génétique), Pharmacologie (p-1 à p-4).
- 51 fenêtres (37 explicatives, 14 Pareto), 5 quiz de cas, 6 figures SVG noir et blanc légendées, environ 14979 mots au total.
- Glossaire `glossary/i68.py` : 15 entrées conditionnelles (ARIA, ARIA-E, ARIA-H, APOE, SWI, FTA-ABS, noms d’essais honnêtement non développés, etc.).

## Sources utilisées
Uniquement celles de `sources.json` (S1 à S25) : CIM-10-GM 2024 et OMS 2019, Revue Médicale Suisse 2023, Boston 2.0, ESO/EANS 2025, Édimbourg, recommandations DGN/IUSTI, EULAR, informations professionnelles suisses (Kisunla, Aciclovir Labatec, Pénicilline Grünenthal via AmiKo).

## Lacunes reprises du dossier et traitées honnêtement
- Aucune recommandation suisse ou ESO spécifique de l’angiopathie amyloïde ; aucune épidémiologie suisse propre à la catégorie (dit dans l’îlot 2).
- Boston 2.0 et angiopathie inflammatoire lus en résumé ou source secondaire (signalé dans les fenêtres) ; angiopathie héréditaire, entité I68.8 urémique, lécanemab, schémas antituberculeux suisses, ESCMID 2016 non couverts.
- Vasculopathie varicelle-zona : niveau de preuve faible, usage de l’aciclovir hors information professionnelle ; règle de double codage et sous-code E85 non précisés.
- Sciences fondamentales : limitées aux données du dossier (aucune histologie de l’endartérite syphilitique, aucune voie de production du peptide).
- Aucune dose de donanemab : le dossier n’en fournit pas.

## Auto-contrôle (cahier W)
- `build_medina.audit()` sur une copie isolée de la racine : `I68 non couvertes: 0`, aucune erreur Pareto.
- HTML bien formé (pile vide), identifiants uniques et préfixés `i68-`, toutes les clés `data-k` ont leur `template data-pop`, aucune fenêtre orpheline.
- Contrôle navigateur `test_preview.py` non exécuté (Chromium non vérifié dans l’environnement).
- Aucun fichier modifié hors du dossier du cycle ; ni `chapters/` racine, ni `glossary/` racine, ni `chapters.json`, ni git.
