# -*- coding: utf-8 -*-
"""Verificação rápida de links e arquivos locais do site (adaptador de infraestrutura)."""
import os
import re
from pathlib import Path


def main():
    root = Path(os.environ.get("FARMA_PROJECT_ROOT", Path(__file__).resolve().parents[2]))
    files = sorted(p for p in root.glob("*.html") if not p.name.startswith("Farma Popular"))
    print("Páginas publicadas: %d" % len(files))
    for p in files:
        print(" -", p.name)

    bad, missing = [], []
    for p in files:
        s = p.read_text(encoding="utf-8")
        if 'href="#"' in s:
            bad.append(p.name)
        for m in re.finditer(r'(?:href|src)="([^"]+)"', s):
            u = m.group(1)
            if u.startswith(("#", "http", "mailto:", "tel:", "data:")):
                continue
            u = u.split("?")[0].split("#")[0]
            if u and not (root / u).exists():
                missing.append((p.name, u))

    print("\nhref=\"#\" restantes:", bad or "nenhum")
    print("Arquivos locais inexistentes:", missing or "nenhum")

    print("\nProdutos ilustrativos por página:")
    for p in files:
        n = p.read_text(encoding="utf-8").count('class="product"')
        if n:
            print(" - %s: %d" % (p.name, n))

    print("\nLinks WhatsApp (data-wa) por página:")
    for p in files:
        n = p.read_text(encoding="utf-8").count("data-wa ")
        if n:
            print(" - %s: %d" % (p.name, n))


if __name__ == "__main__":
    main()
