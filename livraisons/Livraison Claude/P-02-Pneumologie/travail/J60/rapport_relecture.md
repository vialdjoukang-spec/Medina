# J60 — Pneumoconioses (P-02-Pneumologie) — rapport de relecture différée

Auto-audit par Agent différé opus 5.5 · 09.10.2026 · cours unique couvrant J60, J61, J62, J63, J64, J65 et J92 (CIM-10-GM 2024 ; codes dans l’en-tête seulement).
Sources relues : `travail/J60/chapters/J60/` (6 fichiers), `travail/J60/glossary/j60.py`, `rapport_auteur.md`. Le brouillon de l’auteur reste intact dans ce dossier. La version relue est injectée dans `chapters/J60/` et `glossary/j60.py`.

**Cette relecture est une revue par IA. Elle ne vaut pas validation médicale humaine.** Aucun médecin n’a relu ce cours.

## Méthode

Deux passes successives et distinctes ont couvert les quatre dimensions de la section 13 de `LEADERSHIP_CLAUDE_2026-10-08.md`. La **passe 1** a relu les six fichiers en entier et confronté chaque chiffre, seuil et dose à la source primaire, téléchargée de nouveau par le relecteur dans son propre dossier (et non dans celui de l’auteur). La **passe 2** a relu en entier le texte issu de la passe 1, sous forme extraite, puis corrigé les défauts restants. Ensuite sont venus les contrôles techniques et l’injection.

Téléchargements indépendants du 09.10.2026 :
- textes intégraux PMC par `efetch` (db=pmc) : AWMF 2026 (PMC13577655), Ferreiro 2025 (PMC12070196), Hoy 2022 (PMC9310854), Getahun 2015 (PMC4664608) ;
- résumés PubMed par `efetch` (15 PMID) ;
- PDF officiels : fiches Suva Silicose (12.2012), Amiante (10.2019), Bérylliose (09.2012) ; Explications VME/VBT (édition avril 2026) ; critères d’Helsinki (sjweh.fi) ; Tuberculose en Suisse V1.2024 ; Plan de vaccination suisse 2026 ;
- **liste des valeurs limites en vigueur de la Suva** : export Excel officiel de l’application `suva.ch/fr-ch/services/grenzwerte` (fichier `aktuelle-grenzwerte-2026-10-09.xlsx`) ;
- AIPS via AmiKo (`tools/swissmedic_fi.py`) : Ofev®, Rimactan®, Rifinah®, Prednisone Streuli®.

## Réserves de l’auteur tranchées

| Réserve | Décision du relecteur |
|---|---|
| 2. Valeur limite du quartz (fiche 2012) | **Levée.** La liste Suva en vigueur (export du 09.10.2026) donne pour le dioxyde de silicium cristallisé (quartz, cristobalite, tridymite) une VME de **0,15 mg/m³ (fraction alvéolaire)**, cancérogène C1A, toxicité critique silicose et cancer pulmonaire. Amiante 0,01 fibre/ml confirmé ; béryllium 0,0006 mg/m³ (inhalable) ajouté. Le paragraphe « valeur non vérifiée » est supprimé. La valeur européenne (0,1 mg/m³) reste attribuée à Hoy 2022, EUR-Lex étant toujours inaccessible. |
| 4. Corticoïdes de la bérylliose sans dose | **Précisée.** Aucune source ne fixe une dose propre à la bérylliose (lacune maintenue). L’AIPS de la prednisone (06.2026) prévoit, pour la sarcoïdose symptomatique, 15 à 30 mg/j au départ, dose minimale efficace, décroissance par paliers au-delà de 8 à 10 jours ; la transposition est présentée comme choix hors indication du centre spécialisé. Ajout des précautions AIPS : masquage des infections, réactivation tuberculeuse, freinage corticotrope au-delà de deux semaines. |
| 4. Hors indication (corticoïdes, rifampicine seule) | **Maintenus et signalés.** Rimactan® : « doit toujours être associé à d’autres antituberculeux » ; la monothérapie de quatre mois suit le guide suisse 2024. |
| 5. Isoniazide sans AIPS | **Partiellement levée.** La préparation simple n’a toujours pas de texte AmiKo ; l’AIPS de Rifinah® (rifampicine-isoniazide, 02.2026) a été lue : inhibition du métabolisme de la phénytoïne, de la carbamazépine, de la primidone et de l’acide valproïque ; polynévrite dans 20 % des cas sans pyridoxine, prévenue par 10 mg/j ; hépatite plus fréquente avec l’âge (0,8–1,9 %) et avec la rifampicine (2,7 %). Doses : tableau OMS du guide suisse. |
| 3. Durée de la silicotuberculose (guideline allemande 2022) | **Complétée par des sources suisses.** Suva 2012 : « traitement prolongé, risque élevé de récidive ». Guide suisse 2024 : pas de schéma propre à la silicose, mais prolongation à 9 mois en cas de maladie cavitaire à culture positive après la phase intensive. La recommandation allemande (8–12 mois) reste citée via l’AWMF ; décision avec un spécialiste. |
| Glossaire (BIT, EFA, NLST, noms d’auteurs) | **Une collision corrigée.** `AWMF` existe déjà dans `glossary/t78.py` (format liste de tuples, non détecté par l’auteur) et était écrasée au chargement : la clé est retirée de `j60.py`. Les dix autres clés (BIT, ICOERD, IGRA, EFA, NLST, HLA-DPB1, Marchand-Adam, Mora-Cuesta, Müller-Quernheim, Vu-Duc) sont absentes de `glossary/*.py` et des glossaires de travail, et n’apparaissent dans aucun autre cours injecté (aucun faux positif). Ajout conditionnel `_a` : aucune clé existante n’est jamais écrasée. |
| 10. Volume | Voir « Volume ». |

## Corrections de la passe 1

### Exactitude médicale et sources
| Point | Brouillon | Source lue | Correction |
|---|---|---|---|
| Piège bérylliose/sarcoïdose | « Cohorte européenne », « souvent liée à un laboratoire dentaire (Müller-Quernheim) » | Résumé Müller-Quernheim 2006 (Fribourg ; 34/84 ; retard médian 3 ans) ; fiche Suva bérylliose (laboratoires dentaires) | Étude prospective allemande, retard médian de 3 ans ; laboratoires dentaires attribués à la Suva |
| Examen (îlot 6) | Mesure de SpO₂ à l’effort justifiée par un mécanisme non sourcé | Suva (dyspnée d’effort = limitation de la diffusion) ; AWMF (gazométrie repos/effort, ergospirométrie privilégiée) | Reformulé et sourcé |
| Silicoprotéinose | « Opacités qui simulent un œdème » ; mécanisme « macrophages qui ne dégradent plus le surfactant » | Suva 2012 (œdème ou miliaire, décès possible en quelques mois) ; AWMF (apoptose, recyclage, accumulation) | Corrigé ; infections opportunistes alignées sur l’AWMF (nocardia, mycobactéries, CMV, aspergillus, cryptocoque, pneumocystis) |
| Silicotuberculose | « La réactivation en est une source fréquente » | AWMF : la réactivation « peut aussi » être en cause | Nuancé |
| Tabac et amiante | Effet « plus qu’additif » | Suva 2019 : suradditif, moins fort qu’on ne le supposait | Nuance ajoutée |
| Cancer de l’ovaire | « Reconnu comme causé par l’amiante » | Helsinki 2014 (causé, CIRC) ; Suva 2019 (pas de doublement démontré, appréciation au cas par cas) | Les deux positions exposées (îlot 12, fenêtre Helsinki) |
| Affiliation assureur | « Lors de l’exposition » | Suva : assureur « au moment de l’atteinte » | Corrigé |
| Amiante dans les bâtiments | « Centaines de milliers de bâtiments » (non retrouvé) | Suva 2019 (rénovation, démolition, entretien, déchets) | Chiffre retiré |
| Rifampicine | « Résistance en une seule étape » | AIPS Rimactan : résistance pouvant se développer rapidement | Corrigé |
| Interaction rifampicine-nintédanib | « Efficacité antifibrosante compromise » | AIPS Ofev : AUC −50,3 %, Cmax −60,3 %, comédication peu inductrice à envisager | Formulation factuelle |
| Marqueurs du mésothéliome | « Ni sensibles ni spécifiques assez » | Kraus 2021 (recherche seulement) ; Suva 2019 (sans intérêt tant qu’aucun traitement curatif) | Corrigé, références ajoutées |
| Aluminose (lacune) | Lacune totale | AWMF (granulomes, protéinose induite par l’aluminium) ; Nemery 1990 (fibrose occasionnelle, médiation cellulaire) | Lacune réduite, nommée |
| Série britannique pierre artificielle | Titre seul | Résumé Feary 2024 (8 hommes, âge médian 34 ans, 2 bilans de transplantation, imitation de sarcoïdose) | Données ajoutées |
| Cœur pulmonaire | « Impose le bilan d’une HTP » (non sourcé) | AWMF (échocardiographie ; cathétérisme dans des cas choisis) | Sourcé |
| Contentieux tuberculose | « Le guide laisse le clinicien décider avec le patient » (phrase relative aux immunosuppresseurs) | Guide 2024, ch. 4.2 | Arbitrage reformulé et explicitement présenté comme déduction du cours |
| Vaccination | — | Plan 2026 (dose élevée dès 65 ans avec facteur de risque, dès 75 ans) | Ajouté |
| Pyridoxine sous isoniazide | Absente | Guide 2024 (grossesse) ; AIPS Rifinah | Ajoutée (tableau des doses, fenêtres) |
| BeLPT à Lausanne | Présent | Fiche Suva **2012** | Daté |

### Rédaction
Phrases corrigées : « il est gouverné » (sujet ambigu), « Seule la soustraction … et la prévention … modifient » (accord), « Il programme » (sujet ambigu), table « obligatoire si symptômes » ; phrases nominales des fenêtres Rifampicine, Isoniazide, Nintédanib, TDM et EFR réécrites en phrases complètes ; « Science → clinique », « Science → traitement » (physiologie et immunologie) réécrits pour éviter un mécanisme non sourcé et une contradiction avec le nintédanib.

## Corrections de la passe 2
- îlot 3 : accord « Seules la soustraction … et la prévention … » ;
- îlot 10 : affiliation « au moment de l’atteinte » ; texte de lecture du tableau et piège resserrés ;
- îlot 12 : sujet du cas récapitulatif explicité ; critères du dépistage TDM rapportés aux vingt paquets-années du patient ;
- Examens 1 : « cultures si symptômes ou image suspecte » ;
- Immunologie, Science → traitement : cohérence avec l’antifibrosant ;
- Pharmacologie 3 : interaction nintédanib reformulée ; phrase des antituberculeux scindée ;
- terme « vitamine B6 » remplacé par « pyridoxine » (abréviation non couverte par le glossaire) ;
- resserrement des fenêtres redondantes (asbestose, nodule silicotique, mésothéliome, IGRA, silicotuberculose, formes de silicose, TDM, EFR, nintédanib) et de l’îlot 6.

## Sources vérifiées (31 liens, contrôlés le 09.10.2026)

**PubMed (17 PMID), vérifiés par `esummary` (premier auteur, année, revue concordants)** : 10510836 Vu-Duc 1999 · 16540500 Müller-Quernheim 2006 · 18757698 Marchand-Adam 2008 · 20155272 Marchiori 2010 · 2178966 Nemery 1990 · 26152561 Cosgrove 2015 · 28882991 Hoy 2018 · 30292280 Takahashi 2018 · 32145830 Wells 2020 · 33728629 Kraus 2021 · 39107111 Howlett 2024 · 39107113 Feary 2024 · 39438781 Fortarezza 2025 · 40815182 Moriyama 2025 · 41672090 Mora-Cuesta 2026 · 26405286 Getahun 2015 · 25299403 Wolff 2015. Les pages PubMed répondent 203 ou 429 (limitation du proxy) ; leur existence est confirmée par `esummary`.

Mode de lecture : **texte intégral** pour AWMF 2026, Ferreiro 2025, Hoy 2022, Getahun 2015 (résumé et texte), critères d’Helsinki (PDF) ; **résumés** pour les autres.

**URL officielles (HTTP 200, contenu lu)** : fiches Suva silicose, amiante et bérylliose ; Suva Medical 2020 ; Suva « L’amiante rend malade » ; Suva « La silicose » ; Suva liste des valeurs limites (application et export Excel) ; Suva Explications VME (avril 2026) ; OFSP Plan de vaccination 2026 ; Tuberculose en Suisse V1.2024 ; doi Helsinki ; PMC (4) ; swissmedicinfo.

**AIPS (AmiKo, dates de mise à jour lues)** : Ofev® 03.2025 ; Rimactan® 10.2023 ; Rifinah® 02.2026 ; Prednisone Streuli® 06.2026. Vérifié mot à mot : nintédanib 150 mg ×2/j au repas, max 300 mg/j, 100 mg ×2/j (effets indésirables, Child-Pugh A), non recommandé Child-Pugh B/C, non étudié ClCr < 30, arrêt > 5 × LSN, diarrhée 66,9 % contre 23,9 % (INBUILD), différence de déclin de la CVF 107 mL, contre-indications grossesse, arachide, soja, contraception 3 mois ; rifampicine 10 (8–12) mg/kg, max 600 mg, à jeun, contre-indiquée ClCr < 25, cirrhose, porphyrie, contraception non hormonale.

Aucune recommandation américaine ne fonde une conduite. NLST, INBUILD et les séries publiées sont cités comme données ; les recommandations OMS (Eur Respir J) ne servent qu’au contentieux, tranché par le guide suisse 2024.

## Contrôles techniques et rendu

| Contrôle | Résultat |
|---|---|
| Clés et gabarits | 53 `data-k` = 53 gabarits (47 fenêtres et 6 Pareto) ; aucun identifiant dupliqué ; préfixe `j60-` ; ancres et couvertures Pareto valides |
| Classes | liste fermée habituelle (`alert`, `key`, `trap`, `t`, `w`, `quiz`, `fb`, `lab`, `src`, `sci`…) |
| HTML | a+b+c+d concaténés et fenêtres bien formés (pile vide, 0 erreur) |
| Glossaire | `glossary/j60.py` : 10 clés en ajout conditionnel ; AWMF retirée (définie par `t78.py`) ; aucune collision avec `glossary/*.py` ni avec les glossaires de travail (revérifié en fin de relecture) |
| `build_medina.py J60` (copie superposée avec J60 enregistré) | `J60 non couvertes: 0` |
| Contrat Sciences (logique de `tests/audit_sciences.py`) | navigation complète ; 4 disciplines de 404 à 437 mots ; 1 figure légendée et accessible chacune ; les 4 liens présents |
| `build_front.py --fragment S02` (copie superposée) | 6,8 Mo, compressé à 3,2 Mo ; cours classé sous « Maladies du poumon dues à des agents externes » |
| Chromium 1194, `#/entry/J60` | titre correct ; 4 onglets ; 53 mots verts et boutons Pareto distincts cliqués dans les 4 onglets, les 4 disciplines et toutes les pages du pager, plus 2 mots imbriqués dans des fenêtres ; aucune « Fiche absente », aucune fenêtre vide ; **aucune erreur JavaScript ni de console** ; mobile 390 px : `scrollWidth` = 390 sur les 4 onglets |
| `tools/capture_lecon.py` | `captures/j60-1-ouverture.png`, `captures/j60-2-explication.png`, `captures.json` (statut : relu, injecté, non enregistré dans `chapters.json`) |

## Volume

15 360 mots hors références et SVG (16 840 avec références), contre 14 750 hors références dans le brouillon. La hausse (+610) vient des sources suisses ajoutées : liste VME en vigueur, durées de la silicotuberculose (Suva, guide suisse), AIPS Rifinah et prednisone, nuances Suva/Helsinki ; les fenêtres redondantes ont été resserrées. Le cours couvre sept catégories (silicose et ses quatre formes, pneumoconiose des mineurs, asbestose, atteintes pleurales bénignes, bérylliose, métaux durs, sidérose, talcose, aluminose) : un dépassement de 2 % de la cible indicative est jugé préférable à la perte d’une information sourcée.

## Réserves restantes (non bloquantes)

1. **Aucune validation médicale humaine.**
2. **Fiches Suva anciennes** (silicose et bérylliose 2012, amiante 2019) : versions en ligne au 09.10.2026 ; la VME du quartz est désormais confirmée par la liste en vigueur.
3. **Hors indication suisse** : corticoïdes dans la bérylliose (sans dose propre dans les sources) ; rifampicine en monothérapie préventive (guide national).
4. **Isoniazide** : AIPS de la préparation simple sans texte ; données tirées du guide suisse et de l’AIPS Rifinah® (association).
5. **Valeur européenne de 0,1 mg/m³** : citée via Hoy 2022 ; directive 2017/2398 non lue (EUR-Lex inaccessible).
6. **Résumés seulement** pour Vu-Duc, Müller-Quernheim, Marchand-Adam, Nemery, Cosgrove, Takahashi, Marchiori, Hoy 2018, Howlett, Feary, Fortarezza, Moriyama, Mora-Cuesta, Wells, Kraus (AWMF amiante 2020 non lue en texte intégral).
7. **Intervalle de confiance du risque de tuberculose** : AWMF (2,88–5,88) et Hoy (2,88–5,58) divergent ; seul le risque relatif de 4,01 est donné.
8. **Notions physiologiques générales** (compliance, résistance, DLCO) formulées sans citation mot à mot ; signes auscultatoires de l’asbestose non décrits faute de source.
9. **Fiche Suva amiante** : seuil de 1000 corps asbestosiques « par gramme de tissu humide » (Suva) contre « sec » (Helsinki) ; le cours suit Helsinki, source primaire du seuil.
10. **Graphitose, stannose** : non traitées faute de source lue (la liste VME mentionne le graphite naturel, 3 mg/m³, sans donnée clinique).
11. **Enregistrement** : `chapters.json` et `organisation/*` non modifiés, comme demandé. À l’enregistrement, `tests/audit_sciences.py` devra ajouter J60 à la liste des nouvelles productions sans base Git. Entrée proposée : `{"code": "J60", "covers": ["J60","J61","J62","J63","J64","J65","J92"], "integrated": true, "title": "Pneumoconioses et plaques pleurales"}`.

## Injection

- `chapters/J60/` : `J60_a.html`, `J60_b.html`, `J60_c.html`, `J60_d.html`, `J60_pop1.html`, `J60_pop2.html`.
- `glossary/j60.py` : ajout conditionnel, sans AWMF.
- `livraisons/Livraison Claude/P-02-Pneumologie/travail/J60/captures/` : deux captures et `captures.json`.
- Aucune opération Git. Aucun autre cours, ni `chapters.json`, ni `organisation/*`, ni le brouillon de l’auteur n’ont été modifiés.
