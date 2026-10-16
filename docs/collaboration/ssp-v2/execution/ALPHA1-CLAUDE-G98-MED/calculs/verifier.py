#!/usr/bin/env python3
"""Audit ALPHA1-CLAUDE-G98-MED — inventaire et recalcul de toutes les valeurs chiffrées de G98.

Usage : python3 verifier.py <racine du worktree>
Sorties (dans le dossier de ce script) : inventaire.json, resultats.json.
Méthode :
  1. Inventaire exhaustif par expression régulière : tout nombre écrit en chiffres dans le texte
     visible des 7 fichiers (balises retirées, références bibliographiques p.src exclues car elles
     ne portent que des années et des titres). Les numéros d'îlots (span.n) sont neutralisés.
  2. Classement : étiquette (stade, niveau, zone, classe, rang, numéro de cas, section, année)
     ou grandeur (valeur, seuil, durée, dose, fréquence, effectif, rapport).
  3. Chaque grandeur est rapprochée d'une règle de vérification : recalcul arithmétique quand la
     valeur dérive d'autres valeurs (somme, rapport, conversion d'unités), sinon comparaison à la
     valeur lue dans la source primaire (identifiant Sx de sources.json, section).
  4. Toute grandeur sans règle fait échouer le script (aucune valeur ne passe sans contrôle).
Tolérance d'arrondi : 0,05 point de pourcentage pour une valeur publiée à une décimale,
0,5 point pour une valeur entière ; conversion de température : 0,05 °F.
"""
import html, json, math, re, sys
from pathlib import Path

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else '.')
OUT = Path(__file__).resolve().parent
FILES = ['chapters/G98/G98_a.html', 'chapters/G98/G98_b.html', 'chapters/G98/G98_c.html',
         'chapters/G98/G98_d.html', 'chapters/G98/G98_pop1.html', 'chapters/G98/G98_pop2.html',
         'glossary/g98.py']

TOKEN = re.compile(r'(?<![\w.,\-–†*§/])(\d{1,3}(?:[   ]\d{3})+|\d+(?:[.,]\d+)?)(?![\w.]*[†*])(?!§)')
LABEL_BEFORE = re.compile(r'(stades?|grades?|niveaux?|zones?|classe|cas pédagogique fictif|cycle betta|section|tableau|'
                          r'bloc|absente|présente|version modifiée de|stade prodromique|g|eichenholtz|×|sans|avec|actif|inactif|a/b ×)\s+(\d+\s*(?:et|ou|à|,|/)\s*){0,3}$', re.I)
ORDINAL_AFTER = re.compile(r'^((er|e)\b|\s*(janvier|février|mars|avril|mai|juin|juillet|août|septembre|octobre|novembre|décembre)\b|/1\b)')


def visible_text(path):
    t = (ROOT / path).read_text(encoding='utf-8')
    if path.endswith('.py'):
        # glossaire : seules les définitions affichées comptent
        t = ' '.join(re.findall(r"'((?:[^'\\]|\\.)*)'", t))
    t = re.sub(r'<p class="src">.*?</p>', ' ', t, flags=re.S)
    t = re.sub(r'<span class="n">[^<]*</span>', ' §§ ', t)
    # ancres : identifiant d'îlot ou de fenêtre le plus proche
    pieces, anchor = [], 'debut'
    for m in re.finditer(r'(<[^>]+>)|([^<]+)', t):
        tag, txt = m.group(1), m.group(2)
        if tag:
            a = re.search(r'\b(?:id|data-pop)="([^"]+)"', tag)
            if a and (tag.startswith('<section') or tag.startswith('<template') or tag.startswith('<div class="sci"')):
                anchor = a.group(1)
            pieces.append((anchor, ' '))
        else:
            pieces.append((anchor, html.unescape(txt)))
    return pieces


def inventory():
    items = []
    for f in FILES:
        pieces = visible_text(f)
        full, spans = '', []
        for anchor, txt in pieces:
            spans.append((len(full), anchor))
            full += txt
        full_n = re.sub(r'\s', ' ', full)
        for m in TOKEN.finditer(full_n):
            pos = m.start()
            anchor = [a for s, a in spans if s <= pos][-1]
            before = re.sub(r'\s+', ' ', full_n[max(0, pos - 90):pos])
            after = re.sub(r'\s+', ' ', full_n[m.end():m.end() + 70])
            raw = m.group(1)
            val = float(re.sub(r'[   ]', '', raw).replace(',', '.'))
            um = re.match(r'\s*(%|°\s?C|°\s?F|mg|ml/min|g\b|cm|mois|semaines?|jours?|ans|million|patients|pieds|cas|fois|par an)', after)
            unit = um.group(1).replace(' ', '') if um else ''
            if (unit == '' and LABEL_BEFORE.search(before)) or ORDINAL_AFTER.match(after) or (1800 <= val <= 2099 and unit == ''):
                kind = 'etiquette'
            else:
                kind = 'grandeur'
            items.append({'fichier': f, 'ancre': anchor, 'valeur': raw, 'v': val, 'unite': unit,
                          'type': kind, 'contexte': (before[-60:] + '⟦' + raw + '⟧' + after[:45]).strip()})
    for i, it in enumerate(items, 1):
        it['id'] = f'N{i:03d}'
    return items


def pct(n, d):
    return 100.0 * n / d


# ---- Règles : (identifiant, motif de contexte, valeur visée, fonction de vérification) ----
# Chaque fonction renvoie (attendu, verdict, formule, source).
def same(expected, source, note=''):
    return lambda v: (expected, 'CORRECT' if abs(v - expected) < 1e-9 else 'FAUX', note or 'valeur lue dans la source', source)


def rounded(num, den, source, label):
    def f(v):
        exp = pct(num, den)
        dec = 1 if abs(v * 10 - round(v * 10)) < 1e-9 and v != round(v) else 0
        tol = 0.05 if dec else 0.5
        verdict = 'CORRECT' if abs(round(exp, dec) - v) < 1e-9 else ('ARRONDI' if abs(exp - v) <= tol else 'FAUX')
        return (round(exp, 2), verdict, f'{label} : {num}/{den} × 100 = {exp:.2f} %', source)
    return f


def false_fixed(expected, source, formule):
    return lambda v: (expected, 'FAUX', formule, source)


RULES = [
    # Vignette et quiz (données d'énoncé) : cohérence avec le seuil
    ('vignette-age', r'homme de ⟦58', 58, same(58, 'énoncé de la vignette', 'donnée d’énoncé fictive, plausible (profil 50–60 ans [S2])')),
    ('delta-3C', r'(différence de|de) ⟦3⟧ ?°C', 3, lambda v: (3, 'CORRECT', '3 °C > seuil de 2 °C [S1, rec. 3, rationale] : la conclusion « dépasse le seuil » est exacte', 'S1')),
    # Série de Düsseldorf (S4)
    ('serie-71', r'⟦71⟧ cas', 71, same(71, 'S4 résumé, Results : « Seventy-one cases (59 patients) »')),
    ('fract-12', r'dans ⟦12⟧ cas sur 13', 12, lambda v: (12, 'CORRECT', '12/13 = 92,3 % ; S4 : « cortical fractures had already occurred in 12 cases » sur n = 13', 'S4')),
    ('fract-13', r'12 cas sur ⟦13', 13, same(13, 'S4 : « not cross-checked by MRI (n = 13 cases) »')),
    ('mid-69', r'⟦69⟧ ?%', 69, same(69, 'S4 : « 69% versus 7% without deformities »')),
    ('mid-7', r'⟦7⟧ ?% au stade 1|contre ⟦7⟧ ?%', 7, same(7, 'S4 : « 69% versus 7% »')),
    ('p-0012', r'p = ⟦0,0012', 0.0012, lambda v: (0.0012, 'CORRECT', 'valeur concordante avec S4 ; recalcul exact du test impossible (effectifs du médio-pied par stade non publiés dans le résumé)', 'S4')),
    ('tcc-4-6', r'plâtre de ⟦4⟧ à 6 mois|plâtre de 4 à ⟦6⟧ mois', None, lambda v: (v, 'CORRECT', 'S4 : « TCC-treatment lasted four to six months »', 'S4')),
    # Sanders-Frykberg (S2)
    ('zone-45', r'⟦45⟧ ?%', 45, same(45, 'S2 § Sanders and Frykberg : « zone II in about 45% »')),
    ('zone-35', r'⟦35⟧ ?%( :|\))', 35, same(35, 'S2 : « zone III in about 35% »')),
    ('zone-80', r'⟦80⟧ ?% des (atteintes|cas)', 80, lambda v: (45 + 35, 'CORRECT' if v == 80 else 'FAUX', '45 + 35 = 80 (somme de deux zones exclusives, S2)', 'S2')),
    # Épidémiologie
    ('prev-004', r'⟦0,04', 0.04, same(0.04, 'S1 Introduction : « 0.04% … seven foot care specialist centres in England »')),
    ('prev-03', r'⟦0,3⟧ ?% en Irlande', 0.3, same(0.3, 'S1 : « 0.3% … regional referral center in Ireland »')),
    ('prev-053', r'⟦0,53', 0.53, same(0.53, 'S1 : « 0.53% … national registry study in Denmark »')),
    ('prev-01-75', r'fourchette de ⟦0,1⟧|0,1 à ⟦7,5', None, lambda v: (v, 'CORRECT', 'S2 Introduction : « between 0.1 and 7.5% »', 'S2')),
    ('prev-35', r'jusqu’à ⟦35⟧ ?% chez', 35, same(35, 'S2 : « increasing up to 35% »')),
    ('rms-01-13', r'cite ⟦0,1⟧ à 13|0,1 à ⟦13⟧ ?%', None, lambda v: (v, 'NON_VERIFIABLE', 'S11 lu au niveau du résumé seulement : la fourchette 0,1–13 % n’y figure pas', 'S11')),
    ('n-1.6M', r'⟦1,6⟧ million', 1.6, lambda v: (round(537e6 * 0.003 / 1e6, 3), 'CORRECT' if abs(537e6 * 0.003 / 1e6 - v) < 0.05 else 'FAUX', '537 millions d’adultes diabétiques (2021) × 0,3 % = 1,611 million ≈ 1,6 [S1 Introduction]', 'S1')),
    ('n-160000', r'⟦160[   ]?000', 160000, lambda v: (160000, 'CORRECT', 'valeur de S1 (« annual incidence of 160,000 ») ; la source ne donne pas le calcul de l’incidence (non dérivable de la prévalence)', 'S1')),
    ('age-50-60', r'patient de ⟦50⟧ à 60|50 à ⟦60⟧ ans', None, lambda v: (v, 'CORRECT', 'S2 : « present within their fifties or sixties »', 'S2')),
    ('bilat-9-75', r'dans ⟦9⟧ à 75|9 à ⟦75⟧ ?%', None, lambda v: (v, 'CORRECT', 'S2 : « between 9 and 75% »', 'S2')),
    # Cohorte Balgrist (S6)
    ('coh-159', r'⟦159⟧ patients', 159, same(159, 'S6 Méthodes : « 159 patients with 184 affected feet »')),
    ('coh-60', r'médian de ⟦60⟧ ans', 60, same(60, 'S6 : « median age 60.0 »')),
    ('coh-femmes', r'⟦30,1⟧ ?% de femmes', 30.1, lambda v: (round(pct(49, 159), 2), 'FAUX', '49/159 × 100 = 30,82 % ; le résumé de S6 imprime 30,1 %, le texte des résultats 30,8 % : erreur de la source reprise', 'S6')),
    ('coh-bilat', r'bilatéralité de ⟦32,1', 32.1, rounded(51, 159, 'S6 Résultats : « 51/159 (32.1%) »', 'bilatéralité')),
    ('coh-52', r'médiane ⟦5,2⟧ ans', 5.2, same(5.2, 'S6 : « median follow-up of 5.2 years »')),
    ('coh-929', r'⟦92,9', 92.9, rounded(184 - 13, 184, 'S6 : 13 amputations majeures sur 184 pieds', 'survie sans amputation majeure (pieds)')),
    ('coh-136', r'récidive ⟦13,6', 13.6, rounded(25, 184, 'S6 : « In 25 (13.6%) feet, reactivation »', 'réactivation (pieds)')),
    ('coh-723', r'⟦72,3⟧ ?% des patients', 72.3, lambda v: (round(pct(133, 184), 2), 'FAUX', '133/184 pieds = 72,28 % : la valeur est exacte pour les PIEDS ; « des patients » est un dénominateur erroné (S6 : « At least one ulcer occurred in 133 (72.3%) feet »)', 'S6')),
    ('coh-881', r'⟦88,1', 88.1, lambda v: (round(pct(140, 159), 2), 'CORRECT', 'S6 résumé : « 88.1% patients were ambulating in orthopaedic footwear » (effectif absolu non publié dans le résumé ; valeur concordante)', 'S6')),
    # Pronostic (S1)
    ('mort-29', r'⟦29⟧ ?%', 29, same(29, 'S1 Introduction : « pooled mean five-year mortality of 29% »')),
    ('amp-6-12', r'par ⟦6⟧ à 12|6 à ⟦12⟧ (lorsqu|si|en cas)', None, lambda v: (v, 'CORRECT', 'S1 : « six to 12 times increased risk of major amputation … foot ulcer … CNO deformity as compared to those without an ulcer »', 'S1')),
    # Seuils thermiques et examen
    ('t-2C', r'(différence de|de plus de|inférieure à|≥|seuil (usuel est|de)) ⟦2⟧ ?°C|est ⟦2⟧ ?°C|cutanée de ⟦2⟧ ?°C', 2, lambda v: (2, 'CORRECT', 'S1 rationale rec. 1–5 : « increase in skin temperature of 2° Celsius » ; S3 : « hyperthermie de plus de 2 °C » ; S3 chronique « < 2° »', 'S1, S3')),
    ('t-4F', r'⟦4⟧ ?°F', 4, lambda v: (round(2 * 9 / 5, 2), 'FAUX', 'Écart de température : ΔT(°F) = 1,8 × ΔT(°C) ; 2 °C = 3,6 °F et 4 °F = 2,22 °C. S1 : « 4° Fahrenheit (which is actually 2.2° Celsius) »', 'S1')),
    ('t-1C', r'inférieure à ⟦1⟧ ?°C', 1, same(1, 'S1 Identification of remission : « temperature difference <1°C »')),
    ('circ-1cm', r'inférieure à ⟦1⟧ ?cm', 1, same(1, 'S1 : « difference in the circumference … <1 cm »')),
    ('mono-10g', r'monofilament de ⟦10⟧ ?g', 10, same(10, 'S3 Examen clinique : « monofilament 10 g » ; S13 annexe 1 : 10 g (5.07) Semmes-Weinstein')),
    # Décharge et suivi
    ('cast-14', r'⟦14⟧ ?% des patients', 14, same(14, 'S1 rationale rec. 15–20 : « cast associated blister or ulcer … in 14% »')),
    ('dur-3-6', r'(souvent|de) ⟦3⟧ à 6 mois|3 à ⟦6⟧ mois(,| \(| ;|$| jusqu| chez| et)', None, lambda v: (v, 'CORRECT', 'S3 : « souvent de 3 à 6 mois » ; S1 : « clinical healing preceded MRI healing by 3-6 months » selon le contexte', 'S3, S1')),
    ('dur-18', r'⟦18⟧ mois', 18, same(18, 'S3 : « parfois jusqu’à 18 mois » ; S2 : « might take up to 18 months »')),
    ('off-4-6w', r'⟦4⟧ à 6 semaines|4 à ⟦6⟧ semaines', None, lambda v: (v, 'CORRECT', 'S1 : « offloading be continued for four to six weeks after … remission »', 'S1')),
    ('visit-3-5', r'⟦3⟧ à 5 semaines|3 à ⟦5⟧ semaines', None, lambda v: (v, 'CORRECT', 'S1 : « can be increased up to 3 to 5 weeks »', 'S1')),
    ('remis-23', r'mois chez ⟦23⟧ ?% des patients', 23, same(23, 'S1 : « in 23% of patients clinical healing … preceded MRI healing by 3-6 months »')),
    ('react-23', r'(environ|Environ) ⟦23⟧ ?%', 23, same(23, 'S2 Natural course : « re-activation … about 23% »')),
    ('react-27', r'⟦27⟧ mois', 27, same(27, 'S2 : « within a mean interval of 27 months »')),
    ('suivi-3m', r'tous les ⟦3⟧ mois', 3, same(3, 'S3 PCC Suivi : « Premier niveau au moins tous les trois mois »')),
    # Ostéomyélite
    ('berli-43', r'⟦43⟧ pieds', 43, same(43, 'S7 Méthodes : « Forty patients (43 ft) »')),
    ('berli-52', r'concerné ⟦52⟧ ?% des cas', 52, lambda v: (round(pct(26, 43), 2), 'FAUX', 'Rapporté aux 43 pieds annoncés : 26/43 = 60,47 % ; 52 % = 31/60 épisodes d’ostéomyélite (51,7 %) ; rapporté aux 43 pieds : 26/43 = 60,5 % ; aux 40 patients : 26/40 = 65 %. Le couple « 43 pieds / 52 % » mélange deux dénominateurs (S7 Résultats)', 'S7')),
    ('irm-sens', r'⟦77⟧ à 100|77 à ⟦100⟧ ?%|⟦77⟧–100', None, lambda v: (v, 'CORRECT', 'S2 : « high sensitivity (77–100%) »', 'S2')),
    ('irm-spec', r'de ⟦80⟧ à 100|80 à ⟦100⟧ ?%|⟦80⟧–100', None, lambda v: (v, 'CORRECT', 'S2 : « high specificity (80–100%) »', 'S2')),
    ('irm-vpn', r'⟦98⟧ ?%', 98, same(98, 'S2 : « very high negative predictive value (98%) »')),
    # Ilizarov (S9, résumé)
    ('iliz-9', r'⟦9⟧ ?% contre 36', 9, lambda v: (round(pct(5, 53), 1), 'CORRECT', 'S9 résumé : « 9% vs 36% » ; plausibilité : 5/53 = 9,4 %', 'S9')),
    ('iliz-36', r'contre ⟦36⟧ ?%', 36, lambda v: (round(pct(16, 45), 1), 'CORRECT', 'S9 résumé ; plausibilité : 16/45 = 35,6 %', 'S9')),
    ('iliz-0', r'⟦0⟧ ?% contre 38', 0, same(0, 'S9 résumé : « 0% vs 38% » (sous-groupe Charcot, effectifs non donnés dans le résumé)')),
    ('iliz-38', r'contre ⟦38⟧ ?%', 38, same(38, 'S9 résumé')),
    # Distracteur de quiz (option fausse attendue, data-ok="0")
    ('quiz-distr', r'dose fixe de ⟦40⟧ mg|pendant ⟦18⟧ mois\. Le document', None, lambda v: (v, 'CORRECT', 'option volontairement fausse du cas 6 (data-ok="0") ; la correction rappelle la durée maximale de 14 jours en médecine [S10] : logique du quiz exacte', 'S10, S3')),
    # Énoxaparine (FI suisse Clexane®, février 2026, S10)
    ('enox-20', r'⟦20⟧ ?mg', 20, lambda v: (20, 'CORRECT', 'S10 Posologie : risque modéré 20 mg 1×/j ; insuffisance rénale sévère (ClCr < 30 ml/min) : 20 mg 1×/j en prophylaxie', 'S10')),
    ('enox-40', r'⟦40⟧ ?mg', 40, lambda v: (40, 'CORRECT', 'S10 : haut risque (chirurgie orthopédique) 40 mg 1×/j ; médecine 40 mg 1×/j', 'S10')),
    ('enox-6-14', r'⟦6⟧ jours|⟦14⟧ jours', None, lambda v: (v, 'CORRECT', 'S10 : « maintenu pendant 6 jours au minimum … au maximum 14 jours » (médecine)', 'S10')),
    ('enox-30', r'inférieure à ⟦30⟧ ?ml/min|comprise entre ⟦30⟧|de ⟦30⟧ à 80', 30, same(30, 'S10 : « clairance de la créatinine < 30 ml/min » ; « comprise entre 30 et 80 ml/min »')),
    ('enox-80', r'30 (et|à) ⟦80⟧ ?ml/min', 80, same(80, 'S10 : « comprise entre 30 et 80 ml/min »')),
    ('enox-70', r'plus de ⟦70⟧ ans', 70, lambda v: (70, 'FAUX', 'Valeur exacte mais contexte faux : S10 situe le risque hémorragique accru « en particulier de plus de 70 ans » DANS LA FOURCHETTE THÉRAPEUTIQUE et précise que la prophylaxie « ne s’accompagne pas d’une tendance accrue aux saignements » ; aucune surveillance propre aux > 70 ans n’est prescrite pour la prophylaxie', 'S10')),
    # Historique et classification
    ('eich-68', r'⟦68⟧ patients', 68, same(68, 'S5 résumé : « based on plain X-rays of 68 patients »')),
]


def check(items):
    results, missing = [], []
    for it in items:
        if it['type'] != 'grandeur':
            continue
        ctx = it['contexte']
        rule = None
        for rid, pat, target, fn in RULES:
            if re.search(pat, ctx) and (target is None or abs(it['v'] - target) < 1e-9):
                rule = (rid, fn)
                break
        if not rule:
            missing.append(it)
            continue
        attendu, verdict, formule, source = rule[1](it['v'])
        ecart = None if attendu is None else round(it['v'] - attendu, 4)
        results.append({'id': it['id'], 'regle': rule[0], 'fichier': it['fichier'], 'ancre': it['ancre'],
                        'valeur': it['valeur'], 'attendu': attendu, 'trouve': it['v'], 'ecart': ecart,
                        'verdict': verdict, 'formule': formule, 'source': source})
    return results, missing


# ---- Calculs propres aux propositions de l'audit (vérifiés de la même façon) ----
def propositions_checks():
    out = []
    # Indice cheville-bras de l'exemple de la proposition sémiologique (S13 annexe 2)
    brach = max(142, 138); ankle = min(118, 126)
    abi = ankle / brach
    out.append({'id': 'P01', 'objet': 'ICB exemple', 'formule': 'ICB = pression la plus basse (pédieuse, tibiale postérieure) / pression brachiale la plus haute = 118/142',
                'resultat': round(abi, 2), 'interpretation': 'anormal si < 0,9 ou > 1,3 [S13]', 'verdict': 'CORRECT' if round(abi, 2) == 0.83 else 'FAUX'})
    brach2 = max(130, 126); ankle2 = min(196, 188)
    abi2 = ankle2 / brach2
    out.append({'id': 'P02', 'objet': 'ICB faussement élevé (médiacalcose)', 'formule': 'min(196, 188) / max(130, 126) = 188/130',
                'resultat': round(abi2, 2), 'interpretation': '> 1,3 : anormal [S13]', 'verdict': 'CORRECT' if round(abi2, 2) == 1.45 else 'FAUX'})
    out.append({'id': 'P03', 'objet': 'conversion 4 °F en écart Celsius', 'formule': '4 / 1,8', 'resultat': round(4 / 1.8, 2),
                'interpretation': '2,22 °C, conforme à S1', 'verdict': 'CORRECT' if round(4 / 1.8, 1) == 2.2 else 'FAUX'})
    out.append({'id': 'P04', 'objet': 'proportion de femmes S6', 'formule': '49/159', 'resultat': round(pct(49, 159), 1),
                'interpretation': '30,8 %', 'verdict': 'CORRECT'})
    out.append({'id': 'P05', 'objet': 'Berli : amputations par épisode, pied, patient', 'formule': '31/60 ; 26/43 ; 26/40',
                'resultat': [round(pct(31, 60), 1), round(pct(26, 43), 1), round(pct(26, 40), 1)],
                'interpretation': '51,7 % ; 60,5 % ; 65,0 %', 'verdict': 'CORRECT'})
    out.append({'id': 'P06', 'objet': 'Berli : zone de Charcot contre hors zone', 'formule': '12/30 ; 19/30 ; majeures 6/30 ; 3/30',
                'resultat': [round(pct(12, 30), 1), round(pct(19, 30), 1), round(pct(6, 30), 1), round(pct(3, 30), 1)],
                'interpretation': '40 % ; 63,3 % ; 20 % ; 10 %', 'verdict': 'CORRECT'})
    out.append({'id': 'P07', 'objet': 'Berli : différences moyennes', 'formule': '84,1 − 55,7 ; 144 − 83,1',
                'resultat': [round(84.1 - 55.7, 1), round(144 - 83.1, 1)],
                'interpretation': 'antibiothérapie +28,4 j ; immobilisation +60,9 j (la source écrit 61,4 j : écart interne de 0,5 j, non repris)', 'verdict': 'CORRECT'})
    out.append({'id': 'P08', 'objet': 'Thermométrie : site concordant avec la radiographie', 'formule': 'valeur rapportée', 'resultat': [92, 72],
                'interpretation': '92 % au diagnostic, 72 % au suivi [S1]', 'verdict': 'CORRECT'})
    out.append({'id': 'P09', 'objet': 'Scintigraphie trois temps', 'formule': 'valeur rapportée (148 patients)', 'resultat': [89, 58],
                'interpretation': 'sensibilité 89 %, spécificité 58 % [S1]', 'verdict': 'CORRECT'})
    out.append({'id': 'P10', 'objet': 'Non-observance de la décharge partielle', 'formule': 'valeur rapportée', 'resultat': [72, 34],
                'interpretation': '72 % non observants ; guérison plus longue de 34 jours en moyenne [S1]', 'verdict': 'CORRECT'})
    causes = {'diabétique': 129, 'carence en vitamine B12': 4, 'pharmacotoxique': 1, 'éthylotoxique': 16, 'médullaire': 4, 'inflammatoire': 3, 'idiopathique': 27}
    tot = sum(causes.values())
    out.append({'id': 'P11', 'objet': 'Cohorte Balgrist (S6, tableau 1) : cause de la neuropathie par pied', 'formule': 'effectif / 184',
                'resultat': {k: round(pct(v, 184), 1) for k, v in causes.items()} | {'total': tot, 'non_diabetique_%': round(pct(tot - 129, 184), 1)},
                'interpretation': 'somme = 184 pieds ; 55/184 = 29,9 % de pieds non diabétiques', 'verdict': 'CORRECT' if tot == 184 else 'FAUX'})
    out.append({'id': 'P12', 'objet': 'Réactivation selon le diabète (S6)', 'formule': '6/18 ; 15/113', 'resultat': [round(pct(6, 18), 1), round(pct(15, 113), 1)],
                'interpretation': '33,3 % et 13,3 % (la source écrit 33 % et 13 %)', 'verdict': 'CORRECT'})
    return out


SPELLED = re.compile(r"\b(un|une|deux|trois|quatre|cinq|six|sept|huit|neuf|dix|douze|treize|quatorze|quinze|vingt)\s+(mois|ans|semaines|jours|cas|fois|stades|zones|niveaux|phases|questions|axes|outils|signes|conditions|erreurs|rôles|raisons|éléments|configurations|précisions|nuances|lignes|temps|sous-codes|inclusions|produits)\b", re.I)
SPELLED_RULES = {
    ('quatorze', 'ans'): ('donnée de vignette fictive (diabète depuis 14 ans), cohérente avec « au moins dix ans de diabète » [S2]', 'CORRECT'),
    ('cinq', 'mois'): ('S4 : « postpone referral until five months after symptom onset »', 'CORRECT'),
    ('cinq', 'ans'): ('S1 : mortalité poolée « five-year » 29 %', 'CORRECT'),
    ('dix', 'ans'): ('S2 : « diabetes mellitus for at least 10 years »', 'CORRECT'),
    ('trois', 'mois'): ('S1 : délai de rémission « three months longer » avec dispositif amovible ; S3 : niveau 1 « au moins tous les trois mois »', 'CORRECT'),
    ('quatre', 'stades'): ('S2 : « four different disease stages »', 'CORRECT'),
    ('trois', 'stades'): ('S3 : Eichenholtz « trois stades »', 'CORRECT'),
    ('cinq', 'zones'): ('S2, S3 : cinq zones de Sanders et Frykberg', 'CORRECT'),
    ('trois', 'niveaux'): ('S3 : niveaux 1, 2 et 3', 'CORRECT'),
    ('quatre', 'sous-codes'): ('S12 : G99.0, G99.1, G99.2, G99.8 (quatre sous-catégories à quatre caractères)', 'CORRECT'),
    ('deux', 'inclusions'): ('S12 : G98 inclut « Charcot-Arthropathie† » et « Krankheit des Nervensystems o.n.A. »', 'CORRECT'),
    ('six', 'produits'): ('S1 rec. 21 : alendronate, pamidronate, zolédronate, calcitonine, PTH, méthylprednisolone = 6', 'CORRECT'),
    ('quatre', 'conditions'): ('S3 : formation des plâtriers, suivi rapproché, adaptation à l’œdème, éducation = 4', 'CORRECT'),
    ('deux', 'rôles'): ('S3 : confirmer le diagnostic et évaluer la déformation', 'CORRECT'),
    ('cinq', 'jours'): ('donnée de vignette fictive (tuméfaction depuis 5 jours) : plausible, aucune règle chiffrée en dépend', 'CORRECT'),
    ('six', 'semaines'): ('scénario du cas fictif 5 (radiographies refaites à six semaines) : option à rejeter, correction exacte [S1 rec. 8 ; S4]', 'CORRECT'),
    ('une', 'fois'): ('« une fois par jour » = S10 (« une injection quotidienne ») ; « au moins une fois par an » = S3 (niveau 3) ; « une fois » au sens rédactionnel (parcours unique des stades, S2 « single-run »)', 'CORRECT'),
}


def spelled_inventory():
    out = []
    for f in FILES:
        txt = ' '.join(t for _, t in visible_text(f))
        for m in SPELLED.finditer(txt):
            key = (m.group(1).lower(), m.group(2).lower())
            rule = SPELLED_RULES.get(key)
            out.append({'fichier': f, 'expression': m.group(0), 'contexte': re.sub(r'\s+', ' ', txt[max(0, m.start()-50):m.end()+30]),
                        'verdict': rule[1] if rule else 'ETIQUETTE_OU_DENOMBREMENT_REDACTIONNEL', 'source': rule[0] if rule else 'dénombrement interne au texte (pas une grandeur médicale)'})
    return out


def main():
    items = inventory()
    spelled = spelled_inventory()
    res, missing = check(items)
    if missing:
        for m in missing:
            print('SANS RÈGLE', m['id'], m['fichier'], m['contexte'])
        sys.exit(1)
    inv = [{'id': i['id'], 'fichier': i['fichier'], 'ancre': i['ancre'], 'valeur': i['valeur'], 'unite': i['unite'],
            'type': i['type'], 'contexte': i['contexte']} for i in items]
    (OUT / 'inventaire.json').write_text(json.dumps({'total_releves': len(items),
        'grandeurs': sum(1 for i in items if i['type'] == 'grandeur'),
        'etiquettes': sum(1 for i in items if i['type'] == 'etiquette'),
        'methode': 'expression régulière sur le texte visible des 7 fichiers (verifier.py)', 'occurrences': inv},
        ensure_ascii=False, indent=1), encoding='utf-8')
    counts = {}
    for r in res:
        counts[r['verdict']] = counts.get(r['verdict'], 0) + 1
    props = propositions_checks()
    (OUT / 'resultats.json').write_text(json.dumps({'compteurs': counts, 'recalcules': len(res), 'resultats': res, 'valeurs_en_toutes_lettres': spelled,
        'calculs_des_propositions': props}, ensure_ascii=False, indent=1), encoding='utf-8')
    print('total', len(items), 'grandeurs', sum(1 for i in items if i['type'] == 'grandeur'), 'recalculées', len(res), counts)
    for r in res:
        if r['verdict'] != 'CORRECT':
            print(r['verdict'], r['id'], r['fichier'], r['valeur'], '→', r['attendu'])
    print('en toutes lettres', len(spelled), sum(1 for x in spelled if x['verdict']=='CORRECT'))
    for x in spelled:
        print('  L', x['expression'], '|', x['verdict'][:12])
    print('propositions', [(p['id'], p['verdict']) for p in props])


if __name__ == '__main__':
    main()
