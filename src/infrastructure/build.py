# -*- coding: utf-8 -*-
"""Gera o build final em dist/, pronto para Vercel ou qualquer host estático.

Uso:  python build_site.py

O que faz:
  1. Roda build_pages.py (regenera as 26 páginas a partir do gerador).
  2. Copia para dist/ apenas o que é público: HTML, assets/ e documentação.
  3. Mantém fora do build rascunhos, screenshots e arquivos do mockup original.
"""
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(os.environ.get('FARMA_PROJECT_ROOT', Path(__file__).resolve().parents[2]))
DIST = ROOT / "dist"

PUBLIC_MD = ["README.md"]


def main():
    print("==> Regenerando paginas internas")
    subprocess.run([sys.executable, str(ROOT / "build_pages.py")], check=True, cwd=ROOT)

    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()

    pages = 0
    for f in sorted(ROOT.glob("*.html")):
        if f.name.startswith("Farma Popular"):
            continue
        shutil.copy2(f, DIST / f.name)
        pages += 1

    shutil.copytree(ROOT / "assets", DIST / "assets")

    if (ROOT / "docs").exists():
        shutil.copytree(ROOT / "docs", DIST / "docs")

    for name in PUBLIC_MD:
        src = ROOT / name
        if src.exists():
            shutil.copy2(src, DIST / name)

    print("\n==> Build concluido em dist/")
    print("    %d paginas HTML" % pages)
    print("    assets/, docs/ e documentacao Markdown inclusos")
    print("    Publicar dist/ na Vercel (vercel.json ja configurado).")


if __name__ == "__main__":
    main()
