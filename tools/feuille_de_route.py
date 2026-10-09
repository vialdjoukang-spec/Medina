#!/usr/bin/env python3
"""Feuille de route par leçon « Examen fédéral », par spécialité (annexe du prompt de transition)."""
import json, glob, html
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
SSP = json.load(open(ROOT / 'nosology/ssp_profiles2017.json'))
FREQ = set(json.load(open(ROOT / 'nosology/frequency.json'))['codes'])
NAMES = {x['id']: x for x in json.load(open(ROOT / 'organisation/fragments.json'))}
QUEUE = [x['id'] for x in json.load(open(ROOT / 'organisation/FILE_FRAGMENTS_CLAUDE.json'))['file']]
COVER = {}
for c in json.load(open(ROOT / 'chapters.json')):
    if c.get('integrated'):
        for k in c.get('covers', [c['code']]) + [c['code']]: COVER[k] = c
COMMON = ['Définition et classification', 'Épidémiologie (Suisse, puis Europe)', 'Physiopathologie et mécanismes']
END = ['Complications et pronostic', 'Prévention, dépistage et suivi', 'Situations particulières (grossesse, enfant, sujet âgé)',
       'Critères formels du diagnostic (div.alert) puis paramètres clés (div.key)', 'Pareto : ce qui fait 80 % de la décision']
TYPE = {
 'I': (['Agent pathogène, réservoir et transmission', 'Présentation clinique', 'Diagnostic microbiologique et différentiel',
        'Traitement anti-infectieux (information professionnelle suisse)', 'Hygiène, déclaration obligatoire OFSP, vaccination'], 'élevée',
       'SSI (ssi.guidelines.ch), OFSP, plan de vaccination suisse ; ECDC, ESCMID'),
 'II': (['Facteurs de risque et carcinogenèse', 'Présentation clinique et signes d’alarme', 'Diagnostic : imagerie, histologie, biologie moléculaire',
         'Stadification TNM et facteurs pronostiques', 'Traitement multimodal, colloque pluridisciplinaire', 'Dépistage organisé en Suisse'], 'très élevée',
        'ESMO, guidelines suisses de la spécialité, Ligue suisse contre le cancer, registres cantonaux'),
 'XV': (['Physiologie de la grossesse concernée', 'Présentation clinique et dépistage', 'Surveillance materno-fœtale',
         'Prise en charge (gynécologie suisse)', 'Médicaments compatibles grossesse et allaitement'], 'élevée', 'gynécologie suisse (SGGG), avis d’experts ; RCOG, FIGO comme données'),
 'XVI': (['Adaptation néonatale normale', 'Présentation clinique', 'Diagnostic et dépistage néonatal', 'Prise en charge (pédiatrie suisse)'], 'élevée',
         'Société suisse de néonatologie, Pédiatrie suisse (SSP) ; ESPR'),
 'XVIII': (['Physiologie du symptôme', 'Anamnèse et examen orientés', 'Drapeaux rouges', 'Démarche diagnostique étagée',
            'Diagnostics différentiels à ne pas manquer', 'Prise en charge symptomatique'], 'moyenne', 'mediX, Swiss Medical Forum, recommandations de la spécialité'),
 'V': (['Sémiologie psychiatrique et entretien', 'Évaluation du risque suicidaire, de violence et de la capacité de discernement',
        'Diagnostic selon la CIM-10-GM (DSM-5-TR seulement comme donnée) et diagnostic différentiel somatique',
        'Psychothérapies indiquées', 'Traitement médicamenteux (information professionnelle suisse)',
        'Cadre légal suisse : placement à des fins d’assistance, mesures de protection (Code civil)', 'Réseau de soins, réhabilitation et réinsertion'],
       'élevée', 'SSPP (Société suisse de psychiatrie et psychothérapie), SSPPEA (enfant et adolescent) ; EPA, NICE'),
 'XIX': (['Mécanisme lésionnel', 'Évaluation initiale et gravité (ABCDE)', 'Imagerie et bilan lésionnel', 'Traitement d’urgence puis définitif',
          'Rééducation, reprise du travail, assurance accidents (LAA, Suva)'], 'élevée', 'Suva, SSMUS, Swiss Orthopaedics ; ATLS seulement comme donnée'),
}
ORGAN = (['Facteurs de risque et étiologie', 'Anamnèse', 'Examen clinique', 'Examens complémentaires et diagnostic différentiel',
          'Traitement non médicamenteux', 'Traitement médicamenteux (information professionnelle suisse)', 'Urgences et critères d’hospitalisation'], 'élevée', None)
SOURCES = {  # sources de départ à vérifier, jamais citées sans lecture réelle
 'S01': 'Société suisse de cardiologie ; ESC', 'S02': 'Société suisse de pneumologie, Ligue pulmonaire ; ERS',
 'T1': 'SSI, OFSP ; ESCMID, ECDC', 'S03': 'SSG (gastroentérologie), SASL (foie) ; UEG, ESGE, EASL, ECCO',
 'S08': 'Société suisse de neurologie ; EAN', 'S05': 'SSED (endocrinologie et diabétologie) ; EASD, ESE',
 'S04': 'Société suisse de néphrologie ; ERA, KDIGO comme données', 'S06': 'SSH (hématologie) ; EHA',
 'T4': 'SAKK, Ligue contre le cancer, Société suisse de génétique médicale, palliative.ch ; ESMO',
 'S14': 'gynécologie suisse (SGGG) ; ESGO, ESHRE', 'S16': 'gynécologie suisse, Société suisse de néonatologie ; FIGO comme donnée',
 'T2': 'Pédiatrie suisse, Société professionnelle suisse de gériatrie ; EuGMS', 'S07': 'SSAI (allergologie et immunologie) ; EAACI',
 'S10': 'Société suisse de rhumatologie, Swiss Orthopaedics ; EULAR', 'S15': 'Société suisse d’urologie ; EAU',
 'S11': 'Société suisse de dermatologie et vénéréologie ; EADV, EDF', 'S12': 'Société suisse d’ORL, SSO (médecine dentaire) ; EAORL-HNS',
 'S13': 'Société suisse d’ophtalmologie ; EURETINA, EGS', 'T3': 'SSMUS (urgence), Tox Info Suisse, Suva ; ERC',
 'T5': 'Swiss Medical Forum, sociétés de radiologie et de médecine de laboratoire ; ESR', 'T6': 'mediX, SSMIG, OFSP ; WONCA Europe',
 'S09': 'SSPP, SSPPEA, OFSP (addictions), Infodrog ; EPA, ECNP, NICE',
 'T7': 'ASSM (directives éthiques), FMH, droit fédéral (Fedlex)',
}
EXTRA = {'S01': ['Imagerie et explorations fonctionnelles', 'Classification et scores'],
         'S02': ['Imagerie et explorations fonctionnelles respiratoires', 'Classification et scores'], 'T1': ['Microbiologie']}

def plan(fragment, chapter, code):
    add, diff, _ = TYPE.get(chapter, ORGAN)
    extra = [x for x in EXTRA.get(fragment, []) if x not in add]
    gen = ['Génétique et conseil génétique'] if chapter == 'XVII' else []
    return COMMON + add + extra + gen + END, diff

def build():
    out = ['# Annexe — Feuille de route par leçon « Examen fédéral »', '',
           'Générée par `tools/feuille_de_route.py` depuis `nosology/fragments/*.json`, `chapters.json`, `nosology/frequency.json` et PROFILES 2017 (`nosology/sources/profiles2017.pdf`). '
           'Une fiche par catégorie CIM-10-GM à trois caractères marquée « Examen fédéral ». Ordre : file de production, puis pathologies fréquentes, puis code. '
           'Priorité P0 : déjà rédigée, ne pas réécrire (correction seulement si erreur démontrée). P1 : fréquente et examen fédéral. P2 : examen fédéral.', '']
    files = {p.stem: p for p in (ROOT / 'nosology/fragments').glob('*.json')}
    order = QUEUE + [k for k in sorted(files) if k not in QUEUE]
    total = 0
    for fid in order:
        d = json.load(open(files[fid])); L = d['lessons']
        subs = {}
        for l in L:
            if l.get('parent'): subs.setdefault(l['parent'], []).append(l)
        cats = [l for l in L if '.' not in l['code'] and l['gold_star']['enabled']]
        if not cats: continue
        cats.sort(key=lambda l: (l['state'] == 'filled', l['code'] not in FREQ, l['code']))
        blocks = {}
        for l in L:
            if '.' not in l['code']: blocks.setdefault(l['block'], []).append(l['code'])
        label = NAMES[fid]['label']
        done = sum(l['state'] == 'filled' for l in cats)
        out += [f'## {label}', '', f'{len(cats)} leçons « Examen fédéral » ; {done} rédigées ; {sum(l["code"] in FREQ for l in cats)} fréquentes. '
                f'Sources de départ (à lire et dater réellement) : {SOURCES.get(fid, "société suisse de la spécialité, puis européenne")}.', '']
        for l in cats:
            total += 1
            code = l['code']; course = COVER.get(code)
            if l['state'] == 'filled' or course:
                prio = 'P0'
            else:
                prio = 'P1' if code in FREQ else 'P2'
            p, diff = plan(fid, l.get('chapter'), code)
            ssp = ', '.join(f'{n} ({SSP.get(str(n), "?")})' for n in l['gold_star']['ssp'])
            sc = subs.get(code, [])
            sib = [c for c in blocks.get(l['block'], []) if c != code]
            out.append(f'### {code} — {l["title"]} ({label}) · {prio}')
            out.append('')
            out.append(f'- **État** : {"rédigé" if l["state"] == "filled" else "vide"}'
                       + (f' ; couvert par le cours **{course["code"]} — {course["title"]}** : ne pas créer de leçon séparée, enrichir ce cours si besoin.' if course and course['code'] != code else '')
                       + (' ; cours existant : relecture seulement.' if course and course['code'] == code else ''))
            draft = list((ROOT / 'livraisons/Livraison Claude').glob(f'*/travail/{code}/rapport_auteur.md'))
            if draft and l['state'] != 'filled':
                rel = (draft[0].parent / 'rapport_relecture.md').exists()
                out.append(f'- **Brouillon existant** : `{draft[0].parent.relative_to(ROOT)}` — ' + ('relecture entamée, à reprendre' if rel else 'achevé, en attente du relecteur distinct') + ' : **ne pas réécrire**, lancer la relecture.')
            out.append(f'- **Chapitre CIM** {l.get("chapter")} · bloc {l["block"]} · difficulté **{diff}**' + (' · **pathologie fréquente** (sélection éditoriale à confirmer par une source suisse de fréquence)' if code in FREQ else ''))
            out.append(f'- **Situations PROFILES 2017** : {ssp}. Correspondance pédagogique, non officielle : chaque SSP doit se retrouver dans le cas clinique de l’îlot 0 ou dans un quiz.')
            if sc:
                out.append(f'- **Sous-codes à traiter dans ce cours** ({len(sc)}) : ' + ' ; '.join(f'{s["code"]} {s["title"]}' for s in sc[:40]) + (' ; …' if len(sc) > 40 else ''))
            if sib:
                out.append(f'- **Même bloc (renvois, ne pas redévelopper)** : {", ".join(sib[:30])}')
            out.append(f'- **Plan** : ' + ' → '.join(f'{i}. {t}' for i, t in enumerate(p)))
            out.append('- **Livrables** : `chapters/' + code + '/' + code + '_a…d.html`, `_pop1`, `_pop2`, `glossary/' + code.lower() + '.py`, rapports auteur et relecture dans `livraisons/Livraison Claude/' + label + '/travail/' + code + '/`.')
            out.append('')
    out.insert(3, f'Total : {total} fiches.')
    return '\n'.join(out)

if __name__ == '__main__':
    (ROOT / 'ANNEXE_FEUILLE_DE_ROUTE.md').write_text(build(), encoding='utf-8')
    print('ok')
