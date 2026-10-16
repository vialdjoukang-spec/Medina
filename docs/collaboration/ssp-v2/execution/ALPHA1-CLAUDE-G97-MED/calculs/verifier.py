#!/usr/bin/env python3
"""Audit ALPHA1-CLAUDE-G97-MED — inventaire exhaustif et recalcul des grandeurs de la leçon G97.

Exécution (depuis la racine du worktree) :
    python3 docs/collaboration/ssp-v2/execution/ALPHA1-CLAUDE-G97-MED/calculs/verifier.py

Sorties : calculs/inventaire.json (toute occurrence numérique des 7 fichiers) et
calculs/resultats.json (recalculs scriptés, verdicts CORRECT|ARRONDI|FAUX|NON_VERIFIABLE).
Lecture seule des sources canoniques ; aucune écriture hors du dossier calculs/.
Les données des énoncés sont celles de la leçon ; les données de contrôle sont celles des
sources lues par l'audit (identifiants [Sx] de sources.json de ce dossier).
"""
import json
import math
import re
from html.parser import HTMLParser
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]  # racine du worktree
FILES = [
    "chapters/G97/G97_a.html", "chapters/G97/G97_b.html", "chapters/G97/G97_c.html",
    "chapters/G97/G97_d.html", "chapters/G97/G97_pop1.html", "chapters/G97/G97_pop2.html",
    "glossary/g97.py",
]

# ---------------------------------------------------------------- 1. inventaire
NUM = r"(?<![\w.,])(\d{1,3}(?:[   ]\d{3})+|\d+(?:,\d+)?)"
UNITS = [
    "× 10⁹/L", "mL/min", "mm de LCR", "mL", "mg", "cm", "%", "points", "G", "heures", "heure",
    "jours", "jour", "semaines", "semaine", "mois", "ans", "an", "kg", "essais", "participants",
    "patients", "patientes", "parturientes", "enfants", "femmes", "études", "publications",
    "procédures", "centres", "pays", "blood patchs", "médecins", "recommandations", "critères",
]
UNIT_RE = re.compile(NUM + r"\s*(" + "|".join(re.escape(u) for u in UNITS) + r")?")


class Extract(HTMLParser):
    """Collecte le texte visible avec l'ancre la plus proche (data-evidence, id, data-pop)."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.chunks = [], []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        anchor = a.get("data-evidence") or a.get("data-pop") or a.get("id") or a.get("data-k")
        if tag in ("br", "img", "path", "rect", "circle"):
            return
        self.stack.append((tag, anchor))

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                del self.stack[i:]
                break

    def handle_data(self, data):
        if not data.strip():
            return
        anchor = next((a for _, a in reversed(self.stack) if a), None)
        self.chunks.append((anchor, data))


def classify(ctx, value, unit):
    """Nature de l'occurrence : code, numérotation, date, vignette ou valeur médicale."""
    left = ctx[: ctx.find(value)] if value in ctx else ctx
    tail = left[-14:]
    if re.search(r"G ?97[.\d]*$|ICHD-3? ?$|rubrique ?$|7\.2\.?$|CIM-10-GM ?$|\bG$", tail) or re.search(r"G97\.\d", ctx[max(0, ctx.find(value) - 4): ctx.find(value) + 4] if value in ctx else ""):
        return "code_ou_rubrique"
    if re.search(r"(Cas|Figure|Fiche|îlot|Partie|e-|p-|n°|\()\s*$", tail) or re.fullmatch(r"\d\.\d", value):
        return "numerotation"
    if re.fullmatch(r"(19|20)\d\d", value) and not unit:
        return "date"
    if unit in ("ans",) and re.search(r"(femme|patiente?|homme|accouchée|enfant|jeune)[^.]{0,40}$", left[-60:]):
        return "vignette"
    return "valeur"


def inventory():
    occ = []
    for f in FILES:
        raw = (ROOT / f).read_text(encoding="utf-8")
        if f.endswith(".py"):
            chunks = [(None, s) for s in re.findall(r"'([^'\n]*)'", raw)]
        else:
            p = Extract()
            p.feed(raw)
            chunks = p.chunks
        for anchor, text in chunks:
            for m in UNIT_RE.finditer(text):
                value, unit = m.group(1), (m.group(2) or "")
                s, e = max(0, m.start() - 70), min(len(text), m.end() + 70)
                ctx = re.sub(r"\s+", " ", text[s:e]).strip()
                occ.append({
                    "id": f"N{len(occ) + 1:04d}", "fichier": f, "ancre": anchor, "valeur": value,
                    "unite": unit, "nature": classify(ctx, value, unit), "contexte": ctx,
                })
    return occ


# ------------------------------------------------------------------- 2. recalculs
def verdict(attendu, trouve, tol_arrondi, tol_exact=1e-9):
    ecart = abs(attendu - trouve)
    if ecart <= tol_exact:
        return "CORRECT", ecart
    if ecart <= tol_arrondi:
        return "ARRONDI", ecart
    return "FAUX", ecart


def r1(x):
    return round(x + 1e-12, 1)


CHECKS = []


def check(cid, description, attendu, trouve, tol, formule, source, ancre, note="", force=None):
    v, ecart = verdict(attendu, trouve, tol)
    if force:
        v = force
    CHECKS.append({
        "id": cid, "description": description, "attendu": round(attendu, 4), "trouve": trouve,
        "ecart": round(ecart, 4), "tolerance": tol, "verdict": v, "formule": formule,
        "source": source, "ancre": ancre, "note": note,
    })


# 2.1 Aiguille atraumatique (Nath 2018 [S7])
check("K01", "Différence absolue d'incidence", 11.0 - 4.2, 6.8, 0.05,
      "DA = I_conv − I_atr = 11,0 − 4,2 (points)", "S7, résultats", "G97-C0249 ; G97-C0039 ; G97-C0351")
check("K02", "Nombre à traiter à partir des incidences", 1 / 0.068, 14.7, 0.05,
      "NNT = 1 / 0,068", "S7 (incidences) ; calcul de la leçon", "G97-C0351")
check("K03", "Nombre à traiter arrondi à l'entier supérieur", math.ceil(1 / 0.068), 15, 0,
      "NNT arrondi par excès = ⌈14,7⌉", "convention d'arrondi du nombre à traiter", "G97-C0039 ; G97-C0255")
check("K04", "Nombre à traiter par le risque relatif publié appliqué au risque de base",
      1 / (0.110 * (1 - 0.40)), 15, 0.5, "NNT = 1 / (I_conv × (1 − RR)) = 1 / (0,110 × 0,60) = 15,2",
      "S7 (RR 0,40)", "G97-C0039",
      note="Les deux méthodes convergent vers environ 15 ; la leçon reste correcte.")
check("K05", "Rapport brut des incidences comparé au RR publié", 4.2 / 11.0, 0.40, 0.03,
      "4,2 / 11,0 = 0,382 ; RR publié 0,40 (IC 0,34–0,47)", "S7", "G97-C0253 ; G97-C0347",
      note="Le RR poolé des essais n'est pas le rapport des incidences poolées ; 0,382 est dans l'IC publié. "
           "« 40 % de l'autre » reste exact pour le RR publié.")
check("K06", "« divise le risque par plus de deux »", 11.0 / 4.2, 2.62, 0.01,
      "11,0 / 4,2 = 2,62 > 2 ; 1 / 0,40 = 2,5 > 2", "S7", "G97-C0065")
check("K07", "« réduit le risque de plus de moitié »", (1 - 0.40) * 100, 60, 0.5,
      "1 − RR = 0,60 > 0,50", "S7", "G97-C0476")
check("K08", "Cohérence du RR et de son IC (moyenne géométrique des bornes)",
      math.sqrt(0.34 * 0.47), 0.40, 0.01, "√(0,34 × 0,47) = 0,400", "S7", "G97-C0039")
check("K09", "Non-chevauchement des IC des deux incidences", 1.0, 1.0 if 5.2 < 9.1 else 0.0, 0,
      "borne haute atraumatique 5,2 < borne basse conventionnelle 9,1", "S7", "G97-C0344")
check("K10", "Figure 3 : largeur de barre proportionnelle (atraumatique)", 330 * 4.2 / 11.0, 126, 0.5,
      "330 × 4,2 / 11,0 = 126,0 unités SVG", "G97_c.html, figure 3", "Figure 3 — Incidences comparées")

# 2.2 Mutisme (Grønbæk 2021 [S16] ; Laustsen 2026 [S18] ; Grønbæk 2022 [S17])
check("K11", "Trouble de la parole postopératoire 112/376", r1(112 / 376 * 100), 30, 0.5,
      "112 / 376 = 29,8 % (arrondi à l'entier)", "S16, résultats", "G97-C0063 ; G97-C0367", force=None)
check("K12", "Mutisme 53/376", r1(53 / 376 * 100), 14, 0.5, "53 / 376 = 14,1 %", "S16", "G97-C0063")
check("K13", "Parole réduite 59/376", r1(59 / 376 * 100), 16, 0.5, "59 / 376 = 15,7 %", "S16", "G97-C0063")
check("K14", "Somme mutisme + parole réduite", 53 + 59, 112, 0, "53 + 59 = 112", "S16", "G97-C0063")
check("K15", "Hydrocéphalie préopératoire 515/800", r1(515 / 800 * 100), 64, 0.5, "515 / 800 = 64,4 %",
      "S18, résultats", "G97-C0078",
      note="Dénominateur 800 (35 centres, 13 pays), distinct de la cohorte de 376 enfants citée juste avant : voir constat C10.")
for cid, (lo, hi, pt, lab) in {
    "K16": (0.14, 0.77, 0.34, "vermis"), "K17": (0.07, 0.70, 0.23, "hémisphère"),
    "K18": (1.47, 5.60, 2.85, "médulloblastome"), "K19": (2.10, 54.45, 10.30, "tumeur tératoïde/rhabdoïde"),
    "K20": (0.46, 1.73, 0.89, "voie transvermienne"), "K21": (0.60, 2.41, 1.20, "hydrocéphalie ajustée"),
}.items():
    g = math.sqrt(lo * hi)
    check(cid, f"Cohérence OR/IC ({lab})", g, pt, max(0.05 * pt, 0.02) if cid != "K19" else 0.5,
          f"√({lo} × {hi}) = {g:.3f}", "S16 / S18", "G97-C0078 ; G97-C0373",
          note="Contrôle de vraisemblance de la recopie : l'OR doit être proche de la moyenne géométrique des bornes.")

# 2.3 Blood patch (Tomala 2023 [S24] ; Gupta 2022 [S27])
check("K22", "Échec genevois 55/212", r1(55 / 212 * 100), 25.9, 0.05, "55 / 212 = 25,94 %", "S24",
      "G97-C0474 ; G97-C0489")
check("K23", "OR profondeur > 5,5 cm et IC", math.sqrt(1.26 * 7.49), 3.08, 0.05, "√(1,26 × 7,49) = 3,07", "S24", "G97-C0474")
check("K24", "OR intervalle > 48 h et IC", math.sqrt(0.05 * 0.83), 0.20, 0.01, "√(0,05 × 0,83) = 0,204", "S24", "G97-C0474")
check("K25", "EPiMAP échec 167/591", r1(167 / 591 * 100), 28.3, 0.05, "167 / 591 = 28,26 %", "S27", "G97-C0474 ; G97-C0490")
check("K26", "EPiMAP succès complet 195/591", r1(195 / 591 * 100), 33.0, 0.05, "195 / 591 = 32,99 %", "S27", "G97-C0490")
check("K27", "EPiMAP succès partiel 229/591", r1(229 / 591 * 100), 38.7, 0.05, "229 / 591 = 38,75 %", "S27", "G97-C0490",
      note="38,748 % : 38,7 est l'arrondi exact au dixième.")
check("K28", "EPiMAP somme des trois issues", 28.3 + 33.0 + 38.7, 100.0, 0.05, "28,3 + 33,0 + 38,7", "S27", "G97-C0490")
check("K29", "« sept patientes sur dix » (succès complet ou partiel)", (195 + 229) / 591 * 10, 7, 0.5,
      "(195 + 229) / 591 = 71,7 %", "S27", "G97-C0491")
check("K30", "EPiMAP second patch 126 → 19,8 %", r1(126 / 643 * 100), 19.8, 0.05,
      "126 / 643 = 19,6 % ; 126 / 591 = 21,3 % ; 19,8 % suppose ≈ 636", "S27", "G97-C0490",
      note="Dénominateur non publié dans le résumé ; chiffre recopié fidèlement de la source.", force="NON_VERIFIABLE")
check("K31", "Pareto « échec de 26 à 28 % »", round(25.9), 26, 0, "arrondi de 25,9 et 28,3 à l'entier", "S24 ; S27", "G97-C0502")
check("K32", "Données complètes EPiMAP 591/643", r1(591 / 643 * 100), 91.9, 0.05, "591 / 643 = 91,9 %", "S27", "sources")

# 2.4 Suivi à 5 ans (Weiss 2025 [S28])
check("K33", "Effectifs 113 + 113 + 110 = 336", 113 + 113 + 110, 336, 0, "somme des groupes", "S28", "G97-C0473")
check("K34", "Groupes céphalée 54 + 56 = 110", 54 + 56, 110, 0, "54 sans patch + 56 avec patch", "S28", "G97-C0473")
check("K35", "Céphalée chronique après péridurale simple 5,3 %", r1(6 / 113 * 100), 5.3, 0.05, "6 / 113 = 5,31 %", "S28", "G97-C0473")
check("K36", "Céphalée chronique sans péridurale 0,9 %", r1(1 / 113 * 100), 0.9, 0.05, "1 / 113 = 0,88 %", "S28", "G97-C0473")
w_patch = [k for k in range(57) if abs(k / 56 * 100 - 20.4) < 0.05]
w_nopatch = [k for k in range(55) if abs(k / 54 * 100 - 21.4) < 0.05]
check("K37", "20,4 % « avec blood patch » (n = 56) : numérateur entier possible ?", 1.0 if w_patch else 0.0, 1.0, 0,
      "k / 56 = 20,4 % sans k entier (11/56 = 19,6 ; 12/56 = 21,4) ; 11/54 = 20,4 et 12/56 = 21,4",
      "S28 (résumé)", "G97-C0473 ; G97-C0488",
      note="Les pourcentages correspondent exactement aux effectifs inversés (20,4 % = 11/54 ; 21,4 % = 12/56), "
           "alors que les témoins correspondent aux effectifs initiaux. Inversion probable des étiquettes dans le résumé, "
           "ou perdues de vue : non tranchable sans le texte intégral. Voir constat C11.", force="NON_VERIFIABLE")
check("K38", "« environ une femme sur cinq »", 20.9 / 100 * 5, 1, 0.1, "20,4–21,4 % ≈ 1/5", "S28", "G97-C0477")

# 2.5 Hématome (Chen 2022 [S10] ; Djurasovic 2021 [S11])
check("K39", "0,52 % compris dans l'étendue 0,10–0,69 %", 1.0, 1.0 if 0.10 <= 0.52 <= 0.69 else 0.0, 0,
      "0,10 ≤ 0,52 ≤ 0,69", "S10 ; S11", "G97-C0040 ; G97-C0174")
check("K40", "« environ 0,5 % »", 0.52, 0.5, 0.05, "0,52 ≈ 0,5", "S10", "G97-C0065 ; G97-C0425")
for cid, (pt, lo, hi, lab) in {
    "K41": (2.9, 0.6, 8.4, "déformation"), "K42": (1.12, 0.6, 2.0, "dégénératif"), "K43": (0.30, 0.6, 8.4, "tumeur"),
    "K44": (0.44, 0.6, 8.4, "anticoagulation"), "K45": (0.42, 0.3, 0.6, "sans anticoagulation"),
    "K46": (1.94, 0.9, 4.3, "mini-invasive"), "K47": (0.42, 0.3, 0.6, "ouverte"),
}.items():
    ok = lo <= pt <= hi
    check(cid, f"Estimation dans son IC publié ({lab})", 1.0, 1.0 if ok else 0.0, 0,
          f"{lo} ≤ {pt} ≤ {hi} % (IC du résumé converti en %)", "S10 (résumé)", "G97-C0043 à G97-C0061",
          note="" if ok else "Incohérence interne de la source : l'estimation sort de son propre IC (IC recopié de la "
                              "déformation). La leçon recopie fidèlement le point mais tire une conclusion (« ne modifie pas ») "
                              "d'une donnée dont l'IC est erroné. Voir constat C12.",
          force=None if ok else "NON_VERIFIABLE")
check("K48", "Mini-invasive / ouverte ≈ « cinq fois » (source)", 1.94 / 0.42, 4.6, 0.05, "1,94 / 0,42 = 4,62", "S10", "G97-C0062")

# 2.6 Céphalée chronique (Kraus 2024 [S26] ; Zander 2025 [S29])
check("K49", "Liquide épidural 9/83", r1(9 / 83 * 100), 11, 0.5, "9 / 83 = 10,8 %", "S29", "G97-C0478 ; G97-C0494")
check("K50", "Même proportion rapportée aux 86 patients (lecture du texte)", r1(9 / 86 * 100), 11, 0.5,
      "9 / 86 = 10,5 % → 10 % ; la leçon écrit « chez 86 patients … 11 % d'entre eux »", "S29", "G97-C0478",
      note="Le dénominateur réel est 83 (imagerie adéquate). Écart d'arrondi sans conséquence : constat MINEUR C13.")

# 2.7 Posologies (FI suisses lues le 16.10.2026 [S21] [S22])
check("K51", "Paracétamol : 1000 mg × 4 prises (intervalle 6 h) ≤ 4000 mg", 1000 * 24 / 6, 4000, 0,
      "dose max par prise × 24 h / intervalle", "S21, Posologie", "G97-C0291 ; G97-C0292")
check("K52", "Paracétamol, ClCr 10–50 : 3000 mg / (24/6) = 750 mg par prise maximum", 3000 / (24 / 6), 750, 0,
      "plafond / nombre de prises à 6 h", "S21, Troubles de la fonction rénale", "G97-C0299 ; G97-C0300",
      note="Cohérent : la dose par prise doit descendre à 750 mg si l'intervalle est de 6 h, ou rester à 1000 mg toutes les 8 h.")
check("K53", "Paracétamol, ClCr < 10 : 2000 mg / 3 prises = 667 mg par prise", 2000 / (24 / 8), 666.67, 0.01,
      "plafond / nombre de prises à 8 h", "S21", "G97-C0303 ; G97-C0304")
check("K54", "Paracétamol 9–12 ans (30–40 kg) : 2000 mg ≤ 75 mg/kg × 30 kg", 75 * 30, 2250, 0,
      "75 mg/kg/j × 30 kg = 2250 mg ≥ 2000 mg", "S21, Patients pédiatriques", "G97-C0296 ; G97-C0167")
check("K55", "Ibuprofène : 800 mg × 3 = 2400 mg", 800 * 3, 2400, 0, "dose max par prise × 3", "S22, Céphalées, migraines",
      "G97-C0307 ; G97-C0308")
check("K56", "Ibuprofène 800 mg réalisable avec les dosages suisses (200/400/600 mg)", 2 * 400, 800, 0, "2 × 400 mg",
      "S22, Forme pharmaceutique", "G97-C0307")
check("K57", "Paracétamol, insuffisance hépatique, alcoolisme, malnutrition, déshydratation : plafond", 2000, 4000, 0,
      "FI : « La dose quotidienne ne doit pas dépasser 2 g » ; la leçon ne donne que 4000 mg", "S21, Troubles hépatiques",
      "G97-C0315 ; G97-C0316 ; G97-C0174", note="Plafond réduit absent de la leçon : constat MAJEUR C03.", force="FAUX")
check("K58", "Caféine 900 mg/j ; 200–300 mg/j si allaitement", 900, 900, 0, "valeurs recopiées du consensus", "S5, question 5",
      "G97-C0150 ; G97-C0166 ; G97-C0312")
check("K59", "Plaquettes 70 000 × 10⁶/L = 70 × 10⁹/L", 70000e6 / 1e9, 70, 0, "70 000 × 10⁶ / 10⁹", "S5",
      "G97-C0153 ; G97-C0399")
check("K60", "Pression < 60 mm de LCR en kPa (eau, ρ ≈ 1000 kg/m³)", 60e-3 * 1000 * 9.80665 / 1000, 0.59, 0.01,
      "P = ρ g h = 0,060 m × 9,807 m/s² × 1000 kg/m³ = 588 Pa = 0,59 kPa ≈ 4,4 mmHg", "S2 (seuil) ; physique",
      "G97-C0035 ; G97-C0201", note="Conversion proposée en enrichissement (non présente dans la leçon).")

# 2.8 Cohérences temporelles des cas et quiz
for cid, (val, lim, op, lab, anc) in {
    "K61": (3, 5, "<=", "quiz 7.4 : 3 jours ≤ 5", "G97-C0118"),
    "K62": (8, 5, ">", "cas 2 : 8 jours > 5 → imagerie", "G97-C0225"),
    "K63": (30, 48, "<", "cas 4 : 30 h < 48 h → répétition plus probable", "G97-C0482"),
    "K64": (30, 48, "in24-48", "quiz 12 : 30e heure dans 24–48 h", "G97-C0175"),
    "K65": (4, 5, "<=", "cas 1 : 4e jour ≤ 5", "G97-C0223"),
    "K66": (4, 5, "<=", "cas 11.6 : 4e jour ≤ 5", "G97-C0171"),
    "K67": (31, 31, "in31-50", "quiz 7.4 : 31 ans dans la tranche ICHD 31–50 ans", "G97-C0118"),
    "K68": (14, 14, "==", "forme chronique > 14 jours = 2 semaines de rémission", "G97-C0472"),
}.items():
    ok = {"<=": val <= lim, ">": val > lim, "<": val < lim, "==": val == lim,
          "in24-48": 24 <= val <= 48, "in31-50": 31 <= val <= 50}[op]
    check(cid, lab, 1.0, 1.0 if ok else 0.0, 0, f"{val} {op} {lim}", "S3 ; S5 ; S11", anc)

# 2.9 Cohérence inter-fichiers des valeurs-clés (même chiffre partout)
KEYVALS = ["4000 mg", "2400 mg", "900 mg", "200 à 300 mg", "70 × 10⁹/L", "60 mm de LCR", "15 à 20 mL", "33 à 91 %",
           "25,9 %", "28,3 %", "11,0 %", "4,2 %", "0,40", "0,52 %", "381"]



# 2.11 Valeurs introduites par les propositions de l'audit (recalculées avant proposition)
check("K69", "Proposition figure 3 : 16 unités × 11,0", 16 * 11.0, 176, 0, "16 × 11,0 = 176", "propositions/G97_c_figures.html", "Figure 3 (proposition)")
check("K70", "Proposition figure 3 : 16 unités × 4,2", 16 * 4.2, 67, 0.5, "16 × 4,2 = 67,2 → 67", "propositions/G97_c_figures.html", "Figure 3 (proposition)")
check("K71", "Kraus 2024 : nausées 14/30", r1(14 / 30 * 100), 47, 0.5, "14 / 30 = 46,7 %", "S26, tableau 1", "propositions/G97_c_semio.html")
check("K72", "Kraus 2024 : acouphènes 8/30", r1(8 / 30 * 100), 27, 0.5, "8 / 30 = 26,7 %", "S26, tableau 1", "propositions/G97_c_semio.html")
check("K73", "Kraus 2024 : raideur de nuque 9/30", r1(9 / 30 * 100), 30, 0.05, "9 / 30 = 30,0 %", "S26, tableau 1", "propositions/G97_c_semio.html")
check("K74", "Lybecker 1995 : 75 céphalées / 1021 rachianesthésies", r1(75 / 1021 * 100), 7.35, 0.05, "75 / 1021 = 7,35 %", "S31, résumé", "propositions/G97_pop1_semio.html")
check("K75", "Lybecker 1995 : guérison spontanée 45/75", r1(45 / 75 * 100), 60, 0.05, "45 / 75 = 60 %", "S31, résumé", "propositions/G97_c_semio.html")
check("K76", "Seuil 60 mm de LCR ≈ 0,6 kPa (proposition)", 0.588, 0.6, 0.05, "0,588 kPa arrondi à 0,6", "S2 ; physique", "propositions/G97_c_2.html")


def crossfile(occ):
    blob = {f: (ROOT / f).read_text(encoding="utf-8") for f in FILES}
    out = []
    for kv in KEYVALS:
        n = sum(t.count(kv) for t in blob.values())
        out.append({"valeur": kv, "occurrences": n, "fichiers": [f for f, t in blob.items() if kv in t]})
    contradictions = []
    allt = " ".join(blob.values())
    for pat, bad in [(r"caféine[^.]{0,80}(\d{3,4}) mg par jour", {"900", "200", "300"}),
                     (r"plaquettes d’au moins (\d+)", {"70"})]:
        for m in re.finditer(pat, allt):
            if m.group(1) not in bad:
                contradictions.append(m.group(0))
    return out, contradictions


# 2.10 Confrontation des valeurs rapportées (non calculables) aux sources lues par l'audit.
# Valeurs relues mot à mot dans la source (résumé PubMed/Europe PMC, FI AmiKo, ICHD-3, consensus JAMA Netw Open).
SOURCE_VALUES = {
    "S2": ["60"], "S3": ["5", "2", "31", "50"],
    "S5": ["5", "48", "900", "300", "200", "70", "15", "20", "30", "33", "91", "24", "22", "2", "40", "142", "8", "14"],
    "S6": ["50"],
    "S7": ["11,0", "4,2", "0,40", "0,34", "0,47", "9,1", "13,3", "3,3", "5,2", "110", "31 412", "95", "6,8", "0,068", "14,7", "15"],
    "S10": ["0,52", "40", "2,9", "1,12", "0,30", "0,32", "0,84", "0,63", "0,24", "0,70", "1,94", "0,44", "0,42", "0,16", "0,5"],
    "S11": ["0,10", "0,69", "24", "48"],
    "S16": ["25", "26", "9", "376", "112", "30", "14", "16", "2,85", "10,30", "0,34", "0,23", "0,89", "1", "0", "10", "4",
            "2", "50"],
    "S17": ["1,08"], "S18": ["64", "1,20", "800"], "S19": ["9"], "S20": ["0,23", "6", "704", "24"], "S23": ["50", "75"],
    "S24": ["47 920", "212", "25,9", "55", "5,5", "3,08", "1,26", "7,49", "0,20", "0,05", "0,83", "0,38", "6,3", "4", "29",
            "2001", "2018"],
    "S26": ["30", "31", "381", "5", "14"], "S27": ["643", "28,3", "33,0", "38,7", "19,8", "26", "28"],
    "S28": ["336", "113", "110", "20,4", "21,4", "5,3", "0,9", "16,1", "20,8", "5"],
    "S29": ["86", "2,0", "11"],
    "S21": ["4000", "2000", "3000", "500", "1000", "40", "9", "12", "10", "50", "6", "8"],
    "S22": ["400", "800", "2400", "30"],
}


def confront(occ):
    check_anchors = set()
    for c in CHECKS:
        for a in re.split(r"\s*;\s*|\s+à\s+", c["ancre"]):
            check_anchors.add(a.strip())
    stats = {"recalcul_script": 0, "confronte_source": 0, "contexte_seul": 0}
    for o in occ:
        if o["nature"] != "valeur":
            o["controle"] = "non calculable (" + o["nature"] + ")"
            continue
        v = o["valeur"].replace(" ", " ").replace(" ", " ")
        if o["ancre"] in check_anchors:
            o["controle"] = "recalcul scripté (voir resultats.json, ancre " + str(o["ancre"]) + ")"
            stats["recalcul_script"] += 1
            continue
        hit = [s for s, vals in SOURCE_VALUES.items() if v in vals]
        if hit:
            o["controle"] = "valeur rapportée confrontée à " + ", ".join(hit[:3])
            stats["confronte_source"] += 1
        else:
            o["controle"] = "contrôle contextuel manuel (compte, rang ou durée sans source chiffrée)"
            stats["contexte_seul"] += 1
    return stats


def main():
    occ = inventory()
    conf = confront(occ)
    by_nature = {}
    for o in occ:
        by_nature[o["nature"]] = by_nature.get(o["nature"], 0) + 1
    (HERE / "inventaire.json").write_text(json.dumps({
        "methode": "Extraction regex du texte visible (HTMLParser) des 7 fichiers et des chaînes du glossaire ; "
                   "chaque nombre est relevé avec son unité éventuelle et son ancre la plus proche "
                   "(data-evidence, data-pop, id ou data-k).",
        "total_occurrences": len(occ), "par_nature": by_nature, "controle_des_valeurs": conf,
        "occurrences": occ,
    }, ensure_ascii=False, indent=1), encoding="utf-8")
    cross, contra = crossfile(occ)
    counts = {}
    for c in CHECKS:
        counts[c["verdict"]] = counts.get(c["verdict"], 0) + 1
    res = {
        "calculables": len(CHECKS), "recalcules": len(CHECKS), "verdicts": counts,
        "resultats": CHECKS, "coherence_inter_fichiers": cross, "contradictions_inter_fichiers": contra,
    }
    (HERE / "resultats.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"inventaire : {len(occ)} occurrences {by_nature}")
    print(f"recalculs : {len(CHECKS)} {counts} ; contradictions inter-fichiers : {len(contra)}")
    for c in CHECKS:
        if c["verdict"] != "CORRECT":
            print(" ", c["id"], c["verdict"], c["description"])


if __name__ == "__main__":
    main()
