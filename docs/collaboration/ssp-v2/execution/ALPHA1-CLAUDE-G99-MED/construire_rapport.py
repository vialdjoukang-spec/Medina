#!/usr/bin/env python3
"""Construit rapport.json de l'audit ALPHA1-CLAUDE-G99-MED et vérifie que chaque ancre existe telle quelle.

Usage : python3 construire_rapport.py <racine du worktree>
"""
import hashlib
import json
import sys
from pathlib import Path

ICI = Path(__file__).resolve().parent
R = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
A, B, C, D = "chapters/G99/G99_a.html", "chapters/G99/G99_b.html", "chapters/G99/G99_c.html", "chapters/G99/G99_d.html"
P1, P2, GL = "chapters/G99/G99_pop1.html", "chapters/G99/G99_pop2.html", "glossary/g99.py"
FICHIERS = [A, B, C, D, P1, P2, GL]
MANIFESTE = json.loads((R / ".medina/missions/ALPHA1-CLAUDE-G99-MED.json").read_text(encoding="utf-8"))


def pr(s, sec, cit):
    return {"source_id": s, "section": sec, "citation_courte": cit}


def k(i, g, f, ancre, constat, preuve, proposition, justification):
    return {"id": i, "gravite": g, "fichier": f, "ancre": ancre, "constat": constat, "preuve": preuve,
            "proposition": proposition, "justification": justification}


CONSTATS = [
    k("C01", "MAJEUR", C, "data-s=\"g99-s-anat\"",
      "Le sous-onglet « Sémiologie fondamentale et analytique » est absent : #pS compte quatre data-s (g99-s-anat, g99-s-histo, g99-s-physio, g99-s-bioch) et aucun g99-s-semio. L’onglet 1 décrit symptômes et signes (g99-5, g99-6) sans technique, sans mécanisme par signe, sans valeur chiffrée des signes médullaires et sans raisonnement analytique ; la fenêtre g99-signes-mcd déclare « la technique précise de chaque signe n’est pas détaillée ».",
      [pr("S31", "tableau 2 ; résultats", "Hoffmann : chiquenaude du majeur → adduction du pouce ; hyperréflexie Se 0,79 ; clonus Se 0,31"),
       pr("S4", "4.2.2.1", "HR increase … usually not >10 b.p.m."),
       pr("S8", "How is it diagnosed?", "low sensitivity … but high specificity")],
      "propositions/G99_c_semio.html (bouton en tête de la barre, discipline g99-s-semio, îlots g99-sm-1 à g99-sm-7, figure de raisonnement non anatomique, trois cas corrigés) ; propositions/G99_pop1_semio.html (six fenêtres g99-sm-* à ajouter dans G99_pop1.html) ; renvoi depuis l’onglet 1 : proposition P42.",
      "Mécanisme : la sémiologie relie la structure lésée (baroréflexe, voies longues) au signe → conséquence : sans technique ni valeur, l’étudiant ne sait ni rechercher ni peser un signe → décision : localiser avant d’imager et choisir l’examen qui tranche (tests réflexes, IRM)."),
    k("C02", "MAJEUR", A, "est une polyneuropathie axonale de l’insuffisance rénale chronique.",
      "Périmètre CIM-10-GM erroné : la leçon présente la neuropathie urémique (polyneuropathie) comme une atteinte G99, alors que la CIM-10-GM 2024 la classe en G63.8* (« Urämische Neuropathie (N18.-†) ») ; G99.8* ne vise que la paralysie urémique. De même, la polyneuropathie amyloïde relève de G63.3* ; seule la neuropathie autonome amyloïde relève de G99.0*. Les sous-codes G99.00 (gastroparésie), G99.08, G99.1, G99.2 (myélopathie : M47.0-†, M50.0†, M51.0†, C00–D48†, M47.-†) et G99.8 ne sont cités nulle part (une seule occurrence de « G99. » dans la leçon), alors que le rapport de rédaction déclare la rubrique 19 couverte.",
      [pr("S1", "G99.-*", "G99.8* … Inkl.: Urämische Paralyse (N18.-†)"),
       pr("S2", "G63.-*", "G63.8* … Inkl.: Urämische Neuropathie (N18.-†)"),
       pr("S1", "G99.0-*", "G99.00* Gastroparese bei autonomer Neuropathie")],
      "propositions/G99_corrections.html, P01 (phrase de périmètre dans g99-1) et P02 (tableau des sous-codes dans g99-12) ; propositions/glossary_g99_ajouts.py (clés des sous-codes, nécessaires à test_v7).",
      "Mécanisme : G99 est une catégorie de manifestation qui exige un code † → conséquence : un code faux fausse le dossier, la statistique et la question d’examen sur le codage → décision : coder la neuropathie urémique G63.8* avec N18.-†, la gastroparésie diabétique G99.00* avec E1x.4†."),
    k("C03", "MAJEUR", A, "Les symptômes cardinaux sont les nausées et les vomissements (95 %)",
      "Douze occurrences présentent le pourcentage d’accord du panel UEG/ESNM sans le mot « accord », à côté d’un symptôme, d’un test ou d’un traitement : « nausées et vomissements (95 %) », « fréquents (95 %) » (g99-1) ; « La scintigraphie (98 %) et le test respiratoire (95 %) sont valides » (g99-7, g99-e-3, g99-vidange) ; « retenue (85 %) », « D2 (86 %) », « 5-HT4 (85 %) », « cause (88 %) » (g99-9). Le lecteur y lit une fréquence de symptôme, une performance diagnostique ou un taux d’efficacité qui n’existent pas dans la source. Recalcul : calculs/resultats.json, verdict FAUX (grandeur erronée).",
      [pr("S3", "énoncés 1.3, 1.4, 5.4, 5.5, 6.1, 6.7, 6.14, 7.2", "STATEMENT ENDORSED, overall agreement 95% … 98% … 86% … 85% … 88%"),
       pr("S3", "section 4", "Symptoms … poor predictors of the rate of GE")],
      "propositions/G99_corrections.html, P03 à P08 (« accord de … % », phrase de lecture « ces chiffres ne sont ni des sensibilités ni des spécificités »).",
      "Mécanisme : un pourcentage d’accord mesure l’opinion d’un panel, non une propriété du patient ou du test → conséquence : surestimation de la valeur d’une scintigraphie (« 98 % ») ou d’un prokinétique (« 86 % ») → décision : lire ces chiffres comme force de consensus et chercher ailleurs la performance diagnostique."),
    k("C04", "MAJEUR", B, "les gabapentinoïdes sont proposés en première ligne de la douleur neuropathique métabolique (la source ne donne pas de posologie rénale).",
      "La leçon propose les gabapentinoïdes en première ligne de la douleur de la neuropathie urémique, donc d’une population en insuffisance rénale avancée, sans la contrainte de l’information suisse : la prégabaline « ne doit pas être utilisée » si la clairance est < 30 mL/min et voit sa dose réduite de moitié entre 30 et 60 mL/min ; la gabapentine exige une réduction (150–300 mg/j sous 15 mL/min ; 200–300 mg après chaque hémodialyse de 4 h). Les indications suisses (neuropathie diabétique, névralgie postherpétique) n’incluent pas la neuropathie urémique : emploi hors indication. La source citée met aussi les IRSN et les tricycliques en première ligne.",
      [pr("S29", "Troubles de la fonction rénale", "ne doit pas être utilisée chez les patients présentant une insuffisance rénale sévère (Clcr <30 ml/min)"),
       pr("S30", "Troubles de la fonction rénale ; Hémodialyse", "<15 : 150-300 mg/jour ; 200-300 mg après chaque période d’hémodialyse de 4 heures"),
       pr("S17", "2.2", "First-line treatments include selective noradrenaline reuptake inhibitors, gabapentinoids and tricyclic antidepressants")],
      "propositions/G99_corrections.html, P12.",
      "Mécanisme : la prégabaline et la gabapentine sont éliminées par le rein sous forme inchangée → conséquence : accumulation, sédation et chutes chez le patient urémique → décision : éviter la prégabaline sous 30 mL/min, adapter la gabapentine à la clairance et à la dialyse, et signaler le hors indication."),
    k("C05", "MAJEUR", D, "Les traitements spécifiques de la polyneuropathie à transthyrétine (patisiran, vutrisiran, inotersen, eplontersen) n’ont pas été documentés par des informations professionnelles suisses.",
      "Point décisionnel non sourcé alors que la source suisse existe : trois traitements sont autorisés en Suisse pour la polyneuropathie héréditaire à transthyrétine de stade 1 ou 2 (Onpattro : 300 µg/kg IV toutes les 3 semaines, max 30 mg à ≥ 100 kg ; Amvuttra : 25 mg SC tous les 3 mois, vitamine A 2500–3000 UI/j au plus ; Wainzua : 45 mg SC par mois). La leçon (g99-9, g99-p-4, g99-tafamidis, g99-13) affirme qu’aucune information suisse n’a été lue et ne donne aucun traitement de fond de la polyneuropathie.",
      [pr("S26", "Indications ; Posologie", "polyneuropathie de stade 1 ou de stade 2 ; 300 microgrammes par kg … toutes les 3 semaines ; ≥ 100 kg … 30 mg"),
       pr("S27", "Indications ; Posologie", "25 mg … une fois tous les 3 mois ; vitamine A … 2500 UI à 3000 UI par jour au maximum"),
       pr("S28", "Indications ; Posologie", "45 mg … une fois par mois")],
      "propositions/G99_corrections.html, P13 à P15 ; propositions/G99_pop2_attr.html (trois fenêtres g99-patisiran, g99-vutrisiran, g99-eplontersen).",
      "Mécanisme : ces molécules réduisent la production hépatique de transthyrétine, donc le dépôt → conséquence : elles ne s’adressent qu’aux stades 1 et 2 → décision : diagnostiquer tôt et adresser à un centre neuromusculaire, ce que la leçon doit dire."),
    k("C06", "MAJEUR", C, "<div class=\"key\"><b>Corrélation clinique.</b> Corrélation clinique : une compression cervicale touche les quatre membres",
      "Sciences fondamentales sous le contrat : tests/audit_sciences.py échoue avec 21 erreurs. Les quatre disciplines comptent 167, 147, 176 et 160 mots (minimum 280) ; la biochimie n’a aucune figure ; aucun encadré « Science → clinique. », « Science → examen. », « Science → traitement. » ni « À retenir. » (tous intitulés « Corrélation clinique », avec redoublement du libellé). La génétique est fusionnée sans discipline propre. Le passage normal → pathologique est réduit à quelques phrases par discipline.",
      [pr("S9", "Myélopathie cervicale", "le déficit neurologique varie en fonction de la localisation anatomique, de la cinétique de compression ainsi que de la réserve vasculaire"),
       pr("S7", "Penetrance", "80% of mutation carriers … by age 50, whereas this number is only 11% in Sweden")],
      "propositions/G99_c_sciences.html (encadrés aux quatre libellés, paragraphes sourcés, figure de biochimie). Contrôle sur copie : audit_sciences « passed » (374, 311, 305, 319 mots) et test_v7 --static OK.",
      "Mécanisme : les sciences doivent expliquer le pourquoi des signes et des gestes → conséquence : sans corrélations explicites, la cinétique de compression, la pénétrance et le baroréflexe restent des mots → décision : imagerie précoce, biopsie répétée, traitement au bon stade."),
    k("C07", "MAJEUR", C, "aria-label=\"Moelle comprimée\"",
      "Deux figures anatomiques produites par l’agent de rédaction (origine démontrée : rapport du cycle Betta 41, « 5 figures SVG au total dans le chapitre ») : figure 3 « Moelle comprimée » (coupe médullaire stylisée) et figure 4 « Fibre nerveuse » (axone, endonèvre, dépôts). Classe ANATOMIQUE_IA selon la règle de Vial du 15.10.2026 : non recevables. Aucun original n’a pu être validé (Commons : HTTP 429 avec délai d’attente, aucune relance ; figure 1 du BMJ 2018 reproduite avec la permission d’un tiers, non réutilisable).",
      [pr("S8", "Fig 1 (licence)", "Figure reproduced with permission from Michael G Fehlings")],
      "propositions/G99_c_sciences.html : retrait des deux dessins et remplacement par des chaînes causales non anatomiques sourcées (SCHEMA_NON_ANATOMIQUE) ; recherche d’un original (Gray’s Anatomy, Servier Medical Art CC BY) à reprendre par tools/image_clo_finder.py quand le délai Commons sera levé.",
      "Mécanisme : un dessin approximatif d’une structure fixe une image fausse → conséquence : erreur d’anatomie transmise → décision : original sourcé ou schéma causal."),
    k("C08", "MINEUR", A, "L’hyperkaliémie chronique est le mécanisme principal proposé de la neuropathie urémique",
      "La source décrit une « strong correlation » entre kaliémie et altérations nerveuses et un essai positif de restriction potassique, en demandant des essais plus larges ; la leçon en fait « le mécanisme principal proposé » (g99-3, g99-4, g99-s-bioch, g99-uremie). Glissement de l’association vers la causalité, contraire à la consigne de Vial.",
      [pr("S17", "2.1.4 Potassium", "strong correlation between hyperkalaemia and the development of both functional and structural changes … need to be further substantiated")],
      "propositions/G99_corrections.html, P16 à P19.",
      "Mécanisme : corrélation ≠ causalité → conséquence : surestimation de l’effet attendu de la restriction potassique → décision : présenter la restriction comme prometteuse, non comme traitement établi."),
    k("C09", "MINEUR", B, "la décompression est le plus souvent une discectomie antérieure avec cage (Revue médicale suisse, 2015).",
      "La source suisse décrit la discectomie antérieure avec cage pour la hernie discale cervicale ; la leçon l’étend à toute myélopathie cervicale dégénérative. Une série de MCD légère opérée l’était à 88,5 % par voie postérieure.",
      [pr("S9", "Traitement chirurgical", "Celui-ci s’effectue dans la majorité des cas par voie antérieure (discectomie antérieure)"),
       pr("S11", "Article 4 (série japonaise)", "The posterior approach was used in 88.5% of patients")],
      "propositions/G99_corrections.html, P20.", "La voie dépend du nombre de niveaux et du siège de la compression ; une généralisation fausse la représentation de la chirurgie."),
    k("C10", "MINEUR", B, "<td>Inapte tant que diagnostic et traitement manquent ; sinon au moins 12 mois</td>",
      "Tableau de conduite : « sinon au moins 12 mois » peut se lire « une fois le diagnostic établi, 12 mois », alors que la directive fixe 12 mois en l’absence de diagnostic ; la ligne « vasovagale, épisode unique hors conduite : apte (1er et 2e groupe) » manque.",
      [pr("S18", "Tableau 1", "En l’absence de diagnostic, délai d’attente d’au moins 12 mois à compter du dernier événement")],
      "propositions/G99_corrections.html, P21 et P22.", "Une formulation ambiguë sur l’aptitude à conduire expose à un conseil erroné au patient professionnel."),
    k("C11", "MINEUR", D, "jusqu’à 15 mg par jour dans certains cas (ESC 2018 : 2,5 à 10 mg trois fois par jour)",
      "Midodrine : la leçon juxtapose « jusqu’à 15 mg par jour » (FI) et « 2,5 à 10 mg trois fois par jour » (ESC, soit 30 mg/j) sans donner le plafond de la FI suisse : une augmentation au-delà de 30 mg/j en trois prises ne peut être recommandée. Recalcul : 3 × 10 = 30 mg = plafond FI (cohérent) ; 15 mg/j est un palier, non un maximum.",
      [pr("S21", "Posologie c)", "Dans certains cas, des doses allant jusqu’à 15 mg/jour … supérieure à 30 mg … ne peut être recommandée")],
      "propositions/G99_corrections.html, P23 et P24.", "Sans plafond explicite, l’étudiant ne peut concilier la FI et l’ESC."),
    k("C12", "MINEUR", D, "0,1 mg trois fois par semaine à 0,2 mg par jour (indications suisses : insuffisance surrénalienne, perte de sel)",
      "Fludrocortisone : la borne ESC de 0,3 mg/j dépasse la dose usuelle maximale de la FI (0,2 mg/j) sans être signalée ; la limite de 0,05 mg/j en cas d’hypertension induite et quatre contre-indications (herpès simplex oculaire, zona ou varicelle, artériosclérose cérébrale avancée) manquent.",
      [pr("S22", "Posologie ; Contre-indications", "0,1 mg 3 fois par semaine à 0,2 mg par jour … 0,05 mg par jour ne devra pas être dépassée ; Herpès simplex oculaire ; Zona/varicelle")],
      "propositions/G99_corrections.html, P26 et P27.", "Le médicament est déjà hors indication pour l’hypotension ; la dose doit au moins rester dans le cadre de la FI ou le dépassement être assumé."),
    k("C13", "MINEUR", B, "un test réflexe anormal = possible ; ≥ 2 = confirmée ; avec hypotension orthostatique = sévère.",
      "Stadification de Toronto imprécise : il s’agit de tests cardiovagaux (de fréquence) ; la réponse tensionnelle au lever ne compte pas pour « confirmée ». La définition exige aussi l’exclusion des autres causes (g99-13, g99-toronto, g99-e-2).",
      [pr("S6", "résumé", "at least two abnormal cardiovagal test results are required for definite or confirmed CAN … after exclusion of other causes")],
      "propositions/G99_corrections.html, P28 à P30.", "Compter la mesure tensionnelle parmi les deux tests fait sur-diagnostiquer la neuropathie confirmée."),
    k("C14", "MINEUR", B, "Une rétention supérieure à 20 % à quatre heures est citée comme facteur pronostique.",
      "Le sens du facteur n’est pas donné : dans la cohorte citée par le consensus, une rétention > 20 % à 4 h s’associait à une MOINDRE intensité des symptômes à 48 semaines. Le chiffre peut être pris pour un seuil diagnostique.",
      [pr("S3", "section 7", "Factors independently associated with reduced symptoms at 48 weeks included … a 4-h gastric retention more than 20%")],
      "propositions/G99_corrections.html, P09 à P11.", "Lu sans direction, le chiffre suggère un mauvais pronostic qui n’est pas celui de la source."),
    k("C15", "MINEUR", D, "la date de mise à jour de chaque fiche n’a pas pu être extraite.",
      "Les dates des informations professionnelles sont extractibles : Gutron mars 2021, Florinef mars 2026, Motilium juin 2026, Paspertin janvier 2020, Vyndaqel avril 2026. Le mécanisme d’action de la midodrine (promédicament → desglymidodrine, agoniste α direct) figure dans la FI, contrairement à la phrase de la leçon.",
      [pr("S21", "Mise à jour ; Mécanisme d’action", "Mars 2021 ; desglymidodrine … α-sympathomimétique"),
       pr("S24", "Mise à jour", "Janvier 2020")],
      "propositions/G99_corrections.html, P25.", "Loi 3 du PROMPT_VERITE : toute dose porte la date de sa FI."),
    k("C16", "MINEUR", D, "inhibiteurs puissants du CYP3A4 allongeant le QT, insuffisance hépatique modérée ou sévère, prolactinome.",
      "Contre-indications de la dompéridone incomplètes et sans exemple : l’érythromycine (motilinomimétique discuté dans la même leçon) et la clarithromycine sont des inhibiteurs du CYP3A4 contre-indiqués ; hémorragie, occlusion mécanique ou perforation digestive, phéochromocytome manquent. L’interaction midodrine (inhibiteur du CYP2D6) → métoclopramide, plausible chez le même patient, n’est pas signalée.",
      [pr("S23", "Contre-indications", "clarithromycine, l’érythromycine … occlusion d’origine mécanique … phéochromocytome"),
       pr("S21", "Interactions", "La midodrine est un inhibiteur du cytochrome P450 CYP2D6 … métoclopramide")],
      "propositions/G99_corrections.html, P31 et P32.", "Patient type : gastroparésie diabétique sous érythromycine à qui l’on ajoute de la dompéridone."),
    k("C17", "MINEUR", C, "la pression chute et la fréquence cardiaque s’élève peu (au plus 10 battements par minute).",
      "Incohérence de seuil (SEM-20) : la Physiologie écrit « au plus 10 » comme une borne, alors que l’onglet 1 et la fenêtre g99-ho disent « habituellement » et « repère, non seuil absolu », conformément à l’ESC.",
      [pr("S4", "4.2.2.1", "usually not >10 b.p.m.")], "propositions/G99_corrections.html, P33.", "Un repère présenté comme borne fait exclure à tort une origine neurogène chez un patient anémique."),
    k("C18", "MINEUR", A, "<li><a href=\"#g99-12\">Critères formels et paramètres clés</a></li></ol>",
      "Plan du cours désynchronisé : le lien #g99-12 porte le titre « Critères formels et paramètres clés », alors que g99-12 est « Spécificités suisses et points d’examen fédéral » ; g99-13 (critères) n’a pas d’entrée.",
      [], "propositions/G99_corrections.html, P34.", "Navigation : le dernier îlot obligatoire (critères formels) est inaccessible depuis le plan."),
    k("C19", "MINEUR", GL, "développement non fourni par la source lue",
      "Glossaire : PND et NIS sont développés dans la liste des abréviations du consensus européen 2021 (« PND polyneuropathy disability », « NIS Neuropathy Impairment Score »), contrairement aux mentions « non fourni ».",
      [pr("S7", "abréviations du tableau 5", "PND polyneuropathy disability ; NIS Neuropathy Impairment Score")],
      "propositions/G99_corrections.html, P35 et P36.", "Règle 3 de CLAUDE.md : définition littérale lettre à lettre."),
    k("C20", "MINEUR", A, "aria-label=\"Schéma\"",
      "Trois figures (1, 2 et 5) ont pour nom accessible le seul mot « Schéma » ; le lecteur d’écran n’en restitue pas le contenu.",
      [], "propositions/G99_corrections.html, P37 à P39.", "Accessibilité exigée par le contrat des sciences (svg[role=img][aria-label] descriptif)."),
    k("C21", "MINEUR", B, "La baisse systolique de 25 mmHg dépasse le seuil de 20 mmHg : l’hypotension orthostatique est établie.",
      "Cas récapitulatif : recalcul 130/80 → 105/70 mmHg : ΔPAS 25 et ΔPAD 10 ; le critère diastolique est aussi atteint, et la fréquence debout, nécessaire pour suggérer l’origine neurogène, n’est pas donnée.",
      [pr("S4", "4.2.2.1", "≥20 mmHg … or diastolic BP ≥10 mmHg")], "propositions/G99_corrections.html, P40.", "Enseigner les deux critères et l’usage de la fréquence au lever."),
    k("E01", "ENRICHISSEMENT", A, "une image de compression ne prouve pas à elle seule une myélopathie, la clinique décide.",
      "Histoire naturelle de la compression asymptomatique absente (rubriques 13–14) : 8 % de myélopathie à un an et 22 % sur 44 mois médians (n = 199).",
      [pr("S8", "Box 1", "8% … will develop DCM after one year and 22% in total … median follow-up 44 months")],
      "propositions/G99_corrections.html, P41.", "Justifie l’information et le suivi plutôt que la chirurgie prophylactique."),
    k("E02", "ENRICHISSEMENT", D, "Sous dompéridone, le risque cardiaque (QTc, électrolytes) justifie la courte durée.",
      "Pharmacodynamie absente (« mécanismes … non développés ») alors que les FI la donnent ; interaction midodrine–métoclopramide.",
      [pr("S21", "Mécanisme d’action", "promédicament … desglymidodrine … aucun effet β-sympathomimétique"),
       pr("S3", "6.7", "Domperidone is a peripherally acting dopamine-2 antagonist … QTc")],
      "propositions/G99_corrections.html, P25 et P32.", "Le mécanisme explique la bradycardie réflexe, l’hypertension de décubitus et la tolérance extrapyramidale."),
    k("E03", "ENRICHISSEMENT", A, "un signe positif est très évocateur (BMJ, 2018).",
      "Valeur chiffrée des signes de myélopathie absente de l’onglet 1 : groupement de Cook (≥ 3/5 → Sp 99 %, RV+ 30,9 ; probabilité post-test recalculée 94,4 % pour une prévalence d’échantillon de 35,3 %).",
      [pr("S31", "Résultats (Cook 2010)", "any 3 of the 5 variables … specificity of 99% and a positive likelihood ratio of 30.9")],
      "propositions/G99_corrections.html, P42 ; détail dans la sémiologie.", "Un groupement de signes vaut mieux qu’un signe isolé."),
    k("E04", "ENRICHISSEMENT", A, "Environ 20 % des personnes diabétiques sont concernées (Diabetologia, 2024),",
      "Définition de Toronto (exclusion des autres causes) et prévalence jusqu’à 65 % avec l’âge et la durée du diabète non citées.",
      [pr("S6", "résumé", "prevalence of confirmed CAN is around 20%, and increases up to 65% with age and diabetes duration")],
      "propositions/G99_corrections.html, P43.", "L’âge et la durée orientent le dépistage."),
]

MATRICE = [
    (1, "Question clinique et enjeu pour l’examen fédéral", "couvert", "g99-0"),
    (2, "Définition et périmètre CIM-10-GM", "partiel", "g99-1, g99-12 ; neuropathie urémique et polyneuropathie amyloïde hors G99 (C02)"),
    (3, "Classifications et stades", "couvert", "g99-1 (ESC, Toronto, mJOA, stades ATTR) ; précision cardiovagale (C13)"),
    (4, "Épidémiologie suisse puis européenne", "partiel", "g99-2 ; aucune donnée suisse ; cohortes danoise et polonaise"),
    (5, "Normal → pathologique", "partiel", "g99-3, g99-s-* ; sciences sous le contrat (C06)"),
    (6, "Étiologies et facteurs de risque", "couvert", "g99-4"),
    (7, "Anamnèse et symptômes (fréquences)", "partiel", "g99-5 ; fréquences ATTR seules ; % d’accord pris pour fréquences (C03)"),
    (8, "Examen clinique (signes, Se/Sp)", "partiel", "g99-6 ; techniques et valeurs absentes (C01, E03)"),
    (9, "Drapeaux rouges et urgences", "couvert", "g99-8 (alert) ; posologie des corticoïdes de la compression métastatique non sourcée (lacune)"),
    (10, "Examens complémentaires", "partiel", "g99-7, g99-e-1 à g99-e-5 ; seuils scintigraphiques et valeurs de coupure des tests réflexes absents"),
    (11, "Diagnostic différentiel", "partiel", "g99-7.5 (trois lignes), g99-attr-diag"),
    (12, "Prise en charge suisse (FI datées)", "partiel", "g99-9, g99-p-* ; ATTRv-PN (C05), gabapentinoïdes en IR (C04), dates FI (C15)"),
    (13, "Complications et pronostic", "couvert", "g99-2.5, g99-8"),
    (14, "Suivi, prévention, dépistage", "partiel", "g99-10 ; intervalle de dépistage de la neuropathie autonome absent ; histoire naturelle (E01)"),
    (15, "Situations particulières", "partiel", "g99-11 ; grossesse limitée à la contre-indication de la midodrine"),
    (16, "Spécificités suisses", "partiel", "g99-12 ; conduite (C10) ; AI et Liste des spécialités non documentées"),
    (17, "Critères formels du diagnostic (div.alert)", "couvert", "g99-13"),
    (18, "Paramètres clés chiffrés (div.key)", "couvert", "g99-13"),
    (19, "Sous-codes CIM-10-GM couverts", "absent", "aucun sous-code G99.x cité (C02)"),
    (20, "Points d’examen fédéral", "couvert", "g99-12 (PROFILES 103, 104 et rattachements pédagogiques ; pièges)"),
]

SEM = {
    "SEM-01": "non (data-s : g99-s-anat, g99-s-histo, g99-s-physio, g99-s-bioch ; aucun g99-s-semio)", "SEM-02": "non", "SEM-03": "non (audit_sciences : failed, 21 erreurs)",
    "SEM-04": "oui pour la leçon actuelle (test_v7.py --static G99 : OK)", "SEM-05": "non", "SEM-06": "non (« technique précise … non détaillée », g99-signes-mcd)",
    "SEM-07": "non", "SEM-08": "non (pourcentages d’accord pris pour des valeurs, C03)", "SEM-09": "non", "SEM-10": "partiel (pièges g99-4, g99-5, g99-6)",
    "SEM-11": "non", "SEM-12": "non", "SEM-13": "non dans les Sciences (alert g99-8 présente dans l’onglet 1)", "SEM-14": "partiel (g99-7.5 : trois différentiels avec indice)",
    "SEM-15": "non", "SEM-16": "non", "SEM-17": "non (quatre cas en g99-e-6, aucun sur la valeur d’un signe)", "SEM-18": "non évaluable (absente)",
    "SEM-19": "non évaluable (absente)", "SEM-20": "non (« au plus 10 » contre « habituellement », C17)", "SEM-21": "non évaluable", "SEM-22": "non (bouton absent)",
    "SEM-23": "non (aucune capture possible)", "SEM-24": "oui (statut « Revue par intelligence artificielle · Aucune validation médicale humaine »)",
}

LACUNES = [
    "Aucune recommandation suisse propre à la neuropathie autonome diabétique, à la gastroparésie diabétique ou à la neuropathie urémique n’a été trouvée ; RMS 2024 (gastroparésie) et RMS 2025 (hypotension du sujet âgé) lus au résumé seulement (accès payant).",
    "ESC 2018 lu sur les caractères 0 à 200 000 de la page (sections 4 et 5) ; les instructions pratiques web (durée du lever actif, tableau web 1) et le tableau de conduite de l’ESC n’ont pas été lus.",
    "Consensus de Toronto 2011 lu au résumé : valeurs de coupure des tests cardiovasculaires réflexes non lues ; intervalle de dépistage de la neuropathie autonome non trouvé dans une source suisse ou européenne.",
    "Seuils diagnostiques de rétention scintigraphique à 2 et 4 heures : absents du consensus UEG/ESNM ; aucune source européenne lue (les seuils usuels proviennent d’un consensus nord-américain, non utilisé).",
    "Posologie des corticoïdes et délai de radiothérapie dans la compression médullaire métastatique : aucune source suisse ou européenne lue (NICE NG234 et ESMO non consultés).",
    "Figures : aucun original anatomique validé (Commons HTTP 429 ; délai stocké ; aucune relance conformément à la consigne) ; contrôle visuel à 390 px et captures réelles (SEM-22, SEM-23) non réalisés.",
    "Inotersen : aucune information professionnelle suisse trouvée par tools/swissmedic_fi.py (recherche « tegsedi » vide).",
    "Sources lues au résumé : S6, S10, S14, S15, S16, S19, S20 ; sections seulement : S4, S17, S26 à S31.",
    "AI, Liste des spécialités et remboursement des traitements (midodrine, prokinétiques, traitements de l’ATTRv) non recherchés.",
    "Le recalcul est complet (406/406) ; les sommes et doses des propositions d’enrichissement sont recalculées (E01 à E09 dans resultats.json).",
]


def main():
    lect = {}
    ok = True
    for f in FICHIERS:
        h = hashlib.sha256((R / f).read_bytes()).hexdigest()
        m = MANIFESTE["source_files_sha256"][f]
        lect[f] = {"sha256": h, "manifeste": m, "conforme": h == m}
        ok &= h == m
    textes = {f: (R / f).read_text(encoding="utf-8") for f in FICHIERS}
    for c in CONSTATS:
        assert len(c["ancre"]) <= 200, c["id"]
        assert c["ancre"] in textes[c["fichier"]], ("ancre absente", c["id"])
    calc = json.loads((ICI / "calculs/resultats.json").read_text(encoding="utf-8"))
    synth = {g: sum(1 for c in CONSTATS if c["gravite"] == g) for g in ("BLOQUANT", "MAJEUR", "MINEUR", "ENRICHISSEMENT")}
    doc = {
        "mission": "ALPHA1-CLAUDE-G99-MED", "code": "G99", "type_audit": "medical",
        "base_sha": "103745baaa38c76f18288758cc7f689e5091ccdb",
        "source_snapshot_sha": MANIFESTE["source_snapshot_sha"],
        "base_note": "HEAD du worktree au démarrage (fusion de la PR #203) ; manifeste : base 523832d9 ; empreintes SHA-256 des 7 fichiers conformes.",
        "generation": 1, "branche": "claude/alpha1/g99-med-g1",
        "worktree": "/tmp/claude-0/-home-user-Medina/bd99f81d-6b1e-5698-bd58-22e14f9e16b4/scratchpad/missions/ALPHA1-CLAUDE-G99-MED",
        "conversation": "alpha1-claude-g99-med", "agent_executant": "sous-agent Claude Code (voir accusé issue 107)",
        "modele_effort": "conforme au manifeste", "date_debut": "2026-10-16T09:50:00Z", "date_fin": "2026-10-16T10:40:00Z",
        "lecture": {"fichiers": FICHIERS, "empreintes_conformes": ok, "empreintes": lect},
        "premiere_source_lue": {"source_id": "S1", "url": "https://klassifikationen.bfarm.de/icd-10-gm/kode-suche/htmlgm2024/block-g90-g99.htm",
                                "section": "G99.-* : G99.0-* (G99.00*, G99.08*), G99.1*, G99.2*, G99.8* « Urämische Paralyse (N18.-†) »"},
        "synthese": synth,
        "calculs": {k2: calc[k2] for k2 in ("total_releves", "calculables", "recalcules", "correct", "arrondi")} | {
            "faux": calc["faux"], "non_verifiables": calc["non_verifiables"], "references_bibliographiques_exclues": calc["references_bibliographiques_exclues"],
            "script": "calculs/verifier.py", "inventaire": "calculs/inventaire.py → calculs/inventaire.json", "resultats": "calculs/resultats.json",
            "enrichissements_recalcules": ["E01", "E02", "E03", "E04", "E05", "E06", "E07", "E08", "E09"],
            "observations": [
                "12 occurrences FAUX : pourcentages d’accord UEG/ESNM présentés comme fréquence, validité ou efficacité (C03).",
                "8 ARRONDI : QTc 415/445 ms pour 415,1/444,9 ms ; « Plus de 50 ans » pour « in their 50s » ; « au plus 10 » pour « usually not >10 » (C17).",
                "Cas récapitulatif : ΔPAS 25 et ΔPAD 10 mmHg (les deux critères ESC atteints, C21) ; quiz 1 : ΔPAS 22, ΔPAD 5 (réponse A juste).",
                "Midodrine : 3 × 2,5 = 7,5 mg/j au départ ; ESC 3 × 10 = 30 mg/j = plafond FI omis (C11). Fludrocortisone : ESC 0,3 mg/j > FI 0,2 mg/j (C12).",
                "Métoclopramide : max = min(30 mg ; 0,5 mg/kg) ; égalité à 60 kg ; 15 mg/j (ClCr 15–60) et 7,5 mg/j (ClCr ≤ 15) après réduction.",
                "108/183 = 59,02 % ; 32,4 + 15,8 = 48,2 % ; 15/18 = 83,3 % ; 5,2/1,0 = 5,2 ; bornes 6–73 % recalculées.",
                "Propositions : patisiran 21 mg pour 70 kg, 30 mg à 100 kg (= plafond FI) ; Cook : probabilité post-test 94,4 % ; figure 6 : 144 px et 19,8 px."]},
        "controles": {
            "test_v7_static": "G99 mots 11167 fenêtres 37 quiz 4 pareto 13 — OK (leçon actuelle)",
            "audit_sciences": "failed : 21 erreurs (4 disciplines < 280 mots, aucune figure en biochimie, libellés absents)",
            "image_clo_finder_inventory": "5 figures SVG, 0 image ; 2 ANATOMIQUE_IA (figures 3 et 4), 3 SCHEMA_NON_ANATOMIQUE (1, 2, 5)",
            "propositions_ancres_uniques": "43/43 (propositions/verification_ancres.json)",
            "propositions_appliquees_copie": "test_v7.py --static G99 : mots 15896 fenêtres 46 quiz 7 pareto 13 — OK ; tests/audit_sciences.py : passed (g99-s-semio 2162 mots, anat 374, histo 311, physio 305, bioch 319)",
            "propositions_marqueurs": "Les marqueurs [Sx] renvoient à sources.json de l’audit ; appliquer_copie.py les retire avant contrôle."},
        "constats": CONSTATS,
        "matrice_20": [{"rang": r, "rubrique": n, "statut": s, "ancre": a} for r, n, s, a in MATRICE],
        "semiologie": {
            "statut": "absente", "decompte_data_s": 4, "data_s": ["g99-s-anat", "g99-s-histo", "g99-s-physio", "g99-s-bioch"], "sous_onglet_semio": False,
            "gravite": "MAJEUR", "constat_id": "C01",
            "fondamentale": {"statut": "partielle dans l’onglet 1, absente comme discipline", "ancres": ["g99-5", "g99-6", "g99-signes-mcd", "g99-orthostase"],
                             "manques": "technique des signes pyramidaux, mécanisme par signe, valeur chiffrée (Hoffmann, Babinski, clonus, hyperréflexie), normal avant pathologique"},
            "analytique": {"statut": "absente", "ancres": [], "manques": "regroupement syndromique, raisonnement en cinq étapes, examen systématique, synthèse présentée, cas sur la valeur d’un signe"},
            "proposition": ["propositions/G99_c_semio.html", "propositions/G99_pop1_semio.html"],
            "grille_SEM": SEM,
            "lacune_valeurs": "Valeur sémiologique non chiffrée dans les sources lues pour l’intolérance à l’effort, les symptômes de gastroparésie (seulement « poor predictors ») et la douleur rachidienne du patient cancéreux."},
        "figures": [
            {"figure": "Figure 1 (G99_a, g99-3)", "classe": "SCHEMA_NON_ANATOMIQUE", "statut": "recevable ; nom accessible à corriger (C20)"},
            {"figure": "Figure 2 (G99_b, g99-7)", "classe": "SCHEMA_NON_ANATOMIQUE", "statut": "recevable ; nom accessible à corriger (C20)"},
            {"figure": "Figure 3 « Moelle comprimée » (G99_c, g99-s-anat)", "classe": "ANATOMIQUE_IA", "statut": "MAJEUR (C07) ; remplacement par schéma causal proposé ; aucun original validé"},
            {"figure": "Figure 4 « Fibre nerveuse » (G99_c, g99-s-histo)", "classe": "ANATOMIQUE_IA", "statut": "MAJEUR (C07) ; remplacement par schéma causal proposé ; aucun original validé"},
            {"figure": "Figure 5 (G99_c, g99-s-physio)", "classe": "SCHEMA_NON_ANATOMIQUE", "statut": "recevable ; nom accessible à corriger (C20)"}],
        "lacunes": LACUNES,
        "propositions": ["propositions/G99_c_semio.html", "propositions/G99_pop1_semio.html", "propositions/G99_c_sciences.html", "propositions/G99_pop2_attr.html",
                         "propositions/corrections.py", "propositions/G99_corrections.html", "propositions/verification_ancres.json",
                         "propositions/glossary_g99_ajouts.py", "propositions/appliquer_copie.py"],
        "mention": "Audit IA — revue distincte d’une validation médicale humaine ; aucune source canonique modifiée",
    }
    (ICI / "rapport.json").write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(synth, "empreintes", ok, "ancres OK", len(CONSTATS))


if __name__ == "__main__":
    main()
