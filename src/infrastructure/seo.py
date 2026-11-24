# -*- coding: utf-8 -*-
"""Adaptador de infraestrutura: grava sitemap.xml/robots.txt e injeta o bloco
de SEO na home, que é mantida à mão (fora do gerador).

Somente I/O: toda a decisão de conteúdo/URL vive em ``src/domain/seo.py``.
"""
import re
from pathlib import Path

from src.domain import seo

SEO_START = "<!-- seo:start -->"
SEO_END = "<!-- seo:end -->"

_TITLE_RE = re.compile(r"<title>.*?</title>", re.S)
_DESC_RE = re.compile(r'<meta name="description" content="[^"]*">')
_BLOCK_RE = re.compile(re.escape(SEO_START) + r".*?" + re.escape(SEO_END), re.S)
# Links internos com .html (a Vercel serve sem extensão via cleanUrls).
_INTERNAL_HTML_RE = re.compile(r'href="(?!#|https?:|mailto:|tel:|data:)([^"]+?)\.html"')


def clean_internal_links(html):
    """Troca links internos .html pelos caminhos limpos da Vercel."""
    def repl(match):
        target = match.group(1)
        if target in ("/index", "index"):
            return 'href="/"'
        return 'href="%s"' % target
    return _INTERNAL_HTML_RE.sub(repl, html)



def write_site_files(root, entries):
    """Cria sitemap.xml e robots.txt na raiz do projeto (copiados ao dist/)."""
    root = Path(root)
    sitemap = root / "sitemap.xml"
    sitemap.write_text(seo.sitemap_xml(entries), encoding="utf-8", newline="\n")
    robots = root / "robots.txt"
    robots.write_text(seo.robots_txt(), encoding="utf-8", newline="\n")
    print("OK  /sitemap.xml (%d URLs indexáveis)" % len(entries))
    print("OK  /robots.txt")


def refresh_home(index_path):
    """Sincroniza <title>, description e o bloco SEO do index.html.

    O bloco fica entre os marcadores ``<!-- seo:start -->`` e
    ``<!-- seo:end -->``; se não existirem, são criados logo após a meta
    description.
    """
    index_path = Path(index_path)
    if not index_path.exists():
        return
    html = index_path.read_text(encoding="utf-8")

    html = _TITLE_RE.sub(lambda _m: "<title>%s</title>" % seo.HOME_TITLE,
                         html, count=1)
    html = _DESC_RE.sub(
        lambda _m: '<meta name="description" content="%s">'
        % seo.HOME_DESCRIPTION.replace('"', "&quot;"), html, count=1)

    block = seo.head_seo(seo.HOME_TITLE, seo.HOME_DESCRIPTION, "/")
    if _BLOCK_RE.search(html):
        html = _BLOCK_RE.sub(
            lambda _m: SEO_START + "\n" + block + "\n" + SEO_END, html, count=1)
    else:
        insertion = SEO_START + "\n" + block + "\n" + SEO_END + "\n"
        anchor = _DESC_RE.search(html)
        if anchor:
            html = html[:anchor.end()] + "\n" + insertion + html[anchor.end():]
        else:
            html = html.replace("</head>", insertion + "</head>", 1)

    index_path.write_text(clean_internal_links(html), encoding="utf-8")
    print("OK  /index.html (head de SEO sincronizada)")
