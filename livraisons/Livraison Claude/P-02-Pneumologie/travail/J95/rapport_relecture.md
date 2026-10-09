# J95 — Complications respiratoires des actes médicaux et autres troubles respiratoires (P-02-Pneumologie) — rapport de relecture différée

Auto-audit par Agent différé opus 5.5 · 09.10.2026 · cours unique couvrant J95, J98 et J99 (CIM-10-GM 2024 ; code dans l’en-tête seulement).
Sources relues : `travail/J95/chapters/J95/` (6 fichiers), `travail/J95/glossary/j95.py`, `rapport_auteur.md`. Le brouillon de l’auteur reste intact dans ce dossier. La version relue est injectée dans `chapters/J95/` et `glossary/j95.py`.

**Cette relecture est une revue par IA. Elle ne vaut pas validation médicale humaine.** Aucun médecin n’a relu ce cours.

## Méthode

Deux passes successives et distinctes ont couvert les quatre dimensions de la section 13 de `LEADERSHIP_CLAUDE_2026-10-08.md`. La **passe 1** a relu les six fichiers en entier. Elle a confronté chaque chiffre, seuil et dose à la source primaire, téléchargée de nouveau par le relecteur, puis corrigé et renforcé le texte. La **passe 2** a relu en entier le texte issu de la passe 1, sous forme extraite, et corrigé les défauts restants. Ensuite sont venus les contrôles techniques et l’injection.

Les sources ont été téléchargées indépendamment de l’auteur le 09.10.2026 :
- textes intégraux PMC par `efetch` (db=pmc) ;
- résumés PubMed par `efetch` ;
- articles de la Revue médicale suisse en HTML (revmed.ch) et PDF du Swiss Medical Weekly (Kather 2024) ;
- AIPS AmiKo par `tools/swissmedic_fi.py`.

## Points signalés par l’auteur — arbitrage

| Point | Constat du relecteur | Décision |
|---|---|---|
| Score ARISCAT tiré d’un tableau secondaire (Lee 2025, Corée) | Texte intégral de Canet 2010 refusé (HTTP 403 sur pubs.asahq.org ; Europe PMC : non ouvert). Aucune source européenne en accès libre ne reproduit la grille de points ; Valencia 2025 (Espagne) et Giehl-Brown 2025 (Allemagne) citent le score sans ses points. L’essai européen de Hemmes 2014 (texte intégral PMC6682759) confirme les classes (26 à 44 ; plus de 44) et l’usage du score pour le recrutement. Les points de Lee concordent avec une seconde reproduction indépendante (Chikkala 2025, PMC12535847, tableau de cohorte) | Lee conservé comme reproduction ; Hemmes ajouté comme appui européen des classes ; limite d’accès écrite dans la fenêtre ARISCAT. Réserve non bloquante |
| Critères NIH de la bronchiolite oblitérante | Glanville 2022 (ERJ Open Res, journal de l’ERS) écrit explicitement « The US National Institutes of Health definition ». Ils ne fondaient aucune conduite dans le brouillon ; la référence de traitement est ERS/EBMT 2024 (Bos), lue en résumé | Étiquetés « définition diagnostique des National Institutes of Health américains » dans l’alerte, la fenêtre et le Pareto ; phrase explicite : ils ne fondent aucune conduite. Ajout de la recommandation européenne EBMT 2020 (fluticasone, azithromycine, montélukast et bref bolus de corticoïde, niveau 2A, sur 36 patients non randomisés), lue dans Glanville ; Penack 2020 (résumé) cité |
| Hors indication | Solu-Medrol® (08.2025) : œdème laryngé aigu non infectieux, adrénaline en premier choix, aucune prévention post-extubation. Kenacort®-A (12.2021) : sous-lésionnel, chéloïdes, jamais intraveineux, aucune voie trachéale. Pulmicort® (06.2023) : asthme et bronchite chronique obstructive | Mention « hors indication » ajoutée au tableau Pharmacologie (méthylprednisolone) et à l’îlot 10 (triamcinolone) ; déjà présente dans les fenêtres et le tableau des doses |
| Clés de glossaire « noms d’auteurs » | `build_medina.audit()` signale tout mot à deux majuscules ou à majuscule interne : Abu-Omar, Dajer-Fadel, Fuchs-Buder et McGrath seraient « non couverts » sans clé. Ces chaînes exactes n’apparaissent dans aucun autre mot du cours ; aucune autre clé du dépôt ne les recouvre | Conservées. Toutes les clés de `j95.py` passent par un ajout conditionnel `_a` (convention de `j81.py`). SRLF existe aussi dans le dossier de travail R06 : définition neutre ici |

## Corrections de la passe 1

### Exactitude médicale et scientifique
| Point | Brouillon | Source lue | Correction |
|---|---|---|---|
| Atélectasie et dysfonction diaphragmatique (35 % contre 13 %) | Attribuée à Lagier 2022 | Le chiffre figure dans Zeng 2022 (partie I), non dans Lagier | Citation corrigée (Zeng, 2022) |
| Bloc interscalénique | Effet « transitoire » | Lagier 2022 : risque d’atélectasie homolatérale par paralysie phrénique, sans durée | « Transitoire » retiré ; autres blocs cervicaux ajoutés |
| PEEP élevée et hypotension | Attribuée aux essais de Hemmes et de Bluth | Hemmes (PMC6682759) : hypotension et vasopresseurs ; Bluth (résumé) : aucune hypotension rapportée | Hypotension réservée à l’essai de Hemmes |
| Recommandation 1B de la Société européenne d’anesthésiologie et de l’ESICM | « Préfèrent la VNI ou la CPAP » | Résumé Leone 2020 : VNI ou CPAP, selon l’expertise locale, pour améliorer l’oxygénation | Objet et nuance de la recommandation précisés |
| Curarisation résiduelle (fenêtre, Pharmacologie îlot 4) | « C’est la qualité de la décurarisation, non le choix de la molécule, qui protège » (attribué à Kirmeier) | Résumé Kirmeier 2019 : ni surveillance, ni antagonisation, ni sugammadex, ni extubation à un rapport ≥ 0,9, tels que pratiqués, n’étaient associés à moins de complications ; Lagier : moins de complications avec une décurarisation guidée par une surveillance adaptée ; ESAIC R6 à R8 | Résultat négatif exposé en entier ; conclusion rattachée à Lagier et à l’ESAIC |
| Pression motrice ≥ 15 cm H₂O | « Associée aux complications » (non sourcé) | Lagier 2022, figure 6 : signe d’altération mécanique significative sous PEEP 5 et 6 mL/kg | Reformulé selon Lagier (Biophysique, fenêtre Ventilation protectrice) |
| Grands volumes courants | « Empêchent l’atélectasie mais augmentent les complications » (non sourcé) | Lagier 2022 : petit volume courant et PEEP modérée meilleurs qu’un grand volume sans PEEP ; PEEP de 8 à 12 sans bénéfice supplémentaire | Remplacé par la donnée de Lagier |
| Pression critique de fermeture 6 cm H₂O | Généralisée à « l’anesthésié ventilé » | Zeng 2022 : « small number of anesthetized patients » | Précisé ; source ajoutée |
| Recrutement (Science → traitement, fenêtre Shunt) | « Corrige rapidement le trouble des échanges » | Hemmes, Bluth | Ajout : l’oxygénation s’améliore sans réduction des complications |
| Trachéotomie, technique | « La fibroscopie réduit les complications précoces » | Trouillet 2018, R2.3, R3.1, R3.3 | Percutanée par dilatation « probablement » préférable ; fibroscopie « probablement » recommandée ; échographie cervicale : succès accru, complications immédiates réduites |
| Trachéotomie, contre-indications | Instabilité et coagulation seulement | Trouillet 2018, R1.4 | Ajout : hypertension intracrânienne (> 15 mmHg), hypoxémie sévère (PaO₂/FiO₂ < 100 mmHg sous PEEP > 10) |
| Sténose : endoscopie ou résection | « Complexe… relève d’un centre de chirurgie trachéale » ; « récidivante » | Kather 2024 (Ozdemir) : complexe → résection ou prothèse avec surveillance ; Kather : endoscopie possible même après resténose chirurgicale | Reformulé ; « récidivante » retiré ; Ferreirinha cité pour la résection |
| Corticoïde local de la sténose | « Vise l’inflammation qui entretient la refibrose » | Kather 2024 : la triamcinolone réduit l’inflammation muqueuse et la récidive (la refibrose concerne la mitomycine) | Corrigé (Anatomopathologie, deux endroits) |
| Fistule bronchopleurale (ESTS) | « Environ trois fois » ; base entière | Brunelli 2020 : groupes appariés (0,4–0,5 % contre 1,4–1,8 %) | « Trois à quatre fois » ; groupes appariés précisés |
| Esmeron® et anesthésiques volatils | « Prolongent le bloc » | AIPS Esmeron® 07.2026 : les anesthésiques volatils halogénés renforcent l’effet curarisant | Formulation de l’AIPS |
| Kirmeier | « 21 694 patients opérés » | Résumé : 22 803 inclus, 1658 complications sur 21 694 analysés, 28 pays européens | « Patients analysés », « européens » |
| Pneumomédiastin | « Série espagnole » ; « se complique surtout » (sans « spontané ») | Résumés Macia et Dajer-Fadel (nationalité non indiquée ; revue limitée au pneumomédiastin spontané) | Nationalité retirée ; « spontané » ajouté |
| Kather, asthme | « Traités pour un asthme » | Kather, tableau 1 : « previous misdiagnosis of bronchial asthma » | « Reçu à tort un diagnostic d’asthme » |
| Fiz 2020 | « Prédisait l’échec de la décanulation » | Résumé : le score ≥ IIIb prédisait la décanulation finale (moins souvent réussie) | Reformulé |
| Œdème laryngé, premier geste | « Évaluer la réintubation » | Quintard 2019 (échec d’extubation et réintubation) | « Surveillance rapprochée et réintubation préparée » |
| ARISCAT, durée | « Pèse autant qu’une thoracotomie » | Lee, tableau 3 : 23 contre 24 points | « Presque autant qu’une incision intrathoracique (24 points) » |

### Sources et plan
- **Young 2019** était présenté comme « consensus européen » : il s’agit d’un consensus international d’experts (Duke University, avec des anesthésistes européens). Corrigé partout ; la conduite ventilatoire est aussi appuyée par Lagier 2022 et par les essais européens.
- **Recommandations américaines** : aucune ne fonde une conduite. Les critères des National Institutes of Health sont étiquetés comme définition diagnostique.
- **Références ajoutées** : Hemmes (îlot 4, Sciences Physiologie) ; Bluth (Sciences Physiologie) ; Bos ERS et EBMT 2024 (îlot 12) ; Penack EBMT 2020 (fenêtre bronchiolite). François 2007 a été retiré des références d’Anatomopathologie, où il n’était pas cité.
- Le plan monographique est respecté. Le code CIM ne figure que dans l’en-tête.

### Rédaction
- « Raccourcir et miniaturiser l’intervention » est devenu « préférer la laparoscopie et limiter la durée de l’intervention ».
- Un libellé de mot vert était tautologique : « obésité (atélectasie…) accroît l’atélectasie ».
- Un chiffre accolé à une année a été écrit en lettres : « en 2015 22 événements » devient « vingt-deux événements ».
- La mention « cohorte de validation » a été remplacée par « cette classe » dans le quiz ARISCAT, car la source ne la précise pas.
- La nuance « dans la cohorte de Canet » a été ajoutée au Pareto clinique, ainsi que les fréquences par classe ARISCAT.

## Corrections de la passe 2
La relecture intégrale du texte corrigé a encore modifié les points suivants :
- « en 2015 22 » est devenu « vingt-deux » ;
- quiz ARISCAT : « cette classe » ;
- formulation de l’AIPS sur les anesthésiques volatils halogénés ;
- contre-indications de la trachéotomie complétées (R1.4) ;
- Fiz : décanulation ;
- libellé du mot vert Obésité ;
- fenêtre Shunt (nuance sur le recrutement).

## Sources vérifiées (50 liens, tous contrôlés le 09.10.2026)

**PubMed (27), vérifiés par `esummary` : premier auteur, année et revue concordants.**
Les pages PubMed répondent 203 ou 429 à travers le proxy de la session.
8154776 Myer 1994 Ann Otol Rhinol Laryngol · 17398307 François 2007 Lancet · 17420139 Macia 2007 Eur J Cardiothorac Surg · 18283429 Gosselink 2008 Intensive Care Med · 19748792 Perna 2010 Eur J Cardiothorac Surg · 21045639 Canet 2010 Anesthesiology · 21841864 De Feo 2011 Tex Heart Inst J · 22731935 McGrath 2012 Anaesthesia · 24887879 Dajer-Fadel 2014 Asian Cardiovasc Thorac Ann · 25058504 Jammer 2015 Eur J Anaesthesiol · 25951790 Monnier 2015 Eur Arch Otorhinolaryngol · 26975890 Jaber 2016 JAMA · 28077503 Abu-Omar 2017 Eur J Cardiothorac Surg · 29371130 Ferrando 2018 Lancet Respir Med · 29661384 Abbott 2018 Br J Anaesth · 30224322 Kirmeier 2019 Lancet Respir Med · 30956204 Laveneziana 2019 Eur Respir J · 31045901 Hedenstierna 2019 Anesthesiology · 31508817 Fiz 2020 Laryngoscope · 31587835 Young 2019 Br J Anaesth · 32004485 Penack 2020 Lancet Haematol · 32132408 Leone 2020 Eur J Anaesthesiol · 33378546 Ferreirinha 2020 Swiss Med Wkly · 34153272 PRISM trial group 2021 Lancet Respir Med · 34649974 Oczkowski 2022 Eur Respir J · 36377554 Fuchs-Buder 2023 Eur J Anaesthesiol · 38485149 Bos 2024 Eur Respir J.

Mode de lecture par le relecteur :
- **texte intégral PMC** :
  - Zeng 2022 (PMC9869183) ;
  - Lagier 2022 (PMC9885487) ;
  - Lee 2025 (PMC11704732, tableaux 1 et 3) ;
  - Quintard 2019 (PMC6342741, recommandations R5 à R7) ;
  - Trouillet 2018 (PMC5854567) ;
  - Hemmes 2014 (PMC6682759) ;
  - Glanville 2022 (PMC9309343) ;
  - McGrath 2021 (PMC8103083) ;
  - Wragg 2025 (PMC12620918) ;
- **résumé seulement** : Bluth 2019 (PMC6582260, résumé structuré) et Brunelli 2020 (PMC7825477), ainsi que tous les PMID ci-dessus.

**Autres URL (HTTP 200, contenu lu)**
- Younossian et al., Rev Med Suisse 2011 : texte intégral HTML.
- Baskaralingam et al., Rev Med Suisse 2020 : texte intégral HTML. Toutes les valeurs du diaphragme ont été contrôlées : capacité vitale, PImax, SNIP, sensibilité et spécificité de l’imagerie, critères de VNI, délais de plicature, 1 % de syndrome des poumons rétractés.
- Kharat et Plojoux, Rev Med Suisse 2021 : résumé.
- Kather et al., Swiss Med Wkly 2024 : PDF intégral de 6 pages.
- CIM-10-GM 2024, BfArM, bloc J95–J99 : lien de la fenêtre Mendelson.
- AIPS via AmiKo (produit et date de mise à jour confirmés dans le texte) :
  - Esmeron®, 7680526860598, 07.2026 ;
  - Bridion®, 7680585090011, 02.2026 ;
  - Robinul®-Néostigmine, 7680493890192, 04.2020 ;
  - Naloxon OrPha, 7680569520015, 07.2026 ;
  - Solu-Medrol®, 7680351120812, 08.2025 ;
  - Kenacort®-A 10 et A 40, 7680261770145, 12.2021 ;
  - Pulmicort®, 7680501920163, 06.2023.

Doses vérifiées mot à mot dans l’AIPS :
- **rocuronium** : 0,6 mg/kg, conditions acceptables en 60 s chez 75 à 80 % ; 1,0 mg/kg en séquence rapide ; entretien 0,15 mg/kg, ou 0,075 à 0,1 mg/kg sous volatil prolongé. Risque de bloc résiduel après 65 ans. Recurarisation après aminosides, lincosamides, quinidine, quinine et magnésium ;
- **sugammadex** : 2 mg/kg à T2 (environ 2 min) ; 4 mg/kg à 1 ou 2 réponses post-tétaniques (environ 3 min) ; 16 mg/kg après 1,2 mg/kg de rocuronium. Poids réel chez l’obèse. Récurrence du bloc 0,20 %, avec redose de 4 mg/kg. Non recommandé si clairance < 30 mL/min. Bradycardie prononcée rare ; anaphylaxie possible. Une injection équivaut à l’oubli d’un contraceptif oral ; méthode non hormonale pendant 7 jours en cas de contraception non orale. Indiqué dès 2 ans ;
- **néostigmine et glycopyrronium** : 1 mL ou 0,02 mL/kg (50 et 10 µg/kg) en 10 à 30 s, au plus 2 mL. Contre-indiqué en cas d’obstruction digestive ou urinaire. Prudence en cas de bronchospasme ou de bradycardie sévère ;
- **naloxone** : 0,1 à 0,2 mg, puis 0,1 mg toutes les 2 à 3 min ; nouvelle dose possible à 1 ou 2 h ; perfusion possible. Tachycardie et fibrillation ventriculaires rapportées chez des opérés.

## Contrôles techniques et rendu

| Contrôle | Résultat |
|---|---|
| Clés et gabarits | 48 `data-k` = 48 gabarits (42 fenêtres et 6 Pareto) ; tous préfixés `j95-` ou `pareto-j95-` ; aucun identifiant dupliqué ; couvertures Pareto valides |
| Classes | toutes présentes dans les cours de référence J81, J84 et J12 (liste fermée) |
| HTML | a+b+c+d concaténés bien formés (pile vide) ; fenêtres bien formées |
| Glossaire | `glossary/j95.py` : 10 clés, toutes en ajout conditionnel (`_a`). Aucune collision dans `glossary/*.py` au moment de l’injection. SRLF est présente aussi dans `travail/R06/glossary/r06.py`, chargée après et non conditionnelle : l’entrée de R06 prévaudra, sans conséquence. Si R06 n’est pas injecté, celle de J95 s’applique |
| `build_medina.py J95` (copie superposée avec J95 enregistré, `covers` J95, J98, J99) | `J95 non couvertes: 0` ; Pareto calculés : 6 %, 18 %, 8 %, 9 %, 7 % et 6 % |
| Contrat Sciences (logique de `tests/audit_sciences.py`) | navigation complète ; Physiologie 443 mots, Biophysique 468, Anatomie 441, Anatomopathologie 411 ; une figure légendée et accessible par discipline ; les quatre liens présents |
| `build_front.py --fragment S02` (copie superposée) | construit : 6,03 Mo, compressé à 2,91 Mo |
| Chromium 1194, `#/entry/J95` | titre correct ; 48 fenêtres distinctes ouvertes dans les 4 onglets et les 4 disciplines, toutes avec contenu, sans « Fiche absente » ; 6 Pareto ouverts avec leur fraction ; aucune erreur JavaScript ni de console ; mobile 390 px sans défilement horizontal de page (scrollWidth = 390 dans les quatre onglets) ; rendus ordinateur et mobile vérifiés visuellement |
| `tools/capture_lecon.py` | `captures/j95-1-ouverture.png`, `captures/j95-2-explication.png`, `captures/captures.json` (statut : relu, injecté, non enregistré dans `chapters.json`) |

Le texte compte 13 311 mots hors références et SVG, contre 12 858 dans le brouillon selon la même mesure. La hausse vient des nuances de preuve (Kirmeier, Bluth, Young), des contre-indications de la trachéotomie, de la recommandation EBMT 2020 et de la limite d’accès à Canet. Le cours reste dans la cible de 11 000 à 15 000 mots.

## Réserves restantes (non bloquantes)

1. **ARISCAT** : les points proviennent d’une reproduction secondaire (Lee, 2025), recoupée par une seconde reproduction et par les classes de l’essai européen de Hemmes. Le texte intégral de Canet 2010 reste inaccessible.
2. **Aucune recommandation suisse spécifique** n’a été trouvée sur les complications pulmonaires postopératoires, la trachéotomie ou les sténoses. Les sources suisses sont deux revues de la Revue médicale suisse et deux séries zurichoises.
3. **Lectures limitées au résumé** pour plusieurs recommandations :
   - Société européenne d’anesthésiologie et ESICM 2020 ;
   - ERS 2022 ;
   - ESAIC 2023 ;
   - EACTS 2017 ;
   - ERS et EBMT 2024 ;
   - Société européenne de laryngologie 2015 ;
   - EBMT 2020 (détail lu dans Glanville).

   Les essais sont aussi lus en résumé, sauf Hemmes. Les lacunes sont nommées dans le cours : hémorragie massive par érosion artérielle, détail EACTS, détail ERS et EBMT 2024.
4. **Young 2019** est un consensus international d’experts, piloté par Duke University, avec des anesthésistes européens. Il est cité comme tel, et la ventilation protectrice s’appuie aussi sur Lagier et sur les essais européens.
5. **Usages hors indication**, signalés partout : méthylprednisolone préventive avant extubation, triamcinolone sous-muqueuse trachéale, budésonide inhalé après plastie.
6. **Hors champ, faute de source européenne lue pour l’adulte** : maladies bronchiques J98.0, calcifications et kystes J98.4, infection respiratoire non précisée J98.7. Les connectivites (J99.0 et J99.1) sont renvoyées à M06, M32 et J84.
7. **Médiastinite** : la conduite chirurgicale repose sur une série monocentrique (De Feo, 157 patients) et sur le résumé EACTS.
8. **Cas cliniques fictifs** ; l’évolution du cas récapitulatif est illustrative.
9. **Enregistrement non fait** : `chapters.json`, `organisation/*` et l’entrée de `tests/audit_sciences.py` n’ont pas été modifiés, comme demandé. J95, sans base Git, devra figurer parmi les nouvelles productions. Les contrôles ont été faits sur une copie superposée.

## Injection

- `chapters/J95/` : `J95_a.html`, `J95_b.html`, `J95_c.html`, `J95_d.html`, `J95_pop1.html`, `J95_pop2.html`.
- `glossary/j95.py` : glossaire de l’auteur, avec ajout conditionnel de toutes les clés.
- `livraisons/Livraison Claude/P-02-Pneumologie/travail/J95/captures/` : deux captures et `captures.json`.
- Aucune opération Git. Aucun autre cours, ni `chapters.json`, ni `organisation/*`, ni le brouillon de l’auteur n’ont été modifiés.

Entrée `chapters.json` proposée : `{"code": "J95", "covers": ["J95", "J98", "J99"], "title": "Complications respiratoires des actes médicaux et autres troubles respiratoires", "integrated": true}`.
