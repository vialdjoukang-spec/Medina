# Rapport de rédaction — G96 (N-05-Neurologie) — Cycle Betta 41, leçon 1

Agent C41-A1-NEUR (rédaction, Sonnet 5.5), 15.10.2026. Mention : **Audit différé — revue IA, distincte d'une validation médicale humaine.**

## Fichiers (sous ce dossier)
- `chapters/G96/G96_a.html` : 19958 octets
- `chapters/G96/G96_b.html` : 19579 octets
- `chapters/G96/G96_c.html` : 18271 octets
- `chapters/G96/G96_d.html` : 7192 octets
- `chapters/G96/G96_pop1.html` : 17844 octets
- `chapters/G96/G96_pop2.html` : 5441 octets
- `glossary/g96.py` : 4434 octets
- `total` : 92719 octets

## Contenu
- Quatre onglets : Pathologie (13 îlots, 0 à 12, dernier îlot = critères formels `div.alert` puis paramètres clés `div.key`), Examens (6 îlots), Sciences (anatomie, physiologie, biochimie et imagerie, 2 figures SVG), Pharmacologie (4 îlots).
- 37 fenêtres : 25 fenêtres de contenu (dont un moyen mnémotechnique marqué « aide pédagogique, non critère officiel ») et 12 Pareto. 6 quiz. Environ 9 500 mots.
- Axe : G96.0 sous deux volets (fuite spinale / hypotension intracrânienne spontanée ; rhinorrhée de liquide céphalorachidien). Aucun îlot ni tableau consacré au code CIM ; G96.1, G96.8, G96.9 signalés comme sans contenu clinique dans les sources.
- Sources utilisées : S1 à S17 du dossier (`sources.json`) ; rattachement par attribut `data-src` et par mention dans le texte.

## Auto-contrôle (cahier W)
- HTML bien formé (balises équilibrées), identifiants uniques et préfixés `g96-`, aucune clé de fenêtre manquante ni inutilisée, tous les `data-cover` des Pareto existent.
- Essai de construction dans une copie isolée de `build_medina.py` : `G96 non couvertes: 0`. Test navigateur non lancé.
- Glossaire : 9 entrées conditionnelles (ajoutées seulement si la clé est absente des glossaires existants ; IRM, FLAIR, T1, T2 et CIM-10-GM existaient déjà).

## Lacunes (reprises du dossier de recherche)
1. Aucune recommandation suisse (Société suisse de neurologie, Swiss Medical Forum) ni européenne dédiée (EAN) : base = consensus britannique 2023, revues de Fribourg, études de l'Inselspital Berne (résumés).
2. G96.1, G96.8, G96.9 : aucune source clinique.
3. Critères ICHD-3 7.2.1 et 7.2.2 non lus.
4. Informations professionnelles suisses de la caféine, du paracétamol et des anti-inflammatoires non stéroïdiens non lues : doses de caféine issues de la revue de Fribourg.
5. Grossesse et pédiatrie non couvertes (dit explicitement dans le cours).
6. Risque de méningite (10 à 37 %) issu d'un seul résumé ; sidérose superficielle 1,5 % contre 5 à 10 % selon les sources, présentée comme divergence.
7. Techniques du signe du halo et justification physique des séquences d'IRM absentes des sources : signalées comme telles, non inventées.
8. Le pourcentage de hausse du volume ventriculaire (18,8 %) est repris des auteurs ; il diffère du calcul sur les moyennes (15,3 à 18,0 mL).
