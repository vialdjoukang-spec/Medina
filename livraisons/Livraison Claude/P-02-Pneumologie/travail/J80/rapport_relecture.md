# J80 — Syndrome de détresse respiratoire aiguë de l’adulte (P-02-Pneumologie) — rapport de relecture différée

Auto-audit par Agent différé opus 5.5 · 09.10.2026 · cours unique couvrant J80 (code dans l’en-tête seulement).
Sources relues : `travail/J80/chapters/J80/` (6 fichiers) et `travail/J80/glossary/j80.py` ; aucun `rapport_auteur.md` n’accompagnait le brouillon. Le brouillon est conservé intact ; la version relue est injectée dans `chapters/J80/` et `glossary/j80.py`.

**Cette relecture est une revue par IA. Elle ne vaut pas validation médicale humaine.**

## Règles appliquées

`CLAUDE.md`, `LEADERSHIP_CLAUDE_2026-10-08.md` (sections 7 à 13 : règle fondamentale, audit en quatre dimensions, double passe), `CHAPTER_SPEC.md`, `PROMPT_MEDINA.md` § 10, `docs/STYLE_REDACTION.md`, `CONSIGNES_INTERACTION_DENSITE_SOURCES.md` ; modèle J84 injecté.

## Passe 1 — constats et corrections

### Dimension 3 — sources (constat majeur du brouillon)

| Constat | Correction |
|---|---|
| Fondement américain : ATS 2024 (Qadir) retenue comme « source la plus récente » pour la PEEP et la curarisation ; SCCM 2024 (Chaudhuri) et ATS 2024 retenues pour les corticoïdes ; mention dans l’en-tête. Indicateur `tools/americanisation.py` du brouillon : **58,1 % américain, 0 % suisse**. | ATS 2024 et SCCM 2024 retirées. Arbitrages refondus sur des textes européens ou co-signés par l’ESICM : **ESICM 2023** (texte intégral PMC10354163 lu, grades vérifiés), **ATS/ESICM/SCCM 2017** (Fan, co-signé ESICM), **SCCM/ESICM 2017** (Annane, corticoïdes), **ERS/ESICM/ESCMID/ALAT 2023** (pneumonie sévère, texte intégral PMC10069946), **ESICM 2025** (remplissage). Indicateur final : **7,3 % américain, 26,6 % suisse** ; les 9 occurrences « américaines » restantes sont toutes le sigle « /SCCM » du texte conjoint ATS/ESICM/SCCM 2017, que le détecteur ne reconnaît pas comme conjoint. |
| Aucune source suisse. | Ajouts : informations professionnelles suisses (AIPS via AmiKo, texte intégral) Nimbex® (02.2022), Dexaméthasone Galepharm Amp (06.2022), méthylprednisolone injectable Pfizer (08.2025), Lasix® ampoules (03.2025) ; **Swissmedic Hémovigilance, rapport annuel 2024** (TRALI 0,4/100 000, TACO 14/100 000) et page d’obligation de déclaration (art. 59 al. 3 LPTh) ; **SSMI, Choosing wisely soins intensifs** (recommandations 1 et 7, version 10.01.2023). |
| Information professionnelle **allemande** (fachinfo.de) pour le cisatracurium ; monographie suisse déclarée « non consultable ». | Remplacée par l’AIPS suisse Nimbex® lue intégralement. |
| Liens DOI non vérifiés par API. | Tous les liens convertis en PubMed et vérifiés (esummary : auteur, année, revue concordants, 33 PMID) ; 4 URL officielles testées HTTP 200. Liste ci-dessous. |

### Dimension 2 — exactitude médicale

1. **Collision de sigle bloquante** : le brouillon définissait `PEP` = pression expiratoire positive, alors que `glossary/b24.py` définit `PEP` = prophylaxie postexposition ; selon l’ordre de chargement, l’un des deux cours aurait affiché une définition fausse. Le cours emploie désormais **PEEP** (clé nouvelle, définie lettre à lettre) ; `EOLIA` (déjà défini dans `j09.py`) n’est plus redéfini ; toutes les clés de `j80.py` sont gardées par `if k not in G`.
2. **Code CIM enseigné** (règle 4) : paragraphe et fenêtre `j80-codage` sur J80.01–J80.09, entrées de glossaire J80.0x et P22.0, mention « (J81) » retirés.
3. **Corticoïdes** : statut suisse ajouté — dexaméthasone autorisée seulement dans la COVID-19 (6 mg IV/jour ≤ 10 jours) ; SDRA d’autre cause **hors indication** (DEXA-ARDS 20 puis 10 mg ; méthylprednisolone 1 mg/kg/jour selon SCCM/ESICM 2017). Ajouts : début > 14 jours délétère, pneumonie sévère avec choc (0,5 mg/kg/12 h × 5 jours), grippe exclue.
4. **Cisatracurium** : posologie AIPS (3 µg/kg/min ; 0,5–10,2 µg/kg/min), pharmacocinétique en soins intensifs (Hofmann ≈ 80 % de la clairance, demi-vie 27 min, récupération ≈ 50 min), interactions complètes de l’AIPS, incompatibilité de voie avec une transfusion, contre-indication < 1 mois. **Schéma ACURASYS « 15 mg puis 37,5 mg/h » retiré** : non vérifiable dans les sources lues.
5. **Hypercapnie permissive** : seuil « pH < 7,20–7,25 » non sourcé remplacé par les seuils du protocole ARDSNet (objectif 7,30–7,45 ; 7,15–7,30 ; < 7,15). Contre-indications non sourcées (grossesse, hypertension intracrânienne) retirées.
6. **Cible d’oxygénation** : essai européen **LOCO2** ajouté (cible basse : mortalité à 90 jours 44,4 % contre 30,4 %, arrêt pour sécurité).
7. **Définition** : ajout de la correction barométrique au-dessus de 1 000 m (définition globale), des conditions de mesure (repos, ≥ 30 min), des limites de l’oxymétrie (carboxy/méthémoglobine, peau foncée) ; statut exact du texte 2024 (consensus d’experts, non document officiel d’une société). Berlin présentée comme initiative de l’ESICM.
8. **ECMO** : méta-analyse ESICM (RR 0,72 ; 0,57–0,91), complications EOLIA chiffrées. **Cœur pulmonaire aigu** : données Mekontso Dessap 2016 (22 %, score à 4 facteurs, 57 % contre 42 %).
9. **Physiopathologie et sciences** réalignées sur les sources lues : surface ≈ 120 m², distance ≈ 2 µm (Ochs 2020) au lieu de 100 m² et « quelques dixièmes de µm » ; composition du surfactant 80/10/10 et mécanismes d’inactivation (Dushianthan 2023), avec correction : la synthèse par les pneumocytes II restants est préservée, l’inactivation domine ; rapport protéines œdème/plasma 0,65 ; sous-phénotypes 30/70 %. Retirés faute de source : « 95 % de la surface couverte par les type I », drainage lymphatique, vasoconstriction hypoxique atténuée, phase fibrotique « au-delà de 3 semaines », seuil d’éosinophiles « > 25 % », compliance « > 50 mL/cm H₂O », P/F « normal 430–480 », PaCO₂ gravidique, mécanisme des récepteurs J, signes cliniques non sourcés (fenêtres dyspnée, signes de lutte, auscultation supprimées), seuil « FR > 30 / SpO₂ < 90 % » présenté comme validé (remplacé par la lacune nommée de Matthay 2019 : aucun seuil d’intubation validé).
10. **Mortalité** : « la plupart des décès ne sont pas dus à l’hypoxémie » (non sourcé) remplacé par l’incertitude d’attribution (Matthay 2019) et la donnée immunodéprimés LUNG SAFE (21 %, 52 % contre 36 %).
11. **Décubitus ventral** : contre-indications et complications selon Guérin 2020 (seule absolue : fracture instable du rachis ; équipe de 4 à 5) ; arbitrage de durée > 12 h/jour (2017) contre ≥ 16 h consécutives (ESICM 2023).
12. **Grossesse** : affirmations non sourcées remplacées par une lacune nommée.

### Dimension 1 — rédaction

Infinitifs injonctifs de l’îlot 0 réécrits en phrases complètes ; « il faut », « on » remplacés ; tableaux introduits et commentés ; fenêtres contentieux structurées « source retenue / texte antérieur / relation / conséquence » avec liens vers le texte en vigueur ; plan monographique conservé (13 îlots) ; aucune phrase de fabrication.

### Dimension 4 — frontend

Classes de la liste fermée uniquement ; identifiants et clés préfixés `j80-` ; quatrième quiz ajouté (correction barométrique).

## Passe 2 — relecture intégrale du résultat de la passe 1

- Affirmations géographiques non sourcées (« de nombreux hôpitaux suisses au-dessus de 1 000 m ») retirées ; nom de lieu dans le quiz 4 remplacé par un cas hypothétique.
- Numérotation ESICM corrigée (curarisation = recommandation 8.1, non « 8.1 et 8.2 ») ; « trente fois » corrigé en « environ trente-cinq fois » (14/0,4).
- Phrase incohérente avec la COVID-19 (« la pneumocystose, seule cause où les corticoïdes sont établis ») reformulée.
- Libellés du Nimbex® réalignés sur l’AIPS (« myorelaxant non dépolarisant, bloc compétitif ») ; mention « benzylisoquinoléique de durée intermédiaire » retirée (absente de la source) ; effets indésirables de la dexaméthasone séparés de ceux de la méthylprednisolone.
- Sigles non couverts détectés par l’audit (CC, A2, CCL2, noms de titulaires « AG/GmbH/SA », « Solu-MEDROL », « Fuchs-Buder ») reformulés.
- Recalcul de tous les exemples chiffrés (poids prédits, rapports, compliances, correction barométrique) : exacts.

## Sources vérifiées (preuve)

PubMed, vérifiés par `eutils esummary` le 09.10.2026 (premier auteur, année, revue concordants) ; résumé lu pour tous, **texte intégral** lu pour ESICM 2023 (PMC10354163), définition globale (PMC10870872), Matthay 2019 (PMC6709677), PALICC-2 (PMC9848214), ERS/ESICM/ESCMID/ALAT 2023 (PMC10069946), Guérin 2020 (PMC7652705), Vlaar 2019 (PMC6850655), Dushianthan 2023 (PMC10528901), Ochs 2020 (PMC7246550).

| PMID | Référence |
|---|---|
| 22797452 | Ranieri (Berlin), JAMA 2012 |
| 37487152 | Matthay, définition globale, AJRCCM 2024 |
| 26903337 | Bellani, LUNG SAFE, JAMA 2016 |
| 30872586 | Matthay, Nat Rev Dis Primers 2019 |
| 15812622 | Gattinoni, Intensive Care Med 2005 |
| 23370917 | Thille, AJRCCM 2013 |
| 37326646 | Grasselli, ESICM 2023, Intensive Care Med |
| 28459336 | Fan, ATS/ESICM/SCCM 2017 |
| 28940011 | Annane, SCCM/ESICM 2017, Intensive Care Med |
| 40163133 | Mekontso Dessap, ESICM 2025 (remplissage) |
| 37012484 | Martin-Loeches, ERS/ESICM/ESCMID/ALAT 2023 |
| 10793162 | ARDSNet (Brower), NEJM 2000 |
| 23688302 | PROSEVA (Guérin), NEJM 2013 |
| 29791822 | EOLIA (Combes), NEJM 2018 |
| 16714767 | FACTT (Wiedemann), NEJM 2006 |
| 20843245 | ACURASYS (Papazian), NEJM 2010 |
| 31112383 | ROSE (Moss), NEJM 2019 |
| 32043986 | DEXA-ARDS (Villar), Lancet Respir Med 2020 |
| 32678530 | RECOVERY (Horby), NEJM 2021 |
| 32160661 | LOCO2 (Barrot), NEJM 2020 |
| 25693014 | Amato, NEJM 2015 |
| 26650055 | Mekontso Dessap, Intensive Care Med 2016 |
| 21470008 | Herridge, NEJM 2011 |
| 36661420 | Emeriaud (PALICC-2), Pediatr Crit Care Med 2023 |
| 22166903 | BALTI-2 (Gao Smith), Lancet 2012 |
| 27347773 | Gebistorf, Cochrane 2016 |
| 30798570 | Lansbury, Cochrane 2019 |
| 30626363 | Meng, BMC Pulm Med 2019 |
| 37761330 | Dushianthan, Diagnostics 2023 |
| 32349261 | Ochs, Int J Mol Sci 2020 |
| 33169218 | Guérin, Intensive Care Med 2020 |
| 30993745 | Vlaar (TRALI), Transfusion 2019 |
| 36377554 | Fuchs-Buder, ESAIC, Eur J Anaesthesiol 2023 |

URL officielles (HTTP 200 le 09.10.2026) : Swissmedic Hémovigilance rapport 2024 (PDF lu, p. 15-16) ; Swissmedic « ce qu’il faut déclarer » ; SSMI Choosing wisely (PDF français lu) ; protocole ARDSNet 2008 (PDF lu : formule du poids prédit en pouces, convertie en cm dans le cours ; cibles de pH, d’oxygénation, plateau). AIPS lues par `tools/swissmedic_fi.py texte` : GTIN 7680536770108 (Nimbex®), 7680667100010 (Dexaméthasone Galepharm Amp), 7680351120812 (méthylprednisolone Pfizer), 7680306300177 (Lasix® ampoules).

## Réserves restantes (non bloquantes)

1. Le protocole ARDSNet (réseau américain) fonde le poids prédit, la cible de pH et la cible d’oxygénation : document d’essai, cité comme donnée et non comme recommandation ; aucune cible équivalente n’existe dans l’ESICM 2023.
2. La définition globale 2024 est un consensus international d’experts publié dans une revue de l’ATS, non approuvé par une société ; elle est retenue au titre de source primaire la plus récente, l’ESICM 2023 ayant discuté la même extension.
3. Corticoïdes dans le SDRA non lié à la COVID-19 : hors indication suisse ; le texte européen co-signé le plus récent date de 2017.
4. Nombreuses données physiopathologiques et cliniques reposent sur une revue (Matthay 2019, Nat Rev Dis Primers) plutôt que sur les études primaires citées par elle.
5. Aucune donnée d’incidence suisse ni recommandation suisse propre au SDRA (lacune nommée) ; aucune recommandation européenne pour la grossesse (lacune nommée).
6. Train-de-quatre : la recommandation ESAIC 2023 porte sur la période périopératoire ; son application en soins intensifs est une extrapolation signalée.
7. Volume : 16 485 mots (brouillon 13 588, +21 %) ; l’augmentation provient des arbitrages sourcés, des données suisses et des monographies AIPS ; les fenêtres portent l’essentiel du détail.

## Injection

- `chapters/J80/` : J80_a, J80_b, J80_c, J80_d, J80_pop1, J80_pop2 (57 fenêtres dont 7 Pareto, 4 quiz).
- `glossary/j80.py` : 15 clés nouvelles (PEEP, PALICC, PALICC-2, ARDSNet, PROSEVA, ACURASYS, ROSE, FACTT, DEXA-ARDS, LUNG SAFE, LOCO2, BALTI-2, TRALI, TACO, SSMI), aucune collision.
- `chapters.json`, `organisation/*` et autres cours : non modifiés (enregistrement par l’orchestrateur). Aucune opération Git.

## Contrôles

| Contrôle | Résultat |
|---|---|
| Fenêtres | 57 `data-k`, 57 gabarits, aucune clé manquante ni orpheline, aucun identifiant dupliqué, toutes préfixées `j80-` |
| Classes | toutes dans la liste fermée de `build_medina.CLASSMAP` |
| HTML | bien formé (analyseur : aucune balise non fermée ni croisée) |
| Audit des sigles (`build_medina.audit`, racine temporaire avec J80) | `J80 non couvertes: 0` ; ratios Pareto calculés (5 à 8 %) |
| Fragment S02 construit (`build_front.py --fragment S02`, racine temporaire) | 59 mots verts cliqués dans les 4 onglets et les 4 disciplines, 59 fenêtres non vides ; 0 erreur JavaScript ni console ; aucun défilement horizontal à 1300 px ni à 390 px |
| `tools/capture_lecon.py` | `captures/j80-1-ouverture.png`, `captures/j80-2-explication.png` (dossier de travail J80) |
| `python3 -m unittest discover -s tests` (après injection) | 237 tests, OK |

Empreintes SHA-256 :

```
d0dc7b3d552be8e9a81f5bcc624bb011dd4d4e9dbda656f33d7ee3ace6349954  chapters/J80/J80_a.html
cc2d94743b5451a61bfce39d5661afc6939a25738909bacdd89566ea6df1bc99  chapters/J80/J80_b.html
db6d289ce23b2e4591a7c43dbab9f7a809435173001dff1d5b7e173beb3c338f  chapters/J80/J80_c.html
66e905c7d845bdaa07bfd1f68befedc3fd888bc499fe590f0161c9dc4e08657c  chapters/J80/J80_d.html
3765af624289e3f9719083f53db5e2be0b6c328798ef3807c2b6ea461f82df0a  chapters/J80/J80_pop1.html
90af8269e13723a055c13c864cf3441b4ac550e0dfefa2889e48f40ff54ccf03  chapters/J80/J80_pop2.html
8751da13b4ffd9a0c0eef64e6c6d16eeb72adbf7edfa6a0a56b009e97c0f4b1b  glossary/j80.py
```

Statut : injecté après deux passes sans réserve bloquante. Revue IA, non validation médicale.
