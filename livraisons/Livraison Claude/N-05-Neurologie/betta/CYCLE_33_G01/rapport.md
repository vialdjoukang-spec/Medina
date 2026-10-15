# Rapport de rédaction G01 — cycle Betta 33, leçon 1 (agent C33-A4-NEUR, Sonnet 5.5)

Audit différé — revue IA, distincte d'une validation médicale humaine.

## Fichiers (sous `livraisons/Livraison Claude/N-05-Neurologie/betta/CYCLE_33_G01/`)
| Fichier | Octets |
|---|---|
| chapters/G01/G01_a.html (en-tête, onglet Pathologie, îlots 0–6) | 27 178 |
| chapters/G01/G01_b.html (îlots 7–12, références) | 28 442 |
| chapters/G01/G01_c.html (Examens e-1 à e-8 ; Sciences : 5 disciplines) | 28 565 |
| chapters/G01/G01_d.html (Pharmacologie p-1 à p-5) | 12 389 |
| chapters/G01/G01_pop1.html (fenêtres cliniques) | 38 133 |
| chapters/G01/G01_pop2.html (fenêtres examens, pharmacologie, Pareto) | 25 119 |
| glossary/g01.py | 4 599 |

Contenu : environ 15 800 mots, 63 fenêtres (dont 13 Pareto), 6 quiz de cas, 6 figures SVG, 4 onglets.

## Sources utilisées
Les 25 sources du dossier (S1–S26, sans S4) : classification (S1, S2), recommandation allemande, autrichienne et suisse sur la méningite (S3), Cochrane (S5), physiopathologie (S6), OFSP et fiche cantonale sur le méningocoque (S7–S9), cohortes de listériose (S10, S11), listériose OFSP (S12), neurosyphilis (S13), IST OFSP (S14), neuroborréliose (S15–S17, S26), tuberculose (S18–S20), informations professionnelles suisses (S21 ceftriaxone, S22 dexaméthasone, S23 amoxicilline, S24 pénicilline G, S25 doxycycline). Chaque paragraphe porte l'attribut `data-src` listant ses sources.

## Contrôles (auto-contrôle du cahier W)
- HTML bien formé (pile de balises vide, chapitre et fenêtres) ; identifiants uniques et préfixés `g01-` ; aucune classe hors liste fermée.
- 60 clés `data-k` toutes résolues par un `template data-pop` ; aucune fenêtre orpheline ; clés préfixées `g01-` / `pareto-g01-` ; `data-cover` valides.
- Build dans une racine temporaire (`MEDINA_ROOT`) : `G01 non couvertes: 0`. Contrôle navigateur (copie locale de `test_preview.py`, erreur d'environnement `lesson-core.js` filtrée, identique pour N17) : OK (affichage, fenêtres, 4 onglets, mode livre).
- Abréviations : 11 nouvelles entrées lettre à lettre dans `glossary/g01.py` (MONALISA, CXCL13, FTA-ABS, FTA, ITpA, TPLA, TLR2, TLR4, Nod2, MenQuadfi, pCO2) ; aucune entrée existante écrasée.
- Aucun fichier modifié hors du dossier de livraison (ni chapters/ racine, ni glossary/ racine, ni chapters.json, ni git).

## Lacunes et limites (héritées du dossier de recherche)
1. Recommandation ESCMID 2016 inaccessible ; aucune recommandation européenne récente ni article du Swiss Medical Forum sur la méningite bactérienne.
2. Ampicilline : aucune information professionnelle suisse ; amoxicilline i.v. (S23) utilisée comme substitut, **inférence à valider** (signalée dans le texte).
3. Arrêt de la dexaméthasone en neurolistériose : déduction de S10, à valider.
4. Typhoïde, salmonellose non typhique, leptospirose, gonocoque, charbon, syphilis congénitale : aucune source lue ; décrits uniquement comme causes citées par la classification (fenêtre `g01-rares`).
5. Méningite tuberculeuse : recommandation britannique de 2009 lue au résumé ; doses antituberculeuses (mg/kg) non rapportées ; Bulletin OFSP 4/25 lu via la fiche cantonale (S9) ; délais légaux de déclaration non lus.
6. Valeurs normales du liquide cérébro-spinal, procalcitonine (seuil), posologie de l'aciclovir, vancomycine, méropénème : absentes du dossier, donc non rapportées.
7. Épidémiologie suisse de la neuroborréliose et de la neurosyphilis : non disponible.
8. Éléments non issus du dossier, marqués comme tels dans le texte : rappel anatomique non chiffré (enveloppes méningées), mécanismes pharmacologiques généraux des fenêtres ceftriaxone et dexaméthasone, explication didactique des quatre symptômes cardinaux, valeurs de la vignette (fictives). Les 12 sources lues au seul résumé limitent le niveau de preuve des affirmations correspondantes.
