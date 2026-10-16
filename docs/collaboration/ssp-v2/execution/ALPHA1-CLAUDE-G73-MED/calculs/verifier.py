#!/usr/bin/env python3
"""Recalcul et vérification scriptés de toutes les grandeurs de G73 (exigence CALCULS, 16.10.2026).

Usage (depuis la racine du worktree) :
    python3 docs/collaboration/ssp-v2/execution/ALPHA1-CLAUDE-G73-MED/calculs/inventaire.py
    python3 docs/collaboration/ssp-v2/execution/ALPHA1-CLAUDE-G73-MED/calculs/verifier.py

Principe. Chaque occurrence de inventaire.json est rattachée à une règle :
  * NON_GRANDEUR : numérotation d’îlot, de liste ou d’item, index de lettres du glossaire, nom chimique ;
  * CALCUL : grandeur dérivée recalculée ici (formule écrite, tolérance explicite) ;
  * SOURCE : grandeur rapportée, comparée à la valeur lue dans la source (citation dans SOURCES_LUES) ;
    la cohérence numérateur/dénominateur est recalculée quand la source donne n/N.
Aucune occurrence ne doit rester NON_RATTACHEE (sinon l’audit n’est pas clos).
Sortie : resultats.json = [{id, attendu, trouve, ecart, verdict, formule, source}] + synthèse.
"""
import json, re
from pathlib import Path

HERE = Path(__file__).resolve().parent
INV = json.loads((HERE / "inventaire.json").read_text(encoding="utf-8"))

def num(s):
    s = s.replace(" ", "").replace("\xa0", "").replace(" ", "")
    s = re.sub(r"^[≈≤≥<>+]", "", s).replace("−", "-")
    return float(s.replace(",", "."))

def pct(n, d):
    return 100.0 * n / d

# ---------------------------------------------------------------- calculs dérivés
def increment(a0, a1):
    return (a1 - a0) / a0 * 100.0

CALCS = {}
def calc(key, attendu, formule, source, tol=0.5):
    CALCS[key] = dict(attendu=attendu, formule=formule, source=source, tol=tol)

calc("incr_2.0_3.6", increment(2.0, 3.6), "(3,6 − 2,0) ÷ 2,0 × 100", "S5 (définition de l’incrément : hausse relative du PAMC après contraction)")
calc("incr_1.5_2.7", increment(1.5, 2.7), "(2,7 − 1,5) ÷ 1,5 × 100", "S5")
calc("incr_2.5_4.5", increment(2.5, 4.5), "(4,5 − 2,5) ÷ 2,5 × 100", "S5")
calc("incr_distracteur_12", (2.7 - 1.5) / 1.5 * 100.0, "distracteur A : 12 % ≠ 80 % (faux voulu)", "quiz")
calc("incr_distracteur_180", 2.7 / 1.5 * 100.0, "distracteur C : 180 % = A1 ÷ A0 × 100, confusion voulue", "quiz", tol=0.5)
calc("echappent_41", 100 - 58.7, "100 − 58,7 = 41,3 % de faux négatifs au seuil de 100 %", "S5", tol=0.5)
# sensibilités et spécificité recalculées en effectifs entiers (63 SMLE, 93 témoins) : S5 Results
calc("sens60", pct(49, 63), "49/63", "S5 : 63 SMLE")
calc("sens100", pct(37, 63), "37/63", "S5")
calc("spec60", pct(92, 93), "92/93", "S5 : 93 témoins")
calc("cbpc_51", pct(44, 87), "44/87", "S4 : 44 SCLC-LEMS / 87")
calc("cbpc_91", pct(40, 44), "40/44 diagnostiqués ≤ 6 mois", "S4")
calc("cbpc_98", pct(43, 44), "43/44 diagnostiqués ≤ 12 mois", "S4")
calc("femmes_66", pct(46, 70), "46/70", "S7 Table 1")
calc("nt_77", pct(54, 70), "54/70", "S7 Table 1")
calc("amifa_91", pct(59, 65), "59/65 (dénominateur 65, non 70)", "S7 Results")
calc("leg_57", pct(35, 62), "35/62", "S7 Results")
calc("is5ans_44", pct(14, 34), "14/34 = 41,2 % alors que la source imprime « 14/34 (44%) »", "S7 Results")
calc("pred_arret_38", pct(13, 34), "13/34 arrêts (tous motifs)", "S7 Table 3")
calc("aza_arret_50", pct(15, 30), "15/30 arrêts (tous motifs)", "S7 Table 3")
calc("pred_arret_EI", 38 * 0.39, "38 % arrêts × 39 % pour effets indésirables = part des patients arrêtant pour EI", "S7 Results", tol=0.5)
calc("aza_arret_EI", 50 * 0.80, "50 % × 80 %", "S7 Results", tol=0.5)
calc("pyr_arret_EI", 32 * 0.50, "32 % × 50 %", "S7 Results", tol=0.5)
calc("adl_62", pct(39, 63), "39/63", "S6")
calc("garcons_66", pct(31, 47), "31/47", "S12 Table 1")
calc("influB_63", pct(28 + 2, 47), "(28 influenza B + 2 co-infections B + M. pneumoniae)/47", "S12 Table 1", tol=1.0)
calc("influB_seul", pct(28, 47), "28/47 influenza B seule", "S12 Table 1")
calc("trich_europe", pct(56912, 65818), "56 912/65 818 (texte des résultats : 86 %)", "S13", tol=0.6)
calc("pns_lems_vgcc_sans_cancer", 3 + 2 + 1, "phénotype haut risque 3 + anticorps à risque intermédiaire (P/Q VGCC) 2 + cancer non trouvé, suivi < 2 ans 1", "S3 Table 5 et Table 2", tol=0)
calc("pns_cbpc_18mois", 3 + 2 + 4, "3 + 2 + cancer trouvé et concordant 4", "S3 Table 5", tol=0)
calc("pns_sans_cancer_2ans", 3 + 2 + 0, "3 + 2 + cancer non trouvé, suivi ≥ 2 ans 0", "S3 Table 5", tol=0)
calc("pns_max_sans_cancer", 3 + 3 + 1, "maximum sans cancer = 7 < 8 : le niveau « défini » exige un cancer", "S3 Table 5", tol=0)
calc("firdapse_paliers_15_60", (60 - 15) / 5, "(60 − 15) ÷ 5 = 9 paliers ; à 4–5 j/palier : 36–45 jours", "S16 Posologie", tol=0)
calc("firdapse_prises_60", 60 / 20, "60 mg/j ÷ 20 mg par prise = 3 prises au minimum", "S16", tol=0)
calc("firdapse_prises_80", 80 / 20, "80 mg/j ÷ 20 mg = 4 prises au minimum", "S16", tol=0)
calc("firdapse_15mg_3prises", 15 / 3, "15 mg ÷ 3 prises = 5 mg = un demi-comprimé à 10 mg sécable", "S16 Forme pharmaceutique", tol=0)
calc("firdapse_15mg_4prises", 15 / 4, "15 mg ÷ 4 prises = 3,75 mg : non réalisable avec des demi-comprimés de 5 mg", "S16", tol=0)
calc("firdapse_leger_10", 5 * 2, "5 mg × 2 = 10 mg/j", "S16", tol=0)
calc("firdapse_urine", 19 + 81.7, "19 % inchangé + 74,0–81,7 % métabolite = 93–100,7 % (FI : 93,2–100 %)", "S16 Élimination", tol=1.0)
calc("firdapse_cout_jour_60", 1567.25 / 100 * 6, "PP 1567,25 CHF / 100 cp × 6 cp/j (60 mg) = CHF par jour", "S16 Présentation", tol=0.01)
calc("prev_suisse", 0.3e-5 * 9048900, "0,3/100 000 × 9 048 900 habitants = cas prévalents attendus en Suisse", "S8 ; S31", tol=0.5)
calc("inc_suisse", 0.04e-5 * 9048900, "0,04/100 000/an × 9 048 900 = nouveaux cas par an", "S8 ; S31", tol=0.2)
calc("prev_per_million", 0.3 * 10, "0,3/100 000 = 3 par million (S7 : 2,3–3,5 par million)", "S7 ; S8", tol=0)
calc("pns_1_sur_300", 100 / 300, "1/300 = 0,33 % des patients cancéreux", "S3", tol=0.01)
calc("cochrane_ic_sym", 2.44 + (2.44 - 1.22), "borne haute symétrique attendue 2,44 + 1,22 = 3,66 ; la source imprime « 3.6 »", "S10", tol=0.07)
calc("survie_ratio", 17 / 7.0, "17 ÷ 7,0 = rapport des médianes", "S6", tol=0.01)

# ------------------------------------------- contrôle des chiffres écrits dans les propositions
# (valeur écrite dans propositions/*.html, valeur recalculée, tolérance d’arrondi, source)
PROP = [
 ("bulbaire avec cancer 55 %", 55, pct(24, 44), 0.5, "S4 Table 1 : 24/44"),
 ("bulbaire sans cancer 26 %", 26, pct(11, 43), 0.5, "S4 : 11/43"),
 ("perte de poids 61 %", 61, pct(27, 44), 0.5, "S4 : 27/44"),
 ("perte de poids 19 %", 19, pct(8, 43), 0.5, "S4 : 8/43"),
 ("tabac 66 %", 66, pct(29, 44), 0.5, "S4 : 29/44"),
 ("tabac 16 %", 16, pct(7, 43), 0.5, "S4 : 7/43"),
 ("âge ≥ 50 ans 91 %", 91, pct(40, 44), 0.5, "S4 : 40/44"),
 ("âge ≥ 50 ans 70 %", 70, pct(30, 43), 0.5, "S4 : 30/43"),
 ("Karnofsky < 70 : 52 %", 52, pct(23, 44), 0.5, "S4 : 23/44"),
 ("Karnofsky < 70 : 23 %", 23, pct(10, 43), 0.5, "S4 : 10/43"),
 ("bouche sèche 56 %", 56, pct(19, 34), 0.5, "S4 : 19/34"),
 ("bouche sèche 61 %", 61, pct(20, 33), 0.5, "S4 : 20/33"),
 ("dysfonction érectile 56 %", 56, pct(9, 16), 0.5, "S4 : 9/16"),
 ("dysfonction érectile 47 %", 47, pct(8, 17), 0.5, "S4 : 8/17"),
 ("membres supérieurs 74 %", 74, pct(20, 27), 0.5, "S4 : 20/27"),
 ("membres supérieurs 52 %", 52, pct(16, 31), 0.5, "S4 : 16/31"),
 ("rapport symptômes bulbaires ≈ 2,1", 2.1, (24 / 44) / (11 / 43), 0.05, "S4"),
 ("RV+ incrément ≥ 60 % ≈ 72", 72, (49 / 63) / (1 / 93), 0.5, "S5 : 49/63 et 1/93"),
 ("RV− incrément ≥ 60 % ≈ 0,22", 0.22, (14 / 63) / (92 / 93), 0.006, "S5"),
 ("faux négatifs ≈ un sur cinq (22 %)", 22, 100 - 77.8, 0.5, "S5"),
 ("spécificité contre myasthénie 95,7 % = 22/23", 95.7, pct(22, 23), 0.05, "S5"),
 ("Suisse : ≈ 27 patients", 27, 0.3e-5 * 9048900, 0.5, "S8 ; S31"),
 ("Suisse : 3 à 4 nouveaux cas par an", 3.6, 0.04e-5 * 9048900, 0.05, "S8 ; S31"),
 ("Firdapse : ≈ 94 francs par jour", 94, 1567.25 / 100 * 6, 0.1, "S16"),
 ("Firdapse : ≈ 2820 francs par 30 jours", 2820, 1567.25 / 100 * 6 * 30, 2.0, "S16"),
 ("Firdapse : boîte ≈ 17 jours", 17, 100 / 6, 0.5, "S16"),
 ("Leiden : moins d’un sur quatre (16/70)", 22.9, pct(16, 70), 0.05, "S7 Table 1"),
 ("arrêts azathioprine pour EI ≈ 40 %", 40, 50 * 0.80, 0.5, "S7"),
 ("arrêts prednisolone pour EI ≈ 15 %", 15, 38 * 0.39, 0.5, "S7"),
 ("influenza B seule 28/47", 59.6, pct(28, 47), 0.05, "S12"),
 ("trichinellose Europe 86 %", 86, pct(56912, 65818), 0.5, "S13"),
 ("Roumanie : la moitié (28 564 / 56 912)", 50, pct(28564, 56912), 0.5, "S13"),
 ("DELTA-P vignette : au moins 3 points → au moins 55,5 %", 3, 1 + 1 + 1, 0, "S4 (A + T + L)"),
 ("Cas 2 du quiz sémiologique : 4 points → 85,7 %", 4, 1 + 1 + 1 + 1, 0, "S4 (D + L + T + A)"),
 ("PNS-Care : 3 + 2 + 1 = 6", 6, 3 + 2 + 1, 0, "S3"),
 ("PNS-Care : 3 + 2 + 4 = 9", 9, 3 + 2 + 4, 0, "S3"),
 ("PNS-Care : 3 + 2 + 0 = 5", 5, 3 + 2 + 0, 0, "S3"),
 ("PNS-Care : maximum sans cancer 7", 7, 3 + 3 + 1, 0, "S3"),
 ("quatre prises possibles à 20 mg/j (4 × 5 mg)", 20, 4 * 5, 0, "S16"),
 ("atropine 1 à 2 mg IV, répétée toutes les 5 à 30 min", 2, 2, 0, "S17 (valeur recopiée, non calculée)"),
]

# --------------------------------------------------------------- valeurs lues
SOURCES_LUES = {
 "S3": ["approximately 1 of 300 patients with cancer", "1.6 to 8.9 per million person-years", "About 90% of patients have symptoms of autonomic dysfunction",
        "present in nearly 90% of the patients", "repeated every 4–6 months for 2 years", "definite PNS (score ≥8)", "score of 6 (probable)", "definite (score 9)", "possible (score 5)", "18 months later", ">2 years"],
 "S4": ["score 0 = 0%, 1 = 18.8%, 2 = 45%, 3 = 55.5%, 4 = 85.7%, 5 = 87.5%, 6 = 100%", "AUC ... 82.5%", "5-point ... AUC to 84.5%", "within six months in 91% and within 12 months in 98%",
        "DELTA-P score of 1 was diagnosed with SCLC 25 months after", "Number 44 43", "Weight loss ≥ 5%", "age at onset ≥ 50 years", "Karnofsky performance score < 70", "incremental responses of over 60%",
        "repeated after three months, then every six months for two years ... DELTA-P 3–6 ; once after six months ... 0–1 ; every six months for two years ... 2", "over 90% of patients", "Approximately 60% of LEMS patients have an associated SCLC", "within 3 months of symptom onset"],
 "S5": ["156 patients, 63 with LEMS and 93 without", "60% cutoff ... 77.8%", "58.7% ... for 100%", "Specificity was 98.9% ... and 100%"],
 "S6": ["65 patients with NT-LEMS", "median survival 17 vs 7.0 months", "39 (62%) of 63 ... 85% at the 1-year", "physical HRQOL composite score (55.9) ... (76.3"],
 "S7": ["70 LEMS patients ... 1992 and 2023", "Sixty-six percent ... female", "median age of diagnosis was 54 years", "non-tumor LEMS ... (77%)", "91% initiated it within six months", "leg scores in 57%", "58% of patients reported side effects", "discontinuation was rare (7%)",
        "Pyridostigmine was used in 81%", "reaching 44% after five years", "azathioprine, prednisolone and pyridostigmine were discontinued by 50%, 38% and 32%", "Prednisolone ... discontinued in 38% ... remission or side effects (both 39%)", "Azathioprine ... 50% ... side effects (80%)", "Pyridostigmine ... 32% ... side effects (50%)"],
 "S8": ["0.3/100,000 population for Lambert-Eaton myasthenic syndrome", "Review of the literature 1990–2023"],
 "S9": ["38 Lambert-Eaton myasthenic syndrome (LEMS) patients", "38% of LEMS patients"],
 "S10": ["Four controlled trials ... 54 participants", "2.44 points (95% confidence interval 3.6 to 1.22)", "between three and eight days", "1.36 mV (95% confidence interval 0.99 to 1.72)", "nine participants", "up to eight weeks"],
 "S11": ["Six randomised controlled trials (RCTs) involving 115 patients", "2.76 points", "1.34 mV"],
 "S12": ["47 cases", "male predominance (66%)", "median age of 7 years", "median creatine phosphokinase (CPK) level was 4986 U/L", "Influenza B ... (63%)", "median hospital stay of 3.2 days (résumé) ; Mean (SD) 3.2 (1.1) (Table 1)", "January 2016 and December 2024"],
 "S13": ["65,818 cases and 42 deaths reported from 41 countries", "European Region accounted for 87% of cases (résumé) ; 86% (56,912) (résultats)", "261 reports", "1986 through 2009"],
 "S14": ["SOX2 antibodies were detectable in 61% of patients with LEMS-SCLC", "specific (>90%)"],
 "S16": ["dose initiale recommandée est de 15 mg", "trois ou quatre fois par jour avec les repas", "paliers de 5 mg tous les 4 à 5 jours, jusqu'à une dose journalière de 60 mg", "Une dose unique ne doit pas dépasser 20 mg",
         "paliers de 5 mg tous les 7 jours jusqu'à un maximum de 80 mg", "5 mg (un demi-comprimé) une fois par jour", "10 mg (5 mg deux fois par jour)", "demi-vie ... 2,5 heures ... 4 heures", "93,2 % à 100 % ... 24 heures", "Comprimé à 10 mg ... sécable", "Janvier 2022"],
 "S17": ["valeurs moyennes de 1,5 heure", "(75 à 81%) sous forme inchangée par voie rénale", "Juin 2020", "1 à 2 mg de sulfate d'atropine"],
 "S20": ["CK level of 6,106 U/L", "7,020 U/L", "50-year-old male"],
 "S21": ["more than 2 months after the initiation"],
 "S22": ["improved over 3 months"],
 "S23": ["20 patients were enrolled"],
 "S24": ["SCLC in 50%-60% of patients", "about 90% of patients"],
 "S25": ["total of 94 papers"],
 "S18": ["Nineteen pediatric LEMS cases"],
}

# Règles SOURCE : (motif de contexte, liste de valeurs acceptées, source, clé de calcul facultative)
R = []
def src(ctx, vals, s, calc_key=None, verdict=None, note=None):
    R.append(dict(ctx=re.compile(ctx, re.I), vals=[float(v) for v in vals], src=s, calc=calc_key, verdict=verdict, note=note))

# Règles spécifiques placées en tête (la première règle qui correspond l’emporte)
src(r"spécificité supérieure à 90|\(spécificité supérieure à 90", [90], "S14")
src(r"amifampridine, 91 % dans les six mois|Tous traités, 91 %|91 % dans les 6 mois", [91, 6], "S7", "amifa_91")
src(r"DELTA-P de 1 donne un risque de 100", [100], "S4", verdict="DISTRACTEUR_VOULU", note="distracteur C du quiz : 100 % est le risque du score 6")
src(r"44 % des patients prenaient", [44, 5], "S7", "is5ans_44")
# Épidémiologie
src(r"pour 100 000|prévalence", [0.3], "S8")
src(r"sur 300", [300], "S3", "pns_1_sur_300")
src(r"1,6 à 8,9", [1.6], "S3")
src(r"1990–2023|1990-2023", [1990], "S8")
src(r"\(44 sur 87\)|44 sur 87|soit 44 sur 87", [51, 44, 87], "S4", "cbpc_51")
src(r"50 à 60", [50], "S24")
src(r"Femmes 66|garçons représentent 66|Garçons 66|garçons 66", [66], "S7/S12")
src(r"70 patients", [70, 1992], "S7")
src(r"Âge médian au diagnostic 54|54 ans", [54], "S7")
src(r"non tumorale 77|forme non tumorale \(77|77 %", [77], "S7", "nt_77")
src(r"auto-immune associée 38|38 patients|38 % des patients|38 % ont une autre", [38], "S9", verdict="INCOHERENT_N", note="38 % de 38 patients n’est pas un entier (14/38 = 36,8 % ; 15/38 = 39,5 %) : dénominateur réel non donné par le résumé")
src(r"19 cas|Nineteen|19 cas recensés", [19], "S18")
src(r"90 %|≈ 90", [90], "S3/S24")
src(r"6 106|6 000", [6106, 6000], "S20")
src(r"47 cas|47 cas de 2016", [47, 2016], "S12")
src(r"âge médian est de 7|âge médian 7", [7], "S12")
src(r"4 986|≈ 5 000", [4986, 5000], "S12")
src(r"63 %|influenza B dans 63|B est retrouvé dans 63", [63], "S12", "influB_63")
src(r"3,2 jours", [3.2], "S12", verdict="DESCRIPTEUR", note="3,2 j est une MOYENNE (Table 1 : mean (SD) 3,2 (1,1)) ; le résumé dit « médiane »")
src(r"65 818|42 décès|261 rapports|41 pays|1986", [65818, 42, 261, 41, 1986], "S13")
src(r"dont 87 %|87 % dans la Région", [87], "S13", "trich_europe")
# Différentiel, électrophysiologie
src(r"20 patients|essai croisé randomisé de 20", [20], "S23")
src(r"94 articles", [94], "S25")
src(r"> 2 mois|plus de deux mois", [2], "S21")
src(r"supérieur à 60|incrément ≥ 60|seuil d’ incrément de 60|seuil de 60|abaisser le seuil à 60|Au moins 60|à 60 %|60 %", [60], "S4/S5")
src(r"156 patients|dont 63", [156, 63], "S5")
src(r"77,8", [77.8], "S5", "sens60")
src(r"98,9", [98.9], "S5", "spec60")
src(r"58,7", [58.7], "S5", "sens100")
src(r"seuil de 100|100 %|ancien seuil de 100", [100], "S5")
# DELTA-P
src(r"au moins 5 %|perte de poids d’au moins 5", [5], "S4")
src(r"au moins 50 ans|50 ans ou plus|d’au moins 50", [50], "S4")
src(r"Risque de CBPC|0 % 18,8|18,8 %", [0, 18.8, 45, 55.5, 85.7, 87.5, 100], "S4")
src(r"82,5", [82.5], "S4")
src(r"84,5", [84.5], "S4")
src(r"25 mois", [25], "S4")
src(r"Répéter à 3 mois|tous les 6 mois pendant 2 ans|une fois à 6 mois|DELTA-P de 3 à 6|DELTA-P de 0 à 1|DELTA-P de 2", [3, 6, 2, 0], "S4")
src(r"dans les 6 mois chez 91|6 mois chez 91|≤ 6 mois|91 %|en ≤ 12 mois|12 mois chez 98|98 %", [6, 91, 12, 98], "S4", "cbpc_91")
src(r"4 à 6 mois", [4, 2], "S3")
src(r"contrôle à 6 mois", [6], "S4")
# PNS-Care
src(r"score d’au moins 8|au moins 8", [8], "S3", "pns_max_sans_cancer")
src(r"= 6 \(probable\)", [6], "S3", "pns_lems_vgcc_sans_cancer")
src(r"18 mois = 9|= 9 \(défini\)", [18, 9], "S3", "pns_cbpc_18mois")
src(r"plus de 2 ans = 5|= 5 \(possible\)", [2, 5], "S3", "pns_sans_cancer_2ans")
# Traitement
src(r"4 essais|54 participants", [4, 54], "S10")
src(r"2,44", [2.44, 95], "S10")
src(r"1,22 à 3,6|1,22–3,6", [1.22], "S10", "cochrane_ic_sym", verdict="ARRONDI", note="borne haute imprimée 3,6 dans la source ; la symétrie de l’IC attend 3,66")
src(r"entre 3 et 8 jours", [3, 8], "S10")
src(r"1,36", [1.36], "S10")
src(r"0,99 à 1,72|0,99–1,72", [0.99], "S10")
src(r"115 patients|six essais|6 essais", [115, 6], "S11")
src(r"2,76|1,34", [2.76, 1.34], "S11")
src(r"91 % dans les six mois|91 % dans les 6 mois", [91, 6], "S7", "amifa_91")
src(r"57 %", [57], "S7", "leg_57")
src(r"58 %", [58], "S7")
src(r"rare \(7 %\)|arrêt chez 7|\(7 %\)|7 %\)", [7], "S7")
src(r"81 %", [81], "S7")
src(r"9 participants|8 semaines", [9, 8], "S10")
src(r"44 % des patients prenaient|44 % des patients|44 %", [44, 5], "S7", "is5ans_44")
src(r"50 % des patients sous azathioprine|Arrêt pour effets indésirables chez 50|50 %", [50], "S7", "aza_arret_EI", verdict="ATTRIBUTION_FAUSSE", note="50 % = arrêts TOUS motifs ; arrêts pour effets indésirables ≈ 40 % (80 % de 50 %)")
src(r"38 % sous prednisolone|Arrêt pour effets indésirables chez 38|38 %", [38], "S7", "pred_arret_EI", verdict="ATTRIBUTION_FAUSSE", note="38 % = arrêts tous motifs ; pour effets indésirables ≈ 15 % (39 % de 38 %)")
src(r"32 % sous pyridostigmine|32 % des patients ont arrêté|32 %", [32], "S7", "pyr_arret_EI", verdict="ATTRIBUTION_FAUSSE", note="32 % = arrêts tous motifs ; pour effets indésirables ≈ 16 % (50 % de 32 %)")
# Pronostic
src(r"65 patients", [65], "S6")
src(r"17 contre 7|médiane de 17", [17, 7.0, 7], "S6", "survie_ratio")
src(r"62 %|85 %", [62, 85], "S6", "adl_62")
src(r"55,9|76,3", [55.9, 76.3], "S6")
# Posologies Firdapse (FI S16)
src(r"15 mg|départ 15|15 mg/jour", [15], "S16", "firdapse_15mg_3prises")
src(r"3 ou 4 prises|en 3 ou 4", [3, 4], "S16", "firdapse_15mg_4prises", verdict="ENONCE_A_PRECISER", note="15 mg en 4 prises = 3,75 mg, non réalisable avec des demi-comprimés de 5 mg : écrire 3 × 5 mg")
src(r"paliers de 5 mg|Paliers de 5 mg|par paliers de 5", [5, 4, 7], "S16", "firdapse_paliers_15_60")
src(r"60 mg", [60], "S16", "firdapse_prises_60")
src(r"80 mg|80 exceptionnellement|\(80 exceptionnellement\)", [80], "S16", "firdapse_prises_80")
src(r"≤ 20 mg|20 mg au plus|limitée à 20", [20], "S16")
src(r"5 mg une fois|5 mg × 2|10 mg/jour|10 mg par jour|5 mg deux fois", [5, 10, 2], "S16", "firdapse_leger_10")
src(r"2,5 heures", [2.5], "S16")
src(r"3-N-acétylé|4 heures", [3, 4], "S16")
src(r"93 à 100|24 heures", [93, 24], "S16", "firdapse_urine")
src(r"type 2", [2], "S16")
src(r"1,5 heure", [1.5], "S17")
src(r"75 à 81", [75], "S17")
src(r"SOX2.*61|61 %", [61], "S14")
src(r"supérieure à 90|> 90", [90], "S14")
src(r"0 → 0 %, 6 → 100|DELTA-P : 0|DELTA-P de 0 à 6|0 % à 100", [0, 6, 100], "S4")
src(r"10 %", [10], "S4", note="absent chez environ 10 % : complément de « près de 90 % » (100 − 90)")

NON_GRANDEUR = [
    (r"^ch-G73$", "en-tête (date de version, numéro de cycle)"),
    (r"glossaire", "index de lettres ou rang d’isoforme dans les clés du glossaire"),
]

def classify(o):
    v, u, c, a = o["valeur"], o["unite"], o["contexte"], o["ancre"]
    if any(re.search(p, a) for p, _ in NON_GRANDEUR[:1]):
        return ("NON_GRANDEUR", NON_GRANDEUR[0][1])
    if a == "glossaire" and not u:
        return ("NON_GRANDEUR", NON_GRANDEUR[1][1])
    head = c[:40]
    try:
        x = num(v.split(" à ")[0].split("–")[0])
    except ValueError:
        x = None
    if not u and x is not None:
        if re.search(r"\(\d\)", c[max(0, c.find(v) - 3): c.find(v) + len(v) + 3]):
            return ("NON_GRANDEUR", "numérotation de liste (1)…(4)")
        if re.match(r"^\d+$", v) and re.search(rf"(?:^|\s){re.escape(v)}\.\d", c):
            return ("NON_GRANDEUR", "numéro de sous-partie (10.1, 12.2…)")
        if re.search(r"3,4-diaminopyridine|3,4-dia", c) and v == "3,4":
            return ("NON_GRANDEUR", "nom chimique")
        if o.get("premier_de_l_ancre") and re.fullmatch(r"g73-(\d+)", a) and v == a.split("-")[1]:
            return ("NON_GRANDEUR", "numéro d’îlot (titre h2)")
        if re.search(r"\(" + re.escape(v) + r"\)", c) and a == "g73-11":
            return ("NON_GRANDEUR", "numérotation de liste (1)…(4)")
        if re.search(r"\d+\." + re.escape(v) + r"(?:\s|\))", c) or re.search(re.escape(v) + r"\d\.\d", c):
            return ("NON_GRANDEUR", "numéro de sous-partie (10.1, 12.2…) ou renvoi de chapitre")
        if re.search(r"Score Risque de CBPC 0 0 %", c) and x in (1, 2, 3, 4, 5):
            return ("SOURCE_INDEX", "rang du score DELTA-P (tableau de la fenêtre)")
        if re.search(r"Score DELTA-P 0 1 2 3 4 5 6", c) and x in (1, 2, 3, 4, 5, 6):
            return ("SOURCE_INDEX", "rang du score DELTA-P (en-tête du tableau)")
        if re.search(r"neurofibromatose de type 2|isoforme", c) and x == 2:
            return ("NON_GRANDEUR", "nom de maladie")
        if re.search(r"3-N-acétylé", c) and x == 3:
            return ("NON_GRANDEUR", "nom de métabolite")
    return None

def verify(o):
    k = classify(o)
    if k and k[0] == "NON_GRANDEUR":
        return dict(verdict="NON_GRANDEUR", formule=k[1], source=None, attendu=None, trouve=o["valeur"], ecart=None)
    v = o["valeur"]
    vals = [x for x in re.findall(r"\d+(?:[ ,]\d+)?", v.replace(" ", " "))]
    try:
        x = num(re.split(r" à |–", v)[0])
    except ValueError:
        x = None
    if v.strip() == "6 100":   # « 6 | 100 % » du tableau DELTA-P fusionné par l’inventaire
        x = 100.0
    for r in R:
        if r["verdict"] == "ENONCE_A_PRECISER" and " à " in v:
            continue
        if r["ctx"].search(o["contexte"]) and x is not None and any(abs(abs(x) - val) < 1e-9 for val in r["vals"]):
            out = dict(source=r["src"], trouve=v, attendu=x, ecart=0.0, verdict="CORRECT", formule="valeur comparée à la source lue")
            if r["calc"]:
                cdef = CALCS[r["calc"]]
                out["formule"] = cdef["formule"]
                out["attendu"] = round(cdef["attendu"], 3)
                # écart calculé seulement si la grandeur du texte est la grandeur recalculée
                key = r["calc"]
                if key == "cbpc_91" and x == 98:
                    cdef = CALCS["cbpc_98"]; out["formule"] = cdef["formule"]; out["attendu"] = round(cdef["attendu"], 3)
                if o["unite"] == "%" and key in ("sens60", "spec60", "sens100", "cbpc_51", "nt_77", "amifa_91", "leg_57", "is5ans_44", "adl_62", "influB_63", "trich_europe", "cbpc_91") and abs(x - cdef["attendu"]) < 15:
                    out["ecart"] = round(x - cdef["attendu"], 3)
                    out["verdict"] = "CORRECT" if abs(out["ecart"]) <= cdef["tol"] else ("ARRONDI_SOURCE" if abs(out["ecart"]) <= 1.0 else "INCOHERENT_N_SOURCE")
                    if out["verdict"] != "CORRECT":
                        out["note"] = "valeur identique à la source ; le pourcentage imprimé par la source ne correspond pas exactement à son n/N"
            if r["verdict"]:
                out["verdict"] = r["verdict"]
            if r["note"]:
                out["note"] = r["note"]
            return out
    if k and k[0] == "SOURCE_INDEX":
        return dict(verdict="CORRECT", formule=k[1], source="S4", attendu=x, trouve=v, ecart=0.0)
    # calculs explicites des exemples d’incrément (valeurs des énoncés et résultats)
    c = o["contexte"]
    if re.search(r"\(3,6 − 2,0\)|3,6 mV|2,0 mV|Repos 2,0", c) and x in (2.0, 3.6, 100, 80, -2.0):
        cd = CALCS["incr_2.0_3.6"]; return dict(verdict="CORRECT", formule=cd["formule"], source=cd["source"], attendu=round(cd["attendu"], 3), trouve=v, ecart=round((80 - cd["attendu"]), 3) if x == 80 else 0.0)
    if re.search(r"\(2,7 − 1,5\)|1,5 mV|2,7 mV", c) and x in (1.5, 2.7, 100, 80, -1.5, 60, 12, 180):
        key = {12: "incr_distracteur_12", 180: "incr_distracteur_180"}.get(x, "incr_1.5_2.7"); cd = CALCS[key]
        verdict = "CORRECT" if key == "incr_1.5_2.7" else "DISTRACTEUR_VOULU"
        return dict(verdict=verdict, formule=cd["formule"], source=cd["source"], attendu=round(cd["attendu"], 3), trouve=v, ecart=round(x - cd["attendu"], 3) if x in (80, 12, 180) else 0.0)
    if re.search(r"\(4,5 − 2,5\)|A0 = 2,5|2,5 mV|4,5 mV|2,0 ÷ 2,5", c) and x in (2.5, 4.5, 100, 80, -2.5, 2.0):
        cd = CALCS["incr_2.5_4.5"]; return dict(verdict="CORRECT", formule=cd["formule"], source=cd["source"], attendu=round(cd["attendu"], 3), trouve=v, ecart=round(80 - cd["attendu"], 3) if x == 80 else 0.0)
    if re.search(r"environ 41 %|41 % des malades", c) and x == 41:
        cd = CALCS["echappent_41"]; return dict(verdict="CORRECT", formule=cd["formule"], source=cd["source"], attendu=round(cd["attendu"], 3), trouve=v, ecart=round(41 - cd["attendu"], 3))
    if re.search(r"A1 − A0|\(A1", c) and x == 100:
        return dict(verdict="CORRECT", formule="facteur 100 de la formule de l’incrément", source="S5", attendu=100, trouve=v, ecart=0.0)
    if o["ancre"] == "g73-e-2" and re.search(r"L’incrément est de (12|80|180) %", c) and x in (12, 80, 180):
        key = {12: "incr_distracteur_12", 180: "incr_distracteur_180", 80: "incr_1.5_2.7"}[x]; cd = CALCS[key]
        return dict(verdict="CORRECT" if x == 80 else "DISTRACTEUR_VOULU", formule=cd["formule"], source=cd["source"], attendu=round(CALCS["incr_1.5_2.7"]["attendu"], 3), trouve=v, ecart=round(x - CALCS["incr_1.5_2.7"]["attendu"], 3))
    if re.search(r"61 ans|58 ans", c):
        return dict(verdict="NON_VERIFIABLE", formule="âge d’une vignette fictive : DELTA-P incalculable exactement (items bulbaire, dysfonction érectile et Karnofsky non renseignés) ; score ≥ 3 avec âge, tabac et perte de poids", source="S4", attendu=">= 3", trouve=v, ecart=None)
    if re.search(r"perdu 6 %", c) and x == 6:
        return dict(verdict="CORRECT", formule="6 % ≥ 5 % : item « perte de poids » du DELTA-P coté 1", source="S4", attendu=">= 5", trouve=v, ecart=None)
    if re.search(r"DELTA-P est de 1|DELTA-P de 1|DELTA-P 1|score de 1|à score 1", c) and x == 1:
        return dict(verdict="CORRECT", formule="score DELTA-P 1 → risque 18,8 % ; calendrier 0–1", source="S4", attendu=1, trouve=v, ecart=0.0)
    if re.search(r"Réponse B|donne un risque de 100", c) and x == 100:
        return dict(verdict="DISTRACTEUR_VOULU", formule="distracteur C : 100 % correspond au score 6, pas au score 1", source="S4", attendu=18.8, trouve=v, ecart=None)
    return dict(verdict="NON_RATTACHEE", formule=None, source=None, attendu=None, trouve=v, ecart=None)

def main():
    res, cnt, vues = [], {}, set()
    for o in INV["occurrences"]:
        o["premier_de_l_ancre"] = (o["fichier"], o["ancre"]) not in vues
        vues.add((o["fichier"], o["ancre"]))
        r = verify(o); r = {"id": o["id"], "fichier": o["fichier"], "ancre": o["ancre"], **r}
        res.append(r); cnt[r["verdict"]] = cnt.get(r["verdict"], 0) + 1
    extra = []
    for k, cd in CALCS.items():
        extra.append({"id": "C-" + k, "attendu": round(cd["attendu"], 4), "formule": cd["formule"], "source": cd["source"], "tolerance": cd["tol"]})
    grandeurs = [r for r in res if r["verdict"] != "NON_GRANDEUR"]
    synth = {
        "total_releves": len(res),
        "non_grandeurs": cnt.get("NON_GRANDEUR", 0),
        "calculables": len(grandeurs),
        "recalcules": sum(1 for r in grandeurs if r["verdict"] != "NON_RATTACHEE"),
        "par_verdict": cnt,
        "calculs_derives": len(extra),
    }
    synth["correct"] = cnt.get("CORRECT", 0) + cnt.get("DISTRACTEUR_VOULU", 0)
    synth["arrondi"] = cnt.get("ARRONDI", 0) + cnt.get("ARRONDI_SOURCE", 0)
    synth["faux"] = cnt.get("ATTRIBUTION_FAUSSE", 0) + cnt.get("DESCRIPTEUR", 0) + cnt.get("FAUX", 0)
    synth["non_verifiables"] = (cnt.get("NON_VERIFIABLE", 0) + cnt.get("INCOHERENT_N", 0) + cnt.get("INCOHERENT_N_SOURCE", 0)
                                + cnt.get("ENONCE_A_PRECISER", 0))
    synth["non_rattachees"] = cnt.get("NON_RATTACHEE", 0)
    synth["regle_de_cloture"] = "calculables = correct + arrondi + faux + non_verifiables ; non_rattachees doit valoir 0"
    assert synth["calculables"] == synth["correct"] + synth["arrondi"] + synth["faux"] + synth["non_verifiables"] + synth["non_rattachees"]
    prop = []
    for lab, ecrit, calcule, tol, srcx in PROP:
        e = round(ecrit - calcule, 4)
        prop.append({"id": "P-" + str(len(prop) + 1), "libelle": lab, "trouve": ecrit, "attendu": round(calcule, 4), "ecart": e,
                     "verdict": "CORRECT" if abs(e) <= tol else "FAUX", "tolerance": tol, "source": srcx})
    synth["propositions_verifiees"] = len(prop)
    synth["propositions_fausses"] = sum(1 for x in prop if x["verdict"] == "FAUX")
    out = {"synthese": synth, "calculs_derives": extra, "propositions": prop, "resultats": res}
    (HERE / "resultats.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps(synth, ensure_ascii=False, indent=1))
    for r in res:
        if r["verdict"] in ("NON_RATTACHEE", "FAUX", "ATTRIBUTION_FAUSSE", "INCOHERENT_N", "DESCRIPTEUR", "ENONCE_A_PRECISER", "ARRONDI", "ARRONDI_SOURCE", "INCOHERENT_N_SOURCE"):
            o = next(x for x in INV["occurrences"] if x["id"] == r["id"])
            print(r["verdict"], r["id"], r["ancre"], r["trouve"], "|", o["contexte"][40:130])

if __name__ == "__main__":
    main()
