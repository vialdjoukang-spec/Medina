# Rapport de rédaction — E01, Affections thyroïdiennes et apparentées liées à une carence en iode (E-06-Endocrinologie et métabolisme)

Cycle Betta 31, leçon 2. Agent de rédaction C31-A2-ENDO (Sonnet 5.5). Date : 14.10.2026. Audit différé — revue IA, distincte d'une validation médicale humaine.

## Fichiers (sous livraisons/Livraison Claude/E-06-Endocrinologie et métabolisme/betta/CYCLE_31_E01/)
- chapters/E01/E01_a.html : 28851 octets
- chapters/E01/E01_b.html : 27889 octets
- chapters/E01/E01_c.html : 23605 octets
- chapters/E01/E01_d.html : 7857 octets
- chapters/E01/E01_pop1.html : 17742 octets
- chapters/E01/E01_pop2.html : 21580 octets
- glossary/e01.py : 5163 octets
- total : 132687 octets

Mots (texte visible, HTML) : 13981. Fenêtres : 52 dont 11 Pareto. Quiz : 4. Figures SVG : 2. Tableaux : 15. Sciences : Anatomie, Physiologie, Biochimie, Santé publique.

## Sources utilisées
Uniquement le dossier recherche.md et sources.json (28 sources : OFS CIM-10-GM 2024, OMS 2007, ETA 2023/2021/2017, OSAV, étude nationale suisse 2020-2022, informations professionnelles suisses Euthyrox et iodure de potassium, études PubMed). Aucune donnée extérieure au dossier. Les chiffres des vignettes et quiz sont pédagogiques et désignés « fictifs » ; l'ordre de grandeur « 120 000 à 300 000 fois » est un calcul de 18-45 g contre 150 µg.

## Lacunes (reprises du dossier, affichées dans la leçon)
1. Aucune recommandation suisse de société savante sur le goitre ; conduite fondée sur ETA 2023, 2021, 2017 (européennes).
2. Pas de dose suisse d'iode en grossesse (OSAV) ; référence chiffrée OMS 250 µg/jour.
3. Nodulogenèse moléculaire : résumé seul ; non détaillée.
4. Information professionnelle des antithyroïdiens et du perchlorate non lue : doses citées comme ETA 2021, sans posologie Swissmedic.
5. Modalités suisses de l'iode radioactif non lues.
6. Pas de prévalence récente du goitre de l'adulte suisse.
7. Sélénium et tabac : association seulement, non quantifiée.
8. E01.8 chez l'adulte : pas de série clinique ; mécanisme décrit seulement.

## Auto-contrôle du cahier W
- Audit des abréviations (build_medina.audit) : {} (aucune non couverte) ; glossaire glossary/e01.py (ETA, EU-TIRADS, UNICEF, ICCIDD, LISA, TRH, OSAV, BLV, Jod-Basedow, Wolff-Chaikoff, E01.0 à E01.8), ajouts conditionnels.
- Clés de fenêtres : toutes les data-k ont leur template, aucune fenêtre orpheline ; ids uniques et préfixés e01 ; balises équilibrées.
- Classes : liste fermée du modèle N17/D50 uniquement. Quatre onglets ; dernier îlot de la pathologie = div.alert (critères) puis div.key (paramètres) ; Pareto en fin de chaque grande partie ; conflit lévothyroxine (information professionnelle contre ETA 2023) présenté en fenêtre avec arbitrage « source la plus récente ».
- Construction d'essai hors dépôt racine : build sans erreur ; test navigateur sans erreur propre à E01 (seule erreur : module lesson-core.js absent du dossier d'aperçu, identique pour D50).
- Non touché : chapters/ racine, glossary/ racine, chapters.json, git.
