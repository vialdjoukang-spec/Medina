#!/usr/bin/env python3
"""Audit ALPHA77 G94 — inventaire scripté et recalcul de toutes les grandeurs de la leçon.

Exécution (depuis la racine du dépôt ou d'un worktree) :
    python3 docs/collaboration/ssp-v2/execution/ALPHA1-CLAUDE-G94-MED/calculs/verifier.py

Sorties (dans le dossier du script) : inventaire.json, resultats.json.
Lecture seule des 7 fichiers canoniques ; aucune écriture hors de calculs/.

Trois familles de contrôles :
  1. RECALCUL : grandeur dérivable (pourcentage d'un effectif, complément, cohérence d'un
     intervalle de confiance, conversion d'unités, arithmétique de dose, comparaison à un seuil).
  2. CONCORDANCE_SOURCE : valeur rapportée, comparée à la citation exacte de la source lue
     (Sx de sources.json) ; verdict CORRECT si la valeur figure dans la citation.
  3. NON_CALCULABLE : identifiant (année, numéro d'îlot, code CIM, numéro de nerf crânien,
     isotope, rang, numéro de figure ou de cas) ; relevé mais sans objet de calcul.
"""
from __future__ import annotations

import html
import json
import math
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
FILES = [
    "chapters/G94/G94_a.html", "chapters/G94/G94_b.html", "chapters/G94/G94_c.html",
    "chapters/G94/G94_d.html", "chapters/G94/G94_pop1.html", "chapters/G94/G94_pop2.html",
    "glossary/g94.py",
]
NUM = re.compile(r"(?<![\w.,\-])([+−]?\d+(?:[.,]\d+)?)(?:\s?[–-]\s?(\d+(?:[.,]\d+)?))?")
UNIT = re.compile(r"^\s?(%|mmHg|mm H₂O|mmol/L|mg/L|µg/L|mg/kg|mg|g/dL|°C|kJ|mL|/mm³|minutes|heures|jours|"
                  r"semaines|mois|ans|patients|épisodes|pour 100 000|sur 15|sur 577|signes|cas)")
MMHG_PER_KPA = 7.50062
MMH2O_PER_MMHG = 13.595
GLUCOSE_MG_DL_PER_MMOL = 18.016
GLUCOSE_MW = 180.16
KJ_PER_KCAL = 4.184


def texte(path: Path) -> list[tuple[str, str]]:
    s = path.read_text(encoding="utf-8")
    if path.suffix == ".py":
        return [("glossary/g94.py", re.sub(r"\s+", " ", s))]
    # Les attributs SVG (coordonnées) ne sont pas du contenu : seul le texte des <text> est gardé.
    s = re.sub(r"<svg.*?</svg>", lambda m: " " + " ".join(re.findall(r">([^<]+)<", m.group(0))) + " ",
               s, flags=re.S)
    parts, last, anchor = [], 0, path.name
    for m in re.finditer(r'(?:\bid|data-pop)="([^"]+)"', s):
        parts.append((anchor, s[last:m.start()]))
        anchor, last = m.group(1), m.end()
    parts.append((anchor, s[last:]))
    out = []
    for a, chunk in parts:
        chunk = re.sub(r'<[^>]+>', " ", chunk)  # balises et attributs (data-k, href) retirés
        t = re.sub(r"\s+", " ", html.unescape(chunk))
        out.append((a, t))
    return out


def classer(tok: str, avant: str, apres: str) -> str:
    v = tok.lstrip("+−")
    if avant.rstrip().endswith(">") or avant.endswith('"'):
        return "NON_CALCULABLE:numero_ilot"
    if re.search(r"(_k|\[|sys|\(_k|'B|'G)\W{0,3}$", avant) or re.search(r"(import|insert|_k\[)", avant[-15:]):
        return "NON_CALCULABLE:code_python"
    if re.search(r"(Examen ou conduite|liquide cérébrospinal|médicaments|%|contraste en manque plus de 40 %|immédiate|0 à 30 %\)) ?$", avant) and re.match(r" [A-ZÉ]", apres) and len(v) == 1:
        return "NON_CALCULABLE:rang_tableau"
    if re.search(r"contraste\. ?(\d ){0,4}$", avant) or re.search(r"(;|:) ?$", avant) and re.match(r"\. [a-zé]", apres):
        return "NON_CALCULABLE:numero_legende"
    if re.search(r"[ée]tapes ?$", avant) or re.search(r"[ée]tapes \d et ?$", avant):
        return "NON_CALCULABLE:numero_etape"
    if re.search(r"(G ?|G94|K72|B48|B60|B34|A41|A00|B99|C00|D48|E51|block-g|htmlgm)\.?$", avant) or \
            re.match(r"\.\d", apres) and re.search(r"(G|K|B|A|E)\d*$", avant):
        return "NON_CALCULABLE:code_CIM"
    if re.fullmatch(r"(19|20)\d\d", v) and not re.match(r"\s?(%|patients|cas)", apres):
        return "NON_CALCULABLE:date"
    if re.search(r"(Betta|Figure|Cas|Rang|îlot|tableau|niveau|type|S|Type|e-|p-)\s?$", avant):
        return "NON_CALCULABLE:identifiant"
    if re.match(r"\s?(\)|,)?\s?(II|III|IV|VI|VII|VIII)\b", apres) or re.search(r"nerfs crâniens \($", avant):
        return "NON_CALCULABLE:identifiant"
    if re.search(r"(indium|technétium|In|Tc|⁹⁹|¹¹¹)-?$", avant) or re.match(r"-(DTPA|MAA)", apres):
        return "NON_CALCULABLE:isotope"
    if re.search(r"\(\d?$", avant) and re.match(r"\)", apres) and len(v) == 1:
        return "NON_CALCULABLE:numero_de_liste"
    if re.search(r"(^|[ (])$", avant[-1:] or " ") and re.match(r"\. [A-ZÉ]", apres) and len(v) == 1 \
            and not re.search(r"(à|Glasgow) ?$", avant):
        return "NON_CALCULABLE:numero_de_liste"
    return "GRANDEUR"


def inventaire() -> list[dict]:
    items, n = [], 0
    for f in FILES:
        for ancre, t in texte(ROOT / f):
            for m in NUM.finditer(t):
                n += 1
                avant, apres = t[max(0, m.start() - 45):m.start()], t[m.end():m.end() + 35]
                u = UNIT.match(apres)
                items.append({
                    "id": f"I{n:03d}", "fichier": f, "ancre": ancre, "valeur": m.group(0).strip(),
                    "unite": (u.group(1) if u else ""),
                    "contexte": (avant + m.group(0) + apres).strip(),
                    "categorie": classer(m.group(1), avant, apres),
                    "_pos": len(avant) - (len(avant) - len(avant.lstrip())),
                })
    return items


# ------------------------------------------------------------ concordance avec les sources lues
# (valeur telle qu'écrite, motif de contexte, source, citation exacte ou section de la source)
S_SONN, S_SHH, S_THY, S_KAS, S_EANO = "S2", "S3", "S4", "S5", "S6"
S_EFNS, S_ESO, S_DON, S_BEN, S_DEX, S_BFARM = "S7", "S8", "S9", "S10", "S11", "S1"
C = [
    # --- vignettes et identifiants pédagogiques
    ("68", r"homme de 68|68 ans", "VIGNETTE", "âge d'un cas fictif"),
    ("9", r"Glasgow (est )?à 9|à 9 sur 15|Glasgow à 9", "VIGNETTE", "score d'un cas fictif (comparé à l'échelle dans R31)"),
    ("15", r"9 sur 15|sur 15 points|inférieur à 15|Glasgow inférieur à 15", S_SONN, "GCS < 15 (définition) ; échelle sur 15"),
    ("55", r"femme de 55", "VIGNETTE", "âge d'un cas fictif"),
    ("52", r"homme de 52", "VIGNETTE", "âge d'un cas fictif"),
    ("62", r"patient de 62", "VIGNETTE", "âge d'un cas fictif"),
    ("2", r"deuxième jour|au deuxième", "VIGNETTE", "chronologie d'un cas fictif"),
    # --- Kasanmoentalib 2010 (S5)
    ("5", r"taux de 5 %|\(5 %\)", S_KAS, "26 of 577 episodes (5%)"),
    ("15", r"15 % des patients ont reçu une dériva", "RECALCUL", "dénominateur faux : 4/26 et non 4/577 (R09, C07)"),
    ("69", r"69 % des hydrocéphalies", S_KAS, "The majority of patients (69%) presented with hydrocephalus on admission"),
    ("5", r"5 % \(26|complique 5 %|5 % des méningites|Hydrocéphalie : 5 %|5 % de méningite|5 % des ménin", S_KAS, "Hydrocephalus was diagnosed in 26 of 577 episodes (5%)"),
    ("26", r".", S_KAS, "26 of 577 episodes"),
    ("577", r".", S_KAS, "26 of 577 episodes"),
    ("69", r"admission|l’admission|arrivée|dès l’admission|présente à l", S_KAS, "The majority of patients (69%) presented with hydrocephalus on admission"),
    ("69", r"défavorable", S_KAS, "18 had an unfavorable outcome (69%)"),
    ("2006–2009", r".", S_KAS, "prospective nationwide cohort study from Dutch hospitals from 2006 to 2009"),
    ("2006", r".", S_KAS, "from 2006 to 2009"), ("2009", r".", S_KAS, "from 2006 to 2009"),
    ("54", r"pneumoniae", S_KAS, "Streptococcus pneumoniae (in 14 patients, 54%)"),
    ("15", r"monocytogenes", S_KAS, "Listeria monocytogenes (in 4 patients, 15%)"),
    ("50", r"[Dd]écès dans 50|mortalité est de 50|Décès dans 50", S_KAS, "Thirteen patients died (50%)"),
    ("7,81", r".", S_KAS, "odds ratio 7.81, 95% confidence interval 2.91-20.8"),
    ("2,91", r".", S_KAS, "95% confidence interval 2.91-20.8"), ("20,8", r".", S_KAS, "2.91-20.8"),
    ("15", r"dérivation externe|drain ventriculaire|quatre \(15", S_KAS, "4 patients (15%) underwent external ventricular CSF catheter placement"),
    ("8", r"ponctions lombaires répétées|Deux patients \(8", S_KAS, "2 patients (8%) had serial lumbar punctures"),
    ("12", r"délai médian de 12", S_KAS, "Median time from diagnosis of hydrocephalus to CSF shunting was 12 hours"),
    # --- Sonneville 2023 (S2)
    ("70", r"[Jj]usqu’à 70", S_SHH, "occurring in up to 70% of patients admitted to the intensive care unit"),
    ("54", r"50 patients|série de 50", S_SONN, "SAE, defined by a GCS < 15 was observed in 54% of patients"),
    ("54", r"fréquence est de 54", S_SONN, "SAE ... observed in 54% of patients"),
    ("50", r"54 % chez 50|série de 50 patients|chez 50 patients", S_SONN, "a landmark study conducted in 50 non-sedated ICU septic patients"),
    ("53", r"française", S_SONN, "53% in a French ICU multicenter cohort"),
    ("19", r"léger", S_SONN, "from mild delirium (19%) to coma (40%)"),
    ("40", r"coma dans 40", S_SONN, "to coma (40%)"),
    ("10", r"agitation|[Aa]gitation", S_SONN, "agitation (~ 10% of cases)"),
    ("2", r"convulsives|[Cc]rises convulsives", S_SONN, "Convulsive seizures (~ 2% of cases)"),
    ("1", r"focaux|signes focaux", S_SONN, "focal signs (~ 1% of cases)"),
    ("3", r"durée médiane du délire|médiane du délire septique est de trois", S_SONN, "median duration ... 3 (interquartile range 2–6) days"),
    ("2", r"interquartile 2", S_SONN, "interquartile range 2–6"), ("6", r"2 à 6\)", S_SONN, "interquartile range 2–6"),
    ("3", r"score de 3 à 8|de 3 à 8", S_SONN, "patients with GCS 3 to 8 having the worst prognosis"),
    ("8", r"score de 3 à 8|de 3 à 8,", S_SONN, "GCS 3 to 8"),
    ("3,37", r".", S_SONN, "HR 3.37, 95% CI 2.82–4.03"), ("2,82", r".", S_SONN, "95% CI 2.82–4.03"), ("4,03", r".", S_SONN, "2.82–4.03"),
    ("95", r"confiance à 95", S_SONN, "95% CI (identifiant d'intervalle)"),
    ("13", r"13 à 14|de 13 à 14", S_SONN, "a score on the GCS of 13 or 14"), ("14", r"13 à 14", S_SONN, "GCS of 13 or 14"),
    ("1,38", r".", S_SONN, "HR 1.38, 95% CI 1.09–1.38"),
    ("65", r"pression artérielle moyenne", S_SONN, "Table 2 — MAP 65–80 mmHg"), ("80", r"65 à 80", S_SONN, "MAP 65–80 mmHg"),
    ("80", r"PaO₂ de 80", S_SONN, "PaO2 80–120 mmHg"), ("120", r"80 à 120", S_SONN, "PaO2 80–120 mmHg"),
    ("35", r"PaCO₂|35 à 45", S_SONN, "PaCO2 35–45 mmHg"), ("45", r"35 à 45|supérieure à 45", S_SONN, "PaCO2 35–45 mmHg ; Hypercapnia (> 45 mmHg)"),
    ("36", r"température|36 à 38", S_SONN, "Temperature 36–38.3°C"), ("38,3", r".", S_SONN, "Temperature 36–38.3°C"),
    ("135", r"natrémie|135 à 145", S_SONN, "Natremia 135–145 mmol/L"), ("145", r"135 à 145", S_SONN, "Natremia 135–145 mmol/L"),
    ("5", r"glycémie de 5|glycémie 5", S_SONN, "Glycemia 5–10 mmol/L"), ("10", r"5 à 10 mmol", S_SONN, "Glycemia 5–10 mmol/L"),
    ("3", r"inférieure à 3", S_SONN, "Hypoglycemia (< 3 mmol/l)"), ("10", r"ou supérieure à 10", S_SONN, "hyperglycemia (> 10 mmol/l)"),
    ("7", r"hémoglobine supérieure à 7", S_SONN, "Hemoglobin > 7g/dL"),
    ("10", r"thêta 10|10 à 50|bas voltage ou discontinu 10|discontinu 10", S_SONN, "theta ... 10 to 50% ; low voltage and discontinuous background (10–60%)"),
    ("50", r"10 à 50", S_SONN, "theta ... 10 to 50%"),
    ("30", r"delta 30|30 à 60", S_SONN, "delta dominant rhythm in ... 30 to 60%"), ("60", r"30 à 60|10 à 60", S_SONN, "30 to 60% ; 10–60%"),
    ("3", r"suppressions 3", S_SONN, "burst suppression or suppression (3–8% of cases)"), ("8", r"suppressions 3 à 8", S_SONN, "burst suppression or suppression (3–8% of cases)"),
    ("6", r"triphasiques 6", S_SONN, "Diffuse triphasic waves are observed in 6–20%"), ("20", r"6 à 20|5 à 20", S_SONN, "6–20% ; 5–20%"),
    ("5", r"périodiques 5", S_SONN, "periodic discharges are reported in 5–20%"),
    ("0", r"0 à 30", S_SONN, "ESz are observed in 0–30% of cases"), ("30", r"0 à 30|jusqu’à 30", S_SONN, "0–30%"),
    ("11", r"11 % des encéph|anormal dans 11|Anormal dans 11", S_SONN, "CT abnormal findings were observed in 11% of cases"),
    ("5", r"infarctus 5", S_SONN, "infarction (5% of cases)"), ("4", r"hémorragie 4", S_SONN, "hemorrhage (4% of cases)"),
    ("10", r"jusqu’à 10 % des comas", S_SONN, "may represent up to 10% of unexplained non-traumatic coma"),
    ("40", r"plus de 40", S_SONN, "with more than 40% of cases misdiagnosed with non-contrast head CT"),
    ("50", r"plus de 50", S_SONN, "MRI detects brain injury in more than 50% of cases"),
    ("55", r"environ 55", S_SONN, "parenchymal lesions and atrophy ... about 55% and 16%"),
    ("16", r"environ 16", S_SONN, "about 55% and 16%"),
    ("14", r"ischémie 14|14 à 27|substance blanche 14|14 à 81", S_SONN, "Ischemic lesions ... 14–27% ; WML 14–81%"),
    ("27", r"14 à 27", S_SONN, "14–27%"), ("81", r"14 à 81", S_SONN, "14–81%"),
    ("9", r"réversible 9", S_SONN, "Posterior reversible encephalopathy syndrome is reported in 9%"),
    ("24,15", r".", S_SONN, "a NSE threshold > 24.15µg/L (AUC 0.66) had a specificity of 83%"),
    ("83", r"spécificité|énolase", S_SONN, "specificity of 83% and a sensitivity of 54.2%"),
    ("54,2", r".", S_SONN, "sensitivity of 54.2%"), ("0,66", r".", S_SONN, "AUC 0.66"),
    ("4", r"délai médian (de )?4|médian d’apparition de 4|délai médian de quatre|médian 4", S_SONN, "The median time for the development of neurotoxicity after initiating cefepime is 4 days"),
    ("93", r".", S_SONN, "altered mental status (93%)"), ("37", r".", S_SONN, "myoclonus (37%)"), ("28", r".", S_SONN, "non-convulsive seizures (28%)"),
    ("20", r"20 mg/L|dépasse 20|au-dessus de 20|supérieure à 20|de 20 mg", S_SONN, "A trough serum cefepime level exceeding 20 mg/L"),
    ("7,7", r".", S_SONN, "not observed when the trough concentration of cefepime was below 7.7 mg/L"),
    ("38,1", r".", S_SONN, "always present when levels exceeded 38.1 mg/L"),
    ("1,29", r".", S_SONN, "the annual incidence of seizure after sepsis was 1.29%"),
    ("4,98", r".", S_SONN, "incidence rate ratios of 4.98 and 4.33"),
    ("12", r"post-traumatique", S_SONN, "12% of patients had PTSD at 6 months"),
    ("9", r"neuf ans|9 ans|cohorte de 9", S_SONN, "a prospective cohort of patients followed during nine years"),
    ("2023", r".", S_SONN, "Critical Care 2023;27:386 (date de publication)"),
    ("2026", r".", S_SHH, "Intensive Care Med 2026;52:1679-96"),
    ("2025", r".", S_THY, "J Intensive Care 2025;13:5"),
    # --- OUTCOMEREA (S4)
    ("995", r".", S_THY, "We included 995 patients with severe SAE"),
    ("13", r"d’au plus 13", S_THY, "GCS ≤ 13"),
    ("1,77", r".", S_THY, "blood pressure (aHR = 1.77, 95% CI 1.34-2.34)"),
    ("1,78", r".", S_THY, "oxygenation (aHR = 1.78, 95% CI 1.20-2.63)"),
    ("1,46", r".", S_THY, "temperature (aHR = 1.46, 95% CI 1.12-1.91)"),
    ("1,41", r".", S_THY, "glycemia (aHR = 1.41, 95% CI 1.10-1.80)"),
    # --- EANO-ESMO 2023 (S6)
    ("11", r"11 à 17", S_EANO, "Hydrocephalus has been reported in 11%-17% of patients with LM"),
    ("17", r"11 à 17", S_EANO, "11%-17%"),
    ("17", r"17 % et 39,5|Entre 17", "RECALCUL", "complément 100 − 83 (R14)"),
    ("39,5", r".", "RECALCUL", "complément 100 − 60,5 (R14)"),
    ("10", r"Plus de 10|plus de 10 mL", S_EANO, "CSF volume is ideally >10 ml but at least 5 ml"),
    ("5", r"minimum 5", S_EANO, "at least 5 ml"),
    ("30", r"moins de 30", S_EANO, "processed within 30 min after sampling"),
    ("60,5", r".", S_EANO, "tumour cells have been detected at diagnosis in 60.5%-83%"),
    ("83", r"60,5 à 83", S_EANO, "60.5%-83%"),
    ("200", r"mm H₂O|200 mm", S_EANO, "increased opening pressure (>200 mm H2O) in 21%-42%"),
    ("21", r"21 à 42", S_EANO, "21%-42%"), ("42", r"21 à 42", S_EANO, "21%-42%"),
    ("4", r"/mm³|4/mm", S_EANO, "increased leukocyte counts (>4 per mm3) in 39%-77.5%"),
    ("39", r"39 à 77", S_EANO, "39%-77.5%"), ("77,5", r".", S_EANO, "39%-77.5%"),
    ("500", r"mg/L|500 mg", S_EANO, "elevated protein (>500 mg/l) in 56%-91%"),
    ("56", r"56 à 91", S_EANO, "56%-91%"), ("91", r"56 à 91", S_EANO, "56%-91%"),
    ("3", r"T1 3D|FLAIR 3D|3D", S_EANO, "post-gadolinium 3D T1-weighted and post-gadolinium 3D FLAIR sequences (dimension, non grandeur)"),
    ("3,8", r".", S_EANO, "3.8-5.4 months in breast cancer"), ("5,4", r".", S_EANO, "3.8-5.4 months"),
    ("4,2", r".", S_EANO, "4.2-8.1 months in lung cancer"), ("8,1", r".", S_EANO, "4.2-8.1 months"),
    ("4,8", r".", S_EANO, "4.8 months in melanoma"),
    ("20", r"survivent plus d’un an|20 % des patientes", S_EANO, "63 out of 318 patients (20%) surviving >1 year"),
    ("4", r"4 à 8 mois", "RECALCUL", "arrondi de 3,8–8,1 mois (R17)"), ("8", r"4 à 8 mois", "RECALCUL", "arrondi de 3,8–8,1 mois (R17)"),
    ("190", r".", S_EANO, "In a cohort of 190 patients with LM who underwent a CSF shunt procedure"),
    ("83", r"[Aa]mélioration (chez )?83", S_EANO, "83% of the patients experienced clinical improvement"),
    ("79", r".", S_EANO, "One hundred and fifty patients (79%) had no complications"),
    ("5", r"l’infection \(5|la dysfonction \(5", S_EANO, "infections were observed in 9 patients (5%) ; shunt malfunction in 9 patients (5%)"),
    ("5", r"infection \(5|[Ii]nfection 5|infection chez 5|dysfonction \(5|[Dd]ysfonction 5", S_EANO, "infections were observed in 9 patients (5%) ; shunt malfunction in 9 patients (5%)"),
    ("13", r"sous-dural", S_EANO, "subdural hygroma or haematoma in 25 patients [13%"),
    ("6,3", r".", S_EANO, "which was symptomatic in 12 patients (6.3%)"),
    ("8", r"reprise chirurgicale|révision 8|retrait ou révision", S_EANO, "An externalisation, removal or revision was indicated in 15 patients (8%)"),
    ("12", r"12 à 24|moins 12 heures", S_EANO, "Shunts can be blocked ... for 12-24 h ... A test occlusion ... for at least 12 h"),
    ("24", r"12 à 24", S_EANO, "12-24 h"),
    ("6", r"6 à 12 semaines|toutes les 6 à 12", S_EANO, "Cerebrospinal MRI should be carried out every 6-12 weeks"),
    ("12", r"6 à 12 semaines|à 12 semaines", S_EANO, "every 6-12 weeks"),
    ("2", r"deux mois|tous les deux", S_EANO, "every 2 months for the first 6 months and every 3 months thereafter"),
    ("1", r"plus d’un an|plus d'un an", S_EANO, "surviving >1 year"),
    # --- EFNS 2010 (S7)
    ("200", r"200 mg trois|3 × 200|200 mg, 3|propose 3|trois fois par jour", S_EFNS, "It should be given, before any carbohydrate, 200 mg thrice daily, preferably intravenously (Level C)"),
    ("3", r"3 × 200", S_EFNS, "200 mg thrice daily"),
    ("600", r".", "RECALCUL", "3 × 200 mg = 600 mg/j (R18)"),
    ("2010", r".", S_EFNS, "Eur J Neurol 2010;17:1408-18"),
    ("6", r"six mois|au moins six", S_EFNS, "After bariatric surgery we recommend follow-up of thiamine status for at least 6 months (Level B)"),
    # --- Benerva (S10)
    ("0,4", r".", S_BEN, "il faut en moyenne 0,4 mg de thiamine pour que soient produits environ 4200 kJ lors du métabolisme glucidique"),
    ("4200", r".", S_BEN, "environ 4200 kJ"),
    ("1,5", r".", S_BEN, "À des doses correspondant aux besoins journaliers normaux (1,5-2,5 mg)"),
    ("2,5", r".", S_BEN, "(1,5-2,5 mg)"),
    ("10", r"10 à 20 jours|10 et 20", S_BEN, "la demi-vie d'élimination de la thiamine est de 10 à 20 jours"),
    ("20", r"10 à 20 jours", S_BEN, "10 à 20 jours"),
    ("200", r"atteindre 200|jusqu’à 200|au plus 200|pouvant atteindre", S_BEN, "par voie parentérale ... à raison de doses quotidiennes pouvant atteindre 200 mg"),
    ("2019", r".", S_BEN, "Mise à jour de l'information : Avril 2019"),
    # --- Dexaméthasone Galepharm (S11)
    ("0,15", r".", S_DEX, "encéphalite/méningite: administrer 0.15 mg/kg toutes les 6 heures durant 4 jours"),
    ("6", r"toutes les 6", S_DEX, "toutes les 6 heures ; 4 mg i.v. ou i.m. à 6 heures d'intervalle"),
    ("4", r"pendant 4 jours|durant 4|6 heures pendant 4", S_DEX, "durant 4 jours"),
    ("0,4", r"0,4 mg/kg", S_DEX, "ou 0.4 mg/kg toutes les 12 heures durant 2 jours"),
    ("6", r"0,15 mg/kg toutes les 6", S_DEX, "0.15 mg/kg toutes les 6 heures"),
    ("12", r"mg/kg toutes les 12", S_DEX, "0.4 mg/kg toutes les 12 heures"),
    ("12", r"toutes les 12", S_DEX, "toutes les 12 heures"), ("2", r"pendant 2 jours|12 heures pendant 2", S_DEX, "durant 2 jours"),
    ("1", r"1 à 2 heures|après 1 à 2", S_DEX, "un certain délai (1 à 2 heures)"), ("2", r"1 à 2 heures", S_DEX, "(1 à 2 heures)"),
    ("8", r"8 à 12 mg", S_DEX, "administrer une dose initiale de 8 à 12 mg i.v."), ("12", r"8 à 12 mg", S_DEX, "8 à 12 mg i.v."),
    ("6", r"4 mg par voie intraveineuse ou intramusculaire toutes les 6|toutes les 6 heures", S_DEX, "4 mg i.v. ou i.m. à 6 heures d'intervalle"),
    ("4", r"puis 4 mg", S_DEX, "poursuivre le traitement à raison de 4 mg i.v. ou i.m. à 6 heures d'intervalle"),
    ("2022", r".", S_DEX, "Mise à jour de l'information : Juin 2022"),
    # --- ESO 2013 (S8), Donovan (S9)
    ("9", r"100 000|environ 9 pour", S_ESO, "The overall incidence is about 9 per 100,000"),
    ("100 000", r".", S_ESO, "9 per 100,000 (dénominateur)"), ("100", r"pour 100 000|9 pour 100", S_ESO, "dénominateur"),
    ("000", r"100 000", S_ESO, "dénominateur (fragment de « 100 000 »)"),
    ("50", r"50 à 60", S_ESO, "Mortality rate with conservative treatment within the first months is 50-60%"),
    ("60", r"50 à 60", S_ESO, "50-60%"),
    ("2013", r".", S_ESO, "Cerebrovasc Dis 2013;35:93-112"),
    ("2019", r"Lancet Neurology 2019|Donovan", S_DON, "Lancet Neurol 2019;18:771-83"),
    # --- BfArM (S1) et divers
    ("2024", r".", S_BFARM, "CIM-10-GM Version 2024"),
    ("2016", r"ESCMID", "LACUNE", "recommandation ESCMID 2016, non lue (accès refusé, 403)"),
    ("2022", r"European Association for the Study of the Liver|EASL", "LACUNE", "EASL 2022 — résumé non relu par l'audit"),
    ("15", r"15 octobre", "DATE", "date de consultation"),
    ("2", r"deux des quatre|deux signes|2 sur 4", S_EFNS, "requires two of the following four signs"),
    ("100", r"pour 100|100 000", S_ESO, "dénominateur"),
]


def concordance(item: dict) -> dict | None:
    v = item["valeur"].replace(" ", " ")
    # Toutes les entrées compatibles sont recherchées ; la plus spécifique (motif le plus proche
    # de la valeur dans le contexte) l'emporte, pour éviter qu'un motif générique capte la valeur.
    best = None
    for valeur, ctx, src, cit in C:
        if v != valeur:
            continue
        m = re.search(ctx, item["contexte"], re.I)
        if not m:
            continue
        pos = item["_pos"]
        # distance entre le motif et la valeur ; un motif qui contient la valeur vaut 0
        dist = 999 if ctx == "." else (0 if m.start() <= pos <= m.end() else min(abs(m.start() - pos), abs(m.end() - pos)))
        key = (dist, -(m.end() - m.start()))
        if best is None or key < best[0]:
            best = (key, {"source": src, "citation": cit})
    return best[1] if best else None


# ------------------------------------------------------------ recalculs
def r(id_, attendu, trouve, formule, source, tol, note="", ancre=""):
    ecart = None if (attendu is None or trouve is None) else round(trouve - attendu, 4)
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
    return {"id": id_, "ancre": ancre, "attendu": attendu, "trouve": trouve, "ecart": ecart, "tolerance": tol,
            "verdict": verdict, "formule": formule, "source": source, "note": note}


def ic_coherent(hr, lo, hi):
    """Moyenne géométrique des bornes d'un IC à 95 % ≈ estimation ponctuelle (échelle log)."""
    return round(math.sqrt(lo * hi), 2)


def recalculs() -> list[dict]:
    R = []
    pct = lambda a, b: round(100 * a / b, 1)
    # Kasanmoentalib 2010 (S5)
    R.append(r("R01", pct(26, 577), 5.0, "26/577 hydrocéphalies", "S5", 0.5, "4,5 % arrondi à 5 % par la source", "g94-2"))
    R.append(r("R02", pct(18, 26), 69.0, "18/26 présentes à l'admission", "S5", 0.5, "", "g94-2"))
    R.append(r("R03", pct(14, 26), 54.0, "14/26 S. pneumoniae", "S5", 0.5, "", "g94-4"))
    R.append(r("R04", pct(4, 26), 15.0, "4/26 L. monocytogenes", "S5", 0.5, "", "g94-4"))
    R.append(r("R05", pct(13, 26), 50.0, "13/26 décès", "S5", 0, "", "g94-10"))
    R.append(r("R06", pct(18, 26), 69.0, "18/26 évolution défavorable", "S5", 0.5, "", "g94-10"))
    R.append(r("R07", pct(2, 26), 8.0, "2/26 ponctions lombaires répétées", "S5", 0.5, "", "g94-meningite-hydro"))
    R.append(r("R08", pct(4, 26), 15.0, "4/26 drains ventriculaires externes", "S5", 0.5, "", "g94-meningite-hydro"))
    R.append(r("R09", pct(4, 577), 15.0,
               "« dans la méningite bactérienne, 15 % des patients ont reçu une dérivation externe » : 4/577 épisodes = 0,7 %",
               "S5 (dénominateur réel : 26 patients hydrocéphales)", 0.5,
               "dénominateur faux dans l'îlot g94-8 : 15 % et 8 % se rapportent aux 26 hydrocéphalies, non aux méningites (voir C07)",
               "g94-8"))
    R.append(r("R10", pct(2, 577), 8.0, "8 % de ponctions répétées rapportés à toutes les méningites : 2/577 = 0,3 %",
               "S5", 0.5, "même erreur de dénominateur (C07)", "g94-8"))
    R.append(r("R11", 2 + 4, 6.0, "2 + 4 patients traités = 6 interventions", "S5 « Six patients underwent an intervention »", 0, "", "g94-meningite-hydro"))
    R.append(r("R12", ic_coherent(7.81, 2.91, 20.8), 7.81, "√(2,91 × 20,8) ≈ OR", "S5", 0.05, "IC cohérent sur l'échelle log", "g94-meningite-hydro"))
    # Sonneville 2023 (S2), OUTCOMEREA (S4)
    R.append(r("R13", pct(27, 50), 54.0, "27/50 patients non sédatés", "S2", 0, "", "g94-2"))
    R.append(r("R14", round(100 - 83, 1), 17.0, "complément 100 − 83 (premières cytologies négatives)", "S6", 0, "", "g94-e-3"))
    R.append(r("R14b", round(100 - 60.5, 1), 39.5, "complément 100 − 60,5", "S6", 0, "", "g94-e-3"))
    R.append(r("R15", ic_coherent(3.37, 2.82, 4.03), 3.37, "√(2,82 × 4,03) ≈ HR GCS 3–8", "S2", 0.03, "", "g94-gcs"))
    R.append(r("R16", None, 1.38, "HR GCS 13–14 = 1,38 ; IC publié 1,09–1,38 (borne haute = estimation : coquille de la source)",
               "S2", 0, "la leçon ne reprend pas l'IC : aucune erreur dans la leçon ; ne pas recopier l'IC", "g94-gcs"))
    R[-1]["verdict"] = "NON_VERIFIABLE"
    for i, (hr, lo, hi, lab) in enumerate([(1.77, 1.34, 2.34, "pression"), (1.78, 1.20, 2.63, "oxygénation"),
                                            (1.46, 1.12, 1.91, "température"), (1.41, 1.10, 1.80, "glycémie")]):
        R.append(r(f"R17{chr(97 + i)}", ic_coherent(hr, lo, hi), hr, f"√(IC) ≈ aHR {lab}", "S4", 0.02, "", "g94-cibles"))
    R.append(r("R18", 3 * 200, 600.0, "3 × 200 mg = 600 mg/j (EFNS)", "S7", 0, "", "g94-p-2"))
    R.append(r("R18b", round(600 / 200, 1), None, "rapport EFNS / FI parentérale = 3", "S7, S10", 0, "", "g94-thiamine"))
    R.append(r("R18c", 3 * 500, None, "ESPEN 2022 : encéphalopathie d'étiologie incertaine dont Wernicke, 500 mg × 3 = 1500 mg/j IV",
               "S12 (tableau 8)", 0, "dose européenne la plus récente, absente de la leçon (C03)", "g94-p-2"))
    R.append(r("R18d", 200.0, 200.0, "plafond FI parentéral « doses quotidiennes pouvant atteindre 200 mg »", "S10", 0, "", "g94-thiamine"))
    R.append(r("R18e", 300.0, 200.0,
               "« au plus 200 mg par jour (information professionnelle suisse) » présenté comme plafond global : la FI admet 200–300 mg/j per os dans l'hypovitaminose grave",
               "S10 (Posologie, Traitement)", 0, "plafond inexact hors voie parentérale (C03)", "g94-12"))
    R.append(r("R18f", math.ceil(1500 / 100), None, "1500 mg/j = 15 ampoules Benerva 100 mg/1 mL ; 600 mg/j = 6 ampoules", "S10 (Présentation : ampoules 1 mL à 100 mg, boîte de 6)", 0, "", "g94-p-2"))
    R.append(r("R19", round(4200 / KJ_PER_KCAL, 0), None, "4200 kJ ÷ 4,184 = 1004 kcal ≈ 1000 kcal", "S10 ; facteur 1 kcal = 4,184 kJ", 0,
               "conversion utile au lecteur (0,4 mg/1000 kcal)", "g94-3"))
    R.append(r("R20", 0.15 * 4, None, "dexaméthasone enfant 0,15 mg/kg × 4/j = 0,6 mg/kg/j ; × 4 j = 2,4 mg/kg", "S11", 0, "", "g94-p-2"))
    R.append(r("R20b", 0.4 * 2, None, "0,4 mg/kg × 2/j = 0,8 mg/kg/j ; × 2 j = 1,6 mg/kg", "S11", 0, "", "g94-p-2"))
    R.append(r("R20c", round(0.15 * 20, 2), None, "exemple 20 kg : 3 mg par dose toutes les 6 h", "S11", 0, "", "g94-p-2"))
    R.append(r("R21", 4 * 4, None, "dexaméthasone adulte, entretien 4 mg × 4/j = 16 mg/j après 8–12 mg", "S11", 0, "", "g94-p-2"))
    R.append(r("R21b", 10 * 4 * 4, None, "méningite bactérienne de l'adulte : 10 mg × 4/j × 4 j = 160 mg (absent de la leçon)", "S13", 0, "C05", "g94-p-2"))
    # Conversions d'unités des cibles (Sonneville, tableau 2)
    R.append(r("R22", round(80 / MMHG_PER_KPA, 1), None, "PaO₂ 80 mmHg = 10,7 kPa", "conversion", 0, "", "g94-cibles"))
    R.append(r("R22b", round(120 / MMHG_PER_KPA, 1), None, "PaO₂ 120 mmHg = 16,0 kPa", "conversion", 0, "", "g94-cibles"))
    R.append(r("R22c", round(35 / MMHG_PER_KPA, 2), None, "PaCO₂ 35 mmHg = 4,67 kPa", "conversion", 0, "", "g94-cibles"))
    R.append(r("R22d", round(45 / MMHG_PER_KPA, 2), None, "PaCO₂ 45 mmHg = 6,00 kPa", "conversion", 0, "", "g94-cibles"))
    R.append(r("R23", 7 * 10, None, "hémoglobine 7 g/dL = 70 g/L (unité des laboratoires suisses)", "conversion", 0, "C13", "g94-9"))
    R.append(r("R24", round(5 * GLUCOSE_MG_DL_PER_MMOL), None, "glycémie 5 mmol/L = 90 mg/dL", "conversion", 0, "", "g94-cibles"))
    R.append(r("R24b", round(10 * GLUCOSE_MG_DL_PER_MMOL), None, "glycémie 10 mmol/L = 180 mg/dL", "conversion", 0, "", "g94-cibles"))
    R.append(r("R24c", round(3 * GLUCOSE_MG_DL_PER_MMOL), None, "hypoglycémie < 3 mmol/L = 54 mg/dL", "conversion", 0, "", "g94-cibles"))
    R.append(r("R25", round(200 / MMH2O_PER_MMHG, 1), None, "pression d'ouverture 200 mm H₂O = 14,7 mmHg = 20 cm H₂O", "conversion", 0, "", "g94-lcr-ml"))
    R.append(r("R26", round(600 / 1000 / GLUCOSE_MW * 1000, 2), None,
               "glucose du LCS < 600 mg/L (S6) = 3,33 mmol/L : valeur physiologiquement plausible comme seuil bas",
               "S6 + masse molaire 180,16 g/mol", 0, "la leçon juge la valeur « erronée » sans preuve (C15)", "g94-lcr-ml"))
    R.append(r("R26b", 0.5, None, "protéines 500 mg/L = 0,5 g/L", "conversion", 0, "", "g94-e-3"))
    # EANO-ESMO (S6)
    for i, (k, v, lab) in enumerate([(9, 5.0, "infections"), (25, 13.0, "hygromes/hématomes"), (12, 6.3, "symptomatiques"),
                                      (9, 5.0, "dysfonctions"), (15, 8.0, "externalisation/retrait/révision"),
                                      (150, 79.0, "sans complication")]):
        R.append(r(f"R27{chr(97 + i)}", pct(k, 190), v, f"{k}/190 {lab}", "S6", 0.5, "", "g94-dvp"))
    R.append(r("R27g", 100 - 79, None, "patients avec ≥ 1 complication = 21 % ; somme des catégories 5 + 13 + 5 + 8 = 31 % (catégories non exclusives)",
               "S6", 0, "ne pas additionner les complications", "g94-dvp"))
    R.append(r("R28", pct(63, 318), 20.0, "63/318 survivantes > 1 an", "S6", 0.5, "", "g94-10"))
    R.append(r("R29", 3.8, 4.0, "Pareto « 4 à 8 mois » : borne basse source 3,8", "S6", 0.25, "arrondi (C16)", "pareto-g94-suivi"))
    R.append(r("R29b", 8.1, 8.0, "Pareto « 4 à 8 mois » : borne haute source 8,1", "S6", 0.25, "arrondi (C16)", "pareto-g94-suivi"))
    # Seuils et cohérences
    R.append(r("R30", 1.0, 1.0, "céfépime : 7,7 < 20 < 38,1 mg/L (ordre des seuils)", "S2", 0,
               "", "g94-cefepime"))
    R[-1]["trouve"] = 1.0 if 7.7 < 20 < 38.1 else 0.0
    R.append(r("R31", 1.0, 1.0 if 3 <= 9 <= 15 else 0.0, "GCS du cas 1 (9) dans l'échelle 3–15 ; catégorie 9–12 (ni 3–8 ni 13–14)", "S2, S15", 0,
               "le cas n'appartient à aucune des deux strates de HR citées", "g94-0"))
    R.append(r("R32", round(0.542 / (1 - 0.83), 2), None, "RV+ de l'énolase = 0,542 / 0,17 = 3,19", "S2", 0, "discrimination faible, conforme à la leçon", "g94-e-1"))
    R.append(r("R32b", round((1 - 0.542) / 0.83, 2), None, "RV− de l'énolase = 0,458 / 0,83 = 0,55", "S2", 0, "", "g94-e-1"))
    R.append(r("R33", round(100 * 0.4 / 4200 * 4200, 1), None, "besoin 0,4 mg par 4200 kJ produits ; pour 8400 kJ de glucides : 0,8 mg", "S10", 0, "", "g94-3"))
    R.append(r("R34", 4.0, 4.0, "Wernicke : 4 critères EFNS/Caine, seuil 2", "S7", 0, "", "g94-12"))
    R.append(r("R35", pct(883, 995), None, "883/995 = 88,7 % avec au moins une agression systémique (non écrit dans la leçon)", "S4", 0, "", "g94-cibles"))
    R.append(r("R36", 1.0, 1.0, "méningite : 26 hydrocéphalies ; 69 % = 18 ; 54 % = 14 ; 15 % = 4 ; 50 % = 13 (cohérence des effectifs)", "S5", 0, "", "g94-meningite-hydro"))
    R.append(r("R37", 600.0, 600.0, "texte p-2 « 600 mg par jour répartis en trois prises »", "S7", 0, "", "g94-p-2"))
    return R


def main() -> int:
    items = inventaire()
    for it in items:
        if it["categorie"] == "GRANDEUR":
            c = concordance(it)
            if c:
                it["controle"] = "CONCORDANCE_SOURCE" if c["source"] not in ("VIGNETTE", "RECALCUL", "LACUNE", "DATE") else c["source"]
                it.update(c)
            else:
                it["controle"] = "NON_RAPPROCHE"
        else:
            it["controle"] = "NON_CALCULABLE"
    for it in items:
        it.pop("_pos", None)
    R = recalculs()
    (HERE / "inventaire.json").write_text(json.dumps({
        "total_releves": len(items),
        "grandeurs": sum(i["categorie"] == "GRANDEUR" for i in items),
        "non_calculables": sum(i["categorie"] != "GRANDEUR" for i in items),
        "concordance_source": sum(i.get("controle") == "CONCORDANCE_SOURCE" for i in items),
        "vignettes": sum(i.get("controle") == "VIGNETTE" for i in items),
        "renvoi_recalcul": sum(i.get("controle") == "RECALCUL" for i in items),
        "non_rapproches": sum(i.get("controle") == "NON_RAPPROCHE" for i in items),
        "items": items}, ensure_ascii=False, indent=1), encoding="utf-8")
    calculables = [x for x in R if x["verdict"] != "INFORMATIF"]
    stats = {k: sum(x["verdict"] == k for x in R) for k in ("CORRECT", "ARRONDI", "FAUX", "NON_VERIFIABLE", "INFORMATIF")}
    (HERE / "resultats.json").write_text(json.dumps({
        "calculables": len(calculables), "recalcules": len(calculables), "verdicts": stats, "resultats": R},
        ensure_ascii=False, indent=1), encoding="utf-8")
    nr = [i for i in items if i.get("controle") == "NON_RAPPROCHE"]
    print(f"relevés {len(items)} ; non rapprochés {len(nr)} ; recalculs {len(R)} ; {stats}")
    for i in nr:
        print(" NR", i["id"], i["fichier"].split('/')[-1], i["ancre"], "|", i["contexte"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
