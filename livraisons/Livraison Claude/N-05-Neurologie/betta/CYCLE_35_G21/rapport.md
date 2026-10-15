# Rapport de rédaction — G21 Syndrome parkinsonien secondaire (N-05-Neurologie)

Cycle Betta 35, agent C35-A4-NEUR, leçon 1. Rédaction Sonnet 5.5 sur le dossier `recherche.md` + `sources.json` (48 sources). Date : 15.10.2026.

## Fichiers (octets)
-  31349 chapters/G21/G21_a.html
-  28858 chapters/G21/G21_b.html
-  26697 chapters/G21/G21_c.html
-   9364 chapters/G21/G21_d.html
-  26540 chapters/G21/G21_pop1.html
-  15030 chapters/G21/G21_pop2.html
-   3727 glossary/g21.py
- 141565 total (hors rapport.md)
- `rapport.md`

## Contenu
- Onglet Pathologie : 15 îlots (g21-0 à g21-14), dont critères formels (`alert`) puis paramètres clés (`key`) en dernier ; 9 Pareto ; section `src` datée.
- Onglet Examens : 4 îlots (hiérarchie question-examen-statut avec référence nommée, fiches d'interprétation, tableau des configurations, 4 cas cliniques en quiz), 1 Pareto.
- Onglet Sciences : 4 sciences (Anatomie, Histologie, Physiologie, Pharmacologie moléculaire), 4 schémas SVG noir et blanc légendés, encadrés « Science → clinique », 4 Pareto.
- Onglet Pharmacologie : 5 îlots (stratégie, doses sourcées, associations dangereuses, effets indésirables et surveillance, médicaments à éviter et aide pédagogique), 1 Pareto ; monographies en fenêtres (métoclopramide, bipéridène, lévodopa, clozapine, quétiapine, dantrolène, lithium).
- 42 fenêtres (dont 15 Pareto), environ 11 900 mots, 4 quiz, 4 SVG ; glossaire `g21.py` (MDS, DaTSCAN, ElViS, STRIVE, CIM, G21.4, G25.1, Schönfeldt-Lecuona), ajouts conditionnels sans écraser l'existant.

## Sources utilisées
S1–S2 classification CIM-10-GM 2024 ; S3, S42 Revue Médicale Suisse ; S4 étude genevoise (Fleury 2018) ; S5 diapositives HUG ; S6–S11, S26, S43–S44, S49–S50 parkinsonisme médicamenteux ; S8, S32 parkinsonisme vasculaire (Rektor 2018) ; S12–S15, S34–S35, S37–S39, S41 syndrome malin ; S20–S24, S30, S33, S47–S48 toxiques et post-encéphalitique ; S16–S19, S25, S28–S29, S40, S45–S46 informations professionnelles suisses. S27 et S49 (extraits de moteur de recherche) ne sont employés qu'avec la mention « à confirmer ». Hiérarchie : la source primaire la plus récente prime ; fenêtre `g21-sources`.

## Lacunes (reprises du dossier, signalées dans le cours)
1. Aucune recommandation de la Société suisse de neurologie ni de l'Académie européenne de neurologie propre à G21.
2. Articles du Swiss Medical Forum non lus (extraits seulement) : l'affirmation « pas de diagnostic de maladie de Parkinson sous neuroleptique sans DaTSCAN jusqu'à 18 mois » est donnée comme à confirmer ; la tendance bilatérale et symétrique du parkinsonisme médicamenteux (S49) aussi.
3. Critères de la Movement Disorder Society et consensus Delphi lus en résumé seulement.
4. Pas de dose pour la bromocriptine, l'amantadine et le lorazépam dans le syndrome malin ; dantrolène hors indication suisse (Agilus® : hyperthermie maligne).
5. Aucune information professionnelle suisse pour la flunarizine et la cinnarizine (citées comme classe à risque).
6. Causes post-encéphalitiques actuelles, délai avant réintroduction d'un neuroleptique, rattachement CIM de l'hydrocéphalie à pression normale, essai de lévodopa et rééducation du parkinsonisme vasculaire : non sourcés, non inventés.
7. Unité de prévalence genevoise (183/10…) à vérifier dans le texte intégral ; signalée dans le cours.
8. Indication suisse du métoclopramide non reprise dans le dossier : le cours renvoie à la monographie.

## Auto-contrôle (cahier W)
- HTML bien formé (pile de balises vide), identifiants uniques et préfixés `g21-`, toutes les clés `data-k` ont leur `template data-pop`, aucune fenêtre orpheline, fenêtres préfixées `g21-` / `pareto-g21-`.
- `build_medina.audit` (glossaire racine fusionné avec `g21.py`) : abréviations non couvertes = 0 ; ratios Pareto calculés sans erreur.
- Aperçu navigateur non exécuté (aucune écriture hors du dossier de livraison).

Audit différé — revue IA, distincte d'une validation médicale humaine.
