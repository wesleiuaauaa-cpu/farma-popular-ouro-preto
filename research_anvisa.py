# -*- coding: utf-8 -*-
"""Entrypoint de compatibilidade para a pesquisa na base da Anvisa."""
import os
import runpy
from pathlib import Path

_ROOT = Path(__file__).resolve().parent
os.environ["FARMA_PROJECT_ROOT"] = str(_ROOT)
runpy.run_path(str(_ROOT / "src" / "interface" / "research.py"), run_name="__main__")
