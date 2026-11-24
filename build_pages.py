# -*- coding: utf-8 -*-
"""Entrypoint de compatibilidade.

A implementação vive em src/application/generator.py (arquitetura hexagonal).
Este arquivo apenas define a raiz do projeto, delega a geração das páginas e
grava os arquivos de SEO/sitemap (adaptador de infraestrutura).
"""
import os
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent
os.environ["FARMA_PROJECT_ROOT"] = str(_ROOT)
sys.path.insert(0, str(_ROOT))

from src.application.generator import main  # noqa: E402
from src.infrastructure.seo import refresh_home, write_site_files  # noqa: E402

if __name__ == "__main__":
    entries = main()
    write_site_files(_ROOT, entries)
    refresh_home(_ROOT / "index.html")
