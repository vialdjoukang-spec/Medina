#!/usr/bin/env python3
"""Générateur de chapitres MEDINA (contrat CHAPTER_SPEC.md) pour G-04-Gastroentérologie et hépatologie.

Le contenu médical est écrit dans chapitres/<CODE>.py ; ce module ne fait que l'assemblage HTML
(onglets, sommaires, îlots, fenêtres, Pareto, images .gif embarquées) et des contrôles de cohérence.
"""
import base64, html, json, os, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]

def esc(s):
    return html.escape(s, quote=True)

class Chapter:
    def __init__(self, code, title, codeline, status, pharma_tab, toc_e='Examens', toc_p='Pharmacologie'):
        self.code, self.c = code, code.lower()
        self.title, self.codeline, self.status, self.pharma_tab = title, codeline, status, pharma_tab
        self.A, self.E, self.S, self.P, self.pops, self.imgs = [], [], [], [], {}, []
        self.toc_e, self.toc_p = toc_e, toc_p
    # --- mots verts, fenêtres, Pareto
    def w(self, key, label):
        return f'<button class="w" data-k="{key}">{label}</button>'
    def pop(self, key, title, body):
        if key in self.pops: raise SystemExit('fenêtre en double ' + key)
        self.pops[key] = (title, body)
    def pareto(self, key, label, cover, items):
        cov = ','.join(cover)
        self.pop(key, 'Loi de Pareto — ' + label, f'<p class="ratio" data-cover="{cov}"></p><ul>' + ''.join(f'<li>{i}</li>' for i in items) + '</ul>')
        return f'<button class="pareto-btn ui" data-k="{key}">▲ Loi de Pareto — {label}</button>'
    # --- images .gif (fichier sous chapters/<CODE>/img/, intégré en base64 dans la fenêtre ou l'îlot)
    def img(self, fname, alt, caption, credit):
        p = ROOT / 'chapters' / self.code / 'img' / fname
        data = p.read_bytes()
        if not data.startswith(b'GIF8'): raise SystemExit('pas un GIF : ' + fname)
        if len(data) > 160_000: raise SystemExit('GIF trop lourd : %s %d' % (fname, len(data)))
        w, h = int.from_bytes(data[6:8], 'little'), int.from_bytes(data[8:10], 'little')
        b64 = base64.b64encode(data).decode()
        self.imgs.append((fname, len(data)))
        return (f'<figure><img src="data:image/gif;base64,{b64}" width="{w}" height="{h}" loading="lazy" decoding="async" '
                f'alt="{esc(alt)}"><figcaption>{caption} <small>{credit}</small></figcaption></figure>')
    # --- îlots
    def a(self, n, title, body):
        self.A.append((f'{self.c}-{n}', n, title, body))
    def e(self, n, title, body):
        self.E.append((f'{self.c}-e-{n}', n, title, body))
    def p(self, n, title, body):
        self.P.append((f'{self.c}-p-{n}', n, title, body))
    def s(self, sid, tab, title, body):
        self.S.append((f'{self.c}-s-{sid}', tab, title, body))
    @staticmethod
    def _sec(i, n, t, b):
        return f'<section class="ilot" id="{i}"><h2><span class="n">{n}</span>{t}</h2>{b}</section>\n'
    def _toc(self, label, items):
        return '<nav class="toc ui"><b>' + label + '</b><ol>' + ''.join(f'<li><a href="#{i}">{t}</a></li>' for i, n, t, b in items) + '</ol></nav>'
    PAGER = '<div class="pager ui"><button class="prev">← Îlot précédent</button><span></span><button class="next">Îlot suivant →</button></div>'
    def render(self):
        c, C = self.c, self.code
        head = (f'<template id="ch-{C}"><div class="chap">\n<div class="chap-head"><div class="code">{self.codeline}</div>\n'
                f'<h1>{self.title}</h1><span class="status">{self.status}</span></div>\n'
                '<div class="tabs ui" role="tablist">'
                '<button role="tab" aria-controls="pA" data-p="pA" aria-selected="true">⚕ Pathologie et prise en charge</button>'
                '<button role="tab" aria-controls="pE" data-p="pE" aria-selected="false">🔬 Examens complémentaires</button>'
                '<button role="tab" aria-controls="pS" data-p="pS" aria-selected="false">⚛ Sciences fondamentales spécialisées</button>'
                f'<button role="tab" aria-controls="pP" data-p="pP" aria-selected="false">💊 {self.pharma_tab}</button></div>\n')
        half = (len(self.A) + 1) // 2
        fa = head + '<div class="panel" id="pA">' + self._toc('Plan du cours', self.A) + '<div class="chap-body">\n' + ''.join(self._sec(*x) for x in self.A[:half])
        fb = ''.join(self._sec(*x) for x in self.A[half:]) + '</div>' + self.PAGER + '</div>\n'
        fc = ('<div class="panel" id="pE" hidden>' + self._toc(self.toc_e, self.E) + '<div class="chap-body">\n' + ''.join(self._sec(*x) for x in self.E) + '</div>' + self.PAGER + '</div>\n')
        bar = ''.join(f'<button role="tab" aria-selected="{"true" if k == 0 else "false"}" aria-controls="{i}" data-s="{i}">{tab}</button>' for k, (i, tab, t, b) in enumerate(self.S))
        fc += ('<div class="panel" id="pS" hidden><div class="sci-bar ui" role="tablist">' + bar + '</div><div class="chap-body sci-body">'
               + ''.join(f'<div class="sci" id="{i}"><section class="ilot" id="{i}-body"><h2><span class="n"></span>{t}</h2>{b}</section></div>' for i, tab, t, b in self.S)
               + '</div>\n</div>\n')
        fd = ('<div class="panel" id="pP" hidden>' + self._toc(self.toc_p, self.P) + '<div class="chap-body">\n' + ''.join(self._sec(*x) for x in self.P) + '</div>' + self.PAGER + '</div>\n</div></template>\n')
        fp = ''.join(f'<template data-pop="{k}" data-title="{esc(t)}">{b}</template>\n' for k, (t, b) in self.pops.items())
        return {'a': fa, 'b': fb, 'c': fc, 'd': fd, 'pop': fp}
    def check(self, files):
        allsrc = ''.join(files.values())
        keys = set(re.findall(r'data-k="([^"]+)"', allsrc))
        missing = sorted(k for k in keys if k not in self.pops)
        unused = sorted(k for k in self.pops if k not in keys)
        bad = sorted(k for k in self.pops if not (k.startswith(self.c + '-') or k.startswith('pareto-' + self.c + '-')))
        ids = re.findall(r'id="([^"]+)"', allsrc)
        dup = sorted({i for i in ids if ids.count(i) > 1})
        for name, lst in (('A', self.A), ('E', self.E), ('P', self.P)):
            pass
        problems = {'fenetres_absentes': missing, 'cles_sans_prefixe': bad, 'ids_doubles': dup}
        if any(problems.values()):
            raise SystemExit(json.dumps(problems, ensure_ascii=False))
        return {'fenetres': len(self.pops), 'non_utilisees': unused, 'quiz': allsrc.count('class="quiz'), 'mots': len(re.sub(r'<[^>]+>', ' ', re.sub(r'base64,[^"]+', '', allsrc)).split()), 'images': self.imgs}
    def write(self):
        files = self.render()
        rep = self.check(files)
        d = ROOT / 'chapters' / self.code
        d.mkdir(parents=True, exist_ok=True)
        for old in d.glob('*.html'): old.unlink()
        for k, v in files.items():
            (d / f'{self.code}_{k}.html').write_text(v, encoding='utf-8')
        print(self.code, json.dumps(rep, ensure_ascii=False))
        return rep

def quiz(q, options, fb):
    """options : liste de (texte, bon:bool)."""
    return '<div class="quiz ui"><p>' + q + '</p>' + ''.join(f'<button data-ok="{1 if ok else 0}">{t}</button>' for t, ok in options) + f'<p class="fb" hidden>{fb}</p></div>'

def src(*refs):
    return '<p class="src">Références : ' + ' ; '.join(f'<a href="{u}" target="_blank" rel="noopener">{t}</a>' for t, u in refs) + '.</p>'

def table(head, rows):
    return '<table class="t"><tr>' + ''.join(f'<th>{h}</th>' for h in head) + '</tr>' + ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows) + '</table>'

def key(t, label='À retenir.'):
    return f'<div class="key"><b>{label}</b> {t}</div>'

def alert(t, label='Gravité d’abord.'):
    return f'<div class="alert"><b>{label}</b> {t}</div>'

def trap(t, label='Piège'):
    return f'<div class="trap"><span class="k">{label}</span>{t}</div>'

def P(*ps):
    return ''.join(f'<p>{x}</p>' for x in ps)

def cards(*cs):
    return '<div class="two">' + ''.join(f'<div class="card"><b>{t}</b>{b}</div>' for t, b in cs) + '</div>'

def lab(*pairs):
    """Fenêtre structurée : (étiquette, texte)."""
    return ''.join(f'<p class="lab">{l}</p><p>{t}</p>' for l, t in pairs)
