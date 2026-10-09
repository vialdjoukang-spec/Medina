#!/usr/bin/env python3
"""Images .gif des cours G-04 : (a) Wikimedia Commons sous licence libre, (b) schémas dessinés (PIL).
Chaque image est enregistrée sous chapters/<CODE>/img/ avec son entrée dans img/PROVENANCE.json."""
import io, json, re, sys, urllib.parse, urllib.request
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[3]
UA = {'User-Agent': 'MEDINA-G04/1.0 (atlas pedagogique; contact via GitHub vialdjoukang-spec/Medina)'}
FREE = re.compile(r'^(CC BY(-SA)? [0-9.]+( [a-z]+)?|CC0|Public domain|PD|CC BY-SA [0-9.]+|CC-BY-SA-[0-9.]+|CC BY [0-9.]+)', re.I)

def _get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
        return r.read()

def _prov(code, entry):
    d = ROOT / 'chapters' / code / 'img'; d.mkdir(parents=True, exist_ok=True)
    p = d / 'PROVENANCE.json'
    data = json.loads(p.read_text()) if p.exists() else []
    data = [e for e in data if e['fichier'] != entry['fichier']] + [entry]
    p.write_text(json.dumps(data, ensure_ascii=False, indent=1))

def to_gif(im, out, colors=96, maxw=600, dither=True):
    im = im.convert('RGB')
    if im.width > maxw:
        im = im.resize((maxw, round(im.height * maxw / im.width)), Image.LANCZOS)
    q = im.quantize(colors=colors, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.FLOYDSTEINBERG if dither else Image.Dither.NONE)
    q.save(out, format='GIF', optimize=True)
    return out.stat().st_size

def commons(code, title, fname, colors=96, maxw=600, dither=True):
    """title = 'File:xxx.jpg' sur Wikimedia Commons. Refuse toute licence non libre."""
    api = ('https://commons.wikimedia.org/w/api.php?action=query&format=json&prop=imageinfo&iiprop=url|extmetadata&iiurlwidth=%d&titles=' % maxw) + urllib.parse.quote(title)
    page = next(iter(json.loads(_get(api))['query']['pages'].values()))
    ii = page['imageinfo'][0]; md = ii['extmetadata']
    lic = md.get('LicenseShortName', {}).get('value', '')
    if not FREE.match(lic): raise SystemExit('licence non retenue : %s (%s)' % (lic, title))
    artist = re.sub(r'<[^>]+>', '', md.get('Artist', {}).get('value', '')).strip()
    im = Image.open(io.BytesIO(_get(ii.get('thumburl') or ii['url'])))
    out = ROOT / 'chapters' / code / 'img' / fname; out.parent.mkdir(parents=True, exist_ok=True)
    size = to_gif(im, out, colors, maxw, dither)
    _prov(code, {'fichier': fname, 'type': 'Wikimedia Commons', 'source': ii['descriptionurl'], 'titre': title,
                 'auteur': artist, 'licence': lic, 'licence_url': md.get('LicenseUrl', {}).get('value', ''),
                 'modification': 'Redimensionnée (%d px de large) et convertie en GIF %d couleurs' % (min(maxw, im.width), colors), 'octets': size})
    return {'auteur': artist, 'licence': lic, 'url': ii['descriptionurl'], 'octets': size}

def credit(c):
    return f'Image : {c["auteur"]}, Wikimedia Commons, licence {c["licence"]} (<a href="{c["url"]}" target="_blank" rel="noopener">source</a>), adaptée en GIF.'

FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
FONTB = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
def font(size, bold=False):
    try: return ImageFont.truetype(FONTB if bold else FONT, size)
    except OSError: return ImageFont.load_default()

class Schema:
    # Règle d'image du propriétaire (09.10.2026) : images générées interdites.
    def __new__(cls, *a, **k): raise SystemExit('Images générées interdites (MANDATORY IMAGE RULE) : utiliser commons().')
    """Schéma dessiné, sobre, légendé ; enregistré en GIF optimisé."""
    def __init__(self, w=600, h=360, title=''):
        self.im = Image.new('RGB', (w, h), 'white'); self.d = ImageDraw.Draw(self.im); self.w, self.h = w, h
        if title: self.text(w // 2, 16, title, 15, bold=True, anchor='mm')
    def text(self, x, y, t, size=12, fill='#222', bold=False, anchor='la'):
        self.d.multiline_text((x, y), t, font=font(size, bold), fill=fill, anchor=anchor, spacing=3, align='center' if anchor[0] == 'm' else 'left')
    def save(self, code, fname, desc, colors=32):
        out = ROOT / 'chapters' / code / 'img' / fname; out.parent.mkdir(parents=True, exist_ok=True)
        q = self.im.quantize(colors=colors, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)
        q.save(out, format='GIF', optimize=True)
        _prov(code, {'fichier': fname, 'type': 'Schéma original MEDINA (dessin vectoriel PIL)', 'auteur': 'MEDINA, fragment G-04',
                     'licence': 'Œuvre originale du projet MEDINA', 'description': desc, 'octets': out.stat().st_size})
        return out.stat().st_size
