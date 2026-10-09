#!/usr/bin/env python3
"""Images GIF optimisées de I-03-Infectiologie (A04, A46, A69).

Deux familles :
- photographies sous licence libre (Wikimedia Commons), téléchargées depuis leur page
  officielle, recadrées et réduites en GIF à palette adaptative ; attribution dans ATTRIBUTIONS.json ;
- schémas originaux dessinés ici (PIL), en noir, gris et un accent, légendés en français.
Usage : python3 assets/img/infectiologie/build_images.py  (réseau requis pour les photographies)
"""
import json, os, re, urllib.parse, urllib.request
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
UA = {'User-Agent': 'MEDINA/1.0 (atlas pedagogique ; contact via github.com/vialdjoukang-spec/Medina)'}
F = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
FB = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
def font(size, bold=False): return ImageFont.truetype(FB if bold else F, size)

PHOTOS = {
 'a69_erytheme_migrant.gif': ('Erythema migrans - erythematous rash in Lyme disease - PHIL 9875.jpg', None),
 'a69_borrelia_fond_noir.gif': ('Borrelia burgdorferi (CDC-PHIL -6631) lores.jpg', None),
 'a46_erysipele_recidivant.gif': ('Recurrent erysipelas on edematous leg.jpg', (0, 0.25, 1, 0.95)),
 'a46_erysipele_jambe.gif': ('Érysipèle jambe- Leg erysipelas.jpg', None),
 'a04_colite_pseudomembraneuse_macro.gif': ('Clostridioides (pseudomembranous) colitis.jpg', None),
 'a04_colite_pseudomembraneuse_endoscopie.gif': ('Pseudomembranous colitis 1.jpg', None),
 'a04_colite_pseudomembraneuse_tdm.gif': ('Pseudomembranoese Colitis axial.jpg', None),
}

def commons(title):
    u = ('https://commons.wikimedia.org/w/api.php?action=query&format=json&prop=imageinfo'
         '&iiprop=url|extmetadata&iiurlwidth=900&titles=' + urllib.parse.quote('File:' + title))
    d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=60))
    ii = list(d['query']['pages'].values())[0]['imageinfo'][0]; m = ii['extmetadata']
    g = lambda k: re.sub(r'<[^>]+>', '', m.get(k, {}).get('value', '')).strip()
    raw = urllib.request.urlopen(urllib.request.Request(ii.get('thumburl', ii['url']), headers=UA), timeout=60).read()
    return raw, {'source': ii['descriptionurl'], 'licence': g('LicenseShortName'), 'licence_url': g('LicenseUrl'),
                 'auteur': re.sub(r'\s+', ' ', g('Artist'))[:160], 'description_originale': g('ImageDescription')[:300]}

def to_gif(im, path, width=400, colors=64, dither=True):
    im = im.convert('RGB')
    if im.width > width: im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    im.quantize(colors=colors, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.FLOYDSTEINBERG if dither else Image.Dither.NONE).save(path, optimize=True)
    return im.size

def text_center(d, xy, s, f, fill='#111'):
    w = d.textlength(s, font=f); d.text((xy[0] - w / 2, xy[1]), s, font=f, fill=fill)

def schema_lyme(path):
    W, H = 920, 470; im = Image.new('RGB', (W, H), 'white'); d = ImageDraw.Draw(im)
    text_center(d, (W / 2, 14), 'Borréliose de Lyme : délai d’apparition après la piqûre', font(24, True))
    text_center(d, (W / 2, 46), 'Barre grise = extrêmes rapportés ; trait noir = délai typique ou médian (SSI, 2025)', font(15), '#444')
    # axe logarithmique en jours : 1 j -> 1000 j
    import math
    x0, x1 = 300, 890
    X = lambda j: x0 + (x1 - x0) * math.log10(j) / 3
    rows = [('Érythème migrant', 3, 32, 7, 7, 'précoce localisée'),
            ('Lymphocytome bénin', 1, 60, None, None, 'précoce disséminée'),
            ('Cardite (bloc AV)', 4, 210, 21, 21, 'précoce disséminée'),
            ('Arthrite de Lyme', 14, 730, 120, 180, 'tardive'),
            ('Acrodermatite atrophiante', 180, 900, None, None, 'tardive (stade final > 6 mois)')]
    y = 92
    for name, a, b, t1, t2, stage in rows:
        d.text((16, y + 2), name, font=font(17, True), fill='#111'); d.text((16, y + 24), stage, font=font(13), fill='#555')
        d.rounded_rectangle((X(a), y + 8, X(b), y + 30), radius=6, fill='#d9d9d9', outline='#888')
        if t1: d.rectangle((X(t1) - 2, y + 2, X(t2) + 2, y + 36), fill='#111')
        y += 62
    yA = y + 6; d.line((x0, yA, x1, yA), fill='#111', width=2)
    for j, lab in [(1, '1 j'), (7, '1 sem.'), (30, '1 mois'), (180, '6 mois'), (365, '1 an'), (730, '2 ans')]:
        d.line((X(j), yA - 6, X(j), yA + 6), fill='#111', width=2); text_center(d, (X(j), yA + 10), lab, font(14))
    d.text((16, H - 34), 'Lymphocytome : « dans les deux mois » ; acrodermatite : stade atrophique au-delà de 6 mois. Échelle logarithmique.', font=font(13), fill='#444')
    im.save('/tmp/_s.png'); return to_gif(im, path, width=760, colors=32, dither=False)

def schema_peau(path):
    W, H = 920, 500; im = Image.new('RGB', (W, H), 'white'); d = ImageDraw.Draw(im)
    text_center(d, (W / 2, 12), 'Profondeur de l’infection : érysipèle, cellulite, fasciite nécrosante', font(23, True))
    layers = [('Épiderme', 70, 100, '#f2f2f2'), ('Derme superficiel', 100, 170, '#e2e2e2'), ('Derme profond', 170, 240, '#cfcfcf'),
              ('Hypoderme (tissu adipeux)', 240, 340, '#f7f3e6'), ('Fascia', 340, 365, '#9a9a9a'), ('Muscle', 365, 450, '#bdbdbd')]
    for name, a, b, c in layers:
        d.rectangle((30, a, 520, b), fill=c, outline='#777'); d.text((40, a + 4), name, font=font(15, True), fill='#111')
    def bracket(x, a, b, label, sub, col):
        d.line((x, a, x, b), fill=col, width=6); d.line((x - 10, a, x + 10, a), fill=col, width=4); d.line((x - 10, b, x + 10, b), fill=col, width=4)
    bracket(560, 100, 170, '', '', '#b00020'); bracket(600, 170, 340, '', '', '#d35400'); bracket(640, 340, 450, '', '', '#111')
    d.text((680, 102), 'Érysipèle', font=font(18, True), fill='#b00020')
    d.text((680, 126), 'derme superficiel, bord net', font=font(14), fill='#333'); d.text((680, 146), 'streptocoque β-hémolytique A', font=font(14), fill='#333')
    d.text((680, 214), 'Cellulite', font=font(18, True), fill='#d35400')
    d.text((680, 238), 'derme profond + hypoderme', font=font(14), fill='#333'); d.text((680, 258), 'bord diffus ; streptocoques,', font=font(14), fill='#333'); d.text((680, 276), 'Staphylococcus aureus', font=font(14), fill='#333')
    d.text((680, 360), 'Fasciite nécrosante', font=font(18, True), fill='#111')
    d.text((680, 384), 'fascia et muscle ; urgence', font=font(14), fill='#333'); d.text((680, 404), 'chirurgicale ; infection', font=font(14), fill='#333'); d.text((680, 424), 'polymicrobienne', font=font(14), fill='#333')
    d.text((30, H - 40), 'Schéma original d’après le tableau de la SSI « Infections non purulentes de la peau et des tissus mous » (validée le 30 juin 2025).', font=font(13), fill='#444')
    return to_gif(im, path, width=760, colors=48, dither=False)

def schema_cdi(path):
    W, H = 920, 560; im = Image.new('RGB', (W, H), 'white'); d = ImageDraw.Draw(im)
    text_center(d, (W / 2, 12), 'Clostridioides difficile : algorithme microbiologique en deux temps', font(21, True))
    def box(x, y, w, h, t, sub='', fill='#f2f2f2', bold=True):
        d.rounded_rectangle((x, y, x + w, y + h), radius=10, fill=fill, outline='#333', width=2)
        text_center(d, (x + w / 2, y + 10), t, font(16, bold))
        if sub:
            for i, s in enumerate(sub.split('\n')): text_center(d, (x + w / 2, y + 34 + 19 * i), s, font(13, False), '#333')
    def arrow(a, b, lab=''):
        d.line((a, b), fill='#111', width=3); import math
        ang = math.atan2(b[1] - a[1], b[0] - a[0])
        for s in (-0.45, 0.45): d.line((b, (b[0] - 14 * math.cos(ang + s), b[1] - 14 * math.sin(ang + s))), fill='#111', width=3)
        if lab: d.text(((a[0] + b[0]) / 2 + 8, (a[1] + b[1]) / 2 - 10), lab, font=font(14, True), fill='#b00020')
    box(260, 52, 400, 74, 'Selles diarrhéiques (Bristol 6 à 7, ≥ 3/24 h)', 'tableau compatible, aucun autre diagnostic')
    box(310, 160, 300, 64, 'Étape 1 : antigène GDH', 'glutamate déshydrogénase (dépistage)')
    arrow((460, 126), (460, 160))
    box(30, 262, 260, 70, 'GDH négative', 'l’algorithme ne confirme pas\nC. difficile', fill='#ffffff', bold=True)
    arrow((330, 224), (200, 262), 'négatif')
    box(500, 262, 400, 64, 'Étape 2 : toxines A et B', 'immuno-enzymatique ou immunochromatographie')
    arrow((590, 224), (680, 262), 'positif')
    box(430, 380, 220, 84, 'Toxines positives', 'argument d’infection\nactive (avec la clinique)', fill='#e8e8e8')
    box(680, 380, 220, 84, 'Toxines négatives', 'discordance : TAAN possible ;\nTAAN seul = colonisation ?', fill='#ffffff')
    arrow((630, 326), (540, 380), 'positif'); arrow((760, 326), (790, 380), 'négatif')
    d.text((30, 490), 'TAAN : test d’amplification des acides nucléiques. Utilisé seul, il peut détecter une colonisation plutôt qu’une infection ;', font=font(13), fill='#444')
    d.text((30, 510), 'la recherche de toxines lui confère sa spécificité. Schéma original d’après la SSI « Infection à Clostridioides difficile », 17 avril 2026.', font=font(13), fill='#444')
    return to_gif(im, path, width=760, colors=32, dither=False)

if __name__ == '__main__':
    attributions = {}
    for out, (title, crop) in PHOTOS.items():
        raw, meta = commons(title)
        tmp = '/tmp/_photo.jpg'; open(tmp, 'wb').write(raw); im = Image.open(tmp)
        if crop: im = im.crop((int(crop[0] * im.width), int(crop[1] * im.height), int(crop[2] * im.width), int(crop[3] * im.height)))
        size = to_gif(im, os.path.join(HERE, out))
        attributions[out] = dict(meta, fichier_commons=title, type='photographie', dimensions=list(size),
                                 modification='recadrage éventuel, réduction et conversion en GIF à palette de 64 couleurs')
    for out, fn, what in [('a69_stades_delais.gif', schema_lyme, 'schéma original'), ('a46_profondeur_peau.gif', schema_peau, 'schéma original'),
                          ('a04_algorithme_diagnostic.gif', schema_cdi, 'schéma original')]:
        size = fn(os.path.join(HERE, out))
        attributions[out] = {'type': what, 'auteur': 'MEDINA, I-03-Infectiologie', 'licence': 'Création originale du projet MEDINA',
                             'dimensions': list(size), 'source': 'données des directives SSI citées dans la légende'}
    for k in attributions: attributions[k]['octets'] = os.path.getsize(os.path.join(HERE, k))
    json.dump(attributions, open(os.path.join(HERE, 'ATTRIBUTIONS.json'), 'w'), ensure_ascii=False, indent=1)
    for k, v in attributions.items(): print(k, v['octets'], v.get('licence'))
