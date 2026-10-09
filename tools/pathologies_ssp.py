#!/usr/bin/env python3
"""Pathologies permettant de couvrir les 265 SSP de PROFILES 2017, par spécialité, avec plan spécifique.

Méthode (reproductible) :
1. Socle : pathologies fréquentes (nosology/frequency.json) et cours existants (chapters.json).
2. Correspondance SSP → catégorie de Codex (gold_star.ssp) ; couverture gloutonne des SSP restantes, en préférant
   la catégorie qui couvre le plus de SSP encore manquantes (à égalité : fréquente, puis code).
3. SSP sans catégorie dans cette correspondance : rattachement explicite ci-dessous (proposition pédagogique à valider),
   vers une pathologie du catalogue, le volet psychiatrique (F00-F99, hors des 22 fragments, cf. PROMPT_MEDINA.md)
   ou un fragment transversal.
"""
import json
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from feuille_de_route import plan, SOURCES, NAMES, QUEUE, COVER, FREQ, SSP

MANUAL = {  # SSP : catégories (ou 'PSY:Fxx' pour le volet psychiatrique)
 7: ['E34', 'N95'], 8: ['T68'], 13: ['R99'], 20: ['G51'], 21: ['R04'], 22: ['G24'], 23: ['R13', 'T17'], 29: ['Q02', 'Q03'],
 32: ['M54'], 34: ['G47'], 43: ['R07', 'I25'], 56: ['K60', 'K64', 'L29'], 57: ['K62', 'K64', 'K92'], 62: ['Q56', 'E25'],
 89: ['L80', 'L81'], 109: ['S43', 'S83'], 117: ['S25'], 118: ['PSY:F41'], 119: ['PSY:F90'], 120: ['PSY:F07', 'R45'],
 121: ['PSY:F50'], 122: ['PSY:F32', 'R45'], 123: ['PSY:F90'], 124: ['PSY:F40', 'PSY:F45'], 125: ['PSY:F91', 'R45'],
 127: ['PSY:F42'], 128: ['PSY:F43'], 129: ['PSY:F32', 'T74'], 130: ['PSY:F10', 'PSY:F17'], 132: ['Q54', 'Q55'],
 134: ['R22'], 135: ['R22'], 136: ['R22', 'J96'], 141: ['PSY:F20', 'R47'], 142: ['E05', 'H05'], 143: ['R19', 'K05'],
 148: ['I46'], 150: ['E87', 'J96'], 166: ['O36', 'P55', 'T80'], 185: ['PSY:F91', 'PSY:F98'], 186: ['T74'], 192: ['R68'],
 193: ['PSY:F81'], 195: ['Z00'], 196: ['T74'], 198: ['E43', 'E44', 'E46', 'M62'], 199: ['Z91'], 212: ['H57'],
 213: ['PSY:F32', 'T74'], 216: ['PSY:F05', 'R41'], 221: ['Z02'], 228: ['Z63'], 232: ['Z51'], 234: ['PSY:F45'],
 236: ['Z60', 'Z56'], 237: ['Z70'], 239: ['Z63', 'PSY:F43'], 240: ['Z51', 'PSY:F43'], 243: ['Z02'], 245: ['Z73'],
 246: ['Z02'], 248: ['K90', 'T78'], 249: ['R69', 'PSY:F45'], 254: ['Z60', 'Z59'], 257: ['Z01'], 259: ['Z71'],
 260: ['Z71'], 262: ['Z76'], 265: ['Z60', 'Z59'],
}

def main():
    lessons = {}
    for path in (ROOT / 'nosology/fragments').glob('*.json'):
        for l in json.load(open(path))['lessons']:
            if '.' not in l['code']:
                lessons[l['code']] = l
    ssp_of = {c: set(l['gold_star']['ssp']) if l['gold_star']['enabled'] else set() for c, l in lessons.items()}
    # Principe de Vial : jeu de déduction. Une SSP renvoie à TOUS les diagnostics où elle se retrouve
    # (différentiels compris) ; tous ces diagnostics sont prioritaires (P1) dans leur système, le reste vient ensuite (P2).
    chosen = {}
    psy = {}
    for s, targets in MANUAL.items():
        for t in targets:
            if t.startswith('PSY:') and t[4:] in lessons:
                t = t[4:]
            if t.startswith('PSY:'):
                psy.setdefault(t[4:], set()).add(s)
            elif t in lessons:
                ssp_of[t] = ssp_of[t] | {s}
    for c in lessons:
        if ssp_of[c]:
            chosen.setdefault(c, 'P1 · SSP ' + ', '.join(map(str, sorted(ssp_of[c]))))
    rest = [c for c in lessons if c not in chosen]
    holders = {}
    for c in chosen:
        for x in ssp_of[c]: holders.setdefault(x, set()).add(c)
    broad = {x for x, cs in holders.items() if len(cs) > 40}  # SSP transversales, trop générales pour orienter un différentiel
    covered = set().union(*(ssp_of[c] for c in chosen)) | {s for v in psy.values() for s in v}
    missing = sorted(set(range(1, 266)) - covered)
    by_ssp = {}
    for c in chosen:
        for s in ssp_of[c]: by_ssp.setdefault(s, []).append(c)
    out = ['# Annexe A — Diagnostics cibles déduits des 265 situations PROFILES (SSP), par spécialité', '',
           'Principe (Vial) : jeu de déduction entre les SSP et les diagnostics répertoriés. Une SSP renvoie à **tous** les diagnostics où elle se retrouve, '
           'différentiels compris. Tous ces diagnostics sont **prioritaires (P1)** lors de la rédaction de leur système ; les autres catégories du système (**P2**) sont rédigées ensuite.', '',
           f'**{len(chosen)} diagnostics P1** (sur {len(lessons)} catégories) ; **{len(rest)} catégories P2**. SSP couvertes : **{len(covered)} / 265**' + (f' ; non couvertes : {missing}.' if missing else ' (toutes).'), '',
           'Ordre de rédaction dans un système : pathologies fréquentes, puis diagnostics partageant le plus de SSP (les plus « carrefours » du diagnostic différentiel), puis les autres P1, puis P2. '
           'Une catégorie déjà rédigée n’est pas réécrite. Réserve : la correspondance SSP → catégories (outil de Codex) est établie par bloc CIM, donc large ; '
           'elle est pédagogique, non officielle, et doit être affinée catégorie par catégorie pendant la rédaction.', '']
    order = QUEUE + [k for k in sorted(NAMES) if k not in QUEUE]
    for fid in order:
        items = sorted((c for c in chosen if lessons[c]['fragment'] == fid),
                       key=lambda c: (lessons[c]['state'] == 'filled', c not in FREQ, -len(ssp_of[c]), c))
        p2 = sorted(c for c in rest if lessons[c]['fragment'] == fid)
        if not items: continue
        label = NAMES[fid]['label']
        out += [f'## {label} — {len(items)} diagnostics P1, {len(p2)} catégories P2', '', f'Sources de départ (à lire et dater) : {SOURCES.get(fid, "société suisse, puis européenne")}.', '']
        for c in items:
            l = lessons[c]; p, diff = plan(fid, l.get('chapter'), c)
            course = COVER.get(c)
            state = 'rédigée' if l['state'] == 'filled' else ('couverte par ' + course['code'] if course and course['code'] != c else 'à produire')
            draft = list((ROOT / 'livraisons/Livraison Claude').glob(f'*/travail/{c}/rapport_auteur.md'))
            if draft and l['state'] != 'filled': state = 'brouillon achevé, à relire (ne pas réécrire)'
            ssps = '; '.join(f'{s} {SSP[str(s)]}' for s in sorted(ssp_of[c]))
            out += [f'### {c} — {l["title"]}', '',
                    f'- **Priorité** : P1{" · fréquente" if c in FREQ else ""} · **état** : {state} · **difficulté** : {diff} · chapitre {l.get("chapter")}, bloc {l["block"]}',
                    f'- **SSP à satisfaire dans ce cours** : {ssps or "aucune propre (socle clinique)"}',
                    '- **Différentiels à traiter en miroir** (diagnostics partageant au moins une SSP, même système) : '
                    + (', '.join(sorted(d for d in items if d != c and ssp_of[d] & ssp_of[c])) or '—'),
                    '- **Différentiels hors système** (SSP partagée, hors SSP transversales) : '
                    + (', '.join(f'{d} ({lessons[d]["fragment"]})' for d in sorted(d for d in chosen if lessons[d]['fragment'] != fid and (ssp_of[d] & ssp_of[c]) - broad)) or '—'),
                    '- **Plan** : ' + ' → '.join(f'{i}. {t}' for i, t in enumerate(p)), '']
        if p2:
            out += ['**P2 (après les P1 du système)** : ' + ', '.join(f'{c} {lessons[c]["title"]}' for c in p2), '']
    if psy:
        out += ['## Entités psychiatriques hors catalogue', '']
        out += [f'- **{f}** : SSP ' + ', '.join(f'{s} {SSP[str(s)]}' for s in sorted(v)) for f, v in sorted(psy.items())]
    out += ['', '## Matrice SSP → pathologies', '', '| SSP | Situation | Pathologies |', '|---|---|---|']
    for s in range(1, 266):
        cs = by_ssp.get(s, []) + [f'psy {f}' for f, v in psy.items() if s in v]
        out.append(f'| {s} | {SSP[str(s)]} | {", ".join(sorted(cs))} |')
    (ROOT / 'ANNEXE_PATHOLOGIES_SSP.md').write_text('\n'.join(out), encoding='utf-8')
    print(len(chosen), 'P1 ;', len(rest), 'P2 ; couvertes', len(covered), '; manquantes', missing)

if __name__ == '__main__':
    main()
