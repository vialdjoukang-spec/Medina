#!/usr/bin/env python3
"""AIPS (Swissmedic) -> ref/fi/*.md : informations professionnelles (FI) en français.

Usage : python3 tools/aips_to_fi.py [--only REGEX] [--out ref/fi] [--xml ref/aips/AipsDownload_*.xml]
Lit le XML AIPS, retient les SmPC humains en « fr », télécharge le HTML, le convertit en Markdown,
écrit <ATC>_<nom>.md avec en-tête (titre, titulaire, ATC, substances, n° d'autorisation), puis INDEX.md.
"""
import argparse, glob, json, re, sys, time, unicodedata, urllib.request
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from bs4 import BeautifulSoup
from markdownify import markdownify

NS = {'m': 'https://simisinfo.refdata.ch/MedicinalDocuments/1.0/'}


def products(xml):
    for b in ET.parse(xml).getroot().findall('m:MedicinalDocumentsBundle', NS):
        t = lambda p: b.find(p, NS).text
        if t('m:Type') != 'SmPC' or t('m:Domain') != 'Human':
            continue
        for d in b.findall('m:AttachedDocument', NS):
            if d.find('m:Language', NS).text != 'fr':
                continue
            url = [r.find('m:Url', NS).text for r in d.findall('m:DocumentReference', NS)
                   if r.find('m:ContentType', NS).text == 'text/html']
            if url:
                yield dict(auth=[i.text for i in b.findall('m:RegulatedAuthorization/m:Identifier', NS)],
                           holder=t('m:Holder/m:Name'), name=d.find('m:Description', NS).text.strip(),
                           date=d.find('m:Period/m:Start', NS).text[:10], url=url[0])


def fetch(url):
    for i in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'medina-fi'}), timeout=90) as r:
                return r.read().decode('utf-8')
        except Exception:
            time.sleep(2 ** i)
    raise RuntimeError(url)


def section(md, start, stops):
    m = re.search(r'(?m)^' + start + r'\s*$', md)
    if not m:
        return ''
    rest = md[m.end():]
    e = re.search(r'(?m)^(?:' + '|'.join(stops) + r')\s*$', rest)
    return re.sub(r'\s+', ' ', rest[:e.start() if e else 600]).strip()


def slug(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode()
    return re.sub(r'[^A-Za-z0-9]+', '-', s).strip('-')[:80] or 'sans-nom'


def find_atc(md):
    """Codes ATC : fenêtre après « Code ATC », sinon début de « Propriétés/Effets » ; code complet (7 car.), sinon partiel."""
    full, part = r'\b[A-Z]\d{2}[A-Z]{2}\d{2}\b', r'\b[A-Z]\d{2}(?:[A-Z]{1,2})?\b'
    wins = []
    for m in re.finditer(r'Code ATC', md):
        wins.append(md[m.end():m.end() + 400])
    pe = re.search(r'(?m)^Propriétés/Effets\s*$', md)
    if pe:
        wins.append(md[pe.end():pe.end() + 1500])
    for w in wins:
        w = re.split(r"(?:M.canisme d.action|Pharmacodynamique|Propriétés physiques)", w)[0] if 'Code ATC' not in w[:0] else w
        f = list(dict.fromkeys(re.findall(full, w)))
        if f:
            return f
    for w in wins[:-1] if pe else wins:
        f = list(dict.fromkeys(re.findall(part, w[:60])))
        if f:
            return f
    return ['XXXX']


def convert(p):
    html = fetch(p['url'])
    soup = BeautifulSoup(html, 'lxml')
    for t in soup(['style', 'script', 'head']):
        t.decompose()
    md = markdownify(str(soup.body or soup), heading_style='ATX', strip=['img'])
    md = re.sub(r'[ \t]+\n', '\n', md)
    md = re.sub(r'\n{3,}', '\n\n', md).strip()
    atc = find_atc(md)
    subs = section(md, 'Principes actifs', ['Excipients.*', 'Forme pharmaceutique.*', 'Adjuvants.*']).rstrip('.') or 'n.d.'
    return p, atc, subs, md


SALTS = r"(?:chlorhydrate|hydrochlorure|sulfate|sulphate|maléate|fumarate|citrate|tartrate|acétate|succinate|mésilate|bésilate|phosphate|bromhydrate|nitrate|oxalate|lactate|gluconate|carbonate|sodique|monohydrate|dihydrate|anhydre)"


def clean_one(x):
    x = x.lower().strip(' .;')
    x = re.sub(r'\(.*?\)|\[.*?\]', ' ', x)
    x = re.sub(r'\bsous forme (?:de|d\')\s*', '', x)
    x = re.sub(r'^\s*' + SALTS + r"\s+(?:de |d')?", '', x)
    x = re.sub(r"\s+(?:" + SALTS + r")\b.*$", '', x)
    x = re.sub(r"\b(?:corresp|corr)\..*$", '', x)
    return re.sub(r'\s+', ' ', x).strip()


def latinish(x):
    return bool(re.search(r'(?:um|us|is|as|i|ae)(?:\s|$)', x)) and not re.search(r'(?:ine|ole|ide|one|ate|ol|an|il|ium)$', x.split(' ')[0])


def cands(subs):
    parts = [clean_one(x) for x in re.split(r';|,| et | \+ ', subs) if x.strip()]
    parts = [re.sub(r'(?<![i])um$', 'e', x) if ' ' not in x else x for x in parts]
    return list(dict.fromkeys(x for x in parts if x and x not in ('n.d', 'n.d.')))[:4]


def write_index(out, xmlname):
    ent = []
    for f in sorted(out.glob('*.md')):
        if f.name == 'INDEX.md': continue
        h = f.read_text(encoding='utf-8').split('---')[1]
        g = lambda k: (re.search(rf'^{k}: "?(.*?)"?$', h, re.M) or [None, ''])[1]
        ent.append(dict(subs=g('substances'), titre=g('titre'), atc=g('atc'), hold=g('titulaire'), aut=g('autorisation_swissmedic'), f=f.name))
    # DCI : vote par code ATC parmi les fiches monosubstance, en préférant les formes françaises
    vote = {}
    for e in ent:
        c = cands(e['subs'])
        e['c'] = c
        if len(c) == 1 and e['atc'] != 'XXXX':
            vote.setdefault(e['atc'].split(',')[0].strip(), []).append(c[0])
    best = {}
    for k, v in vote.items():
        fr = [x for x in v if not latinish(x)] or v
        cnt = {}
        for x in fr: cnt[x] = cnt.get(x, 0) + 1
        best[k] = sorted(cnt, key=lambda x: (-cnt[x], len(x)))[0]
    for e in ent:
        k = e['atc'].split(',')[0].strip()
        e['dci'] = best[k] if len(e['c']) <= 1 and k in best else (' + '.join(e['c']) or 'n.d.')
        e['dci'] = re.sub(r'(?<=[a-z])um$', 'e', e['dci']) if latinish(e['dci']) else e['dci']
    ent.sort(key=lambda e: (e['atc'], e['dci'], e['titre'].lower()))
    L = ['# Index des informations professionnelles (FI) suisses — français', '',
         f'Source : AIPS Swissmedic ({xmlname}). {len(ent)} FI. Trié par ATC puis DCI. DCI = nom français normalisé (sans sel ni forme), déduit automatiquement ; la colonne « Substance(s) » reproduit le libellé exact de la FI.', '',
         '| ATC | DCI | Substance(s) (libellé FI) | Produit | Titulaire | N° autorisation | Fichier |', '|---|---|---|---|---|---|---|']
    L += [f"| {e['atc']} | {e['dci']} | {e['subs']} | {e['titre']} | {e['hold']} | {e['aut']} | [{e['f']}]({e['f']}) |" for e in ent]
    (out / 'INDEX.md').write_text('\n'.join(L) + '\n', encoding='utf-8')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--only'); ap.add_argument('--out', default='ref/fi')
    ap.add_argument('--xml', default=(sorted(glob.glob('ref/aips/AipsDownload_*.xml')) or [''])[-1])
    ap.add_argument('--jobs', type=int, default=8)
    ap.add_argument('--index-only', action='store_true')
    ap.add_argument('--fix-atc', action='store_true', help='recalcule l\'ATC des fichiers XXXX_* existants (hors ligne)')
    ap.add_argument('--missing', action='store_true', help='ne traiter que les FI sans fichier existant')
    a = ap.parse_args()
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    ps = [p for p in products(a.xml) if not a.only or re.search(a.only, p['name'], re.I)]
    if a.fix_atc:
        for f in sorted(out.glob('XXXX_*.md')):
            t = f.read_text(encoding='utf-8')
            atc = find_atc(t.split('---', 2)[2])
            if atc == ['XXXX']: continue
            t = t.replace('atc: XXXX', 'atc: ' + ', '.join(atc), 1)
            g = out / (atc[0] + f.name[4:])
            f.write_text(t, encoding='utf-8'); f.rename(g)
        write_index(out, Path(a.xml).name); return
    if a.index_only:
        write_index(out, Path(a.xml).name); return
    if a.missing:
        ps = [p for p in ps if not list(out.glob(f"*_{slug(p['name'])}_{p['auth'][0]}.md"))]
    rows, fails = [], []

    def work(p):
        try:
            return convert(p)
        except Exception as e:
            fails.append((p['name'], str(e))); return None
    with ThreadPoolExecutor(a.jobs) as ex:
        for r in ex.map(work, ps):
            if not r: continue
            p, atc, subs, md = r
            fn = f"{atc[0]}_{slug(p['name'])}_{p['auth'][0]}.md"
            head = (f"---\ntitre: \"{p['name']}\"\ntitulaire: \"{p['holder']}\"\natc: {', '.join(atc)}\n"
                    f"substances: \"{subs}\"\nautorisation_swissmedic: {', '.join(p['auth'])}\n"
                    f"date_version: {p['date']}\nsource: {p['url']}\n---\n\n")
            (out / fn).write_text(head + md + '\n', encoding='utf-8')
            rows.append((subs, p['name'], atc[0], p['holder'], ', '.join(p['auth']), fn))
    write_index(out, Path(a.xml).name)
    print(f'{len(rows)} écrits, {len(fails)} échecs'); [print('ÉCHEC', *x) for x in fails]


if __name__ == '__main__':
    main()
