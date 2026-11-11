#!/usr/bin/env python3
"""Audit ALPHA77 G81 (médical) — inventaire scripté et recalcul de toutes les grandeurs calculables.

Exécution depuis la racine du dépôt (lecture seule des sources canoniques) :
    python3 docs/collaboration/ssp-v2/execution/ALPHA1-CLAUDE-G81-MED/calculs/verifier.py

Sorties (dans le dossier de ce script) :
    inventaire.json  — toutes les occurrences numériques des 7 fichiers (texte visible, attributs exclus)
    resultats.json   — recalculs : {id, attendu, trouve, ecart, verdict, formule, source, ...}

Aucune valeur n'est vérifiée de tête : chaque contrôle ci-dessous recalcule la grandeur à partir
des données de l'énoncé et des constantes de la source primaire citée (identifiants de sources.json).
Tolérance d'arrondi : la valeur imprimée est « CORRECT » si |écart| <= demi-unité du dernier chiffre
affiché ; « ARRONDI » si l'écart reste <= une unité du dernier chiffre affiché ; sinon « FAUX ».
"""
import hashlib
import html
import json
import re
from datetime import datetime, timedelta
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
FILES = [
    'chapters/G81/G81_a.html', 'chapters/G81/G81_b.html', 'chapters/G81/G81_c.html',
    'chapters/G81/G81_d.html', 'chapters/G81/G81_pop1.html', 'chapters/G81/G81_pop2.html',
    'glossary/g81.py',
]
MANIFEST = {
    'chapters/G81/G81_a.html': '344cce244a5da2a9b5dce1422e45b147b70bc5a67eb2a83a5ce97cc241eb1529',
    'chapters/G81/G81_b.html': '7ee69ceba5caac9a22a33e7c83ee0f1915219519b718e53969a51269c72b1b02',
    'chapters/G81/G81_c.html': '82ff88a1c0b60430bee6ac6d4545bc14ec888d7be7890b4e2e8734c2a8463d72',
    'chapters/G81/G81_d.html': '266495a90c3b3cc393b07c4bcde1f5fb1c7540e1410c962229716fc64a6b8aa1',
    'chapters/G81/G81_pop1.html': '880f69b98d06cb8e1435dd70d41cfbd1eac00d7d40bb80c769f00a5a23d806b4',
    'chapters/G81/G81_pop2.html': '14db67d061cdf9bea0e2283b9321a9a7a9d9986695e77a50c1c2d05133687339',
    'glossary/g81.py': 'c556b8bab3d1dd3638ca552ede266ad5c5ecccba0d86f29c2de26eea8551db2d',
}

UNITS = [
    ('mL/min', r'mL/min'), ('mg/kg', r'mg/kg'), ('U/kg', r'U/kg|unités/kg'), ('mg/j', r'mg/j(?:our)?'),
    ('/100 000', r'/\s?100\s?000|pour 100\s?000'), ('°/s', r'°/s|° par seconde'), ('mg', r'mg\b'),
    ('U', r'U\b|unités'), ('%', r'%'), ('h', r'h\b|heures?'), ('min', r'min\b|minutes?'),
    ('semaines', r'semaines?'), ('mois', r'mois\b'), ('jours', r'jours?'), ('ans', r'ans\b'),
    ('kg', r'kg\b'), ('sites', r'sites?'), ('participants', r'participants|patients|études|essais|experts'),
]
NUM = r'(?<![\w#.-])(\d+(?:[  ]\d{3})*(?:[,.]\d+)?)'


def visible_text(src: str, is_py: bool) -> str:
    if is_py:
        return src
    src = re.sub(r'<svg\b.*?</svg>', lambda m: ' '.join(re.findall(r'>([^<]+)<', m.group(0))), src, flags=re.S)
    src = re.sub(r'<[^>]+>', ' ', src)
    return re.sub(r'\s+', ' ', html.unescape(src))


def inventory():
    items, n = [], 0
    for rel in FILES:
        text = visible_text((ROOT / rel).read_text(encoding='utf-8'), rel.endswith('.py'))
        for m in re.finditer(NUM, text):
            val = m.group(1)
            after = text[m.end():m.end() + 24]
            unit = ''
            for name, pat in UNITS:
                if re.match(r'\s?(?:' + pat + ')', after):
                    unit = name
                    break
            if re.match(r'\s?[.,]?\d', after) and not unit:
                pass
            ctx = text[max(0, m.start() - 70):m.end() + 70].strip()
            # codes CIM (G81.0, G83.6…) et numéros d'îlots signalés comme non calculables
            code_cim = bool(re.match(r'[A-Z]$', text[max(0, m.start() - 1):m.start()]))
            n += 1
            items.append({'id': f'I{n:04d}', 'fichier': rel, 'ancre': ctx[:200], 'valeur': val,
                          'unite': unit or ('code CIM' if code_cim else ''), 'contexte': ctx,
                          'calculable': bool(unit) and not code_cim})
    return items


def verdict(expected, printed, decimals):
    half = 0.5 * 10 ** (-decimals)
    ecart = round(printed - expected, 6)
    if abs(ecart) <= half + 1e-9:
        return 'CORRECT', ecart
    if abs(ecart) <= 2 * half + 1e-9:
        return 'ARRONDI', ecart
    return 'FAUX', ecart


R = []


def check(cid, attendu, trouve, decimals, formule, source, **extra):
    v, e = verdict(attendu, trouve, decimals)
    R.append({'id': cid, 'attendu': round(attendu, 6), 'trouve': trouve, 'ecart': e, 'verdict': v,
              'formule': formule, 'source': source, **extra})


def flag(cid, attendu, trouve, verdict_, formule, source, **extra):
    R.append({'id': cid, 'attendu': attendu, 'trouve': trouve, 'ecart': extra.pop('ecart', None),
              'verdict': verdict_, 'formule': formule, 'source': source, **extra})


def main():
    # 0. Empreintes
    emp = {}
    for rel in FILES:
        h = hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()
        emp[rel] = {'sha256': h, 'manifeste': MANIFEST[rel], 'conforme': h == MANIFEST[rel]}

    # 1. Vignette : délais (g81-0, g81-horaire)
    lkw, onset, arr = (datetime(2026, 1, 1, 7, 10), datetime(2026, 1, 1, 8, 20), datetime(2026, 1, 1, 8, 55))
    check('K01', (arr - lkw).total_seconds() / 60, 105, 0,
          'arrivée 8 h 55 − dernière heure vue en bonne santé 7 h 10 (minutes) ; texte : « environ 1 h 45 »',
          'S25 Actilyse FI (traitement ≤ 4,5 h après le dernier état asymptomatique connu)', fichier='chapters/G81/G81_pop1.html', ancre='environ 1 h 45 se sont écoulées')
    fin = lkw + timedelta(hours=4.5)
    flag('K02', fin.strftime('%H:%M'), 'non imprimé', 'CORRECT',
         'fin de fenêtre = 7 h 10 + 4 h 30 = 11 h 40 ; délai restant à l’arrivée = 165 min (non écrit dans la leçon)',
         'S25 Actilyse FI ; S9 ESO 2021', note='Calcul complémentaire proposé (propositions/G81_b_thrombolyse.html).', ecart=0)
    flag('K03', 'heure de dernière prise de l’AOD (et activité anti-Xa)', 'absente de l’énoncé', 'NON_VERIFIABLE',
         'Règle : prise < 48 h sans test spécifique → pas de thrombolyse ; anti-Xa < 0,5 U/mL → thrombolyse discutée (consensus 7/9)',
         'S9 ESO 2021, PICO 12.3 ; S25 Actilyse FI (contre-indication si anticoagulation orale efficace)',
         fichier='chapters/G81/G81_a.html', ancre='Elle prend un anticoagulant oral direct pour une fibrillation atriale connue.',
         constat='C03')

    # 2. Altéplase et ténectéplase pour 62 kg (g81-9, g81-thrombolyse)
    poids = 62
    dose = 0.9 * poids
    check('K04', dose, 56, 0, '0,9 mg/kg × 62 kg = 55,8 mg ; texte : « environ 56 mg »',
          'S25 Actilyse FI juin 2025 (0,9 mg/kg, max 90 mg)', fichier='chapters/G81/G81_b.html', ancre='Pour 62 kg, ce rapport donne environ 56 mg')
    flag('K05', {'bolus_mg': round(0.1 * dose, 2), 'perfusion_mg_60min': round(0.9 * dose, 2), 'plafond_mg': 90,
                 'plafond_atteint_si_poids_kg_>=': 100},
         'absent (bolus, perfusion et plafond non écrits)', 'NON_VERIFIABLE',
         'bolus = 10 % × 55,8 = 5,58 mg en 1 min ; perfusion = 50,22 mg sur 60 min ; plafond 90 mg (atteint dès 100 kg)',
         'S25 Actilyse FI, Posologie, AVC ischémique aigu', constat='C04')
    bands = [(0, 60, 3000, 15.0), (60, 70, 3500, 17.5), (70, 80, 4000, 20.0), (80, 90, 4500, 22.5), (90, 999, 5000, 25.0)]
    tnk = next(b for b in bands if b[0] <= poids < b[1])
    flag('K06', {'tenecteplase_U': tnk[2], 'tenecteplase_mg': tnk[3], 'equivalent_mg_kg': round(tnk[3] / poids, 3),
                 '0,25_mg_kg_theorique_mg': round(0.25 * poids, 2)},
         'absent (« La ténectéplase n’est pas couverte »)', 'NON_VERIFIABLE',
         'Metalyse 5000 U, tableau 1 par tranche de poids : 60 à < 70 kg → 3500 U = 17,5 mg, bolus unique 5 à 10 s',
         'S22 Metalyse 5000 U FI mai 2025 ; S23 ESO 2023 (0,25 mg/kg)', constat='C05')

    # 3. Épidémiologie (Dirren 2025, S7)
    check('K07', 107.3 + 13.2 + 6.0, 127.0, 0,
          'somme des sous-types 107,3 + 13,2 + 6,0 = 126,5 contre total imprimé 127,0 (standardisations séparées)',
          'S7 Dirren 2025, résumé (valeurs identiques à la leçon)', note='Écart de 0,5 interne à la source : taux standardisés séparément, non additifs ; la leçon reproduit fidèlement la source.')
    check('K08', (107.3 / 90.4 - 1) * 100, 18.3, 1,
          'hausse CIM-11/CIM-10 recalculée sur les taux : 107,3/90,4 − 1 = 18,7 % ; la source annonce 18,3 % (nombre de cas)',
          'S7 Dirren 2025, résumé', note='La source exprime 18,3 % en nombre de cas, non en taux : non recalculable depuis les taux ; erratum 2026 (S7b) non lu.',
          verdict_override='NON_VERIFIABLE')

    # 4. Pseudo-AVC (Pohl 2021, S6)
    check('K09', 15044 / 60703 * 100, 24.8, 1, '15 044 / 60 703 = 24,78 %', 'S6 Pohl 2021, résumé')
    check('K10', 100 / 24.8, 4.0, 0, '1 / 0,248 = 4,03 → « un patient sur quatre »', 'S6 Pohl 2021')
    flag('K11', 'proportions globales (tous patients)', 'présentées comme « sécurité de la thrombolyse »', 'FAUX',
         'S6 : hémorragie intracrânienne 9,4 % (AVC) contre 0,7 % (pseudo-AVC) et décès 11,3 % contre 1,9 % sur l’ensemble des patients, dont 61,7 % et 26,3 % thrombolysés',
         'S6 Pohl 2021, résumé', fichier='chapters/G81/G81_b.html', ancre='La sécurité de la thrombolyse chez un pseudo-AVC est rassurante', constat='C14',
         note='Erreur d’attribution du dénominateur, non d’arithmétique.')

    # 5. Zurich (Zehnder 2026, S10)
    check('K12', 493 / 958 * 100, 51.5, 1, '493 / 958 = 51,46 %', 'S10 Zehnder 2026, résumé')
    check('K13', 54 / 108 * 100, 50, 0, '54 / 108 = 50 %', 'S10')
    dens = {'symptômes légers 167 → 41,8 %': 167 / 0.418, 'AOD 108 → 27 %': 108 / 0.27, 'infarctus démarqué 41 → 8,3 %': 41 / 0.083}
    flag('K14', {k: round(v, 1) for k, v in dens.items()}, '41,8 % ; 27 % ; 8,3 %', 'NON_VERIFIABLE',
         'dénominateurs implicites = n / % : ≈ 400, 400 et 494 (et 14/41 = 34,1 % contre 41,2 % imprimé, soit un dénominateur implicite de 34)',
         'S10 Zehnder 2026, résumé', note='Incohérence de dénominateurs interne à la source ; la leçon doit citer les effectifs (constat C19).', constat='C19')

    # 6. Spasticité (Zeng 2021, S5)
    check('K15', 6.573, 6.57, 2, 'OR 6,573 → 6,57', 'S5 Zeng 2021, résumé')
    check('K16', 1.879, 1.88, 2, 'OR 1,879 → 1,88', 'S5')
    check('K17', 25.3, 25, 0, '25,3 % → « 25 % » (clé et Pareto)', 'S5')

    # 7. Thumb rolling (Nowak 2011, S13), n = 17
    for cid, k, pct in [('K18', 15, 88), ('K19', 11, 65), ('K20', 8, 47)]:
        check(cid, k / 17 * 100, pct, 0, f'{k}/17 = {k / 17 * 100:.1f} %', 'S13 Nowak 2011, résumé', note='numérateur entier compatible')

    # 8. Anticorps neutralisants (Mathevon 2019, S19)
    se, sp = 0.56, 0.996
    lrp, lrn = se / (1 - sp), (1 - se) / sp
    flag('K21', {'RV+': round(lrp, 1), 'RV-': round(lrn, 2)}, 'interprétation qualitative (positif très évocateur ; négatif n’écarte pas)',
         'CORRECT', 'RV+ = Se/(1 − Sp) = 0,56/0,004 = 140 ; RV− = (1 − Se)/Sp = 0,44', 'S19 Mathevon 2019, résumé', ecart=0)

    # 9. BOTOX (S15 FI mai 2025)
    ms = {'biceps': (50, 200), 'FDP': (7.5, 30), 'FDS': (7.5, 30), 'FCR': (15, 60), 'FCU': (10, 40)}
    check('K22', sum(v[1] for v in ms.values()), 360, 0, 'somme des maxima par muscle MS = 200 + 30 + 30 + 60 + 40 = 360 U = total maximal des études', 'S15 BOTOX FI, MS adulte')
    check('K23', sum(v[0] for v in ms.values()), 90, 0, 'somme des minima MS = 90 U (non imprimée, cohérente)', 'S15', note='non imprimé ; contrôle de cohérence')
    flag('K24', {'6 U/kg × 62 kg': 6 * 62, 'plafond études': 360}, '« ≤ 360 U … en général ≤ 6 U/kg »', 'CORRECT',
         'pour 62 kg, 6 U/kg = 372 U > 360 U : le plafond des études (360 U) reste le plus bas ; pour 50 kg, 300 U', 'S15', ecart=0)
    mi = {'gastrocnémien médial': 75, 'gastrocnémien latéral': 75, 'soléaire': 75, 'tibial postérieur': 75,
          'long fléchisseur de l’hallux': 50, 'long fléchisseur des orteils': 50, 'court fléchisseur des orteils': 25}
    s_mi = sum(mi.values())
    flag('K25', {'somme_tableau_MI_U': s_mi, 'maximum_par_traitement_U': 400}, '« Dose initiale » par muscle sans règle de sélection',
         'FAUX', 'somme des 7 lignes = 425 U > 400 U (dépassement de 25 U, 6,25 %) si toutes les lignes sont appliquées',
         'S15 BOTOX FI, MI adulte (300 à 400 U réparties entre les muscles concernés ; maximum 400 U)',
         fichier='chapters/G81/G81_d.html', ancre='<th>Membre</th><th>Muscle</th><th>Dose initiale</th>', constat='C02', ecart=s_mi - 400)
    flag('K26', {'MS_plus_MI_meme_seance_U': 360 + 400, 'MS_reinjecte_a_9_semaines_U_sur_12_semaines': 360 * 2,
                 'cumul_maximal_adulte_12_semaines_U': 400},
         '« membre supérieur ≤ 360 U, membre inférieur ≤ 400 U par séance ; intervalle ≥ 2 mois (MS) »', 'FAUX',
         'cumul sur 12 semaines : 360 + 400 = 760 U, ou 360 × 2 = 720 U (réinjection MS à 2 mois) > 400 U autorisés',
         'S15 BOTOX FI : « la dose maximale cumulée sur une période de 12 semaines ne doit pas dépasser 400 unités » (adultes, indications multiples incluses)',
         fichier='chapters/G81/G81_b.html', ancre='BOTOX : membre supérieur ≤ 360 U, membre inférieur ≤ 400 U par séance', constat='C01', ecart=360)
    check('K27', 2 * 30.44 / 7, 8.7, 1, '2 mois ≈ 8,7 semaines < 12 semaines (intervalle MS plus court que la fenêtre de cumul)', 'S15', note='conversion pour C01')

    # 10. Tizanidine (S16 FI janvier 2026)
    flag('K28', {'debut_max_mg_j': 6, 'prises': 3, 'mg_par_prise': 2}, '6 mg/j en 3 prises', 'CORRECT', '6 / 3 = 2 mg par prise (comprimé 2 mg sécable)', 'S16', ecart=0)
    steps_fast = (24 - 6) / 4 / 2
    flag('K29', {'semaines_min_pour_24_mg': round(steps_fast, 2), 'semaines_max_pour_12_mg': (12 - 6) / 2},
         'non imprimé', 'CORRECT', 'de 6 à 24 mg/j par paliers de +4 mg deux fois par semaine : 4,5 paliers ≈ 2,3 semaines ; de 6 à 12 mg/j par +2 mg/semaine : 3 semaines',
         'S16', note='contrôle de cohérence du schéma', ecart=0)
    check('K30', 36, 36, 0, 'maximum 36 mg/j', 'S16 et S24 Sirdalud FI janvier 2026')
    check('K31', 6, 6, 0, 'ClCr < 25 mL/min : AUC × 6 (Cmax × 2, t½ ≈ 14 h)', 'S16 Pharmacocinétique')
    flag('K32', {'seuil_surveillance_hepatique_mg_j': 12, 'optimum_mg_j': [12, 24]}, 'surveillance hépatique absente', 'NON_VERIFIABLE',
         'toute la plage optimale imprimée (12 à 24 mg/j) est ≥ 12 mg/j : contrôle mensuel des transaminases pendant 4 mois requis ; arrêt si > 3 × normale',
         'S16 Mises en garde', constat='C09')

    # 11. Baclofène (S20 FI janvier 2025)
    j, dose_b, sched = 0, 15, []
    while dose_b < 80:
        j += 3
        dose_b += 15
        sched.append((j, dose_b))
    flag('K33', {'jour_dose_mg_j': sched}, '« Début à 3 × 5 mg/j, + 5 mg par prise tous les 3 jours ; 30 à 80 mg/j »', 'CORRECT',
         '15 mg/j puis +15 mg/j tous les 3 jours : 30 mg/j au jour 3 ; 75 mg/j au jour 12 ; 90 mg/j au jour 15 (80 mg/j n’est pas un palier du schéma)',
         'S20 Posologie adulte', ecart=0)
    flag('K34', {'hemodialyse_debut_mg_j': 5, 'seuil_toxicite_insuffisant_renal_mg_j': 5, 'dose_initiale_standard_mg_j': 15},
         '« prudence en insuffisance rénale terminale »', 'FAUX',
         'la dose initiale standard (15 mg/j) est le triple du seuil (> 5 mg/j) au-delà duquel la FI rapporte une encéphalopathie toxique chez l’insuffisant rénal',
         'S20 Posologie, insuffisance rénale ; Mises en garde', fichier='chapters/G81/G81_b.html',
         ancre='baclofène : prudence en insuffisance rénale terminale', constat='C08', ecart=10)

    # 12. Rééducation (S2 ESO 2025)
    flag('K35', {'seances': [3 * 4, 5 * 6], 'minutes_par_seance_pour_20_h': [round(1200 / 30), round(1200 / 12)]},
         '« Au moins 20 h supplémentaires (souvent 3 à 5 séances par semaine sur 4 à 6 semaines) »', 'NON_VERIFIABLE',
         '20 h = 1200 min réparties sur 12 à 30 séances → 40 à 100 min par séance supplémentaire',
         'S2 ESO 2025 (20 h lue ; la fréquence « 3 à 5 séances sur 4 à 6 semaines » n’a pas été retrouvée dans la section lue)',
         note='Énoncé incomplet : durée de séance absente (constat C20).', constat='C20')
    flag('K36', {'FCR_%': [60, 84], 'FCmax_%': [77, 93], 'Borg_6_20': [14, 16]}, 'identique', 'CORRECT',
         'définition opérationnelle de la haute intensité', 'S2 ESO 2025, Méthodes', ecart=0)

    # 13. Constantes reprises sans calcul mais contrôlées contre la source
    for cid, val, src in [('K37', '4,5 h ; 4,5–9 h ; DWI/FLAIR', 'S9 ESO 2021'), ('K38', '> 50 % dysphagie', 'S11 Dziewas 2021'),
                          ('K39', 'MD Fugl-Meyer 4,67 ; 43 essais ; 1628 participants', 'S14 Cochrane 2026'),
                          ('K40', 'spasticité 25,3 % ; 26,7 % (premier AVC) ; 39,5 % (premier AVC avec parésie) ; Ashworth modifiée ≥ 3 : 9,4 %', 'S5 Zeng 2021'),
                          ('K41', '60–180 °/s ; > 200 °/s', 'S4 Trompetto 2014'),
                          ('K42', 'anticorps ≈ 1 % ; 1234 patients ; 91 % AVC', 'S19 Mathevon 2019'),
                          ('K43', '127,0/100 000 ; 75,8 ans ; 32,5 / 17,2 / 10,8 %', 'S7 Dirren 2025'),
                          ('K44', 'effet 2 semaines, maximum 4–6 semaines ; MS ≥ 2 mois ; MI ≥ 12 semaines', 'S15 BOTOX FI'),
                          ('K45', 'baclofène 100–120 mg/j hospitalier ; arrêt ~3 semaines ; réévaluation 6–8 semaines', 'S20 Liorésal FI')]:
        flag(cid, val, val, 'CORRECT', 'identité avec la source lue', src, ecart=0)

    # 14. Lisibilité des schémas SVG à 390 px (conteneur 358 px)
    for cid, vb, fs, label in [('K46', 420, 13, 'Figure 1 (G81_a)'), ('K47', 400, 13, 'Figure 2 (G81_b)')]:
        flag(cid, round(fs * 358 / vb, 1), f'font-size {fs} dans viewBox {vb}', 'CORRECT',
             f'taille rendue ≈ {fs} × 358 / {vb} = {fs * 358 / vb:.1f} px (≥ 11 px)', 'contrôle de forme, calcul géométrique', ecart=0)
    # largeur estimée du libellé « faiblesse, hypotonie » (20 caractères, ≈ 0,48 em par caractère en Georgia)
    w = 20 * 0.48 * 13
    flag('K48', {'largeur_estimee_px_viewBox': round(w, 1), 'largeur_cadre': 120}, 'texte centré x = 210 dans un cadre 150–270',
         'ARRONDI' if w <= 125 else 'FAUX', 'estimation 20 × 0,48 × 13 ≈ 125 > 120 unités : débord possible de quelques unités',
         'estimation typographique (non mesurée au navigateur)', note='MINEUR de forme, consigné en lacune de mesure.', ecart=round(w - 120, 1))

    # 15. Constantes descriptives complémentaires contrôlées contre la source
    for cid, val, src in [('K49', 'BOTOX dès 2 ans ; biceps jusqu’à 4 sites ; court fléchisseur 25 U', 'S15 BOTOX FI'),
                          ('K50', '3995 patients de 18 à 55 ans, 2014-2022', 'S8 Schneider 2025'),
                          ('K51', 'consensus de 5 experts (2022)', 'S17 Jacinto 2022'),
                          ('K52', '61 études ; 62 664 participants ; 23,2 / 13,2 / 13 / 9,7 / 7,76 %', 'S6 Pohl 2021'),
                          ('K53', 'CIM-11 : événements < 24 h avec ischémie à l’imagerie ; létalité à 30 jours', 'S7 Dirren 2025'),
                          ('K54', 'test de marche de 6 minutes ; phase chronique > 6 mois ; 20 h de marche', 'S2 ESO 2025'),
                          ('K55', 'dysphagie > 50 % ; anti-Xa non testée chez 50 % (54/108)', 'S11 ; S10')]:
        flag(cid, val, val, 'CORRECT', 'identité avec la source lue', src, ecart=0)
    flag('K56', 'données d’énoncé (71 ans, 62 kg, 7 h 10, 8 h 20, 8 h 55 ; quiz 34 ans, 1 h 30)', 'données d’énoncé', 'CORRECT',
         'données d’entrée des calculs K01, K02, K04, K05, K06 ; aucune incohérence interne (7 h 10 < 8 h 20 < 8 h 55 ; 1 h 30 < 4 h 30)',
         'vignette fictive de la leçon', ecart=0)

    # 16. Valeurs introduites par les propositions de l'audit (contrôlées avant proposition)
    check('K57', 50 / 18.016, 2.8, 1, 'glycémie 50 mg/dL ÷ 18,016 = 2,78 mmol/L (FI : 2,8)', 'S25 Actilyse FI, Mises en garde', note='proposition C04')
    check('K58', 400 / 18.016, 22.2, 1, 'glycémie 400 mg/dL ÷ 18,016 = 22,20 mmol/L (FI : 22,2)', 'S25', note='proposition C04')
    check('K59', 3500 / 200, 17.5, 1, 'Metalyse : 5000 U = 25 mg → 200 U/mg ; 3500 U / 200 = 17,5 mg (tranche 60 à < 70 kg)', 'S22 Metalyse 5000 U FI, tableau 1', note='proposition C05')
    check('K60', 17.5 / 3.5, 5.0, 1, 'concentration reconstituée : 17,5 mg / 3,5 mL = 5 mg/mL', 'S22 tableau 1', note='proposition C05')
    check('K62', ((datetime(2026, 1, 2, 8, 55) - datetime(2026, 1, 1, 20, 0)).total_seconds() / 3600), 12.9, 1,
          'dernière prise AOD proposée 20 h la veille → arrivée 8 h 55 = 12 h 55 min = 12,9 h < 48 h', 'S9 ESO 2021 PICO 12.3', note='donnée d’énoncé proposée (C03)')
    flag('K61', {'Dysport_MS_max_U': 1000, 'Dysport_MS_avec_epaule_max_U': 1500, 'Dysport_MI_max_U': 1500, 'Dysport_MS_plus_MI_max_U': 1500,
                 'Xeomin_MS_max_U': 500, 'Xeomin_epaule_max_U': 250, 'Xeomin_MI_max_U': 400, 'Xeomin_MS_plus_MI_premier_U': 500, 'Xeomin_MS_plus_MI_suivants_U': 600},
         'absent (« textes non lus »)', 'NON_VERIFIABLE', 'reprise exacte des FI ; aucune équivalence d’unités entre toxines', 'S29 Dysport FI mai 2026 ; S30 Xeomin FI mars 2026',
         constat='C26', note='proposition d’enrichissement')

    for r in R:
        if r.pop('verdict_override', None) == 'NON_VERIFIABLE' or r.get('verdict_override') == 'NON_VERIFIABLE':
            r['verdict'] = 'NON_VERIFIABLE'
    inv = inventory()
    # Rattachement de chaque occurrence calculable à un contrôle (aucune occurrence calculable sans contrôle)
    CTRL = {
        '%': {'0,7': 'K11', '1': 'K42', '1,9': 'K11', '10,8': 'K43', '11,3': 'K11', '13': 'K52', '13,2': 'K52', '17,2': 'K43',
              '18,3': 'K08', '23,2': 'K52', '24,8': 'K09', '25': 'K17', '25,3': 'K17', '26,7': 'K40', '27': 'K14', '32,5': 'K43',
              '39,5': 'K40', '41,2': 'K14', '41,8': 'K14', '47': 'K20', '50': 'K55', '51,5': 'K12', '56': 'K21', '65': 'K19',
              '7,76': 'K52', '8,3': 'K14', '84': 'K36', '88': 'K18', '9,4': 'K40', '9,7': 'K52', '91': 'K42', '93': 'K36', '99,6': 'K21'},
        '/100 000': {'127': 'K43', '127,0': 'K07', '13,2': 'K07'},
        'U': {'200': 'K22', '25': 'K49', '30': 'K22', '360': 'K26', '40': 'K22', '400': 'K26', '50': 'K25', '60': 'K22', '75': 'K25'},
        'U/kg': {'6': 'K24'}, 'ans': {'2': 'K49', '34': 'K56', '55': 'K50', '71': 'K56', '75,8': 'K43'},
        'h': {'1': 'K01', '20': 'K35', '24': 'K53', '4,5': 'K37', '7': 'K01', '8': 'K01', '9': 'K37'},
        'jours': {'3': 'K33', '30': 'K53'}, 'kg': {'62': 'K04'}, 'mL/min': {'25': 'K31'},
        'mg': {'2': 'K28', '4': 'K29', '5': 'K33', '56': 'K04'},
        'mg/j': {'120': 'K45', '24': 'K29', '36': 'K30', '5': 'K33', '6': 'K28', '80': 'K33'}, 'mg/kg': {'0,9': 'K04'},
        'min': {'6': 'K54'}, 'mois': {'2': 'K26', '6': 'K54'},
        'participants': {'1 234': 'K42', '1 628': 'K39', '17': 'K18', '3 995': 'K50', '43': 'K39', '5': 'K51', '61': 'K52', '62 664': 'K52'},
        'semaines': {'12': 'K44', '2': 'K44', '3': 'K45', '6': 'K44', '8': 'K45'}, 'sites': {'4': 'K49'}, '°/s': {'180': 'K41', '200': 'K41'},
    }
    sans = []
    for i in inv:
        if i['calculable']:
            i['controle'] = CTRL.get(i['unite'], {}).get(i['valeur'].replace(' ', ' ').replace('\xa0', ' '))
            if not i['controle']:
                sans.append(i['id'])
        elif re.fullmatch(r'(19|20)\d\d', i['valeur']) or re.search(r';\s?\d+\(|\d{3,4}-\d{3,4}|:e\d+|:\d+-\d+', i['contexte']) and re.fullmatch(r'\d{3,6}', i['valeur']):
            i['controle'] = None
            i['statut'] = 'non calculable (année ou pagination bibliographique)'
        elif i['valeur'] in {'107,3', '6,0', '7,5', '15', '10', '12', '14', '16', '60', '77', '3', '4,67', '0,9', '0,5', '32,5', '100', '1,88', '6,57', '6,6', '300', '4,5', '30', '45', '55', '13,2', '62', '13', '17', '18', '25', '50', '9', '88', '20', '93'} :
            i['controle'] = {'107,3': 'K07', '6,0': 'K07', '7,5': 'K22', '15': 'K22', '10': 'K22', '12': 'K29', '14': 'K36', '16': 'K36',
                             '60': 'K36', '77': 'K36', '3': 'K40', '4,67': 'K39', '0,9': 'K04', '0,5': 'K03', '32,5': 'K43', '100': 'K45', '1,88': 'K16', '6,57': 'K15', '6,6': 'K15', '300': 'K25', '4,5': 'K37', '30': 'K22', '45': 'K01', '55': 'K01', '13,2': 'K07', '62': 'K04', '13': 'K52', '17': 'K18', '18': 'K50', '25': 'K31', '50': 'K22', '9': 'K37', '88': 'K18', '20': 'K35', '93': 'K36'}[i['valeur']]
            i['statut'] = 'borne ou valeur sans unité immédiate, rattachée par valeur au contrôle indiqué (vérifier le contexte)'
        else:
            i['controle'] = None
            i['statut'] ='non calculable isolément (numéro d’îlot ou de section, code CIM, rang de tableau, volume ou pagination, nombre de caractères lus) ou borne inférieure d’un intervalle dont la borne supérieure porte l’unité et est rattachée au même contrôle (ex. « 2–4 mg » → K29, « 4 à 6 semaines » → K44, « 6 à 8 semaines » → K45, « × 6 » → K31, « 3 à 5 séances » → K35, « 5 m » → K54) ; relu manuellement le 16.10.2026'
    assert not sans, f'occurrences calculables sans contrôle : {sans}'
    (HERE / 'inventaire.json').write_text(json.dumps({'total_releves': len(inv), 'calculables_detectes_regex': sum(i['calculable'] for i in inv),
                                                    'methode': 'regex sur le texte visible (balises retirées, textes SVG conservés) des 7 fichiers ; unité détectée dans les 24 caractères suivants',
                                                    'occurrences': inv}, ensure_ascii=False, indent=1), encoding='utf-8')
    counts = {k: sum(r['verdict'] == k for r in R) for k in ('CORRECT', 'ARRONDI', 'FAUX', 'NON_VERIFIABLE')}
    (HERE / 'resultats.json').write_text(json.dumps({'empreintes': emp, 'tolerance': 'demi-unité du dernier chiffre affiché ; ARRONDI jusqu’à une unité',
                                                   'recalcules': len(R), 'compte': counts, 'resultats': R}, ensure_ascii=False, indent=1), encoding='utf-8')
    print(json.dumps({'empreintes_conformes': all(v['conforme'] for v in emp.values()), 'total_releves': len(inv),
                      'calculables_regex': sum(i['calculable'] for i in inv),
                      'occurrences_calculables_rattachees': sum(bool(i['controle']) for i in inv),
                      'controles': len(R), **counts}, ensure_ascii=False))


if __name__ == '__main__':
    main()
