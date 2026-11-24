# -*- coding: utf-8 -*-
"""Resumo da situação de registros na base oficial da Anvisa (dados abertos).

Fonte: https://dados.anvisa.gov.br/dados/CONSULTAS/PRODUTOS/TA_CONSULTA_MEDICAMENTOS.CSV
Uso: levantamento de dados cadastrais verificados. Não faz parte do site.

É um adaptador de entrada (CLI): não executa nada ao ser apenas importado.
"""
import csv
import os
import sys
from collections import Counter
from pathlib import Path

csv.field_size_limit(10_000_000)


def main():
    """Lê a base baixada e grava o resumo dos registros pedidos na linha de comando."""
    path = Path(os.environ["TEMP"]) / "anvisa_medicamentos.csv"
    root = Path(os.environ.get("FARMA_PROJECT_ROOT", Path(__file__).resolve().parents[2]))
    out = root / "anvisa_research_output.txt"
    regs = set(sys.argv[1:])

    if not path.exists():
        raise SystemExit("Base nao encontrada: %s" % path)

    status = {r: Counter() for r in regs}
    samples = {}
    with path.open("r", encoding="cp1252", errors="replace", newline="") as f:
        reader = csv.reader(f, delimiter=";")
        header = next(reader)
        idx = {name: i for i, name in enumerate(header)}
        for row in reader:
            reg = row[idx["NU_REGISTRO_PRODUTO"]]
            if reg in status:
                status[reg][row[idx["VALIDADE_SITUACAO"]].strip()] += 1
                if reg not in samples:
                    samples[reg] = {h: row[idx[h]] for h in header if row[idx[h]]}

    lines = []
    for reg in regs:
        s = samples.get(reg, {})
        lines.append("=" * 70)
        lines.append("REGISTRO %s  |  situações: %s" % (reg, dict(status[reg])))
        for h in ["NO_PRODUTO", "NO_RAZAO_SOCIAL_EMPRESA", "DS_TIPO_CATEGORIA_REGULATORIA",
                  "DS_REFERENCIA", "SUBSTANCIAS_MEDICAMENTOS", "CO_TARJA",
                  "DT_VENCIMENTO_PRODUTO", "DATA_PUBLICACAO"]:
            if s.get(h):
                lines.append("  %-34s: %s" % (h, s[h]))

    out.write_text("\n".join(lines), encoding="utf-8")
    print("OK", out)


if __name__ == "__main__":
    main()
