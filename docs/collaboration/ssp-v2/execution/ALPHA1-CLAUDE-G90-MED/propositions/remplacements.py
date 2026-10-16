#!/usr/bin/env python3
"""Génère remplacements.json : propositions locales (ancien → nouveau) de l'audit ALPHA1-CLAUDE-G90-MED,
et vérifie que chaque « ancien » apparaît exactement une fois dans le fichier figé (git show 523832d9…).
Usage : python3 remplacements.py <racine_du_depot>"""
import json, subprocess, sys, os
SHA = "523832d9ef6097607d3443f4398deee9cd0add11"
root = sys.argv[1] if len(sys.argv) > 1 else "."
R = [
 # C02 — dysréflexie : inhibiteurs de la PDE5, forme non commercialisée en Suisse
 ("C02", "chapters/G90/G90_b.html",
  "un nitrate (pâte de nitroglycérine à 2 % au-dessus du niveau lésionnel, retirée dès l’effet) est décrit",
  "un nitrate (pâte de nitroglycérine à 2 % au-dessus du niveau lésionnel, retirée dès l’effet) est décrit par la source américaine ; aucune pâte de nitroglycérine à 2 % n’a d’information professionnelle suisse, et l’information suisse de Nitroderm TTS contre-indique l’association avec les inhibiteurs de la phosphodiestérase de type 5 (sildénafil, tadalafil, vardénafil) et dans les 24 heures qui suivent leur prise <a href=\"https://amiko.oddb.org\" target=\"_blank\" rel=\"noopener\">Information professionnelle suisse Nitroderm TTS (AIPS, septembre 2026)</a>. Le médecin demande donc cette prise avant tout nitré"),
 ("C02", "chapters/G90/G90_pop1.html",
  "Si nécessaire, nitrate (pâte de nitroglycérine à 2 % au-dessus du niveau lésionnel, retirée dès l’effet)",
  "Si nécessaire, nitrate (pâte de nitroglycérine à 2 % au-dessus du niveau lésionnel, retirée dès l’effet), après avoir vérifié l’absence de prise d’un inhibiteur de la phosphodiestérase de type 5 dans les 24 heures : l’association est contre-indiquée par l’information suisse de Nitroderm TTS (septembre 2026). Aucune pâte de nitroglycérine à 2 % n’a d’information professionnelle suisse (recherche AmiKo du 16.10.2026)"),
 ("C02", "chapters/G90/G90_pop2.html",
  "Nitrate (pâte de nitroglycérine à 2 % au-dessus du niveau lésionnel, retirée dès l’effet)",
  "Nitrate (pâte de nitroglycérine à 2 % au-dessus du niveau lésionnel, retirée dès l’effet ; forme sans information professionnelle suisse ; contre-indiqué avec un inhibiteur de la phosphodiestérase de type 5 et dans les 24 heures qui suivent, selon l’information suisse de Nitroderm TTS)"),
 # C03 — midodrine : contre-indications et populations
 ("C03", "chapters/G90/G90_d.html",
  "Contre-indications : cardiopathie organique sévère (bradycardie, coronaropathie",
  "Contre-indications (information suisse, mai 2024) : grossesse et allaitement, phéochromocytome, hyperthyroïdie, glaucome à angle fermé ; l’emploi chez l’enfant et l’adolescent est exclu faute de données. S’y ajoutent : cardiopathie organique sévère (bradycardie, coronaropathie"),
 ("C03", "chapters/G90/G90_b.html",
  "Aucune source lue ne traite la grossesse, l’insuffisance rénale ou hépatique pour ces entités",
  "L’information suisse contre-indique la midodrine pendant la grossesse et l’allaitement et en cas d’insuffisance rénale sévère ; elle demande une adaptation de dose en cas d’insuffisance rénale légère à modérée et un contrôle hépatique, faute d’étude chez l’insuffisant hépatique <a href=\"https://amiko.oddb.org\" target=\"_blank\" rel=\"noopener\">Information professionnelle suisse Midodrin Substipharm (AIPS)</a>. Aucune autre source lue ne traite la grossesse, l’insuffisance rénale ou hépatique pour ces entités"),
 # C04 — tachycardie posturale : critères chiffrés
 ("C04", "chapters/G90/G90_pop1.html",
  "Les seuils chiffrés de fréquence cardiaque et de durée n’ont pas été lus et ne sont pas donnés ici",
  "Le consensus de 2021 retient une accélération soutenue de plus de 30 battements par minute, ou une fréquence de plus de 120 par minute, dans les 10 minutes de station debout ou d’inclinaison, sans chute de pression répondant aux critères d’hypotension orthostatique ; de 12 à 19 ans, l’accélération requise dépasse 40 battements par minute. Le diagnostic exige aussi des symptômes d’intolérance orthostatique (Recommandations sur le test d’inclinaison, Thijs 2021, tableau 1)"),
 ("C04", "chapters/G90/G90_a.html",
  "Accélération cardiaque excessive au lever avec intolérance orthostatique",
  "Accélération cardiaque de plus de 30 battements par minute (plus de 40 de 12 à 19 ans), ou au-delà de 120 par minute, dans les 10 minutes de station debout, avec intolérance orthostatique et sans hypotension orthostatique"),
 # C05 — forme initiale et rapport fréquence/pression (enrichissement)
 ("C05", "chapters/G90/G90_a.html",
  "initiale (dans les premières secondes, elle exige une mesure continue battement par battement)",
  "initiale (chute transitoire de plus de 40 mmHg de systolique ou de plus de 20 mmHg de diastolique dans les 15 secondes, qui exige une mesure continue battement par battement ; Thijs 2021, tableau 1)"),
 # C06 — massage sinocarotidien : précautions
 ("C06", "chapters/G90/G90_c.html",
  "La technique et les contre-indications détaillées n’ont pas été lues ; elles ne sont donc pas décrites ici.",
  "Les complications restent inférieures à 0,5 %, surtout neurologiques et transitoires, mais des AVC et un décès ont été rapportés : selon l’ESC, le massage se fait avec prudence après un AVC ou un accident ischémique transitoire, ou en cas de sténose carotidienne de plus de 70 % <a href=\"https://doi.org/10.1016/j.autneu.2021.102792\" target=\"_blank\" rel=\"noopener\">Recommandations sur le test d’inclinaison (Thijs 2021)</a>. La technique détaillée n’a pas été lue."),
 # C07 — dysréflexie : la fréquence cardiaque ne tranche pas
 ("C07", "chapters/G90/G90_c.html",
  "Une bradycardie devant une hypertension chez un blessé médullaire dénonce la dysréflexie.",
  "Une hypertension brutale chez un blessé médullaire haut dénonce la dysréflexie, que le pouls soit lent ou rapide : la bradycardie est classique, mais la tachycardie est observée aussi souvent dans une série et plus souvent dans d’autres."),
 ("C07", "chapters/G90/G90_a.html",
  "Hypertension épisodique avec bradycardie réflexe",
  "Hypertension épisodique, classiquement avec bradycardie réflexe (une tachycardie est aussi fréquente)"),
 ("C07", "chapters/G90/G90_pop1.html",
  "Hypertension épisodique avec bradycardie réflexe (baroréflexe)",
  "Hypertension épisodique, classiquement avec bradycardie réflexe (baroréflexe) ; une tachycardie est observée aussi souvent dans la série de Lindan et plus souvent dans d’autres séries : la fréquence cardiaque ne tranche pas"),
 # C08 — contrat des sciences : libellé « À retenir. » absent des trois disciplines (tests/audit_sciences.py)
 ("C08", "chapters/G90/G90_c.html", "<button class=\"pareto-btn ui\" data-k=\"pareto-g90-s-anat\">",
  "<div class=\"key\"><b>À retenir.</b> La voie oculosympathique compte trois neurones ; l’étage lésé se déduit de la topographie de l’anhidrose et des signes associés, et il choisit l’imagerie : IRM pour le premier ordre, angioscanner des orbites jusqu’à T4–T5 pour les deuxième et troisième ordres.</div>\n<button class=\"pareto-btn ui\" data-k=\"pareto-g90-s-anat\">"),
 ("C08", "chapters/G90/G90_c.html", "<button class=\"pareto-btn ui\" data-k=\"pareto-g90-s-physio\">",
  "<div class=\"key\"><b>À retenir.</b> Le baroréflexe se juge à la fréquence cardiaque : un cœur qui ne s’accélère pas devant une chute de pression désigne un arc défaillant. Sous une lésion médullaire haute, le même réflexe privé de frein produit la dysréflexie, avec un pouls lent ou rapide.</div>\n<button class=\"pareto-btn ui\" data-k=\"pareto-g90-s-physio\">"),
 ("C08", "chapters/G90/G90_c.html", "<button class=\"pareto-btn ui\" data-k=\"pareto-g90-s-genet\">",
  "<div class=\"key\"><b>À retenir.</b> La dysautonomie familiale est autosomique récessive : deux parents porteurs ont, à chaque grossesse, un risque de 1 sur 4 d’avoir un enfant atteint. La ganglionopathie auto-immune se cherche par les anticorps anti-récepteur ganglionnaire ; le syndrome douloureux régional complexe n’a pas de biomarqueur validé.</div>\n<button class=\"pareto-btn ui\" data-k=\"pareto-g90-s-genet\">"),
 # MINEURS
 ("M01", "chapters/G90/G90_b.html", "environ 15 % ne sont pas améliorés à 2 ans, environ 40 % gardent", "environ 40 % gardent"),
 ("M01", "chapters/G90/G90_b.html", "avis spécialisé à 2 mois ; 15 % non améliorés à 2 ans.", "avis spécialisé à 2 mois ; 15 à 20 % de syndromes non résolus."),
 ("M02", "chapters/G90/G90_c.html", "dans 25 % ; angioscanner", "jusqu’à 25 % ; angioscanner"),
 ("M03", "chapters/G90/G90_pop2.html", "Le consensus de 2018 a introduit le seuil de 90 mmHg", "La recommandation ESC de 2018 a ajouté le seuil de 90 mmHg au consensus de 2011"),
 ("M04", "chapters/G90/G90_b.html", "Une hypertension de décubitus sévère (au moins 180/110 mmHg)", "Une hypertension de décubitus sévère (systolique d’au moins 180 mmHg ou diastolique d’au moins 110 mmHg)"),
 ("M05", "chapters/G90/G90_b.html", "(cible de pression systolique de 140 mmHg chez l’hypertendu âgé)", "(l’ESC propose une cible systolique de 140 mmHg chez l’hypertendu âgé dans la syncope réflexe ; l’hypotension orthostatique médicamenteuse se traite d’abord par le retrait du médicament en cause)"),
 ("M06", "chapters/G90/G90_d.html", "L’ESC 2018 la propose à 0,1–0,3 mg une fois par jour", "L’ESC 2018 la propose à 0,1–0,3 mg une fois par jour ; la borne de 0,3 mg dépasse la posologie usuelle maximale de l’information suisse (0,2 mg par jour)"),
 ("M07", "chapters/G90/G90_pop1.html", "G90.4- dysréflexie autonome (G90.40 crises hypertensives, G90.41 crises de transpiration)", "G90.4- dysréflexie autonome (G90.40 crises hypertensives, G90.41 crises de transpiration, G90.48 autres, G90.49 sans précision) ; G90.5-, G90.6- et G90.7- se subdivisent selon la localisation (membre supérieur, membre inférieur, non précisée)"),
 ("M08", "chapters/G90/G90_c.html", "blessé médullaire au niveau du 5e segment thoracique, a une céphalée violente", "blessé médullaire au niveau du 5e segment thoracique, dont la pression habituelle est de 100/60 mmHg, a une céphalée violente"),
 ("M09", "chapters/G90/G90_c.html", "Un homme de 68 ans sans syncope présente une pause de 4 secondes", "Un homme de 68 ans sans syncope, examiné pendant un bilan cardiologique, présente une pause de 4 secondes"),
 ("M10", "chapters/G90/G90_d.html", "Toxine botulique ou fésotérodine sur la suractivité détrusorienne ; prazosine", "Toxine botulique ou fésotérodine sur la suractivité détrusorienne ; prazosine (aucune information professionnelle suisse trouvée ; elle antagonise la midodrine)"),
 ("M11", "chapters/G90/G90_a.html", "Fréquente chez l’homme âgé sans syncope (jusqu’à 40 %)", "Fréquente chez l’homme âgé sans syncope ; réponses anormales jusqu’à 40 % chez les patients sans syncope"),
 ("M12", "chapters/G90/G90_a.html", "Pour les formes neurogènes, le consensus AAS/EFAS 2018 relève le seuil à 30 mmHg", "Pour les formes neurogènes, la définition de 2011, reprise par le consensus AAS/EFAS 2018, relève le seuil à 30 mmHg"),
 ("M13", "chapters/G90/G90_b.html", "ou systolique < 90 mmHg, progressive", "ou systolique &lt; 90 mmHg, progressive"),
 ("M14", "chapters/G90/G90_b.html", "mesurer assis et debout avant d’intensifier un traitement", "mesurer assis, puis debout si la différence systolique dépasse 10 mmHg, avant d’intensifier un traitement"),
 # ENRICHISSEMENTS locaux
 ("E02", "chapters/G90/G90_b.html", "Horner : traitement de la cause", "Horner : traitement de la cause ; en cas de dissection cervicale, la recommandation européenne laisse le choix entre antiplaquettaire et anticoagulant à la phase aiguë, et maintient thrombolyse et thrombectomie selon les critères habituels en cas d’infarctus cérébral <a href=\"https://pmc.ncbi.nlm.nih.gov/articles/PMC8564160/\" target=\"_blank\" rel=\"noopener\">ESO 2021 sur les dissections artérielles (résumé)</a>"),
 ("E03", "chapters/G90/G90_d.html", "La midodrine est le seul médicament de l’hypotension orthostatique avec indication suisse documentée dans les sources lues.", "La midodrine est le seul médicament de l’hypotension orthostatique avec indication suisse documentée dans les sources lues. Elle existe en comprimés (Midodrin Substipharm 2,5 et 5 mg, hors liste des spécialités) et en gouttes (Gutron 10 mg/mL, 30 gouttes par mL, sur la liste des spécialités) ; 7 gouttes apportent 2,3 mg. Florinef figure sur la liste des spécialités ; son emploi dans l’hypotension orthostatique reste hors étiquette."),
 ("E04", "chapters/G90/G90_pop2.html", "La description du protocole (durée, pression expiratoire) n’a pas été lue et n’est pas donnée ici.", "Le patient expire de façon forcée pendant 15 secondes, glotte ouverte, ou contre une résistance de 40 mmHg ; la respiration profonde se fait à six cycles par minute pendant 1 minute. Le patient est à jeun depuis 3 heures et sans caféine ni nicotine le jour du test (Thijs 2021)."),
 ("E05", "chapters/G90/G90_a.html", "Sur 88 Horner isolés, 7 étaient des dissections, dont 6 douloureux", "Sur 88 Horner isolés, 7 étaient des dissections, dont 6 douloureux ; inversement, un Horner est présent dans jusqu’à 58 % des dissections carotidiennes, derrière la douleur et l’ischémie focale"),
 ("E06", "chapters/G90/G90_c.html", "Apraclonidine 0,5 % (préférée)", "Apraclonidine 0,5 % (préférée ; en Suisse, Iopidine 0,5 % est autorisée pour le glaucome : usage hors étiquette)"),
 # C01 — marqueur de la sémiologie clinique de l'onglet 1 (contrat SEMIOLOGIE_FONDAMENTALE_ANALYTIQUE)
 ("C01", "chapters/G90/G90_a.html", "id=\"g90-6\"", "id=\"g90-6\" data-semiology-clinical=\"G90\""),
]
out = []
ok = True
for id_, f, old, new in R:
    s = subprocess.run(["git", "-C", root, "show", f"{SHA}:{f}"], capture_output=True, check=True).stdout.decode("utf-8")
    n = s.count(old)
    ok &= (n == 1)
    out.append({"constat": id_, "fichier": f, "ancien": old, "nouveau": new, "occurrences_ancien": n, "fond_medical_modifie": id_[0] in "CE"})
json.dump({"source_snapshot_sha": SHA, "verification_unicite": ok, "remplacements": out},
          open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "remplacements.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("remplacements:", len(out), "unicité:", ok)
