# Reprise E11 — Diabète sucré de type 2 (E-06-Endocrinologie et métabolisme, S05)

Remise auteur C01-R-ENDO, cycle 1, 2026-10-11T18:25:55.814209+00:00. Identité d’exécution : `/root/c01_r_endo`. Revue et production par IA ; **validation médicale humaine et audits indépendants en attente**. Ce rapport n’attribue aucune note d’audit et n’autorise aucune injection.

## Résultat et périmètre

Le brouillon Claude du 9 octobre est repris et corrigé dans ce seul dossier : six sources HTML et un glossaire conditionnel. Les sept fichiers finaux sont reliés aux empreintes de `preuves/final_files.json`, de la matrice d’affirmations et de la matrice suisse. Le plan monographique comprend question clinique, définition, épidémiologie, mécanismes, facteurs de risque, anamnèse, examen, diagnostic, urgences, complications, objectifs/traitement, suivi, situations particulières puis critères formels et paramètres clés. Les quatre onglets sont complets ; 68 fenêtres, sept Pareto, quatre quiz et six figures sont présents. Le comptage de `test_v7.py --static` donne 21 992 mots, références et fenêtres comprises ; ce volume ne vaut pas note de qualité.

Seule la catégorie E11 est proposée pour une future déclaration `covers:["E11"]`. E10, E66, E78 et I50 sont des renvois ou des différentiels, sans prétention de cours complets. Les SSP 3 et 158 suivent l’annexe pédagogique MEDINA ; cette correspondance n’est pas une table officielle PROFILES vers la CIM. Ni S05, ni la tétrade, ni la CIM-11 ne sont déclarés complets.

## Provenance et lecture du Prompt de vérité

Les huit fichiers originaux Claude, rapport compris, ont été vérifiés de nouveau contre `provenance/original_hashes.json` et restent strictement identiques. Le rapport original est aussi conservé dans `provenance/rapport_auteur_claude_original.md`. L’inventaire distant du coordinateur examine 87 arbres Git des branches et têtes de PR : aucune version plus récente n’a été trouvée. Sa preuve est `docs/collaboration/reviews/2026-10-11/CYCLE_01/INVENTAIRE_DISTANT_CIBLE.json`. La reprise complète cet existant ; elle ne le remplace pas silencieusement.

En entrée, les deux Prompts, AGENTS, l’instruction active du cycle 1, le plan de la tétrade, le guide de rédaction, le contrat suisse, les sections 7–13 du leadership et CHAPTER_SPEC ont été lus. Le constat initial, conservé tel quel dans `preuves/conformite_entree_initiale.json`, signalait correctement les sources et contrôles encore en cours : aucune approbation médicale ni aucune source inaccessible n’était déclarée vérifiée. Les affirmations provisoires ont ensuite été comparées aux passages téléchargés et effectivement lus, avant leur acceptation dans cette remise.

En sortie, les deux Prompts et instructions actives ont été relus, puis les sept surfaces finales ont été contrôlées contre les exigences. `preuves/revue_auteur.json` conserve l’entrée initiale, sa revalidation datée après levée des réserves et la vérification de sortie, avec chemins et empreintes. La revalidation ne prétend pas avoir eu lieu avant les travaux. Les exigences de l’audit croisé et du contre-audit restent à réaliser par les agents distincts prévus ; le contrôle auteur ne les remplace pas.

## Sources réellement consultées

Le registre `preuves/sources.json` contient **54 sources, dont 21 informations professionnelles suisses exactes**. Les fichiers intégraux restent dans `/workspace/work/cycle1-sources-E11/`, accessibles aux auditeurs. Le dépôt reçoit les URL, titres, versions, populations, limites, sections, empreintes et reformulations, sans republier les articles ou FI en entier.

La priorité clinique est donnée aux recommandations SSED 2023, au diagnostic par HbA1c 2011, aux critères de qualité 2017, à la maladie rénale diabétique SSED/SSN de mai 2024, au pied QualiCCare 2023, à l’insuffisance cardiaque suisse 2024, à la conduite SSED/SGRM 2025, aux recommandations de technologies 2025 et au document d’alternatives insuliniques. Son nom de fichier comprend 2026 mais son état lu est **août 2025**. Les données suisses MonAM sont l’ESS 2022, mise à jour le 17 mars 2025 ; elles concernent le diabète déclaré chez les 15 ans et plus en ménage privé et ne distinguent pas les types.

Le consensus **conjoint ADA/EASD publié le 2 octobre 2026**, DOI `10.1007/s00125-026-06855-7`, a été confirmé par les métadonnées PubMed et le texte de l’éditeur, puis lu dans les sections effectivement utilisées. Il n’est ni rejeté par supposition de date, ni accepté sur la seule déclaration du brouillon. Sa cosignature européenne est explicite ; ses positions ne deviennent pas des autorisations suisses de médicaments. Pour l’ESC 2023, l’accès OUP initial répondait 403 ; les passages décisifs ont été lus dans la **traduction officielle italienne de 2024**, dont le PDF intégral est conservé. La traduction et les numéros de sections sont déclarés.

Le consensus conjoint de crises hyperglycémiques 2024 a été lu, y compris la figure diagnostique 2 réellement vue (page 7 du PDF, page imprimée 1461). JBDS 2023 documente une stratégie distincte pour l’insuline dans l’état hyperosmolaire. Le consensus de rémission 2021, le texte complet mécanistique Galicia-Garcia 2020 et les conclusions IHSG 2017 étayent leurs contenus propres. Pour IWGDF, **seul l’appendice technique 1, pages 26–28 du PDF, a été lu** ; aucune lecture des 349 pages n’est alléguée.

Les publications primaires UKPDS 33/34/80/91, ACCORD, Steno-2, DiRECT, incrétines, sous-groupes, Taylor, LEADER, FLOW, SOUL, FIDELIO et EMPA-REG ont été consultées dans leurs résumés PubMed : seuls les éléments réellement présents dans ces résumés sont utilisés. Les mécanismes détaillés ne sont pas justifiés par ces résumés seuls ; ils reposent sur le texte complet et les propriétés pharmacologiques réellement consultés.

**mediX n’a pas été vérifié** : boucles de redirection avec les accès essayés, y compris navigateur et variantes. Toutes ses citations et les affirmations propres sans autre passage lu ont été supprimées ou reformulées. Les tentatives infructueuses ne sont pas comptées parmi les 54 sources vérifiées. Les anciens intervalles universels de dépistage, chiffres annuels de dépendance insulinique et conditions financières non étayées ne subsistent pas.

## Informations professionnelles exactes

Chaque produit a été recherché par `tools/swissmedic_fi.py chercher`, puis son texte exact a été obtenu et consulté. Le registre donne également les numéros d’autorisation, les sections et l’empreinte du texte téléchargé. La date ci-dessous est celle de la FI, distincte d’une date commerciale de page.

| Produit exact / information professionnelle | Version lue | GTIN d’identification |
|---|---|---|
| Information professionnelle suisse Glucophage — AIPS via AmiKo | 2025-10 | 7680260610169 |
| Information professionnelle suisse Jardiance — AIPS via AmiKo | 2025-07 | 7680632270014 |
| Information professionnelle suisse Forxiga — AIPS via AmiKo | 2026-08 | 7680651760015 |
| Information professionnelle suisse Ozempic — AIPS via AmiKo | 2026-07 | 7680666040010 |
| Information professionnelle suisse Rybelsus — AIPS via AmiKo | 2026-08 | 7680698650010 |
| Information professionnelle suisse Trulicity — AIPS via AmiKo | 2026-07 | 7680652360016 |
| Information professionnelle suisse Mounjaro — AIPS via AmiKo | 2026-07 | 7680687260015 |
| Information professionnelle suisse Januvia — AIPS via AmiKo | 2024-04 | 7680578630019 |
| Information professionnelle suisse Trajenta — AIPS via AmiKo | 2023-11 | 7680618930017 |
| Information professionnelle suisse Diamicron — AIPS via AmiKo | 2025-02 | 7680552340064 |
| Information professionnelle suisse Tresiba — AIPS via AmiKo | 2024-12 | 7680625620017 |
| Information professionnelle suisse Toujeo — AIPS via AmiKo | 2021-07 | 7680654530011 |
| Information professionnelle suisse Lantus — AIPS via AmiKo | 2022-09 | 7680553460037 |
| Information professionnelle suisse Ryzodeg — AIPS via AmiKo | 2020-11 | 7680626270013 |
| Information professionnelle suisse Kerendia — AIPS via AmiKo | 2025-11 | 7680681300014 |
| Information professionnelle suisse Baqsimi — AIPS via AmiKo | 2026-03 | 7680674650010 |
| Information professionnelle suisse NovoRapid — AIPS via AmiKo | 2026-04 | 7680550450024 |
| Information professionnelle suisse Huminsulin — AIPS via AmiKo | 2021-09 | 7680517500397 |
| Information professionnelle suisse Ezetrol — AIPS via AmiKo | 2024-03 | 7680561950025 |
| Information professionnelle suisse Actos — AIPS via AmiKo | 2021-05 | 7680553780012 |
| Information professionnelle suisse Onglyza — AIPS via AmiKo | 2023-09 | 7680593900012 |

Les sections indications, dose/voie, reins/foie, contre-indications, précautions/interactions et grossesse/allaitement ont été examinées pour les faits enseignés ; les propriétés ont été lues pour les mécanismes utilisés. Une FI d’une autre présentation ou d’une autre marque n’est pas substituée. Les produits de classes évoquées sans posologie ni ordonnance individuelle ne sont pas présentés comme des prescriptions vérifiées. Les interactions citées sont celles des FI des médicaments du chapitre, sans prescription de leurs partenaires.

## Corrections médicales décisives et arbitrages

- **Crises :** l’état hyperosmolaire réunit les quatre groupes de critères 2024 : glucose ≥33,3 mmol/L ; osmolalité efficace >300 ou totale >320 mOsm/kg ; β-hydroxybutyrate <3 ou cétonurie <2+ ; pH ≥7,3 et bicarbonates ≥15. L’acidocétose exige diabète connu ou glucose ≥11,1, cétose significative, et acidose. Une cétonémie seule ne devient jamais une acidocétose. La vignette euglycémique comporte maintenant un pH de 7,22. Le seuil de potassium 3,5 avant insuline et les débits 0,05/0,1 U/kg/h sont attribués au consensus 2024 ; NovoRapid est vérifié pour l’usage intraveineux professionnel. JBDS 2023 n’est pas fusionné silencieusement avec ce consensus.
- **Metformine/SGLT2 :** Glucophage est limité à 1 g/j avec DFG 30–59 et contre-indiqué sous 30 ; l’initiation Jardiance sous 20, l’initiation rénale Forxiga sous 25, les doses selon indication et la poursuite éventuelle sont distinguées. L’effet glycémique réduit ou probablement absent n’annule pas un bénéfice d’organe documenté. Le délai préopératoire de trois jours des FI prime sur l’ancien délai de deux jours de SSED 2023, écart explicitement expliqué.
- **Incrétines/insulines :** Rybelsus N 1,5→4→9 mg est distingué des anciennes présentations 3→7→14, sans substitution milligramme pour milligramme. Ozempic et Mounjaro ont leurs paliers et limites exacts ; le risque CMT/MEN2 des FI suisses n’est pas transformé en contre-indication étrangère, et Trulicity n’en reçoit pas un avertissement absent de sa FI. Les règles de contraception du tirzépatide sont décrites. Toujeo se réajuste tous les trois à quatre jours ; Ryzodeg débute à 10 unités **totales quotidiennes**, non dix unités à chaque prise. Les différences grossesse/allaitement de Tresiba, Ryzodeg et glargine sont conservées malgré une phrase plus large d’une recommandation suisse.
- **Cardio-rein :** SCORE2-Diabetes est borné à sa population validée 40–69 ans sans athérosclérose établie ni atteinte sévère ; les quatre risques et atteintes sévères d’organe sont explicités. Les seuils de dépistage d’insuffisance cardiaque ≥60 ans asymptomatique, la zone grise et les seuils symptomatiques hors aigu sont distingués, avec leur niveau de preuve d’experts. A2 est 3 à <30 mg/mmol ; chronicité ≥3 mois. Kerendia comprend ses seuils rénaux, potassium d’initiation et contrôle à quatre semaines.
- **Autres produits :** Ezetrol, Actos et Onglyza ont leurs FI propres. Éviter un médicament selon une recommandation d’insuffisance cardiaque ne signifie pas une CI identique pour toutes les classes : Actos a la CI formelle NYHA III/IV et des précautions plus larges, Onglyza un avertissement. Les observations hépatiques de pioglitazone ne deviennent pas une indication suisse MASH.
- **Rémission/essais :** le critère de rémission est ≥3 mois sans antidiabétique. Le protocole historique DiRECT utilisait deux mois ; ses dénominateurs initiaux et prolongés sont distingués. Le résultat de non-infériorité cardiovasculaire du tirzépatide n’est pas une supériorité ni une indication suisse. La chirurgie dès IMC 30/35 est discutée/à envisager selon le consensus et ne devient pas automatique. ARMMS-T2D est écrit conformément au titre primaire, avec le décalage orthographique du corps du consensus déclaré.
- **Diagnostic/examen/sciences :** HbA1c altérée dans certaines situations signifie limite diagnostique contextualisée, pas inutilité universelle du suivi. Le protocole HGPO et ses seuils sont figurés sans inventer de tracé patient. Le monofilament suisse gradué et les répétitions IWGDF ne sont pas additionnés. Les mécanismes β, IRS/PI3K/AKT/FOXO1 et rénaux sont reformulés au niveau réellement étayé ; GLUT2 n’est pas déclaré universel chez l’humain. L’effet incrétine est diminué ou absent, sans formule absolue. Les six Pareto existants ont été repris et celui des Sciences ajouté ; leurs raccourcis ne réintroduisent pas les erreurs corrigées.

Le détail des transformations est conservé dans `preuves/corrections-medicales.json`. La matrice `preuves/source_ledger.json` contient **392 liaisons entre sources et affirmations/blocs, 90 blocs HTML relus et le glossaire**, couvrant les sept fichiers. Chaque liaison indique clairement que la source étaye les éléments de son résumé de passage, avec les autres sources du bloc ; elle ne prétend pas qu’une source seule justifie tous les faits du paragraphe. La granularité et la justesse de ces correspondances restent à juger par l’auditeur distinct. Aucun résultat de script ne prouve automatiquement l’exactitude scientifique.

`preuves/matrice_contexte_suisse.json` contient **82 décisions**, scope `chapter`, E11/S05, liées aux mêmes empreintes. Les passages et produits sont documentés, les recherches de lacunes sont bornées aux documents suisses effectivement consultés. Son `auditor_verdict` est **en attente d’audit indépendant** : l’auteur ne s’attribue pas ce rôle. Aucun taux de tout MEDINA n’est calculé à partir de ce chapitre.

## Vérification technique et visuelle réelle

Le build utilise une copie isolée `/workspace/work/c01-endo-build`, `MEDINA_OUT` propre, l’E11 de cette livraison et l’entrée de scratch `production_cycle:1`. Les nouveaux CSS du coordinateur sont copiés dans ce scratch. Aucune source canonique ni déclaration partagée n’a été modifiée par l’auteur.

- Reconstruction S05 réussie : 3 050 485 octets avant compression, 2 871 608 après, 69 gabarits. `test_v7.py --static E11` : **OK**, aucune abréviation non couverte, fenêtre manquante, classe hors contrat ni style en ligne.
- Le banc Playwright utilise **`/usr/bin/chromium` et HTTP localhost**, pas `file://`. Ordinateur 1440×1000 et mobile 390×844 : quatre onglets et quatre disciplines affichés, **68 fenêtres réellement cliquées**, **52 abréviations réellement ouvertes**, **quatre quiz avec leurs trois choix et feedback**, sept Pareto ouverts, aucun template E11 inatteignable, zéro erreur JavaScript, largeur du document égale au viewport.
- Navigo : 17 entrées et focus réel du titre de destination ; taille 21 px puis réinitialisation 17 px ; mode livre avec les quatre onglets, puis retour normal, sur les deux formats.
- Couleurs calculées : corps **rgb(23,62,137)**, termes **rgb(155,57,0)**, police **Atkinson Hyperlegible Next**. Les deux jauges filtrantes ont bordure et rail **rgb(255,255,255)** et `appearance:none`. Leurs compteurs scratch ne certifient pas une injection.
- Sciences : quatre unités de 462, 466, 436 et 437 mots, une figure accessible légendée chacune, quatre liens science→clinique/examen/traitement/rétention. Ce contrôle ciblé applique les assertions de `tests/audit_sciences.py` ; le contrôle global de baseline Git n’est pas prétendu exécuté.
- Les deux captures réglementaires `e11-1-ouverture.png` et `e11-2-explication.png` ont été produites par `tools/capture_lecon.py --url ... --browser-executable /usr/bin/chromium`, puis **vues et examinées**. Les captures mobile d’ouverture/fenêtre ont aussi été vues. Elles sont destinées au panneau latéral du coordinateur, pas au fil du chat.

Les premières tentatives du banc ont révélé une erreur d’indentation du script, puis des difficultés de clic du test dans les `tspan` et sur les abréviations à l’intérieur des options. Le banc a été corrigé pour cliquer le texte SVG réellement peint et le corps des options ; aucune assertion en échec n’a été masquée. Les traces de ces essais sont conservées dans le scratch `test_attempts` ; seule la passe finale complète donne le résultat ci-dessus. Les banques/scripts de reproduction sont dans `preuves/verification_frontend.py` et `preuves/construire_preuves.py`.

## État de remise

**Prêt pour audit croisé par C01-R-NEPH ; aucune réserve bloquante auteur identifiée après les corrections documentées.** Cela décrit la remise de l’auteur, sans garantir le futur verdict médical. Les deux passes de l’audit croisé, le contre-audit différé C01-CA-ENDO, le contrôle du coordinateur et la publication vérifiée restent obligatoires avant injection. Aucune injection, aucun commit, aucun push et aucune validation par médecin n’ont été réalisés par C01-R-ENDO. Le cycle 2 demeure fermé.
