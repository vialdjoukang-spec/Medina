# Rapport de rédaction — C32-A4-HEM, D73 Maladies de la rate (H-08-Hématologie)

Cycle Betta 32, leçon 1. Rédaction Sonnet 5.5 d'après `recherche.md` et `sources.json` (31 sources lues). Aucune donnée extérieure au dossier n'a été utilisée.

## Fichiers
- `chapters/D73/D73_a.html` (onglet Pathologie, îlots 0 à 6), `D73_b.html` (îlots 7 à 12, critères formels, paramètres clés, références), `D73_c.html` (Examens e-1 à e-3, Sciences : Anatomie, Histologie, Physiologie, Immunologie), `D73_d.html` (Pharmacologie p-1 à p-4).
- `chapters/D73/D73_pop1.html`, `D73_pop2.html` : 52 fenêtres (34 explicatives et monographies, 18 Pareto).
- `glossary/d73.py` : 21 entrées conditionnelles (OPSI, HbS, PPV23, MenACWY, MenB, BSH, CT, anti-GPIIb-IIIa, noms propres, codes CIM).
- Environ 13 300 mots, 6 quiz de cas (4 en Examens, 2 en Pharmacologie), 5 figures SVG noir et blanc, 4 monographies de produits suisses.

## Sous-codes couverts
D73.0 à D73.5, D73.8 et D73.9, plus les exclusions (Q89.00, Q89.01, R16.1, S36.04). Plan en trois axes : déficit de fonction, excès ou congestion, lésion focale.

## Auto-contrôle du cahier W
- HTML bien formé (analyse de balises : 0 erreur), identifiants uniques et préfixés `d73-`, 0 clé de fenêtre orpheline ou sans fenêtre, 0 clé non préfixée, identifiants de Pareto tous résolus.
- `build_medina.audit()` appliqué aux six fichiers avec le glossaire D73 : 0 abréviation non couverte.
- Quatre onglets, dernier îlot de la pathologie = critères formels (`div.alert`) puis paramètres clés (`div.key`), Pareto en fin de chaque partie.
- Non exécuté : `build_medina.py` / `test_preview.py` sur chapters/ racine (interdit par la mission : racine, chapters.json et git intacts).

## Sources utilisées
Toutes celles du dossier : BfArM CIM-10-GM 2024, OFSP/SSI/CFV 2015, protocole CHUV V6 (22.07.2026) et V5, de Porto 2010, Di Sabatino 2011 (résumé), BSH 2024 (résumé), Lv 2016, Baveno VII, Curovic Rotbain 2017, Ferraioli 2009, ESC 2023 endocardite, Schattner 2015, Renzulli 2009 (Berne), Pastak 2026, Ibikunle 2024, Kaiser 2008, Caracioni 2025 (Valais), Al Blooshi 2025, Arora 2024, Minciuna 2024, Buksh 2022, Huang 2021, Talwar 2020, Al-Hyari 2022, Tan 2022 et cinq informations professionnelles Swissmedic (Augmentin, moxifloxacine Sandoz, Capvaxive, MenQuadfi, Bexsero).

## Lacunes (reprises du dossier, signalées dans le cours)
1. PDF actuels de l'OFSP (addendum méningocoques 2024, plan de vaccination 2026) inaccessibles : schémas actuels issus du protocole CHUV V6 ; texte OFSP 2015 lu sur un miroir tiers.
2. BSH 2024 et Di Sabatino 2011 : résumés seuls.
3. Aucune source européenne lue sur : thrombose de la veine splénique et hypertension portale segmentaire, anticoagulation de l'infarctus splénique, seuils de taille des kystes, D73.8 (périsplénite, splénite), grossesse, sports de contact avec splénomégalie.
4. Bexsero : schéma adulte et adolescent de l'information professionnelle non cité ; l'intervalle de 2 mois du CHUV fait foi.
5. Prise en charge hospitalière détaillée de l'OPSI non décrite dans les sources : le cours n'en donne que le principe (urgence décidée sur la fièvre).
6. Technique de palpation et de percussion de la rate : absente des sources, donc non reproduite.
7. Mécanisme, effets indésirables et interactions des cinq médicaments : non extraits ; renvoi à l'information professionnelle complète.
8. Sources d'appoint non européennes (Lv, Ibikunle, Schattner, Arora) utilisées pour la physiopathologie et l'ordre de grandeur, jamais pour fonder une conduite.

Audit différé — revue IA, distincte d'une validation médicale humaine.
