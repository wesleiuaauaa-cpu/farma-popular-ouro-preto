# -*- coding: utf-8 -*-
"""Gera a imagem de compartilhamento (Open Graph / Twitter Card) 1200x630.

Fonte: recorte do hero da captura ``site-desktop.png`` (mesma arte aprovada),
sem texto novo e sem alterar a identidade visual.

Uso:  python tools/build_og_image.py
Saída: assets/og/farma-popular-ouro-preto.jpg
"""
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "site-desktop.png"
DEST = ROOT / "assets" / "og" / "farma-popular-ouro-preto.jpg"
SIZE = (1200, 630)
# Recorte do hero já aprovado, na proporção 1,91:1 exigida pelo Open Graph.
CROP = (0, 168, 760, 566)


def main():
    with Image.open(SOURCE) as src:
        image = src.convert("RGB").crop(CROP)
    image = image.resize(SIZE, Image.LANCZOS)
    DEST.parent.mkdir(parents=True, exist_ok=True)
    image.save(DEST, "JPEG", quality=88, optimize=True, progressive=True)
    print("OK  %s (%dx%d, %.0f KB)" % (DEST.relative_to(ROOT).as_posix(),
                                       SIZE[0], SIZE[1], DEST.stat().st_size / 1024))


if __name__ == "__main__":
    main()
