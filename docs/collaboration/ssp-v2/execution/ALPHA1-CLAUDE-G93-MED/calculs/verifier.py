#!/usr/bin/env python3
"""Audit ALPHA77 G93 — inventaire scripté et recalcul de toutes les grandeurs de la leçon.

Exécution (depuis la racine du dépôt) :
    python3 docs/collaboration/ssp-v2/execution/ALPHA1-CLAUDE-G93-MED/calculs/verifier.py

Sorties (dossier du script) : inventaire.json, resultats.json. Lecture seule des 7 fichiers canoniques.

Trois familles de contrôles :
  1. RECALCUL : grandeur dérivable (pourcentage d'un effectif, conversion d'unités kPa↔mmHg et cm d'eau↔mmHg,
     arithmétique de dose et de volume, comparaison d'une valeur de cas ou de quiz à un seuil, comparaison
     d'un seuil à la source applicable la plus récente).
  2. CONCORDANCE_SOURCE : valeur rapportée, comparée à la citation exacte de la source lue (Sx de sources.json).
  3. NON_CALCULABLE : identifiant (année, numéro d'îlot, rang, code CIM, nom de gène ou de canal).

Constantes d'unités (définitions conventionnelles, non médicales) :
  1 mmHg = 133,322 Pa ; 1 cm d'eau (cmH2O) = 98,0665 Pa ; 1 kPa = 1000 Pa.
Masse molaire du mannitol : 182,17 g/mol (ChEMBL CHEMBL689, S21).
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from inventaire_base import inventaire  # noqa: E402

PA_MMHG, PA_CMH2O = 133.322, 98.0665
KPA_TO_MMHG = 1000 / PA_MMHG          # 7,5006
CMH2O_TO_MMHG = PA_CMH2O / PA_MMHG    # 0,73556
M_MANNITOL = 182.17

# ---------------------------------------------------------------- concordance avec les sources lues
# (motif de valeur, motif de contexte, source, citation exacte de la source)
C = [
    # Vignettes et quiz : valeurs pédagogiques déclarées fictives (comparées aux seuils dans les recalculs)
    (r"28|38|58", r"Une femme de 28|à 38 kg|homme de 58", "VIGNETTE", "valeurs pédagogiques déclarées fictives (îlot g93-0)"),
    (r"27|25", r"27 cm d’eau|car 27|27 dépasse|27 est|valeur de 27|dépasse 25", "VIGNETTE", "quiz 1 : valeur fictive (recalcul R11)"),
    (r"72|2", r"comateux 72|motrice est de 2", "VIGNETTE", "quiz 2 : valeurs fictives (recalcul R14)"),
    (r"34|74", r"femme de 34|homme de 74", "VIGNETTE", "quiz 3 et 4 : âges fictifs (recalculs R15, R16)"),
    (r"36", r"ouverture est de 36", "VIGNETTE", "cas récapitulatif : valeur déclarée fictive (recalcul R12)"),
    (r"35", r"inférieur à 35", "S3", "A multicomponent lifestyle intervention ... with a BMI <35 kg/m2 (grade B)"),
    (r"40", r"Cycle 40|Betta 40", "NON_CALCULABLE", "numéro de cycle"),
    # HII — EHF 2018 (S2)
    (r"0,5|2|100 000", r"0,5 à 2 pour 100 000", "S2", "Its prevalence has been estimated between 0.5–2 per 100,000 of the general population"),
    (r"90|95", r"90 à 95 %", "S2", "with over 90–95% of patients being obese"),
    (r"5|15", r"prise de 5 à 15 %", "S2", "IIH is reported in the context of gaining 5–15% of body weight"),
    (r"90", r"Jusqu’à 90 %", "S2", "Headache, present in up to 90% of IIH patients"),
    (r"37", r"37 % des patients", "S2", "Medication-overuse headaches are a frequent co-morbidity in IIH (37%)"),
    (r"80", r"Jusqu’à 80 %", "S2", "olfactory dysfunction in up to 80% of IIH patients"),
    (r"4", r"environ 4 %", "S2", "it can be asymmetrical in 4% of cases"),
    (r"40", r"environ 40 %|approche 40 %", "S2", "There is a high frequency (40%) of diagnostic errors in IIH"),
    (r"25|28|30", r"25 cm d’eau|28 cm d’eau|zone grise de 25|25 à 30|28 chez l’|supérieure à 25 cm|Adulte : 25|enfant : 28",
     "S2", "should not exceed 25 cmH2O in adults and 28 cmH2O in children ... 25–30 cmH2O constituting a grey area"),
    (r"250|280", r"250 mm|280 mm", "S2", "CSF pressure exceeds 250 mm CSF (or 280 mm CSF in obese children)"),
    (r"90|50", r"jusqu’à 90 % des|90 % des HII|50 % des sujets sains", "S2",
     "reported prevalence rates of up to 90% ... asymmetry of the transverse sinus can occur in 50% of healthy individuals"),
    (r"48|1500", r"48 %|1500 mg", "S2", "48% of patients discontinue acetazolamide when doses of just 1500 mg are utilised"),
    (r"4|40", r"IIHTT, 4 g|plus de 40 %|IIHTT à 4", "S2", "greater than 40% of patients were treated with 4 g of acetazolamide daily"),
    (r"1,8|4,3", r"1,8 contre 4,3", "S2", "lower revision rates ... (1.8 versus 4.3 revisions per patient respectively)"),
    (r"51|30", r"51 %|30 % multiples|30 % plusieurs", "S2", "Shunt revision is common with 51% requiring revision and multiple revisions required in 30%"),
    (r"26", r"révisée dans 26 %", "S2", "this procedure also has a 26% revision rate"),
    (r"68|79", r"68 %|79 %", "S2", "ongoing headache in 68% at 6 months, 77% at 12 months and 79% at 2 years post-shunting"),
    (r"64", r"64 %", "S2", "there is also a 64% chance of a headache exacerbation in the week following LP"),
    (r"0,05|0,14|100|90", r"0,05 à 0,14|de 100 % et|céphalées de 90", "S2",
     "very low associated mortality (0.05%–0.14%) ... 100% resolution of papilloedema and 90% experience headache improvement"),
    (r"40", r"\(40 patients\)|ouverte \(40", "S2", "an open label study which randomly assigned 40 patients to acetazolamide or topiramate"),
    (r"26", r"ouverte de 26", "S2", "A prospective open-label study of 26 patients"),
    # Abbott 2023 (S3)
    (r"11,9|−27|24|27,2|27,8|11,2|35", r"11,9|−27 kg|kg à 24 mois|27,2|27,8|11,2|atteint 35|dessous de 35|\(35 ou plus", "S3",
     "27.2-27.8 kg weight loss at 24 months ... (-11.9 cm H2O) at 24 months ... (-11.2 cm H2O) at 6 months ... BMI ≥35 (grade A) ... <35 (grade B)"),
    # TCC, œdème — Jha 2019 (S7)
    (r"20–22|20|22|45|80", r"20–22 mmHg|20 à 22 mmHg|45 à 80", "S7", "ICP elevation above the accepted threshold of 20–22 mmHg occurs in 45%–80% of patients with TBI"),
    (r"60|15", r"plus de 60 %|environ 15 %", "S7", "occurring in >60% of patients with mass lesions, and ~15% of those with normal initial computed tomography scans"),
    (r"20|25", r"20 à 25 mL", "S7", "PVI is the volume (mL) required to raise ICP 10-fold and is normally 20-25 mL"),
    (r"1", r"[Dd]ès (environ )?1 heure|surexprimé dès 1", "S7", "It has been reported as early as 1 hour post-TBI in humans ; NKCC1 is upregulated as early as 1 hour post-injury"),
    (r"6|24", r"6 à 24", "S7", "a leaky endothelium/VasE that may peak between 6–24 hours"),
    (r"3|4", r"3 à 4 jours", "S7", "can persist for 3–4 days"),
    (r"9", r"2 et 9", "NON_CALCULABLE", "MMP-9 : identifiant de protéine"),
    (r"66", r"66 sujets", "S7", "Another RCT (66 subjects) demonstrated that glibenclamide reduced contusion expansion"),
    # EUROMENE (S6)
    (r"0,1|0,7", r"0,1 à 0,7", "S6", "Prevalence rates have been estimated as between 0.1 and 0.7%"),
    (r"3", r"3 millions", "S6", "between 1 million and over 5 million people, probably around 3 million"),
    (r"38", r"38 °C", "S6", "prolonged fever ≥ 38 °C"),
    (r"2–4", r"2–4 le nombre", "S6", "we recommend 2–4 ME/CFS specialist doctors/1 million population"),
    # Kystes (S10)
    (r"2,3|29|1235|70", r"2,3|29 sur|1235|70 ans", "S10", "The sample comprised representative populations (n = 1235) aged ≥ 70 years ... prevalence 2.3 % (n = 29)"),
    # Reye (S9) et Aspirine (S13)
    (r"30|40", r"30 à 40", "S9", "Death occurs in about 30-40% of cases from brainstem dysfunction"),
    (r"3|5", r"3 à 5 jours", "S9", "an intermediate disease-free interval of 3-5 days"),
    (r"12", r"12 ans", "S13", "Les adolescents à partir de 12 ans présentant de la fièvre et/ou des infections virales ... Chez les enfants de moins de 12 ans ... n'est pas indiquée"),
    # ERC-ESICM 2021 (S4) — chiffres ensuite confrontés à 2025 (S5) dans les recalculs
    (r"94|98", r"94 à 98", "S4", "titrate the inspired oxygen to achieve an arterial oxygen saturation of 94–98%"),
    (r"10–13|10|13|75|100", r"10–13 kPa|10 à 13 kPa|75 à 100", "S4", "PaO2 10–13 kPa or 75–100 mmHg"),
    (r"4,5|6,0|35|45|35–45", r"4,5 à 6,0|35–45|35 à 45", "S4", "a normal arterial partial pressure of carbon dioxide (PaCO2), i.e. 4.5–6.0 kPa or 35–45 mmHg"),
    (r"65", r"65 mmHg", "S4", "Avoid hypotension (< 65 mmHg)"),
    (r"0,5", r"0,5 mL/kg/h", "S4", "Target mean arterial pressure (MAP) to achieve adequate urine output (> 0.5 mL kg−1 h−1)"),
    (r"32|36|24", r"32 et 36 °C|au moins 24 heures", "S4", "Maintain a target temperature at a constant value between 32 and 36 °C for at least 24 h"),
    (r"37,7|72", r"37,7|72 heures chez le patient|pendant au moins 72|pendant 72", "S4", "Avoid fever (> 37.7 °C) for at least 72 h after ROSC in patients who remain in coma"),
    (r"3|72", r"motrice de 3|3 ou moins|72 heures ou plus|72 heures écoulées|confondants, 72", "S4", "In a comatose patient with M ≤ 3 at ≥ 72 h from ROSC"),
    (r"72|24|60|48|48–72", r"cornéens à 72|somesthésiques à 24|au-delà de 24|60 µg/L|à 48|48–72|avant 72|Absence bilatérale à 24|à 48 et/ou 72",
     "S4", "no pupillary and corneal reflexes at ≥ 72 h, bilaterally absent N20 SSEP wave at ≥ 24 h, highly malignant EEG at > 24 h, NSE > 60 µg L−1 at 48 h and/or 72 h, status myoclonus ≤ 72 h"),
    (r"100", r"exact à 100", "S4", "No single predictor is 100% accurate"),
    (r"24|36", r"observation de 24|réchauffement à 36", "S4", "Includes a 24-h observation period after rewarming to 36 °C before clinical testing for brain death"),
    # Mannitol — FI suisse (S12)
    (r"1|2|30|60|500|20|24", r"Mannitol 20|1 à 2 g/kg|30 à 60 minutes|500 mL|à 20 %|en 1 heure|24 heures en contexte|20 % B. Braun|20 % \(novembre|Mannitol 20 % :",
     "S12", "1–2 g/kg de poids corporel en 30–60 min. Par exemple: 500 ml de Mannitol 20% en 1 heure ... Ne pas perfuser plus de 500 ml de Mannitol 20% B. Braun en 24 heures (posologie de l’oligurie)"),
    # Diamox — FI suisse (S11)
    (r"250", r"Comprimés de 250", "S11", "1 comprimé contient: Acetazolamidum 250 mg"),
]

NC_CTX = [r"consultées le 15\.10|^\s*>|Rang Diagnostic|Étape Moyen|Figure \d|n\b", r"G 93", r"\d{2}\.\d{2}\.20\d\d", r"\(_k\[|insert\(0|'6','six|'1','type 1'|\('1'"]


def concordance(item: dict) -> dict | None:
    v = item["valeur"].replace(" ", " ").replace(" ", " ")
    for vpat, ctx, src, cit in C:
        if re.fullmatch(vpat, v) and re.search(ctx, item["contexte"]):
            return {"source": src, "citation": cit}
    return None


# ---------------------------------------------------------------- recalculs
def r(id_, attendu, trouve, formule, source, tol, note="", verdict=None):
    ecart = None if (attendu is None or trouve is None) else round(trouve - attendu, 4)
    if verdict is None:
        if trouve is None:
            verdict = "INFORMATIF"
        elif attendu is None:
            verdict = "NON_VERIFIABLE"
        elif abs(ecart) <= 1e-9:
            verdict = "CORRECT"
        elif abs(ecart) <= tol:
            verdict = "ARRONDI"
        else:
            verdict = "FAUX"
    return {"id": id_, "attendu": attendu, "trouve": trouve, "ecart": ecart, "tolerance": tol,
            "verdict": verdict, "formule": formule, "source": source, "note": note}


def seuil(id_, valeur, borne, sens, formule, source, note=""):
    ok = {">": valeur > borne, ">=": valeur >= borne, "<": valeur < borne, "<=": valeur <= borne}[sens]
    return r(id_, 1.0, 1.0 if ok else 0.0, formule, source, 0, note)


def recalculs() -> list[dict]:
    R = []
    pct = lambda a, b: round(100 * a / b, 1)
    # Kyste arachnoïdien
    R.append(r("R01", pct(29, 1235), 2.3, "29/1235 × 100", "S10", 0.05, "29/1235 = 2,348 % → 2,3 %"))
    # Conversions kPa → mmHg (cibles post-arrêt)
    R.append(r("R02", round(10 * KPA_TO_MMHG, 1), 75.0, "PaO2 10 kPa × 7,5006", "S4 ; définitions d'unités", 0.5))
    R.append(r("R03", round(13 * KPA_TO_MMHG, 1), 100.0, "PaO2 13 kPa × 7,5006 = 97,5 mmHg (écrit 100)", "S4", 2.6,
               "arrondi de la source (75–100 mmHg) ; écart 2,5 mmHg sans conséquence"))
    R.append(r("R04", round(4.5 * KPA_TO_MMHG, 1), 35.0, "PaCO2 4,5 kPa × 7,5006 = 33,75 mmHg (écrit 35)", "S4 (texte 2021) ; S5 corrige à 4,7 kPa", 0.5,
               "4,5 kPa ≠ 35 mmHg ; 35 mmHg = 4,67 kPa. Incohérence d'unités reprise de la source 2021, corrigée en 2025 (4,7–6,0 kPa) : voir C03"))
    R.append(r("R05", round(35 / KPA_TO_MMHG, 2), 4.5, "35 mmHg ÷ 7,5006 = 4,67 kPa (la leçon écrit 4,5)", "S5 : « 4.7–6.0 kPa (or approximately 35–45 mmHg) »", 0.1,
               "borne basse fausse de 0,17 kPa ; valeur actuelle 4,7 kPa"))
    R.append(r("R06", round(6.0 * KPA_TO_MMHG, 1), 45.0, "PaCO2 6,0 kPa × 7,5006", "S4 ; S5", 0.1))
    # Confrontation des cibles 2021 à la version 2025 (règle : la source primaire applicable la plus récente l'emporte)
    R.append(r("R07", 4.7, 4.5, "borne basse PaCO2 : 2025 = 4,7 kPa ; leçon = 4,5", "S5 Table 1 et « Control of ventilation »", 0.0,
               "C03"))
    R.append(r("R08", 37.5, 37.7, "seuil de fièvre à prévenir : 2025 = 37,5 °C ; leçon = 37,7 °C", "S5 « Actively prevent fever by targeting a temperature [≤]37.5 °C »", 0.0,
               "C02 ; signe ≤ illisible dans l'extraction PDF, sens explicite (prévenir la fièvre)"))
    R.append(r("R09", 6.0, 3.0, "seuil d'entrée de l'algorithme pronostique : 2025 = M < 6 (non-obéissance) ; leçon = M ≤ 3",
               "S5 « applies to unconscious patients, defined as not being awake and obeying commands (M < 6) at 72 h »", 0.0, "C01"))
    R.append(r("R10", 60.0, 65.0, "PAM : 2025 = > 60–65 mmHg ; leçon = ≥ 65 mmHg", "S5 « target a mean arterial pressure (MAP) >60–65 mmHg »", 5.0,
               "65 reste dans la fourchette 2025 ; borne basse élargie : MINEUR (C02)"))
    R.append(r("R10b", 36.0, 72.0, "durée de prévention de la fièvre : 2025 = 36 à 72 h ; leçon = au moins 72 h", "S5 « active prevention of fever for 36 to 72 h »", 36.0,
               "72 h est la borne haute de 2025 : ARRONDI, mais l'intervalle doit être donné"))
    # HII : seuils et cas
    R.append(seuil("R11", 27, 25, ">", "quiz 1 : 27 > 25 (dépasse le seuil adulte)", "S2"))
    R.append(seuil("R11b", 27, 30, "<=", "quiz 1 : 27 ≤ 30 (dans la zone grise 25–30)", "S2", "la correction « zone grise » est exacte"))
    R.append(seuil("R12", 36, 30, ">", "cas récapitulatif : 36 > 30 (au-delà de la zone grise)", "S2"))
    R.append(seuil("R13", 38, 35, ">=", "vignette 1 : IMC 38 ≥ 35 → chirurgie bariatrique à considérer (grade A)", "S3",
                   "le cas récapitulatif laisse les deux options ouvertes au lieu d'appliquer le seuil à la patiente (C15)"))
    R.append(seuil("R14", 2, 3, "<=", "quiz 2 : M2 ≤ 3 (critère 2021) et M2 < 6 (critère 2025) — l'entrée dans l'algorithme est remplie", "S4 ; S5",
                   "la réponse attendue (exclure la sédation d'abord) reste juste sous les deux versions"))
    R.append(seuil("R15", 8, 6, ">=", "quiz 3 : fatigue de 8 mois ≥ 6 mois, mais malaise post-effort absent", "S6"))
    R.append(seuil("R16", 74, 70, ">=", "quiz 4 : 74 ans ≥ 70 ans (population de l'étude suédoise)", "S10"))
    R.append(r("R17", 25.0, 25.0, "ICHD-3 : 250 mm de liquide = 25 cm (même seuil que Friedman)", "S2 tableau 1", 0))
    R.append(r("R18", 28.0, 28.0, "ICHD-3 : 280 mm = 28 cm (enfant obèse)", "S2 tableau 1", 0,
               "la leçon écrit « 250 mm » sans préciser « de liquide » : unité ambiguë (C14)"))
    # Conversions cm d'eau ↔ mmHg (deux unités coexistent dans la leçon sans passerelle)
    R.append(r("R19", round(25 * CMH2O_TO_MMHG, 1), None, "25 cm d'eau × 0,7356 = 18,4 mmHg", "définitions d'unités", 0,
               "non écrit dans la leçon : passerelle proposée (C13)"))
    R.append(r("R20", round(30 * CMH2O_TO_MMHG, 1), None, "30 cm d'eau = 22,1 mmHg", "définitions d'unités", 0))
    R.append(r("R21", round(20 / CMH2O_TO_MMHG, 1), None, "20 mmHg = 27,2 cm d'eau ; 22 mmHg = 29,9 cm d'eau", "définitions d'unités", 0))
    R.append(r("R22", round(11.9 * CMH2O_TO_MMHG, 1), None, "baisse de 11,9 cm d'eau = 8,8 mmHg", "S3 ; définitions d'unités", 0))
    # Mannitol
    R.append(r("R23", 500 * 0.20, 100.0, "500 mL × 200 g/L = 100 g (exemple de la FI)", "S12 composition (200 g/1000 mL)", 0,
               "100 g correspond à 1–2 g/kg seulement pour 50–100 kg : l'exemple n'est pas une dose fixe (C11)"))
    R.append(r("R24", 70 * 1 / 0.2, None, "patient de 70 kg : 1 g/kg = 70 g = 350 mL ; 2 g/kg = 140 g = 700 mL", "S12", 0,
               "700 mL dépasse le plafond de 500 mL/24 h, mais ce plafond appartient à la posologie de l'oligurie : la leçon l'attribue correctement"))
    R.append(r("R25", round(200 / M_MANNITOL * 1000), None, "osmolarité théorique : 200 g/L ÷ 182,17 g/mol = 1098 mOsm/L", "S12 ; S21 (masse molaire)", 0,
               "explique « solution hypertonique » et la contre-indication « hyperosmolarité préexistante »"))
    R.append(r("R26", 1.0, 1.0, "dose-test oligurie : 200 mg/kg ÷ 200 mg/mL = 1 mL/kg", "S12", 0, "cohérence interne de la FI (proposition p-2)"))
    R.append(r("R27", round(2 / 0.5, 1), None, "débit induit : 1–2 g/kg en 30–60 min = 1 à 4 g/kg/h", "S12", 0))
    # Acétazolamide
    R.append(r("R28", 4000 / 250, None, "4 g/j = 16 comprimés de 250 mg", "S2 ; S11", 0))
    R.append(r("R29", 1000.0, 4000.0, "4 g/j (IIHTT) comparé à la dose orale maximale de la FI suisse (1000 mg/24 h, glaucome et épilepsie)",
               "S11 Posologie", 0, "4 fois la dose orale maximale de la FI : à signaler explicitement (C06)", verdict="INFORMATIF"))
    R.append(r("R30", round(1500 / 1000, 2), None, "1500 mg/j = 1,5 × la dose orale maximale de la FI", "S11", 0))
    R.append(r("R31", 24.0, None, "Swisspeddose (pression intracrânienne élevée) : 8–10 mg/kg/dose × 3 = 24–30 mg/kg/j ≤ 100 mg/kg/j", "S11 (Swisspeddose)", 0,
               "cohérence interne ; dose absente de la leçon (C20)"))
    R.append(r("R32", round(62.2 / 2000 * 100, 1), 3.1, "sodium du flacon i.v. : 62,2 mg / 2 g × 100", "S11", 0.05, "cohérence interne de la FI"))
    # Divers
    R.append(r("R33", round(4.3 / 1.8, 2), None, "rapport des révisions LP/VP = 4,3 / 1,8 = 2,39", "S2", 0))
    R.append(r("R34", 1235 - 29, None, "témoins sans kyste = 1206", "S10", 0))
    R.append(r("R35", round(100 / 3, 1), 37.0, "« plus du tiers » (33,3 %) contre 37 % : cohérence", "S2", 4.0,
               "37 % > 33,3 % : les deux formulations de la leçon concordent", verdict="CORRECT"))
    R.append(r("R36", round(0.5 * 80, 1), None, "diurèse cible > 0,5 mL/kg/h : 40 mL/h chez 80 kg", "S4", 0))
    R.append(r("R37", 27.5, 27.0, "« environ −27 kg » contre 27,2–27,8 kg (milieu 27,5)", "S3", 0.8))
    R.append(r("R38", round(8.2 * CMH2O_TO_MMHG, 1), None, "IIH:WT : différence de −8,2 cm d'eau à 24 mois = −6,0 mmHg", "S15", 0))
    R.append(r("R39", 30.0, None, "TSPO (proposition sémiologie) : FC debout > +30/min (> 20 ans), > +40/min (plus jeunes) ou > 120/min", "S6", 0))
    R.append(r("R40", 2.0, 2.0, "pronostic : au moins 2 prédicteurs (2021 et 2025 identiques)", "S4 ; S5", 0))
    R.append(r("R41", 60.0, 60.0, "NSE > 60 µg/L à 48 et/ou 72 h (2021 et 2025 identiques)", "S4 ; S5", 0))
    R.append(r("R42", 72.0, 72.0, "délai minimal de pronostic : 72 h (2021 et 2025)", "S4 ; S5", 0))
    R.append(r("R43", 25.0, 30.0, "zone grise : 25 à 30 cm d'eau", "S2", 0, verdict="CORRECT"))
    return R


def main() -> None:
    items = inventaire()
    for it in items:
        if it["categorie"] == "GRANDEUR":
            if re.fullmatch(r"\d{1,2}\.\d{2}", it["valeur"]) and re.search(r"\d\.20\d\d", it["contexte"]):
                it["categorie"] = "NON_CALCULABLE:date"
                continue
            if any(re.search(p, it["contexte"]) for p in NC_CTX) and re.fullmatch(r"\d{1,2}", it["valeur"]) \
                    and not concordance(it):
                it["categorie"] = "NON_CALCULABLE:identifiant"
                continue
            if it["fichier"].endswith(".py"):
                it["categorie"] = "NON_CALCULABLE:code_glossaire"
                continue
            c = concordance(it)
            if c:
                if c["source"] == "NON_CALCULABLE":
                    it["categorie"] = "NON_CALCULABLE:identifiant"
                else:
                    it["categorie"] = "VIGNETTE" if c["source"] == "VIGNETTE" else "CONCORDANCE_SOURCE"
                    it["source"], it["citation"] = c["source"], c["citation"]
            else:
                it["categorie"] = "NON_RAPPROCHEE"
    res = recalculs()
    cat = lambda k: sum(1 for i in items if i["categorie"].startswith(k))
    inv = {"total_releves": len(items), "grandeurs": cat("CONCORDANCE") + cat("VIGNETTE") + cat("NON_RAPPROCHEE"),
           "non_calculables": cat("NON_CALCULABLE"), "concordance_source": cat("CONCORDANCE"),
           "vignettes": cat("VIGNETTE"), "non_rapprochees": cat("NON_RAPPROCHEE"), "items": items}
    v = {k: sum(1 for x in res if x["verdict"] == k) for k in ("CORRECT", "ARRONDI", "FAUX", "NON_VERIFIABLE", "INFORMATIF")}
    calc = [x for x in res if x["verdict"] != "INFORMATIF"]
    out = {"calculables": len(calc), "recalcules": len(calc), "informatifs_audit": v["INFORMATIF"], "verdicts": v, "resultats": res}
    (HERE / "inventaire.json").write_text(json.dumps(inv, ensure_ascii=False, indent=1), encoding="utf-8")
    (HERE / "resultats.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps({k: inv[k] for k in inv if k != "items"}, ensure_ascii=False))
    print(json.dumps({k: out[k] for k in out if k != "resultats"}, ensure_ascii=False))
    for x in res:
        if x["verdict"] in ("FAUX", "ARRONDI", "NON_VERIFIABLE"):
            print(x["id"], x["verdict"], x["formule"])
    for i in items:
        if i["categorie"] == "NON_RAPPROCHEE":
            print("NR", i["id"], i["ancre"], "|", i["valeur"], "|", i["contexte"][:150])


if __name__ == "__main__":
    main()
