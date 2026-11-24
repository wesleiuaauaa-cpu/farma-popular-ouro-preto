# -*- coding: utf-8 -*-
"""Verificação de links, metadados, dados estruturados e sitemap.

Adaptador de infraestrutura: roda sobre os arquivos gerados na raiz do projeto
(o mesmo conteúdo copiado para dist/) e devolve quantos problemas encontrou.
"""
import json
import os
import re
from pathlib import Path
from xml.etree import ElementTree

from src.domain import seo

SITEMAP_NS = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
SKIP_PREFIX = ("#", "http", "mailto:", "tel:", "data:", "javascript:")
_HREF_RE = re.compile(r'(?:href|src)="([^"]+)"')
_TITLE_RE = re.compile(r"<title>(.*?)</title>", re.S)
_DESC_RE = re.compile(r'<meta name="description" content="([^"]*)"')
_ROBOTS_RE = re.compile(r'<meta name="robots" content="([^"]*)"')
_CANONICAL_RE = re.compile(r'<link rel="canonical" href="([^"]+)"')
_JSONLD_RE = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.S)
_INTERNAL_HTML_RE = re.compile(r'href="(?!#|https?:|mailto:|tel:|data:)[^"]*\.html"')
_URL_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def resolve(root, url):
    """Mapeia uma URL pública limpa (sem .html) para o arquivo no projeto."""
    clean = url.split("?")[0].split("#")[0]
    if clean in ("", "/"):
        return root / "index.html"
    rel = clean.lstrip("/")
    candidates = [root / rel]
    if not rel.endswith(".html"):
        candidates.append(root / (rel + ".html"))
        candidates.append(root / rel / "index.html")
    for candidate in candidates:
        if candidate.is_file():
            return candidate
    return None


def published(root):
    files = [root / "index.html", root / "404.html"]
    files += sorted((root / "pages").rglob("*.html")) if (root / "pages").exists() else []
    return [f for f in files if f.is_file()]


def main():
    root = Path(os.environ.get("FARMA_PROJECT_ROOT", Path(__file__).resolve().parents[2]))
    files = published(root)
    problems = []

    print("Páginas publicadas: %d" % len(files))
    for p in files:
        print(" -", p.relative_to(root).as_posix())

    bad_hash, missing, html_links = [], [], []
    titles, descriptions = {}, {}
    indexable = {}  # arquivo -> URL canônica

    for path in files:
        html = path.read_text(encoding="utf-8")
        name = path.relative_to(root).as_posix()

        if 'href="#"' in html:
            bad_hash.append(name)

        for match in _HREF_RE.finditer(html):
            url = match.group(1)
            if url.startswith(SKIP_PREFIX):
                continue
            if resolve(root, url) is None:
                missing.append((name, url))

        if _INTERNAL_HTML_RE.search(html):
            html_links.append(name)

        title = _TITLE_RE.search(html)
        desc = _DESC_RE.search(html)
        robots = _ROBOTS_RE.search(html)
        canonical = _CANONICAL_RE.search(html)
        noindex = bool(robots and "noindex" in robots.group(1))

        if not title or not title.group(1).strip():
            problems.append("%s: <title> ausente ou vazio" % name)
        else:
            titles.setdefault(title.group(1), []).append(name)

        if not desc or len(desc.group(1).strip()) < 50:
            problems.append("%s: meta description ausente ou curta" % name)
        else:
            descriptions.setdefault(desc.group(1), []).append(name)

        if not robots:
            problems.append("%s: meta robots ausente" % name)

        if noindex:
            if canonical:
                problems.append("%s: página noindex não deve ter canonical" % name)
        else:
            if not canonical:
                problems.append("%s: canonical ausente" % name)
            else:
                expected = seo.absolute(canonical.group(1))
                if canonical.group(1) != expected or not canonical.group(1).startswith(seo.SITE_URL):
                    problems.append("%s: canonical fora do domínio configurado" % name)
                indexable[path] = canonical.group(1)

        for blob in _JSONLD_RE.findall(html):
            try:
                data = json.loads(blob)
            except ValueError as exc:
                problems.append("%s: JSON-LD inválido (%s)" % (name, exc))
                continue
            if data.get("@context") != "https://schema.org":
                problems.append("%s: JSON-LD sem @context schema.org" % name)

    # ---------- sitemap.xml ----------
    sitemap_path = root / "sitemap.xml"
    sitemap_urls = []
    if not sitemap_path.is_file():
        problems.append("sitemap.xml não encontrado")
    else:
        try:
            tree = ElementTree.parse(sitemap_path)
        except ElementTree.ParseError as exc:
            problems.append("sitemap.xml inválido: %s" % exc)
            tree = None
        if tree is not None:
            for node in tree.findall(".//s:url", SITEMAP_NS):
                loc = node.findtext("s:loc", default="", namespaces=SITEMAP_NS).strip()
                lastmod = node.findtext("s:lastmod", default="", namespaces=SITEMAP_NS).strip()
                if not loc.startswith(seo.SITE_URL + "/"):
                    problems.append("sitemap: URL fora do domínio (%s)" % loc)
                if not _URL_DATE_RE.match(lastmod):
                    problems.append("sitemap: lastmod inválido em %s" % loc)
                target = resolve(root, loc[len(seo.SITE_URL):] or "/")
                if target is None:
                    problems.append("sitemap: URL sem arquivo correspondente (%s)" % loc)
                sitemap_urls.append(loc)

    duplicates = sorted({u for u in sitemap_urls if sitemap_urls.count(u) > 1})
    if duplicates:
        problems.append("sitemap: URLs duplicadas (%s)" % ", ".join(duplicates))

    expected = {url for url in indexable.values()}
    declared = set(sitemap_urls)
    for url in sorted(expected - declared):
        problems.append("sitemap: faltou página indexável (%s)" % url)
    for url in sorted(declared - expected):
        problems.append("sitemap: URL não indexável ou inexistente (%s)" % url)

    # ---------- robots.txt ----------
    robots_path = root / "robots.txt"
    if not robots_path.is_file():
        problems.append("robots.txt não encontrado")
    else:
        robots_txt = robots_path.read_text(encoding="utf-8")
        if "User-agent: *" not in robots_txt:
            problems.append("robots.txt: regra User-agent: * ausente")
        if ("Sitemap: %s/sitemap.xml" % seo.SITE_URL) not in robots_txt:
            problems.append("robots.txt: linha Sitemap ausente ou com domínio errado")

    for title, pages in titles.items():
        if len(pages) > 1:
            problems.append("título duplicado em %s: %s" % (", ".join(pages), title))
    for desc, pages in descriptions.items():
        if len(pages) > 1:
            problems.append("meta description duplicada em %s" % ", ".join(pages))

    # ---------- relatório ----------
    print("\n=== Links ===")
    print('href="#" restantes:', bad_hash or "nenhum")
    print("Links internos com .html:", html_links or "nenhum")
    print("Arquivos locais inexistentes:", missing or "nenhum")

    print("\n=== SEO ===")
    print("Páginas indexáveis:", len(indexable))
    print("URLs no sitemap.xml:", len(sitemap_urls))
    print("Domínio configurado:", seo.SITE_URL)
    print("Canonical + JSON-LD + robots: conferidos em %d páginas" % len(files))

    print("\n=== Produtos ilustrativos por página ===")
    for p in files:
        n = p.read_text(encoding="utf-8").count('class="product"')
        if n:
            print(" - %s: %d" % (p.name, n))

    print("\n=== Links WhatsApp (data-wa) por página ===")
    for p in files:
        n = p.read_text(encoding="utf-8").count("data-wa ")
        if n:
            print(" - %s: %d" % (p.name, n))

    print("\n=== Problemas encontrados: %d ===" % len(problems))
    for item in problems:
        print(" !", item)
    return len(problems)


if __name__ == "__main__":
    main()
