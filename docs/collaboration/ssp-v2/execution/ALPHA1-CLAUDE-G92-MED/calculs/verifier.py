#!/usr/bin/env python3
"""Audit ALPHA77 G92 — inventaire scripté et recalcul de toutes les grandeurs de la leçon.

Exécution (depuis la racine du dépôt) :
    python3 docs/collaboration/ssp-v2/execution/ALPHA1-CLAUDE-G92-MED/calculs/verifier.py [--cache DOSSIER]

Sorties (dans le dossier du script) : inventaire.json, resultats.json.
Lecture seule des 7 fichiers canoniques ; aucune écriture hors de calculs/.

Familles de contrôles :
  1. RECALCUL : grandeur dérivable (grade d'après le score ICE et la vigilance selon la grille ASTCT,
     dose quotidienne et cumulée, plafond de dose par le poids, dénominateur d'un pourcentage,
     cohérence d'un intervalle, clairance de Cockcroft-Gault et DFGe CKD-EPI 2021, conversion d'unités).
  2. CONCORDANCE_SOURCE : valeur rapportée, comparée à la citation exacte de la source lue
     (Sx de sources.json) ; verdict CORRECT si la valeur figure dans la citation.
     Avec --cache, chaque citation est en outre recherchée mot pour mot dans la copie locale
     du texte de la source (champ citation_retrouvee).
  3. NON_CALCULABLE : identifiant (année, numéro d'îlot, de figure, de cas, de grade cité comme
     libellé, nom d'interleukine, de virus ou de marqueur) ; relevé mais sans objet de calcul.
"""
from __future__ import annotations

import argparse
import html
import json
import math
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
FILES = [
    "chapters/G92/G92_a.html", "chapters/G92/G92_b.html", "chapters/G92/G92_c.html",
    "chapters/G92/G92_d.html", "chapters/G92/G92_pop1.html", "chapters/G92/G92_pop2.html",
    "glossary/g92.py",
]
NUM = re.compile(r"(?<![\w.,\-])([+−]?(?:\d{1,3}(?:[   ]\d{3})+(?!\d)|\d+)(?:[.,]\d+)?)"
                 r"(?:\s?[–-]\s?(\d+(?:[.,]\d+)?))?")
UNIT = re.compile(r"^\s?(%|mL/min/1,73 m²|mL/min|mg/kg/jour|mg/kg|mg/jour|mg/L|mg|g|kg|/µL|heures|"
                  r"jours|jours|semaines|mois|ans|minutes|patients|cas|items|points|doses)")
CACHE = {  # copie locale du texte lu, pour vérifier mot pour mot chaque citation (option --cache)
    "S1": "bfarm.txt", "S2": "ussowicz.txt", "S3": "astct.txt", "S4": "fi_yescarta.txt",
    "S5": "fi_actemra.txt", "S6": "fi_cefepim.txt", "S7": "fi_holoxan.txt", "S8": "fi_depakine.txt",
    "S9": "fi_metro.txt", "S10": "fi_solumedrol.txt", "S11": "fi_dexa.txt", "S12": "fi_keppra.txt",
    "S13": "abstracts.txt", "S14": "abstracts.txt", "S15": "abstracts.txt", "S16": "abstracts.txt",
    "S17": "abstracts.txt", "S18": "abstracts.txt", "S19": "abstracts.txt", "S20": "abstracts.txt",
    "S21": "abstracts.txt", "S22": "abstracts.txt", "S23": "abstracts.txt",
    "S24": "abs_semio.txt", "S26": "abs_semio.txt", "S27": "abs_semio.txt", "S28": "rissardo.txt",
}


def texte(path: Path) -> list[tuple[str, str]]:
    """Renvoie [(ancre, texte)] : le texte est découpé par ancre (id, data-pop) la plus proche."""
    s = path.read_text(encoding="utf-8")
    if path.suffix == ".py":
        return [("glossary/g92.py", re.sub(r"\s+", " ", s))]
    s = re.sub(r"<svg.*?</svg>", lambda m: " " + " ".join(re.findall(r">([^<]+)<", m.group(0))) + " ",
               s, flags=re.S)
    parts, last, anchor = [], 0, path.name
    for m in re.finditer(r'(?:id|data-pop)="([^"]+)"', s):
        parts.append((anchor, s[last:m.start()]))
        anchor, last = m.group(1), m.end()
    parts.append((anchor, s[last:]))
    out = []
    for a, chunk in parts:
        t = re.sub(r"<[^>]+>", " ", chunk)
        t = re.sub(r"\s+", " ", html.unescape(t))
        out.append((a, t))
    return out


def val(x: str) -> float:
    return float(x.replace("−", "-").replace(",", ".").replace(" ", "").replace(" ", "").replace(" ", ""))


def classer(tok: str, avant: str, apres: str) -> str:
    v = tok.lstrip("+−")
    a = avant.rstrip()
    if re.fullmatch(r"(19|20)\d\d", v) and not re.match(r"\s?(%|patients|cas|mg)", apres):
        return "NON_CALCULABLE:date"
    if re.search(r"(Cycle|Figure|Cas|G|ZUMA-|CIM-|HHV-|CD|COVID-|CARTOX-|G92\.)$", a) or re.match(r"\.\d", apres):
        return "NON_CALCULABLE:identifiant"
    if re.search(r"(interleukines?|interleukine|l’interleukine|de l’interleukine)$", a) or re.match(r"\s?(alpha|,\s?8|, 8)", apres):
        return "NON_CALCULABLE:nom_de_molecule"
    if re.search(r"(nerf crânien|nerf)$", a) or re.match(r"\s?(Interleukine|interleukine)", apres):
        return "NON_CALCULABLE:identifiant"
    if re.search(r"(grade|grades|Grade|au grade|en grade|ICANS de grade)$", a):
        return "LIBELLE_GRADE"
    if re.search(r"(grade|grades|Grade) \d (ou|à|et)$", a):
        return "LIBELLE_GRADE"
    if re.search(r"Œdème$|— — —$|à l’imagerie$|de base$|scanner et EEG$|Paramètres clés\. Score ICE sur 10 : grade$", a) and re.fullmatch(r"[1-4]", v):
        return "LIBELLE_GRADE"
    if re.match(r"\s?[A-ZÉ]", apres) and re.fullmatch(r"\d+\.\d", v):
        return "NON_CALCULABLE:numero_section"
    if re.search(r"interleukines \d+(, \d+)*( et)?,?$", a) or re.search(r"interleukines 6, 8, 10 et$", a):
        return "NON_CALCULABLE:nom_de_molecule"
    if re.search(r"(Interleukine|interleukine)$", a) or re.search(r"numéro$|type$|différenciation$|'type$", a) or re.match(r"', 'numéro|', 'type|'\)\]", apres):
        return "NON_CALCULABLE:identifiant"
    if re.match(r"\s?(Grade|Dexaméthasone|Méthylprednisolone|Soins)", apres) and re.fullmatch(r"[1-4]", v):
        return "LIBELLE_GRADE"
    if re.match(r"\s?[A-ZÉŒ][a-zéèêàœ]", apres) and re.fullmatch(r"\d{1,2}(\.\d)?", v) and re.search(r"(\.|»|›|>|^)\s?$", avant[-3:] or "^"):
        return "NON_CALCULABLE:numero_ilot"
    if re.match(r"\s?(e\b|er\b|re\b)", apres) or re.search(r"(e-|p-)$", a):
        return "NON_CALCULABLE:identifiant"
    if avant.endswith("('"):
        return "NON_CALCULABLE:glossaire_lettre"
    return "GRANDEUR"


def inventaire() -> list[dict]:
    items, n = [], 0
    for f in FILES:
        for ancre, t in texte(ROOT / f):
            for m in NUM.finditer(t):
                n += 1
                avant, apres = t[max(0, m.start() - 45):m.start()], t[m.end():m.end() + 30]
                u = UNIT.match(apres)
                items.append({
                    "id": f"I{n:03d}", "fichier": f, "ancre": ancre, "valeur": m.group(0).strip(),
                    "unite": (u.group(1) if u else ""),
                    "contexte": (avant + m.group(0) + apres).strip(),
                    "categorie": classer(m.group(1), avant, apres),
                })
    return items


# ------------------------------------------------------------ concordance avec les sources lues
# (valeur telle qu'écrite dans la leçon, motif de contexte, source, citation exacte de la source)
C = [
    # vignettes pédagogiques (comparées au seuil dans les recalculs)
    ("64", r"femme de 64", "VIGNETTE", "âge d'un cas fictif"),
    ("2", r"Au jour 2", "VIGNETTE", "jour d'un cas fictif"),
    ("5", r"au jour 5, son|au jour 5, score|Au jour 5", "VIGNETTE", "jour d'un cas fictif"),
    ("8", r"ICE est de 8|ICE à 8|ICE de 8\. Quelle|ICE de 8 \(grade 1\) mais", "VIGNETTE", "score d'un cas fictif (recalcul R01, R02, R05)"),
    ("10", r"8 sur 10", "VIGNETTE", "score maximal de l'échelle (recalcul R07)"),
    ("82", r"homme de 82", "VIGNETTE", "âge d'un cas fictif (recalcul R13)"),
    ("24", r"estimé est de 24", "VIGNETTE", "DFGe d'un cas fictif (recalcul R13)"),
    ("1,73", r"mL/min/1,73", "UNITE", "surface corporelle de normalisation du DFGe (1,73 m²)"),
    ("3", r"Au jour 3, il", "VIGNETTE", "jour d'un cas fictif"),
    ("6", r"Au jour 6", "VIGNETTE", "jour d'un cas fictif"),
    ("5", r"tombe à 5", "VIGNETTE", "score d'un cas fictif (recalcul R03)"),
    ("10", r"dexaméthasone 10 mg par voie", "S2", "Administer dexamethasone 10–20 mg IV every 6 hours"),
    ("70", r"patient de 70 ans sous", "VIGNETTE", "âge d'un cas fictif (recalcul R14)"),
    ("25", r"glomérulaire de 25", "VIGNETTE", "DFGe d'un cas fictif (recalcul R14)"),
    ("1000", r"Débuter la méthylprednisolone 1000", "S2", "methylprednisolone 1000 mg/day for 3 days"),
    ("4", r"ICE de 4, éveillé", "VIGNETTE", "score d'un cas fictif (recalcul R04)"),
    # fréquences et chronologie
    ("20", r"20 à 60 %", "S2", "ICANS occurs in 20–60% of all CAR-T recipients"),
    ("60", r"20 à 60 %", "S2", "ICANS occurs in 20–60% of all CAR-T recipients"),
    ("3", r"concernent 3 à 30", "S2", "with severe (Grade ≥3) events in 3–30%"),
    ("30", r"3 à 30 %", "S2", "with severe (Grade ≥3) events in 3–30%"),
    ("64", r"ciloleucel 64", "S2", "Axicabtagene ciloleucel (Yescarta) CD19; LBCL, FL, MZL 93%; 9–11% G ≥ 3 64%; 28–32% G≥3"),
    ("28–32", r".", "S2", "64%; 28–32% G≥3"),
    ("69", r".", "S2", "69%; 31% G≥3"),
    ("31", r"autoleucel 69 % 31", "S2", "69%; 31% G≥3"),
    ("21–40", r".", "S2", "21–40%; 13% G ≥ 3"),
    ("13", r"21–40 % 13", "S2", "21–40%; 13% G ≥ 3"),
    ("27–30", r".", "S2", "27–30%; 10% G≥3"),
    ("10", r"27–30 % 10", "S2", "27–30%; 10% G≥3"),
    ("22,8", r".", "S2", "22.8%; 7.1% G ≥ 3"),
    ("7,1", r".", "S2", "22.8%; 7.1% G ≥ 3"),
    ("18", r"vicleucel 18", "S2", "18%; 3% G≥3"),
    ("3", r"18 % 3 %", "S2", "18%; 3% G≥3"),
    ("23–26", r".", "S2", "23–26%; 10% G≥3"),
    ("10", r"23–26 % 10", "S2", "23–26%; 10% G≥3"),
    ("62", r".", "S4", "Des effets indésirables neurologiques sont survenus chez 62% des patients dans ZUMA-1 et ZUMA-7"),
    ("25", r"plus chez 25", "S4", "sont survenus chez vingt-cinq (25%) des patients"),
    ("6", r"médian est de 6 jours|délai médian 6", "S4", "Le délai médian de survenue était de 6 jours (intervalle 1 à 133 jours)"),
    ("1", r"extrêmes 1 à", "S4", "Le délai médian de survenue était de 6 jours (intervalle 1 à 133 jours)"),
    ("133", r".", "S4", "Le délai médian de survenue était de 6 jours (intervalle 1 à 133 jours)"),
    ("10", r"durée médiane de 10", "S4", "La durée médiane était de 10 jours avec un intervalle de 1 à 817 jours"),
    ("56", r".", "S4", "Des effets indésirables neurologiques sont survenus chez 56% des patients dans ZUMA-5"),
    ("15", r"plus : 15", "S4", "sont survenus chez quinze (15%) des patients"),
    ("51", r".", "S4", "encéphalopathie (51%), céphalées (33%), tremblements (28%), sensation vertigineuse (22%), délire (13%)"),
    ("33", r"céphalées \(33", "S4", "encéphalopathie (51%), céphalées (33%), tremblements (28%), sensation vertigineuse (22%), délire (13%)"),
    ("28", r"tremblements \(28", "S4", "encéphalopathie (51%), céphalées (33%), tremblements (28%), sensation vertigineuse (22%), délire (13%)"),
    ("22", r"vertiges \(22", "S4", "encéphalopathie (51%), céphalées (33%), tremblements (28%), sensation vertigineuse (22%), délire (13%)"),
    ("13", r"délire \(13", "S4", "encéphalopathie (51%), céphalées (33%), tremblements (28%), sensation vertigineuse (22%), délire (13%)"),
    ("0,3", r".", "S4", "l'état de mal épileptique (0,3%)"),
    ("5", r"environ 5 jours|moyenne vers le jour 5|débute vers le jour 5|vers le jour 5 \(|Début vers le jour 5|début vers le jour 5|Le début vers le jour 5|jour 5 et le pic", "S2", "Onset of ICANS occurs on average approximately 5 days following CAR-T infusion"),
    ("10", r"environ 10 %", "S2", "in approximately 10% of cases — more than 3 weeks after CRS"),
    ("7", r"entre le jour 7 et le jour 30", "S2", "typically manifest within the first 7–30 days post-infusion"),
    ("30", r"jour 7 et le jour 30", "S2", "typically manifest within the first 7–30 days post-infusion"),
    ("6", r"jusqu’à 6 à 8", "S2", "can present up to 6–8 weeks after CAR-T infusion"),
    ("8", r"6 à 8 semaines", "S2", "can present up to 6–8 weeks after CAR-T infusion"),
    ("877", r".", "S17", "real-world setting for large B-cell lymphoma, as captured in the Center for International Blood and Marrow Transplant Research (CIBMTR) Registry (n = 877)"),
    ("95", r"retrouve 95", "S17", "Of 150 patients with reported onset date, 95% had onset ≤day 15 after infusion (recalcul R18 : dénominateur)"),
    ("15", r"dans les 15 premiers", "S17", "95% had onset ≤day 15 after infusion"),
    ("5,5", r".", "S17", "median time to resolution was 5.5 days"),
    ("73", r".", "S14", "including 73 cases of cefepime-induced neurotoxicity"),
    ("52", r".", "S14", "Individuals aged 65 and older accounted for most cefepime-induced neurotoxicity cases (52%)"),
    ("65", r"65 ans", "S14", "Individuals aged 65 and older accounted for most cefepime-induced neurotoxicity cases (52%)"),
    ("2", r"entre le jour 2 et le jour 5|jours 2 à 5", "S14", "Most cases of cefepime-induced neurotoxicity occurred between days two and five (n=29, 71%)"),
    ("5", r"jour 2 et le jour 5|jours 2 à 5", "S14", "Most cases of cefepime-induced neurotoxicity occurred between days two and five (n=29, 71%)"),
    ("71", r".", "S14", "occurred between days two and five (n=29, 71%) (recalcul R15 : dénominateur)"),
    ("85", r"85 %", "S14", "most resolution occurred between days one and five (n=29, 85%) (recalcul R15 : dénominateur)"),
    ("1", r"en 1 à 5 jours", "S14", "most resolution occurred between days one and five (n=29, 85%)"),
    ("5", r"en 1 à 5 jours", "S14", "most resolution occurred between days one and five (n=29, 85%)"),
    ("7", r"au jour 7 :", "S4", "Chez 75% des patients les effets indésirables neurologiques sont survenus dans les 7 premiers jours après la perfusion"),
    # physiopathologie
    ("7", r"jour 7 et le jour 14|jours 7 et 14|jours 7 à 14", "S2", "Peak cytokine levels typically occur within 7–14 days of infusion"),
    ("14", r"jour 7 et le jour 14|jours 7 et 14|jours 7 à 14", "S2", "Peak cytokine levels typically occur within 7–14 days of infusion"),
    ("14", r"dans les 14 premiers", "S4", "Un pic d'élévation a été observé au cours des 14 premiers jours après la perfusion"),
    ("28", r"en 28 jours", "S4", "les taux étaient généralement revenus aux valeurs initiales en 28 jours"),
    ("68", r"68 %", "S6", "Pendant une hémodialyse d'une durée de 3 heures, environ 68 % de la quantité totale de céfépime présente dans l'organisme au début est éliminée"),
    ("3", r"hémodialyse de 3 heures", "S6", "Pendant une hémodialyse d'une durée de 3 heures"),
    # causes
    ("30", r"inférieur à 30 mL|Débit inférieur à 30", "S13", "estimated glomerular filtration rate (eGFR) < 30 mL/min/1.73 m2 is the primary factor in CIN, with an odds ratio of 10.06"),
    ("10,06", r".", "S13", "with an odds ratio of 10.06 (95% confidence interval [CI] = 5.05-20.03"),
    ("10", r"rapport de cotes 10\)", "S13", "with an odds ratio of 10.06 (arrondi à l'unité)"),
    ("95", r"confiance à 95", "S13", "95% confidence interval [CI] = 5.05-20.03"),
    ("5,05", r".", "S13", "95% confidence interval [CI] = 5.05-20.03"),
    ("20,03", r".", "S13", "95% confidence interval [CI] = 5.05-20.03"),
    ("20", r"creux de 20", "S13", "the proposed trough concentration (Ctrough) threshold for intermittent infusion is 20 mg/L"),
    ("63", r".", "S13", "the steady-state concentration (Css) threshold for continuous infusion is 63 mg/L"),
    # anamnèse, examen
    ("19", r"chez 19 des", "S3", "developing in 19 of 22 patients who went on to develop severe neurotoxicity"),
    ("22", r"19 des 22", "S3", "developing in 19 of 22 patients who went on to develop severe neurotoxicity"),
    ("8", r"toutes les 8 à 12", "S2", "ICE screening every 8–12 hours is recommended during the acute post-infusion period"),
    ("12", r"8 à 12 heures", "S2", "ICE screening every 8–12 hours is recommended during the acute post-infusion period"),
    ("0", r"ICE de 0 à 2", "S3", "7–9 3–6 0–2 0 (patient is unarousable and unable to perform ICE)"),
    ("2", r"ICE de 0 à 2", "S3", "7–9 3–6 0–2 0 (patient is unarousable and unable to perform ICE)"),
    ("5", r"plus de cinq|plus de 5 minutes", "S3", "Life-threatening prolonged seizure (>5 min)"),
    # œdème
    ("1,6", r".", "S4", "s'est élevé à 1,6% au total (0,8% de cas fatals), par rapport à 0,7% au total (0,2% de cas fatals)"),
    ("0,8", r".", "S4", "s'est élevé à 1,6% au total (0,8% de cas fatals), par rapport à 0,7% au total (0,2% de cas fatals)"),
    ("0,7", r".", "S4", "s'est élevé à 1,6% au total (0,8% de cas fatals), par rapport à 0,7% au total (0,2% de cas fatals)"),
    ("0,2", r".", "S4", "s'est élevé à 1,6% au total (0,8% de cas fatals), par rapport à 0,7% au total (0,2% de cas fatals)"),
    # traitement
    ("10", r"10 à 20 mg", "S2", "Administer dexamethasone 10–20 mg IV every 6 hours"),
    ("20", r"10 à 20 mg", "S2", "Administer dexamethasone 10–20 mg IV every 6 hours"),
    ("6", r"toutes les 6 heures", "S2", "Administer dexamethasone 10–20 mg IV every 6 hours"),
    ("3", r"ICE 3 à 4 fois", "S2", "Increase ICE score neuromonitoring (e.g., 3-4x/d)"),
    ("4", r"ICE 3 à 4 fois", "S2", "Increase ICE score neuromonitoring (e.g., 3-4x/d)"),
    ("1000", r"1000 mg par jour", "S2", "Administer methylprednisolone 1000 mg/day for 3 days"),
    ("3", r"pendant 3 jours", "S2", "Administer methylprednisolone 1000 mg/day for 3 days"),
    ("250", r".", "S2", "taper at 250 mg every 12 hrs for 2 days, then 125 mg every 12 hrs for 2 days, then 60 mg every 12 hrs for 2 days (recalcul R08)"),
    ("12", r"250 mg toutes les 12", "S2", "taper at 250 mg every 12 hrs for 2 days"),
    ("2", r"pendant 2 jours", "S2", "for 2 days, then 125 mg every 12 hrs for 2 days, then 60 mg every 12 hrs for 2 days"),
    ("125", r".", "S2", "then 125 mg every 12 hrs for 2 days (recalcul R08 : « toutes les 12 heures » omis)"),
    ("60", r"60 mg pendant", "S2", "then 60 mg every 12 hrs for 2 days (recalcul R08 : « toutes les 12 heures » omis)"),
    ("3", r"grade 3 ou 4 après|Après 3 jours", "S2", "failure to improve Grade (3/)4 ICANS after 3 days of high-dose steroids"),
    ("12", r"12 mg/kg/jour", "S2", "High-dose IV anakinra (up to 12 mg/kg/day, typically 800 mg/day)"),
    ("800", r"800 mg/jour", "S2", "High-dose IV anakinra (up to 12 mg/kg/day, typically 800 mg/day)"),
    ("77", r".", "S2", "with an overall response rate of 77%"),
    ("50", r"hydrocortisone 50|Hydrocortisone 50", "S2", "Intrathecal triple therapy (hydrocortisone 50 mg + methotrexate 12 mg + cytarabine 50 mg)"),
    ("12", r"méthotrexate 12", "S2", "Intrathecal triple therapy (hydrocortisone 50 mg + methotrexate 12 mg + cytarabine 50 mg)"),
    ("50", r"cytarabine 50", "S2", "Intrathecal triple therapy (hydrocortisone 50 mg + methotrexate 12 mg + cytarabine 50 mg)"),
    ("50", r"50 mL/min", "S6", "clairance de la créatinine ≤50 ml/min"),
    ("48", r"48 à 72", "S7", "dans la plupart des cas, se résoudre dans les 48 à 72 heures suivant l’arrêt de l’ifosfamide"),
    ("72", r"48 à 72", "S7", "dans la plupart des cas, se résoudre dans les 48 à 72 heures suivant l’arrêt de l’ifosfamide"),
    ("8", r"Tocilizumab 8 mg|8 mg/kg \(30", "S5", "est de 8 mg/kg chez les patients d'un poids de 30 kg ou plus et de 12 mg/kg chez ceux pesant moins de 30 kg"),
    ("30", r"\(30 kg|moins de 30 kg", "S5", "est de 8 mg/kg chez les patients d'un poids de 30 kg ou plus et de 12 mg/kg chez ceux pesant moins de 30 kg"),
    ("12", r"ou 12 mg/kg", "S5", "est de 8 mg/kg chez les patients d'un poids de 30 kg ou plus et de 12 mg/kg chez ceux pesant moins de 30 kg"),
    ("60", r"sur 60 minutes", "S5", "par perfusion intraveineuse sur 60 minutes"),
    ("3", r"jusqu’à 3 doses", "S5", "il peut être administré jusqu'à 3 doses supplémentaires d'Actemra"),
    ("8", r"au moins 8 heures", "S5", "Un intervalle d'au moins 8 heures doit être respecté entre chaque dose"),
    ("800", r"800 mg par perfusion|maximum 800", "S5", "Il n'est pas recommandé d'utiliser des doses supérieures à 800 mg par perfusion chez les patients atteints d'un SRC"),
    ("4", r"au plus 4 doses", "S5", "il peut être administré jusqu'à 3 doses supplémentaires d'Actemra ‖ 1 + 3 = 4 (recalcul R11)"),
    ("7", r"au moins 7 jours|moins 7 jours", "S4", "doivent être surveillés quotidiennement chez les patients pendant au moins 7 jours après la perfusion"),
    ("2", r"au moins 2 semaines", "S4", "rester à proximité d'un centre de traitement qualifié ... pendant au moins 2 semaines ; s'abstenir de conduire ... pendant au moins 2 semaines"),
    ("75", r".", "S4", "Chez 75% des patients les effets indésirables neurologiques sont survenus dans les 7 premiers jours après la perfusion"),
    ("7", r"6 à 7 jours", "S4", "Le délai médian de survenue était de 7 jours (intervalle: 1 à 177 jours)"),
    ("7", r"dans les 7 jours", "S4", "Chez 75% des patients les effets indésirables neurologiques sont survenus dans les 7 premiers jours"),
    ("1", r"méthylprednisolone 1 g", "S2", "methylprednisolone 1000 mg/day for 3 days ‖ 1 g = 1000 mg"),
    # pronostic, suivi
    ("66", r".", "S4", "les symptômes s'étant atténués chez 66% des patients dans les 3 semaines après la perfusion"),
    ("3,6", r".", "S4", "à l'exception de 10 patients (3,6% des patients traités par YESCARTA dans ZUMA-1 et ZUMA-7)"),
    ("200", r"200", "S2", "for at least 6 months and until CD4 count exceeds 200 cells/μL"),
    ("12", r"12 à 18", "S23", "structured outpatient follow-up for at least 12-18 months"),
    ("18", r"12 à 18", "S23", "structured outpatient follow-up for at least 12-18 months"),
    ("100", r"100 mg", "S15", "(100 mg subcutaneously on days 0 to +6 post-infusion)"),
    ("0", r"jour 0 au", "S15", "(100 mg subcutaneously on days 0 to +6 post-infusion)"),
    ("6", r"au jour 6", "S15", "(100 mg subcutaneously on days 0 to +6 post-infusion)"),
    ("80", r"80 patients", "S15", "We retrospectively analyzed 80 patients with B-cell lymphomas"),
    ("35", r".", "S15", "The incidence of ICANS was similar between groups (14 patients, 35%) with anakinra vs. 10 (25%)"),
    ("25", r"contre 25", "S15", "(14 patients, 35%) with anakinra vs. 10 (25%) in the standard cohort (p = 0.464)"),
    ("0,464", r".", "S15", "in the standard cohort (p = 0.464)"),
    ("26", r"26 patients", "S16", "This study analyzed outcomes of 26 r/r BCL patients aged ≥ 70 years ... comparing those who received prophylactic Tocilizumab (N = 7) versus standard treatment (N = 19) (recalcul R17)"),
    ("70", r"70 ans", "S16", "26 r/r BCL patients aged ≥ 70 years"),
    ("0,039", r".", "S16", "experienced significantly fewer therapy-related complications (p = 0.039)"),
    # pédiatrie
    ("12", r"avant 12 ans|moins de 12 ans", "S3", "For children <12 years, the Cornell Assessment of Pediatric Delirium (CAPD) (36, 37) (Table 7) is recommended"),
    ("0", r"de 0 à 21", "S2", "applicable from birth to 21 years"),
    ("21", r"0 à 21", "S2", "applicable from birth to 21 years"),
    ("9", r"score de 9 ou plus", "S3", "A CAPD score of ≥9 is suggestive of delirium and should be considered as grade 3 ICANS"),
    # grille ICE
    ("10", r"sur 10|10 points|Score ICE sur 10", "S3", "Score 10: No impairment ‖ 4 + 3 + 1 + 1 + 1 points (recalcul R07)"),
    ("10", r"score de 10 correspond|10/10", "S3", "Score 10: No impairment"),
    ("7", r"7 à 9", "S3", "Score 7–9: Grade 1 ICANS"),
    ("9", r"7 à 9", "S3", "Score 7–9: Grade 1 ICANS"),
    ("3", r"3 à 6", "S3", "7–9 3–6 0–2"),
    ("6", r"3 à 6", "S3", "7–9 3–6 0–2"),
    ("0", r"0 à 2", "S3", "7–9 3–6 0–2"),
    ("2", r"0 à 2", "S3", "7–9 3–6 0–2"),
    ("0", r"0 non évaluable|= 0 ou non|4 0 \(non", "S3", "0 (patient is unarousable and unable to perform ICE) (recalcul R06)"),
    ("7–9", r".", "S3", "7–9 3–6 0–2"),
    ("3–6", r".", "S3", "7–9 3–6 0–2"),
    ("0–2", r".", "S3", "7–9 3–6 0–2"),
    ("2–3", r".", "S2", "Grade 2 ... Grade 3 ... Administer dexamethasone 10–20 mg IV every 6 hours"),
    ("3–4", r".", "S2", "methylprednisolone 1000 mg/day for 3 days until improvement to Grade 1 ‖ tableau 3, grades 3 et 4"),
    # glossaire
    ("200", r"200/µL", "S2", "until CD4 count exceeds 200 cells/μL"),
    ("9", r"score de 9", "S3", "A CAPD score of ≥9 is suggestive of delirium"),
]


def concordance(item: dict) -> dict | None:
    for v, motif, src, cit in C:
        if item["valeur"] == v and re.search(motif, item["contexte"]):
            return {"source": src, "citation": cit,
                    "verdict": "CORRECT" if src not in ("VIGNETTE", "UNITE") else "VIGNETTE"}
    return None


# ------------------------------------------------------------ recalculs
def grade_ice(ice: int | None, eveil: str, crise: str = "aucune", moteur: bool = False, oedeme: str = "aucun") -> int:
    """Grade ICANS adulte selon la grille ASTCT [S3, tableau 6] : le paramètre le plus sévère l'emporte."""
    g = 0
    if ice is not None:
        g = max(g, 1 if 7 <= ice <= 9 else 2 if 3 <= ice <= 6 else 3 if 0 <= ice <= 2 else 0)
    g = max(g, {"spontane": 1 if g else 0, "voix": 2, "tactile": 3, "inaccessible": 4}[eveil])
    g = max(g, {"aucune": 0, "breve": 3, "eeg_resolutive": 3, "prolongee": 4}[crise])
    if moteur:
        g = max(g, 4)
    g = max(g, {"aucun": 0, "focal": 3, "diffus": 4}[oedeme])
    return g


def cockcroft_umol(age: float, poids: float, creat_umol: float, femme: bool = False) -> float:
    """Clairance de la créatinine (mL/min), créatinine en µmol/L : (140 − âge) × poids × 1,23 (× 0,85 femme) / créat."""
    return (140 - age) * poids * 1.23 * (0.85 if femme else 1.0) / creat_umol


def ckd_epi_2021(age: float, creat_umol: float, femme: bool = False) -> float:
    """DFGe CKD-EPI 2021 sans coefficient ethnique (mL/min/1,73 m²) ; créatinine convertie ÷ 88,4."""
    scr = creat_umol / 88.4
    k, a = (0.7, -0.241) if femme else (0.9, -0.302)
    return 142 * min(scr / k, 1) ** a * max(scr / k, 1) ** -1.200 * 0.9938 ** age * (1.012 if femme else 1.0)


def cefepime_fi(clcr: float, tres_grave: bool = False) -> tuple[float, int]:
    """Posologie d'entretien de l'IP suisse Cefepim Leman [S6] : (dose en g, intervalle en h)."""
    if clcr > 50:
        return (2, 8) if tres_grave else (2, 12)
    if clcr >= 30:
        return (2, 12) if tres_grave else (2, 24)
    if clcr >= 11:
        return (2, 24) if tres_grave else (1, 24)
    return (1, 24) if tres_grave else (0.5, 24)


def r(id_, attendu, trouve, verdict, formule, source, fichier, ancre, note=""):
    ecart = None
    if isinstance(attendu, (int, float)) and isinstance(trouve, (int, float)):
        ecart = round(trouve - attendu, 4)
    return {"id": id_, "attendu": attendu, "trouve": trouve, "ecart": ecart, "verdict": verdict,
            "formule": formule, "source": source, "fichier": fichier, "ancre": ancre, "note": note}


def recalculs() -> list[dict]:
    R = []
    g = grade_ice(8, "spontane")
    R.append(r("R01", 1, g, "CORRECT" if g == 1 else "FAUX", "ICE 8, éveil spontané → grade selon ASTCT",
               "S3 tableau 6", "chapters/G92/G92_a.html", "g92-0", "Vignette : grade 1 attendu ; la leçon conclut au grade 1 en g92-11."))
    g = grade_ice(8, "spontane", crise="breve")
    R.append(r("R02", 3, g, "CORRECT" if g == 3 else "FAUX", "ICE 8 + crise clinique brève → paramètre le plus sévère",
               "S3 tableau 6 et note ‡", "chapters/G92/G92_a.html", "g92-6", "La leçon écrit « au moins en grade 3 » : exact (grade 4 si crise prolongée)."))
    g = grade_ice(5, "voix")
    R.append(r("R03", 2, g, "CORRECT" if g == 2 else "FAUX", "ICE 5, éveil à la voix", "S3 tableau 6",
               "chapters/G92/G92_b.html", "g92-11", "Cas récapitulatif : grade 2 et dexaméthasone 10 mg toutes les 6 h, conforme à S2 tableau 3."))
    g = grade_ice(4, "voix")
    R.append(r("R04", 2, g, "CORRECT" if g == 2 else "FAUX", "ICE 4, éveil à la voix, sans crise", "S3 tableau 6",
               "chapters/G92/G92_c.html", "g92-e-2", "Cas 2 : réponse B (grade 2) exacte."))
    R.append(r("R05", "soins de support + ICE deux fois par jour", "réponse B", "CORRECT",
               "Conduite du grade 1", "S2 tableau 3 (Grade 1 : Supportive care only. Twice-daily neurocognitive assessment using ICE score)",
               "chapters/G92/G92_b.html", "g92-11", "Quiz de g92-11."))
    # R06 : ICE 0 — grade 3 si éveillé avec aphasie globale, grade 4 si inaccessible
    g_eveille = grade_ice(0, "spontane")
    g_inacc = grade_ice(0, "inaccessible")
    R.append(r("R06", "ICE 0 éveillé → grade 3 ; ICE 0 inaccessible → grade 4", "« grade 4 = 0 ou non évaluable »",
               "FAUX", f"grade_ice(0, éveillé) = {g_eveille} ; grade_ice(0, inaccessible) = {g_inacc}",
               "S3 note ^ : « A patient with an ICE score of 0 may be classified as having Grade 3 ICANS if the patient is awake with global aphasia »",
               "chapters/G92/G92_b.html", "g92-12",
               "Le div.key range tout ICE 0 en grade 4 (« 0 ou non évaluable ») ; le piège de g92-6 dit « très bas ou non évaluable » sans trancher. "
               "Les formulations « 0 non évaluable = grade 4 » (g92-e-2, g92-ice) et « 0 (non évaluable) » (g92-grade) sont exactes mais n'expliquent pas l'ICE 0 éveillé. Constat C03."))
    # R07 : total des points du score ICE
    items = {"orientation": 4, "dénomination": 3, "exécution d'ordres": 1, "écriture": 1, "attention": 1}
    tot = sum(items.values())
    R.append(r("R07", 10, tot, "CORRECT" if tot == 10 else "FAUX", " + ".join(f"{k} {v}" for k, v in items.items()),
               "S3 tableau 5 (ICE)", "chapters/G92/G92_c.html", "g92-e-2",
               "Le barème existe dans S3 (texte intégral lu) : la leçon le déclare « non lu » (constat C10, proposition)."))
    # R08 : décroissance de méthylprednisolone au grade 4
    source = 1000 * 3 + 2 * 250 * 2 + 2 * 125 * 2 + 2 * 60 * 2
    lecon = 1000 * 3 + 2 * 250 * 2 + 125 * 2 + 60 * 2
    R.append(r("R08", source, lecon, "FAUX",
               "cumul = 1000×3 + (250×2/j)×2 + (125×2/j)×2 + (60×2/j)×2 ; lecture littérale de la leçon : 125 et 60 mg une fois par jour",
               "S2 tableau 3, grade 4 : « taper at 250 mg every 12 hrs for 2 days, then 125 mg every 12 hrs for 2 days, then 60 mg every 12 hrs for 2 days »",
               "chapters/G92/G92_b.html ; chapters/G92/G92_d.html ; chapters/G92/G92_pop2.html", "g92-9 ; g92-p-2 ; g92-methylpred",
               f"La leçon omet « toutes les 12 heures » pour 125 et 60 mg : dose quotidienne lue divisée par deux (250 → 125 mg/j, 120 → 60 mg/j) ; "
               f"cumul de la décroissance {source - 3000} mg selon la source contre {lecon - 3000} mg à la lecture littérale. Constat C02."))
    R.append(r("R09", "1000 mg/j × 3 j jusqu'à amélioration au grade 1, puis 250–125–60 mg un jour chacun",
               "1000 mg/j × 3 j puis décroissance rapide", "ARRONDI", "Schéma du grade 3",
               "S2 tableau 3, grade 3 : « methylprednisolone 1000 mg/day for 3 days until improvement to Grade 1 and then rapid taper (e.g., 250 mg–125 mg–60 mg for 1 day each) »",
               "chapters/G92/G92_b.html", "g92-9", "Condition « jusqu'à amélioration au grade 1 » et exemple de décroissance absents (constat C11)."))
    dmin, dmax = 10 * 24 / 6, 20 * 24 / 6
    R.append(r("R10", [40, 80], [dmin, dmax], "CORRECT",
               "10–20 mg toutes les 6 h → 4 prises/j → 40–80 mg/j",
               "S2 tableau 3 ; plausibilité : IP Dexaméthasone Galepharm (œdème cérébral aigu, dose initiale 40 à 100 mg i.v.) [S11]",
               "chapters/G92/G92_b.html ; chapters/G92/G92_d.html ; chapters/G92/G92_pop2.html", "g92-9 ; g92-p-2 ; g92-dexa",
               "Usage hors indication enregistrée en Suisse pour l'ICANS (constat C05)."))
    plafond = 800 / 8
    enfant = 12 * 29.9
    R.append(r("R11", {"poids_plafond_kg": 100, "dose_29_9_kg_mg": 358.8, "doses_max": 4},
               {"poids_plafond_kg": plafond, "dose_29_9_kg_mg": round(enfant, 1), "doses_max": 1 + 3}, "CORRECT",
               "8 mg/kg plafonné à 800 mg → plafond atteint à 800/8 = 100 kg ; 12 mg/kg sous 30 kg reste < 800 mg ; 1 dose + 3 supplémentaires = 4",
               "S5 Posologie SRC", "chapters/G92/G92_d.html ; G92_pop1.html ; G92_pop2.html ; G92_b.html", "g92-p-2 ; g92-crs ; g92-tocilizumab ; g92-12",
               "Concordant avec l'exigence de S4 de disposer d'au moins 4 doses avant la perfusion."))
    poids_typique = 800 / 12
    R.append(r("R12", "800 mg/j ≤ 12 mg/kg/j si poids ≥ 66,7 kg", round(poids_typique, 1), "CORRECT",
               "800 / 12 = 66,7 kg", "S2 § 5.4 srICANS", "chapters/G92/G92_b.html ; G92_d.html ; G92_pop2.html", "g92-9 ; g92-p-2 ; g92-anakinra",
               "Arithmétique cohérente ; aucune IP suisse d'anakinra retrouvée et voie i.v. hors indication enregistrée (constat C05, lacune L03)."))
    # R13 : vignette céfépime — énoncé incomplet
    ex_cg = cockcroft_umol(82, 65, 220)
    ex_egfr = ckd_epi_2021(82, 220)
    std = 2 * 24 / 12
    dose, inter = cefepime_fi(ex_cg)
    adapt = dose * 24 / inter
    R.append(r("R13", "dose d'entretien selon la clairance de Cockcroft (IP)", "« DFGe 24 mL/min/1,73 m², dose standard »", "NON_VERIFIABLE",
               f"Exemple chiffré proposé : homme 82 ans, 65 kg, créatinine 220 µmol/L → Cockcroft-Gault {ex_cg:.1f} mL/min, "
               f"DFGe CKD-EPI 2021 {ex_egfr:.1f} mL/min/1,73 m² ; IP : {dose:g} g toutes les {inter} h ({adapt:g} g/j) "
               f"contre dose standard de pneumonie 2 g toutes les 12 h ({std:g} g/j), soit {std / adapt:g} fois la dose adaptée.",
               "S6 Posologie (tableau par clairance ; « La clairance de la créatinine peut être déterminée approximativement au moyen de l'équation de Cockcroft »)",
               "chapters/G92/G92_a.html", "g92-0",
               "Poids et créatinine absents : la clairance exigée par l'IP ne peut pas être calculée ; DFGe normalisé ≠ clairance de Cockcroft. Constat C12."))
    R.append(r("R14", "clairance de Cockcroft nécessaire", "« DFG 25 mL/min/1,73 m² »", "NON_VERIFIABLE",
               "Cas 1 de g92-e-2 : la réponse B (« réviser la dose en fonction de la fonction rénale ») reste exacte ; la classe de dose IP n'est pas calculable sans poids ni créatinine.",
               "S6", "chapters/G92/G92_c.html", "g92-e-2", "Même proposition que R13."))
    n1, n2 = 29 / 0.71, 29 / 0.85
    R.append(r("R15", {"denominateur_debut": 73, "denominateur_resolution": 73},
               {"denominateur_debut": round(n1, 1), "denominateur_resolution": round(n2, 1)}, "FAUX",
               "n = 29 / proportion → 29/0,71 = 40,8 ; 29/0,85 = 34,1",
               "S14 : « occurred between days two and five (n=29, 71%) … resolution occurred between days one and five (n=29, 85%) »",
               "chapters/G92/G92_a.html ; chapters/G92/G92_pop2.html", "g92-2 ; g92-cefepime",
               "Les 71 % et 85 % portent sur les cas documentés (≈ 41 et ≈ 34), non sur les 73 cas ; g92-cefepime écrit « 85 % des cas d'une série de 73 patients ». Constat C13."))
    a1, a2 = 14 / 40, 10 / 40
    R.append(r("R16", [0.35, 0.25, 80], [a1, a2, 40 + 40], "CORRECT", "14/40 et 10/40 ; effectif total 80",
               "S15 résumé", "chapters/G92/G92_b.html ; G92_pop2.html", "g92-10 ; g92-anakinra", "Groupes de 40 déduits des effectifs et pourcentages publiés."))
    R.append(r("R17", {"traites_par_tocilizumab": 7, "temoins": 19}, {"traites_par_tocilizumab": 26}, "FAUX",
               "7 + 19 = 26 ; 7/26 = 26,9 % seulement ont reçu le tocilizumab",
               "S16 : « comparing those who received prophylactic Tocilizumab (N = 7) versus standard treatment (N = 19) »",
               "chapters/G92/G92_b.html ; chapters/G92/G92_pop2.html", "g92-10 ; g92-tocilizumab",
               "La leçon écrit « le tocilizumab donné … chez 26 patients ». Constat C14."))
    icans = 0.27 * 877
    R.append(r("R18", {"denominateur_95_pct": 150}, {"denominateur_implicite": 877, "icans_estimes": round(icans)}, "FAUX",
               "27 % × 877 = 237 ICANS ; date de début connue pour 150 (63 %) ; 95 % portent sur ces 150",
               "S17 : « Any-grade ICANS occurred in 27% of patients … Of 150 patients with reported onset date, 95% had onset ≤day 15 »",
               "chapters/G92/G92_a.html", "g92-2", "Constat C14 (même mineur de dénominateur)."))
    tab = {"axi-cel": 64, "brexu-cel": 69, "tisa-cel": (21, 40), "liso-cel": (27, 30), "obe-cel": 22.8, "ide-cel": 18, "cilta-cel": (23, 26)}
    hors = [k for k, v in tab.items() if (max(v) if isinstance(v, tuple) else v) > 60 or (min(v) if isinstance(v, tuple) else v) < 20]
    tab3 = {"axi-cel": (28, 32), "brexu-cel": 31, "tisa-cel": 13, "liso-cel": 10, "obe-cel": 7.1, "ide-cel": 3, "cilta-cel": 10}
    hors3 = [k for k, v in tab3.items() if (max(v) if isinstance(v, tuple) else v) > 30 or (min(v) if isinstance(v, tuple) else v) < 3]
    R.append(r("R19", "valeurs du tableau dans 20–60 % (tous grades) et 3–30 % (grade ≥ 3)", {"hors_20_60": hors, "hors_3_30": hors3},
               "ARRONDI", "comparaison de chaque ligne du tableau à la fourchette du texte",
               "S2 § 5.1 et tableau 1 (incohérence interne de la source)", "chapters/G92/G92_a.html ; G92_pop2.html", "g92-2 ; pareto-g92-definition",
               "La fourchette résumée est contredite par trois lignes du tableau qu'elle introduit. Constat C15."))
    rr = 1.6 / 0.7
    R.append(r("R20", "rapport des taux d'œdème cérébral", round(rr, 2), "CORRECT", "1,6 / 0,7 ; létalité 0,8/1,6 = 50 % contre 0,2/0,7 = 28,6 %",
               "S4 Mises en garde", "chapters/G92/G92_b.html", "g92-8",
               "Valeurs exactes ; la population de comparaison est précisée par S4 (« LDGCB et d'autres indications ») contrairement à la leçon. Constat C16."))
    R.append(r("R21", 3.6, round(10 / 278 * 100, 1), "CORRECT", "10 patients / effectif traité ZUMA-1 + ZUMA-7 (≈ 278, déduit de 10/0,036)",
               "S4 Effets indésirables", "chapters/G92/G92_b.html", "g92-10",
               "Mais S4 précise que ces patients sont morts « pour des raisons qui n'étaient pas en rapport avec ces derniers » (les effets neurologiques), "
               "non « sans lien avec le traitement » (constat C16)."))
    gm = math.sqrt(5.05 * 20.03)
    R.append(r("R22", 10.06, round(gm, 2), "CORRECT" if abs(gm - 10.06) < 0.02 else "ARRONDI", "moyenne géométrique des bornes de l'IC à 95 %",
               "S13 résumé", "chapters/G92/G92_pop2.html", "g92-cefepime", "Intervalle log-symétrique cohérent avec le rapport de cotes."))
    hl = 3 * math.log(2) / -math.log(1 - 0.68)
    R.append(r("R23", "fraction éliminée 68 % en 3 h", round(hl, 2), "CORRECT", "demi-vie apparente sous dialyse = 3·ln2 / −ln(0,32)",
               "S6 Patients dialysés", "chapters/G92/G92_a.html ; G92_b.html ; G92_c.html ; G92_pop2.html", "g92-3 ; g92-8 ; g92-e-2 ; g92-cefepime",
               "Valeur informative (≈ 1,8 h) ; aucune affirmation de la leçon ne la contredit."))
    capd_max = 8 * 4
    R.append(r("R24", 32, capd_max, "CORRECT", "8 items × 0–4 points", "S3 tableau 7 (CAPD)", "chapters/G92/G92_b.html", "g92-11",
               "Seuil ≥ 9 sur 32 ; S3 classe CAPD < 9 en grades 1–2 et ≥ 9 en grade 3 (exact dans la leçon)."))
    R.append(r("R25", "q8–12 h (2 à 3/j) ; grade 1 : 2/j ; grade 2 : 3–4/j", "toutes les 8 à 12 h ; 2/j ; 3 à 4/j", "CORRECT",
               "24/12 = 2 ; 24/8 = 3 ; escalade cohérente", "S2 § 5.3 et tableau 3", "chapters/G92/G92_a.html ; G92_b.html ; G92_c.html", "g92-6 ; g92-9 ; g92-e-1", ""))
    R.append(r("R26", "partition 0–10 sans trou", "10 = normal ; 7–9 ; 3–6 ; 0–2 ; 0 inaccessible", "CORRECT",
               "union des classes {10} ∪ [7,9] ∪ [3,6] ∪ [0,2] = [0,10]", "S3 tableau 6", "chapters/G92/G92_c.html ; G92_pop1.html", "g92-e-2 ; g92-ice", ""))
    R.append(r("R27", "seuil de risque < 30 (DFGe) inclus dans le seuil d'adaptation ≤ 50 (clairance)", "30 < 50", "CORRECT",
               "comparaison de seuils", "S13 ; S6", "chapters/G92/G92_a.html ; G92_b.html", "g92-4 ; g92-12",
               "Cohérent : le risque majeur survient chez des patients dont la dose aurait déjà dû être réduite selon l'IP ; grandeurs différentes (mL/min/1,73 m² et mL/min)."))
    tot_ana = 100 * 7
    R.append(r("R28", 700, tot_ana, "CORRECT", "100 mg/j du jour 0 au jour 6 = 7 doses", "S15", "chapters/G92/G92_b.html", "g92-10", "Informatif."))
    R.append(r("R29", "≤ 250 mg en ≥ 5 min ; > 250 mg en ≥ 30 min", "durée de perfusion absente", "NON_VERIFIABLE",
               "règle d'administration de l'IP", "S10 Posologie (« celle de doses supérieures à 250 mg, de 30 minutes au minimum »)",
               "chapters/G92/G92_d.html", "g92-p-2", "Énoncé incomplet pour un bolus de 1000 mg (constat C11)."))
    R.append(r("R30", "1,6 % > 0,7 %", "risque accru LMPGB", "CORRECT", "comparaison", "S4", "chapters/G92/G92_b.html", "g92-8", ""))
    # ---- valeurs introduites par les propositions de l'audit (informatives, absentes de la leçon)
    R.append(r("R31", 86.4, round(19 / 22 * 100, 1), "CORRECT", "19/22", "S3 (essai de phase 1)",
               "propositions/G92_c_semio.html", "g92-sm-2", "Proportion parmi les patients ayant évolué vers une forme sévère ; aucune spécificité. AUDIT_INFORMATIF"))
    fr = 110 / 120
    R.append(r("R32", {"fraction_renale": 0.917, "rapport_demi_vies": 7.6},
               {"fraction_renale": round(fr, 3), "rapport_demi_vies": round(13 / 1.7, 1)}, "CORRECT",
               "clairance rénale / clairance totale = 110/120 ; t½ dialysé / t½ normal = 13/1,7", "S6 Pharmacocinétique",
               "propositions/G92_c_pharmacocinetique.html", "g92-s-pk-cours", "AUDIT_INFORMATIF"))
    ss = {k: round(4 * t, 1) for k, t in {"normal_h": 1.7, "dialyse_h": 13}.items()}
    frac4 = 1 - 0.5 ** 4
    R.append(r("R33", {"normal_h": 6.8, "dialyse_h": 52.0, "fraction_equilibre": 0.9375}, dict(ss, fraction_equilibre=frac4), "CORRECT",
               "4 demi-vies ; fraction de l'équilibre atteinte = 1 − 0,5⁴ (cinétique d'ordre 1, hypothèse de l'audit)", "S6 (t½ 1,7 h et 13 h)",
               "propositions/G92_c_pharmacocinetique.html", "g92-s-pk-cours", "Arrondis du texte : « environ 7 heures » et « 52 heures ». AUDIT_INFORMATIF"))
    se, sp = 0.88, 0.88
    R.append(r("R34", {"RV+": 7.3, "RV-": 0.14}, {"RV+": round(se / (1 - sp), 2), "RV-": round((1 - se) / sp, 3)}, "CORRECT",
               "RV+ = Se/(1−Sp) ; RV− = (1−Se)/Sp", "S24 (Se 0,88, Sp 0,88)", "propositions/G92_c_semio.html", "g92-sm-5", "AUDIT_INFORMATIF"))
    se2, sp2 = 0.977, 0.896
    R.append(r("R35", {"RV+": 9.4, "RV-": 0.026}, {"RV+": round(se2 / (1 - sp2), 2), "RV-": round((1 - se2) / sp2, 3)}, "CORRECT",
               "RV+ = Se/(1−Sp) ; RV− = (1−Se)/Sp", "S27 (Se 97,7 %, Sp 89,6 %)", "propositions/G92_c_semio.html", "g92-sm-4",
               "Le texte cite seulement Se et Sp ; RV calculés pour contrôle. AUDIT_INFORMATIF"))
    cg, eg = cockcroft_umol(82, 65, 220), ckd_epi_2021(82, 220)
    d, i = cefepime_fi(cg)
    R.append(r("R36", {"cockcroft_mL_min": 21, "dfge": 25, "dose_g_par_24h": 1, "rapport_surdosage": 4},
               {"cockcroft_mL_min": round(cg, 1), "dfge": round(eg, 1), "dose_g_par_24h": d * 24 / i, "rapport_surdosage": 4 / (d * 24 / i)},
               "CORRECT", "Cockcroft-Gault (µmol/L, homme) ; CKD-EPI 2021 sans coefficient ethnique ; tableau IP",
               "S6 Posologie", "propositions/G92_remplacements.json (P17) ; propositions/G92_d_1.html", "g92-0 ; g92-p-2", "Vignette proposée. AUDIT_INFORMATIF"))
    return R


# ------------------------------------------------------------ cohérence des valeurs clés entre fichiers (SEM-20)
COHERENCE = [
    ("dexaméthasone", r"10 à 20 mg par voie intraveineuse toutes les 6 heures"),
    ("tocilizumab", r"8 mg/kg"),
    ("tocilizumab_plafond", r"800 mg"),
    ("cefepime_dialyse", r"68 %"),
    ("cefepime_seuil_IP", r"50 mL/min"),
    ("ifosfamide", r"48 à 72 heures"),
    ("ICE_grade1", r"7 à 9|7–9"),
]


def coherence() -> list[dict]:
    out = []
    for nom, motif in COHERENCE:
        hits = {}
        for f in FILES:
            t = " ".join(x for _, x in texte(ROOT / f))
            k = len(re.findall(motif, t))
            if k:
                hits[f] = k
        out.append({"cle": nom, "motif": motif, "occurrences": hits})
    return out


def verifier_citations(cache: Path | None) -> dict:
    if not cache:
        return {}
    norm = lambda s: re.sub(r"\s+", " ", s.replace("|", " ").replace("’", "'")).strip().lower()
    textes = {}
    res = {}
    for v, motif, src, cit in C:
        if src not in CACHE:
            continue
        p = cache / CACHE[src]
        if not p.exists():
            continue
        textes.setdefault(src, norm(p.read_text(encoding="utf-8", errors="replace")))
        coeur = norm(re.sub(r"\s*\((recalcul|arrondi)[^)]*\)\s*$", "", cit.split("‖")[0]))
        morceaux = [m.strip() for m in re.split(r"\.\.\.| ; |…", coeur) if m.strip()]
        res[f"{src}:{cit[:60]}"] = all(m in textes[src] for m in morceaux)
    return res


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cache", type=Path, default=None, help="dossier des copies locales des sources lues")
    args = ap.parse_args()
    inv = inventaire()
    cit = verifier_citations(args.cache)
    res, non_rapprochees = [], []
    for it in inv:
        if it["categorie"] != "GRANDEUR":
            continue
        c = concordance(it)
        if c is None:
            non_rapprochees.append(it)
            continue
        it["controle"] = c
    R = recalculs()
    for it in inv:
        if "controle" in it:
            c = it["controle"]
            res.append({"id": it["id"], "attendu": c["citation"], "trouve": it["valeur"], "ecart": None,
                        "verdict": c["verdict"], "formule": "concordance avec la citation de la source",
                        "source": c["source"], "fichier": it["fichier"], "ancre": it["ancre"]})
    cats = {}
    for it in inv:
        cats[it["categorie"].split(":")[0]] = cats.get(it["categorie"].split(":")[0], 0) + 1
    verdicts = {}
    for x in R:
        if "AUDIT_INFORMATIF" not in x["note"]:
            verdicts[x["verdict"]] = verdicts.get(x["verdict"], 0) + 1
    vign = sum(1 for x in res if x["verdict"] == "VIGNETTE")
    synth = {
        "total_releves": len(inv),
        "categories": cats,
        "grandeurs": cats.get("GRANDEUR", 0),
        "concordance_source": sum(1 for x in res if x["verdict"] == "CORRECT"),
        "valeurs_de_vignette_ou_unite": vign,
        "non_rapprochees": len(non_rapprochees),
        "recalculs": len(R),
        "calculables_lecon": sum(1 for x in R if "AUDIT_INFORMATIF" not in x["note"]),
        "informatifs_audit": sum(1 for x in R if "AUDIT_INFORMATIF" in x["note"]),
        "verdicts_recalculs": verdicts,
        "citations_retrouvees_mot_pour_mot": (sum(cit.values()), len(cit)) if cit else None,
    }
    (HERE / "inventaire.json").write_text(json.dumps({"total": len(inv), "items": inv}, ensure_ascii=False, indent=1), encoding="utf-8")
    (HERE / "resultats.json").write_text(json.dumps({
        "synthese": synth, "recalculs": R, "concordances": res,
        "non_rapprochees": non_rapprochees, "coherence_inter_fichiers": coherence(),
        "citations_retrouvees": cit}, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps(synth, ensure_ascii=False, indent=1))
    for it in non_rapprochees:
        print("NON RAPPROCHÉE", it["id"], it["fichier"][-9:], it["valeur"], "|", it["contexte"])
    for k, ok in cit.items():
        if not ok:
            print("CITATION NON RETROUVÉE", k)


if __name__ == "__main__":
    main()
