#!/usr/bin/env python3
"""Recalcul et contrôle scripté de toutes les valeurs de la leçon G80 (audit ALPHA1-CLAUDE-G80-MED).

Usage : python3 calculs/verifier.py
Entrée : calculs/inventaire.json (produit par calculs/extraire.py).
Sortie : calculs/resultats.json.

Trois natures d'occurrence :
- « calcul » : grandeur dérivée (rapport, NNT, dose calculée, plafond, conversion, somme) ;
  elle est recalculée par une formule écrite ci-dessous ;
- « valeur_sourcee » : chiffre recopié d'une source (fréquence, seuil, dose, effectif) ;
  il est comparé, par script, à la valeur transcrite depuis la source lue (sources.json) ;
- « non_calculable » : date, numéro d'îlot, de liste, de cas ou de figure, code CIM, référence
  bibliographique, donnée d'une vignette fictive sans grandeur à recalculer.
Tolérance d'arrondi : 0,5 unité du dernier chiffre affiché (ARRONDI au-delà de l'égalité stricte).
"""
import json
import re
from pathlib import Path

ICI = Path(__file__).parent


def num(s: str) -> float:
    return float(s.replace(" ", "").replace(" ", "").replace(" ", "").replace(",", "."))


def arrondi_ok(affiche: float, exact: float, decimales: int) -> bool:
    return abs(affiche - exact) <= 0.5 * 10 ** (-decimales) + 1e-9


# ---------------------------------------------------------------------------
# 1. Calculs dérivés : formule, données de la source, valeur affichée par la leçon
# ---------------------------------------------------------------------------
CALCULS = []


def calc(fid, motif, valeurs, attendu, trouve, formule, source, verdict=None, decimales=0, note=""):
    if verdict is None:
        if isinstance(attendu, (int, float)) and isinstance(trouve, (int, float)):
            if abs(attendu - trouve) < 1e-9:
                verdict = "CORRECT"
            elif arrondi_ok(trouve, attendu, decimales):
                verdict = "ARRONDI"
            else:
                verdict = "FAUX"
        else:
            verdict = "CORRECT" if attendu == trouve else "FAUX"
    CALCULS.append(dict(id=fid, motif=motif, valeurs=valeurs, attendu=attendu, trouve=trouve,
                        ecart=(round(trouve - attendu, 4) if isinstance(attendu, (int, float)) and isinstance(trouve, (int, float)) else None),
                        verdict=verdict, formule=formule, source=source, note=note, nature="calcul"))


# Rapport de risque avant 28 SA / à terme (g80-3) : 146 / 1,13
calc("K01", r"130 fois|divisé par", ["130", "146", "1,13"], round(146 / 1.13, 1), 130,
     "146 / 1,13 = 129,2 ; la leçon écrit « près de 130 »", "S4, Frequency of CP", decimales=-1,
     note="129,2 arrondi à la dizaine : « près de 130 » est exact.")
# « environ un enfant sur sept » avant 28 SA
calc("K02", r"un enfant sur sept", ["28"], round(1000 / 146, 2), 7, "1000 / 146 = 6,85 → 1 sur 7", "S4", decimales=0)
# « plus de 14 % avant 28 SA »
calc("K03", r"plus de 14 %", ["14"], 146 / 10, 14, "146 pour 1000 = 14,6 % > 14 %", "S4", verdict="CORRECT",
     note="14,6 % : « plus de 14 % » est exact.")
# Cohorte suisse < 30 SA : 14 / 235
calc("K04", r"14 sur 235|6 % ont une PC|6 % de PC", ["6", "14", "235"], round(14 / 235 * 100, 2), 6,
     "14 / 235 × 100 = 5,96 %", "S11, Results", decimales=0)
# Somme des niveaux GMFCS du registre suisse = 100 %
calc("K05", r"I–II chez 59|III chez 12|IV–V chez 29|GMFCS I–II 59|III 12 %|IV–V 29", ["59", "12", "29"], 100, 59 + 12 + 29,
     "59 + 12 + 29 = 100 %", "S3, Results")
# Hanche : 38 / 212
calc("K06", r"18 % de|déplacement de hanche.*18 %|chez 18 %|18 % avaient|18 % de déplacements|212", ["18", "212"], round(38 / 212 * 100, 2), 18,
     "38 / 212 × 100 = 17,9 %", "S9, Results", decimales=0)
# Baclofène intrathécal en Europe : 114 / 3398
calc("K07", r"3,4 %", ["3,4"], round(114 / 3398 * 100, 3), 3.4, "114 / 3398 × 100 = 3,35 %", "S19, Results", decimales=1,
     note="Population : six pays à données populationnelles (2011), non « l'Europe » entière (constat C15).")
# Proportion spastique unilatérale chez les < 1500 g : 336 / 1426
calc("K08", r"dont 24 % unilatérale", ["24"], round(336 / 1426 * 100, 2), 24, "336 / 1426 × 100 = 23,6 %", "S10, Findings", decimales=0)
# 94 % de spastiques chez les < 1500 g : la source donne 1426 (94 %) sur 1575 enfants
calc("K09", r"94 %", ["94"], 94, 94, "valeur de la source : 1426 (94 %) ; 1426 / 1575 = 90,5 %",
     "S10, Findings", verdict="CORRECT",
     note="La leçon reproduit fidèlement 94 %. Le résumé de la source donne 1426/1575 = 90,5 % : son dénominateur exclut probablement les sous-types inconnus (non vérifiable sur le résumé).")
# Sulfate de magnésium : NNT implicite et risque de base
cer = 1 / (60 * (1 - 0.71))
calc("K10", r"60 femmes|60 femmes à traiter", ["60"], 60, 60,
     "NNTB = 1 / (RCT × (1 − RR)) ; RR 0,71 et NNTB 60 impliquent un risque de base de 1/(60 × 0,29) = 5,75 %",
     "S15, Main results (NNTB 60, IC 95 % 41–158)", verdict="CORRECT",
     note=f"Cohérent : risque de PC sous placebo implicite {cer*100:.2f} %. L'unité de compte de la revue est l'enfant (6107 enfants, 5917 femmes) : « 60 femmes » est une approximation (C04).")
# Dysport, cas 1 : enfant de 20 kg, deux jambes
plafond_total = min(30 * 20, 1000)
plafond_jambe = min(15 * 20, 500)
calc("K11", r"600 U|30 U/kg × 20 kg", ["600", "20", "30"], plafond_total, 600,
     "min(30 U/kg × 20 kg ; 1000 U) = 600 U par séance", "S13, Posologie d) membre inférieur")
calc("K12", r"500 U par jambe", ["500"], plafond_jambe, 500,
     "par jambe : min(15 U/kg × 20 kg ; 500 U) = 300 U", "S13, Posologie d) membre inférieur (« jusqu'à 15 unités/kg/jambe » ; « La dose maximale par jambe ne doit pas dépasser 500 unités »)",
     verdict="CORRECT",
     note="Le plafond de 500 U par jambe est exact comme règle, mais pour 20 kg le plafond effectif par jambe est 300 U (15 U/kg) ; la correction du cas ne le dit pas (C11, MINEUR).")
# Baclofène oral : seuil de poids où le plafond de 40 mg/j limite l'entretien de 2 mg/kg/j
calc("K13", r"0,75–2 mg/kg|0,75 à 2 mg/kg|40 mg/jour avant 8 ans", ["40", "0,75–2", "2"], 40 / 2, 20,
     "40 mg/j ÷ 2 mg/kg/j = 20 kg : au-delà de 20 kg avant 8 ans, le plafond de 40 mg/j l'emporte sur 2 mg/kg/j",
     "S14, Posologie Enfants et adolescents", verdict="CORRECT",
     note="Calcul de cohérence ; la leçon ne signale pas cette interaction des deux limites (proposition G80_d_1).")
# Baclofène oral : dose initiale par prise pour un enfant de 12 kg et forme disponible
dose_prise = 0.3 * 12 / 4
calc("K14", r"0,3 mg/kg/jour en 4 prises|départ 0,3 mg/kg/jour", ["0,3", "4"], round(dose_prise, 2), 0.9,
     "0,3 mg/kg/j × 12 kg ÷ 4 prises = 0,9 mg par prise ; plus petite dose orale divisible en doses égales : 5 mg (½ comprimé de 10 mg)",
     "S14, Posologie (« Les comprimés de 10 mg peuvent être divisés en deux doses similaires » ; 25 mg non divisible en doses égales)",
     verdict="CORRECT",
     note="La posologie recopiée est exacte, mais elle n'est pas réalisable avec la forme orale suisse lue chez le petit enfant (C12).")
# Baclofène intrathécal : dose quotidienne initiale après implantation = 2 × bolus efficace
calc("K15", r"Test en bolus|bolus de 100 µg|25 µg", ["25", "100"], 2 * 25, 50,
     "dose initiale/24 h = 2 × dose test efficace (si effet ≤ 12 h) ; ex. bolus efficace 25 µg → 50 µg/24 h",
     "S18, Posologie (phase d'implantation)", verdict="CORRECT",
     note="Règle de la FI absente de la leçon (proposition G80_d_1).")
# Titration IT d'origine cérébrale : paliers 5–15 % (titration) et 5–20 % (entretien)
calc("K16", r"5–20 %", ["5–20"], "titration 5–15 % ; entretien 5–20 %", "5–20 % présenté sans distinction",
     "comparaison texte leçon / FI", "S18, Posologie (« Les augmentations ne dépasseront pas 5 à 15% » ; « augmentée progressivement de 5 à 20% au plus »)",
     verdict="FAUX", note="Le palier de 20 % n'est admis qu'en entretien ; en titration post-implantation la FI limite à 15 % (C09).")
# DAYC : 83 % est un indice C (aire sous la courbe), pas une sensibilité
calc("K17", r"DAYC|indice C", ["83"], "indice C 0,83 (discrimination globale)", "sensibilité 83 %",
     "nature de la mesure", "S5, Abstract et Findings (« Developmental Assessment of Young Children (83% C index) »)",
     verdict="FAUX", note="Un indice C n'est pas une sensibilité : il ne dit pas combien de malades sont détectés (C03).")
# Chirurgie de hanche : gain de migration
calc("K18", r"66,8 %|8,1 %", ["66,8", "8,1"], round(66.8 - 8.1, 1), 58.7, "66,8 − 8,1 = 58,7 points de migration", "S20, Results", verdict="CORRECT",
     note="Valeurs exactes ; série de 54 patients et 64 hanches.")
# Proportion ataxique : sommes des groupes d'imagerie (29 + 28,5 + 23,5 + 19 = 100)
calc("K19", r"29 %|28,5", ["29", "28,5"], 100.0, 29 + 28.5 + 23.5 + 19, "29 + 28,5 + 23,5 (divers) + 19 (lésions) = 100 %", "S7, Results")
# Lecture des sensibilités sur 100 nourrissons atteints (g80-e-2)
calc("K20", r"sur 100 nourrissons|90 un HINE|86 à 89 une IRM", ["100", "98", "90", "86", "89"], [100 * 0.98, 100 * 0.90, 100 * 0.86, 100 * 0.89], [98, 90, 86, 89],
     "vrais positifs attendus = 100 × sensibilité", "S5, Abstract", verdict="CORRECT",
     note="Lecture exacte ; la leçon rappelle à juste titre que la spécificité n'est pas donnée par S5.")
# Rapports de vraisemblance (source européenne ajoutée par l'audit, Morgan 2019) — proposition
for nom, se, sp in (("fidgety absents à 3 mois", .95, .97), ("HINE à 3 mois", .88, .62), ("imagerie", .79, .99)):
    CALCULS.append(dict(id="P-" + nom, motif=None, valeurs=[], attendu={"RV+": round(se / (1 - sp), 2), "RV−": round((1 - se) / sp, 3)},
                        trouve=None, ecart=None, verdict="NON_APPLICABLE", nature="calcul_proposition",
                        formule="RV+ = Se / (1 − Sp) ; RV− = (1 − Se) / Sp", source="S26, Results",
                        note="Valeurs recalculées pour la proposition de sémiologie ; absentes de la leçon."))

# ---------------------------------------------------------------------------
# 2. Valeurs recopiées des sources : (motif de contexte, valeurs, source, verdict, note)
# ---------------------------------------------------------------------------
VS = [
    # motifs spécifiques d'abord (évitent une attribution de source erronée)
    (r"migration|Reimers|déplacement au-delà|= déplacement", ["40"], "S9 : Migration Percentage (MP) > 40 %", "CORRECT", ""),
    (r"3818", ["3818", "20"], "S8 : 3,818 children, 20 European registers", "CORRECT", ""),
    (r"parole compréhensible|90 % de parole|90 % des PC spastiques", ["90"], "S4 : 90 % of children with unilateral spastic CP had normal or understandable speech", "CORRECT", ""),
    (r"avant 12 ans|276 µg|à 12 mois ; avant", ["12", "24–1199", "276", "24"], "S18 : spasticité d'origine cérébrale, enfants < 12 ans", "CORRECT", ""),
    (r"hanche déplacée 79|79 % en tétraplégie|79 % en", ["79"], "S9 : 79 % in spastic tetraplegia", "CORRECT", ""),
    # Épidémiologie
    (r"2,08", ["2,08"], "S4 : 2.08 per 1000 live births (1980–1990)", "CORRECT", ""),
    (r"70 fois|1500 g qu|2500 g", ["70", "1500", "2500"], "S4 : more than 70 times higher < 1500 g vs ≥ 2500 g", "CORRECT", ""),
    (r"Avant 28 SA|146|28 à 31|32 à 36|1,13|^62$|^7$", ["146", "62", "7", "1,13", "28", "31", "32", "36"], "S4 : 146 ; 62 ; 7 ; 1.13 per 1000", "CORRECT",
     "Méta-analyse belge citée par S4 ; l'unité « pour 1000 naissances vivantes » est celle de S4."),
    (r"1,90|1,77|70,9|35,9|1000 et 1499", ["1,90", "1,77", "70,9", "35,9", "1000", "1499"], "S4 (Sellier 2016) : 1.90→1.77 ; 70.9→35.9 (1980–2003)", "CORRECT", ""),
    (r"60,6|39,5", ["60,6", "39,5", "1500"], "S10 : 60.6 → 39.5 per 1000 (1980–1996)", "CORRECT", ""),
    (r"546|55 %|56 %|76 %|73 %|18 mois|médiane|170", ["546", "55", "56", "76", "73", "18", "170", "2", "59", "12", "29"], "S3 : Results", "CORRECT", ""),
    (r"environ 2 enfants pour 1000|environ 2 pour 1000|Environ 2 pour 1000", ["2", "1000"], "S4 : 1.5–3.0 ; 2.08 per 1000 ; S5 : 1 in 500", "CORRECT", ""),
    (r"75 %|10 à 18", ["75", "10", "18"], "S4 : nearly 75 % ; 10 % to 18 %", "CORRECT", ""),
    (r"syndrome génétique|ataxique|ataxie|3,8|679|79 %|marchent|déficience intellectuelle sévère|28,5|IRM normale 29|normale dans 29|20 registres européens", ["9", "679", "3,8", "79", "70", "40", "29", "28,5", "20"], "S7 : Results", "CORRECT", ""),
    (r"80 %|3818|20 registres", ["80", "3818", "20"], "S4 : > 80 % ; S8 : 3818 children, 20 registers", "CORRECT", ""),
    # Comorbidités
    (r"15 à 60|50–94|33–50|16–27", ["15", "60", "50–94", "33–50", "16–27"], "S4 : 15 to 55–60 % ; 50–94 ; 33–50 ; 16–27", "CORRECT", ""),
    (r"1,1 à 3,4|3,4 pour 1000|3,4 enfants", ["1,1", "3,4", "1000"], "S4 : 1.1–3.4/1000 ill children annually ; S25 : < 16 ans 1,11/1000 personnes-années", "CORRECT",
     "Population : enfants épileptiques en général, non spécifiquement PC (C16)."),
    (r"40 à 65", ["40", "65"], "S4 : 40 % and 65 %", "CORRECT", ""),
    (r"2 enfants sur 3$|Environ 2 enfants sur 3|2 enfants sur 3 ;", ["2", "3"], "S4 : 2 out of 3 (dysphagie)", "CORRECT", ""),
    (r"Plus de 50|plus de 50 %|97 %|90 % de parole|90 % des PC spastiques", ["50", "97", "90"], "S4 : over 50 % ; 97 % ; 90 %", "CORRECT", ""),
    (r"212|0 % en GMFCS I|64 %|79 % en tétraplégie|0 % en ataxie|0 % en I", ["18", "212", "0", "64", "79"], "S9 : Results", "CORRECT", ""),
    (r"40 %|supérieure à 40", ["40"], "S9 : MP > 40 %", "CORRECT", ""),
    (r"2–3 ans", ["2–3"], "S9 : Conclusion « often occurs already at 2–3 years »", "CORRECT", ""),
    # Diagnostic précoce
    (r"98 %|Prechtl|mouvements généraux", ["98", "5"], "S5 : GMs 98 % sensitivity before 5 months", "CORRECT", ""),
    (r"HINE|90 %", ["90", "5"], "S5 : HINE 90 % sensitivity", "CORRECT", ""),
    (r"86–89|IRM", ["86–89", "5"], "S5 : MRI 86–89 % sensitivity", "CORRECT", ""),
    (r"12–24 mois|avant 6 mois|6 mois d’âge corrigé", ["12–24", "6"], "S5 : 12–24 months ; before 6 months' corrected age", "CORRECT", ""),
    (r"5 ans, et au moins 4 ans|4 à 5 ans|4–5 ans|après 4 à 5|vers 4–5", ["5", "4", "4–5"], "S4 : register age 5 years ; at least 4 years", "CORRECT", ""),
    (r"avant l’âge de 2 ans|évoluent avant", ["2"], "S5 : emerge and evolve before age 2 years", "CORRECT", ""),
    (r"fiable dès 2 ans|à partir de 2 ans|plus de 2 ans|fiable qu’à partir de 2|Valide et fiable dès 2", ["2"], "S9 : GMFCS valid and reliable from 2 years", "CORRECT", ""),
    (r"moins de 2 ans, 2–4|2–4, 4–6|6–12|12–18", ["2", "2–4", "4–6", "6–12", "12–18"], "S4 : age bands", "CORRECT", ""),
    (r"2 enfants sur 3 marcheront|3 sur 4|1 sur 2|2 sur 3 marchent", ["2", "3", "4", "1"], "S5 : 2 in 3 walk, 3 in 4 talk, 1 in 2 normal intelligence", "CORRECT", ""),
    # Prévention
    (r"0,71|0,57–0,89|6 essais|6107|0,87|3,21|95 %", ["0,71", "95", "0,57–0,89", "6", "6107", "0,87", "3,21"], "S15 : Main results", "CORRECT", ""),
    (r"34 SA", ["34"], "S15 : < 34 weeks (critère d'inclusion des essais) ; S27 (SSGO avis n° 66, 2019) : 24+0 à 32+0 SA en Suisse", "FAUX",
     "Seuil d'indication suisse : 32+0 SA, non 34 SA (C04)."),
    (r"à 2 ans d’âge corrigé|PC à 2 ans|réduit la PC à 2", ["2"], "S15 : up to two years' corrected age", "CORRECT", ""),
    (r"avant 30 SA|moins de 30 SA|nés avant 30|PC à 5 ans|à 5 ans", ["30", "5", "6"], "S11 : < 30 weeks, 5 years", "CORRECT", ""),
    # Traitements
    (r"3 à 8 mois|3 à 8", ["3", "8"], "S4 : improvement lasts approximately 3–8 months", "CORRECT", ""),
    (r"50 à 75", ["50", "75"], "S4 : 50–75 % of dorsal fibres L1–S1", "CORRECT", ""),
    (r"54 patients|66,8|8,1|54 patients GMFCS", ["54", "66,8", "8,1"], "S20 : Results", "CORRECT", ""),
    (r"36 institutions|9 pays|10 000", ["36", "9", "10"], "S17 : 36 institutions in 9 countries, > 10,000 patients", "CORRECT", ""),
    (r"70 médecins|69 %|64 %|63 %", ["70", "69", "64", "63"], "S21 : 70 physicians ; 69 % ; 64 % ; 63 %", "CORRECT",
     "Médecins d'Europe, d'Amérique du Nord et d'Australie, non « du registre suisse » (C14)."),
    (r"3,4 %|3,4 % des enfants", ["3,4"], "S19 : 114 (3.4 %) of 3398", "CORRECT", ""),
    # FI suisses
    (r"16 U/kg|640 U|21 U/kg|840 U", ["16", "640", "21", "840"], "S13 : spasticité focale membres supérieurs enfant", "CORRECT", ""),
    (r"15 U/kg|30 U/kg|500 U|1000 U|0,5 mL", ["15", "30", "500", "1000", "0,5"], "S13 : membre inférieur enfant", "CORRECT", ""),
    (r"dès 2 ans|dès l’âge de 2 ans|2 ans \(toxine\)|toxine botulique qu’à partir de 2|à partir de 2 ans", ["2"], "S13 : patients âgés de 2 ans et plus", "CORRECT", ""),
    (r"1 à 2 semaines|1–2 semaines", ["1", "2", "1–2"], "S14 : intervalles d'environ 1 à 2 semaines", "CORRECT", ""),
    (r"2 semaines", ["2"], "S13 : effet maximal « au cours des 2 semaines » rubrique blépharospasme (et hyperhidrose), non spasticité de l'enfant", "FAUX",
     "Valeur importée d'une autre indication de la même FI (C10)."),
    (r"0,3 mg/kg|4 prises|1–2 semaines|1 à 2 semaines|0,75|40 mg/jour|60 mg/jour|8 ans", ["0,3", "4", "1–2", "1", "2", "0,75–2", "0,75", "40", "60", "8"], "S14 : Posologie Enfants et adolescents", "CORRECT", ""),
    (r"12 mois", ["12"], "S14 : « L'âge minimal est de 12 mois » (posologie) ; indications : SEP et spasticité médullaire seulement", "CORRECT",
     "Âge exact ; le terme « autorisé » est inexact pour la spasticité d'origine cérébrale (C05)."),
    (r"3 semaines", ["3"], "S14 : par paliers sur une durée d'environ 3 semaines", "CORRECT", ""),
    (r"25 µg|100 µg|22–1400|22 à 1400|276|24–1199|24 à 1199|5–20|4 ans|1199|1400", ["25", "100", "22–1400", "22", "1400", "276", "24–1199", "24", "1199", "5–20", "4", "5", "20", "12"],
     "S18 : Posologie et Enfants et adolescents", "CORRECT", "Le palier 5–20 % est exact pour l'entretien seulement (K16, C09)."),
    (r"avant 28 SA", ["28"], "S4 : before the 28th week", "CORRECT", ""),
    (r"1500 g, 94|moins de 1500 g", ["1500", "94"], "S10 : VLBW < 1500 g ; 94 % spastic", "CORRECT", ""),
    (r"59 %|29 %", ["59", "29"], "S3 : GMFCS I–II 59 % ; IV–V 29 %", "CORRECT", ""),
    (r"moins de 2 ans", ["2"], "S5 : signs emerge and evolve before age 2 years ; S9 : GMFCS reliable from 2 years", "CORRECT", ""),
    (r"86 à 89", ["86", "89"], "S5 : MRI 86–89 % sensitivity", "CORRECT", ""),
    (r"10 000 patients", ["10 000"], "S17 : more than 10,000 patients", "CORRECT", ""),
    (r"Âges limites", ["12", "2", "4"], "S14 ; S13 ; S18", "CORRECT", "« Autorisé » à 12 mois : nuance d'indication (C05)."),
    (r"avant 37 SA", ["37"], "aucune source du dossier ni de l'audit pour la définition de la prématurité", "NON_VERIFIABLE_SRC", "Définition non sourcée dans le glossaire (C21)."),
    (r"5 mois", ["5"], "S5 : before / after 5 months' corrected age", "CORRECT", ""),
    (r"83 %", ["83"], "S5 : 83 % C index", "FAUX", "Indice C présenté comme sensibilité (K17, C03)."),
]


# ---------------------------------------------------------------------------
# 3. Règles de non-calculabilité
# ---------------------------------------------------------------------------
def non_calculable(it) -> str | None:
    v, u, c = it["valeur"], it["unite"], it["contexte"]
    vv = v.split("–")[0]
    if it["fichier"].endswith(".py"):
        if re.search(r"G80\.\d|G11\.4|NG62|CIM-10|'10'|dixième|G 80|code CIM", c) and not u:
            return "code de classification ou identifiant de glossaire"
    try:
        x = num(vv)
    except ValueError:
        return "non numérique"
    if not u and 1950 <= x <= 2030 and "," not in vv:
        return "année (date de publication ou de période)"
    if re.fullmatch(r"\s*\d+(\.\d+)?\s*", c) or re.search(r"(^|\s)" + re.escape(v) + r"\.\d", c) or re.search(re.escape(v) + r"(\.\d)? [A-ZÉ][a-zé]", c[:len(v) + 25]) and not u:
        return "numéro d'îlot, de section ou de titre"
    if re.search(r"\(" + re.escape(v) + r"\)", c) and not u:
        return "numéro de liste"
    if re.search(r"G ?80|G11|CIM-10|NG62|10-GM|Betta 39|Figure \d|Cas \d|e-\d|p-\d|w30139|w20084|;152|;149", c) and not u and x < 200:
        return "code, numéro de figure, de cas ou de référence"
    if re.search(r"Prévalence \(pour 1000\)", c):
        return "intitulé de colonne"
    if re.search(r"CIM-11|10e révision|NG62|'62'|numéro 62", c) and not u:
        return "code ou numéro de document"
    if re.search(r"Cycle Betta", c):
        return "identifiant de cycle"
    if re.search(r"vignette fictive|27 SA|7 mois d’âge corrigé|Un garçon de 3 ans|né à 28 SA|3 mois d’âge corrigé, né à 28|enfant de 6 ans pèse 20|2 jours après|enfant de 3 ans classé", c):
        return "donnée de vignette ou de cas fictif (sans calcul attendu)"
    if re.search(r"octobre 2026|mai 2026|janvier 2025|avril 2024|lues le 15", c) and not u:
        return "date de lecture ou de mise à jour"
    if re.search(r"deux antiépileptiques|cinq niveaux|cinq groupes|Trois classifications|trois grands", c) and not u:
        return "dénombrement descriptif"
    return None


def main() -> int:
    inv = json.loads((ICI / "inventaire.json").read_text(encoding="utf-8"))
    res = []
    for it in inv["items"]:
        ctx = it["contexte"]
        v = it["valeur"]
        vals = {v, v.split("–")[0]}
        trouve_fait = None
        for k in CALCULS:
            if k["motif"] and re.search(k["motif"], ctx) and vals & set(k["valeurs"]):
                trouve_fait = ("calcul", k)
                break
        if not trouve_fait:
            for motif, valeurs, source, verdict, note in VS:
                if re.search(motif, ctx) and vals & set(valeurs):
                    trouve_fait = ("valeur_sourcee", dict(source=source, verdict=verdict, note=note, motif=motif))
                    break
        if trouve_fait:
            nature, f = trouve_fait
            if nature == "calcul":
                res.append(dict(id=it["id"], fichier=it["fichier"], ancre=it["ancre"], valeur=v, unite=it["unite"], nature="calcul",
                                calcul=f["id"], attendu=f["attendu"], trouve=f["trouve"], ecart=f["ecart"], verdict=f["verdict"],
                                formule=f["formule"], source=f["source"], note=f["note"]))
            elif f["verdict"] == "NON_VERIFIABLE_SRC":
                res.append(dict(id=it["id"], fichier=it["fichier"], ancre=it["ancre"], valeur=v, unite=it["unite"], nature="valeur_non_sourcee",
                                attendu=None, trouve=v, ecart=None, verdict="NON_VERIFIABLE", formule=None, source=None, note=f["note"]))
            else:
                res.append(dict(id=it["id"], fichier=it["fichier"], ancre=it["ancre"], valeur=v, unite=it["unite"], nature="valeur_sourcee",
                                attendu=f["source"], trouve=v + (" " + it["unite"] if it["unite"] else ""), ecart=None, verdict=f["verdict"],
                                formule="comparaison à la valeur transcrite de la source (motif " + f["motif"] + ")", source=f["source"].split(" :")[0], note=f["note"]))
            continue
        raison = non_calculable(it)
        if raison:
            res.append(dict(id=it["id"], fichier=it["fichier"], ancre=it["ancre"], valeur=v, unite=it["unite"], nature="non_calculable",
                            attendu=None, trouve=v, ecart=None, verdict="SANS_OBJET", formule=None, source=None, note=raison))
        else:
            res.append(dict(id=it["id"], fichier=it["fichier"], ancre=it["ancre"], valeur=v, unite=it["unite"], nature="a_classer",
                            attendu=None, trouve=v, ecart=None, verdict="NON_VERIFIABLE", formule=None, source=None, note=ctx))
    cal = [r for r in res if r["nature"] in ("calcul", "valeur_sourcee")]
    resume = {
        "total_releves": len(res),
        "calculables": len(cal) + sum(1 for r in res if r["nature"] in ("a_classer", "valeur_non_sourcee")),
        "recalcules": len(cal),
        "correct": sum(1 for r in cal if r["verdict"] == "CORRECT"),
        "arrondi": sum(1 for r in cal if r["verdict"] == "ARRONDI"),
        "faux": sum(1 for r in cal if r["verdict"] == "FAUX"),
        "non_verifiables": sum(1 for r in res if r["verdict"] == "NON_VERIFIABLE"),
        "non_calculables": sum(1 for r in res if r["nature"] == "non_calculable"),
        "calculs_derives": len([k for k in CALCULS if k["nature"] == "calcul"]),
        "calculs_derives_faux": [k["id"] for k in CALCULS if k["verdict"] == "FAUX"],
        "script": "calculs/verifier.py",
    }
    (ICI / "resultats.json").write_text(json.dumps({"resume": resume, "calculs_derives": CALCULS, "occurrences": res},
                                                   ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps(resume, ensure_ascii=False, indent=1))
    for r in res:
        if r["nature"] == "a_classer":
            print("A CLASSER", r["id"], r["fichier"][-9:], r["valeur"], r["unite"], "|", r["note"][:130])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
