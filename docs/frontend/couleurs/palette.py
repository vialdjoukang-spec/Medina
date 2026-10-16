#!/usr/bin/env python3
"""MEDINA — source unique des couleurs : calcul OKLCH, contrôles et génération des tokens.

Toutes les teintes sont posées en OKLCH (L, C, h) puis converties en sRGB. Les contrôles
reprennent les fonctions du validateur de la compétence dataviz (validate_palette.py :
OKLab ×100, simulation Machado 2009, contraste WCAG) et appellent validate_palette.js.

Usage :
  python3 docs/frontend/couleurs/palette.py                 # tableau des tokens et contrôles
  python3 docs/frontend/couleurs/palette.py --ecrire        # réécrit le bloc de tokens de engine/couleurs_premium.css
  python3 docs/frontend/couleurs/palette.py --doc           # réécrit les tableaux générés de PALETTE.md
  python3 docs/frontend/couleurs/palette.py --valider       # lance validate_palette.js sur les séquences catégorielles
  python3 docs/frontend/couleurs/palette.py --ordre-portail S16,S08,...   # contrôle un nouvel ordre de l’Accueil

Le validateur se trouve dans le répertoire de la compétence dataviz (option --validateur ou
variable MEDINA_VALIDATEUR). Les 23 emplacements catégoriels ont été choisis par recuit simulé
(recuit.py : luminosité égalisée dans la bande 0,52–0,58 ; écart minimal entre voisins en
protanopie/deutéranopie, plancher 15 en vision normale, voisins verticaux de grille à 3 et 4
colonnes, ordre de l’Accueil ; écart minimal toutes paires ; cibles sémantiques), puis figés ici :
ordre fixe. Les contrôles « vision photopique diurne » (TCP et Duv des neutres, luminosité égale
à rôle égal, plafond de chroma, encres bleues) sont décrits dans PALETTE.md.
"""
import argparse
import json
import math
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CSS = ROOT / 'engine/couleurs_premium.css'
DOC = ROOT / 'docs/frontend/couleurs/PALETTE.md'
DEFAUT_VALIDATEUR = '/tmp/claude-0/bundled-skills/2.1.301/6bebc0210b07966a293216c0a2d1ec32/dataviz/scripts'
ORDRE_PORTAIL = 'S16,S08,S10,S11,S12,T3,S03,S09,S05,S13,S14,T1,S15,T6,S06,S02,S01,S04,T4,T5,S07,T2,T7'
ORDRE_REGISTRE = 'S01,S02,T1,S03,S08,S05,S04,S06,T4,S14,S16,T2,S07,S10,S15,S11,S12,S13,T3,T5,T6,T7,S09'


# ------------------------------------------------------------------ conversions
def oklch_hex(L, C, h):
    a, b = C * math.cos(math.radians(h)), C * math.sin(math.radians(h))
    l_ = L + 0.3963377774 * a + 0.2158037573 * b
    m_ = L - 0.1055613458 * a - 0.0638541728 * b
    s_ = L - 0.0894841775 * a - 1.2914855480 * b
    l, m, s = l_ ** 3, m_ ** 3, s_ ** 3
    rgb = (4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s,
           -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s,
           -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s)
    enc = [12.92 * c if c <= 0.0031308 else 1.055 * max(c, 0) ** (1 / 2.4) - 0.055 for c in rgb]
    ok = all(-1e-4 <= c <= 1 + 1e-4 for c in enc)
    return '#%02x%02x%02x' % tuple(max(0, min(255, round(c * 255))) for c in enc), ok


def chroma_max(L, h, plafond):
    lo, hi = 0.0, plafond
    if oklch_hex(L, hi, h)[1]:
        return hi
    for _ in range(32):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if oklch_hex(L, mid, h)[1] else (lo, mid)
    return lo


def dans_gamut(L, C, h):
    return oklch_hex(L, C, h)[1]


# ------------------------------------------------------------------ neutres et marque
# Vision photopique diurne (16.10.2026, exigence de Vial) : blanc de référence D65, celui de sRGB.
# Les neutres suivent un seul axe « papier sous la lumière du jour » : teinte 80 (très légèrement
# chaude), chroma ≤ 0,006, si bien que leur température de couleur proximale reste entre 5 700 et
# 6 500 K, sur le locus des lumières du jour (Duv ≈ +0,003) : ni bleutés froids (> 6 600 K), ni
# crème jaunie (< 5 500 K). Les anciens neutres (teintes 160 et 250-255) mesuraient 6 530 K avec une
# dérive verte (Duv +0,0047) pour le papier, puis 6 800 à 13 400 K (bleutés) pour filets et encres.
NEUTRE_H = 80
NEUTRES = [
    ('--n-surface', 1.000, 0.000, NEUTRE_H, 'Cartes, îlots, fenêtres, Navigo (blanc D65)'),
    ('--n-paper', 0.976, 0.004, NEUTRE_H, 'Fond de page (surface de validation)'),
    ('--n-sunken', 0.957, 0.005, NEUTRE_H, 'Encarts, puits, jauges informatives, survol neutre'),
    ('--n-line-soft', 0.912, 0.004, NEUTRE_H, 'Séparations décoratives (non interactives)'),
    ('--n-line', 0.862, 0.005, NEUTRE_H, 'Bordures de cartes, de tableaux et d’îlots'),
    ('--n-line-strong', 0.595, 0.006, NEUTRE_H, 'Contours interactifs (≥ 3:1 sur surface, papier et encart)'),
    ('--ink-3', 0.480, 0.005, NEUTRE_H, 'Texte atténué (≥ 4,5:1 sur encart)'),
    ('--ink-2', 0.360, 0.005, NEUTRE_H, 'Texte courant de l’interface'),
    ('--ink-1', 0.215, 0.004, NEUTRE_H, 'Encre primaire, titres de l’interface'),
]
SURFACES_PAPIER = ('--n-surface', '--n-paper', '--n-sunken')   # C ≤ 0,012 et 5 500 K ≤ TCP ≤ 6 600 K
# Ombres : lumière du jour venant d’en haut (décalage vers le bas, liseré clair en haut), couleur
# = surface assombrie (même teinte que le papier), jamais un gris bleuâtre.
OMBRE = (0.240, 0.008, NEUTRE_H)
VOILE = (0.220, 0.008, NEUTRE_H, 0.55)
PAPIER = oklch_hex(*NEUTRES[1][1:4])[0]   # fond de page rendu (--n-paper), surface de validation
MARQUE_H = 158.4            # teinte OKLCH de #1f3428, ancre historique de Medina
MARQUE = [  # pas, L, C — le pas 700 est l’ancre exacte #1f3428
    (50, 0.975, 0.010), (100, 0.948, 0.022), (200, 0.895, 0.038), (300, 0.810, 0.058),
    (400, 0.690, 0.078), (500, 0.580, 0.088), (600, 0.470, 0.080), (700, None, None), (800, 0.235, 0.028),
]
ANCRE = '#1f3428'

# ------------------------------------------------------------------ 23 emplacements catégoriels
# (nom, L, C, h) — luminosité égalisée (bande 0,52–0,58, vision photopique), chroma 0,102 à 0,120 (plafond 0,12 :
# sobriété). Recuit du 16.10.2026 : voisins de rang, colonnes de 3 et 4 et ordre de l’Accueil passent le validateur
# (CVD ≥ 6,6, vision normale ≥ 15,6), voisins verticaux de l’Accueil en 2 et 3 colonnes ≥ 7 (vision normale),
# écart minimal toutes paires ≥ 3,6, cibles sémantiques des spécialités (recuit.py, graine 76).
EMPLACEMENTS = [
    ('moutarde', 0.522, 0.108, 100.4), ('petrole', 0.531, 0.102, 226.8), ('vieux-rose', 0.578, 0.120, 10.7),
    ('lagon', 0.578, 0.102, 215.4), ('prune', 0.522, 0.120, 349.7), ('olive', 0.578, 0.120, 106.8),
    ('amethyste', 0.522, 0.120, 296.9), ('ambre', 0.522, 0.110, 74.9), ('bleuet', 0.541, 0.120, 249.6),
    ('brique', 0.522, 0.120, 31.2), ('jade', 0.578, 0.102, 183.1), ('orchidee', 0.522, 0.120, 330.3),
    ('emeraude', 0.578, 0.120, 165.8), ('pervenche', 0.569, 0.120, 285.2), ('ocre', 0.578, 0.118, 85.9),
    ('saphir', 0.578, 0.120, 255.1), ('rouille', 0.522, 0.120, 56.9), ('malachite', 0.522, 0.106, 167.4),
    ('rose', 0.578, 0.120, 349.3), ('sapin', 0.578, 0.120, 147.6), ('violet', 0.578, 0.120, 305.2),
    ('cuivre', 0.559, 0.120, 69.9), ('indigo', 0.522, 0.120, 274.5),
]
# Une teinte par spécialité (identité fixe, Accueil et fragment). Toujours accompagnée du nom.
SPECIALITES = {
    'S01': 'brique', 'S02': 'bleuet', 'S03': 'jade', 'S04': 'lagon', 'S05': 'ocre', 'S06': 'rose',
    'S07': 'indigo', 'S08': 'pervenche', 'S09': 'violet', 'S10': 'moutarde', 'S11': 'vieux-rose', 'S12': 'petrole',
    'S13': 'saphir', 'S14': 'prune', 'S15': 'amethyste', 'S16': 'cuivre', 'T1': 'sapin', 'T2': 'olive',
    'T3': 'rouille', 'T4': 'ambre', 'T5': 'emeraude', 'T6': 'malachite', 'T7': 'orchidee',
}
# Couleurs de catégorie posées par engine/atlas_v2.js (rang 0..19) → emplacement du même rang.
ATLAS_V2 = ['#C2185B', '#1565C0', '#2E7D32', '#BF360C', '#6A1B9A', '#00796B', '#C62828', '#283593', '#8E5A00', '#AD1457',
            '#0277BD', '#1B5E20', '#7B1FA2', '#9E2A2B', '#00695C', '#5D4037', '#4527A0', '#00777F', '#B23C0E', '#37602B']
DERNIER_RANG = 32            # rangs couverts par un remappage explicite (max actuel : 30, S10)
# Vision photopique : à rôle égal, luminosité perçue égale. Repères dans une bande L 0,52–0,58
# (± 0,03 autour de 0,55) ; encres à L 0,43 ; fonds à L 0,975 ; sélections à L 0,945.
BANDE_REPERES = (0.522, 0.578)
ENCRE_L = 0.430             # encre de chaque teinte (texte) : luminosité unique, ≥ 6:1 sur sa teinte claire
# Faible acuité des cônes S : pas de bleu saturé pour du texte. Les encres bleues à violettes
# (teintes 215 à 300) sont plafonnées à C 0,080 ; leur lisibilité repose sur le contraste de
# luminance (voies L + M), non sur la chroma.
BLEUS, ENCRE_C_BLEU = (215, 300), 0.080
CHROMA_PLAFOND = 0.150      # aucune couleur « néon » : plafond global (repères 0,12 ; or 0,145)
TEINTE_CLAIRE = (0.975, 0.012)   # fond teinté (L, C)
TEINTE_SELECTION = (0.945, 0.028)

# ------------------------------------------------------------------ statuts, jauges, or, leçon
STATUTS = [  # nom, (L, C, h) encre, (L, C, h) fond, libellé, forme
    ('ok', (0.470, 0.100, 150), (0.962, 0.026, 150), 'Disponible', 'disque plein'),
    ('prep', (0.480, 0.005, NEUTRE_H), (0.957, 0.005, NEUTRE_H), 'En préparation', 'cercle vide'),
    ('prov', (0.490, 0.105, 62), (0.962, 0.032, 80), 'Provisoire', 'demi-disque'),
]
JAUGE = [(400, 0.690, 0.078), (500, 0.580, 0.088), (600, 0.470, 0.080), (700, 0.380, 0.060)]   # rampe de la marque
OR = [(100, 0.965, 0.050, 92), (300, 0.880, 0.120, 88), (500, 0.760, 0.145, 80), (600, 0.640, 0.130, 72), (700, 0.520, 0.105, 65), (800, 0.400, 0.075, 62)]
LECON = [  # rôles sémantiques des cours, valeurs historiques conservées (règles de Vial)
    ('--lesson-ink', '#0f2c66', 'Corps des cours du cycle (bleu marine renforcé)'),
    ('--lesson-title', '#b3261e', 'Titres et numéros rouges soulignés'),
    ('--lesson-term', '#9b3900', 'Termes interactifs des cours du cycle'),
    ('--lesson-word', '#187349', 'Mot vert : fenêtre explicative ou contentieux'),
    ('--lesson-abbr', '#205d55', 'Abréviation à clé du glossaire'),
]


# Rôles (alias sémantiques) : les règles de couleurs_premium.css ne lisent que ces noms ou les
# primitives ci-dessus ; un thème peut redéfinir n’importe lequel sur :root sans toucher aux règles.
ROLES = [
    ('--accent', 'var(--brand-600)', 'Accent du contexte : marque sur l’Accueil, teinte de spécialité dans un fragment (filets, pastilles, soulignés)'),
    ('--accent-ink', 'var(--brand-700)', 'Texte et icônes en accent (≥ 4,5:1)'),
    ('--accent-tint', 'var(--brand-50)', 'Fond teinté de l’accent (sélection légère, survol)'),
    ('--accent-sel', 'var(--brand-100)', 'Fond de l’élément sélectionné ou courant'),
    ('--focus-ring', 'var(--accent-ink)', 'Anneau de focus clavier (2 px, ≥ 3:1)'),
    ('--on-accent', 'var(--n-surface)', 'Texte sur un aplat d’encre d’accent'),
    ('--shadow-color', 'var(--n-shadow)', 'Couleur des ombres : surface assombrie, même teinte que le papier'),
    ('--shadow-0', '0 1px 2px color-mix(in srgb,var(--shadow-color) 10%,transparent)', 'Ombre de contact (boutons pleins, barres)'),
    ('--shadow-1', 'inset 0 1px 0 var(--n-surface),0 1px 2px color-mix(in srgb,var(--shadow-color) 5%,transparent),0 8px 22px -16px color-mix(in srgb,var(--shadow-color) 26%,transparent)', 'Relief de repos des cartes (lumière d’en haut : liseré clair, ombre portée vers le bas)'),
    ('--shadow-2', 'inset 0 1px 0 var(--n-surface),0 2px 5px color-mix(in srgb,var(--shadow-color) 7%,transparent),0 14px 30px -18px color-mix(in srgb,var(--shadow-color) 32%,transparent)', 'Relief au survol'),
    ('--shadow-bar', '0 6px 16px -14px color-mix(in srgb,var(--shadow-color) 28%,transparent)', 'Barre supérieure collante'),
    ('--shadow-float', '0 2px 6px color-mix(in srgb,var(--shadow-color) 8%,transparent),0 10px 26px -18px color-mix(in srgb,var(--shadow-color) 40%,transparent)', 'Boutons flottants (Navigo, pagination du Livre)'),
    ('--shadow-pop', '0 2px 6px color-mix(in srgb,var(--shadow-color) 6%,transparent),0 22px 44px -26px color-mix(in srgb,var(--shadow-color) 40%,transparent)', 'Fenêtres, Navigo, panneaux flottants'),
    ('--backdrop', 'var(--n-veil)', 'Voile derrière une fenêtre explicative'),
    ('--gauge-track', 'var(--brand-50)', 'Piste des jauges'),
    ('--gauge-edge', 'var(--n-line-strong)', 'Contour de la piste (≥ 3:1)'),
    ('--gauge-fill', 'var(--gauge-600)', 'Remplissage des jauges'),
    ('--gauge-fill-top', 'var(--gauge-500)', 'Haut du dégradé de remplissage (relief)'),
    ('--star-edge', 'var(--gold-700)', 'Contour de l’étoile d’or (≥ 3:1)'),
    ('--star-fill', 'var(--gold-500)', 'Corps de l’étoile d’or'),
    ('--star-light', 'var(--gold-300)', 'Facette éclairée de l’étoile'),
    ('--star-shade', 'var(--gold-600)', 'Facette ombrée de l’étoile'),
]


def pas(L, C, h):
    return oklch_hex(L, C, h)[0]


def hsl_hex(h, s, l):
    import colorsys
    r, g, b = colorsys.hls_to_rgb(h / 360, l, s)
    return '#%02x%02x%02x' % tuple(round(c * 255) for c in (r, g, b))


def debordement():
    """Rangs 24 à 40 : teinte d’angle d’or d’atlas_v2.js (hsl(i×137,508° 72 % 27 %)) ramenée en OKLCH
    sur les paliers des emplacements. Hors validateur : au-delà de 23 teintes, aucune séquence ne peut passer."""
    import validate_palette as vp
    out = []
    for i in range(len(EMPLACEMENTS), DERNIER_RANG):
        src = 'hsl(%d 72%% 27%%)' % round((i * 137.508) % 360)
        r, g, b = vp.lin(hsl_hex(round((i * 137.508) % 360), 0.72, 0.27))
        _, a, bb = vp.lin2oklab(r, g, b)
        h = round(math.degrees(math.atan2(bb, a)) % 360, 1)
        L = (BANDE_REPERES[0], sum(BANDE_REPERES) / 2, BANDE_REPERES[1])[i % 3]   # même bande que les emplacements
        out.append((f'debord-{i + 1}', L, math.floor(min(0.11, chroma_max(L, h, 0.11)) * 1000) / 1000, h, src))
    return out


def emplacements():
    out = []
    for nom, L, C, h, *_ in EMPLACEMENTS + debordement():
        C = min(C, math.floor(chroma_max(L, h, C) * 1000) / 1000)   # reste dans le gamut sRGB
        # Fonds et sélections suivent à 1/10 la luminosité du repère (± 0,003) : deux teintes voisines
        # de luminosités différentes gardent des fonds distincts, sans rompre l’égalité perçue.
        suivi = round((L - sum(BANDE_REPERES) / 2) * 0.1, 4)
        x, ok = oklch_hex(L, C, h)
        ci = min(C, chroma_max(ENCRE_L, h, C), ENCRE_C_BLEU if BLEUS[0] <= h <= BLEUS[1] else 1)
        out.append({'nom': nom, 'L': L, 'C': C, 'h': h, 'hex': x, 'gamut': ok, 'encre_C': round(ci, 3),
                    'encre': pas(ENCRE_L, ci, h), 'claire': pas(TEINTE_CLAIRE[0] + suivi + (0.004 if nom.startswith('debord') else 0), TEINTE_CLAIRE[1] + 0.003, h),
                    'selection': pas(TEINTE_SELECTION[0] + suivi + (0.004 if nom.startswith('debord') else 0), TEINTE_SELECTION[1], h)})
    return out


def tokens():
    t = []
    for nom, L, C, h, role in NEUTRES:
        t.append((nom, pas(L, C, h), f'oklch({L:.3f} {C:.3f} {h})', role))
    t.append(('--n-shadow', pas(*OMBRE), 'oklch(%.3f %.3f %d)' % OMBRE, 'Couleur des ombres (papier assombri)'))
    r, g, b = (int(pas(*VOILE[:3])[i:i + 2], 16) for i in (1, 3, 5))
    t.append(('--n-veil', f'rgb({r} {g} {b} / {VOILE[3]})', 'oklch(%.3f %.3f %d / %.2f)' % VOILE, 'Voile des fenêtres (papier assombri, 55 %)'))
    for p, L, C in MARQUE:
        x = ANCRE if L is None else pas(L, C, MARQUE_H)
        t.append((f'--brand-{p}', x, 'ancre #1f3428' if L is None else f'oklch({L:.3f} {C:.3f} {MARQUE_H})', 'Rampe de la marque'))
    for i, e in enumerate(emplacements(), 1):
        t.append((f'--cat-{i:02d}', e['hex'], f"oklch({e['L']:.3f} {e['C']:.3f} {e['h']})",
                  f"Emplacement {i} ({e['nom']})" if i <= len(EMPLACEMENTS) else f'Rang {i} (débordement, hors validateur)'))
        t.append((f'--cat-{i:02d}-ink', e['encre'], f"L {ENCRE_L}", 'Encre (texte) de la teinte'))
        t.append((f'--cat-{i:02d}-tint', e['claire'], f"L {TEINTE_CLAIRE[0]}", 'Fond teinté'))
        t.append((f'--cat-{i:02d}-sel', e['selection'], f"L {TEINTE_SELECTION[0]}", 'Fond sélectionné'))
    for nom, encre, fond, lib, forme in STATUTS:
        t.append((f'--status-{nom}', pas(*encre), 'oklch(%.3f %.3f %d)' % encre, f'Statut « {lib} » ({forme})'))
        t.append((f'--status-{nom}-bg', pas(*fond), 'oklch(%.3f %.3f %d)' % fond, 'Fond du statut'))
    for p, L, C in JAUGE:
        t.append((f'--gauge-{p}', pas(L, C, MARQUE_H), f'oklch({L:.3f} {C:.3f} {MARQUE_H})', 'Rampe séquentielle des jauges'))
    for p, L, C, h in OR:
        t.append((f'--gold-{p}', pas(L, C, h), f'oklch({L:.3f} {C:.3f} {h})', 'Étoile d’or, Pareto'))
    for nom, x, role in LECON:
        t.append((nom, x, 'valeur conservée', role))
    return t


def bloc_css():
    lignes = ['/* <tokens> — généré par docs/frontend/couleurs/palette.py --ecrire ; ne pas éditer à la main. */', ':root{']
    for nom, x, src, role in tokens():
        lignes.append(f' {nom}:{x};')
    e = {v['nom']: i for i, v in enumerate(emplacements(), 1)}
    for sid, nom in sorted(SPECIALITES.items()):
        k = sid.lower()
        i = e[nom]
        lignes.append(f' --sp-{k}:var(--cat-{i:02d});--sp-{k}-ink:var(--cat-{i:02d}-ink);--sp-{k}-tint:var(--cat-{i:02d}-tint);--sp-{k}-sel:var(--cat-{i:02d}-sel);')
    for nom, val, role in ROLES:
        lignes.append(f' {nom}:{val};')
    lignes.append('}')
    lignes.append('/* </tokens> */')
    return '\n'.join(lignes)


def bloc_specialites():
    lignes = ['/* <specialites> — généré : la teinte de spécialité devient l’accent du fragment. */']
    for sid in sorted(SPECIALITES):
        k = sid.lower()
        lignes.append(f'html[data-medina-fragment="{sid}"]{{--accent:var(--sp-{k});--accent-ink:var(--sp-{k}-ink);--accent-tint:var(--sp-{k}-tint);--accent-sel:var(--sp-{k}-sel)}}')
    lignes.append('/* </specialites> */')
    return '\n'.join(lignes)


def bloc_categories():
    """Remappe les couleurs posées en style en ligne par engine/atlas_v2.js (rang → même emplacement)."""
    lignes = ['/* <categories> — généré : couleur du rang n (atlas_v2.js) → emplacement n. Rangs 1 à 23 : séquence validée ;',
              '   rangs 24 à 40 : teinte d’angle d’or d’atlas_v2.js ramenée en OKLCH sur les mêmes paliers (débordement). */']
    sources = list(ATLAS_V2) + ['hsl(%d 72%% 27%%)' % round((i * 137.508) % 360) for i in range(len(ATLAS_V2), DERNIER_RANG)]
    for i, src in enumerate(sources, 1):
        n = f'{i:02d}'
        lignes.append(f'[style*="--cat: {src}" i]{{--cat:var(--cat-{n})!important;--cat-tint:var(--cat-{n}-tint)!important;--cat-ink:var(--cat-{n}-ink);--cat-sel:var(--cat-{n}-sel);'
                      f'--mp-cat:var(--cat-{n})!important;--mp-cat-ink:var(--cat-{n}-ink)!important;--mp-cat-tint:var(--cat-{n}-tint)!important}}')
    lignes.append('/* </categories> */')
    return '\n'.join(lignes)


def ecrire():
    s = CSS.read_text(encoding='utf-8')
    neuf = re.sub(r'/\* <tokens>.*?/\* </tokens> \*/', lambda _: bloc_css(), s, count=1, flags=re.S)
    neuf = re.sub(r'/\* <specialites>.*?/\* </specialites> \*/', lambda _: bloc_specialites(), neuf, count=1, flags=re.S)
    neuf = re.sub(r'/\* <categories>.*?/\* </categories> \*/', lambda _: bloc_categories(), neuf, count=1, flags=re.S)
    if neuf == s and '<tokens>' not in s:
        raise SystemExit('marqueurs <tokens> absents de ' + str(CSS))
    CSS.write_text(neuf, encoding='utf-8')
    print('tokens écrits dans', CSS)


def ecrire_doc(vp):
    """Tableaux de PALETTE.md (entre <!-- <tokens-doc> --> et <!-- </tokens-doc> -->) : valeurs L/C/h mesurées."""
    def lch(x):
        r, g, b = vp.lin(x)
        L, a, bb = vp.lin2oklab(r, g, b)
        C = math.hypot(a, bb)
        h = math.degrees(math.atan2(bb, a)) % 360 if C > 0.0015 else None
        return f'{L:.3f} / {C:.3f} / ' + ('—' if h is None else f'{h:.1f}')
    T = {n: (x, src, role) for n, x, src, role in tokens()}
    sp = {v: k for k, v in SPECIALITES.items()}
    try:   # libellé complet du fragment (organisation/fragments.json), par exemple N-05-Neurologie
        lib = {f['id']: f['label'] for f in json.loads((ROOT / 'organisation/fragments.json').read_text(encoding='utf-8'))}
    except (OSError, ValueError, KeyError):
        lib = {}
    out = ['<!-- <tokens-doc> — généré par palette.py --doc ; ne pas éditer à la main. -->', '',
           '### Neutres, marque, statuts, jauges, or, leçon', '',
           'L / C / h : valeurs OKLCH mesurées sur l’hexadécimal arrondi. TCP : température de couleur proximale (CIE 1960, locus de Planck), Duv > 0 vers le vert.', '',
           '| Token | Valeur | L / C / h (OKLCH) | TCP · Duv | Rôle |', '|---|---|---|---|---|']
    for n, (x, src, role) in T.items():
        if n.startswith('--cat-'):
            continue
        if x.startswith('#'):
            k, duv = tcp(x) if n.startswith(('--n-', '--ink-')) else (None, None)
            out.append(f'| `{n}` | `{x}` | {lch(x)} | ' + (f'{k} K · {duv:+.4f}' if k else '') + f' | {role} |')
        else:
            out.append(f'| `{n}` | `{x}` | {src} |  | {role} |')
    out += ['', '### Rôles (alias)', '', '| Token | Valeur | Rôle |', '|---|---|---|']
    for nom, val, role in ROLES:
        out.append(f'| `{nom}` | `{val}` | {role} |')
    out += ['', '### Emplacements catégoriels (ordre fixe) et spécialités', '',
            'Chaque emplacement `--cat-NN` a ses variantes `--cat-NN-ink` (texte), `--cat-NN-tint` (fond) et `--cat-NN-sel` (sélection). '
            'Chaque spécialité a `--sp-<id>`, `--sp-<id>-ink`, `--sp-<id>-tint`, `--sp-<id>-sel` (alias de son emplacement). '
            f'Repères : L {BANDE_REPERES[0]}–{BANDE_REPERES[1]} ; encres : L {ENCRE_L} ; fonds : L {TEINTE_CLAIRE[0]} ; sélections : L {TEINTE_SELECTION[0]}.', '',
            '| N° | Nom | Repère | L / C / h | Encre | L / C / h encre | Fond | Repère / papier | Encre / fond | Spécialité |',
            '|---|---|---|---|---|---|---|---|---|---|']
    for i, e in enumerate(emplacements(), 1):
        s = sp.get(e['nom'])
        out.append(f"| {i} | {e['nom']} | `{e['hex']}` | {lch(e['hex'])} | `{e['encre']}` | {lch(e['encre'])} | `{e['claire']}` | "
                   f"{vp.contrast(e['hex'], PAPIER):.2f}:1 | {vp.contrast(e['encre'], e['claire']):.2f}:1 | "
                   + (f'`--sp-{s.lower()}` {lib.get(s, s)}' if s else ('débordement' if i > len(EMPLACEMENTS) else '')) + ' |')
    out += ['', '<!-- </tokens-doc> -->']
    s = DOC.read_text(encoding='utf-8')
    neuf = re.sub(r'<!-- <tokens-doc>.*?<!-- </tokens-doc> -->', lambda _: '\n'.join(out), s, count=1, flags=re.S)
    if neuf == s and '<tokens-doc>' not in s:
        raise SystemExit('marqueurs <tokens-doc> absents de ' + str(DOC))
    DOC.write_text(neuf, encoding='utf-8')
    print('tableaux écrits dans', DOC)


def controles(vp):
    """Contrastes (WCAG) des rôles de texte et de contour sur leurs fonds réels."""
    T = {n: x for n, x, _, _ in tokens()}
    fonds = {'surface': T['--n-surface'], 'papier': T['--n-paper'], 'encart': T['--n-sunken']}
    res = []
    for role in ('--ink-1', '--ink-2', '--ink-3'):
        for f, x in fonds.items():
            res.append((role, f, vp.contrast(T[role], x), 4.5))
    for f, x in fonds.items():
        res.append(('--n-line-strong', f, vp.contrast(T['--n-line-strong'], x), 3.0))
    for i, e in enumerate(emplacements(), 1):
        res.append((f'--cat-{i:02d}-ink', 'teinte claire', vp.contrast(e['encre'], e['claire']), 4.5))
        res.append((f'--cat-{i:02d}-ink', 'teinte sélection', vp.contrast(e['encre'], e['selection']), 4.5))
        res.append((f'--cat-{i:02d}', 'papier', vp.contrast(e['hex'], PAPIER), 3.0))
    for nom, *_ in STATUTS:
        res.append((f'--status-{nom}', 'fond du statut', vp.contrast(T[f'--status-{nom}'], T[f'--status-{nom}-bg']), 4.5))
        res.append((f'--status-{nom}', 'surface', vp.contrast(T[f'--status-{nom}'], T['--n-surface']), 4.5))
    res.append(('--gauge-600', '--brand-100 (piste)', vp.contrast(T['--gauge-600'], T['--brand-100']), 3.0))
    res.append(('--gold-700', 'surface (contour étoile)', vp.contrast(T['--gold-700'], T['--n-surface']), 3.0))
    res.append(('--gold-800', '--gold-100 (Pareto)', vp.contrast(T['--gold-800'], T['--gold-100']), 4.5))
    res.append(('--brand-600', 'surface (liens, focus)', vp.contrast(T['--brand-600'], T['--n-surface']), 4.5))
    for nom, x, _ in LECON:
        res.append((nom, 'surface', vp.contrast(x, T['--n-surface']), 4.5))
    return res


# ------------------------------------------------------------------ vision photopique diurne
def xyz(x):
    """sRGB (D65) → XYZ, Y = luminance photopique CIE (la luminance relative de WCAG)."""
    r, g, b = (int(x[i:i + 2], 16) / 255 for i in (1, 3, 5))
    r, g, b = ((c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4) for c in (r, g, b))
    return (0.4124564 * r + 0.3575761 * g + 0.1804375 * b, 0.2126729 * r + 0.7151522 * g + 0.0721750 * b,
            0.0193339 * r + 0.1191920 * g + 0.9503041 * b)


def planck_uv(T):
    """Locus de Planck dans l’espace CIE 1960 (u, v), approximation de Krystek (1985), 1 000–15 000 K."""
    u = (0.860117757 + 1.54118254e-4 * T + 1.28641212e-7 * T * T) / (1 + 8.42420235e-4 * T + 7.08145163e-7 * T * T)
    v = (0.317398726 + 4.22806245e-5 * T + 4.20481691e-8 * T * T) / (1 - 2.89741816e-5 * T + 1.61456053e-7 * T * T)
    return u, v


def tcp(x):
    """Température de couleur proximale (K) et Duv (> 0 : vers le vert, < 0 : vers le magenta).
    Repères : D65 (blanc sRGB) = 6 504 K, Duv +0,0032 ; une lumière du jour plus chaude descend vers 5 500 K."""
    X, Y, Z = xyz(x)
    d = X + 15 * Y + 3 * Z
    if d == 0:
        return None, None
    u, v = 4 * X / d, 6 * Y / d
    T = min(range(1500, 15001, 5), key=lambda T: (planck_uv(T)[0] - u) ** 2 + (planck_uv(T)[1] - v) ** 2)
    pu, pv = planck_uv(T)
    qu, qv = planck_uv(T + 5)
    signe = 1 if (qu - pu) * (v - pv) - (qv - pv) * (u - pu) < 0 else -1
    return T, signe * math.hypot(u - pu, v - pv)


def photopique(vp):
    """Contrôles de l’exigence « œil humain normal, de jour » : (libellé, valeur, réussite)."""
    T = {n: x for n, x, _, _ in tokens()}
    res = []
    for nom in SURFACES_PAPIER:
        L, C = vp.oklch(T[nom])
        k, duv = tcp(T[nom])
        res.append((f'{nom} chroma ≤ 0,012', f'C {C:.4f}', C <= 0.012))
        res.append((f'{nom} 5 500 K ≤ TCP ≤ 6 600 K, Duv 0 à +0,005 (lumière du jour, ni bleuté ni crème)',
                    f'{k} K, Duv {duv:+.4f}', 5500 <= k <= 6600 and 0 <= duv <= 0.005))
    for nom in [n for n, *_ in NEUTRES] + ['--status-prep', '--status-prep-bg']:
        L, C = vp.oklch(T[nom])
        k, duv = tcp(T[nom])
        res.append((f'{nom} neutre non bleuté (C ≤ 0,012, TCP ≤ 6 600 K)', f'C {C:.4f} · {k} K', C <= 0.012 and k <= 6600))
    k, duv = tcp(T['--n-shadow'])
    res.append(('--n-shadow ombre teintée du papier, non bleuâtre (TCP ≤ 6 600 K)', f'{k} K, Duv {duv:+.4f}', k <= 6600))
    em = emplacements()
    for titre, cle, n in (('repères (--cat-NN)', 'hex', len(EMPLACEMENTS)), ('encres (-ink)', 'encre', len(EMPLACEMENTS)),
                          ('fonds (-tint)', 'claire', len(EMPLACEMENTS)), ('sélections (-sel)', 'selection', len(EMPLACEMENTS))):
        Ls = [vp.oklch(e[cle])[0] for e in em[:n]]
        res.append((f'Luminosité égale des {titre} : écart ≤ 0,06 (± 0,03)', f'L {min(Ls):.3f}–{max(Ls):.3f}', max(Ls) - min(Ls) <= 0.0605))
    Ls = [vp.oklch(T[f'--status-{s}'])[0] for s, *_ in STATUTS]
    res.append(('Luminosité égale des statuts : écart ≤ 0,06', f'L {min(Ls):.3f}–{max(Ls):.3f}', max(Ls) - min(Ls) <= 0.0605))
    bleus = [vp.oklch(e['encre'])[1] for e in em if BLEUS[0] <= e['h'] <= BLEUS[1]]
    res.append((f'Encres bleues à violettes (teintes {BLEUS[0]}–{BLEUS[1]}) : C ≤ {ENCRE_C_BLEU}', f'C max {max(bleus):.3f}', max(bleus) <= ENCRE_C_BLEU + 0.003))
    texte = [vp.oklch(T[n])[1] for n in ('--ink-1', '--ink-2', '--ink-3')]
    res.append(('Texte courant (--ink-1/2/3) achromatique : C ≤ 0,012', f'C max {max(texte):.4f}', max(texte) <= 0.012))
    em_all = emplacements()
    for cle, titre in (('hex', 'repères'), ('claire', 'fonds teintés'), ('selection', 'sélections'), ('encre', 'encres')):
        vals = [e[cle] for e in em_all]
        res.append((f'{len(vals)} {titre} distincts (rangs 1 à {len(vals)}, une couleur par catégorie)', f'{len(set(vals))} valeurs', len(set(vals)) == len(vals)))
    import itertools
    allp = min(vp.deltaE(a, b) for a, b in itertools.combinations([e['hex'] for e in em_all[:len(EMPLACEMENTS)]], 2))
    res.append(('Écart minimal toutes paires des 23 repères (vision normale, ΔE OKLab ×100) ≥ 3,5', f'{allp:.2f}', allp >= 3.5))
    plafond = max((vp.oklch(x)[1], n) for n, x, src, _ in tokens() if x.startswith('#') and src != 'valeur conservée')
    res.append((f'Aucune couleur « néon » : C ≤ {CHROMA_PLAFOND} (hors valeurs conservées des cours)', f'C max {plafond[0]:.3f} ({plafond[1]})', plafond[0] <= CHROMA_PLAFOND + 0.003))
    return res


def sequences(ordre_portail):
    e = {v['nom']: v for v in emplacements()}
    cat = [v['hex'] for v in emplacements()[:len(EMPLACEMENTS)]]
    portail = [e[SPECIALITES[s]]['hex'] for s in ordre_portail.split(',')]
    registre = [e[SPECIALITES[s]]['hex'] for s in ORDRE_REGISTRE.split(',')]
    # Contractuelles : séquences de lecture où les repères se touchent (barre latérale, rangées).
    seqs = [('Catégories (rang 1 à 23, barre latérale et rangées de grille)', cat, True),
            ('Accueil (ordre d’affichage des 23 spécialités)', portail, True)]
    for k in (3, 4):
        for d in range(k):
            seqs.append((f'Catégories, colonne {d + 1} sur {k} (voisins verticaux de la grille)', cat[d::k], True))
    # Informatives : cartes séparées par une gouttière et toujours nommées (encodage secondaire).
    seqs.append(('Registre (ordre de production, informatif)', registre, False))
    for k in (2, 3):
        for d in range(k):
            seqs.append((f'Accueil, colonne {d + 1} sur {k} (informatif : gouttière de 18 px et nom)', portail[d::k], False))
    return seqs


def valider(validateur, ordre_portail, sortie=None):
    js = Path(validateur) / 'validate_palette.js'
    rapport, ok_global = [], True
    for titre, seq, contrat in sequences(ordre_portail):
        r = subprocess.run(['node', str(js), ','.join(seq), '--mode', 'light', '--surface', PAPIER],
                           capture_output=True, text=True)
        if contrat:
            ok_global &= r.returncode == 0
        rapport.append(f'## {titre}\n$ node validate_palette.js "{",".join(seq)}" --mode light --surface "{PAPIER}"\n{r.stdout.strip()}\n')
    jauge = [pas(L, C, MARQUE_H) for _, L, C in JAUGE]
    r = subprocess.run(['node', str(js), ','.join(jauge), '--ordinal', '--mode', 'light', '--surface', PAPIER], capture_output=True, text=True)
    ok_global &= r.returncode == 0
    rapport.append(f'## Jauges (rampe séquentielle à une teinte, --ordinal)\n$ node validate_palette.js "{",".join(jauge)}" --ordinal --mode light --surface "{PAPIER}"\n{r.stdout.strip()}\n')
    texte = '\n'.join(rapport)
    print(texte)
    if sortie:
        Path(sortie).write_text(texte + '\n', encoding='utf-8')
    return ok_global


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--validateur', default=os.environ.get('MEDINA_VALIDATEUR', DEFAUT_VALIDATEUR))
    ap.add_argument('--ecrire', action='store_true')
    ap.add_argument('--doc', action='store_true', help='réécrit les tableaux générés de PALETTE.md')
    ap.add_argument('--valider', action='store_true')
    ap.add_argument('--rapport', help='fichier où écrire la sortie du validateur')
    ap.add_argument('--ordre-portail', default=ORDRE_PORTAIL)
    ap.add_argument('--json')
    a = ap.parse_args()
    sys.path.insert(0, a.validateur)
    import validate_palette as vp
    if a.ecrire:
        ecrire()
    for nom, x, src, role in tokens():
        if not nom.startswith('--cat-') or nom.count('-') == 3:
            print(f'{nom:20s} {x}  {src:26s} {role}')
    echecs = 0
    print('\nContrastes WCAG')
    for role, fond, r, seuil in controles(vp):
        ok = r >= seuil
        echecs += not ok
        if not ok or not role.startswith('--cat-'):
            print(f'  {"ok " if ok else "ÉCHEC"} {role:18s} sur {fond:26s} {r:5.2f}:1 (seuil {seuil})')
    print(f'  {echecs} échec(s) de contraste ;', sum(1 for e in emplacements() if not e['gamut']), 'teinte(s) hors gamut sRGB')
    print('\nVision photopique diurne (D65, luminosité perçue, chroma modérée)')
    for libelle, valeur, ok in photopique(vp):
        echecs += not ok
        print(f'  {"ok " if ok else "ÉCHEC"} {libelle} : {valeur}')
    if a.doc:
        ecrire_doc(vp)
    if a.json:
        Path(a.json).write_text(json.dumps({'tokens': tokens(), 'emplacements': emplacements(), 'specialites': SPECIALITES}, ensure_ascii=False, indent=1))
    if a.valider:
        if not valider(a.validateur, a.ordre_portail, a.rapport):
            echecs += 1
    sys.exit(1 if echecs else 0)


if __name__ == '__main__':
    main()
