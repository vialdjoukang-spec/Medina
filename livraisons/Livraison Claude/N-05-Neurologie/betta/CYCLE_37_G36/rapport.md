# Rapport de rédaction — G36 Autres affections démyélinisantes aiguës disséminées (N-05-Neurologie)

Cycle Betta 37, leçon 2, agent C37-A1-NEUR (rédaction Sonnet 5.5). État au 15.10.2026.

## Fichiers livrés (octets)
- chapters/G36/G36_a.html 26 890 (onglet Pathologie, îlots 0 à 6)
- chapters/G36/G36_b.html 24 960 (îlots 7 à 13 : diagnostic, urgences, traitements, suivi, situations particulières, critères et paramètres clés)
- chapters/G36/G36_c.html 29 228 (onglet Examens : 6 îlots, 4 quiz de cas ; onglet Sciences : anatomie, physiologie, histologie, biochimie)
- chapters/G36/G36_d.html 12 518 (onglet Pharmacologie : 4 îlots)
- chapters/G36/G36_pop1.html 21 528 et G36_pop2.html 17 657 : 47 fenêtres (dont 10 Pareto)
- glossary/g36.py 8 537 : 24 clés, ajoutées seulement si absentes des glossaires existants

## Sources utilisées
S1 à S19 de sources.json (S1 à S3 classification ; S4 et S5 NEMOS ; S6 et S7 critères et revue MOGAD ; S8 à S10 leucoencéphalite hémorragique ; S11 à S13a informations professionnelles suisses Enspryng, Uplizna, Ultomiris, Soliris ; S14 cohorte zurichoise du liquide ; S15 et S16 performance des critères MOGAD ; S17 Solu-Medrol ; S18 grossesse ; S19 non citée dans le texte, résumé seul). Aucune donnée hors dossier n'a été ajoutée.

## Contrôles effectués (auto-contrôle du cahier W)
- HTML bien formé (analyseur, aucune balise déséquilibrée), identifiants uniques et préfixés g36, 47 clés de fenêtres toutes présentes, aucune fenêtre orpheline, tous les Pareto présents et leurs îlots couverts existants.
- build_medina.py sur une copie isolée (racine temporaire, rien écrit dans chapters/ ni glossary/ du dépôt) : « G36 non couvertes: 0 ». test_preview.py : toutes les vérifications passent (affichage, fenêtre d'abréviation, fenêtres vertes, quatre onglets, mode livre) ; seule erreur restante, un module lesson-core.js absent de l'environnement, identique sur N17 (cause environnementale).
- Sha-256 (fin de livraison) : a 5bf2336b…, b a35d820d…, c 30aa63fa…, d 74cfda96…, pop1 2a2c1329…, pop2 7479742a…, g36.py 54ca8de0….

## Lacunes (héritées du dossier de recherche, non comblées)
- Aucune recommandation suisse sur la NMOSD ni sur la leucoencéphalite de Hurst ; aucune épidémiologie suisse.
- Critères MOGAD 2023 lus via revue et résumé ; texte original non lu.
- Rattachement CIM-10-GM de la MOGAD (G36.8 ou G37.8) non tranché : le cours le dit explicitement ; ADEM classique en G37.8 (G04.0 pour la forme post-vaccinale).
- Traitement symptomatique (douleur, spasticité, vessie) non couvert ; informations professionnelles suisses non lues pour rituximab, tocilizumab, azathioprine, mycophénolate ; mécanisme de l'inébilizumab non extrait ; effets indésirables détaillés des informations professionnelles non extraits.
- Anatomie et histologie : seule la topographie lésionnelle et l'histologie de la leucoencéphalite hémorragique figurent au dossier ; le trajet anatomique complet des voies et l'histologie fine de la NMOSD ne sont pas traités. Le cours le signale.
- Volume : monographie plus courte que N17 et D50 (141 ko contre environ 400 ko), en raison de la limite stricte « aucune donnée absente du dossier ».

Audit différé — revue IA, distincte d'une validation médicale humaine.
