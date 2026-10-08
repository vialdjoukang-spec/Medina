#!/usr/bin/env python3
"""Construit MEDINA.html : frontend MEDORA V6 (renommé MEDINA) + cours rédigés + moteur + glossaire."""
import re, json, sys, glob, html as H
import os
ROOT = os.environ.get('MEDINA_ROOT', os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT + '/tools')
from insert_justifications import load_course_justifications
sys.path.insert(0, ROOT + '/glossary')
import importlib
G = {}
for mod in sorted(glob.glob(ROOT + '/glossary/*.py')):
    name = mod.split('/')[-1][:-3]
    try:
        m = importlib.import_module(name)
        G.update(m.G)
    except Exception as ex:
        print('AVERTISSEMENT glossaire', name, ex)

CLASSMAP = {'tabs':'mc-tabs','panel':'mc-panel','chap-body':'mc-body','sci-body':'mc-sci-body','ilot':'mc-ilot','toc':'mc-toc','sci-bar':'mc-sci-bar',
 'sci':'mc-sci','key':'mc-key','trap':'mc-trap','k':'mc-k','alert':'mc-alert','two':'mc-two','card':'mc-card','t':'mc-t','pareto-btn':'mc-pareto-btn',
 'src':'mc-src','pager':'mc-pager','quiz':'mc-quiz','fb':'mc-fb','status':'mc-status','chap-head':'mc-chap-head','code':'mc-code','n':'mc-n','lab':'mc-lab',
 'ratio':'mc-ratio','maj':'mc-maj','ui':'mc-ui','chap':'mc-chap','prev':'mc-prev','next':'mc-next','w':'mc-w','ssp':'mc-ssp'}

GREEN_BUTTON = re.compile(r'<button\b([^>]*)>(.*?)</button>', re.S)
ATTR = re.compile(r'\s+([\w:-]+)(?:\s*=\s*("[^"]*"|\'[^\']*\'))?')

def green_word(m):
    """Mot vert -> span interactif, quel que soit l'ordre des attributs.

    Chromium rend un <button> comme un bloc en ligne insécable, même en display:inline :
    un libellé long passait entier à la ligne suivante. Le span se coupe comme du texte ;
    role, tabindex et le gestionnaire clavier du moteur conservent l'accessibilité."""
    attrs = [(a.group(1), a.group(2)) for a in ATTR.finditer(m.group(1))]
    names = dict(attrs)
    if names.get('class', '').strip('"\'').split() != ['w'] or 'data-k' not in names:
        return m.group(0)
    rest = ''.join(' ' + k + ('=' + v if v is not None else '') for k, v in attrs
                   if k not in ('class', 'data-k', 'type', 'role', 'tabindex'))
    return '<span class="mc-w" role="button" tabindex="0" data-k=' + names['data-k'] + rest + '>' + m.group(2) + '</span>'

def transform(src):
    # boutons « mot vert » -> span interactif (autorise l'imbrication des abréviations et la coupure en fin de ligne)
    src = GREEN_BUTTON.sub(green_word, src)
    src = re.sub(r'<button data-ok="([01])">(.*?)</button>', r'<div class="mc-opt" role="button" tabindex="0" data-ok="\1">\2</div>', src, flags=re.S)
    def cls(m):
        return 'class="' + ' '.join(CLASSMAP.get(c, c) for c in m.group(1).split()) + '"'
    src = re.sub(r'class="([^"]*)"', cls, src)
    # sommaires internes : pas de href="#…" (conflit avec le routage)
    src = re.sub(r'<a href="#([^"/]+)">', r'<a data-go="\1" role="button" tabindex="0">', src)
    # Le numéro des sous-parties reçoit sa propre couleur sans teinter le titre (apport Alpha).
    src = re.sub(r'(<h[34]>)\s*(\d+(?:\.\d+)+)(?=\s)', r'\1<span class="mc-subn">\2</span>', src)
    return src

KEYS = sorted(G.keys(), key=len, reverse=True)
BOUND_L = r'(?<![A-Za-zÀ-ÿ0-9₀-₉⁺′])'
BOUND_R = r'(?![A-Za-zÀ-ÿ0-9₀-₉⁺′])'
AB_RE = re.compile(BOUND_L + '(' + '|'.join(re.escape(k) for k in KEYS) + ')' + BOUND_R)

def wrap_text(txt, svg=False):
    def rep(m):
        k = m.group(1)
        if svg:
            return f'<tspan class="mc-ab" data-ab="{H.escape(k)}">{k}</tspan>'
        return f'<span class="mc-ab" role="button" tabindex="0" data-ab="{H.escape(k)}">{k}</span>'
    return AB_RE.sub(rep, txt)

TOKEN = re.compile(r'(<!--.*?-->|<[^>]+>)', re.S)
def wrap_html(src):
    out = []; stack_button = 0; in_svg = 0; skip = 0; references = 0; anchors = 0; spans = []
    for part in TOKEN.split(src):
        if not part: continue
        if part.startswith('<'):
            low = part.lower()
            if re.match(r'<span(?:\s|>)', low) and not low.rstrip().endswith('/>'):
                spans.append(bool(spans and spans[-1]) or bool(re.search(r'\bdata-k\s*=', low)))
            elif re.match(r'</span\s*>', low) and spans:
                spans.pop()
            if low.startswith('<ul') and 'data-justification-sources="1"' in low: references += 1
            elif low.startswith('</ul') and references: references -= 1
            if re.match(r'<a(?:\s|>)', low): anchors += 1
            elif re.match(r'</a\s*>', low) and anchors: anchors -= 1
            if low.startswith('<button'): stack_button += 1
            elif low.startswith('</button'): stack_button -= 1
            elif low.startswith('<svg'): in_svg += 1
            elif low.startswith('</svg'): in_svg -= 1
            elif low.startswith('<script') or low.startswith('<style'): skip += 1
            elif low.startswith('</script') or low.startswith('</style'): skip -= 1
            out.append(part)
        else:
            if skip or stack_button or references or anchors or (spans and spans[-1]): out.append(part)
            else: out.append(wrap_text(part, svg=bool(in_svg)))
    return ''.join(out)

CAND = re.compile(r'(?<![A-Za-zÀ-ÿ0-9])([A-Za-zÀ-ÿ0-9][A-Za-zÀ-ÿ0-9₀-₉⁺′\-/.]*)')
WHITE = re.compile(r'^(I{1,3}[ab]?|IV|V|VI|VII|X|[A-Z]|I\d\d(\.\d+)?|[A-Z]\d{2}(-[A-Z]\d{2})?|Frank-Starling|Cheyne-Stokes|Ken-tuc-ky|Val|Ile|Met|mL|mmHg|kDa|mU|mg|pg|ng|µg|mmol|kg|cm|mm|ms|min)$')
def audit(src, name):
    """Retourne les abréviations candidates non couvertes (hors balises, hors mots déjà enveloppés)."""
    s = re.sub(r'<(script|style)[^>]*>.*?</\1>', '', src, flags=re.S)
    s = re.sub(r'<ul[^>]*data-justification-sources="1"[^>]*>.*?</ul>', ' ', s, flags=re.S)
    s = re.sub(r'<a[^>]*data-reference-source="1"[^>]*>.*?</a>', ' ', s, flags=re.S)
    s = re.sub(r'<span class="mc-ab"[^>]*>.*?</span>|<tspan class="mc-ab"[^>]*>.*?</tspan>', ' ', s, flags=re.S)
    s = H.unescape(re.sub(r'<[^>]+>', ' ', s))
    # Dans le texte protégé, chaque terme connu reste couvert aux frontières lexicales,
    # y compris les constituants de formes séparées par un tiret ou une barre oblique.
    s = AB_RE.sub(' ', s)
    miss = {}
    for m in CAND.finditer(s):
        w = m.group(1).rstrip('.-/')
        for piece in re.split(r'[/]', w):
            p = piece.strip('-.')
            if not p or WHITE.match(p) or p in G: continue
            up = sum(ch.isupper() for ch in p)
            if up >= 2 or re.search(r'[A-Z][0-9₀-₉]', p) or re.search(r'[a-z][A-Z]', p) or re.search(r'^[A-Z][a-z]?[⁺₂]', p):
                if p in ('HbA1c',) : pass
                miss[p] = miss.get(p, 0) + 1
    return miss

def words(x): return len(re.sub(r'<[^>]+>', ' ', x).split())
def pareto_ratios(src):
    secs = {m.group(1): m.group(0) for m in re.finditer(r'<section class="mc-ilot" id="([^"]+)">.*?</section>', src, re.S)}
    def fill(m):
        ids = m.group(1).split(',')
        miss = [i for i in ids if i not in secs]
        if miss: raise SystemExit('Pareto : îlot introuvable ' + ','.join(miss))
        tot = sum(words(secs[i]) for i in ids)
        end = src.index('</template>', m.end()); pw = words(src[m.end():end])
        return '<p class="mc-ratio">Fraction contractée : %d mots sur %d, soit %d %% du texte, pour 100 %% des notions utiles</p>' % (pw, tot, round(100*pw/max(tot,1)))
    return re.sub(r'<p class="mc-ratio" data-cover="([^"]+)"></p>', fill, src)

def build(chapters, out):
    v6 = open(os.environ.get('MEDINA_V6', ROOT + '/shell/medina_front.html')).read()
    # renommage visible
    v6 = v6.replace('MEDORA_TEST', 'MEDINA_TEST').replace('MEDORA', 'MEDINA')
    v6 = v6.replace('V6 · SYSTÈMES · INTELLIGENCE &amp; CIM', 'MEDINA · COURS PAR SYSTÈMES').replace('V6 · SYSTÈMES · INTELLIGENCE & CIM', 'MEDINA · COURS PAR SYSTÈMES')
    v6 = v6.replace('Plans détaillés, cours à rédiger.', 'Cours rédigés : ' + str(len(chapters)) + '. Autres entrées : plans.')
    # accroche du moteur dans entryPage et render
    hook = "function entryPage(){const e=EM[route.id];if(!e)return notFound();"
    assert hook in v6
    rh = "drawSidebar();closeNav();bindPage();"
    assert rh in v6
    v6 = v6.replace(rh, rh + "if(typeof MEDINA_mount==='function')MEDINA_mount();")
    stale_home = 'Les plans sont disponibles ; les développements cliniques, les monographies et les exercices corrigés ne sont pas encore rédigés pour les nouvelles entrées CIM. Aucun cours n’est déclaré complet.'
    assert stale_home in v6
    v6 = v6.replace(stale_home, 'Les cours intégrés sont accessibles par le directeur des systèmes. Les autres entrées CIM conservent leur plan ; la couverture rédactionnelle ne vaut pas validation médicale.', 1)
    # La coque d'origine renvoie #/entry/I30, K35, A41, I63 vers d'anciens modules pilotes (#/pathology/…)
    # introuvables dans le fichier autonome : un cours MEDINA existant prend la priorité.
    legacy = "if(probe.type==='entry'&&['I30','K35','A41','I63'].includes(probe.id.toUpperCase())){"
    assert v6.count(legacy) == 1
    v6 = v6.replace(legacy, "if(probe.type==='entry'&&['I30','K35','A41','I63'].includes(probe.id.toUpperCase())&&!(window.MEDINA_ALIAS||{})[probe.id.toUpperCase()]){", 1)
    rpat = "render=function(){\n  const probe=readRoute();\n"
    assert v6.count(rpat) == 1
    v6 = v6.replace(rpat, rpat + "  if(probe.type==='pathology'&&(window.MEDINA_ALIAS||{})[probe.id.toUpperCase()]){location.replace('#/entry/'+probe.id.toUpperCase());return;}\n", 1)
    body = ''; report = {}
    for code, files in chapters:
        compiled = load_course_justifications(code, ROOT + '/chapters/' + code)
        if compiled:
            transformed_files, justification_templates, justification_report = compiled
            src = ''.join(transformed_files[os.path.basename(f)] for f in files) + justification_templates
        else:
            src = ''.join(open(f).read() for f in files)
        src = transform(src)
        src = pareto_ratios(src)
        src = wrap_html(src)
        report[code] = audit(src, code)
        body += src
    css = open(ROOT + '/engine/medina_course.css').read()
    css += '\n' + open(ROOT + '/engine/justifications.css').read()
    js = open(ROOT + '/engine/medina_course.js').read()
    gl = json.dumps(G, ensure_ascii=False)
    # La politique de sécurité de la coque (style-src 'self' 'unsafe-inline') bloque Google Fonts : la feuille
    # externe n'était jamais chargée et produisait une erreur de console. Les polices du sélecteur retombent
    # sur les polices locales (Georgia, police système).
    v6 = v6.replace('</head>', '<style id="medina-course-css">' + css + '</style></head>', 1)
    alias = {}
    for code, files in chapters:
        for c in COVERS.get(code, [code]): alias[c] = code
    # Les alias sont lus par la coque dès son premier rendu : ils vont dans <head>.
    v6 = v6.replace('</head>', '<script>window.MEDINA_ALIAS=' + json.dumps(alias) + '</script></head>', 1)
    tail = body + '<script id="medina-glossary" type="application/json">' + gl.replace('</', '<\\/') + '</script><script>' + js + '</script>'
    i = v6.rindex('</body>')
    v6 = v6[:i] + tail + v6[i:]
    with open(out, 'w', encoding='utf-8') as output:
        output.write(v6)
    return report, len(v6)

COVERS = {}
if __name__ == '__main__':
    cfg = json.load(open(ROOT + '/chapters.json'))
    only = sys.argv[1:]
    chapters = []
    for c in cfg:
        code = c['code']; COVERS[code] = c.get('covers', [code])
        if only and code not in only and not c.get('integrated'): continue
        if not only and not c.get('integrated'): continue
        files = sorted(glob.glob(f'{ROOT}/chapters/{code}/*.html'))
        chapters.append((code, files))
    out = ROOT + '/MEDINA.html' if not only else ROOT + '/preview/' + '_'.join(only) + '.html'
    import os; os.makedirs(ROOT + '/preview', exist_ok=True)
    rep, size = build(chapters, out)
    print('fichier', out)
    print('taille', size)
    for c, m in rep.items():
        print(c, 'non couvertes:', len(m), ' '.join(f'{k}:{v}' for k, v in sorted(m.items())))
