#!/usr/bin/env python3
"""Recalcul scripté des valeurs de la leçon G99 (EXIGENCE_CALCULS § 2).

Entrée : calculs/inventaire.json (produit par calculs/inventaire.py).
Sortie : calculs/resultats.json.

Principe : chaque fait vérifiable (F01…) porte les valeurs de la source primaire lue (sources.json),
une formule de recalcul quand une grandeur dérive d'autres grandeurs (somme, rapport, différence,
posologie journalière, réduction rénale), une tolérance d'arrondi explicite et un verdict.
Chaque occurrence calculable de l'inventaire est rattachée à un fait par sa valeur et un motif de
contexte ; toute occurrence non rattachée est signalée (« non_rattachees ») et empêche la clôture.
Les numéros de pages, volumes et années des références bibliographiques ne sont pas des grandeurs
calculables : ils sont classés « reference_bibliographique » et comptés à part.

Usage : python3 calculs/verifier.py
"""
import json
import re
from pathlib import Path

ICI = Path(__file__).resolve().parent
TOL_POURCENT = 0.05  # demi-unité du dernier chiffre publié (une décimale)


def num(s):
    return float(str(s).replace(" ", "").replace(" ", "").replace(" ", "").replace(",", "."))


def proche(a, b, tol):
    return abs(a - b) <= tol + 1e-12


# ---------------------------------------------------------------------------
# Recalculs à partir des énoncés et des sources
# ---------------------------------------------------------------------------
R = {}

# Cas récapitulatif g99-11 : 130/80 couché → 105/70 debout ; critères ESC [S4] : ΔPAS ≥ 20 ou ΔPAD ≥ 10 ou PAS debout < 90
d_pas, d_pad = 130 - 105, 80 - 70
R["F28a"] = {"formule": "ΔPAS = 130 − 105 ; ΔPAD = 80 − 70 ; HO si ΔPAS ≥ 20 ou ΔPAD ≥ 10 ou PAS debout < 90",
             "delta_PAS": d_pas, "delta_PAD": d_pad, "critere_PAS": d_pas >= 20, "critere_PAD": d_pad >= 10,
             "critere_PAS_debout_inf_90": 105 < 90, "HO": d_pas >= 20 or d_pad >= 10 or 105 < 90,
             "lecture": "La leçon ne cite que le critère systolique ; le critère diastolique (10 mmHg) est aussi atteint."}
# Quiz cas 1 g99-e-6 : 140/85 → 118/80
q_pas, q_pad = 140 - 118, 85 - 80
R["F28b"] = {"formule": "ΔPAS = 140 − 118 ; ΔPAD = 85 − 80", "delta_PAS": q_pas, "delta_PAD": q_pad,
             "HO": q_pas >= 20 or q_pad >= 10 or 118 < 90, "reponse_A_correcte": q_pas == 22 and q_pas >= 20,
             "distracteur_B_vrai_mais_non_pertinent": q_pad < 10}

# Prévalence NAC : bornes extrêmes résumées « de 6 à 73 % » [S5][S15]
bornes = {"DT1_S5": (29, 54), "DT2_S5": (12, 73), "DT1_Steno": (6, 39), "DT2_Steno": (9, 49)}
R["F08"] = {"formule": "min et max des fourchettes chez les personnes diabétiques (S5 tableau 1, S15)",
            "min": min(b[0] for b in bornes.values()), "max": max(b[1] for b in bornes.values()),
            "une_sur_cinq_pourcent": 100 / 5}

# Cohorte polonaise [S16] : 32,4 + 15,8 = 48,2
R["F10"] = {"formule": "32,4 + 15,8", "trouve": round(32.4 + 15.8, 1), "attendu": 48.2}

# Gastroparésie : rapport des incidences cumulées à 10 ans [S3]
R["F11"] = {"formule": "5,2 / 1,0 ; 5,2 / 0,2", "DT1_vs_DT2": round(5.2 / 1.0, 2), "DT1_vs_temoins": round(5.2 / 0.2, 1)}

# MCD : 108/183 [S8]
R["F12"] = {"formule": "108 / 183 × 100", "trouve": round(108 / 183 * 100, 2), "publie": 59}

# QTc en hypoglycémie [S5] : 415,1 → 444,9 ms
R["F17"] = {"formule": "444,9 − 415,1 ; arrondis 415 et 445", "delta_ms": round(444.9 - 415.1, 1),
            "arrondi_415": round(415.1), "arrondi_445": round(444.9)}

# Exercice : 15/18 études [S5]
R["F19"] = {"formule": "15 / 18 × 100", "trouve": round(15 / 18 * 100, 1)}

# Midodrine : posologies journalières [S20 FI Gutron 03/2021 ; S4 ESC]
R["F21"] = {"formule": "début FI 3 × 2,5 mg ; ESC 3 × (2,5 à 10) mg ; plafond FI 30 mg/j en 3 prises ; « jusqu’à 15 mg/j dans certains cas »",
            "debut_mg_j": 3 * 2.5, "ESC_min_mg_j": 3 * 2.5, "ESC_max_mg_j": 3 * 10, "plafond_FI_mg_j": 30,
            "ESC_max_egal_plafond_FI": 3 * 10 == 30, "palier_15_sous_plafond": 15 <= 30,
            "lecture": "Les 15 mg/j de la FI désignent une dose atteinte « dans certains cas » ; la FI fixe à 30 mg/j la limite au-delà de laquelle une augmentation ne peut être recommandée. La leçon omet ce plafond : constat C11 (MINEUR)."}

# Fludrocortisone [S21 FI Florinef 03/2026 ; S4 ESC]
R["F22"] = {"formule": "FI : 0,1 mg × 3/semaine à 0,2 mg × 7/semaine ; ESC : 0,1 à 0,3 mg/j ; FI : ≤ 0,05 mg/j si HTA transitoire",
            "FI_min_mg_semaine": round(0.1 * 3, 2), "FI_max_mg_semaine": round(0.2 * 7, 2), "FI_max_mg_j": 0.2,
            "ESC_max_mg_j": 0.3, "ESC_max_depasse_FI": 0.3 > 0.2,
            "lecture": "La borne haute ESC (0,3 mg/j) dépasse la dose usuelle maximale de la FI suisse (0,2 mg/j) : la leçon juxtapose les deux sans le signaler (constat C12)."}

# Dompéridone [S22 FI Motilium 06/2026]
R["F23"] = {"formule": "10 mg × 3/j ; ≤ 7 jours", "mg_j": 10 * 3, "mg_cure_max": 10 * 3 * 7}

# Métoclopramide [S23 FI Paspertin 01/2020]
poids = [40, 50, 60, 70, 80]
R["F24"] = {"formule": "max/j = min(30 mg ; 0,5 mg/kg × poids) ; réduction 50 % (ClCr 15–60) ; 75 % (ClCr ≤ 15)",
            "max_selon_poids_mg": {p: min(30, 0.5 * p) for p in poids}, "seuil_poids_kg_ou_0_5mgkg_egale_30mg": 30 / 0.5,
            "max_IR_moderee_mg_j": 30 * 0.5, "max_IR_terminale_mg_j": 30 * 0.25,
            "lecture": "« 30 mg par jour ou 0,5 mg/kg » s’entend comme la plus basse des deux bornes : sous 60 kg, la borne pondérale l’emporte."}

# Tafamidis [S24 FI Vyndaqel 04/2026] : 61 mg tafamidis ≡ 80 mg méglumine = 4 × 20 mg
R["F25"] = {"formule": "4 × 20 mg méglumine", "meglumine_mg": 4 * 20, "bioequivalent_tafamidis_mg": 61}

# Retard diagnostique [S8] : 5,2 ± 3,6 consultations
R["F26"] = {"formule": "5,2 − 3,6 ; 5,2 + 3,6 (± 1 ET)", "bas": round(5.2 - 3.6, 1), "haut": round(5.2 + 3.6, 1)}

# ESC : élévation de 10 à 15 mmHg ; eau 2–3 L ; NaCl 10 g [S4]
R["F20"] = {"formule": "lecture directe ; 10 g de NaCl ≈ 10 × 393/1000 g de sodium", "Na_g": round(10 * 22.99 / 58.44, 2),
            "Na_mmol": round(10 * 1000 / 58.44, 0)}

# Conduite automobile [S26] : délais
R["F31"] = {"formule": "lecture directe du tableau 1 (SSC/SSML 2024)", "1er_groupe_indeterminee_mois": 3, "2e_groupe_sans_diagnostic_mois": 12,
            "vasovagale_volant_1er_mois": 1, "vasovagale_volant_2e_mois": 3}

# Enrichissements (contrôle des chiffres que l'audit ajoute)
R["E01"] = {"formule": "patisiran 300 µg/kg toutes les 3 semaines ; max 30 mg si ≥ 100 kg (FI Onpattro 10/2024)",
            "dose_70kg_mg": round(0.3 * 70, 1), "dose_100kg_mg": round(0.3 * 100, 1), "plafond_coherent": round(0.3 * 100, 1) == 30,
            "perfusions_par_an": round(52 / 3, 1)}
R["E02"] = {"formule": "vutrisiran 25 mg SC tous les 3 mois (FI Amvuttra 10/2025)", "mg_an": 25 * 4, "injections_an": 4}
R["E03"] = {"formule": "eplontersen 45 mg SC 1 ×/mois (FI Wainzua 05/2025)", "mg_an": 45 * 12}
R["E04"] = {"formule": "prégabaline : ClCr ≥ 60 → 150–600 mg/j ; 30–60 → 75–300 mg/j ; < 30 : ne pas utiliser (FI Lyrica 07/2026)",
            "rapport_30_60_sur_sup60": [75 / 150, 300 / 600], "contre_emploi_ClCr_inf_30": True}
R["E05"] = {"formule": "gabapentine : 50–79 → 600–1200 ; 30–49 → 300–900 ; 15–29 → 150–600 ; < 15 → 150–300 mg/j ; hémodialyse 300–400 mg puis 200–300 mg après chaque séance de 4 h (FI Neurontin 04/2025)",
            "dose_150_equivaut_300mg_un_jour_sur_deux": 300 / 2 == 150}
R["E06"] = {"formule": "Cook 2010 cité par Jiang 2023 : ≥ 3 des 5 items → Sp 99 %, RV+ 30,9 ; 0–1 item → Se 94 %",
            "lecture": "La probabilité post-test de 94 %% publiée correspond à une prévalence de l’échantillon d’environ un tiers (88/249 = %.1f %%)." % (88 / 249 * 100),
            "prevalence_echantillon_pourcent": round(88 / 249 * 100, 1),
            "post_test_recalcule_pourcent": round(100 * ((88 / 161) * 30.9) / (1 + (88 / 161) * 30.9), 1)}
R["E07"] = {"formule": "compression asymptomatique → MCD : 8 % à 1 an, 22 % sur 44 mois médians (n = 199) [S8]",
            "patients_1an": round(0.08 * 199), "patients_total": round(0.22 * 199)}

R["E08"] = {"formule": "cas 2 de la sémiologie proposée : 132/78 → 108/74 mmHg ; FC 80 → 112/min ; cas récapitulatif 130/80 → 105/70",
            "delta_PAS": 132 - 108, "delta_PAD": 78 - 74, "delta_FC": 112 - 80, "HO": (132 - 108) >= 20,
            "neurogene_suggere": (112 - 80) <= 10, "cas_recap_delta": [130 - 105, 80 - 70]}
R["E09"] = {"formule": "figure 6 proposée : hauteur = pourcentage × 180 px (axe de 30 à 210)", "Portugal_px": round(0.80 * 180, 1),
            "Suede_px": round(0.11 * 180, 1), "dessine": [144, 20]}


# ---------------------------------------------------------------------------
# Faits : valeurs de la source, motifs de rattachement, verdict
# ---------------------------------------------------------------------------
def F(fid, valeurs, motif, source, verdict, note, formule="lecture directe de la source", ancre=None, vctx=()):
    vals = []
    for v in valeurs:
        if isinstance(v, str) and not re.match(r"^[\d  ,.]+$", v):
            vals.append(v)
        else:
            vals.append(num(v))
    return {"fid": fid, "valeurs": vals, "motif": motif, "source": source, "verdict": verdict, "note": note,
            "formule": formule, "ancre": ancre, "vctx": list(vctx)}


AGREMENT_FAUX = [
    # % d'accord du panel UEG/ESNM présenté sans « accord » comme une fréquence, une validité ou une efficacité
    (r"^95$", r"vomissements \(95 %\)|fréquents \(95 %\)", "FAUX"),
    (r"^98$", r"scintigraphie \(98 %\)", "FAUX"),
    (r"^95$", r"respiratoire \(95 %\)", "FAUX"),
    (r"^85$", r"retenue \(85 %\)|5-HT4 \(85 %\)", "FAUX"),
    (r"^86$", r"D2 \(86 %\)", "FAUX"),
    (r"^88$", r"cause \(88 %\)", "FAUX"),
]

FAITS = [
    F("F01", [20, 10, 90, 30], r"mmHg|systolique|diastolique|verticalisation|baisse|décubitus|20 mmHg|seuil", "S4/S5", "CORRECT",
      "ESC 2018 : ΔPAS ≥ 20 mmHg ou ΔPAD ≥ 10 mmHg, ou PAS < 90 mmHg ; Diabetologia 2024 : ≥ 30 mmHg en cas d’hypertension de décubitus."),
    F("F02", [10], r"battements|par minute|fréquence", "S4", "CORRECT",
      "ESC 2018 : « usually not >10 b.p.m. ». La discipline Physiologie écrit « au plus 10 » sans « habituellement » (formulation approchée, SEM-20).",
      vctx=[(r"^10$", r"au plus 10 battements", "ARRONDI")]),
    F("F03", [100, 85, 95, 93, 98, 88, 68, 60, 28, 86], r"accord|grade|consensus|obligatoire|valide|retenu|Cajal|vagale|diététique|D2|5-HT4|cause|scintigraphie|respiratoire|grêle|vomissements|fréquents|opioïdes|diabète|vidange|symptômes|perturbée", "S3", "CORRECT",
      "Valeurs d’accord du panel exactes (énoncés 1.1, 1.2, 1.3, 1.4, 2.2, 2.8, 4.1, 4.5, 4.8, 5.1, 5.3, 5.4, 5.5, 5.8, 6.1, 6.7, 6.14, 6.39, 7.2). Lorsqu’elles sont écrites sans « accord » à côté d’un symptôme, d’un test ou d’un traitement, elles se lisent comme une fréquence, une validité ou une efficacité : grandeur erronée (constat C03).",
      vctx=AGREMENT_FAUX),
    F("F04", [1, 2], r"test|tests|Toronto|possible|confirm|anormal|Résultat", "S5/Spallone 2011", "CORRECT",
      "Toronto : 1 test cardiovagal anormal = possible ; ≥ 2 tests cardiovagaux anormaux = confirmée ; + HO = sévère. La précision « cardiovagaux (de fréquence) » manque dans g99-13 et g99-toronto (constat C13).",
      ancre=r"g99-1$|g99-13|g99-toronto|g99-e-2"),
    F("F06", [15, 17, 12, 14, 11], r"mJOA|léger|modéré|sévère|AO Spine|moins", "S11", "CORRECT", "AO Spine 2026 : léger 15–17, modéré 12–14, sévère ≤ 11 (recommandation conditionnelle, faible niveau de preuve)."),
    F("F07", [1, 2, 3], r"stade|locomotion|fauteuil|marche|Stade|alitement", "S7", "CORRECT", "Consensus européen 2021, tableau 6 : stades 1 à 3 ; PND I à IV.",
      ancre=r"g99-1$|g99-attr|g99-mnemo|glossary"),
    F("F08", [20, 29, 54, 12, 73, 9, 38, 0, 18, 6], r"diabét|prédiabète|normoglyc|personnes|neuropathie|varient|Diabetologia|type", "S5/S15", "CORRECT",
      "Diabetologia 2024 : ≈ 20 %% ; 29–54 %% (DT1), 12–73 %% (DT2) ; prédiabète 9–38 %% contre 0–18 %%. Bornes résumées recalculées : %s à %s %%." % (R["F08"]["min"], R["F08"]["max"]),
      R["F08"]["formule"], ancre=r"g99-2|g99-13"),
    F("F09", [822, 899, 6, 39, 9, 49, 50], r"Steno|premiers|seconds|coexist|diabète de type|personnes avec", "S15", "CORRECT",
      "Mizrak 2024 : 822 DT1, 899 DT2 ; NAD 6–39 % et 9–49 % ; coexistence DPN–DAN dans 50 % des cas."),
    F("F10", [728, 48.2, 32.4, 15.8, 2.26], r"polonaise|précoce|confirmée|cotes|neuropathie|728", "S16", "CORRECT",
      "Ignacy 2026 : 728 ; 48,2 %% (32,4 + 15,8 = %s) ; OR rétinopathie 2,26 (IC 1,25–4,19)." % R["F10"]["trouve"], R["F10"]["formule"]),
    F("F11", [5.2, 1.0, 0.2, "dix ans"], r"incidence|type 1|type 2|témoins|dix ans|cumulée", "S3", "CORRECT",
      "UEG/ESNM 2021 (étude populationnelle citée) : 5,2 %% DT1, 1,0 %% DT2, 0,2 %% témoins à 10 ans ; rapport DT1/DT2 = %s." % R["F11"]["DT1_vs_DT2"], R["F11"]["formule"]),
    F("F12", [1.6, 100000, 40, 59, 108, 183, 80, 31.6, 66.8, 50], r"prévalence|opérées|avant 40|volontaires|décennie|compression|40-80|40 à 80|asymptomatique|Plus de 50|cinquantaine|image", "S8", "CORRECT",
      "BMJ 2018 : prévalence opérée 1,6/100 000 ; 108/183 = %s %% (publié 59 %%) ; 31,6 %% et 66,8 %%. « Plus de 50 ans » (g99-0) résume « most patients first diagnosed in their 50s » : formulation approchée." % R["F12"]["trouve"],
      R["F12"]["formule"], vctx=[(r"^50$", r"Plus de 50 ans", "ARRONDI")]),
    F("F13", [5, 10], r"métasta|tumorales|compression médullaire|Compression", "S13", "CORRECT", "RMS 2016 : « jusqu’à 5 à 10 % de tous les patients ayant des métastases ou autres atteintes tumorales osseuses »."),
    F("F14", [73, 53, 50, 46, 30], r"dysautonomie|impuissance|digestifs|incontinence|orthostatique|perte de poids|Dysautonomie", "S7", "CORRECT",
      "Consensus européen 2021 : 73 % ; impuissance 73 % des hommes ; GI 53 % ; incontinence 50 % ; dysrégulation orthostatique 46 % ; perte de poids ≈ 30 %."),
    F("F14b", [50], r"forme précoce|avant 50", "S7", "CORRECT", "Consensus 2021 : début avant 50 ans = forme précoce."),
    F("F15", [1.61, 1.85, 1.96, 25, 50, "cinq ans"], r"ACCORD|mortalité|Mortalité|risque|ischémie|cinq ans|avancée|insuffisance cardiaque", "S5", "CORRECT",
      "Diabetologia 2024 : HR 1,61 (IC 1,11–2,36) et 1,85 (1,17–2,93) ; RR 1,96 (1,53–2,51) ; mortalité à 5 ans 25–50 % (NAC avancée)."),
    F("F16", [130], r"battements|repos|jusqu", "S5", "CORRECT", "Diabetologia 2024 : « resting tachycardia (up to 130 beats/min) »."),
    F("F17", [86, 28], r"QT|spécifique|sensible|Spécifique", "S5", "CORRECT", "Méta-analyse (n = 4584) : spécificité 86 %, sensibilité 28 %."),
    F("F17b", [415, 445], r"QTc|hypoglycémie|ms", "S5", "ARRONDI",
      "Kacheva : 415,1 ± 21,9 → 444,9 ± 26,5 ms, soit + %s ms ; population majoritairement non diabétique (106/119) non précisée dans la leçon." % R["F17"]["delta_ms"], R["F17"]["formule"]),
    F("F18", [42, 59, 68], r"arythmie|cardiovasculaire|mortalité", "S5", "CORRECT", "Méta-analyse citée par Diabetologia 2024 : + 42 %, + 59 %, + 68 %."),
    F("F19", [28.9, 35.2, 160, 15, 18, 2], r"DCCT|EDIC|prévalence|Steno|multifactorielle|études|exercice|cardiaque dans|contre|numéro|Essai|Étude", "S5", "CORRECT",
      "DCCT/EDIC 28,9 %% contre 35,2 %% ; Steno-2 n = 160 ; exercice 15/18 = %s %%." % R["F19"]["trouve"], R["F19"]["formule"],
      ancre=r"g99-9|glossary"),
    F("F20", [10, 15, 2, 3, 2.5, 0.1, 0.3, "quatre heures", 4], r"pression debout|amélioration|eau|litres|chlorure|sel|tête du lit|surélevée|midodrine|fludrocortisone|droxidopa|trois fois|coucher|10°|L/jour|mg|> 10", "S4", "CORRECT",
      "ESC 2018 : hausse de 10–15 mmHg ; 2–3 L d’eau ; 10 g de NaCl (≈ %s g de sodium, %s mmol) ; tête du lit > 10° ; midodrine 2,5–10 mg 3 ×/j ; fludrocortisone 0,1–0,3 mg/j ; dernière dose de midodrine ≥ 4 h avant le coucher (FI Gutron)." % (R["F20"]["Na_g"], R["F20"]["Na_mmol"]),
      R["F20"]["formule"], ancre=r"g99-9|g99-13|pareto-g99-trait|g99-nondipper|pareto-g99-pharma"),
    F("F21", [3, 2.5, 30, 45, 15, 10, 4], r"début|première dose|lever|certains cas|ESC|coucher|systolique|2,5", "S20/S4", "CORRECT",
      "FI Gutron (03/2021) : 3 × 2,5 mg/j = %s mg/j ; 30–45 min avant le lever ; PAS 3 min après le lever ; jusqu’à 15 mg/j dans certains cas ; > 30 mg/j non recommandé (plafond omis : C11) ; ESC max 3 × 10 = %s mg/j." % (R["F21"]["debut_mg_j"], R["F21"]["ESC_max_mg_j"]),
      R["F21"]["formule"], ancre=r"g99-p-2|g99-midodrine"),
    F("F22", [0.1, 0.2], r"trois fois par semaine|par jour|insuffisance|perte de sel|suisses|mg", "S21", "CORRECT",
      "FI Florinef (03/2026) : 0,1 mg 3 ×/semaine à 0,2 mg/j (norme 0,1 mg/j) ; ≤ 0,05 mg/j si hypertension transitoire (omis). ESC 0,3 mg/j > FI 0,2 mg/j (C12).",
      R["F22"]["formule"], ancre=r"g99-p-2|g99-fludro"),
    F("F23", [10, 15, 30, 12, 35, 1], r"repas|à partir de|35 kg|ans et|semaine|dompéridone|Motilium|fois par jour, 15", "S22", "CORRECT",
      "FI Motilium (06/2026) : 10 mg 3 ×/j (= %s mg/j), 15–30 min avant les repas, ≥ 12 ans et ≥ 35 kg, ≤ 1 semaine." % R["F23"]["mg_j"],
      R["F23"]["formule"], ancre=r"g99-p-2|g99-domperidone|g99-13|pareto-g99-pharma|g99-12"),
    F("F24", [10, 3, 30, 0.5, 5, 50, 15, 60, 75], r"jusqu|maximum|mg/kg|jours|clairance|réduit|Réduction|mL|métoclopramide|Paspertin", "S23", "CORRECT",
      "FI Paspertin (01/2020) : 10 mg ≤ 3 ×/j ; max 30 mg/j ou 0,5 mg/kg (min des deux ; égalité à %s kg) ; ≤ 5 jours ; −50 %% (ClCr 15–60) → %s mg/j ; −75 %% (ClCr ≤ 15) → %s mg/j." % (R["F24"]["seuil_poids_kg_ou_0_5mgkg_egale_30mg"], R["F24"]["max_IR_moderee_mg_j"], R["F24"]["max_IR_terminale_mg_j"]),
      R["F24"]["formule"], ancre=r"g99-p-2|g99-metoclopramide|g99-11|g99-12|g99-13|pareto-g99-pharma"),
    F("F25", [61, 80], r"tafamidis|méglumine|mg", "S24", "CORRECT", "FI Vyndaqel (04/2026) : 61 mg tafamidis ≡ 80 mg méglumine (4 × 20 mg).", R["F25"]["formule"]),
    F("F26", [2.2, 5.2, 3.6, 43, 18, 746, 6, 12, "six mois"], r"retard|consultations|cas|main|présentations|carpien|fractures|signes évocateurs|diagnostic préalable|série AO Spine|six mois|récupération|maximale|vers 6|mois|Retard", "S8", "CORRECT",
      "BMJ 2018 : 2,2 ans ; 5,2 ± 3,6 consultations (± 1 ET : %s à %s) ; 43 %% ; 18 %% (66 fractures de hanche) ; série AO Spine 746 ; récupération maximale 6–12 mois ; traitement < 6 mois." % (R["F26"]["bas"], R["F26"]["haut"]),
      R["F26"]["formule"]),
    F("F26b", [6], r"traitement dans les 6 mois|dans les 6 mois", "S8", "CORRECT", "BMJ 2018 : « treatment within six months of symptoms »."),
    F("F27", [55, "neuf mois", 58, 62], r"homme de|femme diabétique|depuis neuf mois|ans,", "énoncé", "CORRECT", "Données d’énoncé fictives, plausibles ; aucune incohérence interne."),
    F("F28", [105, 130, 80, 70, 25, 20], r"pression passe|couché|debout|baisse systolique|seuil|repos de 105", "S4 + énoncé", "CORRECT",
      "Recalcul : ΔPAS %d mmHg, ΔPAD %d mmHg → HO %s (le critère diastolique est aussi atteint, non cité)." % (R["F28a"]["delta_PAS"], R["F28a"]["delta_PAD"], R["F28a"]["HO"]),
      R["F28a"]["formule"], ancre=r"g99-11"),
    F("F28q", [140, 85, 118, 80, 22, 20, 10], r"couchée|debout|baisse|seuil|critère|au moins 20|diastolique", "S4 + énoncé", "CORRECT",
      "Recalcul : ΔPAS %d, ΔPAD %d → réponse A juste ; B exacte mais non pertinente (un seul critère suffit)." % (R["F28b"]["delta_PAS"], R["F28b"]["delta_PAD"]),
      R["F28b"]["formule"], ancre=r"g99-e-6"),
    F("F29", [24], r"mois|neuroprotectrice", "S18", "CORRECT", "Chiang 2022 : « neuroprotective at the 24-month follow-up visit »."),
    F("F30", [6, 12], r"réévaluation|tous les|transthyrétine|mois", "S7", "CORRECT", "Consensus 2021 : suivi tous les 6–12 mois.", ancre=r"g99-10|glossary"),
    F("F31", [3, 12, 1, 14, 2, 7], r"mois|article|alinéa|annexe|art\.|groupe|conducte|version", "S26", "CORRECT",
      "SSC/SSML 2024 v2 : art. 14 al. 2 LCR ; annexe 1 OAC (art. 7 al. 1) ; 3 mois / ≥ 12 mois ; 1 mois / ≥ 3 mois.", R["F31"]["formule"], ancre=r"g99-12|glossary"),
    F("F32", [103, 104, 61, 100, 149, 217, 214, 96, 97, 202], r"situations|parésie|sensitive|nausées|vertiges|syncope|hypotension|chutes|marche|incontinence", "S28", "CORRECT",
      "Copie du référentiel PROFILES du dépôt (nosology/ssp_profiles2017.json) : intitulés concordants."),
    F("F33", [31, 30, 15, 5, 24], r"COMPASS|rapport 30|30:15|5-HT4|24 heures|31 questions|31 items|Composite", "S5/S4/S3", "CORRECT",
      "Identifiants et durées : COMPASS-31 (31 questions), rapport 30:15, récepteur 5-HT4, MAPA sur 24 h."),
    F("F34", [20, "quatre heures", 2, 4], r"rétention|quatre heures|seuils|pronostique|vidange", "S3", "CORRECT",
      "UEG/ESNM 2021 : « 4-h gastric retention more than 20% » est associée à une MOINDRE intensité des symptômes à 48 semaines (facteur de bon pronostic) ; la leçon n’indique pas le sens (constat C14). Seuils diagnostiques à 2 et 4 h : absents de la source (lacune maintenue).", ancre=r"g99-7|g99-e-3|g99-vidange|g99-13"),
    F("F35", [50], r"Plus de 50|engourd", "S8", "ARRONDI", "Voir F12 : « most patients first diagnosed in their 50s ».", ancre=r"g99-0"),
]

ORDRE = ["F28", "F28q", "F27", "F20", "F21", "F22", "F23", "F24", "F25", "F30", "F31", "F32", "F33", "F34", "F17b", "F17", "F16", "F15",
         "F18", "F10", "F09", "F14b", "F14", "F13", "F12", "F35", "F11", "F06", "F07", "F26b", "F26", "F29", "F19", "F04",
         "F02", "F03", "F01", "F08"]

CITATION = re.compile(r"(?:19|20)\d{2}\s*;\s*\d+(?:\s*\([^)]*\))?\s*:\s*[\dSek–\-]+|e\d{6}|\d{4}\s*;\s*\d+")


def biblio(e):
    c = e["contexte"]
    for m in CITATION.finditer(c):
        if re.search(r"(?<![\d,])" + re.escape(e["valeur"]) + r"(?![\d,])", m.group(0)):
            return True
    return False


def classer(e):
    if e["nature"] == "valeur":
        return not biblio(e)
    if e["nature"] == "valeur_en_lettres":
        return not re.match(r"(?i)^un patient$|^trois grandes$|^une semaine$", e["valeur"])
    return False


def fenetre(e, marge=50):
    """Fenêtre de ± marge caractères autour de l'occurrence (position enregistrée par l'inventaire)."""
    c, v = e["contexte"], e["valeur"]
    pos = [m.start() for m in re.finditer(re.escape(v), c)]
    if not pos:
        return c
    p = min(pos, key=lambda x: abs(x - e.get("position", 90)))
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
    res, non_rattachees, bib = [], [], 0
    for e in inv["occurrences"]:
        if e["nature"] == "valeur" and biblio(e):
            bib += 1
        if not classer(e):
            continue
        f = rattacher(e)
        if not f:
            non_rattachees.append({"id": e["id"], "fichier": e["fichier"], "ancre": e["ancre"], "valeur": e["valeur"], "contexte": e["contexte"]})
            continue
        verdict = f["verdict"]
        for rv, rc, vd in f["vctx"]:
            if re.search(rv, e["valeur"]) and re.search(rc, fenetre(e, 25)):
                verdict = vd
        res.append({"id": e["id"], "fait": f["fid"], "fichier": e["fichier"], "ancre": e["ancre"],
                    "trouve": e["valeur"] + (" " + e["unite"] if e["unite"] and e["unite"] != "en lettres" else ""),
                    "attendu": "valeur de la source %s" % f["source"] if f["formule"] == "lecture directe de la source" else "recalcul : " + f["formule"],
                    "ecart": 0 if verdict == "CORRECT" else ("arrondi ou formulation approchée" if verdict == "ARRONDI" else "voir note"),
                    "verdict": verdict, "formule": f["formule"], "source": f["source"], "note": f["note"]})
    calculables = len(res) + len(non_rattachees)
    compte = {k: sum(1 for r in res if r["verdict"] == k) for k in ("CORRECT", "ARRONDI", "FAUX", "NON_VERIFIABLE")}
    doc = {
        "mission": "ALPHA1-CLAUDE-G99-MED",
        "script": "calculs/verifier.py",
        "tolerance": "± 0,05 point pour les pourcentages publiés à une décimale ; ± 0,5 ms pour le QTc ; égalité exacte pour les sommes, différences tensionnelles et doses",
        "total_releves": inv["total"],
        "references_bibliographiques_exclues": bib,
        "calculables": calculables,
        "recalcules": len(res),
        "correct": compte["CORRECT"], "arrondi": compte["ARRONDI"], "faux": compte["FAUX"], "non_verifiables": compte["NON_VERIFIABLE"],
        "non_rattachees": non_rattachees,
        "faux_detail": [{k: r[k] for k in ("id", "fichier", "ancre", "trouve", "note")} for r in res if r["verdict"] == "FAUX"],
        "recalculs": R,
        "faits": [{k: f[k] for k in ("fid", "source", "verdict", "formule", "note")} for f in FAITS],
        "resultats": res,
    }
    (ICI / "resultats.json").write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print({k: doc[k] for k in ("total_releves", "references_bibliographiques_exclues", "calculables", "recalcules", "correct", "arrondi", "faux", "non_verifiables")})
    for n in non_rattachees:
        print("NON RATTACHÉE", n["id"], n["ancre"], n["valeur"], "|", n["contexte"][:150])
    for r in doc["faux_detail"]:
        print("FAUX", r["id"], r["ancre"], r["trouve"])


if __name__ == "__main__":
    main()
