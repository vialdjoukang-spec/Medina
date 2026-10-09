# J81 — Œdème pulmonaire non cardiogénique (P-02-Pneumologie) — rapport de relecture différée

Auto-audit par Agent différé opus 5.5 · 09.10.2026 · cours unique couvrant J81 (CIM-10-GM 2024 ; code dans l’en-tête seulement).
Sources relues : `travail/J81/chapters/J81/` (6 fichiers), `travail/J81/glossary/j81.py`, `rapport_auteur.md`. Le brouillon de l’auteur reste intact dans ce dossier. La version relue est injectée dans `chapters/J81/` et `glossary/j81.py`.

**Cette relecture est une revue par IA. Elle ne vaut pas validation médicale humaine.** Aucun médecin n’a relu ce cours.

## Méthode

Deux passes successives et distinctes ont couvert les quatre dimensions de la section 13 de `LEADERSHIP_CLAUDE_2026-10-08.md`. La **passe 1** a relu les six fichiers en entier. Elle a confronté chaque chiffre, seuil et dose à la source primaire, téléchargée de nouveau par le relecteur, puis corrigé et renforcé le texte. La **passe 2** a relu en entier le texte issu de la passe 1, sous forme extraite, et corrigé les défauts restants. Ensuite sont venus les contrôles techniques et l’injection.

Les sources ont été téléchargées indépendamment de l’auteur le 09.10.2026 :
- textes intégraux PMC par `efetch` (db=pmc) ;
- résumés PubMed par `efetch` ;
- PDF officiels (UIAA, ISBT, Swissmedic) ;
- AIPS AmiKo en HTML.

## Corrections de la passe 1

### Exactitude médicale et scientifique
| Point | Brouillon | Source lue | Correction |
|---|---|---|---|
| Interaction tadalafil-nifédipine | « Ne s’associe pas à la nifédipine » (alerte, À retenir, Pareto, fenêtre) | AIPS tadalafil Spirig HC : avec les antihypertenseurs, dont l’amlodipine, aucun effet cliniquement significatif jusqu’à 10 mg ; il faut avertir le patient du risque de baisse tensionnelle | Interdiction non sourcée retirée ; mise en garde de l’AIPS reprise |
| Traitement du TRALI | « Se traite comme un SDRA » (sans source : Vlaar 2019 ne traite pas du traitement) | ESICM 2023, recommandation 5.1 | Aucun traitement spécifique ; soutien du SDRA avec petits volumes courants de 4 à 8 mL/kg de poids prédit (recommandation forte) |
| Urgence hypoxémique | « Prépare une ventilation non invasive » | ESICM 2023, recommandations 3.1 et 4.1 | Oxygénothérapie nasale à haut débit plutôt qu’oxygène conventionnel hors œdème cardiogénique (forte, niveau modéré) ; aucune recommandation pour ou contre la ventilation non invasive |
| Cathéter artériel pulmonaire | « N’a pas amélioré le devenir » (non sourcé) | Komiya 2017 (PMC6389074) | « Invasif, coûteux, rarement employé, n’aide pas au diagnostic » ; consensus 2019 : évaluation objective, d’abord échocardiographique |
| Examen de référence (onglet Examens) | Mesure invasive présentée comme référence | Komiya 2017 | **Absence de référence objective nommée** (pas de gold standard) ; aucun marqueur de haute qualité |
| Nifédipine dans l’OPHA | « Lorsque l’oxygène manque ou que la descente est impossible » | UIAA n° 2 v3.3 ; Luks 2017 (PMC9488514) | Divergence explicitée. UIAA : traitement d’urgence d’emblée, 20 mg à libération prolongée, effet en 10 à 15 min, à répéter si aggravation. Luks : si la descente est impossible, 30 mg toutes les 12 h |
| Dexaméthasone, œdème cérébral de haute altitude | UIAA seule | UIAA (8 mg puis 8 mg/6 h) ; Luks (8 mg puis 4 mg/6 h) | Deux schémas présentés avec leur source |
| Rupture de contrainte | « Hémorragie et albumine corrélées à la pression systolique » (absent du résumé lu ; JAMA inaccessible) | Swenson 2002, résumé | Remplacé : pression artérielle pulmonaire systolique de 66 contre 37 mm Hg ; cytokines non élevées |
| TRALI, second coup | « Médiateurs des produits stockés » rangés parmi les seconds coups | Vlaar 2019 (PMC6850655) | Corrigé : les surnageants stockés sont inflammatoires et peuvent fournir le **premier** coup |
| Acétazolamide et OPHA | « Effet plausible, non étudié » (non sourcé) | Luks 2017, tableau 2 | « Luks ne le compte pas parmi les médicaments de prévention de l’OPHA » |
| Neurogénique | « Sidération → soutien inotrope » ; « le remplissage aggrave… » | Davison 2012 (PMC3681357) | Implication sur le remplissage et le choix des agents inotropes ou vasoactifs ; remplissage abondant en neuroréanimation : surcharge et diagnostic différentiel ; Davison propose un essai d’α-bloquant si la pression le permet, sans preuve |
| Pression négative | Diurétique et pression positive présentés comme établis | Bhaskar 2011 (PMC3168351) | Rôle propre non démontré ; résolution généralement < 24 h ; diurétique sauf hypovolémie ou choc |
| TACO grave (Suisse) | « Classé grave chez 8 des 37 » | Swissmedic HV 2024, tableaux 6 et 9 | « 8 des 37 ont engagé le pronostic vital » (grade 3) ; reformulation de la comparaison avec les réactions allergiques |
| OPHA à 5500 m | « Montée en avion porte l’incidence de 2,5 à 15,5 % » | Luks 2017 | Précisé : marche de 4 à 6 jours (2,5 %) contre transport aérien (15,5 %) |
| Sexe et OPHA | Chiffres cas-témoins seuls | Pichler Hefti 2023, résumé | Étude rétrospective unique ; différence « possible » selon les auteurs |
| Peptides en réanimation | « Presque toujours élevés » | Vlaar 2019 | « Toujours élevés » selon le consensus (vasoconstriction hypoxique) |
| Anaphylaxie et contamination | « À écarter systématiquement » | Vlaar 2019 | « À envisager dans tout œdème post-transfusionnel » |
| Délai du TACO | 12 h seul | ISBT 2018 et Vlaar 2019 | Contentieux exposé dans la fenêtre TACO. ISBT (référence de l’hémovigilance suisse) : 12 h. Consensus TRALI : 6 h, puis dyspnée associée à la transfusion |
| TACO, critères | — | ISBT 2018 | Ajouts : définition de surveillance, non outil de décision immédiate ; hypotension possible comme signe d’appel |
| Clairance alvéolaire | 13 % contre 6 % par heure, sans effectifs | Ware 2001, résumé | Séries précisées : 65 œdèmes hydrostatiques contre 79 lésions pulmonaires aiguës |
| Immersion | Hémoptysie sans chiffre | Grünig 2017 (PMC5583207) | 68 % des 38 cas |
| Notions générales signalées par l’auteur (réserve 7) | Correction barométrique, caisson, pression expiratoire positive, crépitants | Luks 2017 (baisse de pression partielle d’O₂ avec la pression barométrique) ; ESICM 2023 (PEP : réduire le poumon non aéré) ; ISBT (crépitants, signe d’œdème) | Rattachées à une source ; formulations alignées |

### Sources et plan
- Le lien BfArM (bloc J80-J84) a été retiré de l’îlot 1 : le code CIM n’est pas un contenu enseigné (section 11, règle 4) et n’apparaît que dans l’en-tête.
- ESICM 2023 et Bhaskar 2011 ont été ajoutés aux références des îlots 8 et 9 ; Matthay 2014 à l’îlot Examens 3 ; Vlaar 2019 à la fenêtre TACO ; l’ISBT à la fenêtre Crépitants.
- Aucune recommandation américaine ne fonde une conduite. Les essais nord-américains (Feller-Kopman, Lentz, Sporer) et les revues (Bhattacharya, Ware et Matthay) sont cités comme données. La définition de Berlin est une initiative de l’ESICM.

### Rédaction
Phrases ternes ou imprécises reprises :
- « l’œdème du cardiaque » ;
- « frontières poreuses » (image) ;
- « cœur gauche normal ou insuffisant pour expliquer » ;
- redondance sur la saturation ;
- clause non sourcée sur les dons futurs ;
- « la vigilance au lit du patient en est la condition ».

Ont aussi été corrigés : l’exemple TRALI de type I, où le critère du type II (« patient stable ») avait été employé, et la conclusion de la fenêtre « Oxygène et descente », qui contredisait l’UIAA.

## Corrections de la passe 2
La relecture intégrale du texte corrigé a encore modifié les points suivants :
- tableau Pharmacologie (place de la nifédipine) ;
- formulation « peuvent accroître » pour les inhibiteurs du CYP3A4 (AIPS) ;
- ligne « Remplissage abondant non guidé » étendue au TRALI (bilan positif, facteur de risque selon Vlaar) ;
- fenêtre TRALI (dyspnée associée à la transfusion « si elle paraît liée ») ;
- résultat des anticorps antileucocytaires : délai « des semaines » non sourcé, retiré ;
- échographie : « monocentrique » retiré, au profit de « petite série de 58 patients » ;
- nifédipine de classe des 1,4-dihydropyridines (AIPS) ;
- Pareto « Urgences et traitements » complété par l’oxygénothérapie à haut débit.

## Sources vérifiées (39 liens, tous contrôlés le 09.10.2026)

**PubMed (29), vérifiés par `esummary` : premier auteur, année et revue concordants.**
11319198 Maggiorini 2001 Circulation · 11371404 Ware 2001 AJRCCM · 11713145 Sporer 2001 Chest · 11980523 Swenson 2002 JAMA · 12023995 Sartori 2002 NEJM · 15703168 Bärtsch 2005 J Appl Physiol · 17015867 Maggiorini 2006 Ann Intern Med · 17954079 Feller-Kopman 2007 Ann Thorac Surg · 18442425 Copetti 2008 Cardiovasc Ultrasound · 1922223 Bärtsch 1991 NEJM · 21957413 Bhaskar 2011 Saudi J Anaesth · 22429697 Davison 2012 Crit Care · 22797452 Ranieri (ARDS Definition Task Force) 2012 JAMA · 24881936 Matthay 2014 AJRCCM · 24993976 Gargani 2014 Cardiovasc Ultrasound · 2573760 Oelz 1989 Lancet · 27063348 Bhattacharya 2016 Chest · 28143879 Luks 2017 Eur Respir Rev · 28841896 Komiya 2017 Crit Care · 28912730 Grünig 2017 Front Physiol · 30772283 Lentz 2019 Lancet Respir Med · 30993745 Vlaar 2019 Transfusion · 31080132 Wiersum-Osselton 2019 Lancet Haematol · 31222929 Mueller 2019 Eur J Heart Fail · 34987415 Beretta 2021 Front Physiol · 37326646 Grasselli 2023 Intensive Care Med · 37906126 Pichler Hefti 2023 High Alt Med Biol · 39675743 Banham 2024 Diving Hyperb Med · 8592525 Scherrer 1996 NEJM.

Mode de lecture par le relecteur :
- **texte intégral PMC** : Luks (PMC9488514), Vlaar (PMC6850655), Beretta (PMC8720972), Komiya (PMC6389074), Davison (PMC3681357), Bhaskar (PMC3168351), Grünig (PMC5583207), Gargani (PMC4098927), Copetti (PMC2386861), Grasselli (PMC10354163) ;
- **résumé** : les autres.

**URL officielles (HTTP 200, contenu lu)**
- UIAA MedCom n° 2 v3.3 (2012, mise à jour 2024), PDF de 19 pages lu en entier : https://theuiaa.org/documents/mountainmedicine/English_UIAA_MedCom_Rec_No_2_AMS_HAPE_HACE_2012_V3.3.pdf
- ISBT/IHN/AABB, définition du TACO 2018 (version web de mars 2019), PDF intégral : https://isbtweb.org/asset/19FED2C2%2DE257%2D42F5%2D9B2C2B51DF1F87D4
- Swissmedic, Hémovigilance, rapport annuel 2024, PDF intégral (chapitres 2-3) : https://www.swissmedic.ch/dam/swissmedic/fr/dokumente/marktueberwachung/haemovigilance/haemovigilance_jahresbericht_2024.pdf.download.pdf/H%C3%A9movigilance%20Rapport%20annuel%202024.pdf
- AIPS via AmiKo (produit et date de mise à jour confirmés sur la page) :
  - Nifedipin-Mepha 20 retard, 7680528960104, 01.2026 ;
  - Fortecortin® comprimés, 7680486700323, 01.2022 ;
  - Lasix® solution injectable, 7680306300177, 03.2025 ;
  - Diamox®, 7680211910195, 07.2026 ;
  - Tadalafil Spirig HC, 7680676250126, 11.2025 ;
  - Naloxon OrPha, 7680569520015, 07.2026 ;
  - Serevent, 7680530210181, 07.2021.

Doses et contre-indications vérifiées mot à mot dans l’AIPS :
- **nifédipine** : 20 mg deux fois par jour, au plus 40 mg deux fois par jour, intervalle d’au moins 4 h, comprimés ni mâchés ni fractionnés. Contre-indiquée pendant les 20 premières semaines de grossesse, l’allaitement, en cas de choc, d’angor instable ou d’infarctus de moins de 4 semaines, et avec la rifampicine. Prudence sous 90 mm Hg et chez le sujet de plus de 65 ans ;
- **furosémide** : 40 mg par voie intraveineuse dans l’œdème pulmonaire aigu, puis 20 à 40 mg à 20 min ; au plus 4 mg/min ; voie intramusculaire non indiquée ; contre-indications ;
- **acétazolamide** : 250 mg deux fois par jour pendant au moins 4 jours, dès la veille ; œdème non cardiogénique même après une dose unique ; grossesse ; contre-indications ;
- **naloxone** : 0,4 à 2 mg, toutes les 2 à 3 min, seuil de 10 mg ; œdème pulmonaire très rare ;
- **salmétérol** : 50 µg deux fois par jour, au plus 100 µg deux fois par jour ; tremblements et tachycardie plus fréquents au-delà de 50 µg deux fois par jour ;
- **tadalafil** : au plus 20 mg par jour ; contre-indiqué avec les nitrés, la molsidomine, les stimulateurs de la guanylate cyclase et en cas de Child-Pugh C ;
- **dexaméthasone** : comprimés de 4 mg ; œdème cérébral parmi les indications ; freinage corticotrope au-delà de 2 semaines.

## Contrôles techniques et rendu

| Contrôle | Résultat |
|---|---|
| Clés et gabarits | 46 `data-k` = 46 gabarits (40 fenêtres et 6 Pareto) ; aucun identifiant dupliqué ; ancres et couvertures Pareto valides |
| Classes | toutes dans la liste fermée de `CHAPTER_SPEC.md` |
| HTML | a+b+c+d concaténés bien formés (pile vide) ; fenêtres bien formées |
| Glossaire | `glossary/j81.py` : ajout conditionnel (`_a`). `glossary/j80.py`, chargé avant, définit déjà TRALI et TACO : ces clés ne sont pas écrasées et pointent vers `j80-trali`. OPHA, ISBT, UIAA et HNA sont nouveaux, sans collision |
| `build_medina.py J81` (copie superposée avec J81 enregistré) | `J81 non couvertes: 0` ; Pareto calculés : 4 %, 9 %, 6 %, 6 %, 8 % et 6 % |
| `build_front.py --fragment S02` (copie superposée) | construit : 4,67 Mo, compressé à 2,45 Mo |
| Chromium 1194, `#/entry/J81` | titre correct ; 4 onglets non vides ; 40 mots verts distincts cliqués dans les 4 onglets, les 5 disciplines et toutes les pages du pager, tous ouverts avec contenu ; 6 Pareto ouverts ; aucune erreur JavaScript ni de console ; mobile 390 px sans défilement horizontal |
| `tools/capture_lecon.py` | `captures/j81-1-ouverture.png`, `captures/j81-2-explication.png` (statut : relu, injecté, non enregistré dans `chapters.json`) |

Le texte compte 14 972 mots hors références et SVG, contre 14 477 dans le brouillon. La légère hausse vient des sources ajoutées : ESICM, divergences UIAA/Luks et ISBT/Vlaar, nuances de preuve. Le cours couvre huit entités.

## Réserves restantes (non bloquantes)

1. **Aucune recommandation suisse sur l’OPHA** n’a été trouvée. La conduite repose sur l’UIAA (siège à Berne), la revue européenne de Luks (ERS) et les essais suisses. Tous les médicaments de l’OPHA sont hors indication en Suisse. La dose de salmétérol de prévention dépasse le maximum de l’AIPS, ce que le cours signale.
2. **Lectures limitées au résumé** pour Swenson 2002, Sartori 2002, Bärtsch 1991 et 2005, Maggiorini 2001 et 2006, Scherrer 1996, Oelz 1989, Ware 2001, Matthay 2014, Sporer 2001, Feller-Kopman 2007, Lentz 2019, Bhattacharya 2016, Mueller 2019, Ranieri 2012, Wiersum-Osselton 2019, Pichler Hefti 2023 et Banham 2024. Les facteurs de risque du SDRA sont contrôlés sur la liste de Berlin reproduite par Vlaar (tableau 4).
3. **Œdème de réexpansion** : uniquement deux études nord-américaines, faute de source suisse ou européenne lue (limite nommée dans la fenêtre).
4. **Œdème neurogénique** : critères proposés par des auteurs (Davison 2012), non officiels.
5. **Notions physiologiques générales** encore formulées sans citation mot à mot : mécanisme de l’hypoxémie par alvéoles non aérées ; formation de la mousse de l’expectoration.
6. **Glossaire TRALI et TACO** : les définitions affichées sont celles de `j80.py` (fenêtre `j80-trali`). Si J80 n’était pas enregistré, cette fenêtre manquerait. Il faudrait alors retirer la garde ou recharger `j81.py`.
7. **Enfant** : la recommandation UIAA n° 9 n’a pas été lue ; le cours se limite à un renvoi.
8. **Contentieux du délai du TACO** (12 h selon l’ISBT, 6 h selon Vlaar) : il est exposé dans la fenêtre TACO. Le cours suit l’ISBT, référence de l’hémovigilance suisse.
9. `chapters.json` et `organisation/*` n’ont pas été modifiés, comme demandé : l’enregistrement revient à l’orchestrateur. Les contrôles de construction ont été faits sur une copie superposée.

## Injection

- `chapters/J81/` : `J81_a.html`, `J81_b.html`, `J81_c.html`, `J81_d.html`, `J81_pop1.html`, `J81_pop2.html`.
- `glossary/j81.py` : glossaire de l’auteur, avec ajout conditionnel pour éviter toute collision.
- `livraisons/Livraison Claude/P-02-Pneumologie/travail/J81/captures/` : deux captures et `captures.json`.
- Aucune opération Git. Aucun autre cours, ni `chapters.json`, ni `organisation/*`, ni le brouillon de l’auteur n’ont été modifiés.
