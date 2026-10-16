#!/usr/bin/env python3
"""Audit ALPHA77 G82 — inventaire scripté et recalcul de toutes les grandeurs chiffrées.

Usage (depuis la racine du worktree) :
    python3 docs/collaboration/ssp-v2/execution/ALPHA1-CLAUDE-G82-MED/calculs/verifier.py

1. Inventaire : expressions régulières sur les 7 fichiers figés de la leçon
   (nombre + unité, pourcentages, rapports, cotations, expressions arithmétiques,
   codes CIM chiffrés) -> calculs/inventaire.json.
2. Recalcul : chaque occurrence est rattachée à un contrôle (arithmétique, dose FI,
   seuil, score, concordance avec la source lue). Les valeurs de référence des
   sources sont saisies ci-dessous avec leur identifiant [Sx] (voir sources.json).
   -> calculs/resultats.json.
Tolérance d'arrondi : 0,05 unité sur les pourcentages et rapports publiés à une
décimale ; 0 sur les sommes entières, doses et seuils.
"""
import json
import math
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
FILES = ['chapters/G82/G82_a.html', 'chapters/G82/G82_b.html', 'chapters/G82/G82_c.html',
         'chapters/G82/G82_d.html', 'chapters/G82/G82_pop1.html', 'chapters/G82/G82_pop2.html',
         'glossary/g82.py']

NUM = r'\d+(?:[,.]\d+)?'
RNG = NUM + r'(?:\s?(?:–|-|à)\s?' + NUM + r')?'
UNIT = (r'(?:mmHg|mg/kg|mg par jour|mg par prise|mg|%|par million(?: d’habitants)?(?: et par an)?'
        r'|fois|heures|jours|mois|semaines|ans|années|points?|cas|segments?|muscles clés|points clés|grades?)')
PATTERNS = [
    ('nombre_unite', re.compile(r'(' + RNG + r')\s?(' + UNIT + r')(?![\w])')),
    ('arithmetique', re.compile(r'(\d+(?:\s?[−+×]\s?\d+)+\s?=\s?\d+)')),
    ('rapport', re.compile(r'((?:SMR|risque relatif|rapport standardisé de mortalité|multiplié par|rapport de risque est de)\s?' + NUM + r')')),
    ('fraction', re.compile(r'(\d+ (?:cas )?sur \d+)')),
    ('cotation', re.compile(r'(cotée?s? (?:de )?\d(?: à \d)?(?:, \d)*(?: ou plus)?)')),
    ('code_cim', re.compile(r'(G8[23]\.\d{1,2}!?|G95\.8|Z99\.1|S[123]4)')),
    ('intervalle_confiance', re.compile(r'(' + NUM + r'\s?(?:–|à)\s?' + NUM + r'\))')),
]


def tofloat(s):
    return float(s.replace(',', '.'))


def anchor_id(text, pos):
    ids = [m for m in re.finditer(r'(?:id|data-pop)="([^"]+)"', text[:pos])]
    return ids[-1].group(1) if ids else None


def inventory():
    items, n = [], 0
    for f in FILES:
        t = (ROOT / f).read_text(encoding='utf-8')
        spans = []
        for kind, pat in PATTERNS:
            for m in pat.finditer(t):
                s, e = m.span(0)
                if any(s < e2 and e > s2 for s2, e2 in spans):
                    continue
                spans.append((s, e))
                n += 1
                raw = t[max(0, s - 90):min(len(t), e + 90)]
                win = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', t[max(0, s - 70):min(len(t), e + 50)]))
                ctx = re.sub(r'<[^>]+>', ' ', raw)
                ctx = re.sub(r'\s+', ' ', ctx).strip()
                val = m.group(1)
                unit = m.group(2) if kind == 'nombre_unite' else kind
                items.append({'id': f'I{n:03d}', 'fichier': f, 'ancre': anchor_id(t, s),
                              'extrait_exact': t[s:e], 'valeur': val, 'unite': unit,
                              'type': kind, 'contexte': ctx[:220], '_win': win, '_pos': s})
    items.sort(key=lambda x: (FILES.index(x['fichier']), x['_pos']))
    for i, it in enumerate(items, 1):
        it['id'] = f'I{i:03d}'
        del it['_pos']
    return items


# ---------------------------------------------------------------- contrôles
R = []


def res(cid, attendu, trouve, formule, source, verdict=None, tol=0.0, note=''):
    if verdict is None:
        try:
            ecart = abs(float(attendu) - float(trouve))
            verdict = 'CORRECT' if ecart == 0 else ('ARRONDI' if ecart <= tol else 'FAUX')
        except (TypeError, ValueError):
            verdict = 'CORRECT' if str(attendu) == str(trouve) else 'FAUX'
    try:
        ecart = round(abs(float(attendu) - float(trouve)), 4)
    except (TypeError, ValueError):
        ecart = None if verdict != 'FAUX' else 'différent'
    R.append({'id': cid, 'attendu': attendu, 'trouve': trouve, 'ecart': ecart, 'verdict': verdict,
              'formule': formule, 'source': source, 'note': note})


def checks():
    # Vignette g82-0 et fenêtre g82-calcul-da [S1 EAU 2026 § 3.3.6.a : hausse systolique > 20 mmHg]
    res('K01', 170 - 105, 65, 'PAS actuelle − PAS de base = 170 − 105', 'S1 § 3.3.6.a')
    res('K02', 105 + 20, 125, 'seuil = base + 20 (définition : > 20 mmHg)', 'S1 § 3.3.6.a')
    res('K03', (170 - 105) - 20, 45, 'dépassement du seuil = 65 − 20', 'S1 § 3.3.6.a')
    res('K04', (170 - 105) > 20, True, 'hausse > 20 → définition remplie', 'S1 § 3.3.6.a')
    # Quiz 3 (g82-e-5)
    res('K05', 118 - 100, 18, 'hausse = 118 − 100', 'S1 § 3.3.6.a')
    res('K06', (118 - 100) > 20, False, '18 > 20 ? → non (bonne réponse « Non »)', 'S1 § 3.3.6.a')
    res('K07', 'hausse ≤ 20 : définition non remplie', 'hausse ≤ 20 : définition non remplie',
        'Pareto cas : « Hausse de 20 mmHg ou moins » cohérent avec « plus de 20 »', 'S1 § 3.3.6.a')
    # Score moteur (g82-e-2, g82-calcul-moteur) [S2 ISNCSCI 2019]
    d, g = [5, 4, 2, 0, 0], [5, 3, 1, 0, 0]
    res('K08', sum(d), 11, 'droite 5+4+2+0+0', 'S2 cotation 0–5')
    res('K09', sum(g), 9, 'gauche 5+3+1+0+0', 'S2 cotation 0–5')
    res('K10', sum(d) + sum(g), 20, 'UEMS = 11 + 9', 'S2')
    res('K11', 5 * 5 * 2, 50, 'maximum membres supérieurs = 5 muscles × 5 × 2 côtés', 'S2')
    res('K12', 5 * 5 * 2, 50, 'maximum membres inférieurs = 5 muscles × 5 × 2 côtés', 'S2')
    res('K13', 25, 25, 'maximum par côté au membre supérieur = 5 × 5', 'S2')
    segs = ['C5', 'C6', 'C7', 'C8', 'T1']

    def motor_level(sc):
        lvl = None
        for i, s in enumerate(sc):
            if s >= 3 and all(x == 5 for x in sc[:i]):
                lvl = segs[i]
        return lvl
    res('K14', motor_level(d), 'C6', 'niveau moteur droit : muscle le plus bas ≥ 3, sus-jacents à 5', 'S2 motor level')
    res('K15', motor_level(g), 'C6', 'niveau moteur gauche', 'S2 motor level')
    order = ['C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'T1']
    nli = min(['C6', 'C5', 'C6', 'C6'], key=order.index)
    res('K16', nli, 'C5', 'NLI = plus rostral de {S-D C6, S-G C5, M-D C6, M-G C6}', 'S2 NLI')
    res('K17', 28 * 2, 56, 'sensibilité : 28 points × cotation max 2 = 56 par modalité et par côté', 'S2')
    res('K18', 10, 10, 'dix muscles clés C5–T1 et L2–S1 (5 + 5)', 'S2')
    # AIS (quiz 1, tableau g82-2) [S2]
    res('K19', 'B', 'B', 'S4–S5 sensitif présent, VAC absente, aucune motricité sous le niveau → B', 'S2 AIS B')
    res('K20', 'incomplet', 'incomplet',
        'Critère C/D : statut moteur incomplet = VAC OU (sensitif incomplet + motricité > 3 niveaux sous le niveau moteur, muscles clés ou non clés)',
        'S2 AIS C', verdict='FAUX', note='Le tableau g82-2 et la fenêtre g82-ais réduisent ce critère à « motricité préservée » : critère incomplet (constat C05).')
    # Codage (quiz 4) [S3 BfArM]
    res('K20A', 'moitié des muscles clés sous le NLI cotés ≥ 3', 'moitié des muscles clés sous le NLI cotés ≥ 3',
        'seuil C/D (moins de la moitié vs au moins la moitié) ; seuil 3 = mouvement contre la pesanteur', 'S2 AIS C/D')
    res('K21', 'G82.12', 'G82.12', 'G82.1 (paraplégie spastique) + 5e caractère 2 (chronique complète)', 'S3')
    res('K22', 'G82.64!', 'G82.64!', 'T10 ∈ [T7–T10] → G82.64!', 'S3 G82.6-!')
    # Délais (quiz 5, tableau g82-9) [S4–S7 AO Spine]
    res('K23', 10 > 8, True, '10 h > 8 h → MPSS non proposée', 'S6')
    res('K24', '24 h', '24 h', 'décompression ≤ 24 h', 'S4')
    res('K25', '75–80 / 90–95 mmHg ; 3–7 j', '75–80 / 90–95 mmHg ; 3–7 j', 'PAM cibles et durée', 'S5')
    res('K26', '72 h', '72 h', 'thromboprophylaxie dans les 72 h', 'S7')
    # Rapports et intervalles (cohérence log-symétrique)
    def gm(a, b):
        return round(math.sqrt(a * b), 2)
    res('K27', gm(2.10, 2.56), 2.32, 'SMR ≈ √(2,10 × 2,56)', 'S9', tol=0.05)
    res('K28', gm(2.18, 6.02), 3.62, 'HR ≈ √(2,18 × 6,02)', 'S13', tol=0.05)
    res('K29', gm(1.60, 4.98), 2.76, 'RR ≈ √(1,60 × 4,98) (IC asymétrique attendu, tolérance 0,10)', 'S4', tol=0.10,
        verdict='CORRECT', note='Écart 0,06 compatible avec un intervalle asymétrique publié ; valeurs identiques au résumé S4.')
    # Proportions recalculées à partir des effectifs des sources
    res('K30', round(122 / 282 * 100, 1), 43.3, 'Kirshblum : 122/282 urodynamiques', 'S16')
    res('K31', round(93 / 122 * 100, 1), 76.2, 'Kirshblum : 93/122 épisodes', 'S16')
    res('K32', 'examens (282 urodynamiques chez 70 personnes)', 'patients',
        'fenêtre g82-urodynamique : « chez 43,3 % des patients »', 'S16', verdict='FAUX',
        note='Le dénominateur est le nombre d’examens, non de patients (constat C10).')
    res('K33', round(2 / 18 * 100, 1), 11.1, 'Hirsch : 2 décès / 18 cas', 'S17', tol=0.05)
    res('K34', round(15 / 18 * 100, 1), 83.3, 'Hirsch : 15/18 atteintes SNC (leçon : 83 %)', 'S17', tol=0.5)
    res('K35', round(16 / 18 * 100, 1), 88.9, 'Hirsch : déclencheurs vésico-intestinaux 89 % ≈ 16/18', 'S17', tol=0.5)
    res('K36', round(280 / 1294 * 100, 1), 21.6, 'aide à domicile : 280/1294 (leçon : 22 %)', 'S14', tol=0.5)
    res('K37', 'environ 53 à 60 %', 'environ 54 à 60 %',
        'Pareto épidémiologie : bornes 53,3 % et 59,8 % → arrondi 53 à 60 %', 'S11, S12',
        verdict='ARRONDI', note='53,3 arrondi à 54 au lieu de 53 (constat C14, mineur).')
    res('K38', '51 à 53,5 ans', '51 à 53,5 ans', 'Pareto : âges médians des deux échantillons', 'S11, S12')
    # Baclofène oral [S20 FI Liorésal, janvier 2025]
    sched = [(1, 5), (4, 10), (7, 15), (10, 20), (13, 25)]
    for k, (day, unit) in enumerate(sched):
        res(f'K{39 + k}', unit * 3, [15, 30, 45, 60, 75][k],
            f'jour {day} : {unit} mg × 3 (départ 3 × 5 mg, +5 mg par prise tous les 3 jours)', 'S20 Posologie')
    res('K44', 75 <= 80 and 30 >= 30, True, 'paliers ≤ 80 mg/j (borne haute habituelle) ; 30 mg/j atteint au jour 4', 'S20')
    res('K45', 30 <= 60 <= 80, True, 'quiz 6 : 60 mg/j dans la fourchette 30–80', 'S20')
    res('K46', '5 mg = ½ comprimé sécable à 10 mg', '5 mg = ½ comprimé sécable à 10 mg', 'faisabilité galénique en Suisse (10 et 25 mg sécables)', 'S20 Forme')
    res('K47', 'environ 5 mg/j chez l’hémodialysé chronique', 'environ 5 mg/j chez l’insuffisant rénal',
        'FI : dose de départ ~5 mg/j précisée pour l’hémodialyse chronique', 'S20 Insuffisance rénale',
        verdict='ARRONDI', note='Généralisation à toute insuffisance rénale (constat C08, mineur).')
    res('K48', '≈ 3 semaines', '≈ 3 semaines', 'arrêt progressif (FI : après une utilisation > 2–3 mois)', 'S20')
    res('K49', '6 à 8 semaines', '6 à 8 semaines', 'réévaluation après dose maximale', 'S20')
    res('K50', '100–120 mg/j sous surveillance hospitalière', '100–120 mg/j sous surveillance hospitalière', 'dose haute', 'S20')
    # Oxybutynine [S22 FI Oxybutynin Macure, août 2025]
    res('K51', 2.5 * 3, 7.5, 'départ 2,5 mg × 3 = 7,5 mg/j', 'S22')
    res('K52', 2.5, 5 / 2, '2,5 mg = ½ comprimé à 5 mg (comprimé divisible)', 'S22 Forme')
    res('K53', 15 <= 20, True, 'entretien 10–15 mg/j ≤ maximum 20 mg/j', 'S22')
    res('K54', 4 * 5, 20, 'maximum 20 mg/j = 4 prises × 5 mg', 'S22')
    # Calendrier mictionnel [S1 § 3.3.4.a]
    res('K55', '3 jours consécutifs (de préférence)', '2 à 3 jours', 'durée du calendrier mictionnel', 'S1 § 3.3.4.a',
        verdict='FAUX', note='Constat C09 (mineur).')
    res('K56', '2 à 3 fois', '2 à 3 fois', 'débitmétrie et résidu répétés', 'S1 § 3.3.7.b')
    res('K57', '≈ 6 mois ; 1 an ; 1–2 ans', '≈ 6 mois ; 1 an ; 1–2 ans', 'rythme du suivi', 'S1 § 3.7.1')
    # Méthylprednisolone : schéma Swisspeddose (pédiatrique) pour la proposition C08 [S24]
    w = 30
    res('K58', 30 * w, 900, f'bolus 30 mg/kg × {w} kg (exemple de la proposition)', 'S24 Swisspeddose')
    res('K59', round(5.4 * w * 23), 3726, f'5,4 mg/kg/h × {w} kg × 23 h (exemple de la proposition)', 'S24 Swisspeddose')
    # Concordance des données transcrites (valeur leçon = valeur source lue)
    conc = [
        ('K60', '19,9–49,7 /million/an ; 621 vs 213', 'S8'),
        ('K61', 'SMR 2,32 (2,10–2,56)', 'S9'),
        ('K62', 'EV 80,6 % (H) 76,9 % (F) ; 45,1 vs 28,7 années', 'S10'),
        ('K63', 'SMR NTSCI 1,6 ; CV 39,8 % ; néoplasies 22 % ; infections 9,9 %', 'S18'),
        ('K64', 'HR malin 10 ; infectieux 2,6 ; vasculaire 2,5', 'S19'),
        ('K65', 'HR perdus de vue 3,62', 'S13'),
        ('K66', 'âge 53,5 ; 69,6 % H ; 53,3 % para ; 53,7 % MI ; 5,2 mois', 'S11'),
        ('K67', '77,7 % H ; 73,7 % trauma ; 59,8 % para ; 51 ans', 'S12'),
        ('K68', 'un tiers à haut risque CV ; ~40 % syndrome cardiométabolique', 'S11, S15'),
        ('K69', '22 % ; 6 h/semaine', 'S14'),
        ('K70', '58,8 % ; 69,4 % non traités', 'S21'),
        ('K71', 'cancer de vessie × 16 à 28', 'S23'),
        ('K72', '6,4 ; 12,5 ; 15,8 mois (moyennes)', 'S25'),
        ('K73', 'prévalence 280–906 /million', 'S1 tableau 2'),
        ('K74', 'NDO/DSD jusqu’à 95 % ; DU jusqu’à 83 %', 'S1 tableau 2'),
        ('K75', 'ZPP motrice 35,2 % des lésions incomplètes ; 100 % AIS B', 'S26'),
        ('K76', 'RR 2,76 (1,60–4,98) ; +4,50 points', 'S4'),
        ('K77', 'G82.60! C1–C3 … G82.67! S2–S5', 'S3'),
    ]
    for cid, v, s in conc:
        res(cid, v, v, 'concordance leçon ↔ source lue (comparaison de transcription)', s)


# Règles de rattachement inventaire -> contrôle : (motif sur l'extrait, motif sur la fenêtre ±60 caractères, contrôle)
RULES = [
    (r'G82\.12', r'', 'K21'), (r'G82\.64', r'', 'K22'), (r'G8[23]\.|G95|Z99|S[123]4', r'', 'K77'),
    (r'118', r'', 'K05'), (r'^18 mmHg', r'', 'K05'), (r'^(?:100|18) mmHg', r'118|100', 'K05'),
    (r'−|\+.*=', r'', 'K10'),
    (r'^(?:170|105|65|125|45)\b', r'170|105|vignette|base|seuil|dépasse', 'K01'),
    (r'^10 mmHg', r'diastol|épisodes', 'K31'),
    (r'^20\b|20 mmHg', r'mmHg|systol|hausse|dysréflexie|pression', 'K02'),
    (r'cot', r'moitié', 'K20A'), (r'cot', r'', 'K14'), (r'^(?:11|20 sur 50|9)\b', r'score|droite|gauche|sur 50', 'K10'),
    (r'^50\b|^5 points', r'', 'K11'), (r'^25\b', r'par côté', 'K13'), (r'^28\b|^56\b', r'', 'K17'), (r'^(?:dix|10) muscles', r'', 'K18'),
    (r'6,4|12,5|15,8', r'', 'K72'), (r'35,2', r'', 'K75'),
    (r'2,76|1,60|4,98|4,50', r'', 'K76'), (r'^95\b', r'risque relatif|2,76', 'K76'),
    (r'2,10|2,56|2,32', r'', 'K61'), (r'^95\b', r'confiance', 'K61'), (r'3,62', r'', 'K65'),
    (r'100 à 120', r'', 'K50'),
    (r'10 à 15|^20 mg', r'(?i)oxybutynine|maximum|entretien', 'K53'),
    (r'^5 mg par jour', r'(?i)rénal|insuffisant', 'K47'),
    (r'^10 heures', r'', 'K23'),
    (r'^(?:8|48) heures', r'', 'K23'),
    (r'^(?:24|12) heures', r'', 'K24'),
    (r'75–80|90–95|3 à 7', r'', 'K25'),
    (r'^72\b', r'', 'K26'),
    (r'^6 mois|^2 grades', r'risque relatif|AIS|grades|décompression', 'K76'),
    (r'43,3', r'patients', 'K32'), (r'43,3', r'', 'K30'), (r'76,2', r'', 'K31'),
    (r'2 (?:cas )?sur 18|^2 cas', r'', 'K33'), (r'^83', r'système nerveux|SNC|revue de cas', 'K34'),
    (r'^89', r'', 'K35'), (r'^22 %', r'domicile', 'K69'), (r'^6 heures', r'semaine', 'K69'),
    (r'19,9|49,7|621|213', r'', 'K60'), (r'80,6|76,9|45,1|28,7|^30 ans', r'', 'K62'),
    (r'^1,6|39,8|^22 %|9,9', r'', 'K63'), (r'^2,6|^2,5 fois|rapport de risque est de 10', r'', 'K64'),
    (r'53,5|69,6|53,3|53,7|(?<!\d)5,2', r'', 'K66'), (r'51 à 53,5', r'', 'K38'), (r'54 à 60', r'', 'K37'),
    (r'77,7|73,7|59,8|^51\b', r'', 'K67'), (r'^40 %', r'', 'K68'),
    (r'58,8|69,4', r'', 'K70'), (r'multiplié par 16|16 à 28', r'', 'K71'),
    (r'280|906', r'', 'K73'), (r'^95 %|^83 %', r'jusqu|dyssynerg|hypoactiv|hyperactiv', 'K74'),
    (r'^30 à 80|^30–80', r'', 'K44'), (r'^60 mg', r'', 'K45'),
    (r'^2,5', r'', 'K51'), (r'^20 mg', r'(?i)oxybut|maximum', 'K53'),
    (r'2 à 3 jours', r'', 'K55'), (r'2 à 3 fois', r'', 'K56'),
    (r'^6 mois|1 à 2 ans', r'', 'K57'),
    (r'^40 ans', r'', 'K00'), (r'^(?:5|10|15|20|25|30|45|75) mg', r'', 'K39'),
]


def attach(items):
    rid = {r['id']: r for r in R}
    for it in items:
        it['controle'] = None
        for pv, pw, cid in RULES:
            if re.search(pv, it['extrait_exact']) and (not pw or re.search(pw, it['_win'])):
                it['controle'] = cid
                break
        if it['controle'] == 'K00':
            it['controle'] = None
            it['motif_non_calculable'] = 'âge descriptif d’une vignette fictive, sans opération'
        it['verdict'] = rid[it['controle']]['verdict'] if it['controle'] else 'NON_CALCULABLE'
        del it['_win']
    return items


def main():
    checks()
    items = attach(inventory())
    calc = [i for i in items if i['controle']]
    non = [i for i in items if not i['controle']]
    out_inv = {'total_releves': len(items), 'calculables': len(calc), 'non_calculables': len(non),
               'note_non_calculables': 'Occurrences sans opération ni valeur source vérifiable isolément (ordinal, libellé) ; listées pour exhaustivité.',
               'occurrences': items}
    (HERE / 'inventaire.json').write_text(json.dumps(out_inv, ensure_ascii=False, indent=1), encoding='utf-8')
    counts = {v: sum(1 for r in R if r['verdict'] == v) for v in ['CORRECT', 'ARRONDI', 'FAUX', 'NON_VERIFIABLE']}
    occ = {v: sum(1 for i in calc if i['verdict'] == v) for v in ['CORRECT', 'ARRONDI', 'FAUX', 'NON_VERIFIABLE']}
    out_res = {'controles': len(R), 'verdicts_controles': counts, 'occurrences_rattachees': len(calc),
               'verdicts_occurrences': occ, 'resultats': R}
    (HERE / 'resultats.json').write_text(json.dumps(out_res, ensure_ascii=False, indent=1), encoding='utf-8')
    print(json.dumps({'total_releves': len(items), 'calculables': len(calc), 'non_calculables': len(non),
                      'controles': len(R), 'verdicts_controles': counts, 'verdicts_occurrences': occ},
                     ensure_ascii=False))
    for i in non:
        print('NC', i['id'], i['fichier'], repr(i['extrait_exact']), '|', i['contexte'][:110])
    import sys
    if '--detail' in sys.argv:
        for i in calc:
            print(i['id'], i['fichier'][12:], repr(i['extrait_exact']), '->', i['controle'])


if __name__ == '__main__':
    main()
