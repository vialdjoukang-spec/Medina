#!/usr/bin/env python3
"""Figures GIF de la cardiologie (C-01) : schémas originaux et photographies sous licence libre.

Les schémas sont dessinés ici (PIL) à partir des définitions citées dans les cours ;
ils sont pédagogiques et ne reproduisent aucune figure publiée. Les photographies
viennent de Wikimedia Commons (licences dans PROVENANCE.json), redimensionnées et
converties en GIF optimisé. Usage : python3 generer_figures.py <jpg_raynaud> <jpg_lymphoedeme>
"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parent
F = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
FB = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
def font(size, bold=False):
    return ImageFont.truetype(FB if bold else F, size)

INK = (34, 34, 34)
GREY = (120, 120, 120)
BG = (255, 255, 255)

def photo(src, dest, width, credit):
    im = Image.open(src).convert('RGB')
    ratio = width / im.width
    im = im.resize((width, int(im.height * ratio)), Image.LANCZOS)
    band = 22
    canvas = Image.new('RGB', (im.width, im.height + band), BG)
    canvas.paste(im, (0, 0))
    d = ImageDraw.Draw(canvas)
    d.text((6, im.height + 4), credit, font=font(11), fill=GREY)
    canvas.quantize(colors=128, method=Image.MEDIANCUT, dither=Image.FLOYDSTEINBERG).save(OUT / dest, optimize=True)

def finger(d, x, y, w, h, tip_color, base_color, split):
    """Doigt stylisé : la partie distale (au-dessus de split) prend la couleur de la phase."""
    d.rounded_rectangle((x, y, x + w, y + h), radius=w // 2, fill=base_color, outline=INK, width=2)
    d.rounded_rectangle((x, y, x + w, y + split), radius=w // 2, fill=tip_color, outline=INK, width=2)
    d.line((x + 3, y + split, x + w - 3, y + split), fill=INK, width=2)

def raynaud_phases():
    skin = (232, 196, 170)
    phases = [
        ('Repos', 'Perfusion digitale normale', skin, ''),
        ('1. Pâleur (ischémie)', 'Vasospasme des artères digitales : limite nette, engourdissement', (246, 246, 242), 'obligatoire pour le diagnostic'),
        ('2. Cyanose (désoxygénation)', 'Sang veineux immobile, désaturé', (128, 140, 196), 'inconstante'),
        ('3. Rougeur (hyperhémie réactive)', 'Retour du flux : rougeur, paresthésies, douleur', (214, 92, 84), 'inconstante'),
    ]
    frames = []
    for title, sub, col, note in phases:
        im = Image.new('RGB', (560, 370), BG)
        d = ImageDraw.Draw(im)
        d.text((20, 14), 'Phénomène de Raynaud : séquence d’une crise', font=font(17, True), fill=INK)
        d.text((20, 42), title, font=font(16, True), fill=INK)
        d.text((20, 66), sub, font=font(13), fill=INK)
        if note:
            d.text((20, 86), 'Phase ' + note, font=font(12), fill=GREY)
        # paume et quatre doigts ; le pouce est épargné
        d.rounded_rectangle((150, 260, 390, 345), radius=18, fill=skin, outline=INK, width=2)
        for i, (hh, sp) in enumerate([(110, 60), (125, 70), (118, 64), (95, 52)]):
            finger(d, 160 + i * 58, 270 - hh, 46, hh + 10, col, skin, sp)
        d.rounded_rectangle((395, 280, 437, 340), radius=20, fill=skin, outline=INK, width=2)
        d.text((444, 300), 'pouce souvent\népargné', font=font(11), fill=GREY)
        d.text((20, 352), 'Schéma pédagogique MEDINA d’après ESVM 2017', font=font(10), fill=GREY)
        frames.append(im.quantize(colors=32))
    frames[0].save(OUT / 'i73_raynaud_phases.gif', save_all=True, append_images=frames[1:],
                   duration=[1400, 2200, 2200, 2200], loop=0, optimize=True)

def axes(d, x0, y0, x1, y1):
    d.line((x0, y1, x1, y1), fill=INK, width=2)
    d.line((x0, y0, x0, y1), fill=INK, width=2)

def orthostatic():
    W, H = 700, 470
    im = Image.new('RGB', (W, H), BG)
    d = ImageDraw.Draw(im)
    d.text((20, 12), 'Pression systolique après le passage debout : trois profils (ESC 2018)', font=font(16, True), fill=INK)
    x0, x1, yb = 70, 660, 330
    axes(d, x0, 60, x1, yb)
    # échelle : 0 à 8 minutes ; 120 mmHg en haut de référence
    def X(t): return x0 + (t / 8.0) * (x1 - x0)
    def Y(p): return yb - (p - 60) * 2.6
    for p in (80, 100, 120):
        d.line((x0 - 5, Y(p), x0, Y(p)), fill=INK, width=2)
        d.text((22, Y(p) - 8), str(p), font=font(12), fill=INK)
    for t in (0, 1, 2, 3, 4, 6, 8):
        d.line((X(t), yb, X(t), yb + 5), fill=INK, width=2)
        d.text((X(t) - 4, yb + 8), str(t), font=font(12), fill=INK)
    d.text((W // 2 - 60, yb + 28), 'minutes debout', font=font(12), fill=INK)
    d.text((8, 44), 'mmHg', font=font(12), fill=INK)
    d.line((X(3), 60, X(3), yb), fill=GREY, width=1)
    d.text((X(3) + 4, 62), '3 min', font=font(11), fill=GREY)
    d.line((X(0), 60, X(0), yb), fill=GREY, width=1)
    d.text((X(0) + 4, 62), 'lever', font=font(11), fill=GREY)
    base = 120
    def curve(pts, col, w=3, dash=False):
        pts = [(X(t), Y(p)) for t, p in pts]
        for a, b in zip(pts, pts[1:]):
            d.line((a, b), fill=col, width=w)
    # initiale : chute > 40 en < 15 s, retour < 40 s
    curve([(-0.0, base), (0.1, 76), (0.25, 82), (0.6, 118), (8, 119)], (40, 40, 40))
    # classique : chute soutenue >= 20 dans les 3 min
    curve([(0, base), (0.5, 108), (1.5, 98), (3, 94), (8, 92)], (180, 60, 50))
    # retardée : déclin lent au-delà de 3 min
    curve([(0, base), (3, 114), (5, 104), (8, 92)], (60, 90, 170))
    d.line((X(0), Y(100), x1, Y(100)), fill=(200, 200, 200), width=1)
    d.text((X(6.1), Y(100) - 16), 'seuil : baisse de 20', font=font(11), fill=GREY)
    ly = 392
    for col, txt in [((40, 40, 40), 'Initiale : chute > 40 mmHg en 15 s, retour spontané en moins de 40 s'),
                     ((180, 60, 50), 'Classique : baisse soutenue ≥ 20 mmHg (ou < 90 mmHg) dans les 3 minutes'),
                     ((60, 90, 170), 'Retardée : déclin lent et progressif au-delà de 3 minutes')]:
        d.line((30, ly + 8, 60, ly + 8), fill=col, width=3)
        d.text((68, ly), txt, font=font(12), fill=INK)
        ly += 22
    d.text((W - 300, H - 16), 'Schéma pédagogique MEDINA, valeurs illustratives', font=font(10), fill=GREY)
    im.quantize(colors=32).save(OUT / 'i95_profils_orthostatiques.gif', optimize=True)

def lymph_balance():
    W, H = 700, 360
    im = Image.new('RGB', (W, H), BG)
    d = ImageDraw.Draw(im)
    d.text((20, 12), 'Lymphoedème : charge lymphatique et capacité de transport', font=font(16, True), fill=INK)
    # capillaire sanguin
    d.rounded_rectangle((30, 70, 670, 110), radius=20, fill=(236, 200, 200), outline=INK, width=2)
    d.text((40, 80), 'Capillaire sanguin : filtration d’eau et de protéines plasmatiques', font=font(12), fill=INK)
    for x in range(120, 640, 90):
        d.line((x, 112, x, 150), fill=INK, width=2)
        d.polygon([(x - 5, 144), (x + 5, 144), (x, 154)], fill=INK)
    d.rectangle((30, 158, 670, 230), outline=GREY, width=1)
    d.text((40, 166), 'Interstitium : la charge lymphatique (eau, protéines, cellules)', font=font(12), fill=INK)
    d.text((40, 186), 'doit être évacuée ; les protéines ne retournent au sang que par la lymphe', font=font(12), fill=INK)
    for x in range(120, 640, 90):
        d.line((x, 232, x, 262), fill=INK, width=2)
        d.polygon([(x - 5, 256), (x + 5, 256), (x, 266)], fill=INK)
    d.rounded_rectangle((30, 270, 670, 305), radius=16, fill=(214, 228, 214), outline=INK, width=2)
    d.text((40, 279), 'Vaisseaux lymphatiques : capacité de transport', font=font(12), fill=INK)
    d.text((30, 318), 'Lymphoedème = capacité de transport inférieure à la charge (ISL 2023) : accumulation riche en protéines,', font=font(11), fill=INK)
    d.text((30, 334), 'puis fibrose et dépôt adipeux (stades II–III). Schéma pédagogique MEDINA.', font=font(11), fill=INK)
    im.quantize(colors=32).save(OUT / 'i89_charge_transport.gif', optimize=True)

def lymph_histo():
    """Coupe cutanée schématique : peau normale et lymphoedème avancé (stades II-III), d'après la S2k 2017."""
    import random
    random.seed(7)
    W, H = 900, 450
    im = Image.new('RGB', (W, H), BG); d = ImageDraw.Draw(im)
    d.text((20, 12), 'Peau : normale et lymphoedème avancé (stades II–III)', font=font(17, True), fill=(30, 30, 30))
    def panel(x0, w, thick, title):
        d.text((x0, 44), title, font=font(14, True), fill=(30, 30, 30))
        y = 72; marks = {}
        ker = 14 if thick else 5
        d.rectangle([x0, y, x0 + w, y + ker], fill=(214, 190, 150)); marks['ker'] = y + ker // 2
        y += ker
        epi = 22 if thick else 16
        d.rectangle([x0, y, x0 + w, y + epi], fill=(226, 170, 160))
        if thick:
            for i in range(x0, x0 + w - 21, 22):
                d.polygon([(i, y + epi), (i + 22, y + epi), (i + 11, y + epi + 12)], fill=(226, 170, 160))
        marks['epi'] = y + epi // 2
        y += epi
        cor = 130 if thick else 70
        d.rectangle([x0, y, x0 + w, y + cor], fill=(244, 214, 214))
        if thick:
            for i in range(x0, x0 + w - 21, 22):
                d.polygon([(i, y), (i + 22, y), (i + 11, y + 12)], fill=(226, 170, 160))
        n = 80 if thick else 22
        for _ in range(n):
            a_ = random.randint(x0 + 4, x0 + w - 40); b_ = random.randint(y + 16, y + cor - 6)
            d.line([(a_, b_), (a_ + random.randint(18, 34), b_ + random.randint(-4, 4))], fill=(150, 90, 120), width=2 if thick else 1)
        cx, cy = x0 + w - 70, y + cor // 2
        r = 20 if thick else 7
        d.ellipse([cx - r, cy - int(r * 0.7), cx + r, cy + int(r * 0.7)], outline=(40, 90, 170), width=2, fill=(220, 235, 250))
        marks['cor'] = y + 22; marks['lym'] = cy + 6
        y += cor
        sub = 130 if thick else 90
        d.rectangle([x0, y, x0 + w, y + sub], fill=(250, 238, 200))
        cell = 16 if thick else 22
        for i in range(x0 + 4, x0 + w - cell - 2, cell + 4):
            for j in range(y + 4, y + sub - cell - 2, cell + 4):
                d.ellipse([i, j, i + cell, j + cell], outline=(210, 180, 110))
        marks['sub'] = y + sub // 2
        return marks
    panel(20, 250, False, 'Normale')
    m = panel(310, 300, True, 'Lymphoedème avancé')
    f = font(12)
    labels = [('ker', 'hyperkératose'), ('epi', 'épiderme hyperplasique, papillomatose'), ('cor', 'derme épaissi, fibrose :'), ('lym', 'vaisseau lymphatique ectasique'), ('sub', 'tissu adipeux sous-cutané accru')]
    for k, t in labels:
        yy = m[k]
        d.line([(612, yy), (628, yy)], fill=(60, 60, 60), width=1)
        d.text((632, yy - 7), t, font=f, fill=(40, 40, 40))
    d.text((632, m['cor'] + 8), 'collagène de types I et III', font=f, fill=(40, 40, 40))
    d.text((20, 412), 'Schéma pédagogique original MEDINA d’après la ligne directrice S2k 2017 (modifications cutanées des stades II et III) ;', font=font(11), fill=GREY)
    d.text((20, 428), 'épaisseurs non à l’échelle.', font=font(11), fill=GREY)
    im.quantize(colors=48).save(OUT / 'i89_histologie_peau.gif', optimize=True)

if __name__ == '__main__':
    raynaud_phases(); orthostatic(); lymph_balance(); lymph_histo()
    if len(sys.argv) > 2:
        photo(sys.argv[1], 'i73_raynaud_photo.gif', 420, 'Wikimedia Commons, knotimpressed, CC0')
        photo(sys.argv[2], 'i89_lymphoedeme_photo.gif', 360, 'Wikimedia Commons, Wesalius, CC BY-SA 4.0')
