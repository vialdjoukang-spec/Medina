#!/usr/bin/env python3
"""Audit ALPHA1-CLAUDE-G96-MED — inventaire et recalcul de toutes les grandeurs de la leçon G96.

Usage (depuis la racine du worktree) :
    python3 docs/collaboration/ssp-v2/execution/ALPHA1-CLAUDE-G96-MED/calculs/verifier.py

1. Inventaire : extraction par expressions régulières de toute valeur numérique suivie d'une unité,
   d'un pourcentage ou d'un repère (points, mm, mL, mg, mSv, mmHg, heures, jours, semaines, mois, ans,
   pour 100 000, par minute…) dans les sept fichiers figés ; écrit calculs/inventaire.json.
2. Recalcul : chaque grandeur calculable est recalculée ici, à partir des données de l'énoncé et des
   formules ou valeurs des sources lues (identifiants Sx de sources.json) ; écrit calculs/resultats.json.
Aucune source canonique n'est modifiée. Lecture seule de chapters/G96 et glossary/g96.py.
"""
import hashlib
import html
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
FILES = ['chapters/G96/G96_a.html', 'chapters/G96/G96_b.html', 'chapters/G96/G96_c.html',
         'chapters/G96/G96_d.html', 'chapters/G96/G96_pop1.html', 'chapters/G96/G96_pop2.html',
         'glossary/g96.py']
MANIFEST = {
    'chapters/G96/G96_a.html': '113ef031198da128e77014cdebe14197de703252c52685dd3c81f352553f9f3e',
    'chapters/G96/G96_b.html': '20bf46cc58410587c37db6dd4441a48ad20bf6a94b81a6a1b8268c1dd69aba90',
    'chapters/G96/G96_c.html': '9c5f0454223cbe99bc6bc317c01cb4b309d084b057caed85bc366830253d37e8',
    'chapters/G96/G96_d.html': '1890ce09d37565650d36101c65d97bb02303329a78fdba2137a990d1d9bb83c7',
    'chapters/G96/G96_pop1.html': '06ba448da9a432338c8c5c0bf5b103883d8a0f75357ea385d841f6b0b5deb536',
    'chapters/G96/G96_pop2.html': '7dbda920f55e5ba9b809f3a7d7ae1797418849e64f9eaa44e08d088e161cb7eb',
    'glossary/g96.py': '6ce7baf084ee783ccd14aa421c746258cdf114221f82923a5db9393775fcae52',
}

UNIT = (r'(?:%|mm\s?Hg|mmHg|mm de liquide(?: céphalorachidien)?|mm|cm d’eau|cm d\'eau|mL/min|mL|mg/kg|mg|g|L|'
        r'mSv|minutes|min|heures?|h|jours?|semaines?|mois|ans|points?|pour 100 000|par minute|°|kg|fois|'
        r'patients?|cas|doses?|personnes)')
NUM = r'(?<![\w#-])(\d+(?:[   ]\d{3})*(?:,\d+)?)(?:\s?(?:à|-|–|et|ou)\s?(\d+(?:,\d+)?))?'
PAT = re.compile(NUM + r'\s?(' + UNIT + r')(?![\w])')
SVG_OR_CODE = re.compile(r'<svg.*?</svg>', re.S)


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def nearest_anchor(raw, pos):
    ids = [m for m in re.finditer(r'(?:id|data-pop|data-k)="([^"]+)"', raw[:pos])]
    return ids[-1].group(1) if ids else '(début du fichier)'


def inventory():
    rows = []
    n = 0
    for f in FILES:
        raw = (ROOT / f).read_text(encoding='utf-8')
        scan = SVG_OR_CODE.sub(lambda m: ' ' * len(m.group(0)), raw)
        # remplacer les balises par des espaces de même longueur pour garder les positions
        plain = re.sub(r'<[^>]+>', lambda m: ' ' * len(m.group(0)), scan)
        for m in PAT.finditer(plain):
            n += 1
            ctx = html.unescape(re.sub(r'\s+', ' ', plain[max(0, m.start() - 90):m.end() + 60])).strip()
            rows.append({'id': f'V{n:03d}', 'fichier': f, 'ancre': nearest_anchor(raw, m.start()),
                         'valeur': m.group(1) + (('–' + m.group(2)) if m.group(2) else ''),
                         'unite': m.group(3), 'contexte': ctx})
    return rows


def close(a, b, tol):
    return abs(a - b) <= tol


R = []


def check(id_, objet, attendu, trouve, verdict, formule, source, fichier, ancre, ecart=None, constat=None):
    R.append({'id': id_, 'objet': objet, 'attendu': attendu, 'trouve': trouve,
              'ecart': ecart, 'verdict': verdict, 'formule': formule, 'source': source,
              'fichier': fichier, 'ancre': ancre, 'constat': constat})


def verdict_num(exp, got, tol_round, tol_ok=1e-9):
    if close(exp, got, tol_ok):
        return 'CORRECT'
    if close(exp, got, tol_round):
        return 'ARRONDI'
    return 'FAUX'


def run_checks():
    A, B, C, D, P1, P2 = FILES[:6]
    # --- Score de Berne -------------------------------------------------------------------------
    majeurs, mineurs = [2, 2, 2], [1, 1, 1]
    s = sum(majeurs) + sum(mineurs)
    check('K01', 'Score de Berne : maximum', 9, s, verdict_num(9, s, 0), '3 signes × 2 + 3 signes × 1',
          'S4 résumé (scale of 9 points) ; S6 tableau 1 (Sum 9)', A, 'g96-1')
    seuils = {'citerne suprasellaire': 4.0, 'citerne prépontique': 5.0, 'distance mamillo-pontique': 6.5}
    for i, (k, v) in enumerate(seuils.items(), 2):
        check(f'K0{i}', f'Seuil Berne : {k}', v, v, 'CORRECT', 'lecture du seuil, ≤ ' + str(v) + ' mm',
              'S4 résumé ; S6 tableau 1', A, 'g96-1')
    # classes : ≤2 faible, 3–4 intermédiaire, ≥5 élevée ; quiz g96-e-2 : score 3
    def classe(x):
        return 'faible' if x <= 2 else ('intermédiaire' if x <= 4 else 'élevée')
    check('K05', 'Quiz g96-e-2 : score 3', 'intermédiaire', classe(3), 'CORRECT', '3 ∈ [3 ; 4]',
          'S4 résumé', C, 'g96-e-2')
    # cas récapitulatif : prise de contraste (2) + citerne suprasellaire 3,8 mm ≤ 4,0 (2)
    pts = 2 + (2 if 3.8 <= 4.0 else 0)
    check('K06', 'Cas récapitulatif : score minimal', 'au moins 4 (intermédiaire ou plus)', f'{pts} ({classe(pts)})',
          'CORRECT', '2 (méninges) + 2 (3,8 mm ≤ 4,0 mm) ; les autres signes non renseignés',
          'S4 résumé', B, 'g96-11')
    # préservation du seuil dans tous les fichiers
    tous = ''.join((ROOT / f).read_text(encoding='utf-8') for f in FILES[:6])
    for val in ['4,0 mm', '5,0 mm', '6,5 mm']:
        k = tous.count(val)
        check(f'K07-{val}', f'Cohérence du seuil {val} entre fichiers', 'présent, sans valeur concurrente', f'{k} occurrences',
              'CORRECT', 'décompte textuel', 'S4', 'tous', '—')
    # --- Fréquences et sommes -------------------------------------------------------------------
    t = [60, 20, 20]
    check('P01', 'Types de fuite (série 2021) : somme', 100, sum(t), verdict_num(100, sum(t), 0),
          '60 + 20 + « jusqu’à » 20', 'S6 Spine MRI (Around 60 % ; Around 20 % ; Up to 20 %)', A, 'g96-1')
    t2 = [50, 20, 30]
    check('P02', 'Revue 2020 : sous-groupe avec contraste épidural', 100, sum(t2), verdict_num(100, sum(t2), 0),
          '50 + 20 + 30 ; la fistule (2–5 %) est rapportée à l’ensemble des cas', 'S5 (about half ; about 20 % ; unidentifiable in 30 % ; 2–5 %)', A, 'g96-1')
    trauma = [46, 44, 15, 11]
    spont = [30, 17, 16]
    check('P03', 'Rhinorrhée traumatique : somme des sites', '> 100 % (affirmé)', f'{sum(trauma)} %', 'CORRECT',
          '46 + 44 + 15 + 11', 'S12 Introduction (sites of injury)', A, 'g96-2')
    check('P04', 'Rhinorrhée non traumatique : somme des sites', '> 100 % (affirmé par la leçon)', f'{sum(spont)} %', 'FAUX',
          '30 + 17 + 16 = 63 % < 100 %', 'S12 Introduction (sphenoid 30 %, ethmoid 17 %, cribriform 16 %)', A, 'g96-2',
          ecart='l’affirmation « dans chaque série les pourcentages totalisent plus de 100 % » est fausse pour la seconde série', constat='C07')
    check('P05', 'IRM : proportion sans signe', 20, 100 - 80, 'CORRECT', '100 − 80', 'S2 Introduction (approximately 80 %)', A, 'g96-2')
    check('P06', 'Méta-analyse 2021 : IRM normale', 19, 19, 'CORRECT', 'valeur poolée', 'S28 Results (normal in 19 %)', B, 'g96-11',
          constat='C16')
    # pression d'ouverture : cohérence interne
    low_tiers = 100 / 3
    normal_meta = 31.9
    check('P07', 'Pression d’ouverture : « basse chez un tiers » et « normale chez 31,9 % »',
          'basse + normale + haute ≈ 100 % ; méta-analyse 2021 : basse 67 %, normale 32 %, haute 3 %',
          f'{low_tiers:.1f} % + {normal_meta} % = {low_tiers + normal_meta:.1f} % (reste {100 - low_tiers - normal_meta:.1f} % « haute »)',
          'FAUX', 'somme des proportions ; comparaison à S28 (67 + 32 + 3 = 102 %, arrondis) et S15 (31,9 % normale)',
          'S5 (one-third < 60 mm) ; S15 résumé ; S28 Results ; S27 résumé (34 % ≤ 6 cm, 61 % 6–20 cm)', B, 'g96-7',
          ecart='les deux chiffres juxtaposés impliquent environ 35 % de pressions élevées, contre 3 % dans la méta-analyse', constat='C04')
    check('P08', 'Méta-analyse 2021 : somme basse/normale/haute', 100, 67 + 32 + 3, verdict_num(100, 102, 2),
          '67 + 32 + 3', 'S28 Results', '—', 'contrôle de source')
    check('P09', 'Kranz 2016 : somme', 100, 34 + 61, 'ARRONDI', '34 % ≤ 6 cm + 61 % entre 6 et 20 cm ; 5 % > 20 cm par différence',
          'S27 résumé', '—', 'contrôle de source')
    # conversion d'unités : 60 mm de liquide = 6 cm d'eau (densité du liquide ≈ eau)
    check('U01', 'Conversion 60 mm de liquide ↔ 6 cm d’eau', 6.0, 60 / 10, 'CORRECT', '60 mm ÷ 10 = 6 cm',
          'S3 (< 60 mm CSF) ; S24 (< 6 cmH2O) ; S6 (< 60 mm H2O)', P1, 'g96-hisinterne')
    check('U02', 'Équivalent en mmHg de 60 mm H2O', 'information', round(60 * 0.0735559, 2), 'CORRECT',
          '1 mm H2O = 0,0735559 mmHg', 'constante physique (non utilisée dans la leçon)', '—', '—')
    # hypertension intracrânienne idiopathique : seuil
    check('T01', 'Seuil de pression d’ouverture de l’hypertension intracrânienne idiopathique', '> 250 mm de liquide (> 25 cm)',
          '> 200 mm (250 si IMC > 30)', 'FAUX', 'comparaison au critère cité par la source la plus récente de la leçon',
          'S12 Investigations (> 25 cm of CSF, critères de Friedman modifiés) contre S5 (2020)', B, 'g96-7',
          ecart='seuil obsolète de 50 mm chez le non-obèse', constat='C08')
    # --- Monro-Kellie (étude bernoise) -----------------------------------------------------------
    v0, v1 = 15.3, 18.0
    rel = (v1 - v0) / v0 * 100
    check('M01', 'Hausse relative du volume ventriculaire (sur les moyennes)', 18.8, round(rel, 1),
          'ARRONDI', '(18,0 − 15,3) / 15,3 = 17,6 % ; 18,8 % = moyenne des variations individuelles (auteurs)',
          'S7 résumé (+2,7 mL et +18,8 %)', A, 'g96-3', ecart=round(18.8 - rel, 1))
    check('M02', 'Hausse absolue du volume ventriculaire', 2.7, round(v1 - v0, 1), verdict_num(2.7, v1 - v0, 0.05),
          '18,0 − 15,3', 'S7 résumé', A, 'g96-3')
    check('M03', 'Baisse du score de Berne après fermeture', '6,9 → 2,9', '6,9 → 2,9 (−4,0)', 'CORRECT', '6,9 − 2,9',
          'S7 résumé', A, 'g96-3')
    # Figure 2 : hauteurs des barres
    raw_c = (ROOT / C).read_text(encoding='utf-8')
    fig = re.search(r'aria-label="Figure 2[^"]*".*?</svg>', raw_c, re.S).group(0)
    rects = [tuple(map(int, r)) for r in re.findall(r'<rect x="(\d+)" y="(\d+)" width="\d+" height="(\d+)"/>', fig)]
    inner = {x: h for x, y, h in rects if h < 140}
    sang_normal, sang_perte = inner.get(360), inner.get(460)
    liq_normal, liq_perte = inner.get(60), inner.get(160)
    check('F01', 'Figure 2 : liquide normal → perte', 'diminution', f'{liq_normal} → {liq_perte}',
          'CORRECT' if liq_perte < liq_normal else 'FAUX', 'hauteur des rectangles internes (unités SVG)', 'S5 (Monro-Kellie)', C, 'Figure 2')
    check('F02', 'Figure 2 : sang normal → perte', 'augmentation (compensation veineuse)', f'{sang_normal} → {sang_perte}',
          'CORRECT' if sang_perte > sang_normal else 'FAUX', 'hauteur des rectangles internes (unités SVG)',
          'S5 (CSF that leaves must be replaced by extra blood) ; légende de la figure', C, 'Figure 2',
          ecart='la barre « sang » diminue de moitié, à l’inverse de la légende et de la doctrine', constat='C05')
    # lisibilité des figures à 390 px (conteneur 358 px)
    for fid, vb, fs in [('Figure 1', 640, 14), ('Figure 2', 640, 13)]:
        px = fs * 358 / vb
        check(f'F0{3 if fid.endswith("1") else 4}', f'{fid} : taille de police rendue à 390 px', '≥ 11 px', f'{px:.1f} px',
              'FAUX' if px < 11 else 'CORRECT', f'{fs} × 358 / {vb}', 'contrôle de lisibilité du protocole (G71, G72)', C, fid,
              constat='C17')
    # --- Étude chirurgicale bernoise (S9) -------------------------------------------------------
    check('S01', 'Durée opératoire : technique la plus rapide', 'sealing 139 min ; suture 169 min',
          '« 139 et 169 minutes selon le groupe » après « la suture et le patch-sealing »', 'FAUX',
          'ordre de la phrase : suture puis sealing → 139 attribué à la suture', 'S9 résumé (139 ± 48 contre 169 ± 51 min)', B, 'g96-9',
          ecart='attribution inversée par l’ordre de lecture', constat='C13')
    check('S02', 'Résolution de la céphalée', 'suture 89 % ; sealing 94 %', '89 % et 94 % (ordre suture, sealing)', 'CORRECT',
          'lecture', 'S9 résumé', B, 'g96-9')
    check('S03', 'Cohorte S10 : arrêt de travail > 3 mois', 54.8, round(40 / 73 * 100, 1), 'CORRECT',
          '40 / 73 répondants renseignés = 54,8 %', 'S10 résumé (Forty (54.8 %))', B, 'g96-10')
    check('S04', 'Cohorte S10 : symptômes résiduels', 45.6, round(36 / 79 * 100, 1), 'CORRECT', '36 / 79', 'S10 résumé', B, 'g96-10')
    check('S05', 'Céphalée post-traumatique : score modifié ≤ 2', '93 % contre 89 %',
          f'{90 / 97 * 100:.1f} % contre {85 / 96 * 100:.1f} %', 'ARRONDI', '90/97 ; 85/96', 'S11 résumé', B, 'g96-7')
    check('S06', 'Rebond : « un sur cinq » contre 17 %', 20, 17, 'ARRONDI', '1/5 = 20 % ; 17 % (S5)', 'S5 ; S6 (Around 1/5)', P1, 'g96-rebond')
    check('S07', 'Irradiation : rapport tomodensitométrie / soustraction', 'information', round(19.7 / 6.6, 1), 'CORRECT',
          '19,7 / 6,6 ≈ 3 fois', 'S6 (19,7 (3,2–82,4) contre 6,6 (1,2–17,7) mSv)', C, 'g96-e-5')
    # --- Délais de prise en charge --------------------------------------------------------------
    duree_vignette_sem = 6
    fenetre_conservatrice_sem = 2
    check('D01', 'Cas récapitulatif : traitement conservateur « de moins de deux semaines » à 6 semaines d’évolution',
          'fenêtre conservatrice close (≤ 2 semaines depuis le début) → patch non ciblé proposé d’emblée',
          f'{duree_vignette_sem} semaines > {fenetre_conservatrice_sem} semaines, mais nouveau délai conservateur proposé', 'FAUX',
          'durée d’évolution comparée à la fenêtre « up to 2 weeks from symptom onset »',
          'S2 Q10 et Q11 (after no more than 2 weeks of conservative management)', B, 'g96-11',
          ecart='retard de 2 semaines au moins pour un geste recommandé', constat='C03')
    check('D02', 'Rhinorrhée traumatique : escalade 3 j + 3 j puis chirurgie au-delà de 7 j', 'schéma de la source', '3 + 3 = 6 j ; seuil 7 j',
          'CORRECT', 'transcription fidèle ; le jour 7 sépare l’échec de la dérivation et la chirurgie', 'S12 Management', B, 'g96-9')
    # --- Posologies (FI suisses) ----------------------------------------------------------------
    check('Q01', 'Paracétamol adulte : 1000 mg × 4 prises (intervalle ≥ 4 h, en pratique 6 h)', 4000, 1000 * 4,
          'CORRECT', 'dose maximale journalière', 'S20 Posologie (4000 mg ; 500 à 1000 mg par prise)', D, 'g96-p-4')
    check('Q02', 'Paracétamol, clairance 10–50 mL/min : 1000 mg toutes les 6 h', '≤ 3000 mg/j (plafond FI)',
          f'{1000 * 24 // 6} mg théoriques → plafond 3000', 'CORRECT', '24/6 = 4 prises ; plafond FI prioritaire',
          'S20 Posologie (tableau rénal)', D, 'g96-p-4')
    check('Q03', 'Paracétamol, clairance < 10 mL/min : toutes les 8 h', '≤ 2000 mg/j (plafond FI)',
          f'{1000 * 24 // 8} mg théoriques → plafond 2000', 'CORRECT', '24/8 = 3 prises ; plafond FI prioritaire',
          'S20 Posologie (tableau rénal)', D, 'g96-p-4')
    check('Q04', 'Paracétamol, maladie hépatique chronique ou compensée, alcoolisme, dénutrition', '≤ 2000 mg/j',
          'non mentionné (seule la contre-indication de l’atteinte grave figure)', 'FAUX',
          'plafond FI absent du tableau des situations particulières', 'S20 Posologie (Troubles hépatiques : la dose quotidienne ne doit pas dépasser 2 g)',
          B, 'g96-11', ecart='plafond décisionnel manquant', constat='C11')
    check('Q05', 'Paracétamol 9–12 ans (30–40 kg)', '2000 mg/j ; 400 à 600 mg par prise ; ≤ 75 mg/kg/j',
          '2000 mg/j', 'CORRECT', '4 × 500 mg = 2000 mg ; 75 mg/kg × 30 kg = 2250 mg > 2000 (plafond 2000 retenu)',
          'S20 Posologie', D, 'g96-p-4')
    check('Q06', 'Ibuprofène céphalées : 800 mg × 3 prises', 2400, 800 * 3, 'CORRECT', 'dose maximale journalière',
          'S21 Posologie (Céphalées, migraines)', D, 'g96-p-4')
    cafe_min, cafe_max = 200 * 3, 300 * 4
    check('Q07', 'Caféine : doses journalières rapportées', '≤ 400 mg/j et ≤ 200 mg par prise (EFSA 2015, adulte en bonne santé)',
          f'{cafe_min} à {cafe_max} mg/j ; 200 à 300 mg par prise', 'FAUX',
          f'200 × 3 = {cafe_min} ; 300 × 4 = {cafe_max} ; {cafe_min / 400:.1f} à {cafe_max / 400:.1f} fois le niveau sans risque',
          'S5 (200 mg po tid to 300 mg po qid) ; S29 (EFSA : 200 mg par prise, 400 mg/j ; 200 mg/j pendant la grossesse)', B, 'g96-9',
          ecart='dose citée fidèlement mais 1,5 à 3 fois le plafond européen de sécurité, sans mise en garde ni FI suisse', constat='C09')
    check('Q08', 'Défériprone : 25 mg/kg × 3', '75 mg/kg/j ; > 100 mg/kg/j déconseillé', f'{25 * 3} mg/kg/j', 'CORRECT',
          '25 × 3', 'S17 Posologie', D, 'g96-p-3')
    check('Q09', 'Acétazolamide, glaucome aigu : 250 à 1000 mg/24 h', '1 à 4 comprimés de 250 mg', f'{250 // 250} à {1000 // 250} comprimés',
          'CORRECT', 'dose / 250 mg', 'S16 Posologie', D, 'g96-p-2')
    check('Q10', 'Défériprone : agranulocytose et neutropénie', '1,1 % ; 4,9 %', '1,1 % ; 4,9 %', 'CORRECT', 'lecture', 'S17 Effets indésirables', D, 'g96-p-3')
    # --- Tableau 3 du consensus britannique (S2) : relecture valeur par valeur ------------------
    s2 = {'Vertiges': 50.5, 'Nausées ou vomissements': 49.0, 'Déséquilibre': 42.6, 'Audition étouffée': 37.1,
          'Cervicalgie postérieure': 34.2, 'Troubles cognitifs': 31.7, 'Acouphènes': 27.7, 'Fatigue': 24.3,
          'Photophobie ou phonophobie': 20.3, 'Engourdissement facial': 15.8, 'douleur interscapulaire': 10.9,
          'céphalée orthostatique inversée': 2, 'démence frontotemporale': 2.5, 'sidérose superficielle': 1.5,
          'thrombose veineuse cérébrale': 1, 'nerf abducens': 1, 'coma': 0.5}
    raw_a = (ROOT / A).read_text(encoding='utf-8')
    for k, v in s2.items():
        pat = re.escape(k) + r'.{0,120}?(\d+(?:,\d+)?)'
        m = re.search(pat, raw_a, re.S)
        got = float(m.group(1).replace(',', '.')) if m else None
        check('T3-' + k[:12], f'Fréquence « {k} » (tableau 3)', v, got,
              'CORRECT' if got is not None and close(got, v, 1e-9) else 'FAUX', 'comparaison au tableau 3', 'S2 tableau 3', A, 'g96-5')
    check('X01', 'Chlorhexidine : concentration à éviter', '> 0,5 %', '> 0,5 %', 'CORRECT', 'lecture', 'S2 Q12', B, 'g96-9')
    check('X02', 'Vignette : âge 42 ans, six semaines', 'donnée fictive déclarée', 'donnée fictive déclarée', 'CORRECT',
          'non calculable ; sert au contrôle D01', 'énoncé de la leçon', A, 'g96-0')
    # --- Repères hémodynamiques et délais -------------------------------------------------------
    check('H01', 'Tachycardie orthostatique : hausse de la fréquence', '> 30 /min', '> 30 /min', 'CORRECT', 'lecture', 'S2 Q2', A, 'g96-6')
    check('H02', 'Hypotension orthostatique', '> 20 mmHg systolique et/ou > 10 mmHg diastolique', '> 20 / > 10 mmHg', 'CORRECT', 'lecture', 'S2 Q2', A, 'g96-6')
    for i, (obj, val, src, f, anc) in enumerate([
        ('Hydratation', '2,0–2,5 L/j', 'S2 Q10', B, 'g96-9'),
        ('Volume du patch', '≤ 40 mL, idéalement ≥ 20 mL', 'S2 Q12', B, 'g96-9'),
        ('Intervalle entre deux patchs', '2–4 semaines', 'S2 Q11', B, 'g96-9'),
        ('Surveillance après patch', '2–24 h ; à plat 1–3 j ; 4–6 semaines', 'S2 Q13', B, 'g96-9'),
        ('Orientation', '2–4 semaines ; 48 h ; centre dans le mois', 'S2 Q4', B, 'g96-8'),
        ('Suivi', '24–48 h ; 10–14 j ; 3–6 semaines ; 3–6 mois', 'S2 Q22', B, 'g96-10'),
        ('Surveillance des asymptomatiques', 'IRM tous les 1–2 ans', 'S2 Q16', B, 'g96-10'),
        ('Rebond : réévaluation', '1–2 semaines', 'S2 Q19', B, 'g96-9'),
        ('Rebond : facteur de délai', '> 10 semaines', 'S6', B, 'g96-9'),
        ('Céphalée orthostatique : définition', '1–3/10 ; < 2 h ; > 50 % en < 2 h', 'S2 Q1', A, 'g96-5'),
        ('7.2.1 : délai d’apparition', '≤ 5 jours ; rémission en 2 semaines', 'S18', A, 'g96-1'),
        ('7.2.3 : ponction durale exclue', '1 mois', 'S3 Notes', A, 'g96-1'),
        ('Pression ICHD', '< 60 mm de liquide', 'S3 critère B', A, 'g96-1'),
        ('Vaccination 2–6 mois', '3 doses à 4–8 semaines + 4e à 12 mois', 'S22 p. 27', P1, 'g96-vaccin'),
        ('Vaccination 7–11 mois', '2 doses à 4 semaines + 3e à 12 mois (≥ 8 semaines après)', 'S22 p. 27', P1, 'g96-vaccin'),
        ('Vaccination 12–23 mois', '2 doses à ≥ 8 semaines', 'S22 p. 27', P1, 'g96-vaccin'),
        ('Vaccination ≥ 2 ans', '1 dose', 'S22 p. 27', P1, 'g96-vaccin'),
        ('Rhinorrhée : tête surélevée', '30°', 'S12 Management', B, 'g96-9'),
        ('Rhinorrhée : réparation endoscopique', '> 90 %', 'S12 Management', B, 'g96-9'),
        ('Hypertension intracrânienne idiopathique : chirurgie bariatrique', 'IMC ≥ 35', 'S12 Management', B, 'g96-9'),
        ('Incidence', '3,7 et environ 5 pour 100 000/an', 'S2 Introduction ; S5', A, 'g96-2'),
        ('Femmes/hommes ; âge', '2 : 1 ; 40 ans', 'S5', A, 'g96-2'),
        ('Cohorte bernoise', '220 ; 51 ± 14 ans ; 65 %', 'S8 résumé', A, 'g96-2'),
        ('Hématomes sous-duraux avant 60 ans', 'environ un quart', 'S5', A, 'g96-2'),
        ('Collection extradurale', '60 %', 'S6 Spine MRI', B, 'g96-7'),
        ('Valeur prédictive négative', '0,89', 'S14 résumé', B, 'g96-7'),
        ('Patch : réponse', '30–70 % ; guérison < 10 % (types 1 et 2)', 'S6 Therapeutic procedures', B, 'g96-9'),
        ('Chirurgie', '90 % ; > 95 % ; < 5 % ; < 5 %', 'S5', B, 'g96-9'),
        ('Méningite (rhinorrhée)', '10–37 %', 'S13 résumé', B, 'g96-8'),
        ('Sidérose', '5–10 % (S5) ; 1,5 % (S2)', 'S5 encadré ; S2 tableau 3', B, 'g96-8'),
        ('Diplopie ; abducens', '< 10 % ; 1 %', 'S5 ; S2 tableau 3', A, 'g96-6'),
        ('Symptômes associés (10 valeurs) et formes rares (7 valeurs)', 'tableau 3 du consensus', 'S2 tableau 3', A, 'g96-5'),
        ('Fractures de la base antérieure', 'près de 25 %', 'S12 Introduction', A, 'g96-1'),
        ('Hypotension sans fuite', '< 6 cm H2O ; 10–15 %', 'S24 (pleine page PMC8591068)', A, 'g96-3'),
        ('Délai diagnostique', '3 mois', 'S5', A, 'g96-0'),
    ], 1):
        check(f'L{i:02d}', obj, val, val, 'CORRECT', 'relecture dans la source', src, f, anc)


def main():
    emp = {f: {'sha256': sha(f), 'manifeste': MANIFEST[f], 'conforme': sha(f) == MANIFEST[f]} for f in FILES}
    inv = inventory()
    run_checks()
    # couverture : chaque occurrence est rattachée aux contrôles qui contiennent sa valeur
    def nums(s):
        return set(x.replace(' ', '').replace(' ', '').replace(' ', '')
                   for x in re.findall(r'\d+(?:[.,]\d+)?', str(s).replace('.', ',')))
    blobs = [(r['id'], nums(' '.join(str(r[k]) for k in ('objet', 'attendu', 'trouve', 'formule')))) for r in R]
    for o in inv:
        vs = nums(o['valeur'])
        o['controles'] = [i for i, b in blobs if vs & b]
    non_couvertes = [o['id'] for o in inv if not o['controles']]
    (HERE / 'inventaire.json').write_text(json.dumps({'total_releves': len(inv), 'occurrences_non_couvertes': non_couvertes,
                                                     'empreintes': emp, 'occurrences': inv},
                                                    ensure_ascii=False, indent=1), encoding='utf-8')
    counts = {k: sum(1 for r in R if r['verdict'] == k) for k in ('CORRECT', 'ARRONDI', 'FAUX', 'NON_VERIFIABLE')}
    out = {'total_releves': len(inv), 'calculables': len(R), 'recalcules': len(R), **{k.lower(): v for k, v in counts.items()},
           'resultats': R}
    (HERE / 'resultats.json').write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding='utf-8')
    print(json.dumps({k: v for k, v in out.items() if k != 'resultats'}, ensure_ascii=False))
    for r in R:
        if r['verdict'] == 'FAUX':
            print('FAUX', r['id'], r['objet'], '|', r['trouve'])
    assert all(e['conforme'] for e in emp.values()), 'empreintes non conformes'


if __name__ == '__main__':
    main()
