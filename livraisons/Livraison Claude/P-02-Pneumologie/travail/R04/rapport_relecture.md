# R04 — Hémoptysie (P-02-Pneumologie) — rapport de relecture différée

Auto-audit par Agent différé opus 5.5 · 09.10.2026 · cours unique couvrant R04 (CIM-10-GM 2024 ; code dans l’en-tête seulement).
Sources relues : `travail/R04/chapters/R04/` (6 fichiers), `travail/R04/glossary/r04.py`, `rapport_auteur.md`. Le brouillon de l’auteur reste intact dans ce dossier. La version relue est injectée dans `chapters/R04/` et `glossary/r04.py`.

**Cette relecture est une revue par IA. Elle ne vaut pas validation médicale humaine.** Aucun médecin n’a relu ce cours.

## Méthode

Deux passes successives et distinctes ont couvert les quatre dimensions de la section 13 de `LEADERSHIP_CLAUDE_2026-10-08.md`. La **passe 1** a relu les six fichiers en entier. Elle a confronté chaque chiffre, seuil et dose à la source primaire, téléchargée de nouveau par le relecteur, puis corrigé et renforcé le texte. La **passe 2** a relu en entier le texte issu de la passe 1, sous forme extraite, et corrigé les défauts restants. Ensuite sont venus les contrôles techniques et l’injection.

Les sources ont été téléchargées indépendamment de l’auteur le 09.10.2026 :
- PDF officiels : Collège des enseignants de pneumologie (SPLF), item 205, 2023 (11 pages, lu en entier) ; OFSP et Ligue pulmonaire suisse, *Tuberculose en Suisse*, guide V1.2024 (63 pages, chapitres 3, 6 et 7.5 lus) ;
- textes intégraux PMC (BioC ou HTML) : CIRSE 2022, Ittrich 2017, Fartoukh 2007, Mondoni 2021, Cochrane Prutsky 2016, Moen 2013 ;
- page HTML intégrale de la Revue médicale suisse 2015 (Théone et al., HUG) ;
- résumés PubMed par `efetch` pour les autres études ;
- AIPS AmiKo en texte intégral via `tools/swissmedic_fi.py`.

## Corrections de la passe 1

### Exactitude médicale et scientifique
| Point | Brouillon | Source lue | Correction |
|---|---|---|---|
| Définition | « Rejet par la bouche, au cours d’un effort de toux… » attribué à la SPLF | SPLF 2023 : « saignement, extériorisé ou non, des voies respiratoires sous-glottiques » ; l’effort de toux est le « point crucial » du diagnostic | Définition rendue fidèle (îlot 1, fenêtre, critères formels) ; l’effort de toux devient le critère diagnostique |
| BPCO | « La BPCO n’explique jamais une hémoptysie » (À retenir, Pareto) | SPLF 2023 : « n’est pas une cause » ; CIRSE 2022 range BPCO et bronchite chronique parmi les causes d’hémoptysie massive ; Mondoni retient « exacerbation de BPCO » | Divergence exposée dans la fenêtre ; conduite commune conservée (recherche systématique d’un cancer) ; formules absolues retirées |
| Étiologies | « Quatre causes dominent les séries européennes » ; infections aiguës absentes du tableau | Abdulmalak 2015 et Ittrich 2017, tableau 1 : infections respiratoires 22 %, cancer 17,4 %, bronchectasies 6,8 % ; Fartoukh 2007 : quatre causes = 87 % des hémoptysies graves | Infections aiguës ajoutées (texte et tableau) ; les quatre causes situées dans les formes graves |
| Tuberculose | Seule la recherche de BAAR ; aucun isolement (réserve 9 de l’auteur) | Guide suisse OFSP/Ligue pulmonaire V1.2024, ch. 6 et 7.5 | PCR directe des expectorations = test primaire ; microscopie et culture ; isolement hospitalier jusqu’à un premier échantillon PCR négatif, second échantillon si forte probabilité ; 5 à 15 jours sous traitement ; FFP2/N95 ; masque chirurgical hors chambre ; déclaration au médecin cantonal. Ajouté à la biologie, aux Examens, aux situations particulières, au Pareto |
| Gravité du cas index | 100 mL « modérée » selon la CIRSE | CIRSE : modérée 100–300 mL/j, mortalité possible par asphyxie ; grave si > 100 mL/24 h | Cas situé à la frontière ; traitement précoce |
| Mortalité traitée | Absente | CIRSE : moins de 20 % si diagnostic et traitement optimaux | Ajoutée (îlot 2) |
| Acide tranexamique, insuffisance rénale | Tableau sans la ligne > 500 µmol/L | AIPS Tranexamic acid Leman (02.2024) | 5 mg/kg toutes les 24 h au-delà de 500 µmol/L |
| Acide tranexamique oral, contre-indications | Incomplètes | AIPS Cyklokapron (06.2026) | Hémorragie sous-arachnoïdienne ajoutée |
| Acide tranexamique, preuves | « Sans preuve d’un bénéfice sur la mortalité » | Cochrane 2016 : durée −19,47 h ; pas d’effet sur la rémission à 7 jours ; mortalité non rapportée | Formulation alignée sur la revue ; SPLF « non systématique » ajouté |
| Acide tranexamique nébulisé | Seuil « > 200 mL dans Wand » ; bronchoconstriction attribuée aux deux essais | Résumés Wand 2018 et Gopinath 2023 | Seuil non lu retiré ; bronchoconstriction rattachée au seul bras nébulisé de Gopinath ; plans d’essai précisés (double aveugle, pilote ouvert) |
| Terlipressine | « Contracte les petits vaisseaux » ; grossesse = contre-indication absolue | AIPS Glypressine (03.2024) : vaisseaux intestinaux et utérins ; grossesse contre-indiquée sauf indication vitale | Mécanisme et grossesse précisés ; contre-indications de la Revue médicale suisse (AVC récent, crise hypertensive) ajoutées |
| Vitamine K adulte (réserve 5) | Lacune vague | AmiKo, recherche plein texte « Phytomenadion » : seule l’AIPS Konakion MM paediatric (2 mg, nouveau-né) existe ; aucune AIPS adulte | Lacune nommée précisément, sans dose inventée ; avis du spécialiste de l’hémostase (AIPS Beriplex) |
| Andexanet alfa | — | AIPS Ondexxya (04.2025) | « Ne convient pas en prétraitement d’une chirurgie urgente » ; tests anti-Xa commerciaux inutilisables |
| Chirurgie | « Mortalité opératoire en urgence 4 à 19 % » | Ittrich 2017 : 37–42 % en urgence et 7–18 % entre épisodes avant 1980 ; 4–19 % dans les séries récentes (sans distinction) | Corrigé ; indication CIRSE d’une chirurgie urgente si récidive < 72 h malgré une embolisation inefficace ajoutée |
| Intubation | « La revue allemande recommande » une sonde de gros calibre | Ittrich : « one can consider » | « Propose » |
| Hémoptysie cryptogénique | 50 %, 11 %, 15–20 % | SPLF (> 1/3), Revue médicale suisse (≈ 15 %), CIRSE (précède une tumeur maligne dans 10 %) | Fourchettes complétées et sourcées |
| Enfant (réserve 7) | Hors champ sans donnée | Ittrich : l’hémoptysie touche rarement l’enfant | Rareté sourcée ; absence de conduite pédiatrique européenne lue nommée |

Chiffres contrôlés sans changement (extraits) : 0,1 % ambulatoires et 0,2 % hospitalisés ; 15 000 adultes/an, 62 ans, 2/1 ; mortalité 9,2 %, 21,6 %, 27 % ; récidive 16,3 % ; OR 38,2 et 2,6 ; 90/5/5 % ; 150–200 mL ; PAPm 14,0 ± 3,3 mmHg ; artère bronchique 1,6 ± 0,3 mm, > 2 mm ; scanner 60–77 % et 63–100 % ; radiographie 33–82 % et 35–50 % ; bronchoscopie 73–93 % et 2,5–8 % ; Revel 77/8 % et 70/73 % ; Fartoukh 2012 (1087 patients, 6,5 %, AUC 0,87, probabilités 1 à 91 %) ; Fartoukh 2007 (toux 73 %, dyspnée 66 %, anomalie localisée 48 %, récidive 27 %) ; CIRSE (succès 90–100 %, 82–100 %, 70–92 %, 64–92 %, complications du tableau 9, anatomie T5–T6, 70/20/10 %, branche spinale 5–10 %) ; récidives 1–27 % et 10–55 %, survie sans récidive 94/87/34 % ; aspergillome 30–100 % ; doses Beriplex, Praxbind, Ondexxya, Glypressine, Cyklokapron.

### Sources et plan
- Source suisse ajoutée : guide *Tuberculose en Suisse* (OFSP et Ligue pulmonaire suisse, V1.2024), lien officiel bag.admin.ch.
- La mention de « catégorie de classification » a été retirée des fenêtres Définition et Pseudo-hémoptysie : le code CIM n’est pas un contenu enseigné.
- Références ajoutées aux îlots 2, 4 et Pharmacologie 1 (Ittrich, CIRSE), à la fenêtre BPCO (CIRSE), à la fenêtre cryptogénique (SPLF, Revue médicale suisse).
- Aucune recommandation américaine ne fonde une conduite. Les essais Wand (Israël) et Gopinath (Inde), publiés dans *Chest*, sont cités comme données ; NICE (Royaume-Uni) est européen.

### Rédaction
Phrases absolues ou imprécises reprises (BPCO « jamais », « recommande » pour une proposition, « sans preuve sur la mortalité ») ; paragraphe de lecture du tableau Pharmacologie rendu fidèle à Ittrich et à la SPLF ; titre de la fenêtre tuberculose élargi au diagnostic et à l’isolement.

## Corrections de la passe 2
- Îlot 1 : le cas index de 100 mL était présenté comme « modéré » sans signaler qu’il touche le seuil CIRSE de gravité ; reformulé.
- Îlot 2 : la phrase sur l’enfant manquait de référence ; Ittrich et CIRSE ajoutés.
- Fenêtre tuberculose : vérification mot à mot du masque chirurgical hors chambre (EN 14683) et de la déclaration au médecin cantonal dès le début du traitement.
- Glossaire : FFP2 et MM (micelles mixtes, Konakion MM) signalés non couverts par `build_medina.py` ; ajoutés de façon conditionnelle.

## Sources vérifiées (27 liens, tous contrôlés le 09.10.2026)

**PubMed (11), vérifiés par `efetch` : premier auteur, année, revue et titre concordants.**
12388502 Revel 2002 AJR · 17332480 Savale 2007 AJRCCM · 17989162 Khalil 2008 Chest · 19324955 Kovacs 2009 Eur Respir J · 22025193 Fartoukh 2012 Respiration · 25891303 Parrot 2015 Rev Mal Respir · 26022949 Abdulmalak 2015 Eur Respir J · 26699723 Denning 2016 Eur Respir J (ERS/ESCMID) · 30321510 Wand 2018 Chest · 30895588 Forster 2019 Pneumologie · 36410494 Gopinath 2023 Chest. Les pages pubmed.ncbi.nlm.nih.gov répondent 203 (page anti-robot) dans cet environnement ; les PMID sont valides.

**PMC (6), texte intégral, HTTP 200** : PMC9117352 (CIRSE 2022), PMC5478790 (Ittrich 2017), PMC1802746 (Fartoukh 2007), PMC8336236 (Mondoni 2021), PMC6464927 (Prutsky, Cochrane 2016), PMC3829500 (Moen 2013).

**URL officielles (HTTP 200, contenu lu)** : SPLF item 205 (2023, PDF) ; Revue médicale suisse 2015 ; OFSP/Ligue pulmonaire, *Tuberculose en Suisse* V1.2024 (PDF) ; NICE NG12 1.1.1 ; AIPS AmiKo : Beriplex P/N 7680006650015 (10.2022), Cyklokapron 7680337410494 (06.2026), Glypressine 7680444700129 (03.2024), Praxbind 7680658040011 (03.2021), Ondexxya 7680677590016 (04.2025), Tranexamic acid Leman 7680693850033 (02.2024).

Doses et contre-indications vérifiées mot à mot dans l’AIPS :
- **acide tranexamique IV** : 0,5–1 g IV lente (1 mL/min) 2–3 ×/j (fibrinolyse locale) ; 1 g/6–8 h (générale) ; créatinine 120–249 : 10 mg/kg/12 h ; 250–500 : 10 mg/kg/24 h ; > 500 : 5 mg/kg/24 h ; contre-indications (thrombose aiguë, convulsions, IR grave, CIVD, voies intrathécale et péridurale) ; bradycardie et asystolie si injection rapide ; grossesse et allaitement ;
- **acide tranexamique oral** : 2–3 comprimés 2–3 ×/j ; épistaxis 2 comprimés 3 ×/j pendant 7 jours ; créatinine 120–250 : 15 mg/kg/12 h, 250–500 : 15 mg/kg/24 h ; biodisponibilité 40 %, demi-vie 2 h, activité 10 fois celle de l’acide aminocaproïque ;
- **terlipressine** : > 50 kg 1–2 mg/4–6 h ; < 50 kg 1 mg ; 12 mg/j pendant 36 h au plus puis 6 mg ; 5 jours au plus ; contre-indications ; QT ; hyponatrémie ; effet 2–10 h ;
- **Beriplex P/N** : 25, 35, 50 UI/kg selon l’INR ; 5000 UI au plus ; correction en ≈ 30 min ; vitamine K (effet en 4–6 h) ; répétition non étayée ; contre-indications ;
- **Praxbind** : 5 g ; seconde dose possible ; reprise du dabigatran à 24 h ; aucune contre-indication ;
- **Ondexxya** : 400 mg puis 4 mg/min ou 800 mg puis 8 mg/min pendant 120 min ; dose élevée si apixaban > 5 mg ou rivaroxaban > 10 mg pris moins de 8 h auparavant ; héparine, chirurgie urgente, edoxaban, énoxaparine.

## Contrôles techniques et rendu

| Contrôle | Résultat |
|---|---|
| Clés et gabarits | 47 `data-k` = 47 gabarits (41 fenêtres et 6 Pareto), tous préfixés `r04-` ou `pareto-r04-` ; aucun identifiant dupliqué ; couvertures Pareto valides |
| Classes | identiques à la liste fermée employée par J81 |
| HTML | a+b+c+d concaténés bien formés (pile vide) ; fenêtres bien formées |
| Glossaire | `glossary/r04.py` : ajouts conditionnels `_a` de CIRSE, FFP2 et MM ; aucune de ces clés dans `glossary/*.py` au moment de l’injection ; FFP2 est aussi défini dans le dossier de travail J67 (non injecté) et ne sera pas écrasé |
| `build_medina.py R04` (copie superposée avec R04 enregistré) | `R04 non couvertes: 0` ; Pareto calculés (6 % pour le premier) |
| Contrat Sciences (logique `tests/audit_sciences.py`) | navigation complète ; 4 disciplines de 391, 348, 349 et 359 mots ; une figure légendée et accessible chacune ; les quatre liens présents |
| `build_front.py --fragment S02` (copie superposée, `MEDINA_OUT` dans le scratchpad) | 5,85 Mo, compressé à 2,85 Mo |
| Chromium 1194, `#/entry/R04` | 60 clics sur les mots verts des 4 onglets, des 4 disciplines et de toutes les pages du pager ; 41 fenêtres distinctes, toutes avec contenu, aucune « Fiche absente » ; 6 Pareto ouverts avec leur fraction ; aucune erreur JavaScript ni de console ; mobile 390 px sans défilement horizontal dans les 4 onglets |
| `tools/capture_lecon.py` | `captures/r04-1-ouverture.png`, `captures/r04-2-explication.png`, `captures.json` (statut : relu, injecté, non enregistré dans `chapters.json`) |

Le texte compte 13 698 mots hors références et SVG (14 929 avec références), dans la cible de 11 000 à 15 000 mots. La légère hausse vient du guide suisse de la tuberculose, des divergences BPCO et cryptogénique, et des précisions des AIPS.

## Réserves restantes (non bloquantes)

1. **Swiss Medical Forum non lu.** Les articles repérés (Joos Zellweger, « Hämoptoe », SMF 2018, DOI 10.4414/smf.2018.03194 ; Manzoni, « Approche diagnostique devant une hémoptysie », SMF 2014, DOI 10.4414/smf.2014.01825) existent selon Crossref et OpenAlex, mais medicalforum.ch, doi.emh.ch et web.archive.org sont refusés par le proxy ou en échec DNS. Ils ne sont pas cités. La source suisse sur l’hémoptysie reste la Revue médicale suisse 2015 (HUG), datée.
2. **Hors indication suisse** : acide tranexamique dans l’hémoptysie (IV, oral et nébulisé) et terlipressine (indication limitée aux varices œsophagiennes). Le cours rapporte les schémas autorisés les plus proches et le signale.
3. **Vitamine K adulte** : aucune information professionnelle suisse adulte de phytoménadione n’est disponible sur AmiKo ; aucune dose n’est donnée (lacune nommée dans la fenêtre et le tableau des doses).
4. **Épidémiologie suisse** : aucune donnée trouvée ; lacune nommée. **Enfant** : aucune conduite pédiatrique européenne lue. **Grossesse** : un cas publié et les AIPS seulement.
5. **Lectures limitées au résumé** pour Abdulmalak, Fartoukh 2012, Revel, Khalil, Savale, Denning, Parrot, Forster, Kovacs, Wand et Gopinath.
6. **Notion physiologique générale** formulée sans citation mot à mot : le shunt créé par les alvéoles inondées mais perfusées (les sources parlent de retentissement sur l’hématose et de troubles des échanges gazeux).
7. `tests/audit_sciences.py` exigera l’ajout de R04 à la liste des nouvelles productions sans base Git lors de l’enregistrement.
8. `chapters.json` et `organisation/*` n’ont pas été modifiés, comme demandé : l’enregistrement revient à l’orchestrateur. Une première construction `build_front.py --fragment S02` lancée sans `MEDINA_OUT` a écrit `/mnt/user-data/outputs/fragments/MEDINA_S02_respiratoire.html` (sortie de construction hors dépôt, contenu R04 inclus) ; les contrôles ont ensuite été refaits dans le scratchpad.

## Injection

- `chapters/R04/` : `R04_a.html`, `R04_b.html`, `R04_c.html`, `R04_d.html`, `R04_pop1.html`, `R04_pop2.html`.
- `glossary/r04.py` : CIRSE, FFP2 et MM en ajouts conditionnels.
- `livraisons/Livraison Claude/P-02-Pneumologie/travail/R04/captures/` : deux captures et `captures.json`.
- Entrée proposée pour `chapters.json` : `{"code": "R04", "covers": ["R04"], "title": "Hémoptysie", "integrated": true}`.
- Aucune opération Git. Aucun autre cours, ni `chapters.json`, ni `organisation/*`, ni le brouillon de l’auteur n’ont été modifiés.
