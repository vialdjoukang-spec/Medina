#!/usr/bin/env python3
"""Recalcul scripté des valeurs de la leçon G83 (EXIGENCE_CALCULS § 2).

Entrée : calculs/inventaire.json (produit par calculs/inventaire.py).
Sortie : calculs/resultats.json.

Principe : chaque fait vérifiable (F01…) porte la valeur de la source primaire lue (sources.json),
une formule de recalcul quand une grandeur dérive d'autres grandeurs (tableau 2 × 2, somme, rapport,
différence, posologie), une tolérance d'arrondi explicite et un verdict. Chaque occurrence calculable
de l'inventaire est rattachée à un fait par sa valeur et un motif de contexte ; toute occurrence non
rattachée est signalée (« non_rattachees ») et empêche la clôture de l'audit.

Usage : python3 calculs/verifier.py
"""
import json
import re
from fractions import Fraction
from pathlib import Path

ICI = Path(__file__).resolve().parent
TOL_POURCENT = 0.05  # demi-unité du dernier chiffre publié (une décimale)


def num(s):
    return float(str(s).replace(" ", "").replace(" ", "").replace(" ", "").replace(",", "."))


def proche(a, b, tol):
    return abs(a - b) <= tol + 1e-12


# ---------------------------------------------------------------------------
# Recalculs à partir des données des énoncés et des sources
# ---------------------------------------------------------------------------
R = {}

# F01 — vignette : résidu 350 mL contre seuil 200 mL [S10]
R["F01"] = {"formule": "350 − 200", "attendu": 150, "trouve": 350 - 200, "positif": 350 >= 200}

# F02 — 16 études sur 110 [S13]
R["F02"] = {"formule": "16 / 110 × 100", "trouve": round(16 / 110 * 100, 3)}

# F06 — 0,04 % de 10 000 lombalgiques [S3]
R["F06"] = {"formule": "0,04 / 100 × 10 000", "trouve": round(0.04 / 100 * 10000, 6)}


# F11/F12 — reconstruction du tableau 2 × 2 de Katzouraki 2020 (N = 260) [S10]
def deux_x_deux(N, Se, Sp, VPP, VPN):
    """Cherche les effectifs entiers (VP, FN, FP, VN) qui redonnent les quatre indices publiés à 0,05 % près."""
    sol = []
    for D in range(1, N):
        nd = N - D
        for VP in range(0, D + 1):
            if not proche(100 * VP / D, Se, TOL_POURCENT):
                continue
            for VN in range(0, nd + 1):
                if not proche(100 * VN / nd, Sp, TOL_POURCENT):
                    continue
                FP, FN = nd - VN, D - VP
                if VP + FP == 0 or VN + FN == 0:
                    continue
                if proche(100 * VP / (VP + FP), VPP, TOL_POURCENT) and proche(100 * VN / (VN + FN), VPN, TOL_POURCENT):
                    sol.append({"malades": D, "VP": VP, "FN": FN, "FP": FP, "VN": VN})
    return sol


pvr = deux_x_deux(260, 94.1, 66.8, 29.9, 98.7)
R["F12"] = {"formule": "recherche entière du tableau 2 × 2 (N = 260) compatible avec Se 94,1 %, Sp 66,8 %, VPP 29,9 %, VPN 98,7 %",
            "solutions": pvr}
if pvr:
    s = pvr[0]
    p = s["malades"] / 260
    Se, Sp = 0.941, 0.668
    vpn_recalc = Sp * (1 - p) / (Sp * (1 - p) + (1 - Se) * p)
    R["F12"].update({"prevalence_pourcent": round(100 * p, 2), "VPN_recalculee_pourcent": round(100 * vpn_recalc, 2),
                     "non_malades_parmi_positifs_pourcent": round(100 * s["FP"] / (s["VP"] + s["FP"]), 2)})

# Sciatique bilatérale : même échantillon (malades = 34 si F12 unique)
sci = []
if pvr:
    D = pvr[0]["malades"]
    nd = 260 - D
    for VP in range(D + 1):
        if not proche(100 * VP / D, 32.4, TOL_POURCENT):
            continue
        for FP in range(nd + 1):
            if VP + FP == 0:
                continue
            VN, FN = nd - FP, D - VP
            if proche(100 * VP / (VP + FP), 17.2, TOL_POURCENT) and proche(100 * VN / (VN + FN), 88.3, TOL_POURCENT):
                sci.append({"VP": VP, "FN": FN, "FP": FP, "VN": VN, "Sp_deduite_pourcent": round(100 * VN / nd, 1)})
R["F11"] = {"formule": "tableau 2 × 2 de la sciatique bilatérale dans le même échantillon (N = 260, malades = %s)" % (pvr[0]["malades"] if pvr else "?"),
            "solutions": sci}

# F13 — « plus de deux patients sur trois » positifs sans syndrome (VPP 29,9 %)
R["F13"] = {"formule": "1 − 0,299 comparé à 2/3", "trouve": round(1 - 0.299, 3), "seuil": round(2 / 3, 3)}

# F14 — Boktor 2023 : prévalence 125/734 ; Se 82 % → faux négatifs 18 % ; Sp 65 % hors IC 0,70–0,90 [S11]
R["F14"] = {"formule": "125/734 ; 1 − 0,82 ; 0,65 ∈ [0,70 ; 0,90] ?", "prevalence_pourcent": round(125 / 734 * 100, 1),
            "faux_negatifs_pourcent": round(100 - 82, 1), "un_sur": round(1 / 0.18, 2), "Sp_dans_IC": 0.70 <= 0.65 <= 0.90}

# F20 — Kumar : rapport 50,3/24,6 [S4]
R["F20"] = {"formule": "50,3 / 24,6", "trouve": round(50.3 / 24.6, 3)}

# F23 — retards : 4 + 20 = 24 ; 7 + 8 + 5 = 20 [S3]
R["F23"] = {"formule": "4 + 20 ; 7 + 8 + 5", "trouve": [4 + 20, 7 + 8 + 5]}

# F25 — série de 1986 [S17] : sommes internes
R["F25"] = {"formule": "85 + 52 ; 89 + 46 + 3 ; comparés à 139", "trouve": [85 + 52, 89 + 46 + 3],
            "source": "S17 : 85 hommes, 52 femmes ; 89 classiques, 46 incomplets, 3 complets et 1 non classé"}

# F32 — Stroke Mimics Score : 3266/6998 [S20]
R["F32"] = {"formule": "3266 / 6998 × 100", "trouve": round(3266 / 6998 * 100, 2)}

# F33 — Klimbytė : 37/330 [S21]
R["F33"] = {"formule": "37 / 330 × 100", "trouve": round(37 / 330 * 100, 2)}

# F35 — baclofène intrathécal : schéma de test [S22]
serie = [25, 50, 75]
R["F35"] = {"formule": "paliers successifs de 25 µg ; (n doses − 1) × 24 h ; plafond de test 100 µg (FI)",
            "paliers_ok": all(b - a == 25 for a, b in zip(serie, serie[1:])), "doses": len(serie), "increments": len(serie) - 1,
            "delai_min_h": (len(serie) - 1) * 24, "sous_plafond_100": max(serie) <= 100,
            "series_maximales_FI": {"depart_25": [25, 50, 75, 100], "delai_25_h": 72, "depart_50": [50, 75, 100], "delai_50_h": 48}}

# F04 — kappa : définition κ = (po − pe)/(1 − pe) ; bornes
def kappa(po, pe):
    return (po - pe) / (1 - pe)
R["F04"] = {"formule": "κ = (po − pe) / (1 − pe)", "accord_parfait": kappa(1.0, 0.4), "accord_du_hasard": kappa(0.4, 0.4),
            "bande_McHugh_0_34": "0,21–0,39 = minimal (le résumé S12 dit « minimal agreement »)",
            "IC_publie_0_27_0_31_contient_0_34": 0.27 <= 0.34 <= 0.31}

# F08 — plausibilité bayésienne de « 1 sur 10 000 » [S3] avec p = 0,04 % (S3), Se = 90 %, Sp hypothétique 0,90–1,00
plaus = {}
for sp in (0.90, 0.95, 1.0):
    pr = 0.0004
    p_abs = (1 - 0.90) * pr / ((1 - 0.90) * pr + sp * (1 - pr))
    plaus["Sp=%.2f" % sp] = "1 sur %d" % round(1 / p_abs)
R["F08"] = {"formule": "P(CES | pas de rétention) = (1 − Se)·p / [(1 − Se)·p + Sp·(1 − p)]", "plausibilite": plaus,
            "lecture": "même ordre de grandeur (10⁻⁴ à 10⁻⁵) ; la spécificité de la rétention n'est pas donnée par S3 : valeur reprise de la source, non recalculable exactement"}

# Enrichissements proposés (contrôle des chiffres que l'audit ajoute)
R["E01"] = {"formule": "44 / 328 × 100 (Gallmetzer 2004, S30)", "trouve": round(44 / 328 * 100, 2)}
R["E02"] = {"formule": "117 / 1005 × 100 (Curtis Lopez 2024, S33)", "trouve": round(117 / 1005 * 100, 2)}
R["E03"] = {"formule": "altéplase 0,9 mg/kg (max 90 mg), 10 % en bolus, reste en 60 min — exemple 70 kg (FI Actilyse, S27)",
            "dose_totale_mg": round(0.9 * 70, 1), "bolus_mg": round(0.09 * 70, 2), "perfusion_mg": round(0.9 * 70 - 0.09 * 70, 2),
            "table_FI_70kg": [63.0, 6.3, 56.7], "plafond_100kg": min(0.9 * 110, 90)}
R["E04"] = {"formule": "dose initiale de perfusion = 2 × dose test efficace sur 24 h, sauf effet > 12 h (FI Liorésal, S22) — exemple dose test efficace 50 µg",
            "dose_initiale_ug_24h": 2 * 50, "debit_ug_h": round(2 * 50 / 24, 2)}
R["E05"] = {"formule": "ténectéplase : bandes de poids de la FI Metalyse 5000 (S28)",
            "bandes": {"<60": 15, "60-<70": 17.5, "70-<80": 20, "80-<90": 22.5, ">=90": 25}, "plafond_mg": 25}

R["E06"] = {"formule": "sciatique bilatérale (F11) : FP/(VP+FP) ; FN/malades ; RPM : FP/(VP+FP)",
            "non_malades_parmi_sciatiques_pourcent": round(53 / 64 * 100, 1), "malades_sans_sciatique_pourcent": round(23 / 34 * 100, 1),
            "non_malades_parmi_RPM_positifs_pourcent": round(75 / 107 * 100, 1)}
R["E07"] = {"formule": "1 − AUC (S20)", "trouve": round(1 - 0.777, 3)}
R["E08"] = {"formule": "1 / prévalence des compressions parmi les suspicions (S33, S10, S11)",
            "un_sur": [round(1005 / 117, 1), round(260 / 34, 1), round(734 / 125, 1)]}
_tableau = {40: (36.0, 3.6, 32.4), 50: (45.0, 4.5, 40.5), 70: (63.0, 6.3, 56.7), 90: (81.0, 8.1, 72.9), 100: (90.0, 9.0, 81.0)}
R["E09"] = {"formule": "contrôle de la table FI Actilyse : total = min(0,9 × poids ; 90) ; bolus = 10 % ; perfusion = reste (S27)",
            "ecarts_mg": {k: [round(min(0.9 * k, 90) - v[0], 2), round(min(0.9 * k, 90) * 0.1 - v[1], 2), round(min(0.9 * k, 90) * 0.9 - v[2], 2)] for k, v in _tableau.items()}}

# ---------------------------------------------------------------------------
# Faits : valeurs de la source, motifs de rattachement, verdict
# ---------------------------------------------------------------------------
def F(fid, valeurs, motif, source, verdict, note, formule="lecture directe de la source", fichier=None, ancre=None, vctx=()):
    return {"fid": fid, "valeurs": [num(v) if not isinstance(v, str) or re.match(r"^[\d ,. ]+$", v) else v for v in valeurs],
            "motif": motif, "source": source, "verdict": verdict, "note": note, "formule": formule, "fichier": fichier, "ancre": ancre,
            "vctx": list(vctx)}


s12 = R["F12"]
FAITS = [
    F("F01", [350, 200, 150], r"350|seuil|résidu|vignette", "S10", "CORRECT",
      "350 − 200 = 150 mL ; 350 ≥ 200 : test positif.", R["F01"]["formule"]),
    F("F02", [110, 52008, 16, 14.5], r"110|52\s?008|16|14,5", "S13", "CORRECT",
      "16/110 = %.3f %% publié 14,5 %% (arrondi correct)." % R["F02"]["trouve"], R["F02"]["formule"],
      vctx=[(r"^14,5$", r"", "ARRONDI")]),
    F("F03", [212, 17], r"212|17 définitions|définitions", "S5", "CORRECT",
      "Valeurs exactes ; mais S5 attribue les 17 définitions à Fraser et les 212 articles à la revue de Lavy (attribution fusionnée : constat C11)."),
    F("F04", [0.34, 0.17, 1, 0, 100], r"kappa|consultants|accord|hasard|vignettes", "S12", "CORRECT",
      "Valeurs exactes (S12). Bornes de κ vérifiées par la définition. Réserve : 0,17 est l'accord des consultants toutes catégories confondues, non sur la question « rétention contre autres » ; l'IC publié 0,27–0,31 n'inclut pas 0,34 (erreur de la source). « 0,34 proche du hasard » est une interprétation forcée (constat C12).",
      R["F04"]["formule"], vctx=[(r"^0,34$", r"proches de l", "ARRONDI")]),
    F("F05", [0.34, 7, 100000], r"100 000|pour 100", "S9", "CORRECT", "0,34 à 7 pour 100 000 par an (S9, résumé)."),
    F("F06", [0.04, 4, 10000], r"0,04|4 patients|lombalgiques", "S3", "CORRECT",
      "0,04 %% × 10 000 = %s." % R["F06"]["trouve"], R["F06"]["formule"]),
    F("F07", [2], r"hernies|^Environ 2 %$", "S4", "CORRECT", "« approximately 2% of cases of lumbar disc herniation » (S4)."),
    F("F08", [90, 1, 10000], r"rétention|Rétention|sensibilité est d’environ 90|sensibilité d’environ 90|sensibilité environ 90|1 sur 10", "S3", "CORRECT",
      "Valeurs de S3 (« sensibilité de près de 90 %% » ; « 1 sur 10 000 »). Plausibilité bayésienne : %s." % R["F08"]["plausibilite"], R["F08"]["formule"]),
    F("F09", [44, 24, 89], r"44|moins de 24 heures chez|moins de 24 heures dans|89 %", "S3", "CORRECT",
      "« revue de 44 patients … moins de 24 heures pour 89 % » (S3, réf. 26 de l'article ; série non suisse)."),
    F("F10", [9, 8, 5, 4, "neuf recommandations"], r"recommandations|^\d$|dans [45]|8 des 9", "S6", "CORRECT",
      "9 recommandations ; 8/9 douleur radiculaire, 5/9 faiblesse, 4/9 toucher rectal, 5/9 résidu (S6).", ancre=r"g83-5|g83-drapeaux"),
    F("F11", [32.4, 17.2, 88.3, 260], r"sciatique|suspicions|32,4|17,2|88,3", "S10", "CORRECT",
      "Tableau 2 × 2 reconstruit : %s." % R["F11"]["solutions"], R["F11"]["formule"]),
    F("F12", [200, 94.1, 66.8, 29.9, 98.7, 260, 13, "Treize pour cent"], r"résidu|200 mL|94,1|66,8|29,9|98,7|260|13 %|Treize|bas risque|fréquence|seuil|mesure",
      "S10", "CORRECT",
      "Tableau 2 × 2 unique : %s ; prévalence %s %% (« autour de 13 %% ») ; VPN recalculée %s %%. « Treize pour cent » (bas risque) est une autre grandeur de S10, égale par coïncidence." % (
          s12.get("solutions"), s12.get("prevalence_pourcent"), s12.get("VPN_recalculee_pourcent")), R["F12"]["formule"]),
    F("F13", ["deux patients"], r"deux patients sur trois", "S10", "CORRECT",
      "1 − 0,299 = %.3f > 2/3 = %.3f." % (R["F13"]["trouve"], R["F13"]["seuil"]), R["F13"]["formule"]),
    F("F14", [7, "sept études", 734, 125, 200, 82, 65, "un malade"], r"méta-analyse|7 études|sept études|734|125|82|65|meilleur seuil|un malade sur cinq|ponctuelle",
      "S11", "CORRECT",
      "Valeurs exactes (S11). Prévalence 125/734 = %s %% ; IC de Sp 0,70–0,90 n'inclut pas 0,65 : %s → incohérence de la source confirmée. « Un malade sur cinq » : 18 %% = 1 sur %s (arrondi acceptable)." % (
          R["F14"]["prevalence_pourcent"], not R["F14"]["Sp_dans_IC"], R["F14"]["un_sur"]), R["F14"]["formule"],
      vctx=[(r"(?i)^un malade$", r"", "ARRONDI")]),
    F("F15", ["dans l’heure"], r"BASS|britannique|heure", "S25", "CORRECT",
      "« within 1 hour of presentation to the emergency department » (S25). Le parcours GIRFT actuel (S32, 2026) fixe ≤ 4 h après la demande : constat C09."),
    F("F16", [24], r"24 heures sur 24|disponible 24", "S7", "CORRECT", "« aim for 24-hour MRI local diagnostic capabilities » (S7)."),
    F("F17", [24, 48], r"Allemagne|absolue|au plus tard|Décompression urgente : 24|attendre jusqu’à 48", "S4", "CORRECT",
      "« immediate surgery (i.e., within 24–48 hours) » (S4). « au plus tard 48 heures » : formulation du cours, cohérente avec S8 ; voir C10."),
    F("F18", [24], r"en général dans les 24|faite dans les 24|urgente, en général", "S7", "CORRECT", "« usually within 24 hours » (S7)."),
    F("F19", [322, 48, 24, 2.5, 9.1, 3.5], r"322|Ahn|significatif|différence entre moins de 24|avant 24 h|délai court|plus de 48 h|^\d,\d$|48 h ou moins|opérer dans les 48|opérés d’un|lieu en 48|pour l’incontinence|pour le déficit|pour la dysfonction|après 48 heures\. L’association", "S23/S4", "CORRECT",
      "322 patients ; ≤ 48 h contre > 48 h ; pas de différence < 24 h contre 24–48 h (S23) ; OR 2,5 / 9,1 / 9,1 / 3,5 (S4, eTable).", ancre=r"g83-7|g83-ahn|g83-kumar|g83-meta2026"),
    F("F20", [22, 852, 1, 24.6, 50.3, 48], r"22 études|852|24,6|50,3|1 an|double|incontinence résiduelle|Incontinence résiduelle|Décompression en 48", "S4", "CORRECT",
      "Valeurs de S4 ; 50,3/24,6 = %.3f (« double environ » exact)." % R["F20"]["trouve"], R["F20"]["formule"]),
    F("F21", [15, "Quinze études", 26627, 48, 2.3, 24, 12], r"15 études|Quinze|26 627|2,3|12 mois|constant de moins de 24|24 heures contre 24 à 48|par rapport à 24 à 48|accrues au-delà|dégénératif", "S8", "CORRECT",
      "Valeurs du résumé S8."),
    F("F22", [1.77, 2.19], r"1,77|2,19", "S24", "CORRECT", "RR 1,77–2,19 pour « Fair/Poor » sur 5 seuils ; significatif à 24 h et 72 h seulement (S24)."),
    F("F23", [24, 48, 4, 20, 7, 8, 5], r"patients opérés|imputable|médecin dans|diagnostic 7|diagnostiques 8|chirurgical 5|8 cas", "S3", "CORRECT",
      "4 + 20 = %d ; 7 + 8 + 5 = %d. Valeurs exactes ; G83_c qualifie à tort la série de « suisse » (réf. 26 de S3) : constat C15." % tuple(R["F23"]["trouve"]),
      R["F23"]["formule"]),
    F("F24", [43, 31, 53, 38, 40, 70, 60, "deux études"], r"43|rectale|sensitif|moteur|sexuelle|Kumar\)|hommes et 60|Sangondimath|deux études|^\d\d %$", "S4", "CORRECT",
      "Valeurs exactes ; S4 les rapporte d'après Kumar 2022 (eTable), non comme synthèse propre de Kögl."),
    F("F25", [139, 52, 85, 89, 46, 3, 82, 60, 75, "quatre premiers mois"], r"139|1986|hommes pour|52 femmes|formes classiques|incomplètes|complètes|infarctus pontiques|mortalité atteignait|mortalité était|mortalité 60|75 % en phase|quatre premiers", "S17", "CORRECT",
      "Sommes internes : 85 + 52 = %d ≠ 139 ; 89 + 46 + 3 = %d ≠ 139. S17 précise « 1 non classé » ; le sexe de 2 cas n'est pas donné. Énoncé incomplet : constat C13." % tuple(R["F25"]["trouve"]),
      R["F25"]["formule"], vctx=[(r"^(139|85|89|46|3)$", r"", "NON_VERIFIABLE"), (r"^52$", r"^patients$", "NON_VERIFIABLE", "unite")]),
    F("F26", [0.7, 10000], r"0,7|établissement", "S17", "CORRECT", "« 0.7/10,000 patients with classical LiS in Dutch nursing homes » (S17)."),
    F("F27", [1, 2], r"1 à 2|artère basilaire|accidents vasculaires|des AVC", "S18", "CORRECT", "« 1%–2% of ischaemic stroke » (S18)."),
    F("F28", [24], r"thrombolyse|Jusqu’à 24 heures sauf", "S18/S27/S28", "CORRECT",
      "Exact pour ESO/ESMINT (consensus d'experts, « suggests »). Hors autorisation suisse : Actilyse (FI 06/2025) et Metalyse 5000 (FI 05/2025) limitent l'AVC ischémique à 4,5 h. Constat C02 (MAJEUR)."),
    F("F29", [10], r"NIHSS|en dessous de 10", "S18", "CORRECT", "Seuil NIHSS 10 du résumé S18 (certitude très faible ; ECR : faible)."),
    F("F30", [63, 72, 7, 9, "la moitié", "un mois", "deux mois", "un quart"], r"63|72|7 %|9 %|moitié des patients|un mois|deux mois|quart|délai moyen|heureux|enquête", "S17", "CORRECT",
      "Valeurs de S17 (72 % heureux + 28 % malheureux = 100 %)."),
    F("F31", [78, 45, 31, 24, "deux mois"], r"manifestations|habituellement|postcritiques|78 articles|45 en", "S19", "CORRECT", "Valeurs du résumé S19."),
    F("F32", [46.7, 6998, 10, 0.777, 0.774, 0.77, "la moitié"], r"46,7|6 998|10 variables|0,77|simulateurs|moitié des suspicions", "S20", "CORRECT",
      "3266/6998 = %.2f %% (46,7 %%). AUC 0,777/0,774 exacts ; « discrimination moyenne » : qualification non sourcée, les auteurs écrivent « excellent » (constat C12)." % R["F32"]["trouve"],
      R["F32"]["formule"]),
    F("F33", [330, 11.2], r"330|11,2", "S21", "CORRECT", "37/330 = %.2f %%." % R["F33"]["trouve"], R["F33"]["formule"]),
    F("F35", [25, 50, 24, 4, 8, 75, 48, "trois paliers"], r"µg|paliers|Effet de|tests à|bolus|d’intervalle|soit au moins 48", "S22", "CORRECT",
      "FI Liorésal intrathécal (04/2024) : 25 ou 50 µg, paliers de 25 µg ≥ 24 h, effet 4–8 h, enfant 25 µg. Série 25-50-75 : %d doses, %d intervalles, ≥ %d h ; ≤ 100 µg : %s. Le plafond de test de 100 µg (FI) manque dans la leçon : constat C03." % (
          R["F35"]["doses"], R["F35"]["increments"], R["F35"]["delai_min_h"], R["F35"]["sous_plafond_100"]), R["F35"]["formule"],
      vctx=[(r"(?i)^trois paliers$", r"", "ARRONDI")]),
    F("F36", [46, "trois jours", 52, 18, 120, 60, "une semaine", 5], r"46 ans|52 ans présente|homme de 52|60 ans est|18 heures|120 mL|une semaine|rendez-vous|il y a trois jours", "énoncé", "CORRECT",
      "Cohérence des énoncés : 120 mL < 200 mL (sous le seuil) ; 18 h < 24 h ; âges plausibles ; rendez-vous à trois jours."),
    F("F37", ["deux cas", "un cas", "Deux cas", "deux ans", 2], r"cas suisses|Balgrist|un cas|deux ans|2 ans|Deux cas", "S15", "CORRECT",
      "Deux femmes de 72 ans ; séquelles à 2 ans (S15)."),
]


ORDRE = ["F28", "F35", "F25", "F23", "F36", "F31", "F26", "F27", "F16", "F18", "F15", "F13", "F11", "F12", "F14", "F22", "F32",
         "F33", "F30", "F37", "F10", "F08", "F06", "F05", "F07", "F03", "F02", "F04", "F24", "F20", "F21", "F19", "F17", "F09", "F01", "F29"]


def classer(e):
    """Occurrences calculables : valeurs chiffrées et quantités en lettres, hors formules génériques."""
    if e["nature"] == "valeur":
        if e["fichier"].endswith(".py") and not re.search(r"\d", e["contexte"].split("#")[-1]):
            return False
        if re.search(r"^0?5$", e["valeur"]) and "N-05" in e["contexte"]:
            return False
        return True
    if e["nature"] == "valeur_en_lettres":
        return not re.match(r"(?i)un patient|un patient", e["valeur"])
    return False


def fenetre(e, marge=45):
    """Fenêtre de ± marge caractères autour de l'occurrence (le contexte est centré à 90 caractères)."""
    c, v = e["contexte"], e["valeur"]
    pos = [m.start() for m in re.finditer(re.escape(v), c)]
    if not pos:
        return c
    p = min(pos, key=lambda x: abs(x - min(90, len(c) // 2)))
    return c[max(0, p - marge):p + len(v) + marge]


def rattacher(e):
    v = e["valeur"]
    try:
        vn = num(v)
    except ValueError:
        vn = None
    for f in sorted(FAITS, key=lambda f: ORDRE.index(f["fid"]) if f["fid"] in ORDRE else 99):
        if f["ancre"] and not re.search(f["ancre"], e["ancre"]):
            continue
        ok_val = (vn is not None and any(isinstance(x, float) and abs(x - vn) < 1e-9 for x in f["valeurs"])) or \
                 any(isinstance(x, str) and x.lower() == v.lower() for x in f["valeurs"])
        if ok_val and re.search(f["motif"], fenetre(e), flags=re.I):
            return f
    return None


def main():
    inv = json.loads((ICI / "inventaire.json").read_text(encoding="utf-8"))
    res, non_rattachees = [], []
    for e in inv["occurrences"]:
        if not classer(e):
            continue
        f = rattacher(e)
        if not f:
            non_rattachees.append({"id": e["id"], "fichier": e["fichier"], "valeur": e["valeur"], "contexte": e["contexte"]})
            continue
        verdict = f["verdict"]
        for regle in f["vctx"]:
            rv, rc, vd = regle[:3]
            cible = e["unite"] if len(regle) > 3 else e["contexte"]
            if re.search(rv, e["valeur"]) and re.search(rc, cible):
                verdict = vd
        res.append({"id": e["id"], "fait": f["fid"], "fichier": e["fichier"], "ancre": e["ancre"], "trouve": e["valeur"] + (" " + e["unite"] if e["unite"] and e["unite"] != "en lettres" else ""),
                    "attendu": "valeur de la source %s" % f["source"] if f["formule"] == "lecture directe de la source" else "recalcul : " + f["formule"],
                    "ecart": 0 if verdict == "CORRECT" else ("arrondi ou formulation approchée" if verdict == "ARRONDI" else "voir note"),
                    "verdict": verdict, "formule": f["formule"], "source": f["source"], "note": f["note"]})
    calculables = len(res) + len(non_rattachees)
    compte = {k: sum(1 for r in res if r["verdict"] == k) for k in ("CORRECT", "ARRONDI", "FAUX", "NON_VERIFIABLE")}
    doc = {
        "mission": "ALPHA1-CLAUDE-G83-MED",
        "script": "calculs/verifier.py",
        "tolerance": "± 0,05 point de pourcentage pour les indices publiés à une décimale ; égalité exacte pour les sommes et les doses",
        "total_releves": inv["total"],
        "calculables": calculables,
        "recalcules": len(res),
        "correct": compte["CORRECT"], "arrondi": compte["ARRONDI"], "faux": compte["FAUX"], "non_verifiables": compte["NON_VERIFIABLE"],
        "non_rattachees": non_rattachees,
        "recalculs": R,
        "faits": [{k: f[k] for k in ("fid", "source", "verdict", "formule", "note")} for f in FAITS],
        "resultats": res,
    }
    (ICI / "resultats.json").write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print({k: doc[k] for k in ("total_releves", "calculables", "recalcules", "correct", "arrondi", "faux", "non_verifiables")})
    for n in non_rattachees:
        print("NON RATTACHÉE", n["id"], n["fichier"], n["valeur"], "|", n["contexte"][:140])


if __name__ == "__main__":
    main()
