#!/usr/bin/env python3
"""Conversion des images réelles sous licence libre en GIF optimisés (aucun dessin, aucune image générée).

Chaque image source est redimensionnée et réduite à une palette ; l'attribution figure dans
PROVENANCE.json et dans la légende de la figure, jamais incrustée dans l'image.
"""
import sys
from pathlib import Path
from PIL import Image

OUT = Path(__file__).resolve().parent

def convertir(src, dest, width, colors=160):
    im = Image.open(src).convert('RGB')
    im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    im.quantize(colors=colors, method=Image.MEDIANCUT, dither=Image.FLOYDSTEINBERG).save(OUT / dest, optimize=True)
    return im.size

if __name__ == '__main__':
    src, dest, width = sys.argv[1], sys.argv[2], int(sys.argv[3])
    print(dest, convertir(src, dest, width))
