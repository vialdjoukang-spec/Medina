# Auto-revue interne Claude — P-02-Pneumologie — 08.10.2026

Périmètre : 18 cours nouveaux de la zone de travail (J10, J47, J84, J90, R06, I27, J12, J93, R05, J21, J80, J96, J85, J67, J95, R04, J60, J69) et cohérence avec les 5 cours canoniques du fragment (J45, J44, J18, I26, J40). Le canonique n’a pas été modifié. Aucun commit ni push.

Cette auto-revue ne vaut ni audit croisé Codex, ni validation médicale, ni relecture exhaustive (R-10.13, R-17.7). Les affirmations non citées ci-dessous restent à contrôler par l’audit croisé.

## 1. Contrôles exécutés

Méthode : copie du dépôt (HEAD `19c6798`, sans `.git`, `dist`, `livraisons`, `espace_partage`, `_alpha_in`, `deliverables`) dans `scratchpad/p02rev`, superposition de `sources/chapters/*`, `sources/glossary/*.py`, `sources/modules/*` et des 18 entrées de `chapters_additions.json` dans `chapters.json` (champ `supersedes` retiré pour la copie).

| Commande | Résultat |
|---|---|
| `python3 test_v7.py --static` sur les 23 codes du fragment, avant corrections | OK |
| idem, après corrections | OK (un échec intermédiaire « MEDINA » non couvert dans J90, corrigé) |
| `MEDINA_OUT=<copie>/out python3 build_front.py --fragment S02` | Construit : `MEDINA_S02_respiratoire.html`, 7 542 429 octets, 3 596 886 compressés, 1 578 gabarits |
| Contrôle du glossaire embarqué S02 (BTS, PEP, PAO₂, FDA, ROX, RAPID, MIST2, J68.4, Guillain-Barré, Rendu-Osler, ESTS) | Présents, définition fusionnée unique |
| Recouvrement des `covers` (18 nouveaux + 5 canoniques) | Aucun chevauchement |
| Renvois `#/entry/` des cours nouveaux | Tous vers un cours existant (A41, I26, I27, I40, I50, J10, J18, J44, J45, J60, J80, J84, J85, J93, J96, T78) ; les renvois hors fragment (A41, I40, I50, T78) sont neutralisés par `build_front.py` dans la version fragment |
| Phrases de 12 mots ou plus clonées entre cours | Aucune (seulement des libellés de navigation et des titres de références) |

Non exécuté : `test_v7.py` navigateur (ordinateur et mobile), `tests/audit_fragments.py`, `tests/audit_sciences.py`, `verify_course_native.cjs`, contrôle visuel du fragment autonome.

## 2. Constats et corrections

Gravité : B = bloquant, M = majeur, m = mineur.

| Cours | Fichier | Problème | Gravité | Correction appliquée | Source |
|---|---|---|---|---|---|
| J21 | `J21_d.html`, `J21_pop3.html`, `J21_pop4.html` | Paracétamol sirop : plafond « 75 mg/kg par jour » attribué à l’information suisse ; la monographie donne 15 mg/kg, au plus 3 (à 4) fois par jour, soit 60 mg/kg par jour | B | Plafond ramené à 60 mg/kg par jour dans les trois fichiers | Information professionnelle suisse, compendium.ch, Dafalgan sirop 30 mg/mL enfants (`/product/1628803…/mpro`), consultée le 08.10.2026 |
| J69 | `J69_b.html`, `J69_d.html`, `J69_pop3.html`, `J69_pop4.html` | Relais oral de l’amoxicilline-acide clavulanique à « 1 g deux fois par jour », contradictoire avec J18 (canonique, SSI : 1 g toutes les 8 heures) et J85 (1 g trois fois par jour) dans la même indication pulmonaire | M | Relais harmonisé à 1 g toutes les 8 heures (schéma SSI repris dans J18), dans le cadre du maximum de 3 comprimés par jour de l’information professionnelle ; fenêtre réécrite pour distinguer schéma de l’étiquette et schéma retenu | J18 canonique (SSI) ; Information professionnelle suisse, Augmentin 1 g (citée par J69, consultée le 08.10.2026 par le rédacteur) |
| J90 | `J90_pop3.html` | Fenêtre lidocaïne : « dose maximale non vérifiée » (formule de chantier) et absence de plafond, alors que J93 fixe 3 mg/kg sans dépasser 250 mg dans le cadre suisse de 400 mg | M | Plafond aligné sur J93, avec exemple chiffré et renvoi nommé | Information professionnelle suisse Rapidocain : ≤ 400 mg en infiltration (table Swissmedic retrouvée en ligne, 08.10.2026) ; BTS 2023 (choix déjà documenté dans J93) |
| J96 | `J96_c.html` | « au-delà de 92 à 98 % » : borne incohérente avec la cible BTS 94–98 % utilisée partout ailleurs | m | « au-delà de la borne haute de 98 % » | BTS 2017, déjà cité dans J96 |
| Transversal | glossaires | 35 clés définies dans plusieurs glossaires, souvent avec des définitions divergentes ; la dernière chargée l’emportait (R-13.4, R-13.12) | M | Une seule définition conservée par clé, fusionnée et rendue exacte (tableau 3) | — |
| J80 → J96 | `glossary/j96.py` (ROX) | La définition retirée de J80 affirmait que le « X » de ROX vient de « index » ; ROX = Respiratory rate–OXygenation | m | Définition unique dans `j96.py`, avec la valeur ≥ 4,88 à 12 heures | Roca, AJRCCM 2019 |
| J21 | `glossary/j21.py` (MATISSE) | « environ 7300 femmes » ; l’essai en a randomisé 7358 | m | « environ 7400 » | Kampmann, NEJM 2023 |
| J95 | `glossary/j95.py` (MDA5) | MDA5 qualifié de « gène » ; c’est une protéine (hélicase), codée par IFIH1 | m | Définition unique dans `j84.py` (« protéine… hélicase cytoplasmique ») | — |
| J10 | `glossary/j10.py` | J10.0 en double avec le glossaire canonique `j18.py`, qui l’emporte au chargement | m | Clé retirée de `j10.py` ; seule la définition canonique subsiste | — |
| J12 | `J12_a/b/c/d.html` | 11 paragraphes ouverts par « Le lecteur… » (fabrication du cours, R-12.5) | M | « Le médecin… » | STYLE_REDACTION § 3 |
| J84, J69 | `J84_c.html`, `J69_a.html` | « piège le lecteur », « afin que le lecteur reconnaisse », « Le lecteur gagne à revoir » | m | Sujet clinique (« le médecin », « le médecin assistant ») | STYLE_REDACTION § 3 |
| J60 | `J60_c.html` | « Le lecteur » ambigu | m | « Le lecteur de radiographies » (sens ILO conservé) | — |
| J96 | `J96_b.html` | « cet îlot résume » | m | Phrase reformulée sur le contenu médical | R-12.5 |
| J95 | `J95_a.html`, `J95_b.html` | « Le §9 » dans un encadré | m | « L’îlot 9 » | — |
| J10 | `J10_b.html` (paramètres clés), `J10_d.html`, `J10_pop2.html` | Encadrés en phrases nominales et infinitif injonctif (« Incubation de… », « Grave ou hospitalisé : oseltamivir… », « Réduire la dose… ») | M | Réécrits en phrases complètes, chiffres inchangés ; mécanisme ajouté au plafond du paracétamol (glutathion) | STYLE_REDACTION § 2 |
| J69 | `J69_a.html`, `J69_d.html` | « À retenir » nominal (doses en liste, ellipse « les rayonnements par lésion de l’ADN ») | M | Réécrits en phrases complètes avec l’indication de chaque dose | STYLE_REDACTION § 2 |
| J90 | `J90_c.html` (2 encadrés) | « Plèvre pariétale sensible… », « Mésothélium unicellulaire… » | M | Phrases complètes | STYLE_REDACTION § 2 |
| J96 | `J96_b.html` | « Sédatifs arrêtés, potassium et phosphore corrigés… » | M | Phrase complète | STYLE_REDACTION § 2 |
| R05 | `R05_b.html` | « À retenir » entièrement en style télégraphique | M | Réécrit en phrases complètes, contenu inchangé | STYLE_REDACTION § 2 |
| J90 | `J90_pop3.html` | Mot « MEDINA » introduit par la correction, non couvert par le glossaire | m | « ce cours retient » | test statique |

## 3. Glossaire : clés unifiées

Chaque clé est désormais définie dans un seul glossaire de travail.

| Clé | Glossaire conservé | Retirée de |
|---|---|---|
| BTS | j90 (définition élargie : plèvre 2023, bronchiectasies 2019, macrolides 2020, oxygène 2017, toux 2023) | j47, j85, j93, j96, r05, r06 |
| CFV, HARMONIE, MATISSE, MELODY, IgG1, J98.7 | j21 | j12 (et j95 pour J98.7) |
| EFR, FDA, JRS, MDA5, MUC5B, J68.4, J70.1, J84.0, J98.2 | j84 | i27, r05, j95, j47, j21 |
| ESTS, RAPID, J94.2 | j90 | j85, j93, j95 |
| F45.33, Guillain-Barré | r06 | r05, j10, j12, j96 |
| FLCN, J95.80, S27.0, S27.2 | j93 | j95, j90 |
| FLORALI, PAO₂, ROX, R09.2 | j96 | j80, j95, r06 |
| JAK1 | j12 | j95 |
| MIST1, MIST2, J85.3, J98.50 | j85 | j90, j95 |
| PEP | j80 | j95, j96 |
| R04.2 | r04 | r05 |
| Rendu-Osler | i27 (avec critères de Curaçao) | r04 |
| J10.0 | canonique j18 | j10 |

Conséquence : les clés gardent un `ref` vers une fenêtre du cours qui les porte ; dans les autres cours, la fenêtre d’approfondissement n’apparaît pas (comportement prévu par `engine/medina_course.js`).

## 4. Cohérence chiffrée vérifiée entre cours

| Paramètre | Résultat |
|---|---|
| Cibles de SpO₂ | 94–98 %, ou 88–92 % si risque d’hypercapnie (BTS 2017) dans J12, J69, J93, J95, J96, R06 et J18/J44 ; 88–95 % propre au SDRA ventilé (ARMA) dans J80, population distincte et explicitée ; seuils de bronchiolite (NICE) propres à J21 |
| Amoxicilline-acide clavulanique | 2,2 g toutes les 8 heures par voie intraveineuse partout ; relais oral désormais 1 g toutes les 8 heures (J18, J69) ou trois fois par jour (J85) |
| Drainage pleural | pH ≤ 7,2, ou glucose < 3,3 mmol/L si le pH manque, pus = drain, dans J85 et J90 (BTS 2023) |
| Lidocaïne | 3 mg/kg sans dépasser 250 mg, cadre suisse 400 mg, dans J90 et J93 |
| Insuffisance respiratoire | PaO₂ < 8,0 kPa (60 mmHg) ; PaCO₂ > 6,0 kPa (45 mmHg) ; VNI si pH < 7,35 et PaCO₂ > 6,5 kPa, dans J96, R06, J95 |
| Dexaméthasone COVID-19, nirsévimab, oseltamivir rénal | Identiques entre J12, J80, J21, J10 et J18 |

## 5. Exactitude ciblée (affirmations à fort enjeu)

« En ligne » signifie qu’une source a été consultée pendant cette revue. « Cohérent » signifie un contrôle par connaissance de la source primaire citée, sans relecture en ligne ; ces points restent à confirmer par l’audit croisé.

| Cours | Affirmation | Statut |
|---|---|---|
| J10 | Oseltamivir : 30 mg deux fois par jour si clairance de plus de 30 à 60 mL/min, 30 mg une fois par jour de 10 à 30 | Cohérent (Tamiflu, EMA/Suisse) |
| J10 | Baloxavir 40 mg de 20 à moins de 80 kg, 80 mg dès 80 kg | Cohérent (Xofluza) |
| J10 | Vaccin à dose élevée dès 75 ans ou dès 65 ans avec un facteur de risque | Cohérent (OFSP 2024/25) |
| J47 | Azithromycine 250 mg/j ou 500 mg trois fois par semaine ; érythromycine 400 mg deux fois par jour ; gentamicine nébulisée 80 mg deux fois par jour | Cohérent (BAT, EMBRACE, BLESS, Murray 2011) |
| J84 | Nintédanib 150 mg deux fois par jour ; pirfénidone 801 mg trois fois par jour, 1 602 mg/j avec ciprofloxacine 750 mg deux fois par jour | Cohérent (Ofev, Esbriet) |
| J90 | Altéplase 10 mg + dornase 5 mg intrapleurales deux fois par jour, 3 jours ; spironolactone 100–400 mg | Cohérent (MIST2, EASL 2018) |
| J90/J85 | RAPID : mortalité à 3 mois 2,3 %, 9,2 %, 29,3 % | En ligne (Corcoran, Eur Respir J 2020;56:2000130) |
| R06 | NEWS2 : barèmes saturation et fréquence respiratoire | Cohérent (RCP 2017) |
| R06 | Paspertin : contre-indiqué avant 18 ans | **Non confirmé** en ligne (les étiquettes allemande et autrichienne fixent < 1 an) ; à relire dans la monographie suisse |
| I27 | Définition PAPm > 20 mmHg, RVP > 2 unités Wood ; sotatercept 0,3 puis 0,7 mg/kg ; riociguat jusqu’à 2,5 mg trois fois par jour si PAS ≥ 95 mmHg | Cohérent (ESC/ERS 2022, Winrevair, Adempas) |
| J12 | Nirmatrelvir-ritonavir si DFG < 30 : 300/100 mg le jour 1, puis 150/100 mg par jour | Cohérent (Paxlovid, mise à jour 2024) |
| J12 | Tocilizumab selon le poids (RECOVERY) ; SpO₂ < 90 % = forme sévère (OMS) | Cohérent |
| J93 | Lidocaïne : Swiss ≤ 400 mg en infiltration | En ligne (table Swissmedic Rapidocain) |
| J93 | Geste sûr si pneumothorax ≥ 2 cm ; pas de clampage d’un drain qui bulle | Cohérent (BTS 2023) |
| R05 | Géfapixant 45 mg deux fois par jour, 45 mg une fois par jour si DFGe < 30 | Cohérent (Lyfnua, Swissmedic 2022) |
| R05 | Amoxicilline-acide clavulanique 22,5 mg/kg deux fois par jour, 2 semaines (toux humide de l’enfant) | Cohérent (Marchant) |
| J21 | Abrysvo entre 32 et 36 semaines | En ligne (Bulletin OFSP 47/2024, infovac) |
| J21 | Seuils NICE de SpO₂ (< 90 % dès 6 semaines, < 92 % avant ou comorbidité) | Cohérent (NICE NG9) |
| J21 | Paracétamol : 75 mg/kg/j | **Erreur corrigée** (60 mg/kg/j, compendium.ch) |
| J80 | DEXA-ARDS 20 mg puis 10 mg ; cisatracurium 15 mg puis 37,5 mg/h ; décubitus ventral si P/F < 150 | Cohérent (Villar 2020, ACURASYS, PROSEVA) |
| J96 | Naloxone 0,4–2 mg ; flumazénil 0,2 mg puis 0,1 mg/min, 1 mg max | Cohérent ; monographie suisse d’Anexate non relue (déjà signalé dans le cours) |
| J96 | Ventilation à domicile si PaCO₂ > 7 kPa 2 à 4 semaines après l’exacerbation | Cohérent (HOT-HMV) |
| J85 | Métronidazole intraveineux 15 mg/kg puis 7,5 mg/kg toutes les 6 h, 3 jours, puis toutes les 12 h, max 4 g/j | En ligne (compendium.ch, Metronidazole Sintetica) |
| J85 | Clindamycine ≤ 1 200 mg par perfusion d’une heure | Cohérent (Dalacin C) |
| J67 | Lymphocytose du lavage > 30 % ; prednisone ≤ 0,5 mg/kg/j dans la forme fibrosante | Cohérent (ATS/JRS/ALAT 2020, S2k 2024) |
| J95 | Recommandation ERS/ESTS 2025 sur l’aptitude au traitement à visée curative ; VO₂ max < 12 mL/kg/min ou pente VE/VCO₂ > 40 | En ligne (Brunelli, Eur Respir J 2025;66:2500156) |
| J95 | Sugammadex 2, 4 et 16 mg/kg ; ARISCAT < 26 / 26–44 / ≥ 45 | Cohérent |
| R04 | Beriplex 25/35/50 UI/kg selon l’INR, max 5 000 UI ; idarucizumab 5 g | Cohérent |
| R04 | Acide tranexamique intraveineux : 10 mg/kg toutes les 12 h si créatinine 120–249 µmol/L | Cohérent |
| J60 | Rifampicine contre-indiquée si clairance < 25 mL/min | En ligne (Rifampicin Labatec, résumé de monographie suisse) |
| J60 | Valeur limite suisse du quartz alvéolaire 0,15 mg/m³ ; RR de tuberculose 4,01 avec silicose | Cohérent (Suva ; Ehrlich 2021) |
| J69 | Hydroxocobalamine 5 g en 15 min, 10 g au total | Cohérent (Cyanokit) |
| J69 | Pneumopathie d’immunothérapie : prednisone 1–2 mg/kg au grade 2, méthylprednisolone au grade 3–4 | Cohérent (ESMO/ASCO) |

## 6. Réserves restantes

1. **Encadrés « Paramètres clés » en listes à puces nominales** (J12, J21, J47, J60, J67, J80, J84, J85, J90, J93, J95, J96, R04, R05, R06). Ces listes reprennent la forme des cours canoniques, mais STYLE_REDACTION § 2 interdit la phrase nominale dans les encadrés. Elles ne sont pas réécrites ; l’auditeur peut en exiger la conversion en phrases complètes.
2. **R06** : « Paspertin contre-indiqué avant 18 ans » n’est pas confirmé en ligne. Il faut relire la monographie suisse.
3. **J18 canonique** : ce cours écrit « pH inférieur à 7,2 » (BTS 2010), alors que J85 et J90 appliquent « ≤ 7,2 » (BTS 2023). Ce cours étant canonique, il n’a pas été modifié ; la divergence est signalée à Codex.
4. **J21** : HARMONIE annonce 8 057 nourrissons ; la publication rapporte 8 058 randomisés. Ce point n’a pas été vérifié.
5. **J96** : la monographie suisse du flumazénil n’a pas été relue (le cours le signale déjà).
6. Les affirmations marquées « Cohérent » n’ont pas été relues dans le texte intégral pendant cette revue (R-11.5).
7. Les contrôles navigateur (ordinateur et mobile), `audit_fragments.py`, `audit_sciences.py` et `verify_course_native.cjs` ne sont pas exécutés.
