#!/usr/bin/env python3
"""Images GIF optimisées de I-03-Infectiologie (toutes les leçons de la spécialité).

Une seule famille :
- photographies sous licence libre (Wikimedia Commons), téléchargées depuis leur page
  officielle, recadrées et réduites en GIF à palette adaptative ; attribution dans ATTRIBUTIONS.json ;
Règle du propriétaire : aucune image générée ; uniquement des images réelles sous licence libre.
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
 'a04_cdifficile_gram.gif': ('Clostridium difficile .jpg', None, (400, 64)),
 'a04_colite_pseudomembraneuse_endoscopie.gif': ('Pseudomembranous colitis 1.jpg', None, (400, 64)),
 'a04_colite_pseudomembraneuse_macro.gif': ('Clostridioides (pseudomembranous) colitis.jpg', None, (400, 64)),
 'a04_colite_pseudomembraneuse_tdm.gif': ('Pseudomembranoese Colitis axial.jpg', None, (400, 64)),
 'a09_campylobacter_meb.gif': ('Campylobacter jejuni 01.jpg', None, (400, 64)),
 'a15_radiographie_tuberculose.gif': ('Tuberculosis-x-ray-1.jpg', None, (400, 64)),
 'a15_ziehl_neelsen.gif': ('Mycobacterium tuberculosis Ziehl-Neelsen stain 02.jpg', None, (400, 64)),
 'a46_anatomie_peau.gif': ('Blausen 0810 SkinAnatomy 01.png', None, (460, 96)),
 'a46_erysipele_jambe.gif': ('Érysipèle jambe- Leg erysipelas.jpg', None, (400, 64)),
 'a46_erysipele_recidivant.gif': ('Recurrent erysipelas on edematous leg.jpg', (0, 0.25, 1, 0.95), (400, 64)),
 'a49_staphylocoque_gram.gif': ('Staphylococcus aureus Gram.jpg', None, (400, 64)),
 'a69_borrelia_fond_noir.gif': ('Borrelia burgdorferi (CDC-PHIL -6631) lores.jpg', None, (400, 64)),
 'a69_erytheme_migrant.gif': ('Erythema migrans - erythematous rash in Lyme disease - PHIL 9875.jpg', None, (400, 64)),
 'a69_ixodes_ricinus.gif': ('Ixodes ricinus on dry grass.jpg', None, (400, 64)),
 'a69_lymphocytome.gif': ('Borrelial lymphocytoma 1.jpg', (0, 0.1, 1, 0.85), (400, 64)),
 'b00_herpes_labial.gif': ('Herpes labialis.jpg', None, (400, 64)),
 'b00_tzanck.gif': ('Tzanck test.png', None, (400, 64)),
 'b02_zona_thorax.gif': ('Shingles on the chest.jpg', None, (400, 64)),
 'b02_zona_vesicules.gif': ('Herpetic shingles.jpg', None, (400, 64)),
 'b07_verrue_histologie.gif': ('Verruca vulgaris - intermed mag.jpg', (0, 0.3, 1, 0.7), (400, 64)),
 'b07_verrue_vulgaire.gif': ('Verruca vulgaris.jpg', None, (400, 64)),
 'b35_intertrigo_interdigital.gif': ('Tinea-pedis-interdigital-Sean.jpg', None, (400, 64)),
 'b35_tinea_corporis.gif': ('Ringworm on the arm, or tinea corporis due to Trichophyton mentagrophytes PHIL 2938 lores.jpg', None, (400, 64)),
 'b37_candidose_pseudomembraneuse.gif': ('CandidiasisFromCDCinJPEG03-18-06.JPG', None, (400, 64)),
 'b37_muguet.gif': ('Oral thrush Aphthae Candida albicans. PHIL 1217 lores.jpg', None, (400, 64)),
 'b50_falciparum_anneaux.gif': ('Plasmodium falciparum (malaria) parasite in blood.jpg', None, (400, 64)),
 'b50_falciparum_gametocytes.gif': ('Plasmodium falciparum 01.png', None, (400, 64)),
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


if __name__ == '__main__':
    attributions = json.load(open(os.path.join(HERE, 'ATTRIBUTIONS.json')))
    for out, (title, crop, (width, colors)) in PHOTOS.items():
        raw, meta = commons(title)
        tmp = '/tmp/_photo.img'; open(tmp, 'wb').write(raw); im = Image.open(tmp)
        if crop: im = im.crop((int(crop[0] * im.width), int(crop[1] * im.height), int(crop[2] * im.width), int(crop[3] * im.height)))
        size = to_gif(im, os.path.join(HERE, out), width, colors)
        keep = {k: attributions.get(out, {}).get(k) for k in ('auteur',) if out in attributions}
        attributions[out] = dict(meta, **{k: v for k, v in keep.items() if v}, fichier_commons=title, type='photographie', dimensions=list(size),
                                 modification='recadrage éventuel, réduction et conversion en GIF à palette de %d couleurs' % colors,
                                 octets=os.path.getsize(os.path.join(HERE, out)))
    json.dump(attributions, open(os.path.join(HERE, 'ATTRIBUTIONS.json'), 'w'), ensure_ascii=False, indent=1)
    for k, v in attributions.items(): print(k, v['octets'], v.get('licence'))
