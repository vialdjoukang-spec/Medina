#!/usr/bin/env python3
"""Propositions de remplacement locales de l'audit ALPHA1-CLAUDE-G99-MED (ancien → nouveau).

Chaque entrée : id, constat, fichier, ancien (extrait exact, unique dans le fichier), nouveau (HTML conforme aux
classes existantes). Les marqueurs [Sx] renvoient à sources.json de l'audit et sont retirés à l'intégration.
Exécution : python3 propositions/corrections.py <racine du worktree>
  → vérifie que chaque « ancien » apparaît exactement une fois (propositions/verification_ancres.json),
  → applique les remplacements sur une copie temporaire (contrôle d'application, sans toucher aux sources),
  → écrit la lecture humaine propositions/G99_corrections.html.
"""
import html
import json
import sys
import tempfile
import shutil
from pathlib import Path

A, B, C, D = "chapters/G99/G99_a.html", "chapters/G99/G99_b.html", "chapters/G99/G99_c.html", "chapters/G99/G99_d.html"
P1, P2, GL = "chapters/G99/G99_pop1.html", "chapters/G99/G99_pop2.html", "glossary/g99.py"

P = []


def p(i, constat, fichier, ancien, nouveau):
    P.append({"id": i, "constat": constat, "fichier": fichier, "ancien": ancien, "nouveau": nouveau})


# --- C02 : périmètre CIM-10-GM et sous-codes -------------------------------------------------------------
p("P01", "C02", A,
  "<p>La <button class=\"w\" data-k=\"g99-uremie\">neuropathie urémique</button> est une polyneuropathie axonale de l’insuffisance rénale chronique.",
  "<p>La <button class=\"w\" data-k=\"g99-uremie\">neuropathie urémique</button> est une polyneuropathie axonale de l’insuffisance rénale chronique. La CIM-10-GM la range sous G63.8*, avec les polyneuropathies, et non sous G99 ; G99.8* ne vise que la paralysie urémique (code † N18.-) [S1][S2]. De même, la polyneuropathie de l’amylose relève de G63.3*, et seule la neuropathie autonome amyloïde relève de G99.0* [S1][S2]. Le cours traite la neuropathie urémique parce qu’elle partage le mécanisme et la démarche, mais son code n’est pas G99.")
p("P02", "C02", B,
  "<p><b>Codage.</b> G99 est une catégorie à astérisque : elle décrit une manifestation et ne se code jamais seule. La maladie causale reçoit le code à croix (†), par exemple E10 à E14 avec le quatrième caractère .4 pour la neuropathie autonome diabétique, ou E85.- pour l’amylose (CIM-10-GM 2024, OFS). La classification ne liste aucune exclusion pour G99.</p>",
  "<p><b>Codage.</b> G99 est une catégorie à astérisque : elle décrit une manifestation et ne se code jamais seule. La maladie causale reçoit le code à croix (†). La classification ne liste aucune exclusion pour G99 [S1]. Le tableau donne les sous-codes et les maladies causales que la CIM-10-GM 2024 y rattache.</p>\n"
  "<table class=\"t\"><thead><tr><th>Sous-code</th><th>Intitulé</th><th>Code † de la cause</th></tr></thead><tbody>"
  "<tr><td>G99.00*</td><td>Gastroparésie lors de neuropathie autonome au cours d’une maladie endocrinienne ou métabolique</td><td>E10–E14, quatrième caractère .4 ; E85.-</td></tr>"
  "<tr><td>G99.08*</td><td>Autre neuropathie autonome au cours d’une maladie endocrinienne ou métabolique</td><td>E10–E14, quatrième caractère .4 ; E85.-</td></tr>"
  "<tr><td>G99.1*</td><td>Autre affection du système nerveux autonome au cours d’autres maladies</td><td>Aucun exemple listé</td></tr>"
  "<tr><td>G99.2*</td><td>Myélopathie au cours de maladies classées ailleurs</td><td>M47.0-† (compression des artères spinale antérieure et vertébrale), M50.0†, M51.0†, C00–D48†, M47.-†</td></tr>"
  "<tr><td>G99.8*</td><td>Autre affection précisée</td><td>Paralysie urémique (N18.-†)</td></tr></tbody></table>\n"
  "<p>Le lecteur cherche d’abord la maladie causale, puis la manifestation. L’erreur fréquente est de coder la neuropathie urémique en G99 : elle relève de G63.8*, comme la polyneuropathie amyloïde relève de G63.3* [S2]. Une gastroparésie diabétique se code donc E10.4† ou E11.4† avec G99.00*, et une myélopathie cervicarthrosique M47.1† avec G99.2* [S1].</p>")
# --- C03 : pourcentages d'accord présentés comme fréquences ou validités --------------------------------
p("P03", "C03", A,
  "Le panel y ajoute une fonction motrice gastrique sévèrement perturbée (accord de 85 %). Les symptômes cardinaux sont les nausées et les vomissements (95 %) ; la plénitude postprandiale, la satiété précoce, la douleur épigastrique, les ballonnements et les éructations sont fréquents (95 %).",
  "Une seconde définition, fondée sur une fonction motrice gastrique sévèrement perturbée, est aussi retenue (accord de 85 %). Le panel retient les nausées et les vomissements comme symptômes cardinaux (accord de 95 %) ; il juge fréquents la plénitude postprandiale, la satiété précoce, la douleur épigastrique, les ballonnements et les éructations (accord de 95 %) [S3]. Ces pourcentages mesurent l’accord des experts : le consensus ne chiffre pas la fréquence des symptômes.")
p("P04", "C03", B,
  "est obligatoire (95 %). La scintigraphie (98 %) et le test respiratoire (95 %) sont valides ; une imagerie exclut une occlusion du grêle (88 %).",
  "est obligatoire (accord de 95 %). Le panel juge valides la scintigraphie (accord de 98 %) et le test respiratoire (accord de 95 %) ; une imagerie exclut une occlusion du grêle (accord de 88 %) [S3]. Ces chiffres ne sont ni des sensibilités ni des spécificités.")
p("P05", "C03", B,
  "<p>L’adaptation diététique est retenue (85 %), ainsi que les antagonistes dopaminergiques D2 (86 %) et les agonistes de la sérotonine 5-HT4 (85 %).",
  "<p>Le panel retient l’adaptation diététique (accord de 85 %), l’efficacité des antagonistes dopaminergiques D2 (accord de 86 %) et celle des agonistes de la sérotonine 5-HT4 (accord de 85 %) [S3]. Ces pourcentages mesurent l’accord des experts, non un taux de réponse.")
p("P06", "C03", B, "Le pronostic dépend de la cause (88 %) ;", "Le pronostic dépend de la cause (accord de 88 %) ;")
p("P07", "C03", C,
  "Les deux examens de vidange valides sont la scintigraphie (98 %) et le test respiratoire (95 %).",
  "Le panel juge valides la scintigraphie (accord de 98 %) et le test respiratoire (accord de 95 %) ; ces chiffres ne sont pas des performances diagnostiques [S3].")
p("P08", "C03", P1,
  "<p>La scintigraphie (98 %) et le test respiratoire (95 %) sont valides pour démontrer un retard de vidange.",
  "<p>Le panel juge valides la scintigraphie (accord de 98 %) et le test respiratoire (accord de 95 %) pour démontrer un retard de vidange ; ces pourcentages mesurent l’accord des experts, non la performance du test.")
# --- C14 : sens pronostique de la rétention > 20 % à 4 h ----------------------------------------------
p("P09", "C14", B,
  "Une rétention supérieure à 20 % à quatre heures est citée comme facteur pronostique.",
  "Dans une cohorte suivie 48 semaines, une rétention supérieure à 20 % à quatre heures s’associait à une moindre intensité des symptômes ; c’est un facteur pronostique, non un seuil diagnostique [S3].")
p("P10", "C14", C,
  "Une rétention supérieure à 20 % à quatre heures est citée comme facteur pronostique ;",
  "Une rétention supérieure à 20 % à quatre heures s’associait, dans une cohorte, à une moindre intensité des symptômes à 48 semaines ; c’est un facteur pronostique, non un seuil diagnostique [S3] ;")
p("P11", "C14", P1,
  "<p>Une rétention supérieure à 20 % à quatre heures est citée comme facteur pronostique.</p>",
  "<p>Une rétention supérieure à 20 % à quatre heures s’associait à une moindre intensité des symptômes à 48 semaines ; ce n’est pas un seuil diagnostique.</p>")
# --- C04 et C05 : douleur urémique et traitements suisses de l'ATTRv-PN ---------------------------------
p("P12", "C04", B,
  "les gabapentinoïdes sont proposés en première ligne de la douleur neuropathique métabolique (la source ne donne pas de posologie rénale).",
  "la source cite en première ligne de la douleur neuropathique métabolique les inhibiteurs de la recapture de la noradrénaline, les gabapentinoïdes et les tricycliques [S17]. L’insuffisance rénale change ce choix : l’information suisse interdit la prégabaline si la clairance de la créatinine est inférieure à 30 mL/min et réduit sa dose de moitié entre 30 et 60 mL/min [S29] ; la gabapentine reste possible à dose réduite, 150 à 300 mg par jour sous 15 mL/min et, en hémodialyse, 200 à 300 mg après chaque séance de 4 heures [S30]. La neuropathie urémique ne figure pas parmi leurs indications suisses : leur emploi y est hors indication [S29][S30].")
p("P13", "C05", B,
  "Dans l’amylose à transthyrétine, le tafamidis est autorisé en Suisse pour la <b>cardiomyopathie</b> seulement (information professionnelle consultée) : aucune information suisse sur les traitements de la polyneuropathie n’a été lue (voir lacunes).",
  "Dans l’amylose à transthyrétine, le tafamidis est autorisé en Suisse pour la <b>cardiomyopathie</b> seulement [S25]. Trois traitements sont autorisés en Suisse pour la polyneuropathie héréditaire de stade 1 ou 2 : le patisiran, 300 µg/kg en perfusion toutes les 3 semaines, au maximum 30 mg à partir de 100 kg [S26] ; le vutrisiran, 25 mg sous-cutanés tous les 3 mois avec un apport de vitamine A de 2500 à 3000 UI par jour au plus [S27] ; l’eplontersen, 45 mg sous-cutanés une fois par mois [S28]. Les informations professionnelles demandent de commencer tôt, car la poursuite au stade 3 relève d’une décision individuelle [S26][S27][S28].")
p("P14", "C05", D,
  "Les traitements spécifiques de la polyneuropathie à transthyrétine (patisiran, vutrisiran, inotersen, eplontersen) n’ont pas été documentés par des informations professionnelles suisses.",
  "La polyneuropathie héréditaire à transthyrétine de stade 1 ou 2 dispose de trois traitements autorisés en Suisse : <button class=\"w\" data-k=\"g99-patisiran\">patisiran (Onpattro)</button>, <button class=\"w\" data-k=\"g99-vutrisiran\">vutrisiran (Amvuttra)</button> et <button class=\"w\" data-k=\"g99-eplontersen\">eplontersen (Wainzua)</button> [S26][S27][S28]. Aucune information professionnelle suisse de l’inotersen n’a été trouvée.")
p("P15", "C05", P2,
  "<div class=\"lab\">Limite</div><p>Les traitements spécifiques de la polyneuropathie à transthyrétine (patisiran, vutrisiran, inotersen, eplontersen) n’ont pas été lus.</p>",
  "<div class=\"lab\">Polyneuropathie</div><p>La polyneuropathie héréditaire de stade 1 ou 2 relève en Suisse du patisiran, du vutrisiran ou de l’eplontersen (informations professionnelles d’octobre 2024, d’octobre 2025 et de mai 2025).</p>")
# --- C08 : hyperkaliémie : corrélation, non mécanisme démontré -----------------------------------------
p("P16", "C08", A,
  "L’hyperkaliémie chronique est le mécanisme principal proposé de la neuropathie urémique : la kaliémie est fortement corrélée aux altérations nerveuses, indépendamment de la cause de la maladie rénale.",
  "La kaliémie est fortement corrélée aux altérations fonctionnelles et structurelles des nerfs, que la maladie rénale soit d’origine diabétique ou non [S17]. Un essai randomisé a montré un effet neuroprotecteur de la restriction potassique ; la source demande des essais plus larges avant de conclure à une causalité [S17].")
p("P17", "C08", A,
  "Mécanisme principal proposé : hyperkaliémie chronique",
  "Kaliémie fortement corrélée aux lésions nerveuses")
p("P18", "C08", C,
  "La corrélation forte entre kaliémie et altérations nerveuses fait de l’hyperkaliémie chronique le mécanisme principal proposé ;",
  "La kaliémie est fortement corrélée aux altérations nerveuses, mais cette corrélation ne prouve pas à elle seule la causalité ;")
p("P19", "C08", P1,
  "<p>Hyperkaliémie chronique proposée comme mécanisme principal ; atteinte axonale longueur-dépendante.</p>",
  "<p>Kaliémie fortement corrélée aux altérations nerveuses, causalité à confirmer ; atteinte axonale longueur-dépendante.</p>")
# --- C09 : voie chirurgicale --------------------------------------------------------------------------
p("P20", "C09", B,
  "la décompression est le plus souvent une discectomie antérieure avec cage (Revue médicale suisse, 2015).",
  "pour la hernie discale cervicale, la décompression se fait le plus souvent par discectomie antérieure avec cage (Revue médicale suisse, 2015). La voie dépend de la lésion : dans une série japonaise de MCD légère opérée, la voie postérieure représentait 88,5 % des gestes [S11].")
# --- C10 : tableau de conduite automobile -------------------------------------------------------------
p("P21", "C10", B,
  "<td>Inapte tant que diagnostic et traitement manquent ; sinon au moins 12 mois</td>",
  "<td>Inapte tant que le diagnostic n’est pas établi et le traitement entrepris ; en l’absence de diagnostic, délai d’au moins 12 mois</td>")
p("P22", "C10", B,
  "<tr><td>Vasovagale au volant ou récidivante</td>",
  "<tr><td>Vasovagale, épisode unique hors de la conduite</td><td>Apte</td><td>Apte</td></tr><tr><td>Vasovagale au volant ou récidivante</td>")
# --- C11, C15, E02 : midodrine et fiches suisses ------------------------------------------------------
p("P23", "C11", D,
  "jusqu’à 15 mg par jour dans certains cas (ESC 2018 : 2,5 à 10 mg trois fois par jour)",
  "jusqu’à 15 mg par jour dans certains cas ; la FI ne recommande pas de dépasser 30 mg par jour en trois prises (ESC 2018 : 2,5 à 10 mg trois fois par jour, soit 30 mg au plus)")
p("P24", "C11", P2,
  "jusqu’à 15 mg par jour dans certains cas. Dernière dose",
  "jusqu’à 15 mg par jour dans certains cas ; au-delà de 30 mg par jour en trois prises, une augmentation ne peut être recommandée. Dernière dose")
p("P25", "C15", D,
  "la date de mise à jour de chaque fiche n’a pas pu être extraite. Les mécanismes d’action détaillés ne figurent pas dans les extraits lus et ne sont donc pas développés.",
  "les fiches datent de mars 2021 (Gutron), mars 2026 (Florinef), juin 2026 (Motilium), janvier 2020 (Paspertin) et avril 2026 (Vyndaqel) [S21][S22][S23][S24][S25]. La midodrine est un promédicament transformé en desglymidodrine, agoniste α direct des récepteurs périphériques ; elle n’accélère pas le cœur et peut provoquer une bradycardie réflexe [S21]. La dompéridone est un antagoniste D2 périphérique qui franchit peu la barrière hémato-encéphalique, d’où moins d’effets extrapyramidaux, mais elle allonge le QTc [S3].")
# --- C12 : fludrocortisone ---------------------------------------------------------------------------
p("P26", "C12", D,
  "0,1 mg trois fois par semaine à 0,2 mg par jour (indications suisses : insuffisance surrénalienne, perte de sel)",
  "0,1 mg trois fois par semaine à 0,2 mg par jour, norme 0,1 mg par jour ; au plus 0,05 mg par jour en cas d’hypertension induite (indications suisses : insuffisance surrénalienne, perte de sel). La borne de 0,3 mg par jour de l’ESC dépasse cette dose usuelle maximale")
p("P27", "C12", D,
  "<b>Fludrocortisone</b> : hypertension artérielle sévère, ulcères gastro-intestinaux aigus, mycoses systémiques.",
  "<b>Fludrocortisone</b> : hypertension artérielle sévère, ulcères gastro-intestinaux aigus, mycoses systémiques, herpès simplex oculaire, zona ou varicelle, artériosclérose cérébrale avancée.")
# --- C13 : stadification de Toronto -----------------------------------------------------------------
p("P28", "C13", B,
  "un test réflexe anormal = possible ; ≥ 2 = confirmée ; avec hypotension orthostatique = sévère.",
  "un test cardiovagal (de fréquence) anormal = possible ; ≥ 2 tests cardiovagaux anormaux = confirmée ; tests de fréquence anormaux et hypotension orthostatique = sévère ; diagnostic posé après exclusion des autres causes [S6].")
p("P29", "C13", P1, "<tr><td>2 tests anormaux ou plus</td>", "<tr><td>2 tests de fréquence (cardiovagaux) anormaux ou plus</td>")
p("P30", "C13", C, "<tr><td>Deux tests ou plus anormaux</td>", "<tr><td>Deux tests de fréquence ou plus anormaux</td>")
# --- C16, E02 : dompéridone, interactions ------------------------------------------------------------
p("P31", "C16", D,
  "inhibiteurs puissants du CYP3A4 allongeant le QT, insuffisance hépatique modérée ou sévère, prolactinome.",
  "inhibiteurs puissants du CYP3A4 allongeant le QT, dont l’érythromycine et la clarithromycine, hémorragie, occlusion mécanique ou perforation digestive, insuffisance hépatique modérée ou sévère, prolactinome, phéochromocytome.")
p("P32", "E02", D,
  "Sous dompéridone, le risque cardiaque (QTc, électrolytes) justifie la courte durée.</p>",
  "Sous dompéridone, le risque cardiaque (QTc, électrolytes) justifie la courte durée. La midodrine inhibe le CYP2D6 et peut augmenter l’exposition au métoclopramide : l’association, fréquente chez la personne qui souffre à la fois d’hypotension orthostatique et de gastroparésie, demande une surveillance [S21].</p>")
# --- C17 : cohérence du repère de 10 battements ------------------------------------------------------
p("P33", "C17", C,
  "la pression chute et la fréquence cardiaque s’élève peu (au plus 10 battements par minute).",
  "la pression chute et la fréquence cardiaque s’élève peu (habituellement de 10 battements par minute au plus).")
# --- C18 : plan du cours ------------------------------------------------------------------------------
p("P34", "C18", A,
  "<li><a href=\"#g99-12\">Critères formels et paramètres clés</a></li></ol>",
  "<li><a href=\"#g99-12\">Spécificités suisses et points d’examen fédéral</a></li><li><a href=\"#g99-13\">Critères formels et paramètres clés</a></li></ol>")
# --- C19 : glossaire ---------------------------------------------------------------------------------
p("P35", "C19", GL,
  "[('PND','score de locomotion de I à IV correspondant aux stades 1 à 3 ; développement non fourni par la source lue')]",
  "[('P','Poly'),('N','Neuropathy'),('D','Disability')]")
p("P36", "C19", GL,
  "Le développement n’est pas donné dans la source lue ; il est le développement usuel.",
  "Développement donné par la liste des abréviations du consensus européen 2021.")
# --- C20 : noms accessibles des figures ---------------------------------------------------------------
p("P37", "C20", A, "aria-label=\"Schéma\"", "aria-label=\"Chaîne causale de la neuropathie autonome cardiovasculaire : hyperglycémie et glycation, lésion du nerf vague, déficit parasympathique, fréquence fixe et hypotension orthostatique\"")
p("P38", "C20", B, "aria-label=\"Schéma\"", "aria-label=\"Démarche devant une suspicion de myélopathie cervicale : signes du premier motoneurone, IRM cervicale, corrélation clinique, avis spécialisé\"")
p("P39", "C20", C, "aria-label=\"Schéma\"", "aria-label=\"Hypotension orthostatique neurogène : verticalisation, vasoconstriction sympathique défaillante, chute de pression sans accélération, vertiges et syncope\"")
# --- C21 : cas récapitulatif --------------------------------------------------------------------------
p("P40", "C21", B,
  "La baisse systolique de 25 mmHg dépasse le seuil de 20 mmHg : l’hypotension orthostatique est établie.",
  "La baisse systolique de 25 mmHg dépasse le seuil de 20 mmHg, et la baisse diastolique de 10 mmHg atteint aussi le sien : l’hypotension orthostatique est établie. La fréquence debout manque pour juger de l’origine neurogène.")
# --- E01, E03, E04 : enrichissements ------------------------------------------------------------------
p("P41", "E01", A,
  "Cette fréquence a une conséquence importante : une image de compression ne prouve pas à elle seule une myélopathie, la clinique décide.",
  "Cette fréquence a une conséquence importante : une image de compression ne prouve pas à elle seule une myélopathie, la clinique décide. Dans la seule étude prospective, 8 % des personnes porteuses d’une compression asymptomatique ont développé une myélopathie à un an et 22 % sur un suivi médian de 44 mois [S8] : c’est pourquoi l’information et le suivi clinique sont recommandés [S12].")
p("P42", "E03", A,
  "L’examen est <b>peu sensible mais spécifique</b> : un examen normal n’exclut pas la MCD, alors qu’un signe positif est très évocateur (BMJ, 2018).",
  "L’examen est <b>peu sensible mais spécifique</b> : un examen normal n’exclut pas la MCD, alors qu’un signe positif est très évocateur (BMJ, 2018). L’association de signes vaut mieux qu’un signe isolé : trois des cinq éléments du groupement de Cook (trouble de la marche, Hoffmann, réflexe supinateur inversé, Babinski, âge supérieur à 45 ans) donnent une spécificité de 99 % [S31]. La technique et la valeur de chaque signe sont développées dans l’onglet Sciences, discipline « Sémiologie ».")
p("P43", "E04", A,
  "Environ 20 % des personnes diabétiques sont concernées (Diabetologia, 2024),",
  "Environ 20 % des personnes diabétiques sont concernées, jusqu’à 65 % avec l’âge et la durée du diabète selon le consensus de Toronto, qui pose le diagnostic après exclusion des autres causes [S6] (Diabetologia, 2024),")


def main():
    racine = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    ici = Path(__file__).resolve().parent
    contrôle = []
    textes = {}
    for e in P:
        t = textes.setdefault(e["fichier"], (racine / e["fichier"]).read_text(encoding="utf-8"))
        contrôle.append({"id": e["id"], "constat": e["constat"], "fichier": e["fichier"], "occurrences": t.count(e["ancien"])})
    # application sur copie temporaire
    tmp = Path(tempfile.mkdtemp())
    appli = {}
    for f, t in textes.items():
        for e in P:
            if e["fichier"] == f:
                t = t.replace(e["ancien"], e["nouveau"], 1)
        (tmp / Path(f).name).write_text(t, encoding="utf-8")
        appli[f] = all(e["nouveau"] in t for e in P if e["fichier"] == f)
    shutil.rmtree(tmp)
    ok = all(c["occurrences"] == 1 for c in contrôle)
    (ici / "verification_ancres.json").write_text(json.dumps({"toutes_uniques": ok, "total": len(contrôle), "application_sur_copie": appli,
                                                              "controle": contrôle}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    lignes = ["<!-- Lecture humaine générée par propositions/corrections.py ; chaque bloc : fichier, ancien, nouveau. -->"]
    for e in P:
        lignes.append("<section class=\"ilot\" id=\"audit-%s\"><h3>%s — constat %s — %s</h3>" % (e["id"].lower(), e["id"], e["constat"], e["fichier"]))
        lignes.append("<p><b>Ancien (extrait exact, unique)</b></p><pre>%s</pre>" % html.escape(e["ancien"]))
        lignes.append("<p><b>Nouveau</b></p>%s</section>" % e["nouveau"])
    (ici / "G99_corrections.html").write_text("\n".join(lignes) + "\n", encoding="utf-8")
    print("ancres uniques :", ok, "/", len(contrôle), "; application :", appli)
    for c in contrôle:
        if c["occurrences"] != 1:
            print("ÉCHEC", c)


if __name__ == "__main__":
    main()
