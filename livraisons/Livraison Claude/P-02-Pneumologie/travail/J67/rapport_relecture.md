# J67 — Pneumopathies d’hypersensibilité et maladies des poussières organiques (P-02-Pneumologie) — rapport de relecture différée

Auto-audit par Agent différé opus 5.5 · 09.10.2026 · cours unique couvrant J66 et J67 (CIM-10-GM 2024 ; code dans l’en-tête seulement).
Sources relues : `travail/J67/chapters/J67/` (6 fichiers), `travail/J67/glossary/j67.py`, `rapport_auteur.md`. Le brouillon de l’auteur reste intact dans ce dossier. La version relue est injectée dans `chapters/J67/` et `glossary/j67.py`.

**Cette relecture est une revue par IA. Elle ne vaut pas validation médicale humaine.** Aucun médecin n’a relu ce cours.

## Méthode

Deux passes successives et distinctes ont couvert les quatre dimensions de la section 13 de `LEADERSHIP_CLAUDE_2026-10-08.md`. La **passe 1** a relu les six fichiers en entier et confronté chaque chiffre, seuil et dose à la source primaire, téléchargée de nouveau par le relecteur. La **passe 2** a relu en entier le texte issu de la passe 1, sous forme extraite, puis corrigé les défauts restants. Ont suivi les contrôles techniques, l’injection et les captures.

Sources téléchargées indépendamment de l’auteur le 09.10.2026 :
- textes intégraux PMC par `efetch` (db=pmc) : S2k 2024/2025 (PMC12215178), Raghu 2020 (PMC7397797), Nafees 2023 (PMC9985716), Nosotti 2022 (PMC9008138), Shi 2010 AJRCCM (PMC2913234), Salisbury 2019 (PMC6514431, résumé structuré) ;
- résumés PubMed par `efetch` et métadonnées par `esummary` ;
- LAA et OLAA, état au 01.01.2026, en HTML depuis le dépôt de fichiers Fedlex (point SPARQL officiel) ;
- AIPS par `tools/swissmedic_fi.py` (AmiKo).

## Corrections de la passe 1

### Exactitude médicale et scientifique
| Point | Brouillon | Source lue | Correction |
|---|---|---|---|
| Antigène introuvable | « 30 à 50 % » des formes fibrosantes (îlots 5 et 13, quiz, Pareto) | S2k : « up to 50 % » des PHS chroniques (Raghu : jusqu’à 60 %) | « jusqu’à la moitié des formes chroniques » partout |
| Dépôt des particules | « Une particule de moins de 5 µm franchit les bronches et se dépose dans la bronchiole terminale et l’alvéole » (îlot 3, Anatomie, figure 2, Pareto) | Aucune source lue ne décrit le site de dépôt ; S2k : antigènes < 5 µm, inflammation bronchiolocentrique ; nodules centrolobulaires = bronchiolite inflammatoire | Mécanisme non sourcé retiré ; réécrit autour de la distribution bronchiolocentrique ; figure 2 et légende corrigées ; titre « Anatomie : le lobule et sa bronchiole » |
| Endotoxines des actinomycètes | « leurs protéines sensibilisent, leurs endotoxines intoxiquent » (Microbiologie) | S2k : actinomycètes à Gram positif ; endotoxines des Gram négatif et mycotoxines | Erreur corrigée : les endotoxines viennent des Gram négatif de la même poussière |
| Rapport de risque 0,18 | « L’éviction réduisait la mortalité » (îlot 8, fenêtre Éviction) | Gimenez 2018 : *amélioration* sous éviction associée à une mortalité moindre | Formulation exacte ; « étude brésilienne » précisée |
| LBA | « Indiqué si le diagnostic n’est pas acquis » ; « LBA et biopsie ne le sont que si… » | S2k R5 : LBA « shall be done » devant toute PID nouvelle suspecte de PHS | LBA recommandé devant toute PID nouvelle, superflu si les cinq critères non invasifs de la forme aiguë sont réunis |
| Couinements | « orientent spécifiquement vers une atteinte bronchiolaire » ; « la bronchiolite explique les couinements » | Raghu 2020 : signe fréquent des deux phénotypes, prédicteur potentiel ; mécanisme non décrit | Spécificité et mécanisme non sourcés retirés |
| Saison | « Le poumon de fermier survient en hiver » (Microbiologie) | S2k : incidence accrue dans les régions pluvieuses, surtout à la récolte | Corrigé |
| Tabac | « protège de la forme aiguë » | S2k : risque plus faible de PHS (sans précision de forme) | Corrigé (îlot 4, Immunologie) |
| Th1 et cytokines | « TNF-α et interféron gamma organisent des granulomes » | S2k : le TNF-α est nécessaire aux granulomes ; les cytokines Th1 (dont IFN-γ) orientent vers l’infiltrat CD8 | Corrigé (îlot 3, Immunologie) |
| Glucocorticoïdes et fibrose | « La fibrose ne cède qu’aux antifibrosants » ; « les glucocorticoïdes freinent la réponse Th1 » | S2k R11 ; De Sadeleer 2018 | Les antifibrosants freinent la progression sans régression ; mécanisme non sourcé remplacé par le résultat de Louvain |
| Sarcoïdose | « adénopathies » (différentiel) | Non lu ; S2k et Raghu : granulomes volumineux, confluents, le long des lymphatiques | Remplacé par la description sourcée |
| Asthme (différentiel) | « Obstruction réversible » (non sourcé) | S2k : hyperréactivité dans jusqu’à 50 % des PHS aiguës, à ne pas prendre pour un asthme | Reformulé |
| UIP dans la PHS | « Près de la moitié des PHS fibrosantes » | S2k : 46 % d’une série portugaise de 63 PHS | Effectif et contexte précisés |
| Auto-anticorps | « Anticorps antinucléaires… font croire à une connectivite » | S2k : FR positif → erreur vers PID de PR ; AAN chez 43–58 %, associés à une progression plus rapide | Corrigé |
| Culs-de-sac | « postérieurs » | S2k : culs-de-sac costodiaphragmatiques | Corrigé |
| Radiographie | « normale dans 20 % des formes aiguës » ; « méconnaît une fibrose débutante » | S2k : normale dans 20 % des cas ; TDM volumique devenue la référence | Corrigé ; clause non sourcée retirée |
| Azathioprine, contraception | « trois mois (hommes) ou six mois (femmes) » | AIPS Imurek (04.2026) : hommes et femmes, trois à six mois | Corrigé |
| Glucocorticoïdes, grossesse | « préférées » sans motif | AIPS Prednisone Streuli (06.2026) : préférées aux autres, surtout fluorés, passage placentaire le plus faible ; allaitement proscrit | Complété |
| Dose de prednisolone | « forme aiguë sévère » | S2k R10 : forme aiguë ou non fibrosante avec atteinte modérée à sévère | Corrigé (îlot 13, Pharmacologie, fenêtre) |
| Bagassose | « les mêmes espèces » | S2k, tableau 3 : T. sacchari et L. sacchari | Précisé |
| Exacerbation | « facteur de risque reconnu » | S2k : « recent data suggest » | Nuancé |
| Pronostic | Allèle MUC5B « aggrave le pronostic » ; lymphocytose « l’améliore » | S2k : lymphocytose → meilleur pronostic et meilleure réponse à l’immunosuppression | Complété ; doublon S2k/Salisbury retiré |
| Transplantation | « groupe de transplantation de la Société européenne de chirurgie thoracique », HR 0,25 attribué à Nosotti | Nosotti 2022 : ESTS Lung Transplantation Working Group ; HR 0,25 et récidive rare = S2k | Attribution corrigée |
| Nintédanib, sécurité | « transaminases chez jusqu’à 7,8 % » | AIPS Ofev (03.2025) : 7,8 % dans INBUILD ; lésions hépatiques graves parfois mortelles ; thromboses artérielles, perforations rares | Complété |
| Shanghai | « gain de 11,3 mL par an » | Shi 2010 AJRCCM : 11,3 mL par année écoulée sur la variation quinquennale du VEMS, 5,6 mL chez les ouvriers de la soie | Corrigé ; essai de Karachi chiffré (+1,3 point de VEMS en % prédit) |

### Sources et plan
- **Recommandation de 2020 (Raghu, ATS/JRS/Asociación Latinoamericana de Tórax).** Elle était présentée comme « internationale ». Aucune société européenne ne la cosigne : sa désignation est désormais exacte partout (« recommandation ATS/JRS de 2020 », nom complet à la première mention). Elle ne fonde aucune conduite : la S2k DGP/DGAKI 2024/2025 est la seule source de conduite (classification, critères, indications d’examens, traitements). Le texte de 2020 sert de source de définitions et de données (définition, grille TDM, seuils du LBA, niveaux de confiance présentés à titre de comparaison). La fenêtre de contentieux le dit explicitement, et la ligne « Cryobiopsie » y a été corrigée (2020 : aucune recommandation dans la forme non fibrosante, suggestion dans la forme fibrosante).
- **Maladie professionnelle.** La LAA a été relue (art. 1a, 4 et 9) : l’assurance obligatoire couvre les salariés ; l’agriculteur indépendant n’est couvert que s’il est assuré à titre facultatif. Ce point pratique a été ajouté à l’îlot 11 et à la fenêtre. La reconnaissance par la Suva au titre de l’art. 9, al. 1, est citée d’après la S2k.
- **Documents Suva.** Recherche du 09.10.2026 (suva.ch, recherche web) : aucun document Suva sur la PHS ou le poumon de fermier n’a pu être consulté. La lacune reste nommée.
- **Questionnaire suisse (Pohle 2023).** Le texte Karger reste inaccessible (403) ; seule la notice bibliographique a été vérifiée. La lacune reste nommée.
- Le lien Spagnolo 2025 (épidémiologie mondiale) a été remplacé à l’îlot 2 par Raghu 2020, qui porte réellement le chiffre « prévalence maximale après 65 ans ».
- Plan monographique respecté ; le code CIM n’apparaît que dans l’en-tête.

### Rédaction
Les phrases nominales des fenêtres (technique TDM, provocation, surveillance hépatique) ont été rendues complètes, comme les encadrés « Forme aiguë typique » et « Formes trompeuses ». Les doublons ont été resserrés : fenêtre byssinose (définition reprise de l’îlot 10), poumon de fermier (épidémiologie et essai finlandais), IgG chez les exposés sains (cité trois fois), seuils du LBA, posologie des glucocorticoïdes (quatre occurrences), piège IgG de l’onglet Examens. « Une emphysème », « La hypertension » et « transmise par un aérosol » ont été corrigés.

## Corrections de la passe 2
La relecture intégrale du texte corrigé a encore modifié les points suivants :
- titre et annonce de l’Anatomie, encore centrés sur le « trajet de la particule » ;
- doublon Treg dans l’Immunologie ;
- mécanisme de l’emphysème (Physiologie), aligné sur la S2k ;
- « guérit après éviction » nuancé en amélioration fonctionnelle (Histologie) ;
- poumon des bains bouillonnants : « éviction, éventuellement aidée de corticoïdes » ;
- Pareto « Notions » : dépôt particulaire retiré ;
- réponse du cas 3 (« qui guérit spontanément », non sourcé) ;
- îlot 13 : précision du délai (3 à 12 h observés, critère 4 à 8 h).

## Sources vérifiées (27 liens, contrôlés le 09.10.2026)

**PubMed (21), vérifiés par `esummary` : premier auteur, année et revue concordants.**
1731594 Kokkarinen 1992 Am Rev Respir Dis · 6861923 Mönkäre 1983 Eur J Respir Dis · 10086207 Christiani 1999 Am J Ind Med · 10086208 Vogelzang 1999 Am J Ind Med · 12842854 Lacasse 2003 AJRCCM · 20797932 Shi 2010 Environ Health Perspect · 23828161 Fernández Pérez 2013 Chest · 26010749 Tsutsui 2015 Ann Am Thorac Soc · 26489943 Er 2016 Int J Occup Med Environ Health · 26913451 Quirce 2016 Allergy (EAACI) · 28883091 Gimenez 2018 Thorax · 30577667 De Sadeleer 2018 J Clin Med · 32145830 Wells 2020 Lancet Respir Med · 33798455 Behr 2021 Lancet Respir Med · 35073782 Nafees 2022 Asia Pac J Public Health · 37088078 Pohle 2023 Respiration · 37857425 Nafees 2024 Eur Respir J · 38655831 Schumacher 2024 Ther Umsch ; et, par lien PMC : 39870058 Koschel 2025 Respiration (version allemande 39227017, Pneumologie 2024), 32706311 Raghu 2020 AJRCCM, 30243979 Salisbury 2019 Chest.

Liens HTTP : PMC 200 ; PubMed 203 (page servie par le mandataire) ou 429 (limitation de débit, PMID confirmés par `esummary`) ; Fedlex 200 ; swissmedicinfo.ch 200.

Mode de lecture par le relecteur :
- **texte intégral PMC** : Koschel (S2k), Raghu, Nafees 2023, Nosotti, Shi 2010 AJRCCM (passage cité) ;
- **résumé** : les autres ; Pohle 2023 : notice seulement.

**URL officielles (contenu lu)**
- LAA (RS 832.20), art. 1a, 4 et 9, et OLAA (RS 832.202), annexe 1, ch. 2, let. b, état au 01.01.2026 (Fedlex).
- AIPS via AmiKo (date de mise à jour lue sur la page) : Ofev® 7680653300011 (03.2025) ; Esbriet® 7680664220032 (08.2022) ; Imurek® 7680318870460 (04.2026) ; CellCept® Roche 7680533370011 (09.2025) ; Prednisone Streuli® 7680293490370 (06.2026).

Doses et contre-indications vérifiées mot à mot dans l’AIPS :
- **nintédanib** : PID fibrosantes chroniques à phénotype progressif ; 150 mg deux fois par jour, au plus 300 mg/j ; 100 mg deux fois par jour en cas d’effet indésirable ou de Child-Pugh A ; non recommandé en Child-Pugh B ou C ; contre-indiqué pendant la grossesse et en cas d’allergie à l’arachide ou au soja ; contraception jusqu’à 3 mois ; diarrhée 66,9 % contre 23,9 % ; inhibiteurs de la P-gp ;
- **pirfénidone** : FPI seule ; titration 267 → 534 → 801 mg trois fois par jour ; contre-indiquée avec la fluvoxamine (exposition ×4) et en insuffisance hépatique ou rénale sévère (< 30 mL/min) ; bilan hépatique mensuel 6 mois puis tous les 3 mois ; tabac −50 % ; photosensibilité ;
- **azathioprine** : 1 à 3 mg/kg/j (autres affections), paliers de 0,5 mg/kg ; formule sanguine hebdomadaire 8 semaines puis au moins tous les 3 mois ; allopurinol → quart de dose, décès rapportés ; TPMT, NUDT15 ; contraception 3 à 6 mois ;
- **mycophénolate** : transplantation seule ; 1 g deux fois par jour (rein) ; malformations 23 à 27 % contre environ 2 % ; neutropénie < 1,3 × 10³/µl ; surveillance hebdomadaire puis bimensuelle puis mensuelle ;
- **prednisone** : indication « états allergiques graves ou invalidants » (PHS non nommée) ; arrêt par paliers au-delà de 8 à 10 jours ; contre-indications du traitement prolongé ; grossesse et allaitement ; prednisolone préférée en cas d’affection hépatique.

## Contrôles techniques et rendu

| Contrôle | Résultat |
|---|---|
| Clés et gabarits | 53 `data-k` = 53 gabarits (47 fenêtres et 6 Pareto), préfixe `j67-` / `pareto-j67-` ; aucun identifiant dupliqué ; couvertures Pareto valides |
| Classes | toutes dans la liste fermée |
| HTML | a+b+c+d concaténés bien formés (pile vide) ; fenêtres bien formées |
| Glossaire | `glossary/j67.py` : ajouts conditionnels (`_a`). **S2k existait déjà** dans `glossary/t78.py` (non vu par l’auteur) : la clé n’écrase rien, et t78, chargé après, garde sa définition. **FFP2** est aussi défini conditionnellement par `glossary/r04.py`, injecté entre-temps. Les définitions de Th1, FFP2, S2k, LAA et OLAA sont génériques, sans fenêtre propre à J67, pour ne pas capter les autres cours (Th1 apparaît dans M31, S2k dans T78). STOP ne capte ni STOP-BANG (I10) ni STOPDAPT-2 (I21), grâce aux bornes lexicales et au tri par longueur ; le brouillon J69 définit aussi STOP sans garde : s’il est injecté, sa définition générique remplacera celle de J67 sans dommage |
| `build_medina.py J67` (copie superposée, J67 enregistré) | `J67 non couvertes: 0` ; M31, T78, I10, I21, R04 : 0 |
| Contrat Sciences (logique `tests/audit_sciences.py`) | navigation complète ; 5 disciplines de 370 à 422 mots ; une figure légendée et accessible chacune ; quatre liens présents |
| `build_front.py --fragment S02` (copie superposée) | 6,05 Mo, compressé à 2,92 Mo |
| Chromium 1194, `#/entry/J67` | titre correct ; 4 onglets non vides ; 53 fenêtres distinctes ouvertes (mots verts des 4 onglets, des 5 disciplines, toutes les pages du pager, 6 Pareto), aucune « Fiche absente » ; aucune erreur JavaScript ni de console ; mobile 390 px : `scrollWidth` = 390 |
| `tools/capture_lecon.py` | `captures/j67-1-ouverture.png`, `captures/j67-2-explication.png`, `captures.json` (statut : relu, injecté, non enregistré dans `chapters.json`) |
| Liens externes | 27 contrôlés (voir plus haut) |

Le texte compte 14 948 mots hors références et SVG, contre 14 581 dans le brouillon. Les ajouts sourcés (assurance LAA, sécurité du nintédanib, nuances de preuve, contentieux) ont été compensés par la suppression des doublons.

## Réserves restantes (non bloquantes)

1. **Hors indication suisse** : azathioprine, mycophénolate, pirfénidone et rituximab dans la PHS. Les glucocorticoïdes sont autorisés dans les « états allergiques graves », sans que la PHS soit nommée. Aucune dose de mycophénolate propre à la PHS n’a été trouvée : la dose de transplantation rénale est citée comme telle. Le cours le dit dans le tableau et dans la fenêtre.
2. **Aucune recommandation suisse** sur la PHS. La S2k allemande est la source de conduite. Le texte ATS/JRS/ALAT de 2020 ne sert que de données.
3. **Documents Suva non consultés** (procédure d’annonce, fiche poumon de fermier, principe STOP version Suva) et **questionnaire suisse (Pohle 2023)** lu au niveau de la notice seulement : lacunes nommées dans les fenêtres.
4. **Lectures limitées au résumé** : Lacasse, Kokkarinen, Mönkäre, De Sadeleer, Gimenez, Fernández Pérez, Tsutsui, Wells, Behr, Nafees 2022 et 2024, Shi 2010 EHP, Christiani, Er, Vogelzang, Quirce, Schumacher.
5. **Notions anatomiques générales** encore formulées sans citation mot à mot : le lobule secondaire « que bordent les septums interlobulaires » et la fonction normale (CVF, CPT et DLCO au-dessus de la LIN).
6. **Byssinose** : aucune recommandation européenne sur son traitement médicamenteux ; aucune donnée européenne récente sur la maladie du lin et la cannabinose (lacunes nommées).
7. **Enregistrement** : `chapters.json`, `organisation/*` et `tests/audit_sciences.py` n’ont pas été modifiés, comme demandé. Ce test exigera d’ajouter J67 à sa liste des nouvelles productions sans base Git.

## Injection

- `chapters/J67/` : `J67_a.html`, `J67_b.html`, `J67_c.html`, `J67_d.html`, `J67_pop1.html`, `J67_pop2.html`.
- `glossary/j67.py` : ajouts conditionnels, définitions génériques pour les clés partagées.
- `livraisons/Livraison Claude/P-02-Pneumologie/travail/J67/captures/` : deux captures et `captures.json`.
- Entrée proposée pour `chapters.json` : `{"code": "J67", "covers": ["J66", "J67"], "title": "Pneumopathies d’hypersensibilité et maladies des poussières organiques", "integrated": true}`.
- Aucune opération Git. Aucun autre cours, ni `chapters.json`, ni `organisation/*`, ni le brouillon de l’auteur n’ont été modifiés.
