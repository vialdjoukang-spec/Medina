#!/usr/bin/env python3
"""Audit ALPHA77 G91 — inventaire scripté et recalcul de toutes les grandeurs de la leçon.

Exécution (depuis la racine du dépôt) :
    python3 docs/collaboration/ssp-v2/execution/ALPHA1-CLAUDE-G91-MED/calculs/verifier.py

Sorties (dans le dossier du script) : inventaire.json, resultats.json.
Lecture seule des 7 fichiers canoniques ; aucune écriture hors de calculs/.

Trois familles de contrôles :
  1. RECALCUL : grandeur dérivable (pourcentage d'un effectif, différence, taux annuel,
     somme, conversion d'unités, comparaison d'un cas à un seuil, arithmétique de dose).
  2. CONCORDANCE_SOURCE : valeur rapportée, comparée à la citation exacte de la source lue
     (Sx de sources.json) ; verdict CORRECT si la valeur figure dans la citation.
  3. NON_CALCULABLE : identifiant (année, numéro d'îlot, ordinal, code CIM, nom de gène,
     borne d'échelle descriptive) ; relevé mais sans objet de calcul.
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
    "chapters/G91/G91_a.html", "chapters/G91/G91_b.html", "chapters/G91/G91_c.html",
    "chapters/G91/G91_d.html", "chapters/G91/G91_pop1.html", "chapters/G91/G91_pop2.html",
    "glossary/g91.py",
]
NUM = re.compile(r"(?<![\w.,\-])([+\u2212]?(?:\d{1,3}(?:[ \u202f\u00a0]\d{3})+(?!\d)|\d+)(?:[.,]\d+)?)"
                 r"(?:\s?[–-]\s?(\d+(?:[.,]\d+)?))?")
UNIT = re.compile(r"^\s?(%|mmH2O|cmH2O|m/s|mL|mg/kg/dose|mg/kg/jour|mg/kg|pour 100 000|/100 000|"
                  r"€|QALY|ans?|mois|semaines|heures|patients|cas|centres|experts|études|termes|"
                  r"témoins|candidats|opérés|hyperdrainages|iNPH|°|e\b|hémorragies)")
MMHG_PER_MMH2O = 1 / 13.595  # 1 mmHg = 13,595 mmH2O (masse volumique Hg/eau à 0 °C)


def texte(path: Path) -> list[tuple[str, str]]:
    """Renvoie [(ancre, texte)] : le texte est découpé par ancre (id, data-pop) la plus proche."""
    s = path.read_text(encoding="utf-8")
    if path.suffix == ".py":
        return [("glossary/g91.py", re.sub(r"\s+", " ", s))]
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
    if avant.rstrip().endswith(">") or avant.endswith("('") or re.search(r"(Betta|CIM-|chlorure|e-|p-)\s?$", avant):
        return "NON_CALCULABLE:identifiant"
    if re.search(r"(pour|/)\s?$", avant) and v.replace(" ", "") in ("100000", "1000"):
        return "NON_CALCULABLE:denominateur"
    if re.fullmatch(r"(19|20)\d\d", v) and not re.match(r"\s?(%|patients|cas)", apres):
        return "NON_CALCULABLE:date"
    if re.match(r"\.\d{4}", apres) or re.fullmatch(r"\d{1,2}[.,]\d{2}", v) and re.match(r"\.20", apres):
        return "NON_CALCULABLE:date"
    if re.match(r"e\b", apres) or re.search(r"(grade|niveau|Figure|Cas|îlot|numéro|chapitre|G|P|Q)\s?$", avant):
        return "NON_CALCULABLE:identifiant"
    if re.search(r"(IC|IC95|à) ?$", avant) and v == "95":
        return "NON_CALCULABLE:identifiant"
    if re.match(r"\s?[A-ZÉ][a-zé]", apres) and re.fullmatch(r"\d{1,2}", v) and re.search(r"[.)] ?$|^ ?$|» ?$", avant[-3:] or " "):
        return "NON_CALCULABLE:identifiant"
    return "GRANDEUR"


def inventaire() -> list[dict]:
    items, n = [], 0
    for f in FILES:
        for ancre, t in texte(ROOT / f):
            for m in NUM.finditer(t):
                n += 1
                avant, apres = t[max(0, m.start() - 40):m.start()], t[m.end():m.end() + 30]
                u = UNIT.match(apres)
                items.append({
                    "id": f"I{n:03d}", "fichier": f, "ancre": ancre, "valeur": m.group(0).strip(),
                    "unite": (u.group(1) if u else ""),
                    "contexte": (avant + m.group(0) + apres).strip(),
                    "categorie": classer(m.group(1), avant, apres),
                })
    return items


# ---------------------------------------------------------------- concordance avec les sources lues
# (valeur telle qu'écrite dans la leçon, motif de contexte, source, citation exacte de la source)
C = [
    ("0,36", r"Evans", "VIGNETTE", "valeur pédagogique d'un cas fictif (comparée au seuil dans les recalculs)"),
    ("0,34", r"Evans", "VIGNETTE", "valeur pédagogique d'un cas fictif"),
    ("170", r"mmH2O", "VIGNETTE", "valeur pédagogique d'un cas fictif"),
    ("180", r"mmH2O", "VIGNETTE", "valeur pédagogique d'un cas fictif"),
    ("40", r"retrait de 40 mL", "VIGNETTE", "valeur pédagogique d'un cas fictif"),
    ("76", r"homme de 76|76 ans, marche", "VIGNETTE", "âge d'un cas fictif"),
    ("78", r"femme de 78", "VIGNETTE", "âge d'un cas fictif"),
    ("80", r"homme de 80", "VIGNETTE", "âge d'un cas fictif"),
    ("18", r"depuis 18 mois", "VIGNETTE", "durée d'un cas fictif"),
    ("50", r"amélioration \(50 mL\)", "VIGNETTE", "volume d'un cas fictif"),
    ("48", r"termes", "S13", "A total of 33 studies collectively used 48 terms"),
    ("33", r"études", "S13", "A total of 33 studies collectively used 48 terms"),
    ("200", r"mmH2O", "S1", "CSF pressure of 200 mmH2O or less and normal CSF content"),
    ("3,7", r"Suède|total", "S1", "is 3.7%; prevalence rates of 8.9% and 5.9% were reported in the population aged 80 years"),
    ("8,9", r".", "S1", "prevalence rates of 8.9% and 5.9%"),
    ("5,9", r"80 ans|Suède|scanner", "S1", "prevalence rates of 8.9% and 5.9%"),
    ("5,9", r"argent", "S6", "in 5.9% (= 31/526) of those who received the silver shunt"),
    ("80", r"80 ans|≥ 80|80 ans et", "S1", "aged 80 years and above"),
    ("1,5", r"critères japonais|japo", "S1", "would be 1.5%, if the researchers had used the criteria of the Japanese guidelines"),
    ("1,6", r"pondérée", "S1", "a weighted average of 1.6% in four population-based studies in Japan"),
    ("175", r".", "S1", "175 per 100000"),
    ("400", r"100 000", "S1", "it is 400 per 100000 in the population aged 80 years and above"),
    ("660", r".", "S1", "the mean prevalence reported in these studies is 660 per 100000"),
    ("53", r"hors Japon", "S1", "the mean prevalence in countries other than Japan is 53 per 100000"),
    ("2–10", r"hospitali", "S1", "medical examination rate was reported to be 2–10 people per 100000"),
    ("30–60", r".", "S1", "increased to 30–60 per 100000 among people aged 65–70 years and higher"),
    ("65–70", r".", "S1", "among people aged 65–70 years and higher"),
    ("25", r"hydrocéphalie|Hémorragie sous-arachnoïdienne|hémorragies sous-a|environ 25|développent", "S3", "a build-up of fluid in the brain (in approximately 25% of patients)"),
    ("40", r"[Ll]étalité", "S3", "The case-fatality after aSAH is approximately 40%"),
    ("6–12", r".", "S1", "four of them developed iNPH (corresponding to an incidence of 6–12% per year)"),
    ("4", r"4 sur 8", "S1", "Eight patients with AVIM were followed up for 4–8 years ... four of them developed iNPH"),
    ("8", r"4 sur 8", "S1", "Eight patients with AVIM"),
    ("4–8", r".", "S1", "followed up for 4–8 years"),
    ("17", r"par an", "S1", "(incidence of 17% per year)"),
    ("27", r"27 sur 52", "S1", "27 of 52 AVIM cases ... developed iNPH within 3 years"),
    ("52", r".", "S1", "27 of 52 AVIM cases"),
    ("3", r"52 en 3 ans", "S1", "within 3 years"),
    ("400 000", r".", "S2", "an estimated 400,000 new cases of paediatric hydrocephalus arise annually"),
    ("80", r"revenu faible|pays à revenu", "S2", "with over 80% occurring in low- and middle-income countries"),
    ("85", r"myéloméningoc", "S2", "Up to 85% of children born with myelomeningocele"),
    ("85", r"tubercul|enfants développent", "S2", "up to 85% of children with TB meningitis develop hydrocephalus"),
    ("6000", r".", "S2", "the annual incidence of PHH in high-income countries is over 6,000 cases annually"),
    ("0,7–3,7", r".", "S2", "after a traumatic head injury is low (0.7–3.7%)"),
    ("50", r"[Tt]umeur", "S2", "Over 50% of children with brain tumors develop hydrocephalus"),
    ("30", r"animal, 30", "S4", "around 30–40% of the cerebrospinal fluid is formed upstream from the aqueduct"),
    ("40", r"30 à 40", "S4", "around 30–40% of the cerebrospinal fluid is formed upstream from the aqueduct"),
    ("14", r"14 à 33", "S11", "positivity rates ranging from approximately 14% to 33%"),
    ("33", r"14 à 33", "S11", "positivity rates ranging from approximately 14% to 33%"),
    ("1000", r"tube neural|nouveau-né", "S2", "to below 1 per 1,000 following effective folate supplementation"),
    ("1", r"1 pour 1000", "S2", "below 1 per 1,000"),
    ("94–100", r".", "S1", "The percentage of gait disturbance is 94–100%"),
    ("78–98", r".", "S1", "being 78–98% and 60–92%, respectively"),
    ("60–92", r".", "S1", "being 78–98% and 60–92%, respectively"),
    ("90,9", r".", "S1", "90.9% experience urine dribbling, and 74.5% urinary incontinence"),
    ("74,5", r".", "S1", "and 74.5% urinary incontinence"),
    ("60", r"[Tt]riade|complète|60 % des", "S1", "the triad is complete in approximately 60% of cases"),
    ("12,1", r".", "S1", "the full triad was present in only 12.1% of 1524 patients"),
    ("1524", r".", "S1", "12.1% of 1524 patients"),
    ("86", r".", "S8", "This retrospective analysis included 86 patients"),
    ("76", r"âge moyen 76|moyen 76", "S8", "mean age: 76.26 ± 9.08 years"),
    ("94,2", r".", "S8", "Gait disorders were the most common complaint (94.2% of the patients)"),
    ("75,6", r".", "S8", "followed by cognitive (75.6%)"),
    ("60,5", r".", "S8", "and urinary (60.5%) complaints"),
    ("70", r"détrusor", "S1", "detrusor hyperactivity was seen in about 70% of patients"),
    ("84", r"museau", "S1", "84% had a snout reflex"),
    ("77", r"glabellaire", "S1", "77% had an eyebrow reflex"),
    ("65", r"paratonie", "S1", "65% had paratonia (Gegenhalten)"),
    ("61", r"palmo", "S1", "61% had a palmar reflex (palmomental)"),
    ("26", r"série de 26", "S1", "In a study that evaluated neurological symptoms in 26 patients with iNPH"),
    ("70,3", r"apathie", "S1", "A BPSD survey conducted in Japan reported that apathy was seen at a rate of 70.3% (autre étude que la série de 26 : voir C12)"),
    ("69,2", r".", "S10", "apathy (69.2%, 95% CI 63.1-74.6, n = 293)"),
    ("30,1", r".", "S10", "depression (30.1%, 20.1-42.3, n = 7,670)"),
    ("22,6", r".", "S10", "Agitation (22.6%, 11.8-39.1)"),
    ("21,9", r".", "S10", "anxiety (21.9%, 13.2-34.2)"),
    ("22", r"études|22 sont", "S10", "Twenty-two studies were included ... A total of 12 of 22 studies were rated 'low' quality"),
    ("18–20", r"semaines", "S2", "during the second trimester of pregnancy (18 to 20 weeks) via ultrasonography"),
    ("1", r"≥ 1 symptôme", "S1", "More than one symptom in the clinical triad (traduction officielle du critère « 1 ou plus »)"),
    ("0,3", r"Evans", "S1", "Hydrocephalus is defined as EI >0.3"),
    ("30", r"30 à 50|30 ou 50", "S1", "in the range of 30–50 ml"),
    ("50", r"30 à 50|30 ou 50", "S1", "in the range of 30–50 ml"),
    ("30–50", r".", "S1", "in the range of 30–50 ml"),
    ("2–4", r"heures", "S1", "Evaluation should be performed 2–4 hours after the tap test"),
    ("24", r"24 heures|vers 24", "S1", "and on the following day (approximately 24 hours later)"),
    ("24", r"avant et 24 heures après|et 24 heures", "S8", "physiotherapeutic evaluation before and 24 h after the CSF tap-test"),
    ("21", r"Lewy", "S1", "among 127 patients with definite iNPH, Lewy body disease (LBD) was suspected in 21"),
    ("127", r".", "S1", "among 127 patients with definite iNPH"),
    ("58", r"sensibilit|Sensibilit", "S1", "The CSF tap test has a sensitivity of 58% (26–87%)"),
    ("26–87", r".", "S1", "sensitivity of 58% (26–87%)"),
    ("75", r"spécificit", "S1", "and a specificity of 75% (33–100%)"),
    ("33–100", r".", "S1", "specificity of 75% (33–100%)"),
    ("6", r"6 semaines|à 6 semaines|visites à 6", "S8", "interdisciplinary consultations took place at 6 weeks, 6 and 12 months"),
    ("6", r"semaines, 6 et 12", "S8", "at 6 weeks, 6 and 12 months"),
    ("12", r"6 et 12 mois", "S8", "at 6 weeks, 6 and 12 months"),
    ("44", r".", "S8", "the Board evaluated 44 candidates"),
    ("27", r"recommandés", "S8", "recommended ventriculoperitoneal shunting for 27 patients"),
    ("16", r"opérés", "S8", "So far, 16 patients have been operated"),
    ("92", r".", "S8", "A total of 92% reported gait improvement at 6 weeks postoperative control (dénominateur : 12 patients revus, voir C08)"),
    ("80", r"plus de 80 ans|Sujet de plus de 80", "S8", "Patients above 80 years of age reported more often gait improvement"),
    ("99", r".", "S5", "A total of 99 participants underwent randomization"),
    ("110", r".", "S5", "open-shunt valve setting (opening pressure, 110 mm of water)"),
    ("400", r"mmH2O", "S5", "placebo valve setting (opening pressure, >400 mm of water)"),
    ("3", r"À 3 mois|suivi 3 mois|à 3 mois", "S5", "The primary outcome was the change in gait velocity 3 months after surgery"),
    ("0,23", r".", "S5", "mean [±SD] change, 0.23±0.23 m per second"),
    ("+0,23", r".", "S5", "mean [±SD] change, 0.23±0.23 m per second"),
    ("0,03", r".", "S5", "mean change, 0.03±0.23 m per second"),
    ("+0,03", r".", "S5", "mean change, 0.03±0.23 m per second"),
    ("0,21", r".", "S5", "resulting in a treatment difference of 0.21 m per second"),
    ("+0,21", r".", "S5", "resulting in a treatment difference of 0.21 m per second (différence entre groupes, non gain absolu : voir C19)"),
    ("0,12–0,31", r".", "S5", "(95% confidence interval, 0.12 to 0.31; P<0.001)"),
    ("24", r"[Cc]hutes", "S5", "more participants in the placebo group reporting falls (46% vs. 24%)"),
    ("46", r".", "S5", "reporting falls (46% vs. 24%)"),
    ("12", r"sous-dural", "S5", "more participants in the open-shunt group having subdural bleeding (12% vs. 2%)"),
    ("2", r"12 % contre 2", "S5", "subdural bleeding (12% vs. 2%)"),
    ("59", r".", "S5", "and positional headaches (59% vs. 28%)"),
    ("28", r"posturales", "S5", "and positional headaches (59% vs. 28%)"),
    ("13", r"centres", "S7", "Patients (n = 142) were prospectively included in the European multicentre study by 13 centres"),
    ("142", r".", "S7", "Patients (n = 142)"),
    ("1", r"à 1 an|À 1 an", "S7", "Re-examinations, 12 months after surgery"),
    ("69", r"Rankin|mRS\)", "S7", "Sixty-nine per cent of the patients were improved according to the mRs"),
    ("84", r"iNPH\)|échelle iNPH", "S7", "and 84% according to the iNPH scale"),
    ("0–2", r"mRS", "S7", "(scores 0-2 on the mRs)"),
    ("53", r"autonome|vie a", "S7", "was increased from 53% before to 82% 12 months after surgery"),
    ("82", r".", "S7", "from 53% before to 82% 12 months after surgery"),
    ("28", r"complications", "S7", "Twenty-eight per cent of the patients experienced complications"),
    ("13", r"conservatrices", "S7", "either conservatively (13%) or surgically (15%) treated"),
    ("15", r"chirurgicales", "S7", "either conservatively (13%) or surgically (15%) treated"),
    ("10", r"Complications 10", "S1", "The complication rates were 10% in the VP shunt group and 14% in the LP shunt group"),
    ("14", r"Complications 14", "S1", "and 14% in the LP shunt group"),
    ("15,3", r".", "S1", "significantly less frequent in VA shunts (6.7% and 10.7%) than in VP shunts (15.3% and 28.9%)"),
    ("6,7", r".", "S1", "VA shunts (6.7% and 10.7%)"),
    ("12,7", r".", "S1", "significantly more frequent in the VA shunt group (12.7%) than in the VP shunt group (5.5%)"),
    ("5,5", r".", "S1", "than in the VP shunt group (5.5%)"),
    ("12", r"12 mois", "S1", "symptomatic improvement 12 months after the surgical intervention"),
    ("50", r"ETV|76,9|améliorés|patients étaient", "S1", "50% of patients who underwent ETV achieved symptomatic improvement"),
    ("76,9", r".", "S1", "whereas the VP shunt intervention achieved improvement in 76.9% of the patients"),
    ("12", r"cmH2O", "S1", "another group in which the pressure was fixed at 12 cmH2O"),
    ("9", r"hyperdrainage", "S1", "nine patients exhibited over-drainage (9/34)"),
    ("34", r".", "S1", "(9/34)"),
    ("63–84", r".", "S1", "63–84% in 1 year"),
    ("1", r"63–84 % à 1 an", "S1", "63–84% in 1 year"),
    ("69", r"2 ans", "S1", "69% in 2 years"),
    ("2", r"69 % à 2 ans|améliorés à 2 ans|% à 2 ans", "S1", "69% in 2 years ; improvement rate ... is 93% after 2 years"),
    ("60–74", r".", "S1", "approximately 60–74% in 3–6 years"),
    ("3–6", r".", "S1", "approximately 60–74% in 3–6 years"),
    ("60–77", r".", "S1", "it is reported to be approximately 60–77%"),
    ("61–69", r".", "S1", "the improvement rate is reported to be 61–69%"),
    ("52", r"incontinence", "S1", "Regarding urinary incontinence, an improvement rate of 52% has been reported"),
    ("3", r"Kiefer ≤ 3|Kiefer ≤", "S1", "If the Kiefer comorbidity index is 3 points or less, improvement rate ... is 93% after 2 years"),
    ("93", r".", "S1", "improvement rate following a shunt intervention is 93% after 2 years"),
    ("6", r"≥ 6", "S1", "no improvement can be expected if it is 6 points or more"),
    ("58", r".", "S1", "The CSF tap test has a sensitivity of 58%"),
    ("75", r".", "S1", "and a specificity of 75%"),
    ("2", r"avant 2 ans|moins de 2 ans", "S2", "ETV-CPC is typically used in children younger than 2 years old"),
    ("8", r"ETV|jusqu’à 8 ans", "S2", "ETV failure is possible even after 8 years after the initial procedure"),
    ("1605", r".", "S6", "1605 patients from neonate to 91 years of age were randomised"),
    ("91", r"91 ans|à 91", "S6", "from neonate to 91 years of age"),
    ("21", r"centres", "S6", "The trial was set in 21 neurosurgical wards across the UK and the Republic of Ireland"),
    ("6,0", r".", "S6", "Infection occurred in 6.0% (= 32/533) of those who received the standard shunt"),
    ("2,2", r"cathéter|infection|Infection|imprégné", "S6", "in 2.2% (= 12/535) of those who received the antibiotic shunt"),
    ("0,38", r".", "S6", "cause-specific hazard ratio 0.38, 97.5% confidence interval 0.18 to 0.80"),
    ("25", r"[ÉéEe]chec", "S6", "The ventriculoperitoneal shunt failure rate attributable to any cause was 25.0% overall"),
    ("3–11", r".", "S2", "In high-income countries, shunt infection rates average 3–11%"),
    ("3", r"3 à 11", "S2", "shunt infection rates average 3–11%"),
    ("11", r"3 à 11", "S2", "shunt infection rates average 3–11%"),
    ("18", r"experts", "S12", "A modified Delphi consensus process was conducted with 18 neurosurgeons and neuroscientists"),
    ("18", r"18 ans", "S12", "Radiological findings include ventricular collapse (age < 18 years)"),
    ("1", r"avant 1 an|1 an, de 1|de 1 à 7", "S12", "infants (age < 1 year), children with a growing skull (age 1 to 7 years)"),
    ("7", r"7 ans", "S12", "children with a fixed skull (age > 7 years)"),
    ("12", r"PENS \(12", "S5", "subdural bleeding (12% vs. 2%)"),
    ("2", r"contre 2 %\)", "S5", "subdural bleeding (12% vs. 2%)"),
    ("2,2", r"années de vie", "S1", "an additional lifetime of 2.2 years and 1.7 QALY was gained with treatment"),
    ("+2,2", r".", "S1", "an additional lifetime of 2.2 years and 1.7 QALY was gained with treatment"),
    ("1,7", r"QALY", "S1", "and 1.7 QALY was gained"),
    ("+1,7", r".", "S1", "and 1.7 QALY was gained"),
    ("13 000", r".", "S1", "with an additional cost of €13,000"),
    ("8", r"mortalité", "S2", "The incidence of shunt-related mortality was 8%"),
    ("20–40", r".", "S2", "Two studies have evaluated 20-year or 40-year outcomes"),
    ("67", r".", "S2", "Most children graduated from a typical school (67%)"),
    ("56", r".", "S2", "56% of patients were socially independent"),
    ("42", r".", "S2", "and 42% of the patients were employed"),
    ("20", r"bilan neuro|environ 20", "S2", "Only 20% of all children with hydrocephalus undergo standardized assessments"),
    ("1,23", r".", "S3", "or hydrocephalus (OR: 1.23; 95% CI, 0.93–1.63)"),
    ("0,93–1,63", r".", "S3", "or hydrocephalus (OR: 1.23; 95% CI, 0.93–1.63)"),
    ("3", r"tous les 3 mois", "S2", "measuring head circumference at least every 3 months (recommandation américaine, signalée comme telle)"),
    ("18", r"18 mois", "S2", "until age 18 months"),
    ("70", r"hémorragies par an|≥ 70", "S3", "the proposed minimum volumes for centres (70 aSAH patients per year, or 35 per year for centres in remote areas)"),
    ("35", r".", "S3", "or 35 per year for centres in remote areas"),
    ("6", r"Kiefer ≥ 6|Kiefer ≥", "S1", "no improvement can be expected if it is 6 points or more"),
    ("0,356", r".", "S1", "(average EI: 0.356 ± 0.040)"),
    ("97", r".", "S1", "a sensitivity of 97%, a specificity of 88% ... at a cutoff value of 90°"),
    ("88", r".", "S1", "a specificity of 88%"),
    ("64", r".", "S1", "DESH findings were reported in 64%"),
    ("77", r"VPP", "S1", "a 77% positive predictive value was shown"),
    ("25", r"VPN", "S1", "the negative predictive value was as low as 25%"),
    ("25,7", r".", "S9", "25.7% of responders were identified only through dual-task conditions (voir C09)"),
    ("122", r".", "S9", "GAITRite gait data from 122 patients with suspected iNPH"),
    ("146", r".", "S9", "and from 146 cognitively healthy controls"),
    ("0", r"0 à 4", "S1", "each evaluated on a scale from 0 to 4"),
    ("4", r"0 à 4", "S1", "each evaluated on a scale from 0 to 4"),
    ("0,86", r".", "S14", "areas under the curve ... ranging between .86 (Delayed Recall) and .95 (Grooved Pegboard)"),
    ("0,95", r".", "S14", "and .95 (Grooved Pegboard)"),
    ("0,86–0,95", r".", "S14", "ranging between .86 and .95"),
    ("142", r"142 iNPH", "S14", "One hundred and forty-two iNPH patients"),
    ("108", r".", "S14", "compared to that of 108 healthy individuals"),
    ("50", r"NKCC1", "S4", "by which it contributes to CSF secretion in mice, rats, and dogs (~ 50% of the total CSF secretion)"),
    ("1", r"1 mois", "S18", "Swisspeddose — Âge 1 mois - 12 an(s) ; 12 an(s) - 18 an(s)"),
    ("18", r"mois–18 ans", "S18", "Swisspeddose — 12 an(s) - 18 an(s)"),
    ("8–10", r".", "S18", "Swisspeddose, pression intracrânienne élevée : 8 - 10 mg/kg/dose"),
    ("3", r"3 fois|×3", "S18", "Répétitions quotidiennes : 3"),
    ("100", r"mg/kg/jour", "S18", "Dose quotidienne maximale : 100 mg/kg/jour"),
    ("6", r"6 mois", "S2", "Infants, particularly those <6 months of age, are more prone to shunt malfunction"),
    ("1–2", r"1–2 ans", "LACUNE", "la leçon déclare elle-même la donnée non lue"),
    ("0", r"0 à 6", "S1", "mRS : échelle 0 à 6 (borne d'échelle ; relevée)"),
    ("6", r"0 à 6", "S1", "mRS : échelle 0 à 6"),
    ("142", r"Étude de 142", "S7", "Patients (n = 142)"),
    ("13", r"13 centres", "S7", "by 13 centres"),
    ("2", r"ETV|2 ans", "S2", "ETV-CPC is typically used in children younger than 2 years old"),
    ("200", r".", "S1", "CSF pressure of 200 mmH2O or less"),
    ("91.0", r".", "S16", "code CIM"), ("91.1", r".", "S16", "code CIM"), ("91.2", r".", "S16", "code CIM"),
    ("91.20", r".", "S16", "code CIM"), ("91.21", r".", "S16", "code CIM"), ("91.29", r".", "S16", "code CIM"),
    ("91.3", r".", "S16", "code CIM"), ("91.8", r".", "S16", "code CIM"), ("91.9", r".", "S16", "code CIM"),
    ("91.7", r".", "S16", "code CIM"), ("37.1", r".", "S16", "code CIM"),
]


def concordance(item: dict) -> dict | None:
    v = item["valeur"].replace(" ", " ")
    for valeur, ctx, src, cit in C:
        if v == valeur and re.search(ctx, item["contexte"]):
            return {"source": src, "citation": cit}
    return None


# ---------------------------------------------------------------- recalculs
def r(id_, attendu, trouve, formule, source, tol, note=""):
    ecart = None if (attendu is None or trouve is None) else round(trouve - attendu, 4)
    if trouve is None:
        verdict = "INFORMATIF"  # grandeur dérivée par l'audit, absente de la leçon
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


def recalculs() -> list[dict]:
    R = []
    pct = lambda a, b: round(100 * a / b, 1)
    # AVIM — taux annuels moyens (division simple, sans actualisation)
    R.append(r("R01", round(100 * 4 / 8 / 8, 2), 6.0, "4/8 évolués en 8 ans → borne basse annuelle", "S1 (AVIM)", 0.3,
               "4/8 = 50 % ; 50/8 = 6,25 %/an et 50/4 = 12,5 %/an : fourchette 6–12 % cohérente"))
    R.append(r("R02", round(100 * 4 / 8 / 4, 2), 12.0, "4/8 évolués en 4 ans → borne haute annuelle", "S1 (AVIM)", 0.6))
    R.append(r("R03", round(100 * 27 / 52 / 3, 1), 17.0, "27/52 en 3 ans, taux moyen annuel", "S1 (AVIM)", 0.5,
               "27/52 = 51,9 % ; /3 = 17,3 %/an"))
    # Triade complète, enquête japonaise
    R.append(r("R04", pct(184, 1524), 12.1, "184/1524 (effectif entier le plus proche de 12,1 %)", "S1", 0.05))
    # Lausanne
    R.append(r("R05", pct(81, 86), 94.2, "81/86 plaintes de marche", "S8", 0.05))
    R.append(r("R06", pct(65, 86), 75.6, "65/86 plaintes cognitives", "S8", 0.05))
    R.append(r("R07", pct(52, 86), 60.5, "52/86 plaintes urinaires", "S8", 0.05))
    R.append(r("R08", pct(28, 86), 32.6, "28/86 femmes (contrôle de cohérence de la source)", "S8", 0.05))
    R.append(r("R09", pct(27, 44), None, "27/44 recommandés = 61,4 % (non écrit dans la leçon)", "S8", 0,
               "valeur dérivée non affichée ; aucune erreur"))
    k16 = [pct(k, 16) for k in range(17)]
    R.append(r("R10", min(k16, key=lambda x: abs(x - 92)), 92.0,
               "92 % de 16 opérés : 0,92 × 16 = 14,72 ; aucun effectif entier k/16 ne donne 92 % (14/16 = 87,5 ; 15/16 = 93,8)",
               "S8 (« Among the 12 patients seen at the first postoperative consultation »)", 0.5,
               "le dénominateur réel est 12 patients revus : 11/12 = 91,7 % ≈ 92 % (voir C08)"))
    R.append(r("R11", pct(11, 12), 92.0, "11/12 patients revus à 6 semaines", "S8", 0.5))
    # Signes frontaux, série de 26
    for i, (k, v) in enumerate([(22, 84), (20, 77), (17, 65), (16, 61)]):
        R.append(r(f"R12{chr(97 + i)}", pct(k, 26), float(v), f"{k}/26", "S1 (série de 26)", 0.6,
                   "16/26 = 61,5 % : la source arrondit à 61 % (troncature)" if k == 16 else ""))
    apathie = [pct(k, 26) for k in range(27)]
    R.append(r("R13", min(apathie, key=lambda x: abs(x - 70.3)), 70.3,
               "70,3 % attribué à la série de 26 (fenêtre g91-front) : 18/26 = 69,2 ; 19/26 = 73,1",
               "S1 (70,3 % vient d'une enquête BPSD distincte)", 0.05, "attribution erronée (voir C12)"))
    # Urinaire 90,9 / 74,5 : cohérence avec un effectif de 55
    R.append(r("R14", pct(50, 55), 90.9, "50/55 (contrôle de cohérence)", "S1", 0.05))
    R.append(r("R15", pct(41, 55), 74.5, "41/55 (contrôle de cohérence)", "S1", 0.05))
    # PENS
    R.append(r("R16", round(0.23 - 0.03, 2), 0.21, "différence = 0,23 − 0,03", "S5", 0.01,
               "la source publie 0,21 calculé sur des moyennes non arrondies : écart d'arrondi (voir C19)"))
    R.append(r("R17", pct(23, 50), 46.0, "chutes placebo 23/50", "S5 (99 randomisés : 50/49)", 0.5))
    R.append(r("R18", pct(12, 50), 24.0, "chutes valve ouverte 12/50 (ou 12/49 = 24,5)", "S5", 0.5))
    R.append(r("R19", pct(6, 49), 12.0, "hématome sous-dural 6/49", "S5", 0.5))
    R.append(r("R20", round(110 * MMHG_PER_MMH2O, 1), None, "110 mmH2O = 8,1 mmHg (conversion, non écrite)", "physique", 0,
               "aucune conversion n'est écrite dans la leçon ; ajoutée par l'audit pour la sémiologie"))
    R.append(r("R21", round(200 * MMHG_PER_MMH2O, 1), None, "200 mmH2O = 14,7 mmHg (conversion, non écrite)", "physique", 0))
    R.append(r("R22", 120.0, 120.0, "12 cmH2O = 120 mmH2O (cohérence avec l'unité des critères)", "physique", 0))
    # Eu-iNPH
    R.append(r("R23", 13 + 15, 28.0, "complications 13 % + 15 %", "S7", 0))
    R.append(r("R24", round(100 * 115 / 142, 1), None, "115 réexaminés / 142 inclus = 81,0 % ; les pourcentages portent sur 115",
               "S7", 0, "dénominateur non précisé dans la leçon (voir C11)"))
    # BASICS
    R.append(r("R25", pct(32, 533), 6.0, "32/533", "S6", 0.05))
    R.append(r("R26", pct(12, 535), 2.2, "12/535", "S6", 0.05))
    R.append(r("R27", pct(31, 526), 5.9, "31/526", "S6", 0.05))
    R.append(r("R28", round((12 / 535) / (32 / 533), 2), 0.38, "risque relatif brut 2,24/6,00 comparé au HR 0,38",
               "S6", 0.02, "HR à risques concurrents 0,38 et RR brut 0,37 : cohérents"))
    # Bâle, double tâche
    resp_tot = 122 - 9
    seul_dt = resp_tot - 84
    R.append(r("R29", pct(seul_dt, resp_tot), 25.7, f"répondeurs uniquement en double tâche = {seul_dt}/{resp_tot}", "S9", 0.05,
               "25,7 % des répondeurs, et non « 25,7 % de répondeurs supplémentaires »"))
    R.append(r("R30", pct(seul_dt, 84), 25.7,
               "« répondeurs supplémentaires » rapportés aux répondeurs de marche simple = 29/84",
               "S9", 0.5, "lecture de la phrase de la leçon : 34,5 % attendu (voir C09)"))
    # Lewy
    R.append(r("R31", pct(21, 127), None, "21/127 = 16,5 % (non écrit)", "S1", 0))
    # Épidémiologie : « facteur supérieur à dix »
    f_min = (1.5 / 100) / (60 / 100000)
    R.append(r("R32", round(f_min, 1), None,
               "rapport minimal imagerie/critères (1,5 %) sur cas diagnostiqués (60/100 000, ≥ 65 ans) = 25 ; > 10 vrai",
               "S1", 0, "affirmation « facteur supérieur à dix » : vraie (25 à 1850 selon les couples comparés)"))
    # Coût-efficacité
    R.append(r("R33", round(13000 / 1.7), None, "13 000 € / 1,7 QALY = 7647 €/QALY (non écrit)", "S1", 0))
    # Acétazolamide
    R.append(r("R34", 3 * 8, 24.0, "8 mg/kg/dose × 3 = 24 mg/kg/j (bas de fourchette)", "S18", 0))
    R.append(r("R35", 3 * 10, 30.0, "10 mg/kg/dose × 3 = 30 mg/kg/j (haut de fourchette) ≤ 100 mg/kg/j", "S18", 0))
    for kg in (10, 20, 40, 60):
        R.append(r(f"R36_{kg}kg", 100 * kg, 100.0 * kg,
                   f"plafond 100 mg/kg/j × {kg} kg = {100 * kg} mg/j ; FI adulte per os ≤ 1000 mg/j (glaucome, épilepsie)",
                   "S18 ; FI Diamox® juillet 2026, Posologie", 0,
                   "aucun plafond absolu dans la ligne Swisspeddose « pression intracrânienne élevée » ; "
                   "dépasse 1000 mg/j dès 10 kg (voir C05)" if kg >= 20 else ""))
    R.append(r("R37", 250 / 250, 1.0, "comprimé Diamox® 250 mg sécable : 8 mg/kg × 31 kg = 248 mg ≈ 1 comprimé", "FI Diamox®", 0,
               "arrondi au dosage commercialisé suisse (250 mg sécable en deux) ; exemple de l'audit"))
    # Vignettes : comparaison au seuil
    R.append(r("R38", 1.0, 1.0 if 0.36 > 0.3 else 0.0, "index d'Evans 0,36 > 0,3 (cas 0 et cas récapitulatif)", "S1", 0))
    R.append(r("R39", 1.0, 1.0 if 0.34 > 0.3 else 0.0, "index d'Evans 0,34 > 0,3 (cas 1)", "S1", 0))
    R.append(r("R40", 1.0, 1.0 if 170 <= 200 else 0.0, "170 mmH2O ≤ 200 (cas 1)", "S1", 0))
    R.append(r("R41", 1.0, 1.0 if 180 <= 200 else 0.0, "180 mmH2O ≤ 200 (cas récapitulatif)", "S1", 0))
    R.append(r("R42", 1.0, 1.0 if 30 <= 40 <= 50 else 0.0, "retrait 40 mL dans 30–50 mL (cas récapitulatif)", "S1", 0))
    R.append(r("R43", 1.0, 1.0 if 30 <= 50 <= 50 else 0.0, "retrait 50 mL dans 30–50 mL (cas 2)", "S1", 0))
    # Exemples de la source (figure z-EI et BVR), utiles pour la sémiologie d'imagerie
    R.append(r("R44", round(46.7 / 95.0, 2), 0.49, "z-EI = 46,7/95,0 (figure 5 de la source)", "S1, Fig. 5", 0.005))
    R.append(r("R45", round(28.1 / 46.7, 1), 0.6, "BVR au niveau AC = 28,1/46,7 (figure 5 de la source)", "S1, Fig. 5", 0.05))
    # Prévalence ESO : vérification de cohérence d'unités
    R.append(r("R46", 70 / 2, 35.0, "seuil des centres éloignés = moitié du seuil standard (70/2)", "S3", 0))
    # Ventricules : 12 mmH2O vs 12 cmH2O, mélange d'unités
    R.append(r("R47", 110 / 10, None, "valve PENS 110 mmH2O = 11 cmH2O ; leçon mélange mmH2O (PENS, critères) et cmH2O (réglage)",
               "physique", 0, "aucune erreur, mais unité à harmoniser (MINEUR, intégré à C19)"))
    return R


def main() -> None:
    inv = inventaire()
    res = recalculs()
    for it in inv:
        if it["categorie"] == "GRANDEUR":
            c = concordance(it)
            if c:
                it["verification"] = "CONCORDANCE_SOURCE" if c["source"] not in ("VIGNETTE", "LACUNE") else c["source"]
                it.update(c)
            else:
                it["verification"] = "NON_RAPPROCHEE"
    nr = [i for i in inv if i.get("verification") == "NON_RAPPROCHEE"]
    (HERE / "inventaire.json").write_text(json.dumps({
        "total_releves": len(inv),
        "grandeurs": sum(1 for i in inv if i["categorie"] == "GRANDEUR"),
        "non_calculables": sum(1 for i in inv if i["categorie"] != "GRANDEUR"),
        "concordance_source": sum(1 for i in inv if i.get("verification") == "CONCORDANCE_SOURCE"),
        "vignettes": sum(1 for i in inv if i.get("verification") == "VIGNETTE"),
        "lacune_declaree": sum(1 for i in inv if i.get("verification") == "LACUNE"),
        "non_rapprochees": len(nr),
        "items": inv}, ensure_ascii=False, indent=1), encoding="utf-8")
    calculables = [x for x in res if x["attendu"] is not None or x["verdict"] == "NON_VERIFIABLE"]
    cnt = {k: sum(1 for x in res if x["verdict"] == k) for k in ("CORRECT", "ARRONDI", "FAUX", "NON_VERIFIABLE", "INFORMATIF")}
    (HERE / "resultats.json").write_text(json.dumps({
        "calculables": sum(1 for x in res if x["verdict"] != "INFORMATIF"),
        "recalcules": sum(1 for x in res if x["verdict"] != "INFORMATIF"),
        "informatifs_audit": cnt["INFORMATIF"], "verdicts": cnt, "resultats": res}, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"relevés {len(inv)} ; grandeurs {sum(1 for i in inv if i['categorie'] == 'GRANDEUR')} ; "
          f"non rapprochées {len(nr)} ; recalculs {len(res)} {cnt}")
    for i in nr:
        print("  NR", i["id"], i["fichier"][-9:], i["valeur"], "|", i["contexte"][:110])
    for x in res:
        if x["verdict"] in ("FAUX", "ARRONDI"):
            print("  ", x["id"], x["verdict"], x["attendu"], x["trouve"], x["formule"][:90])


if __name__ == "__main__":
    main()
