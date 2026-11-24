# -*- coding: utf-8 -*-
"""Identidade pública do site e vocabulário de SEO (domínio puro, sem I/O).

Toda URL absoluta do projeto (canonical, Open Graph, JSON-LD e sitemap.xml)
nasce de ``SITE_URL``. Para publicar em outro domínio basta definir a variável
de ambiente ``FARMA_SITE_URL`` no build ou alterar a constante abaixo.

Regra do projeto: nada de preço, estoque ou promessa terapêutica nos dados
estruturados — o site é uma vitrine informativa.
"""
import os
from html import escape
from json import dumps

# ---------------------------------------------------------------------------
# Identidade
# ---------------------------------------------------------------------------
SITE_URL = os.environ.get(
    "FARMA_SITE_URL", "https://farma-popular-ouro-preto.vercel.app").rstrip("/")
SITE_NAME = "Farma Popular Ouro Preto"
SITE_ALT_NAME = "Rede Minas Farma Popular"
LOCALE = "pt_BR"
LANG = "pt-BR"
THEME_COLOR = "#c8102e"

# Data editorial do conteúdo. O build é determinístico de propósito: atualize
# esta data (AAAA-MM-DD) quando o texto das páginas mudar de verdade.
CONTENT_UPDATED = "2026-11-24"

OG_IMAGE = "/assets/og/farma-popular-ouro-preto.jpg"
OG_IMAGE_WIDTH = 1200
OG_IMAGE_HEIGHT = 630
OG_IMAGE_ALT = (
    "Fachada da Farma Popular Ouro Preto na Rua Diogo de Vasconcelos, 39, "
    "com a marca da farmácia em amarelo e vermelho."
)

ROBOTS_INDEX = "index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1"
ROBOTS_NOINDEX = "noindex, follow"

# Metadados da home (fonte única: o build reescreve a <head> do index.html).
HOME_TITLE = "Farma Popular Ouro Preto — Farmácia em Ouro Preto/MG"
HOME_DESCRIPTION = (
    "Farmácia no centro de Ouro Preto/MG: medicamentos, genéricos, beleza, "
    "higiene e infantil. Consulte disponibilidade e preço pelo WhatsApp."
)

# ---------------------------------------------------------------------------
# Dados do negócio (conferidos em README e docs/05-dominio/fontes-e-dados.md)
# ---------------------------------------------------------------------------
PHONE_DISPLAY = "(31) 3551-5271"
PHONE_E164 = "+55-31-3551-5271"
STREET = "Rua Diogo de Vasconcelos, 39"
CITY = "Ouro Preto"
STATE = "MG"
POSTAL_CODE = "35400-000"
COUNTRY = "BR"
MAPS_URL = ("https://www.google.com/maps/search/?api=1&query="
            "Rua+Diogo+de+Vasconcelos%2C+39%2C+Ouro+Preto%2C+MG%2C+35400-000")
INSTAGRAM = "https://www.instagram.com/farmapopular.ouropreto/"
FACEBOOK = ("https://www.facebook.com/p/Farma-Popular-Ouro-Preto-100064645796782/"
            "?locale=pt_BR")
PAYMENT_ACCEPTED = "Cartão de crédito, Cartão de débito, Cheque, Pagamento por aproximação (NFC)"


def absolute(path):
    """URL absoluta e canônica de um caminho público (sem .html)."""
    if path.startswith(("http://", "https://")):
        return path
    if not path.startswith("/"):
        path = "/" + path
    return SITE_URL + path


def _jsonld(data):
    raw = dumps(data, ensure_ascii=False, separators=(",", ":"))
    # Evita fechar o <script> caso algum texto contenha "</".
    return raw.replace("</", "<\\/")


def _pharmacy():
    return {
        "@type": "Pharmacy",
        "@id": SITE_URL + "/#pharmacy",
        "name": SITE_NAME,
        "alternateName": SITE_ALT_NAME,
        "url": SITE_URL + "/",
        "image": absolute(OG_IMAGE),
        "telephone": PHONE_E164,
        "address": {
            "@type": "PostalAddress",
            "streetAddress": STREET,
            "addressLocality": CITY,
            "addressRegion": STATE,
            "postalCode": POSTAL_CODE,
            "addressCountry": COUNTRY,
        },
        "hasMap": MAPS_URL,
        "areaServed": {"@type": "City", "name": CITY},
        "openingHoursSpecification": [
            {
                "@type": "OpeningHoursSpecification",
                "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
                "opens": "08:30",
                "closes": "19:00",
            },
            {
                "@type": "OpeningHoursSpecification",
                "dayOfWeek": ["Saturday"],
                "opens": "08:30",
                "closes": "13:00",
            },
        ],
        "currenciesAccepted": "BRL",
        "paymentAccepted": PAYMENT_ACCEPTED,
        "sameAs": [INSTAGRAM, FACEBOOK],
    }


def _website():
    return {
        "@type": "WebSite",
        "@id": SITE_URL + "/#website",
        "url": SITE_URL + "/",
        "name": SITE_NAME,
        "description": HOME_DESCRIPTION,
        "inLanguage": LANG,
        "publisher": {"@id": SITE_URL + "/#pharmacy"},
    }


def _breadcrumbs(path, trail):
    """BreadcrumbList com Início + a trilha da página (último item = atual)."""
    items = [{"@type": "ListItem", "position": 1, "name": "Início",
              "item": SITE_URL + "/"}]
    for position, (label, item_path) in enumerate(trail, start=2):
        items.append({
            "@type": "ListItem",
            "position": position,
            "name": label,
            "item": absolute(item_path),
        })
    if len(items) < 2:
        return None
    return {
        "@type": "BreadcrumbList",
        "@id": absolute(path) + "#breadcrumb",
        "itemListElement": items,
    }


def structured_data(full_title, description, path, page_type="WebPage", trail=()):
    """Grafo @graph: farmácia + site + página (+ trilha de navegação)."""
    url = absolute(path)
    graph = [_website(), _pharmacy()]
    page = {
        "@type": page_type,
        "@id": url + "#webpage",
        "url": url,
        "name": full_title,
        "description": description,
        "isPartOf": {"@id": SITE_URL + "/#website"},
        "about": {"@id": SITE_URL + "/#pharmacy"},
        "inLanguage": LANG,
        "primaryImageOfPage": {
            "@type": "ImageObject",
            "url": absolute(OG_IMAGE),
            "width": OG_IMAGE_WIDTH,
            "height": OG_IMAGE_HEIGHT,
        },
    }
    crumbs = _breadcrumbs(path, trail)
    if crumbs:
        page["breadcrumb"] = {"@id": crumbs["@id"]}
        graph.append(crumbs)
    graph.append(page)
    return {"@context": "https://schema.org", "@graph": graph}


def head_seo(full_title, description, path, page_type="WebPage", trail=(),
             indexable=True, og_type="website"):
    """Bloco de <head> com canonical, robots, Open Graph, Twitter e JSON-LD."""
    url = absolute(path)
    image = absolute(OG_IMAGE)
    tags = []
    if indexable:
        tags.append('<link rel="canonical" href="%s">' % escape(url, quote=True))
    tags.append('<meta name="robots" content="%s">'
                % (ROBOTS_INDEX if indexable else ROBOTS_NOINDEX))
    tags.append('<meta name="theme-color" content="%s">' % THEME_COLOR)
    tags.append('<meta name="author" content="%s">' % escape(SITE_NAME))
    if indexable:
        tags.append('<link rel="alternate" hreflang="%s" href="%s">' % (LANG, url))
        tags.append('<link rel="alternate" hreflang="x-default" href="%s">' % url)
    tags += [
        '<meta property="og:type" content="%s">' % og_type,
        '<meta property="og:locale" content="%s">' % LOCALE,
        '<meta property="og:site_name" content="%s">' % escape(SITE_NAME, quote=True),
        '<meta property="og:title" content="%s">' % escape(full_title, quote=True),
        '<meta property="og:description" content="%s">' % escape(description, quote=True),
        '<meta property="og:url" content="%s">' % escape(url, quote=True),
        '<meta property="og:image" content="%s">' % escape(image, quote=True),
        '<meta property="og:image:type" content="image/jpeg">',
        '<meta property="og:image:width" content="%d">' % OG_IMAGE_WIDTH,
        '<meta property="og:image:height" content="%d">' % OG_IMAGE_HEIGHT,
        '<meta property="og:image:alt" content="%s">' % escape(OG_IMAGE_ALT, quote=True),
        '<meta name="twitter:card" content="summary_large_image">',
        '<meta name="twitter:title" content="%s">' % escape(full_title, quote=True),
        '<meta name="twitter:description" content="%s">' % escape(description, quote=True),
        '<meta name="twitter:image" content="%s">' % escape(image, quote=True),
        '<meta name="twitter:image:alt" content="%s">' % escape(OG_IMAGE_ALT, quote=True),
    ]
    tags.append('<script type="application/ld+json">%s</script>'
                % _jsonld(structured_data(full_title, description, path,
                                          page_type=page_type, trail=trail)))
    return "\n".join(tags)


# ---------------------------------------------------------------------------
# sitemap.xml e robots.txt
# ---------------------------------------------------------------------------
def sitemap_xml(entries):
    """Serializa as páginas indexáveis. ``entries`` aceita também dicionários."""
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for entry in entries:
        lines.append('  <url>')
        lines.append('    <loc>%s</loc>' % escape(absolute(entry["path"]), quote=True))
        lines.append('    <lastmod>%s</lastmod>' % entry.get("lastmod", CONTENT_UPDATED))
        lines.append('    <changefreq>%s</changefreq>' % entry.get("changefreq", "monthly"))
        lines.append('    <priority>%.1f</priority>' % entry.get("priority", 0.5))
        lines.append('  </url>')
    lines.append('</urlset>')
    return "\n".join(lines) + "\n"


def robots_txt():
    return "\n".join([
        "# Farma Popular Ouro Preto — https://%s" % SITE_URL.split("://", 1)[-1],
        "User-agent: *",
        "Allow: /",
        "",
        "# Documentação interna do projeto (não é conteúdo do site)",
        "Disallow: /docs/",
        "Disallow: /README.md",
        "",
        "Sitemap: %s/sitemap.xml" % SITE_URL,
        "",
    ])
