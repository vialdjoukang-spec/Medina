#!/usr/bin/env python3
"""Génère le portail clair des 22 espaces de spécialité MEDINA."""
import argparse
import base64
import gzip
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent

# Portal illustrations identify destinations; teaching stays in each fragment.
ICONS = {
    'S01': '<path d="M16 28S5 21 5 13a6 6 0 0 1 11-3 6 6 0 0 1 11 3c0 8-11 15-11 15Z"/><path d="m8 17 4 0 2-5 4 10 2-5h5"/>',
    'S02': '<path d="M14 5v11m4-11v11m-4-4c-3-6-5-3-7 2-2 5-3 11 1 12 3 1 6-2 6-6m4-8c3-6 5-3 7 2 2 5 3 11-1 12-3 1-6-2-6-6m-4-5-3 3m7-3 3 3"/>',
    'T1': '<rect x="8" y="7" width="16" height="18" rx="8" transform="rotate(35 16 16)"/><path d="m6 8-2-2m11-2V1m10 5 3-2m1 12h3m-7 9 2 3m-12-1v3m-8-9-3 1"/><circle cx="13" cy="12" r="1"/><circle cx="19" cy="18" r="1"/>',
    'S03': '<path d="M16 4v7c0 4 4 3 5 1 3-4 7 0 7 5 0 7-5 11-11 10-5-1-7-5-5-8-6-2-5-7-4-9m6-6v7"/><path d="M16 22c2 2 5 0 6-2"/>',
    'S08': '<path d="M11 26c-4 1-6-3-4-6-4-2-3-7 0-9-1-4 4-7 7-4 2-3 7-2 8 2 5 0 7 5 4 8 4 4 0 9-4 8m-6-17v20m-7-13 4 2m7-5-4 3m1 5 5 2"/>',
    'S05': '<circle cx="16" cy="16" r="4"/><circle cx="6" cy="7" r="3"/><circle cx="27" cy="9" r="3"/><circle cx="24" cy="27" r="3"/><path d="m8 9 5 4m6 0 5-3m-6 9 4 5M6 16v8h6"/>',
    'S04': '<path d="M12 7c-5-7-10 2-9 10 1 8 7 11 11 5 3-5-5-4-4-9 0-2 2-3 2-6m8 0c5-7 10 2 9 10-1 8-7 11-11 5-3-5 5-4 4-9 0-2-2-3-2-6m-8 10c5 0 3 7 3 12m5-12c-5 0-3 7-3 12"/>',
    'S06': '<path d="M16 4c-2 4-9 11-9 17a9 9 0 0 0 18 0c0-6-7-13-9-17Z"/><path d="M12 19c-2 3-1 6 2 7"/>',
    'T4': '<circle cx="11" cy="17" r="8"/><circle cx="22" cy="15" r="8"/><circle cx="10" cy="17" r="2"/><circle cx="23" cy="15" r="2"/><path d="m14 7 3-3m0 24 3-3"/>',
    'S14': '<circle cx="16" cy="11" r="7"/><path d="M16 18v11m-5-5h10m-16-13 4 3m18-3-4 3"/>',
    'S16': '<path d="M22 6c-7-4-15 1-15 10s8 15 17 9"/><circle cx="20" cy="12" r="4"/><path d="M19 17c-7-2-8 8-2 8 3 0 5-2 5-5m-8 0 4 1"/>',
    'T2': '<circle cx="16" cy="6" r="3"/><path d="M7 15c6-5 12-5 18 0m-9-5v17m-6 1 6-7 6 7"/><circle cx="5" cy="22" r="2"/><circle cx="27" cy="22" r="2"/>',
    'S07': '<path d="m16 3 11 5v9c0 6-6 10-11 13C11 27 5 23 5 17V8l11-5Z"/><path d="m10 16 4 4 8-9"/>',
    'S10': '<path d="M6 7c-2-5 5-7 7-2l5 8m-2 6 4 9c2 5 9 2 6-3l-5-8m-7-9 5 8m-9-3 5 8"/><circle cx="16" cy="16" r="4"/>',
    'S15': '<path d="M16 4c-4 6-9 12-9 17a9 9 0 0 0 18 0c0-5-5-11-9-17Z"/><path d="M11 21h10m-5-5v10"/>',
    'S11': '<path d="m3 11 13-6 13 6-13 6-13-6Zm0 7 13 6 13-6M3 25l13 6 13-6"/>',
    'S12': '<path d="M10 22c-4-3-5-7-4-11 2-9 17-10 19 0 2 7-8 7-8 13 0 6-7 7-7 1m0-12c0-7 10-8 11-1 0 3-5 3-6 7"/>',
    'S13': '<path d="M2 16S7 7 16 7s14 9 14 9-5 9-14 9S2 16 2 16Z"/><circle cx="16" cy="16" r="5"/><circle cx="16" cy="16" r="1"/>',
    'T3': '<path d="m19 2-12 17h8l-2 11 12-18h-8l2-10Z"/>',
    'T5': '<circle cx="14" cy="14" r="9"/><path d="m21 21 8 8m-20-15h10m-5-5v10"/>',
    'T6': '<path d="m3 14 13-11 13 11m-23-2v16h20V12m-15 7h10m-5-5v10"/>',
    'T7': '<path d="M5 4h22v17H14l-7 7v-7H5V4Z"/><path d="M10 10h12m-12 5h8"/>',
}


def fragment_catalogue(path):
    """Read a built frontend's own course counts, including packed builds."""
    source = path.read_text(encoding='utf-8')
    packed = re.search(r'<script id="mdn-pack"[^>]*>([^<]+)</script>', source)
    if packed:
        source += gzip.decompress(base64.b64decode(packed.group(1))).decode('utf-8')
    match = re.search(r'<script\b[^>]*\bid=["\']medina-category-organisation-data["\'][^>]*>(.*?)</script>', source, re.S)
    if not match:
        raise ValueError(f'organisation du fragment absente : {path}')
    data = json.loads(match.group(1))
    if type(data.get('integrated_count')) is not int or data['integrated_count'] < 0:
        raise ValueError(f'compteur de cours intégrés invalide : {path}')
    return data


def embedded_typography():
    path = ROOT / 'shell/typography.css'
    if not path.exists():
        return ''
    css = path.read_text(encoding='utf-8')
    for style in ('Roman', 'Italic'):
        filename = f'AnthropicSerif-{style}-Web.woff2'
        font = ROOT / 'assets/fonts' / filename
        if not font.is_file():
            raise ValueError(f'police de lecture manquante : {font}')
        css = css.replace('../assets/fonts/' + filename, 'data:font/woff2;base64,' + base64.b64encode(font.read_bytes()).decode('ascii'))
    return css


STYLE = """
:root{color-scheme:light;--paper:#faf9f6;--ink:#292821;--muted:#73726b;--line:#e4e2dc;--accent:#317765;--medina-serif:Georgia,'Times New Roman',serif}
*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:2rem}body{margin:0;background:var(--paper);color:var(--ink);font:17px/1.5 var(--medina-serif);-webkit-font-smoothing:antialiased}button,input{font:inherit}button,a{-webkit-tap-highlight-color:transparent}a{color:inherit}button{cursor:pointer}svg{display:block}::selection{background:#e2e9df}a:focus-visible,button:focus-visible,input:focus-visible{outline:2px solid var(--accent);outline-offset:5px}[hidden]{display:none!important}
.wrap{width:min(1160px,100% - 64px);margin-inline:auto}.skip{position:fixed;left:18px;top:16px;z-index:20;padding:12px 18px;background:white;border:1px solid var(--accent);border-radius:8px;transform:translateY(-160%)}.skip:focus{transform:translateY(0)}
.masthead{display:flex;align-items:center;justify-content:space-between;min-height:108px;border-bottom:1px solid var(--line);gap:20px}.brand{display:flex;align-items:center;gap:13px;text-decoration:none}.brand-symbol{width:38px;height:38px;display:grid;place-items:center;color:var(--accent);border:1px solid #d9dfd4;border-radius:11px;background:#f1f3ec}.brand-name{display:block;font-size:25px;line-height:1.15;letter-spacing:.045em}.brand-caption{display:block;font-size:12px;color:var(--muted);margin-top:3px;letter-spacing:.02em}.masthead nav{display:flex;align-items:center;gap:28px;font-size:15px}.masthead nav a{text-decoration:none;color:#5d5c55}.masthead nav a:hover{color:var(--accent)}.nav-marker{width:6px;height:6px;background:var(--accent);border-radius:50%;display:inline-block;margin-right:8px;vertical-align:middle}
.hero{display:grid;grid-template-columns:minmax(0,1.6fr) minmax(0,1fr);align-items:center;gap:64px;padding:78px 0 72px}.eyebrow{display:flex;align-items:center;gap:10px;color:var(--accent);font-size:12px;letter-spacing:.13em;text-transform:uppercase;margin:0 0 21px}.eyebrow::before{content:'';width:22px;height:1px;background:currentColor}h1{font-size:clamp(42px,5.1vw,68px);font-weight:400;line-height:1.07;letter-spacing:-.045em;margin:0;max-width:720px}h1 em{font-weight:400;color:var(--accent)}.hero-copy{font-size:19px;line-height:1.6;color:var(--muted);max-width:515px;margin:24px 0 0}.hero-meta{display:flex;gap:25px;align-items:center;margin-top:28px;font-size:14px;color:var(--muted)}.hero-meta strong{font-size:17px;font-weight:400;color:var(--ink);margin-right:4px}.hero-meta span+span{border-left:1px solid var(--line);padding-left:25px}
.hero-art{position:relative;min-height:278px;isolation:isolate;perspective:1000px;display:grid;place-items:center}.art-halo{position:absolute;inset:0;z-index:-1;background:radial-gradient(ellipse,#e9eee4 0%,#f4f4ed 48%,transparent 70%)}.reading-page{width:245px;min-height:222px;border:1px solid #e3e5da;border-radius:12px;background:linear-gradient(150deg,#fffefb,#f7f8ef);box-shadow:0 22px 45px #4d584d0d,0 4px 8px #4d584d06;position:relative;transform:rotate(-4deg);padding:25px}.reading-page::before,.reading-page::after{content:'';position:absolute;inset:0;border:1px solid #e1e5d9;background:#f9faf2;border-radius:12px;z-index:-1;transform:rotate(7deg) translate(12px,7px)}.reading-page::after{background:#eff3ea;transform:rotate(13deg) translate(20px,13px);z-index:-2}.art-note{color:#777d6f;font-size:10px;letter-spacing:.14em;text-transform:uppercase;margin:0 0 14px}.art-title{font-size:28px;line-height:1.2;letter-spacing:-.02em;margin:0;color:#4a594b}.art-lines{display:grid;gap:8px;margin:20px 0 21px}.art-lines i{height:1px;background:#e2e7db}.art-lines i:nth-child(2){width:83%}.art-lines i:nth-child(3){width:65%}.art-subjects{display:flex;flex-wrap:wrap;gap:5px}.art-subjects span{background:#eaf0e3;color:#5a705c;border:1px solid #dfe7d7;padding:3px 7px;border-radius:5px;font-size:10px}.art-seal{position:absolute;right:-20px;top:55px;display:grid;place-items:center;width:57px;height:57px;background:#fcfcf6;border:1px solid #dde5d7;border-radius:50%;color:#78956f;box-shadow:0 5px 14px #364c3c0d}
.library{padding-bottom:64px}.library-head{display:flex;justify-content:space-between;gap:36px;align-items:flex-end;margin:0 0 28px}.section-kicker{font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);margin:0 0 8px}h2{font-size:32px;letter-spacing:-.025em;line-height:1.2;font-weight:400;margin:0}.section-copy{margin:8px 0 0;color:var(--muted);font-size:15px}.search{position:relative;width:330px;flex:none}.search svg{position:absolute;left:17px;top:15px;width:18px;height:18px;color:#77796e;pointer-events:none}.search input{appearance:none;border:1px solid #deded6;border-radius:10px;background:#fffefa;width:100%;height:49px;padding:10px 43px 10px 46px;font-size:15px;color:var(--ink);box-shadow:0 2px 5px #494a3003}.search input::placeholder{color:#73726b}.search input::-webkit-search-cancel-button{-webkit-appearance:none}.search button{position:absolute;right:7px;top:7px;width:35px;height:35px;border:0;background:transparent;color:var(--muted);font-size:24px;border-radius:5px}.search button:hover{background:#f0f1e8}.sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}.search-status{font-size:14px;color:var(--muted);margin:0 0 18px;min-height:21px}
.specialties{list-style:none;padding:0;margin:0;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:19px}.specialty{min-width:0}.specialty-card{--card-accent:var(--accent);display:flex;flex-direction:column;height:100%;min-height:225px;padding:26px 25px 22px;border:1px solid #e5e4dd;border-radius:13px;background:linear-gradient(148deg,#fffefa,#fffefa 70%,var(--card-tint,#f5f7ef));text-decoration:none;box-shadow:0 2px 1px #ffffff inset,0 4px 10px #46433604;position:relative;transition:transform .22s ease,border-color .22s ease,box-shadow .22s ease}.specialty-card:hover{transform:translateY(-5px);border-color:color-mix(in srgb,var(--card-accent) 38%,#e5e4dd);box-shadow:0 13px 24px #474b360a,0 3px 6px #474b3605}.specialty-card:focus-visible{outline-color:var(--card-accent)}.card-top{display:flex;align-items:center;justify-content:space-between;gap:20px;margin-bottom:23px}.card-symbol{width:44px;height:44px;background:var(--card-tint,#f1f4eb);border:1px solid color-mix(in srgb,var(--card-accent) 17%,#edece5);border-radius:12px;color:var(--card-accent);display:grid;place-items:center;box-shadow:0 1px 1px #fff inset,0 3px 5px #46533805}.card-symbol svg{width:27px;height:27px}.card-arrow{width:28px;height:28px;display:grid;place-items:center;border:1px solid #eeeee5;border-radius:50%;color:#93988a;transition:color .2s,transform .2s,border-color .2s}.specialty-card:hover .card-arrow{color:var(--card-accent);border-color:color-mix(in srgb,var(--card-accent) 30%,#eeeee5);transform:translate(2px,-2px)}h3{font-size:25px;line-height:1.22;letter-spacing:-.023em;font-weight:400;margin:0 0 11px;overflow-wrap:anywhere}.card-description{margin:0;color:var(--muted);font-size:14px;line-height:1.5;max-width:290px}.card-count{display:flex;align-items:center;gap:7px;color:#70756a;font-size:12px;line-height:1.3;margin-top:auto;padding-top:24px}.count-dot{height:5px;width:5px;flex:none;border-radius:50%;background:var(--card-accent)}.specialty-card[data-course-count="0"] .count-dot{background:#bec3b7}.specialty-card[data-course-count="0"] .card-count{color:#73726b}.empty{padding:44px 22px;margin:0;text-align:center;border:1px dashed #d8dbcf;border-radius:13px;color:var(--muted);background:#f4f5ed}.empty strong{display:block;color:var(--ink);font-size:23px;font-weight:400;margin-bottom:6px}.empty button{color:var(--accent);background:transparent;border:0;text-decoration:underline;text-underline-offset:4px;margin-top:12px;padding:7px}
.footer{display:flex;align-items:center;justify-content:space-between;gap:20px;border-top:1px solid var(--line);padding:27px 0 40px;font-size:13px;color:var(--muted)}.footer p{margin:0}.footer a{text-decoration:none}.footer a:hover{text-decoration:underline;text-underline-offset:4px}.footer-brand{color:#65695e;letter-spacing:.08em}.footer-note{margin-left:12px}
@media(min-width:1300px){.hero{padding-top:89px;padding-bottom:83px}.specialty-card{min-height:242px}.card-top{margin-bottom:25px}}
@media(max-width:920px){.hero{gap:32px;grid-template-columns:minmax(0,1.5fr) minmax(0,1fr)}.hero-art{transform:scale(.88)}.specialties{grid-template-columns:repeat(2,minmax(0,1fr))}.reading-page{width:222px}.library-head{gap:24px}.search{width:290px}.hero-copy{font-size:18px}}
@media(max-width:640px){.wrap{width:calc(100% - 36px)}.masthead{min-height:90px}.masthead nav{gap:16px;font-size:13px}.masthead nav a:last-child{display:none}.brand-name{font-size:22px}.brand-symbol{width:33px;height:33px}.hero{display:block;padding:44px 0 37px}.hero-art{display:none}h1{font-size:37px;line-height:1.09;letter-spacing:-.04em}.hero-copy{font-size:17px;margin-top:21px;max-width:390px}.eyebrow{font-size:10px;margin-bottom:18px}.hero-meta{margin-top:22px;font-size:13px;gap:18px}.hero-meta span+span{padding-left:18px}.hero-meta strong{font-size:16px}.library-head{display:block;margin-bottom:18px}h2{font-size:29px}.section-copy{font-size:14px}.search{width:100%;margin-top:23px}.search-status{margin-bottom:17px;font-size:13px}.specialties{gap:13px}.specialty-card{padding:20px 18px 19px;min-height:218px;border-radius:11px}.card-top{margin-bottom:21px}.card-symbol{width:38px;height:38px;border-radius:10px}.card-symbol svg{width:24px;height:24px}h3{font-size:22px}.card-description{font-size:13px}.card-count{font-size:11px;padding-top:21px}.library{padding-bottom:39px}.footer{padding:23px 0 30px;align-items:flex-start;font-size:12px}.footer-note{display:block;margin:5px 0 0}.footer a{max-width:105px;text-align:right}}
@media(max-width:460px){.specialties{grid-template-columns:minmax(0,1fr)}.specialty-card{min-height:194px;padding:21px 22px}.card-top{margin-bottom:17px}.card-description{max-width:none}h3{font-size:25px}.card-count{padding-top:20px;font-size:12px}.card-symbol{width:41px;height:41px}.card-symbol svg{width:26px;height:26px}}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}*,*::before,*::after{transition:none!important}.specialty-card:hover{transform:none}}
"""

SCRIPT = r"""
(()=>{
 const input=document.getElementById('specialty-search');
 const cards=[...document.querySelectorAll('[data-specialty-item]')];
 const status=document.getElementById('search-status');
 const empty=document.getElementById('search-empty');
 const clear=document.getElementById('clear-search');
 const normalize=value=>value.normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLocaleLowerCase('fr');
 function filter(){
  const query=normalize(input.value.trim());let visible=0;
  for(const card of cards){const match=normalize(card.dataset.search).includes(query);card.hidden=!match;if(match)visible++;}
  status.textContent=query?(visible===1?'1 spécialité correspond à votre recherche.':visible+' spécialités correspondent à votre recherche.'):'22 spécialités à explorer.';
  empty.hidden=visible!==0;clear.hidden=!input.value;
 }
 function reset(){input.value='';filter();input.focus();}
 input.addEventListener('input',filter);
 input.addEventListener('keydown',event=>{if(event.key==='Escape'){event.preventDefault();reset();}});
 clear.addEventListener('click',reset);document.getElementById('reset-search').addEventListener('click',reset);
 filter();
})();
"""


def portal_v2():
    faces = ''.join("@font-face{font-family:'Atkinson Hyperlegible Next';font-style:%s;font-weight:%s;font-display:swap;src:url(data:font/woff2;base64,%s) format('woff2')}"
                    % (style, weight, base64.b64encode((ROOT / 'shell/fonts' / name).read_bytes()).decode('ascii'))
                    for name, style, weight in (('ahn-400.woff2', 'normal', '400'), ('ahn-400i.woff2', 'italic', '400'),
                                                ('ahn-600.woff2', 'normal', '600'), ('ahn-700.woff2', 'normal', '700')))
    return faces + (ROOT / 'engine/portal_v2.css').read_text(encoding='utf-8') + (ROOT / 'engine/portal_v3.css').read_text(encoding='utf-8')


def progress(catalogue):
    """Catégories couvertes et leçons intégrées, d'après l'organisation du fragment construit."""
    lessons = [lesson for block in catalogue.get('blocks', []) for lesson in block.get('lessons', [])]
    done = [lesson for lesson in lessons if lesson.get('integrated')]
    categories = catalogue.get('category_count', 0)
    covered = min(categories, sum(len(lesson.get('variants') or [lesson]) for lesson in done))
    if catalogue.get('nosology'):
        gauge = catalogue['nosology']['progress']
        return covered, categories, gauge['filled'], gauge['total']
    return covered, categories, len(done), len(lessons)


def gauge(label, part, whole):
    if not whole:
        return (f'<span class="gauge" data-empty><span class="gauge-label">{label}</span><span class="gauge-track" aria-hidden="true">'
                '<span class="gauge-fluid" style="width:0%"></span></span><span class="gauge-value">—</span></span>')
    pct = round(100 * part / whole, 2)
    return (f'<span class="gauge" role="img" aria-label="{label} : {part} sur {whole}, {pct} %"><span class="gauge-label">{label}</span>'
            f'<span class="gauge-track" aria-hidden="true"><span class="gauge-fluid" style="width:{pct}%"></span></span>'
            f'<span class="gauge-value">{pct} %</span></span>')


MOTIFS = (('M4 12h4l2-5 4 10 2-5h4', 'Quatre onglets par cours'),
          ('M12 3 4 7v6c0 4 3.5 7 8 8 4.5-1 8-4 8-8V7l-8-4Z', 'Sources suisses, puis européennes'),
          ('M6 4h12v16H6zM9 8h6M9 12h6M9 16h4', 'Information professionnelle Swissmedic'),
          ('M5 12l4 4 10-10', 'Relecture distincte en deux passes'))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--fragments-dir', type=Path, default=ROOT / 'dist/fragments')
    parser.add_argument('--output', type=Path, default=ROOT / '_site/index.html')
    args = parser.parse_args()
    fragments = json.loads((ROOT / 'fragments.json').read_text(encoding='utf-8'))
    registry = json.loads((ROOT / 'organisation/fragments.json').read_text(encoding='utf-8'))
    names = {fragment['id']: fragment for fragment in registry}
    if len(fragments) != 22 or len(names) != 22 or {f['id'] for f in fragments} != set(names):
        raise SystemExit('Le portail doit présenter les 22 spécialités du registre partagé.')
    fragments.sort(key=lambda fragment: names[fragment['id']]['order'])
    cards = []
    total_courses = 0
    totals = [0, 0, 0, 0]
    for fragment in fragments:
        ident = fragment['id']
        filename = f"MEDINA_{ident}_{fragment['slug']}.html"
        path = args.fragments_dir / filename
        if not path.is_file():
            raise SystemExit(f'fragment manquant : {path}')
        catalogue = fragment_catalogue(path)
        presentation = catalogue['fragment']
        if presentation['id'] != ident:
            raise SystemExit(f'organisation d’une autre spécialité : {path}')
        count = catalogue['integrated_count']
        total_courses += count
        specialty = presentation.get('display_name') or names[ident]['specialty']
        description = presentation.get('description') or 'Explorer les catégories de cette spécialité.'
        accent = presentation.get('accent', '#317765')
        if not re.fullmatch(r'#[0-9a-fA-F]{6}', accent):
            accent = '#317765'
        label = 'cours intégré' if count == 1 else 'cours intégrés'
        search_text = ' '.join([specialty, names[ident]['specialty'], names[ident]['label'], description])
        symbol = ICONS[ident]
        covered, categories, done, lessons = progress(catalogue)
        for i, value in enumerate((covered, categories, done, lessons)):
            totals[i] += value
        gauges = f'<span class="gauges">{gauge("Catégories", covered, categories)}{gauge("Leçons", done, lessons)}</span>'
        cards.append(f'''<li class="specialty" data-specialty-item data-search="{html.escape(search_text, quote=True)}">
 <a class="specialty-card" href="fragments/{filename}" data-testid="specialty-card" data-fragment-id="{ident}" data-course-count="{count}" style="--card-accent:{accent};--card-tint:color-mix(in srgb,{accent} 7%,#fffefa)" title="{html.escape(names[ident]['label'], quote=True)}">
  <div class="card-top"><span class="card-symbol" aria-hidden="true"><svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.45" stroke-linecap="round" stroke-linejoin="round">{symbol}</svg></span><span class="card-arrow" aria-hidden="true"><svg width="13" height="13" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.3"><path d="M4 12 12 4M4 4h8v8"/></svg></span></div>
  <h3>{html.escape(specialty)}</h3><p class="card-description">{html.escape(description)}</p>
  <span class="card-count"><i class="count-dot" aria-hidden="true"></i><span>{count} {label}</span></span>
  {gauges}
 </a></li>''')
    covered, categories, done, lessons = totals
    motifs = ''.join(f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="{path}"/></svg>{text}</li>' for path, text in MOTIFS)
    overview = (f'<div class="overview" data-testid="portal-overview" aria-label="Progression de l’atlas">'
                f'<div class="overview-item"><b>{covered}<small> / {categories}</small></b><span>catégories couvertes</span>{gauge("Catégories", covered, categories)}</div>'
                f'<div class="overview-item"><b>{done}<small> / {lessons}</small></b><span>leçons remplies</span>{gauge("Leçons", done, lessons)}</div>'
                f'<div class="overview-item"><b>{total_courses}</b><span>cours publiés dans les 22 spécialités</span></div><ul class="motifs" aria-label="Principes de l’atlas">{motifs}</ul></div>'
                '<p class="legend-note">Jauges : catégories reliées à un cours existant, puis leçons remplies sur le total des leçons et entités prévues. Une coquille vide compte pour zéro leçon remplie.</p>')
    page = f'''<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="light">
<meta name="description" content="Explorez MEDINA : 22 espaces de spécialité pour lire, comprendre et relier les connaissances médicales.">
<title>MEDINA — Une spécialité, un espace de lecture</title><style>{STYLE}</style><style id="medina-typography">{embedded_typography()}</style><style id="medina-portal-v2">{portal_v2()}</style></head><body data-testid="medina-portal">
<a class="skip" href="#specialites">Aller aux spécialités</a><div class="wrap">
<header class="masthead"><a class="brand" href="index.html" aria-label="MEDINA, accueil"><span class="brand-symbol" aria-hidden="true"><svg width="21" height="21" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3"><path d="M3 20V5l9 11 9-11v15M3 5l9 7 9-7"/></svg></span><span><span class="brand-name">MEDINA</span><span class="brand-caption">Atlas médical interactif</span></span></a><nav aria-label="Navigation principale"><a href="#specialites"><span class="nav-marker" aria-hidden="true"></span>Les spécialités</a><a href="organisation.html">L’atlas</a></nav></header>
<main><section class="hero" aria-labelledby="welcome-title" data-testid="portal-hero"><div><p class="eyebrow">Un espace pour apprendre</p><h1 id="welcome-title">Explorer la médecine,<br><em>une spécialité à la fois.</em></h1><p class="hero-copy">Prenez le temps de comprendre et de relier les savoirs. Choisissez une spécialité pour ouvrir votre espace de lecture.</p><div class="hero-meta"><span><strong>22</strong> spécialités</span><span data-testid="portal-course-total"><strong>{total_courses}</strong> cours intégrés</span></div></div>
<div class="hero-art" aria-hidden="true"><div class="art-halo"></div><div class="reading-page"><p class="art-note">Le plaisir de comprendre</p><p class="art-title">Un savoir.<br>Plusieurs regards.</p><div class="art-lines"><i></i><i></i><i></i></div><div class="art-subjects"><span>Pathologie</span><span>Examens</span><span>Sciences</span><span>Pharmacologie</span></div><span class="art-seal"><svg width="31" height="31" viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.3"><path d="M16 5v22M5 16h22m-19-8 16 16m0-16L8 24"/><circle cx="16" cy="16" r="10"/></svg></span></div></div></section>
<section class="library" id="specialites" aria-labelledby="specialties-title"><div class="library-head"><div><p class="section-kicker">Les espaces de l’atlas</p><h2 id="specialties-title">Quelle spécialité vous intéresse ?</h2><p class="section-copy">Chaque spécialité ouvre ses catégories et ses cours.</p></div><div class="search" role="search"><label class="sr-only" for="specialty-search">Rechercher une spécialité</label><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><circle cx="10" cy="10" r="6"/><path d="m15 15 5 5"/></svg><input id="specialty-search" type="search" placeholder="Rechercher une spécialité…" autocomplete="off" aria-controls="specialty-grid" data-testid="specialty-search"><button id="clear-search" type="button" aria-label="Effacer la recherche" hidden>×</button></div></div>
{overview}<p class="search-status" id="search-status" role="status" aria-live="polite" aria-atomic="true" data-testid="search-status">22 spécialités à explorer.</p><ul class="specialties" id="specialty-grid" data-testid="specialty-grid">{''.join(cards)}</ul>
<div class="empty" id="search-empty" hidden data-testid="search-empty"><strong>Aucune spécialité trouvée.</strong><span>Essayez un autre nom pour poursuivre votre exploration.</span><br><button id="reset-search" type="button">Voir toutes les spécialités</button></div><noscript><p class="section-copy">Les 22 spécialités restent accessibles ci-dessus. La recherche nécessite JavaScript.</p></noscript></section></main>
<footer class="footer"><p><span class="footer-brand">MEDINA</span><span class="footer-note">Une spécialité, un espace de lecture.</span></p><a href="organisation.html">Explorer l’organisation de l’atlas ↗</a></footer></div><script>{SCRIPT}</script></body></html>
'''
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(page, encoding='utf-8')
    print(f'index {args.output} ({len(fragments)} spécialités, {total_courses} cours intégrés)')


if __name__ == '__main__':
    main()
