# Rapport de rédaction C86 — Autres lymphomes à cellules T/NK spécifiés (H-08-Hématologie)

Agent C34-A3-HEM (Sonnet 5.5), cycle Betta 34, leçon 1, 15.10.2026. Base exclusive : `recherche.md` et `sources.json` du même dossier (18 sources lues et datées). Audit différé : revue IA, distincte d'une validation médicale humaine.

## Fichiers (octets)
- chapters/C86/C86_a.html 27 003 (pathologie, sections 0–6)
- chapters/C86/C86_b.html 25 650 (pathologie, sections 7–12, références)
- chapters/C86/C86_c.html 27 838 (Examens e-1 à e-5 ; Sciences : anatomie, histologie, physiologie, génétique et biochimie)
- chapters/C86/C86_d.html 10 536 (Pharmacologie p-1 à p-4)
- chapters/C86/C86_pop1.html 34 746 (17 fenêtres : entités, mécanismes, risque)
- chapters/C86/C86_pop2.html 39 189 (20 fenêtres de bilan, médicaments, statut suisse, lacunes ; 12 fenêtres Pareto)
- glossary/c86.py (abréviations ajoutées par `add` conditionnel, sans mutation des glossaires existants)

Total HTML : 164 962 octets, environ 17 600 mots, 49 fenêtres (37 explicatives, 12 Pareto), 5 quiz de cas, 4 figures SVG noir et blanc légendées. Modèle structurel : chapters/N17 et chapters/D50 (gabarit, classes, préfixes `c86-`, Pareto `pareto-c86-…`, dernier îlot de la pathologie = `div.alert` des critères formels puis `div.key` des paramètres clés).

## Sources utilisées (clés de sources.json)
BFARM-C86, OFS-GM2024, ONKO-PTCL2025, ESMO-EHA2025, WHO-HAEM5, WHO-EORTC2018, KEMPF2011, WILLEMZE2008, GAYDEN2018, MOONLA2023, TSE2022, CARVAO2019, ESSCD2019, ZANDER2021, NGUYEN2023, ADCETRIS-FI, ELZONRIS-FI, ONCASPAR-FI. Aucune donnée extérieure au dossier n'a été ajoutée ; les chiffres dérivés (12 points, 28 mois, 30 points, 19 mois, rapport 2,1 ; 0,028 %) sont des calculs signalés.

## Lacunes assumées dans le cours
1. Aucune recommandation suisse spécifique ni chiffre suisse par sous-code ; seule source suisse : SZO 2021.
2. Recommandation ESMO 2018 des lymphomes cutanés inaccessible (403) ; remplacée par OMS-EORTC 2018 et consensus 2011.
3. Traitement du SPTCL (corticoïdes, ciclosporine), panniculite lupique, critères HLH-2004, tableau clinique de l'EATL : non rédigés faute de source ; ICC 2022 non lue en texte intégral.
4. Remboursement suisse 2026 du BV-CHP non vérifié ; pégaspargase hors étiquette dans l'ENKTL (déduction à partir de l'indication LLA) ; statut suisse du pembrolizumab, du nivolumab et de la crisantaspase non lu.
5. Aucun intervalle de référence de laboratoire dans les sources : aucune valeur normale n'est affichée ; grossesse non documentée ; type C de la papulose lymphomatoïde non détaillé ; posologies du CHOP et du pégaspargase, contre-indications détaillées des informations professionnelles non reprises.
6. Sigles de schémas (DDGP, SMILE, AspaMetDex, P-GemOx, DeVIC, IVE) : développement non établi par les sources, déclaré tel dans le glossaire ; CHOEP et ICE : développement usuel, signalé.
7. Le consensus 2011 inclut un consortium américain (USCLC), utilisé pour sa composante européenne.
8. Deux explications pédagogiques sont signalées comme telles dans le texte (dépendance à l'asparagine ; effet de dose des odds ratios HAVCR2) ; elles ne sont pas des citations.

## Auto-contrôle (cahier W)
- HTML bien formé (pile de balises vide, aucune erreur) ; identifiants uniques, tous préfixés `c86-` / `pA pE pS pP`.
- Toute clé `data-k` possède sa fenêtre ; aucune fenêtre orpheline ; toute référence de glossaire pointe vers une fenêtre existante.
- Moteur `build_medina` (transform, Pareto, wrap, audit) exécuté sur les six fichiers avec le glossaire racine plus `glossary/c86.py` : abréviations non couvertes = 0 ; ratios Pareto calculés sans erreur.
- Aucun fichier de `chapters/`, `glossary/`, `chapters.json` à la racine n'a été modifié ; aucune opération git.

## Mention
Audit différé — revue IA, distincte d'une validation médicale humaine.
