#!/usr/bin/env python3
"""ALPHA1-CLAUDE-G93-MED — remplacements locaux proposés (ancien → nouveau) et contrôle mécanique d'unicité.

Exécution depuis la racine du dépôt :
    python3 docs/collaboration/ssp-v2/execution/ALPHA1-CLAUDE-G93-MED/propositions/remplacements.py
Écrit remplacements.json à côté du script et vérifie que chaque « ancien » apparaît exactement une fois
dans son fichier. Aucune écriture dans chapters/ ni glossary/.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
R = []


def add(id_, constat, fichier, ancien, nouveau, motif):
    R.append({"id": id_, "constat": constat, "fichier": fichier, "ancien": ancien, "nouveau": nouveau, "motif": motif})


B, A, C, D, P1, P2, G = ("chapters/G93/G93_b.html", "chapters/G93/G93_a.html", "chapters/G93/G93_c.html",
                         "chapters/G93/G93_d.html", "chapters/G93/G93_pop1.html", "chapters/G93/G93_pop2.html", "glossary/g93.py")

# ------------------------------------------------------------------ C01, C02, C04 : ERC-ESICM 2025
add("M01", "C04", B, "<tr><td>Dioxyde de carbone</td><td>PaCO₂ 4,5 à 6,0 kPa (35–45 mmHg)</td>",
    "<tr><td>Dioxyde de carbone</td><td>PaCO₂ 4,7 à 6,0 kPa (environ 35–45 mmHg)</td>",
    "ERC-ESICM 2025 [S5] ; 4,5 kPa = 33,8 mmHg ≠ 35 mmHg (R04, R05)")
add("M02", "C02", B, "<tr><td>Pression artérielle moyenne</td><td>Éviter moins de 65 mmHg ; viser une diurèse supérieure à 0,5 mL/kg/h et un lactate normal ou décroissant</td>",
    "<tr><td>Pression artérielle moyenne</td><td>Viser plus de 60 à 65 mmHg, avec un cathéter artériel ; adapter liquides, noradrénaline ou dobutamine au besoin du patient</td>",
    "ERC-ESICM 2025 [S5] « target a mean arterial pressure (MAP) >60–65 mmHg » (R10)")
add("M03", "C02", B, "<tr><td>Température</td><td>Cible constante entre 32 et 36 °C pendant au moins 24 heures ; éviter la fièvre (plus de 37,7 °C) pendant au moins 72 heures</td><td>La fièvre aggrave la lésion</td></tr>",
    "<tr><td>Température</td><td>Prévenir activement la fièvre en visant une température de 37,5 °C au plus, pendant 36 à 72 heures chez le patient resté comateux ; ne pas réchauffer activement une hypothermie légère (32–36 °C) ; pas de refroidissement préhospitalier par grands volumes de liquide froid</td><td>La fièvre aggrave la lésion ; aucune cible hypothermique n’a fait mieux qu’une cible normothermique</td></tr>",
    "ERC-ESICM 2025 [S5] : prévention de la fièvre, 36 à 72 h ; égalité des stratégies hypothermique et normothermique (R08, R10b)")
add("M04", "C02", B, "<div class=\"trap\"><span class=\"k\">Piège</span> Ces valeurs viennent des recommandations ERC-ESICM de 2021, lues dans leur texte intégral. La version 2025 existe ; son texte intégral n’a pas été lu dans ce dossier, et d’éventuelles modifications chiffrées ne sont donc pas reprises.</div>",
    "<div class=\"trap\"><span class=\"k\">Piège</span> Ces cibles sont celles des recommandations ERC-ESICM 2025. Elles remplacent trois valeurs de 2021 : la borne basse de la PaCO₂ passe de 4,5 à 4,7 kPa, la pression artérielle moyenne visée passe à plus de 60 à 65 mmHg, et la cible thermique constante de 32 à 36 °C cède la place à la prévention de la fièvre.</div>",
    "texte intégral 2025 lu [S5]")
add("M05", "C01", B, "Le patient doit rester comateux, avec une réponse motrice de 3 ou moins, à 72 heures ou plus du retour à une circulation spontanée.",
    "La stratégie s’applique au patient qui n’est pas éveillé et n’obéit pas aux ordres (réponse motrice inférieure à 6) à 72 heures ou plus du retour à une circulation spontanée ; la recommandation de 2021 retenait une réponse motrice de 3 ou moins, seuil qui laissait de côté la plupart des patients destinés à récupérer.",
    "ERC-ESICM 2025 [S5] (R09)")
add("M06", "C01", B, "<li>état de mal myoclonique avant 72 heures ;</li>",
    "<li>état de mal myoclonique, c’est-à-dire des myoclonies continues et généralisées de plus de 30 minutes, dans les 72 premières heures ;</li>",
    "définition 2025 [S5]")
add("M07", "C01", B, "<li>énolase neuronale spécifique supérieure à 60 µg/L à 48 et/ou 72 heures ;</li>",
    "<li>énolase neuronale spécifique supérieure à 60 µg/L à 48 et/ou 72 heures, dosée en série à 24, 48 et 72 heures ; une hausse entre ces dosages renforce le pronostic défavorable ;</li>",
    "[S5] dosages sériés")
add("M08", "C01", B, "Le syndrome de Lance-Adams (myoclonies généralisées avec décharges épileptiformes chez des patients qui se réveillent) rappelle que des myoclonies n’annoncent pas toujours un mauvais pronostic.</p>",
    "Le syndrome de Lance-Adams (myoclonies généralisées avec décharges épileptiformes chez des patients qui se réveillent) rappelle que des myoclonies n’annoncent pas toujours un mauvais pronostic.</p>\n<p>La version 2025 ajoute des <b>prédicteurs de récupération</b> : retrait ou localisation à la douleur (réponse motrice 4 ou 5) dans les quatre premiers jours, énolase neuronale spécifique normale (moins de 17 µg/L) dans les 72 heures, absence de restriction de diffusion à l’imagerie par résonance entre 72 heures et 7 jours, et tracé électroencéphalographique continu de voltage normal dans les 72 heures. Un signe favorable qui coexiste avec un signe défavorable impose la prudence : dans une cohorte, cette discordance s’accompagnait d’une récupération dans 11 % des cas, contre 3 % avec un signe défavorable seul. Si le premier scanner ne montre pas de lésion anoxique, il est répété au moment du pronostic, entre 72 et 96 heures.</p>",
    "[S5] « Prediction of good neurological outcome » et « Imaging »")
add("M09", "C01", B, "Au moins deux prédicteurs, une réponse motrice de 3 ou moins, 72 heures écoulées et aucun facteur confondant : c’est le seuil minimal d’un pronostic défavorable probable.",
    "Au moins deux prédicteurs défavorables, un patient qui n’obéit pas aux ordres à 72 heures, aucun facteur confondant et aucun prédicteur de récupération discordant : c’est le seuil minimal d’un pronostic défavorable probable.",
    "[S5]")
add("M10", "C01", B, "<u>Pronostic défavorable après arrêt cardiaque</u> : réponse motrice de 3 ou moins à 72 heures ou plus, facteurs confondants exclus, et au moins deux prédicteurs.",
    "<u>Pronostic défavorable après arrêt cardiaque</u> : patient qui n’obéit pas aux ordres (réponse motrice inférieure à 6) à 72 heures ou plus, facteurs confondants exclus, et au moins deux prédicteurs défavorables (ERC-ESICM 2025).",
    "[S5]")
add("M11", "C02", B, "Après arrêt cardiaque : saturation 94 à 98 %, PaCO₂ 4,5 à 6,0 kPa, pression artérielle moyenne d’au moins 65 mmHg, absence de fièvre au-delà de 37,7 °C pendant 72 heures, énolase neuronale spécifique supérieure à 60 µg/L à 48–72 heures.",
    "Après arrêt cardiaque (ERC-ESICM 2025) : saturation 94 à 98 %, PaCO₂ 4,7 à 6,0 kPa, pression artérielle moyenne de plus de 60 à 65 mmHg, prévention de la fièvre avec une température de 37,5 °C au plus pendant 36 à 72 heures, énolase neuronale spécifique supérieure à 60 µg/L à 48–72 heures.",
    "[S5] (R04–R10b)")
add("M12", "C04", C, "<div class=\"key\"><b>Corrélation clinique.</b> La normocapnie (PaCO₂ 4,5 à 6,0 kPa) après un arrêt cardiaque",
    "<div class=\"key\"><b>Corrélation clinique.</b> La normocapnie (PaCO₂ 4,7 à 6,0 kPa) après un arrêt cardiaque", "[S5]")
add("M13", "C04", P1, "Normocapnie, PaCO₂ de 4,5 à 6,0 kPa (35 à 45 mmHg). Pression artérielle moyenne d’au moins 65 mmHg, avec une diurèse supérieure à 0,5 mL/kg/h et un lactate normal ou décroissant. Température cible constante entre 32 et 36 °C pendant au moins 24 heures ; fièvre (plus de 37,7 °C) évitée pendant au moins 72 heures chez le patient resté comateux ; pas de solutés froids préhospitaliers.",
    "Normocapnie, PaCO₂ de 4,7 à 6,0 kPa (environ 35 à 45 mmHg) ; chez le patient hypothermique, la PaCO₂ est contrôlée souvent, car l’hypocapnie est fréquente. Pression artérielle moyenne de plus de 60 à 65 mmHg. Prévention active de la fièvre, avec une température de 37,5 °C au plus, pendant 36 à 72 heures chez le patient resté comateux ; une hypothermie légère n’est pas activement réchauffée ; pas de grands volumes de liquide froid préhospitaliers.",
    "[S5] Table 1 et concise guidelines")
add("M14", "C02", P1, "<div class=\"lab\">Limite</div><p>Ce sont les valeurs de la version 2021. La version 2025 (Intensive Care Medicine 2025) existe ; seul son résumé a été lu, de sorte que d’éventuelles modifications chiffrées ne figurent pas ici.</p>",
    "<div class=\"lab\">Ce qui a changé depuis 2021</div><p>La version 2025 relève la borne basse de la PaCO₂ de 4,5 à 4,7 kPa, abaisse la pression artérielle moyenne visée à plus de 60 à 65 mmHg et remplace la cible constante de 32 à 36 °C par la prévention de la fièvre. Les antiépileptiques de première ligne restent le lévétiracétam et le valproate de sodium ; un essai de réveil est tenté chez le patient myoclonique dont le tracé est bénin.</p>",
    "[S5] Table 1")
add("M15", "C01", P1, "<div class=\"lab\">Condition d’entrée</div><p>Patient comateux avec réponse motrice de 3 ou moins à 72 heures ou plus du retour à la circulation spontanée,",
    "<div class=\"lab\">Condition d’entrée</div><p>Patient qui n’est pas éveillé et n’obéit pas aux ordres (réponse motrice inférieure à 6) à 72 heures ou plus du retour à la circulation spontanée (version 2025 ; la version 2021 retenait une réponse motrice de 3 ou moins),",
    "[S5]")
add("M16", "C01", P2, "<li>Pronostic : exclure les confondants, 72 heures, réponse motrice de 3 ou moins, au moins deux prédicteurs.</li>",
    "<li>Pronostic : exclure les confondants, 72 heures, patient qui n’obéit pas aux ordres, au moins deux prédicteurs défavorables, rechercher les signes de récupération.</li>", "[S5]")
add("M17", "C02", P2, "<li>Après arrêt cardiaque : saturation 94 à 98 %, normocapnie, pression artérielle moyenne d’au moins 65 mmHg, pas de fièvre.</li>",
    "<li>Après arrêt cardiaque : saturation 94 à 98 %, normocapnie, pression artérielle moyenne de plus de 60 à 65 mmHg, prévention de la fièvre.</li>", "[S5]")
add("M18", "C01", B, "<a href=\"https://pmc.ncbi.nlm.nih.gov/articles/PMC7993077/\" target=\"_blank\" rel=\"noopener\">ERC-ESICM 2021, soins post-réanimation</a>",
    "<a href=\"https://doi.org/10.1016/j.resuscitation.2025.110809\" target=\"_blank\" rel=\"noopener\">ERC-ESICM 2025, soins post-réanimation</a> (et version 2021 pour l’historique)",
    "référence la plus récente [S5]")

# ------------------------------------------------------------------ C05, C06, C08, C12 : pharmacologie
add("M20", "C05", D, "Le topiramate ne se prescrit pas pendant la grossesse.</p>",
    "Le topiramate est contre-indiqué pendant la grossesse et, dans la prévention de la migraine, chez toute femme en âge de procréer qui n’utilise pas une contraception hautement efficace ; un programme de prévention de la grossesse impose un test de grossesse avant l’instauration et une réévaluation au moins annuelle. Il diminue en outre l’efficacité des contraceptifs hormonaux systémiques (induction du CYP3A4) : une méthode barrière doit alors être associée.</p>\n<div class=\"alert\"><b>Associations à éviter.</b> L’information professionnelle suisse du topiramate demande d’éviter son association à l’acétazolamide, autre inhibiteur de l’anhydrase carbonique, car elle augmente le risque de calculs rénaux. Celle du Diamox® signale que l’association de l’acétazolamide à l’acide acétylsalicylique à doses élevées peut provoquer une acidose métabolique sévère et une toxicité accrue sur le système nerveux central. L’acétazolamide augmente aussi l’excrétion du lithium et peut élever la ciclosporinémie.</div>",
    "FI Topamax® juin 2026 [S14] ; FI Diamox® juillet 2026 [S11]")
add("M21", "C08", D, "<td>Comprimés de 250 mg ; dose de l’hypertension idiopathique non extraite de l’information professionnelle. Dans l’essai IIHTT, 4 g/jour pour plus de 40 % des patients, dose souvent mal tolérée ; 48 % d’arrêts à 1500 mg dans des études antérieures</td>",
    "<td>Comprimés de 250 mg. L’information professionnelle suisse ne donne <b>aucune</b> posologie pour l’HII ; ses posologies orales maximales sont de 1000 mg par 24 heures (glaucome, épilepsie). Dans l’essai IIHTT, plus de 40 % des patients ont reçu 4 g par jour, soit 16 comprimés et 4 fois ce maximum ; 48 % des patients arrêtaient déjà à 1500 mg dans des études antérieures. Toute dose au-delà du libellé relève d’un usage hors indication décidé par le spécialiste, avec contrôle de la formule sanguine et des électrolytes. Enfant : Swisspeddose donne, pour une pression intracrânienne élevée, 8 à 10 mg/kg par dose trois fois par jour, au maximum 100 mg/kg/jour ; l’administration pédiatrique n’a pas été étudiée selon l’information professionnelle</td>",
    "FI Diamox® [S11] (R28–R31)")
add("M22", "C05", D, "<td><button class=\"w\" data-k=\"g93-topiramate\">Topiramate</button></td><td>Dose non sourcée dans le dossier</td><td>Information professionnelle suisse non lue</td>",
    "<td><button class=\"w\" data-k=\"g93-topiramate\">Topiramate</button></td><td>Dose de l’HII non fixée : l’HII ne figure pas parmi ses indications (épilepsie ; prévention de la migraine dès 16 ans)</td><td>Information professionnelle suisse Topamax®, juin 2026 ; contre-indications liées à la grossesse et à la contraception</td>",
    "FI Topamax® [S14]")
add("M23", "C05", P2, "<div class=\"lab\">Limite</div><p>L’information professionnelle suisse du topiramate n’a pas été lue ; l’hypertension idiopathique n’est pas dans son libellé selon ce dossier. Aucune dose n’est donnée.</p>",
    "<div class=\"lab\">Information professionnelle suisse</div><p>Le Topamax® est autorisé dans l’épilepsie et la prévention de la migraine dès 16 ans ; l’HII n’en fait pas partie. Il est contre-indiqué pendant la grossesse et, en prévention de la migraine, chez la femme en âge de procréer sans contraception hautement efficace ; il réduit l’efficacité des contraceptifs hormonaux. Son association à l’acétazolamide est à éviter (risque de calculs rénaux). Il expose à une acidose métabolique hyperchlorémique : le bicarbonate sérique est contrôlé. Aucune dose de l’HII n’est fixée par le libellé.</p>",
    "FI Topamax® juin 2026 [S14]")
add("M24", "C06", D, "<p>L’acétazolamide est contre-indiqué en cas d’hyponatrémie, d’hypokaliémie, d’insuffisance rénale ou hépatique grave, d’insuffisance surrénalienne, d’acidose hyperchlorémique ou d’hypersensibilité aux sulfamides.",
    "<p>L’acétazolamide est contre-indiqué en cas d’hyponatrémie, d’hypokaliémie, d’insuffisance rénale ou hépatique grave, d’insuffisance surrénalienne, d’acidose hyperchlorémique ou d’hypersensibilité aux sulfamides ; un traitement au long cours est aussi contre-indiqué dans le glaucome chronique non congestif à angle fermé, dont l’aggravation serait masquée.",
    "FI Diamox® [S11]")
add("M25", "C12", P2, "<div class=\"lab\">Surveillance</div><p>Pression veineuse centrale, fonction rénale, électrolytes et trou osmotique.",
    "<div class=\"lab\">Délai et durée d’action</div><p>La pression intracrânienne baisse dès 15 minutes après le début de la perfusion ; l’effet est maximal en 30 à 60 minutes et dure 3 à 8 heures après la fin de la perfusion. La solution contient 200 g de mannitol par litre, soit une osmolarité théorique d’environ 1100 mOsm/L : 500 mL apportent 100 g, ce qui correspond à 1 à 2 g/kg seulement pour un poids de 50 à 100 kg.</p>\n<div class=\"lab\">Interactions</div><p>Contrôler la lithémie sous lithium ; surveiller la néphrotoxicité sous ciclosporine ; ne jamais administrer simultanément du sang et du mannitol sans électrolytes.</p>\n<div class=\"lab\">Surveillance</div><p>Pression veineuse centrale, fonction rénale, électrolytes et trou osmotique.",
    "FI Mannitol 20 % B. Braun, novembre 2025 [S12] ; masse molaire [S21] (R23–R27)")

# ------------------------------------------------------------------ C10 : engagement
add("M30", "C10", A, "Les sources retenues pour ce cours ne décrivent pas les types cliniques d’engagement ni leurs signes précis : le lecteur ne trouvera donc pas ici de description détaillée de ces tableaux, et doit les rechercher dans un traité de neurologie ou de neurochirurgie.</p>",
    "Chez un patient comateux, l’engagement et la mort cérébrale imminente se signalent par des <button class=\"w\" data-k=\"g93-sm-engagement\">pupilles fixes et dilatées, un diabète insipide et une bradycardie avec hypertension</button> ; ce tableau impose d’alerter sans délai l’équipe de soins intensifs. Les syndromes topographiques d’engagement (temporal, sous-falcoriel, amygdalien) restent à sourcer avant d’être enseignés.</p>",
    "ERC-ESICM 2025 [S5] « Suggested prognostication strategy »")

# ------------------------------------------------------------------ mineurs
add("M40", "C13", B, "Traitement visant la sécrétion de liquide cérébrospinal ; seul médicament évalué par des essais randomisés ; bénéfice modeste, mal toléré à forte dose",
    "Traitement visant la sécrétion de liquide cérébrospinal ; seul médicament de l’HII évalué par des essais randomisés en 2018, depuis rejoint par un petit essai randomisé de l’exénatide ; bénéfice modeste, mal toléré à forte dose",
    "Mitchell 2023 [S16]")
add("M41", "C15", A, "L’indice pression-volume normal est d’environ 20 à 25 mL.</p>",
    "L’indice pression-volume, volume qui multiplie par dix la pression intracrânienne, est normalement d’environ 20 à 25 mL. La pression d’ouverture lombaire s’exprime en centimètres d’eau et la pression intracrânienne en millimètres de mercure : la <button class=\"w\" data-k=\"g93-unites\">conversion entre ces deux unités (calcul)</button> évite de comparer des chiffres incompatibles.</p>",
    "Jha 2019 [S7] (définition du PVI) ; fenêtre g93-unites (R19–R22)")
add("M42", "C16", P1, "HII diagnostiquée avec pression du liquide supérieure à 250 mm (280 mm chez l’enfant obèse)",
    "HII diagnostiquée avec pression du liquide cérébrospinal supérieure à 250 mm de liquide, soit 25 cm (280 mm, soit 28 cm, chez l’enfant obèse)",
    "unité ambiguë (R17, R18)")
add("M43", "C17", B, "Le plan associe une intervention multicomposante de perte de poids (indice de masse corporelle inférieur à 35 : grade B) ou la chirurgie bariatrique (35 ou plus : grade A), l’acétazolamide selon la tolérance,",
    "Son indice de masse corporelle de 38 kg/m² dépasse le seuil de 35 : la chirurgie bariatrique est à considérer (grade A), après information sur ses bénéfices et ses risques ; l’intervention multicomposante (grade B) reste réservée aux indices inférieurs à 35. Le plan associe l’acétazolamide selon la tolérance,",
    "application du seuil au cas (R13) [S3]")
add("M44", "C18", A, "Pour cette raison, les recommandations du traumatisme crânio-cérébral fixent un seuil de traitement de la pression intracrânienne à 20 à 22 mmHg.",
    "Pour cette raison, un seuil de traitement de la pression intracrânienne de 20 à 22 mmHg est admis dans le traumatisme crânio-cérébral, selon la revue de 2019 qui cite des lignes directrices américaines ; aucune recommandation suisse ou européenne n’a été lue sur ce point.",
    "attribution exacte [S7]")
add("M45", "C19", G, "a('FOUR', [('F','Full'),('O','Outline'),('U','of UnResponsiveness'),('R','score')],",
    "a('FOUR', [('F','Full'),('O','Outline'),('U','Un-'),('R','Responsiveness')],",
    "lettrage : FOUR = Full Outline of UnResponsiveness ; R ne signifie pas « score »")
add("M46", "C23", B, "L’aspirine est restreinte dès 12 ans en cas d’infection virale.",
    "L’aspirine en comprimés à croquer et en granulé n’est pas indiquée avant 12 ans ; dès 12 ans, en cas de fièvre ou d’infection virale, elle n’est employée que sur prescription et en deuxième intention.",
    "FI Aspirine® [S13]")
add("M47", "C13", P2, "<div class=\"lab\">Preuves</div><p>Seul médicament évalué dans des essais randomisés ; la revue Cochrane 2015 conclut à un bénéfice modeste avec des preuves insuffisantes.",
    "<div class=\"lab\">Preuves</div><p>Seul médicament évalué dans des essais randomisés jusqu’en 2018 ; la revue Cochrane 2015 conclut à un bénéfice modeste avec des preuves insuffisantes. Un essai randomisé de 16 femmes a depuis montré que l’exénatide, agoniste du récepteur du GLP-1, abaisse la pression intracrânienne de 5,7 cm d’eau à 2,5 heures ; il ne constitue pas un traitement établi.",
    "Mitchell 2023 [S16]")


def main():
    erreurs = []
    for x in R:
        n = (ROOT / x["fichier"]).read_text(encoding="utf-8").count(x["ancien"])
        x["occurrences"] = n
        if n != 1:
            erreurs.append((x["id"], n))
    (HERE / "remplacements.json").write_text(json.dumps(R, ensure_ascii=False, indent=1), encoding="utf-8")
    print(len(R), "remplacements ; erreurs d'unicité :", erreurs)


if __name__ == "__main__":
    main()
