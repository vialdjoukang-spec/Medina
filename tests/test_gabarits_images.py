"""Dédoublonnage et WebP sans perte des figures des gabarits (tools/gabarits_images.py)."""
import base64
import io
import os
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools import gabarits_images as G  # noqa: E402

try:
    from PIL import Image, ImageChops, features
    WEBP = features.check('webp')
except Exception:  # pragma: no cover - dépend de l'environnement
    Image = None
    WEBP = False


def gif_palette(taille=(120, 80)):
    image = Image.new('P', taille, 0)
    image.putpalette([0, 0, 0, 255, 255, 255, 200, 30, 30] + [0] * (256 * 3 - 9))
    for x in range(taille[0]):
        for y in range(taille[1]):
            image.putpixel((x, y), (x // 7 + y // 5) % 3)
    sortie = io.BytesIO()
    image.save(sortie, 'GIF', transparency=0)
    return sortie.getvalue()


def uri(genre, octets):
    return 'data:image/%s;base64,%s' % (genre, base64.b64encode(octets).decode())


class GabaritsImages(unittest.TestCase):
    def setUp(self):
        os.environ['MEDINA_CACHE_WEBP'] = '0'

    def test_restitution_exacte_sans_webp(self):
        grande = uri('gif', os.urandom(3000))
        petite = uri('png', b'x' * 30)
        texte = ('<template id="ch-A01"><img src="%s"><img src="%s"></template>'
                 '<template data-pop="a01-x"><img src="%s"><i style="background:url(%s)"></i></template>') % (grande, petite, grande, grande)
        reduit, images, stats = G.extraire(texte, webp=False)
        self.assertEqual(G.restituer(reduit, images), texte)
        self.assertEqual(images, [grande])
        self.assertEqual(stats['occurrences'], 3)
        self.assertIn(petite, reduit)  # les petites icônes restent en place
        self.assertNotIn('base64,' + grande.split(',')[1], reduit)

    def test_jeton_preexistant_refuse(self):
        with self.assertRaises(ValueError):
            G.extraire('<p>@mdn-img-0@</p>', webp=False)

    def test_chargeur_javascript_aligne(self):
        source = (ROOT / 'build_front.py').read_text(encoding='utf-8')
        self.assertIn('t.replace(/@mdn-img-(\\\\d+)@/g', source)
        self.assertIn('id="mdn-img" type="application/json"', source)
        self.assertEqual(G.JETON % 7, '@mdn-img-7@')

    @unittest.skipUnless(WEBP, 'Pillow avec WebP requis')
    def test_webp_pixels_identiques(self):
        gif = gif_palette()
        sortie = G.optimiser_uri('gif', base64.b64encode(gif).decode(), G._pillow())
        if sortie.startswith('data:image/webp'):
            webp = base64.b64decode(sortie.split(',', 1)[1])
            avant = Image.open(io.BytesIO(gif)).convert('RGBA')
            apres = Image.open(io.BytesIO(webp)).convert('RGBA')
            self.assertIsNone(ImageChops.difference(avant, apres).getbbox())
            self.assertLess(len(webp), len(gif))
        else:
            self.assertEqual(sortie, uri('gif', gif))

    @unittest.skipUnless(WEBP, 'Pillow avec WebP requis')
    def test_animation_et_jpeg_conserves(self):
        images = [Image.new('RGB', (40, 40), c) for c in ((255, 0, 0), (0, 255, 0), (0, 0, 255))]
        tampon = io.BytesIO()
        images[0].save(tampon, 'GIF', save_all=True, append_images=images[1:], duration=100)
        self.assertIsNone(G.webp_identique(tampon.getvalue(), 'gif'))
        jpeg = io.BytesIO()
        Image.new('RGB', (40, 40), (10, 120, 200)).save(jpeg, 'JPEG')
        charge = base64.b64encode(jpeg.getvalue()).decode()
        self.assertEqual(G.optimiser_uri('jpeg', charge, G._pillow()), 'data:image/jpeg;base64,' + charge)

    @unittest.skipUnless(WEBP, 'Pillow avec WebP requis')
    def test_png_avec_profil_conserve(self):
        tampon = io.BytesIO()
        Image.new('RGB', (64, 64), (10, 20, 30)).save(tampon, 'PNG', icc_profile=b'\0' * 128)
        self.assertIsNone(G.webp_identique(tampon.getvalue(), 'png'))


class PolicesPartagees(unittest.TestCase):
    def test_defaut_incorpore_et_partage_relatif(self):
        from tools import polices_partagees as P
        ancien = os.environ.pop('MEDINA_POLICES_PARTAGEES', None)
        try:
            self.assertTrue(P.url_police(ROOT, 'shell/fonts/ahn-400.woff2', 1).startswith('data:font/woff2;base64,'))
            os.environ['MEDINA_POLICES_PARTAGEES'] = '1'
            self.assertEqual(P.url_police(ROOT, 'shell/fonts/ahn-400.woff2', 1), '../polices/ahn-400.woff2')
            self.assertEqual(P.url_police(ROOT, 'assets/fonts/AnthropicSerif-Roman-Web.woff2', 0), 'polices/AnthropicSerif-Roman-Web.woff2')
            with self.assertRaises(ValueError):
                P.url_police(ROOT, 'shell/fonts/inconnue.woff2', 0)
        finally:
            os.environ.pop('MEDINA_POLICES_PARTAGEES', None)
            if ancien is not None:
                os.environ['MEDINA_POLICES_PARTAGEES'] = ancien


if __name__ == '__main__':
    unittest.main()
