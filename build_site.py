# -*- coding: utf-8 -*-
"""Entrypoint de compatibilidade.

A implementação vive em src/infrastructure/build.py (arquitetura hexagonal).
Este arquivo apenas define a raiz do projeto e delega a execução.
"""
import os
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent
os.environ["FARMA_PROJECT_ROOT"] = str(_ROOT)
sys.path.insert(0, str(_ROOT))

from src.infrastructure.build import main  # noqa: E402

if __name__ == "__main__":
    main()
