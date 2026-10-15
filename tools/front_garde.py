#!/usr/bin/env python3
"""front_garde — contrôle qualité automatique du frontend MEDINA construit.

Usage :
    python3 tools/front_garde.py --out <dossier construit> [--json rapport.json]

Le dossier construit est celui de ``build_front.py`` (variable MEDINA_OUT),
complété au besoin par ``build_index.py`` (portail ``index.html``). L'outil
sert ce dossier en HTTP local, ouvre Chromium (déjà installé : il n'appelle
jamais ``playwright install``) et contrôle l'Accueil, une page de fragment,
une Leçon et Navigo, à 390 et 1280 px de largeur.

Contrôles (seuils documentés dans docs/frontend/outils/README.md) :
  police      police calculée = Atkinson Hyperlegible Next (CSS et police rendue)
  erreurs     aucune erreur JavaScript ni ressource HTTP >= 400
  debordement aucun défilement horizontal à 390 px
  contraste   texte/fond >= 4,5:1 (calcul WCAG 2.x) sur un échantillon visible
  saturation  aucune grande surface de couleur saturée éblouissante (HSL)
  cartes      rapport max/min de hauteur et de largeur des cartes <= 1,2
  transitions durée + délai <= 300 ms ; prefers-reduced-motion respecté
  focus       indicateur de focus visible au clavier sur liens et boutons
  axe         axe-core (facultatif, informatif sauf --axe-strict)

Code retour : 0 si tout passe, 1 si un contrôle échoue, 2 si l'outil ne peut
pas s'exécuter (dossier, navigateur ou page introuvable).
"""
from __future__ import annotations

import argparse
import functools
import glob
import http.server
import json
import os
import re
import sys
import threading
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# --------------------------------------------------------------------------
# Seuils
# --------------------------------------------------------------------------
POLICE_ATTENDUE = "atkinson hyperlegible next"
CONTRASTE_MIN = 4.5
CONTRASTE_GRAND_TEXTE = 3.0          # seulement avec --grand-texte-wcag
SATURATION_MIN = 0.80                # HSL S >= 80 %
LUMINOSITE_PLAGE = (0.30, 0.70)      # HSL L entre 30 % et 70 %
SURFACE_EBLOUISSANTE_PX2 = 4000      # ≈ 63 × 63 px pour un même élément
RATIO_CARTES_MAX = 1.2
TRANSITION_MAX_MS = 300.0
REDUIT_MAX_MS = 20.0                 # sous prefers-reduced-motion: reduce
LARGEURS = (390, 1280)
AXE_VERSION = "4.13.0"
AXE_CACHE = Path(os.environ.get("XDG_CACHE_HOME", Path.home() / ".cache")) / "medina-front-garde" / f"axe-core-{AXE_VERSION}"

CARTES_SELECTEUR = ".specialty-card, .mcg-category-card"
LECON_SELECTEUR = "[data-mcg-lesson] a[href^='#/entry/'], a[data-fragment-chapter], a[href^='#/entry/']"


# --------------------------------------------------------------------------
# Fonctions de calcul (pures, testées par tests/test_front_garde.py)
# --------------------------------------------------------------------------
def _canal_lineaire(c: float) -> float:
    c = c / 255.0
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def luminance_relative(rgb) -> float:
    """Luminance relative WCAG 2.x d'une couleur sRGB (0-255)."""
    r, g, b = (_canal_lineaire(float(x)) for x in rgb[:3])
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def rapport_contraste(c1, c2) -> float:
    """Rapport de contraste WCAG (L1 + 0,05) / (L2 + 0,05), entre 1 et 21."""
    l1, l2 = luminance_relative(c1), luminance_relative(c2)
    hi, lo = max(l1, l2), min(l1, l2)
    return (hi + 0.05) / (lo + 0.05)


def composer(dessus, dessous):
    """Compose une couleur RGBA (alpha 0-1) sur une couleur opaque."""
    a = float(dessus[3]) if len(dessus) > 3 else 1.0
    return tuple(a * float(dessus[i]) + (1 - a) * float(dessous[i]) for i in range(3))


def fond_effectif(couches, base=(255, 255, 255)):
    """Compose des couches de fond données de la plus profonde à la plus haute."""
    fond = tuple(float(x) for x in base[:3])
    for couche in couches:
        fond = composer(couche, fond)
    return fond


def fonds_possibles(couches, base=(255, 255, 255), limite=24):
    """Fonds possibles sous un texte : couches {couleur} ou {degrade: [arrêts]}, de la plus profonde à la plus haute.

    Chaque arrêt d'un dégradé est composé sur les fonds déjà calculés ; le texte est
    ensuite mesuré contre le pire d'entre eux (approche conservatrice).
    """
    fonds = [tuple(float(x) for x in base[:3])]
    for couche in couches:
        if "degrade" in couche:
            fonds = [composer(arret, f) for f in fonds for arret in couche["degrade"]][:limite]
        else:
            fonds = [composer(couche["couleur"], f) for f in fonds]
    return fonds


def rgb_vers_hsl(rgb):
    """Convertit sRGB (0-255) en HSL (teinte en degrés, S et L entre 0 et 1)."""
    r, g, b = (float(x) / 255.0 for x in rgb[:3])
    mx, mn = max(r, g, b), min(r, g, b)
    l = (mx + mn) / 2
    if mx == mn:
        return 0.0, 0.0, l
    d = mx - mn
    s = d / (2 - mx - mn) if l > 0.5 else d / (mx + mn)
    if mx == r:
        h = ((g - b) / d) % 6
    elif mx == g:
        h = (b - r) / d + 2
    else:
        h = (r - g) / d + 4
    return h * 60.0, s, l


def couleur_eblouissante(rgb, saturation_min=SATURATION_MIN, plage=LUMINOSITE_PLAGE) -> bool:
    """Vrai si la couleur est saturée et de luminosité moyenne (vive, éblouissante)."""
    _, s, l = rgb_vers_hsl(rgb)
    return s >= saturation_min and plage[0] <= l <= plage[1]


def rapport_max_min(valeurs):
    """Rapport max/min de dimensions strictement positives ; None si < 2 valeurs."""
    v = [float(x) for x in valeurs if x and float(x) > 0]
    if len(v) < 2:
        return None
    return max(v) / min(v)


def durees_css_ms(texte: str):
    """Analyse une liste CSS de durées (« 0.3s, 200ms ») en millisecondes."""
    out = []
    for morceau in (texte or "").split(","):
        m = morceau.strip()
        if not m:
            continue
        if m.endswith("ms"):
            out.append(float(m[:-2]))
        elif m.endswith("s"):
            out.append(float(m[:-1]) * 1000.0)
        else:
            out.append(float(m) * 1000.0)
    return out


def totaux_transitions_ms(durees: str, delais: str):
    """Durée + délai de chaque transition, avec la répétition cyclique CSS des listes."""
    d, r = durees_css_ms(durees), durees_css_ms(delais) or [0.0]
    if not d:
        return []
    return [d[i] + r[i % len(r)] for i in range(len(d))]


def police_principale(famille: str) -> str:
    """Première famille d'une valeur font-family, sans guillemets, en minuscules."""
    premier = (famille or "").split(",")[0].strip().strip("'\"")
    return premier.lower()


def est_monospace(famille: str) -> bool:
    """Les codes CIM en chasse fixe sont une exception typographique voulue."""
    return police_principale(famille) in {"ui-monospace", "monospace", "menlo", "consolas", "courier new", "sfmono-regular"}


def indicateur_focus_visible(avant: dict, apres: dict) -> bool:
    """Vrai si l'état focalisé expose un contour, une ombre ou un changement visible."""
    largeur = apres.get("outlineWidth", "0px")
    try:
        largeur_px = float(re.sub(r"[^0-9.]", "", largeur) or 0)
    except ValueError:
        largeur_px = 0.0
    alpha = float((apres.get("outlineRgba") or [0, 0, 0, 0])[3])
    if apres.get("outlineStyle", "none") != "none" and largeur_px >= 1 and alpha > 0:
        return True
    for cle in ("boxShadow", "backgroundColor", "borderColor", "textDecorationLine", "color"):
        if avant.get(cle) != apres.get(cle):
            return True
    return False


# --------------------------------------------------------------------------
# Scripts exécutés dans la page
# --------------------------------------------------------------------------
JS_COMMUN = r"""
window.__fg = window.__fg || (() => {
  const cv = document.createElement('canvas'); cv.width = cv.height = 1;
  const cx = cv.getContext('2d', {willReadFrequently: true});
  const rgba = (c) => { // toute couleur CSS -> [r,g,b,a]
    if (!c || c === 'transparent') return [0,0,0,0];
    cx.clearRect(0,0,1,1); cx.fillStyle = '#000'; cx.fillStyle = c; cx.fillRect(0,0,1,1);
    const d = cx.getImageData(0,0,1,1).data; const a = d[3]/255;
    return a ? [d[0]/a, d[1]/a, d[2]/a, a].map((x,i)=> i<3 ? Math.min(255, Math.round(x)) : x) : [0,0,0,0];
  };
  const visible = (el) => {
    const r = el.getBoundingClientRect(); if (r.width < 2 || r.height < 2) return false;
    for (let e = el; e && e.nodeType === 1; e = e.parentElement) {
      const cs = getComputedStyle(e);
      if (cs.display === 'none' || cs.visibility === 'hidden' || +cs.opacity < 0.1) return false;
      if (e.hidden || e.closest('[hidden]')) return false;
    }
    return true;
  };
  const chemin = (el) => {
    const p = []; for (let e = el; e && e.nodeType === 1 && p.length < 4; e = e.parentElement) {
      let s = e.tagName.toLowerCase(); if (e.id) { s += '#' + e.id; p.unshift(s); break; }
      const c = [...e.classList].slice(0,2).join('.'); if (c) s += '.' + c; p.unshift(s);
    } return p.join(' > ');
  };
  const stops = (img) => (img.match(/(rgba?|hsla?|oklch|oklab|lab|lch|color)\([^()]*\)|#[0-9a-f]{3,8}\b/gi) || []).map(rgba);
  return {rgba, visible, chemin, stops};
})();
"""

JS_POLICE = r"""
(scope) => {
  document.querySelectorAll('[data-fg-police]').forEach(e => e.removeAttribute('data-fg-police'));
  const root = document.querySelector(scope) || document.body;
  const out = {body: getComputedStyle(document.body).fontFamily, scope: getComputedStyle(root).fontFamily,
               charge: document.fonts.check('16px "Atkinson Hyperlegible Next"'), echantillon: []};
  const els = [...root.querySelectorAll('p, li, h1, h2, h3, a, button, span, td, summary')]
    .filter(e => [...e.childNodes].some(n => n.nodeType === 3 && n.textContent.trim().length > 2) && __fg.visible(e));
  const pas = Math.max(1, Math.floor(els.length / 40));
  els.filter((_, i) => i % pas === 0).slice(0, 40).forEach((e, i) => {
    e.setAttribute('data-fg-police', String(i));
    out.echantillon.push({chemin: __fg.chemin(e), famille: getComputedStyle(e).fontFamily});
  });
  return out;
}
"""

JS_CONTRASTE = r"""
([scope, n]) => {
  const root = document.querySelector(scope) || document.body;
  const els = [...root.querySelectorAll('*')].filter(e =>
    !['SCRIPT','STYLE','TEMPLATE','NOSCRIPT','SVG','PATH','OPTION'].includes(e.tagName.toUpperCase()) &&
    [...e.childNodes].some(t => t.nodeType === 3 && t.textContent.trim().length > 1) && __fg.visible(e));
  const pas = Math.max(1, Math.floor(els.length / n));
  return els.filter((_, i) => i % pas === 0).slice(0, n).map(e => {
    const cs = getComputedStyle(e); const couches = []; let indetermine = false;
    let op = 1;
    for (let a = e; a && a.nodeType === 1; a = a.parentElement) {
      const s = getComputedStyle(a); op *= +s.opacity;
      if (s.backgroundImage && s.backgroundImage !== 'none') {
        if (/url\(/.test(s.backgroundImage)) { indetermine = true; break; }
        const st = __fg.stops(s.backgroundImage).filter(c => c[3] > 0);
        if (st.length) couches.push({degrade: st});
      }
      const c = __fg.rgba(s.backgroundColor);
      if (c[3] > 0) { couches.push({couleur: c}); if (c[3] >= 1) break; }
    }
    couches.reverse(); // de la plus profonde à la plus haute
    const fg = __fg.rgba(cs.color); fg[3] *= op;
    return {chemin: __fg.chemin(e), texte: e.textContent.trim().slice(0, 50), couleur: fg, couches, indetermine,
            taille: parseFloat(cs.fontSize), graisse: parseInt(cs.fontWeight) || 400};
  });
}
"""

JS_SATURATION = r"""
(scope) => {
  const root = document.querySelector(scope) || document.body; const out = [];
  for (const e of [root, ...root.querySelectorAll('*')]) {
    const r = e.getBoundingClientRect(); const aire = r.width * r.height; if (aire < 400) continue;
    const cs = getComputedStyle(e); const cols = [];
    const c = __fg.rgba(cs.backgroundColor); if (c[3] >= 0.6) cols.push(c);
    if (cs.backgroundImage !== 'none' && !/url\(/.test(cs.backgroundImage)) __fg.stops(cs.backgroundImage).filter(x => x[3] >= 0.6).forEach(x => cols.push(x));
    if (cols.length && __fg.visible(e)) out.push({chemin: __fg.chemin(e), aire: Math.round(aire), couleurs: cols});
  }
  return out;
}
"""

JS_CARTES = r"""
(sel) => [...document.querySelectorAll(sel)].filter(__fg.visible).map(e => {
  const r = e.getBoundingClientRect(); return {chemin: __fg.chemin(e), largeur: r.width, hauteur: r.height};
})
"""

JS_MOUVEMENT = r"""
() => {
  const out = [];
  const pousse = (e, cs, pseudo) => {
    if (cs.transitionDuration && cs.transitionDuration !== '0s')
      out.push({chemin: __fg.chemin(e) + pseudo, type: 'transition', proprietes: cs.transitionProperty,
                durees: cs.transitionDuration, delais: cs.transitionDelay});
    if (cs.animationName && cs.animationName !== 'none')
      out.push({chemin: __fg.chemin(e) + pseudo, type: 'animation', nom: cs.animationName,
                durees: cs.animationDuration, delais: cs.animationDelay, iterations: cs.animationIterationCount});
  };
  for (const e of document.querySelectorAll('*')) {
    pousse(e, getComputedStyle(e), '');
    for (const p of ['::before', '::after']) { const cs = getComputedStyle(e, p); if (cs.content && cs.content !== 'none') pousse(e, cs, p); }
  }
  return {elements: out, scroll: getComputedStyle(document.documentElement).scrollBehavior};
}
"""

JS_DEBORDEMENT = r"""
() => {
  const vw = document.documentElement.clientWidth; const coupables = [];
  for (const e of document.body.querySelectorAll('*')) {
    const r = e.getBoundingClientRect(); if (r.width < 1 || r.right <= vw + 1) continue;
    const p = e.parentElement && e.parentElement.getBoundingClientRect();
    if (p && p.right > vw + 1) continue; // ne garder que le coupable le plus externe
    if (!__fg.visible(e)) continue;
    coupables.push({chemin: __fg.chemin(e), droite: Math.round(r.right), largeur: Math.round(r.width)});
    if (coupables.length >= 8) break;
  }
  return {scrollWidth: document.documentElement.scrollWidth, clientWidth: vw, coupables};
}
"""

JS_FOCUS_PREP = r"""
(scope) => {
  const root = document.querySelector(scope) || document.body; let i = 0;
  const etat = (e) => { const s = getComputedStyle(e); return {outlineStyle: s.outlineStyle, outlineWidth: s.outlineWidth,
    outlineRgba: __fg.rgba(s.outlineColor), boxShadow: s.boxShadow, backgroundColor: s.backgroundColor,
    borderColor: s.borderColor, textDecorationLine: s.textDecorationLine, color: s.color}; };
  window.__fgEtat = etat; window.__fgAvant = {};
  for (const e of root.querySelectorAll('a[href], button, [role="button"], summary')) {
    e.setAttribute('data-fg-focus', String(i)); window.__fgAvant[i] = etat(e); i++;
  }
  return i;
}
"""

JS_FOCUS_LIRE = r"""
() => {
  const e = document.activeElement; if (!e || e === document.body) return null;
  const id = e.getAttribute('data-fg-focus');
  return {id, tag: e.tagName.toLowerCase(), chemin: __fg.chemin(e), texte: (e.textContent || e.getAttribute('aria-label') || '').trim().slice(0, 40),
          avant: id === null ? null : window.__fgAvant[id], apres: window.__fgEtat(e),
          focusVisible: e.matches(':focus-visible')};
}
"""


# --------------------------------------------------------------------------
# Analyse (Python) des données collectées
# --------------------------------------------------------------------------
def analyser_contraste(echantillon, seuil=CONTRASTE_MIN, grand_texte_wcag=False):
    echecs, mesures, indetermines = [], 0, 0
    for e in echantillon:
        if e["indetermine"]:
            indetermines += 1
            continue
        fg = e["couleur"]
        if fg[3] <= 0.05:
            continue
        fonds = fonds_possibles(e["couches"])
        mesures_fonds = sorted((rapport_contraste(composer(fg, f), f), f) for f in fonds)
        pire, fond_pire = mesures_fonds[0]
        grand = e["taille"] >= 24 or (e["taille"] >= 18.66 and e["graisse"] >= 700)
        limite = CONTRASTE_GRAND_TEXTE if (grand_texte_wcag and grand) else seuil
        mesures += 1
        if pire < limite:
            echecs.append({"chemin": e["chemin"], "texte": e["texte"], "rapport": round(pire, 2), "seuil": limite,
                           "couleur": [round(x, 2) for x in fg], "fond": [round(x) for x in fond_pire]})
    return {"mesures": mesures, "indetermines": indetermines, "echecs": echecs}


def analyser_saturation(surfaces, aire_min=SURFACE_EBLOUISSANTE_PX2):
    echecs = []
    for s in surfaces:
        if s["aire"] < aire_min:
            continue
        for c in s["couleurs"]:
            if couleur_eblouissante(c):
                h, sat, l = rgb_vers_hsl(c)
                echecs.append({"chemin": s["chemin"], "aire": s["aire"], "rgb": [round(x) for x in c[:3]],
                               "hsl": [round(h), round(sat * 100), round(l * 100)]})
                break
    return echecs


def analyser_mouvement(donnees, reduit=False):
    limite = REDUIT_MAX_MS if reduit else TRANSITION_MAX_MS
    echecs, vus = [], set()
    for e in donnees["elements"]:
        if e["type"] == "transition":
            pire = max(totaux_transitions_ms(e["durees"], e["delais"]) or [0])
        else:
            if not reduit:
                continue  # les animations sont contrôlées sous prefers-reduced-motion
            pire = max(durees_css_ms(e["durees"]) or [0])
        if pire > limite:
            cle = (e["chemin"], e["type"])
            if cle in vus:
                continue
            vus.add(cle)
            echecs.append({"chemin": e["chemin"], "type": e["type"], "ms": round(pire, 1),
                           "detail": e.get("proprietes") or e.get("nom")})
    if reduit and donnees.get("scroll") == "smooth":
        echecs.append({"chemin": "html", "type": "scroll-behavior", "ms": None, "detail": "smooth"})
    return echecs


# --------------------------------------------------------------------------
# Exécution navigateur
# --------------------------------------------------------------------------
class _Serveur(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


def servir(dossier: Path):
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(_Serveur, directory=str(dossier)))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv, f"http://127.0.0.1:{srv.server_address[1]}/"


def candidats_chromium():
    racines = [os.environ.get("PLAYWRIGHT_BROWSERS_PATH"), "/opt/pw-browsers", str(Path.home() / ".cache/ms-playwright")]
    out = []
    for r in filter(None, racines):
        out += sorted(glob.glob(os.path.join(r, "chromium-*/chrome-linux*/chrome")), reverse=True)
        out += sorted(glob.glob(os.path.join(r, "chromium_headless_shell-*/chrome-*/*headless*shell")), reverse=True)
    return [p for p in out if os.access(p, os.X_OK)]


def lancer_chromium(pw, chemin=None):
    if chemin:
        return pw.chromium.launch(executable_path=chemin)
    try:
        return pw.chromium.launch()
    except Exception as erreur:  # version du module différente du navigateur installé
        for c in candidats_chromium():
            try:
                return pw.chromium.launch(executable_path=c)
            except Exception:
                continue
        raise RuntimeError("Chromium introuvable (aucune installation n'est tentée) : " + str(erreur).splitlines()[0])


def trouver_axe(explicite=None):
    candidats = [explicite, os.environ.get("AXE_CORE_JS"), ROOT / "node_modules/axe-core/axe.min.js",
                 AXE_CACHE / "node_modules/axe-core/axe.min.js"]
    for c in candidats:
        if c and Path(c).is_file():
            return Path(c)
    return None


def installer_axe():
    import subprocess
    AXE_CACHE.mkdir(parents=True, exist_ok=True)
    subprocess.run(["npm", "install", "--no-save", "--ignore-scripts", "--prefix", str(AXE_CACHE), f"axe-core@{AXE_VERSION}"],
                   check=True, stdout=subprocess.DEVNULL)
    return trouver_axe()


def attendre_page(page, delai_ms=600):
    page.wait_for_load_state("load")
    try:
        page.wait_for_function("!document.getElementById('mdn-pack') || window.MDN_READY === true", timeout=20000)
    except Exception:
        pass
    page.wait_for_timeout(delai_ms)
    page.evaluate(JS_COMMUN)


class Garde:
    def __init__(self, args):
        self.args = args
        self.dossier = Path(args.out).resolve()
        self.resultats = []

    # -- pages -------------------------------------------------------------
    def pages(self):
        accueil = "index.html" if (self.dossier / "index.html").is_file() else "MEDINA.html"
        if not (self.dossier / accueil).is_file():
            raise RuntimeError(f"aucun index.html ni MEDINA.html dans {self.dossier}")
        frags = sorted(self.dossier.glob("fragments/MEDINA_*.html"))
        voulu = [f for f in frags if f.name.startswith(f"MEDINA_{self.args.fragment}_")]
        frag = (voulu or frags or [self.dossier / "MEDINA.html"])[0]
        return accueil, frag.relative_to(self.dossier).as_posix()

    def choisir_lecon(self, page, base, fragment):
        if self.args.lecon:
            return self.args.lecon
        page.goto(base + fragment + "#/home")
        attendre_page(page)
        codes = page.evaluate(f"[...document.querySelectorAll(\"{LECON_SELECTEUR}\")].map(a=>a.getAttribute('href').split('/').pop())")
        for code in dict.fromkeys(codes):
            page.goto(base + fragment + "#/entry/" + code)
            page.reload()
            attendre_page(page)
            if page.locator(".mc").count():
                return code
        raise RuntimeError("aucune leçon rédigée trouvée dans " + fragment)

    # -- contrôles ---------------------------------------------------------
    def ajouter(self, page_nom, largeur, controle, ok, detail, info=False):
        self.resultats.append({"page": page_nom, "largeur": largeur, "controle": controle,
                               "statut": "info" if info else ("ok" if ok else "echec"), "detail": detail})

    def police(self, page, cdp, nom, largeur, scope):
        d = page.evaluate(JS_POLICE, scope)
        css_ok = police_principale(d["body"]) == POLICE_ATTENDUE and police_principale(d["scope"]) == POLICE_ATTENDUE
        hors = [e for e in d["echantillon"] if police_principale(e["famille"]) != POLICE_ATTENDUE
                and not est_monospace(e["famille"])]
        rendues = {}
        try:
            doc = cdp.send("DOM.getDocument", {"depth": 0})
            ids = cdp.send("DOM.querySelectorAll", {"nodeId": doc["root"]["nodeId"], "selector": "[data-fg-police]"})["nodeIds"]
            for nid in ids[:12]:
                for f in cdp.send("CSS.getPlatformFontsForNode", {"nodeId": nid})["fonts"]:
                    rendues[f["familyName"]] = rendues.get(f["familyName"], 0) + f["glyphCount"]
        except Exception as e:  # le CDP peut manquer sur certains navigateurs
            rendues = {"indisponible": str(e)[:80]}
        total = sum(v for v in rendues.values() if isinstance(v, int))
        atk = sum(v for k, v in rendues.items() if isinstance(v, int) and k.lower().startswith("atkinson hyperlegible next"))
        part = atk / total if total else None
        ok = css_ok and d["charge"] and (part is None or part >= 0.9)
        self.ajouter(nom, largeur, "police", ok, {"body": d["body"], "conteneur": d["scope"], "police_chargee": d["charge"],
                                                   "glyphes_atkinson": None if part is None else round(part, 3),
                                                   "polices_rendues": rendues, "elements_hors_atkinson": hors[:8],
                                                   "echantillon": len(d["echantillon"])})

    def debordement(self, page, nom, largeur):
        d = page.evaluate(JS_DEBORDEMENT)
        ok = d["scrollWidth"] <= d["clientWidth"] + 1
        if largeur <= 400:
            self.ajouter(nom, largeur, "debordement", ok, d)
        elif not ok:
            self.ajouter(nom, largeur, "debordement", True, d, info=True)

    def contraste(self, page, nom, largeur, scope):
        r = analyser_contraste(page.evaluate(JS_CONTRASTE, [scope, self.args.echantillon]),
                               grand_texte_wcag=self.args.grand_texte_wcag)
        r["echecs"] = sorted(r["echecs"], key=lambda x: x["rapport"])
        self.ajouter(nom, largeur, "contraste", not r["echecs"], {**r, "echecs": r["echecs"][:10], "nb_echecs": len(r["echecs"])})

    def saturation(self, page, nom, largeur, scope):
        e = analyser_saturation(page.evaluate(JS_SATURATION, scope))
        self.ajouter(nom, largeur, "saturation", not e, {"nb_echecs": len(e), "echecs": sorted(e, key=lambda x: -x["aire"])[:10]})

    def cartes(self, page, nom, largeur):
        c = page.evaluate(JS_CARTES, self.args.cartes)
        if len(c) < 2:
            return
        rh, rl = rapport_max_min([x["hauteur"] for x in c]), rapport_max_min([x["largeur"] for x in c])
        ok = rh <= RATIO_CARTES_MAX and rl <= RATIO_CARTES_MAX
        tri = sorted(c, key=lambda x: x["hauteur"])
        self.ajouter(nom, largeur, "cartes", ok, {"nombre": len(c), "ratio_hauteur": round(rh, 3), "ratio_largeur": round(rl, 3),
                                                  "plus_basse": tri[0], "plus_haute": tri[-1]})

    def mouvement(self, page, nom, largeur, reduit):
        e = analyser_mouvement(page.evaluate(JS_MOUVEMENT), reduit=reduit)
        self.ajouter(nom, largeur, "mouvement-reduit" if reduit else "transitions", not e,
                     {"nb_echecs": len(e), "echecs": e[:10], "limite_ms": REDUIT_MAX_MS if reduit else TRANSITION_MAX_MS})

    def focus(self, page, nom, largeur, scope, depart=None):
        n = page.evaluate(JS_FOCUS_PREP, scope)
        if depart:
            page.locator(depart).first.focus()
        else:
            page.evaluate("document.activeElement && document.activeElement.blur()")
        vus, sans = 0, []
        for _ in range(self.args.tabulations):
            page.keyboard.press("Tab")
            f = page.evaluate(JS_FOCUS_LIRE)
            if not f or f["id"] is None:
                continue
            vus += 1
            if not indicateur_focus_visible(f["avant"], f["apres"]):
                sans.append({k: f[k] for k in ("chemin", "tag", "texte", "focusVisible")})
        self.ajouter(nom, largeur, "focus", vus > 0 and not sans,
                     {"candidats": n, "focalises": vus, "sans_indicateur": sans[:10], "nb_sans_indicateur": len(sans)})

    def axe(self, page, nom, largeur, scope, chemin_axe):
        page.add_script_tag(path=str(chemin_axe))
        r = page.evaluate("""(scope) => axe.run(document.querySelector(scope) || document,
            {runOnly: {type: 'tag', values: ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa']}, resultTypes: ['violations']})""", scope)
        v = [{"regle": x["id"], "impact": x["impact"], "noeuds": len(x["nodes"]), "aide": x["help"],
              "exemple": (x["nodes"][0]["target"] if x["nodes"] else None)} for x in r["violations"]]
        graves = [x for x in v if x["impact"] in ("serious", "critical")]
        self.ajouter(nom, largeur, "axe", not (self.args.axe_strict and graves),
                     {"version": r.get("testEngine", {}).get("version"), "violations": v}, info=not self.args.axe_strict)

    # -- parcours ----------------------------------------------------------
    def controler_etat(self, page, cdp, nom, largeur, scope, depart_focus=None):
        self.police(page, cdp, nom, largeur, scope)
        self.debordement(page, nom, largeur)
        self.contraste(page, nom, largeur, scope)
        self.saturation(page, nom, largeur, scope)
        self.cartes(page, nom, largeur)
        self.mouvement(page, nom, largeur, reduit=False)
        self.focus(page, nom, largeur, scope, depart_focus)
        if self.chemin_axe and (largeur == max(self.args.largeurs) or self.args.axe_toutes_largeurs):
            try:
                self.axe(page, nom, largeur, scope, self.chemin_axe)
            except Exception as e:
                self.ajouter(nom, largeur, "axe", True, {"erreur": str(e)[:200]}, info=True)

    def executer(self):
        if not self.dossier.is_dir():
            raise RuntimeError(f"dossier construit introuvable : {self.dossier}")
        accueil, fragment = self.pages()
        from playwright.sync_api import sync_playwright
        self.chemin_axe = None
        if not self.args.sans_axe:
            self.chemin_axe = trouver_axe(self.args.axe)
            if not self.chemin_axe and self.args.installer_axe:
                self.chemin_axe = installer_axe()
        srv, base = servir(self.dossier)
        debut = time.time()
        try:
            with sync_playwright() as pw:
                navigateur = lancer_chromium(pw, self.args.chromium)
                self.navigateur = navigateur.version
                for largeur in self.args.largeurs:
                    for reduit in (False, True):
                        ctx = navigateur.new_context(viewport={"width": largeur, "height": 900},
                                                     reduced_motion="reduce" if reduit else "no-preference")
                        page = ctx.new_page()
                        cdp = ctx.new_cdp_session(page)
                        cdp.send("DOM.enable"); cdp.send("CSS.enable")
                        etat = {"nom": None}
                        page.on("pageerror", lambda e, s=etat, l=largeur: self.erreurs.append(
                            {"page": s["nom"], "largeur": l, "type": "js", "message": str(e)[:300]}))
                        page.on("console", lambda m, s=etat, l=largeur: m.type == "error" and not m.text.startswith("Failed to load resource")
                                and self.erreurs.append({"page": s["nom"], "largeur": l, "type": "console", "message": m.text[:300]}))
                        page.on("response", lambda r, s=etat, l=largeur: r.status >= 400 and self.erreurs.append(
                            {"page": s["nom"], "largeur": l, "type": "http", "statut": r.status, "url": r.url}))
                        page.on("requestfailed", lambda r, s=etat, l=largeur: self.erreurs.append(
                            {"page": s["nom"], "largeur": l, "type": "requete", "url": r.url[:200], "message": r.failure}))
                        if not getattr(self, "lecon", None):
                            self.lecon = self.choisir_lecon(page, base, fragment)
                        etapes = [("accueil", accueil, None), ("fragment", fragment + "#/home", ".mcg-home, main"),
                                  ("lecon", fragment + "#/entry/" + self.lecon, ".mc")]
                        for nom, url, attendu in etapes:
                            etat["nom"] = nom
                            page.goto(base + url)
                            page.reload()  # un simple changement de fragment d'URL ne recharge pas la page
                            attendre_page(page)
                            if attendu and not page.locator(attendu).count():
                                self.ajouter(nom, largeur, "chargement", False, {"url": url, "attendu": attendu})
                                continue
                            if reduit:
                                self.mouvement(page, nom, largeur, reduit=True)
                            else:
                                self.controler_etat(page, cdp, nom, largeur, ".mc" if nom == "lecon" else "body")
                        etat["nom"] = "navigo"
                        declencheur = page.locator(".mc-navigo-trigger")
                        if not declencheur.count() or not declencheur.first.is_visible():
                            if not reduit:
                                self.ajouter("navigo", largeur, "chargement", False, {"attendu": ".mc-navigo-trigger visible"})
                        else:
                            declencheur.first.click()
                            page.wait_for_timeout(500)
                            panneau = page.locator(".mc-navigo-panel")
                            if not panneau.first.is_visible():
                                self.ajouter("navigo", largeur, "chargement", False, {"attendu": ".mc-navigo-panel visible"})
                            elif reduit:
                                self.mouvement(page, "navigo", largeur, reduit=True)
                            else:
                                self.controler_etat(page, cdp, "navigo", largeur, ".mc-navigo-panel", ".mc-navigo-trigger")
                        ctx.close()
                navigateur.close()
        finally:
            srv.shutdown()
        self.duree = round(time.time() - debut, 1)
        self.consolider_erreurs(accueil, fragment)

    erreurs: list = []

    def consolider_erreurs(self, accueil, fragment):
        favicon = [e for e in self.erreurs if e.get("url", "").endswith("/favicon.ico")]
        reelles = [e for e in self.erreurs if e not in favicon]
        for nom in ("accueil", "fragment", "lecon", "navigo"):
            for largeur in self.args.largeurs:
                liste = [e for e in reelles if e["page"] == nom and e["largeur"] == largeur]
                self.ajouter(nom, largeur, "erreurs", not liste, {"nb": len(liste), "erreurs": liste[:10]})
        if favicon:
            self.ajouter("accueil", None, "favicon", True,
                         {"note": "requête implicite du navigateur vers /favicon.ico sans réponse (404)", "nb": len(favicon)}, info=True)

    def rapport(self):
        echecs = [r for r in self.resultats if r["statut"] == "echec"]
        return {"outil": "front_garde", "version": 1, "dossier": str(self.dossier), "lecon": getattr(self, "lecon", None),
                "navigateur": getattr(self, "navigateur", None), "axe": str(self.chemin_axe) if self.chemin_axe else None,
                "duree_s": getattr(self, "duree", None), "largeurs": list(self.args.largeurs),
                "seuils": {"police": POLICE_ATTENDUE, "contraste_min": CONTRASTE_MIN, "saturation_hsl_min": SATURATION_MIN,
                           "luminosite_hsl": list(LUMINOSITE_PLAGE), "surface_eblouissante_px2": SURFACE_EBLOUISSANTE_PX2,
                           "ratio_cartes_max": RATIO_CARTES_MAX, "transition_max_ms": TRANSITION_MAX_MS, "reduit_max_ms": REDUIT_MAX_MS},
                "succes": not echecs, "nb_echecs": len(echecs), "resultats": self.resultats}


def resume_lisible(rap) -> str:
    lignes = [f"front_garde — {'SUCCÈS' if rap['succes'] else 'ÉCHEC'} ({rap['nb_echecs']} contrôle(s) en échec), "
              f"leçon {rap['lecon']}, {rap['duree_s']} s, Chromium {rap['navigateur']}, axe {'oui' if rap['axe'] else 'non'}"]
    ordre = ["chargement", "police", "erreurs", "debordement", "contraste", "saturation", "cartes", "transitions",
             "mouvement-reduit", "focus", "axe"]
    for controle in ordre:
        rs = [r for r in rap["resultats"] if r["controle"] == controle]
        if not rs:
            continue
        ko = [r for r in rs if r["statut"] == "echec"]
        marque = "ÉCHEC" if ko else ("info " if all(r["statut"] == "info" for r in rs) else "ok   ")
        lignes.append(f"  [{marque}] {controle:<17} " + ", ".join(f"{r['page']}@{r['largeur']}" for r in ko)[:150])
        for r in ko[:3]:
            d = r["detail"]
            exemple = (d.get("echecs") or d.get("sans_indicateur") or d.get("coupables") or d.get("erreurs")
                       or d.get("elements_hors_atkinson") or []) if isinstance(d, dict) else []
            extrait = {k: d[k] for k in ("ratio_hauteur", "ratio_largeur", "body", "glyphes_atkinson", "scrollWidth") if isinstance(d, dict) and k in d}
            lignes.append(f"           {r['page']}@{r['largeur']} : {json.dumps(extrait, ensure_ascii=False)} "
                          f"{json.dumps(exemple[:1], ensure_ascii=False)[:260]}")
        if controle == "axe":
            for r in rs[:2]:
                v = r["detail"].get("violations", [])
                lignes.append(f"           {r['page']}@{r['largeur']} : " + ", ".join(f"{x['regle']}({x['impact']},{x['noeuds']})" for x in v)[:260])
    return "\n".join(lignes)


def main(argv=None):
    p = argparse.ArgumentParser(description="Contrôle qualité automatique du frontend MEDINA construit.")
    p.add_argument("--out", required=True, help="dossier construit (MEDINA_OUT, avec index.html et fragments/)")
    p.add_argument("--json", help="chemin du rapport JSON (sinon : seulement le résumé)")
    p.add_argument("--fragment", default="S08", help="identifiant du fragment contrôlé (défaut S08)")
    p.add_argument("--lecon", help="code de la leçon contrôlée (défaut : première leçon rédigée)")
    p.add_argument("--largeurs", type=lambda s: tuple(int(x) for x in s.split(",")), default=LARGEURS)
    p.add_argument("--echantillon", type=int, default=80, help="éléments de texte mesurés pour le contraste")
    p.add_argument("--tabulations", type=int, default=20, help="pressions de Tab pour le contrôle du focus")
    p.add_argument("--cartes", default=CARTES_SELECTEUR, help="sélecteur CSS des cartes de catégories")
    p.add_argument("--grand-texte-wcag", action="store_true", help="seuil 3:1 pour le grand texte (WCAG 1.4.3)")
    p.add_argument("--chromium", help="exécutable Chromium (sinon recherche sous PLAYWRIGHT_BROWSERS_PATH)")
    p.add_argument("--axe", help="chemin de axe.min.js")
    p.add_argument("--installer-axe", action="store_true", help=f"installe axe-core@{AXE_VERSION} via npm dans le cache")
    p.add_argument("--sans-axe", action="store_true")
    p.add_argument("--axe-strict", action="store_true", help="échec sur violation axe grave (serious/critical)")
    p.add_argument("--axe-toutes-largeurs", action="store_true")
    args = p.parse_args(argv)
    garde = Garde(args)
    garde.erreurs = []
    try:
        garde.executer()
    except Exception as e:
        print(f"front_garde : impossible d'exécuter le contrôle : {e}", file=sys.stderr)
        return 2
    rap = garde.rapport()
    if args.json:
        Path(args.json).parent.mkdir(parents=True, exist_ok=True)
        Path(args.json).write_text(json.dumps(rap, ensure_ascii=False, indent=1), encoding="utf-8")
    print(resume_lisible(rap))
    return 0 if rap["succes"] else 1


if __name__ == "__main__":
    sys.exit(main())
