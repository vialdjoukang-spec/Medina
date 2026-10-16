#!/usr/bin/env python3
"""MEDINA — recuit simulé des 23 emplacements catégoriels (outil de régénération, non exécuté au build).

Cherche 23 teintes (L, h) dans une bande de luminosité égalisée, leur ordre de rang et l’affectation
des 23 spécialités, sous les contraintes du validateur de la compétence dataviz :
  - contractuel (doit passer) : voisins de rang, voisins verticaux des grilles à 3 et 4 colonnes,
    ordre d’affichage de l’Accueil — CVD (Machado 2009, protan/deutan) ≥ --cvd, vision normale ≥ 15,6 ;
  - Accueil en 2 et 3 colonnes : voisins verticaux, vision normale ≥ --colonnes ;
  - écart minimal toutes paires (vision normale) ≥ --toutes-paires (23 teintes distinctes) ;
  - puis : cibles sémantiques des spécialités (écart de teinte pondéré).
Le résultat (JSON) se reporte dans palette.py avec --emettre, puis : palette.py --ecrire --doc --valider.

Exemple (16.10.2026, palette par défaut, à partir de la palette en vigueur) :
  python3 docs/frontend/couleurs/recuit.py --graine 64 --iterations 1500000 --t0 1.5 --semantique 1.2 \\
      --depart actuel --sortie /tmp/recuit.json
  python3 docs/frontend/couleurs/recuit.py --emettre /tmp/recuit.json
Les validateurs sont recherchés comme dans palette.py (--validateur ou MEDINA_VALIDATEUR).
"""
import argparse
import json
import math
import os
import random
import sys
from functools import lru_cache
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import palette as P  # noqa: E402

N = len(P.EMPLACEMENTS)
SPEC = sorted(P.SPECIALITES)
# cibles sémantiques (teinte OKLCH) et poids : rouge cardiaque, grenat hématologique, pervenche
# neurologique, bleu pulmonaire, violet psychiatrique, vert sapin infectiologique ; les autres
# spécialités gardent la teinte de la palette précédente (poids 1).
CIBLES = {'S01': 25, 'S06': 5, 'S08': 285, 'S02': 250, 'S09': 305, 'T1': 145}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--validateur', default=os.environ.get('MEDINA_VALIDATEUR', P.DEFAUT_VALIDATEUR))
    ap.add_argument('--bande', default=f'{P.BANDE_REPERES[0]},{P.BANDE_REPERES[1]}')
    ap.add_argument('--graine', type=int, default=1)
    ap.add_argument('--iterations', type=int, default=1000000)
    ap.add_argument('--t0', type=float, default=20.0)
    ap.add_argument('--semantique', type=float, default=0.3, help='poids de l’écart sémantique (par degré)')
    ap.add_argument('--cvd', type=float, default=6.6)
    ap.add_argument('--toutes-paires', type=float, default=3.6)
    ap.add_argument('--colonnes', type=float, default=9.0)
    ap.add_argument('--depart', help='« actuel » (palette.py) ou fichier JSON d’un recuit précédent')
    ap.add_argument('--sortie')
    ap.add_argument('--emettre', help='affiche EMPLACEMENTS et SPECIALITES à reporter dans palette.py')
    ap.add_argument('--noms', help='noms des 23 emplacements, séparés par des virgules (avec --emettre)')
    a = ap.parse_args()
    if a.emettre:
        return emettre(a)
    sys.path.insert(0, a.validateur)
    import validate_palette as vp
    lmin, lmax = (float(x) for x in a.bande.split(','))
    niveaux = [round(lmin + i * (lmax - lmin) / 6, 4) for i in range(7)]
    random.seed(a.graine)
    actuel = {n: h for n, L, C, h in P.EMPLACEMENTS}
    cible = {s: actuel[P.SPECIALITES[s]] for s in SPEC} | CIBLES
    poids = {s: 3.0 if s in CIBLES else 1.0 for s in SPEC}
    ordre = P.ORDRE_PORTAIL.split(',')

    @lru_cache(maxsize=None)
    def couleur(L, h):
        C = math.floor(min(0.12, P.chroma_max(L, h, 0.12)) * 1000) / 1000
        x = P.oklch_hex(L, C, h)[0]
        return C, {k: vp.lin2oklab(*(vp.simulate(x, k) if k else vp.lin(x))) for k in (None, 'protan', 'deutan')}

    @lru_cache(maxsize=2000000)
    def ecart(u, v):
        la, lb = couleur(*u)[1], couleur(*v)[1]
        return (100 * min(math.dist(la['protan'], lb['protan']), math.dist(la['deutan'], lb['deutan'])),
                100 * math.dist(la[None], lb[None]))

    paires = [(i, i + 1) for i in range(N - 1)] + [(i, i + k) for k in (3, 4) for i in range(N - k)]

    def score(pos, spec):
        pire, pire_cvd = 99, 99
        accueil = [pos[spec[s]] for s in ordre]
        for u, v in [(pos[i], pos[j]) for i, j in paires] + list(zip(accueil, accueil[1:])):
            cvd, nor = ecart(u, v)
            pire, pire_cvd = min(pire, cvd / a.cvd, nor / 15.6), min(pire_cvd, cvd / 8.0)
        for k in (2, 3):
            for c in range(k):
                col = accueil[c::k]
                for u, v in zip(col, col[1:]):
                    pire = min(pire, ecart(u, v)[1] / a.colonnes)
        toutes = min(ecart(pos[i], pos[j])[1] for i in range(N) for j in range(i + 1, N))
        pire = min(pire, toutes / a.toutes_paires)
        penal = sum(1 for L, h in pos if couleur(L, h)[0] < 0.102)
        sem = sum(poids[s] * abs((pos[spec[s]][1] - cible[s] + 180) % 360 - 180) for s in SPEC) / sum(poids.values())
        return (min(pire, 1) * 1000 + min(pire_cvd, 1.1) * 150 + min(toutes / 6, 1) * 40 - penal * 1000 - sem * a.semantique,
                {'contraintes': round(pire, 4), 'cvd_sur_8': round(pire_cvd, 4), 'toutes_paires': round(toutes, 2), 'semantique_deg': round(sem, 2)})

    noms = [n for n, *_ in P.EMPLACEMENTS]
    if a.depart == 'actuel':
        pos = [(L, h) for _, L, C, h in P.EMPLACEMENTS]
        spec = {s: noms.index(P.SPECIALITES[s]) for s in SPEC}
    elif a.depart:
        w = json.loads(Path(a.depart).read_text(encoding='utf-8'))
        pos, spec = [tuple(x) for x in w['slots']], dict(w['spec'])
    else:   # teintes équiréparties, luminosités alternées, affectation gloutonne aux cibles
        theta = random.uniform(0, 360)
        pos = [((niveaux[0], niveaux[6], niveaux[3])[k % 3], round((theta + k * 360 / N) % 360, 1)) for k in range(N)]
        spec, libres = {}, set(range(N))
        for s in sorted(SPEC, key=lambda s: -poids[s]):
            j = min(libres, key=lambda j: abs((pos[j][1] - cible[s] + 180) % 360 - 180))
            spec[s] = j
            libres.remove(j)
    cur, info = score(pos, spec)
    meilleur = (cur, info, list(pos), dict(spec))
    for it in range(a.iterations):
        T = a.t0 * (1 - it / a.iterations) + 0.02
        np_, ns = list(pos), dict(spec)
        r = random.random()
        if r < 0.40:      # échanger deux rangs ; les spécialités suivent leur couleur
            i, j = random.sample(range(N), 2)
            np_[i], np_[j] = np_[j], np_[i]
            inv = {v: k for k, v in ns.items()}
            ns[inv[i]], ns[inv[j]] = j, i
        elif r < 0.55:    # échanger les couleurs de deux spécialités
            u, v = random.sample(SPEC, 2)
            ns[u], ns[v] = ns[v], ns[u]
        elif r < 0.85:    # déplacer une teinte
            i = random.randrange(N)
            np_[i] = (np_[i][0], round((np_[i][1] + random.gauss(0, 3)) % 360, 1))
        else:             # changer de niveau de luminosité dans la bande
            i = random.randrange(N)
            np_[i] = (random.choice(niveaux), np_[i][1])
        sc, inf = score(np_, ns)
        if sc > cur or random.random() < math.exp((sc - cur) / T):
            pos, spec, cur, info = np_, ns, sc, inf
            if sc > meilleur[0]:
                meilleur = (sc, inf, list(np_), dict(ns))
    sortie = {'score': meilleur[0], 'mesures': meilleur[1], 'slots': meilleur[2], 'spec': meilleur[3]}
    texte = json.dumps(sortie, ensure_ascii=False)
    print(texte)
    if a.sortie:
        Path(a.sortie).write_text(texte + '\n', encoding='utf-8')


def emettre(a):
    w = json.loads(Path(a.emettre).read_text(encoding='utf-8'))
    noms = a.noms.split(',') if a.noms else [f'teinte-{i + 1}' for i in range(N)]
    items = []
    for i, (L, h) in enumerate(w['slots']):
        C = math.floor(min(0.12, P.chroma_max(L, h, 0.12)) * 1000) / 1000
        items.append(f"('{noms[i]}', {L:.3f}, {C:.3f}, {h:.1f})")
    print('EMPLACEMENTS = [')
    for k in range(0, N, 3):
        print('    ' + ', '.join(items[k:k + 3]) + ',')
    print(']')
    sp = {s: noms[j] for s, j in w['spec'].items()}
    print('SPECIALITES = {')
    cles = sorted(sp)
    for k in range(0, len(cles), 6):
        print('    ' + ' '.join(f"'{s}': '{sp[s]}'," for s in cles[k:k + 6]))
    print('}')


if __name__ == '__main__':
    main()
