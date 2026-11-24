# -*- coding: utf-8 -*-
"""Compatibilidade: o domínio agora vive em src/domain/legal.py."""
import os
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent
os.environ["FARMA_PROJECT_ROOT"] = str(_ROOT)
sys.path.insert(0, str(_ROOT))

from src.domain.legal import LEGAL_PAGES  # noqa: E402,F401

__all__ = ["LEGAL_PAGES"]
