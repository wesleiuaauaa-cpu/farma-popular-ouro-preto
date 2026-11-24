# -*- coding: utf-8 -*-
"""Servidor local que imita as URLs limpas da Vercel (cleanUrls).

Sem isto, ``python -m http.server`` não encontra /sobre quando o arquivo é
sobre.html. Este script resolve o caminho com e sem extensão, servindo dist/.

Uso:  python serve.py [porta]
"""
import argparse
import http.server
import os
from functools import partial
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PUBLIC = ROOT / "dist" if (ROOT / "dist").is_dir() else ROOT


class CleanURLHandler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        resolved = Path(super().translate_path(path))
        if resolved.is_file():
            return str(resolved)
        if not resolved.suffix:
            with_html = Path(str(resolved) + ".html")
            if with_html.is_file():
                return str(with_html)
        if resolved.is_dir():
            index = resolved / "index.html"
            if index.is_file():
                return str(index)
        return str(resolved)

    def log_message(self, fmt, *args):  # noqa: A003 - assinatura da stdlib
        print("%s - %s" % (self.address_string(), fmt % args))


def main():
    parser = argparse.ArgumentParser(description="Preview local com URLs limpas")
    parser.add_argument("porta", nargs="?", type=int, default=8765)
    args = parser.parse_args()

    handler = partial(CleanURLHandler, directory=str(PUBLIC))
    with http.server.ThreadingHTTPServer(("127.0.0.1", args.porta), handler) as httpd:
        print("Servindo %s em http://127.0.0.1:%d/" % (PUBLIC.name, args.porta))
        print("Ctrl+C para encerrar.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nEncerrado.")


if __name__ == "__main__":
    main()
