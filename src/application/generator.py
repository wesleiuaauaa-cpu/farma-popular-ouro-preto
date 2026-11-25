# -*- coding: utf-8 -*-
"""
Gerador das páginas internas da Farma Popular Ouro Preto.
Executar:  python build_pages.py

Gera: medicamentos-e-genericos.html, beleza-e-cuidados.html,
higiene-pessoal.html, infantil.html, saude-e-bem-estar.html,
perfumaria.html, sobre.html, contato.html, dicas-de-saude.html

A home (index.html) NÃO é gerada aqui — ela foi apenas ajustada pontualmente.
"""
import os
from pathlib import Path

from src.domain import seo
from src.domain.legal import LEGAL_PAGES
from html import escape

ROOT = Path(os.environ.get('FARMA_PROJECT_ROOT', Path(__file__).resolve().parents[2]))

# Caminhos publicos. A home fica na raiz; as internas em pages/ por dominio.
PAGE_PATHS = {
    'medicamentos-e-genericos.html': '/pages/medicamentos/medicamentos-e-genericos.html',
    'medicamentos-dor-e-febre.html': '/pages/medicamentos/medicamentos-dor-e-febre.html',
    'medicamentos-gripes-e-resfriados.html': '/pages/medicamentos/medicamentos-gripes-e-resfriados.html',
    'medicamentos-alergias.html': '/pages/medicamentos/medicamentos-alergias.html',
    'medicamentos-saude-digestiva.html': '/pages/medicamentos/medicamentos-saude-digestiva.html',
    'produto-novalgina-dipirona-monoidratada.html': '/pages/medicamentos/produto-novalgina-dipirona-monoidratada.html',
    'produto-tylenol-paracetamol.html': '/pages/medicamentos/produto-tylenol-paracetamol.html',
    'produto-alivium-ibuprofeno.html': '/pages/medicamentos/produto-alivium-ibuprofeno.html',
    'produto-paracetamol-clorfeniramina-fenilefrina.html': '/pages/medicamentos/produto-paracetamol-clorfeniramina-fenilefrina.html',
    'produto-loratadina-generico.html': '/pages/medicamentos/produto-loratadina-generico.html',
    'produto-cetirizina-generico.html': '/pages/medicamentos/produto-cetirizina-generico.html',
    'produto-omeprazol-generico.html': '/pages/medicamentos/produto-omeprazol-generico.html',
    'beleza-e-cuidados.html': '/pages/categorias/beleza-e-cuidados.html',
    'higiene-pessoal.html': '/pages/categorias/higiene-pessoal.html',
    'infantil.html': '/pages/categorias/infantil.html',
    'saude-e-bem-estar.html': '/pages/categorias/saude-e-bem-estar.html',
    'perfumaria.html': '/pages/categorias/perfumaria.html',
    'sobre.html': '/pages/institucionais/sobre.html',
    'contato.html': '/pages/institucionais/contato.html',
    'dicas-de-saude.html': '/pages/institucionais/dicas-de-saude.html',
    'politica-de-privacidade.html': '/pages/legais/politica-de-privacidade.html',
    'termos-de-uso.html': '/pages/legais/termos-de-uso.html',
    'politica-de-cookies.html': '/pages/legais/politica-de-cookies.html',
    'responsabilidade.html': '/pages/legais/responsabilidade.html',
    'entrega-e-troca.html': '/pages/legais/entrega-e-troca.html',
    'index.html': '/index.html',
}


def public_path(name):
    if name in PAGE_PATHS:
        return PAGE_PATHS[name]
    if name.startswith('produto-'):
        return '/pages/medicamentos/' + name
    return '/' + name


def public_url(name_or_path):
    """URL pública limpa (sem .html), como a Vercel serve (cleanUrls)."""
    path = PAGE_PATHS.get(name_or_path) or (
        name_or_path if name_or_path.startswith('/') else '/' + name_or_path)
    if path in ('/index.html', 'index.html', '/'):
        return '/'
    return path[:-5] if path.endswith('.html') else path


# Páginas indexáveis publicadas, na ordem em que entram no sitemap.
SITEMAP = []


def register(path, priority, changefreq='monthly', indexable=True):
    if indexable:
        SITEMAP.append({'path': path, 'priority': priority,
                        'changefreq': changefreq})


def rewrite_links(html):
    """Reescreve links e recursos para caminhos públicos absolutos e limpos."""
    for old, new in sorted(PAGE_PATHS.items(), key=lambda kv: -len(kv[0])):
        html = html.replace('href="%s"' % old, 'href="%s"' % public_url(old))
    html = html.replace('href="assets/', 'href="/assets/')
    html = html.replace('src="assets/', 'src="/assets/')
    return html


# ---------------------------------------------------------------------------
# Ícones SVG embutidos (mesmo conjunto de traços da home — sem emoji)
# ---------------------------------------------------------------------------
I = {
 'pill': '<rect x="2" y="8.6" width="20" height="7.2" rx="3.6" transform="rotate(-40 12 12)" stroke="currentColor" stroke-width="1.8" fill="none"/><path d="M9.2 7.6l7.2 7.2" stroke="currentColor" stroke-width="1.8"/><path d="M13.3 6.2l4.5 4.5a3.6 3.6 0 01-4.5 4.5L8.8 10.7z" fill="#ffc20e"/>',
 'beauty': '<rect x="3" y="9" width="7" height="12" rx="2" stroke="currentColor" stroke-width="1.8" fill="none"/><rect x="14" y="6" width="7" height="15" rx="2" stroke="currentColor" stroke-width="1.8" fill="none"/><path d="M5 9V5h3v4M16 6V3h3v3" stroke="currentColor" stroke-width="1.8"/><rect x="4.5" y="12.5" width="4" height="2.6" rx=".6" fill="#ffc20e"/>',
 'hygiene': '<rect x="6" y="8" width="12" height="13" rx="2" stroke="currentColor" stroke-width="1.8" fill="none"/><path d="M10 8V4h5M15 4h3" stroke="currentColor" stroke-width="1.8"/><rect x="9" y="12" width="6" height="5.4" rx="1" stroke="currentColor" stroke-width="1.6" fill="none"/>',
 'baby': '<circle cx="12" cy="13.4" r="7.4" stroke="currentColor" stroke-width="1.8" fill="none"/><circle cx="12" cy="13.4" r="4.6" stroke="currentColor" stroke-width="1.5" fill="none"/><circle cx="5.4" cy="5.8" r="2.4" fill="currentColor"/><circle cx="18.6" cy="5.8" r="2.4" fill="currentColor"/><circle cx="10" cy="12.6" r=".8" fill="currentColor"/><circle cx="14" cy="12.6" r=".8" fill="currentColor"/><ellipse cx="12" cy="15.6" rx="2.4" ry="1.7" stroke="currentColor" stroke-width="1.4" fill="none"/>',
 'wellness': '<path d="M12 21s-8-5-8-11a4.5 4.5 0 018-2.8A4.5 4.5 0 0120 10c0 6-8 11-8 11z" fill="currentColor"/><path d="M5.4 11.8h3.4l1.7-2.6 2.4 4.6 1.6-2h4.1" stroke="#fff" stroke-width="1.7" fill="none" stroke-linecap="round" stroke-linejoin="round"/>',
 'perfume': '<rect x="5" y="10" width="14" height="11" rx="4" stroke="currentColor" stroke-width="1.8" fill="none"/><path d="M10 10V7h4v3M9 7h6V4H9z" stroke="currentColor" stroke-width="1.8" fill="none"/><path d="M9.5 14.5h5" stroke="#ffc20e" stroke-width="1.8" stroke-linecap="round"/>',
 'arrow': '<path d="M9 5l7 7-7 7" stroke="currentColor" stroke-width="2.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>',
 'car': '<path d="M2 4l4 4 4-4" stroke="currentColor" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>',
 'home': '<path d="M3 11l9-8 9 8M5 10v10h14V10M9 20v-6h6v6" stroke="currentColor" stroke-width="1.9" fill="none" stroke-linecap="round" stroke-linejoin="round"/>',
 'store': '<path d="M3 10l2-6h14l2 6M4 10v10h16V10M9 20v-6h6v6" stroke="currentColor" stroke-width="1.9" fill="none" stroke-linejoin="round"/><path d="M8 10c.8-1.4 2.2-1.4 3 0s2.2 1.4 3 0" stroke="#ffc20e" stroke-width="1.6" fill="none"/>',
 'phone': '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 005 5L15 13l5 2v4a2 2 0 01-2 2A16 16 0 013 6a2 2 0 012-2z" stroke="currentColor" stroke-width="1.9" fill="none" stroke-linejoin="round"/>',
 'pin': '<path d="M12 22s7-6.5 7-12a7 7 0 10-14 0c0 5.5 7 12 7 12z" stroke="currentColor" stroke-width="1.9" fill="none"/><circle cx="12" cy="10" r="2.5" stroke="currentColor" stroke-width="1.9" fill="none"/>',
 'clock': '<circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="1.9" fill="none"/><path d="M12 7v5l3 2" stroke="currentColor" stroke-width="1.9" fill="none" stroke-linecap="round"/>',
 'whatsapp': '<path d="M12.04 2a9.9 9.9 0 00-8.4 15.2L2.3 22l4.9-1.3A9.9 9.9 0 1012.04 2zm0 18a8 8 0 01-4.1-1.1l-.3-.2-2.9.8.8-2.9-.2-.3A8 8 0 1112.04 20zm4.4-5.6c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.5.1-.2.2-.6.8-.8 1-.1.2-.3.2-.5.1a6.5 6.5 0 01-3.2-2.8c-.2-.4.2-.4.6-1.2.1-.2 0-.4 0-.5l-.8-1.8c-.2-.5-.4-.4-.5-.4h-.5c-.2 0-.4.1-.7.3-.2.3-.9.9-.9 2.2s1 2.6 1.1 2.7c.1.2 1.9 2.9 4.6 4 .6.3 1.1.4 1.5.6.6.2 1.2.2 1.6.1.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.1-.3-.2-.5-.3z" fill="currentColor"/>',
 'instagram': '<rect x="3" y="3" width="18" height="18" rx="5" stroke="currentColor" stroke-width="2" fill="none"/><circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="2" fill="none"/><circle cx="17.2" cy="6.8" r="1.1" fill="currentColor"/>',
 'facebook': '<circle cx="12" cy="12" r="11" fill="currentColor"/><path d="M13 20v-7h2.5l.5-3h-3V8.5c0-1 .5-1.5 1.5-1.5H16V4.5C15.5 4.4 14.5 4.3 13.8 4.3 11.6 4.3 10 5.6 10 8v2H7.5v3H10v7z" fill="#8e0a18"/>',
 'check': '<path d="M4 12l5 5L20 6" stroke="currentColor" stroke-width="2.4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>',
 'alert': '<path d="M12 3l10 17H2z" stroke="currentColor" stroke-width="1.9" fill="none" stroke-linejoin="round"/><path d="M12 9v5" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><circle cx="12" cy="17" r="1.1" fill="currentColor"/>',
 'card': '<rect x="2" y="5" width="20" height="14" rx="3" stroke="currentColor" stroke-width="1.9" fill="none"/><path d="M2 10h20" stroke="currentColor" stroke-width="1.9"/><path d="M6 15h4" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/>',
 'cheque': '<rect x="2" y="5" width="20" height="14" rx="2" stroke="currentColor" stroke-width="1.9" fill="none"/><path d="M5 15h7M5 11h5M15 10l2 2 3-4" stroke="currentColor" stroke-width="1.8" fill="none" stroke-linecap="round" stroke-linejoin="round"/>',
 'nfc': '<path d="M6 9a5 5 0 010 6M10 6a9 9 0 010 12M14 3.5a13 13 0 010 17" stroke="currentColor" stroke-width="1.9" fill="none" stroke-linecap="round"/><circle cx="18.5" cy="12" r="1.5" fill="#ffc20e"/>',
 'truck': '<path d="M2 7h11v10H2zM13 10h4l3 3v4h-7z" stroke="currentColor" stroke-width="1.9" fill="none" stroke-linejoin="round"/><circle cx="6" cy="18" r="2" stroke="currentColor" stroke-width="1.8" fill="none"/><circle cx="17" cy="18" r="2" stroke="currentColor" stroke-width="1.8" fill="none"/>',
 'bag': '<path d="M4 8h16l-1 12H5zM9 8V6a3 3 0 016 0v2" stroke="currentColor" stroke-width="1.9" fill="none" stroke-linejoin="round"/>',
 'hand': '<path d="M8 12V6a1.5 1.5 0 013 0v5-7a1.5 1.5 0 013 0v7-5a1.5 1.5 0 013 0v6-3a1.5 1.5 0 013 0v6c0 4-2.5 6-6 6h-2c-2 0-3.5-1-4.5-2.5L4 14a1.6 1.6 0 012.5-2z" stroke="currentColor" stroke-width="1.7" fill="none" stroke-linejoin="round"/>',
 'shield': '<path d="M12 2l8 3v6c0 5-3.5 9-8 11-4.5-2-8-6-8-11V5z" stroke="currentColor" stroke-width="1.9" fill="none"/><path d="M8 12l3 3 5-6" stroke="#ffc20e" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>',
 'search': '<circle cx="11" cy="11" r="7" stroke="currentColor" stroke-width="2.2" fill="none"/><path d="M20.5 20.5l-4.2-4.2" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/>',
 'tag': '<path d="M3 12l9-9h8v8l-9 9z" stroke="currentColor" stroke-width="1.9" fill="none" stroke-linejoin="round"/><circle cx="16" cy="8" r="1.6" fill="#ffc20e"/>',
 'heart': '<path d="M12 21s-8-5-8-11a4.5 4.5 0 018-2.8A4.5 4.5 0 0120 10c0 6-8 11-8 11z" stroke="currentColor" stroke-width="1.9" fill="none"/>',
 'info': '<circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="1.9" fill="none"/><path d="M12 11v6" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><circle cx="12" cy="7.5" r="1.2" fill="currentColor"/>',
 'back': '<path d="M15 5l-7 7 7 7" stroke="currentColor" stroke-width="2.4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>',
}


def ico(name, size=24, cls=''):
    return ('<svg width="%s" height="%s" viewBox="0 0 24 24" fill="none" '
            'aria-hidden="true"%s>%s</svg>') % (size, size, (' class="%s"' % cls if cls else ''), I[name])


# ---------------------------------------------------------------------------
# Fragmentos compartilhados
# ---------------------------------------------------------------------------
LOGO_SVG = ('<svg width="54" height="54" viewBox="0 0 52 52" aria-hidden="true">'
 '<defs><clipPath id="cy"><polygon points="0,0 52,0 0,52"/></clipPath>'
 '<clipPath id="cw"><polygon points="52,0 52,52 0,52"/></clipPath></defs>'
 '<g clip-path="url(#cy)"><path transform="translate(-1.6 -1.6)" d="M18 2h16v16h16v16H34v16H18V34H2V18h16z" fill="#ffc20e"/></g>'
 '<g clip-path="url(#cw)"><path transform="translate(1.6 1.6)" d="M18 2h16v16h16v16H34v16H18V34H2V18h16z" fill="#fff"/></g></svg>')

DECO = ('<div class="deco" aria-hidden="true">'
 '<svg class="d1" width="46" height="46" viewBox="0 0 52 52"><path d="M18 2h16v16h16v16H34v16H18V34H2V18h16z" fill="#ffc20e"/></svg>'
 '<svg class="d2" width="30" height="30" viewBox="0 0 52 52"><path d="M18 2h16v16h16v16H34v16H18V34H2V18h16z" fill="#fff"/></svg>'
 '<svg class="d3" width="66" height="66" viewBox="0 0 52 52"><path d="M18 2h16v16h16v16H34v16H18V34H2V18h16z" fill="#ffc20e"/></svg>'
 '<svg class="d4" width="34" height="34" viewBox="0 0 52 52"><path d="M18 2h16v16h16v16H34v16H18V34H2V18h16z" fill="#fff"/></svg>'
 '<svg class="d5" width="44" height="18" viewBox="0 0 44 18"><rect width="44" height="18" rx="9" fill="#fff"/><rect width="22" height="18" rx="9" fill="#ffc20e"/></svg>'
 '</div>')

# Cidade no rodapé: SVG embutido, igual ao da home aprovada (sem arquivo externo).
FOOTER_CITY_SVG = (
 '<svg class="fch" viewBox="0 0 340 230" aria-hidden="true">'
 '<g fill="#ffc20e">'
 '<rect x="18" y="150" width="46" height="80"/><polygon points="12,152 41,128 70,152"/>'
 '<rect x="30" y="168" width="12" height="16" fill="#a50b1f" opacity=".45"/>'
 '<rect x="70" y="132" width="40" height="98"/><polygon points="64,134 90,112 116,134"/>'
 '<rect x="140" y="96" width="74" height="134"/><polygon points="132,98 177,64 222,98"/>'
 '<rect x="118" y="52" width="20" height="178"/><polygon points="114,54 128,30 142,54"/>'
 '<rect x="216" y="52" width="20" height="178"/><polygon points="212,54 226,30 240,54"/>'
 '<rect x="240" y="140" width="44" height="90"/><polygon points="234,142 262,118 290,142"/>'
 '<rect x="288" y="158" width="44" height="72"/><polygon points="282,160 309,138 338,160"/>'
 '</g>'
 '<g fill="#a50b1f">'
 '<path d="M166 230v-44a11 11 0 0122 0v44z"/>'
 '<rect x="146" y="120" width="8" height="18" rx="4"/>'
 '<rect x="201" y="120" width="8" height="18" rx="4"/>'
 '<rect x="122" y="70" width="12" height="20" rx="6"/>'
 '<rect x="220" y="70" width="12" height="20" rx="6"/>'
 '<circle cx="177" cy="88" r="6"/>'
 '</g>'
 '<g stroke="#ffc20e" stroke-width="3" fill="none">'
 '<path d="M128 30v-11M123 25h10M226 30v-11M221 25h10"/>'
 '</g></svg>')

TOPBAR = (
 '<div class="top"><div class="wrap">'
 '<span>' + ico('pin', 14) + 'Rua Diogo de Vasconcelos, 39 – Ouro Preto/MG</span>'
 '<span>' + ico('phone', 14) + '<a href="tel:+553135515271">(31) 3551-5271</a></span>'
 '<span>' + ico('clock', 14) + 'Seg–Sex 08:30–19h · Sáb 08:30–13h</span>'
 '<div class="soc">'
 '<a href="https://www.instagram.com/farmapopular.ouropreto/" target="_blank" rel="noopener" aria-label="Instagram da Farma Popular Ouro Preto">' + ico('instagram', 17) + '</a>'
 '<a href="https://www.facebook.com/p/Farma-Popular-Ouro-Preto-100064645796782/?locale=pt_BR" target="_blank" rel="noopener" aria-label="Facebook da Farma Popular Ouro Preto">' + ico('facebook', 17) + '</a>'
 '</div></div></div>')

CATS = [
 ('medicamentos', 'Medicamentos e Genéricos', 'medicamentos-e-genericos.html', 'pill'),
 ('beleza', 'Beleza e Cuidados', 'beleza-e-cuidados.html', 'beauty'),
 ('higiene', 'Higiene Pessoal', 'higiene-pessoal.html', 'hygiene'),
 ('infantil', 'Infantil', 'infantil.html', 'baby'),
 ('saude', 'Saúde e Bem-estar', 'saude-e-bem-estar.html', 'wellness'),
 ('perfumaria', 'Perfumaria', 'perfumaria.html', 'perfume'),
]

MENU = [
 ('inicio', 'Início', 'index.html', False),
 ('medicamentos', 'Medicamentos', 'medicamentos-e-genericos.html', True),
 ('beleza', 'Beleza e Cuidados', 'beleza-e-cuidados.html', False),
 ('sobre', 'Nossa Loja', 'sobre.html', False),
 ('dicas', 'Dicas de Saúde', 'dicas-de-saude.html', False),
 ('contato', 'Contato', 'contato.html', False),
]

# Subcategorias reais (todas com produtos cadastrados no catálogo demonstrativo).
SUBCATS = [
 ('dor-febre', 'Dor e febre', 'medicamentos-dor-e-febre.html'),
 ('gripes-resfriados', 'Gripes e resfriados', 'medicamentos-gripes-e-resfriados.html'),
 ('alergias', 'Alergias', 'medicamentos-alergias.html'),
 ('saude-digestiva', 'Saúde digestiva', 'medicamentos-saude-digestiva.html'),
]


def submenu():
    return ('<div class="submenu" aria-label="Subcategorias de medicamentos">'
            + ''.join('<a href="%s">%s</a>' % (href, label) for _, label, href in SUBCATS)
            + '</div>')


def menu(active):
    out = []
    for key, label, href, caret in MENU:
        on = ' class="on" aria-current="page"' if key == active else ''
        car = ('<svg class="car" viewBox="0 0 12 12" fill="none" stroke="currentColor" '
               'stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M2 4l4 4 4-4"/></svg>') if caret else ''
        link = '<a%s href="%s"%s>%s%s</a>' % (on, href, ' aria-haspopup="true"' if caret else '', label, car)
        if key == 'medicamentos':
            out.append('<div class="mi">%s%s</div>' % (link, submenu()))
        else:
            out.append(link)
    return '<nav class="menu" id="menu" aria-label="Principal">' + ''.join(out) + '</nav>'


def catbar(active):
    out = []
    for key, label, href, icon in CATS:
        on = ' class="on" aria-current="page"' if key == active else ''
        out.append('<a%s href="%s">%s%s</a>' % (on, href, ico(icon, 17), label))
    return '<div class="catbar"><div class="wrap">' + ''.join(out) + '</div></div>'


WA_DEFAULT = 'Olá! Gostaria de informações sobre os produtos da Farma Popular Ouro Preto.'


def crumb_nav(trail):
    """Trilha de navegação visível, espelhando o BreadcrumbList do JSON-LD."""
    out = ['<a href="/">Início</a>']
    last = len(trail) - 1
    for i, (label, path) in enumerate(trail):
        out.append(ico('arrow', 13))
        if i == last:
            out.append('<span aria-current="page">' + escape(label) + '</span>')
        else:
            out.append('<a href="%s">%s</a>' % (path, escape(label)))
    return ('<nav class="crumb" aria-label="Trilha de navegação">'
            + ''.join(out) + '</nav>')


def header(active, title, script, desc, trail):
    return (
      '<a class="skip" href="#conteudo">Pular para o conteúdo</a>'
      + TOPBAR
      + '<header class="pagehead">' + DECO
      + '<div class="wrap navwrap"><div class="nav" id="nav">'
      + '<a class="logo" href="index.html" aria-label="Rede Minas Farma Popular – início">' + LOGO_SVG
      + '<span><small>Rede Minas</small><b>Farma</b><b>Popular</b></span></a>'
      + menu(active)
      + '<a class="btn wa-cta" href="https://wa.me/553135515271" data-wa data-wa-message="' + WA_DEFAULT + '" target="_blank" rel="noopener">'
      + '<svg width="21" height="21" viewBox="0 0 24 24" fill="#fff" aria-hidden="true">' + I['whatsapp'] + '</svg> Fale Conosco</a>'
      + '<button class="menu-toggle" id="menuToggle" aria-expanded="false" aria-controls="menu" aria-label="Abrir menu"><i></i><i></i><i></i></button>'
      + '</div></div>'
      + catbar(active)
      + '<div class="wrap"><div class="ptitle">'
      + crumb_nav(trail)
      + '<h1>' + escape(title) + '</h1><div class="script">' + escape(script) + '</div>'
      + '<p>' + escape(desc) + '</p>'
      + '</div></div>'
      + '<svg class="headwave" viewBox="0 0 1440 46" preserveAspectRatio="none" aria-hidden="true">'
      + '<path d="M0 46 L0 26 C 240 4 480 4 720 22 C 960 40 1200 36 1440 12 L1440 46 Z" fill="#ffc20e"/>'
      + '<path d="M0 46 L0 32 C 240 10 480 10 720 28 C 960 46 1200 42 1440 18 L1440 46 Z" fill="#fff"/>'
      + '</svg></header>'
      + '<main id="conteudo" class="page"><div class="wrap">'
    )


PAYMENT = (
 '<div class="pay" aria-label="Formas de pagamento informadas: cartão de crédito, cartão de débito, cheques e pagamento por dispositivo móvel via NFC">'
 '<span class="pm">' + ico('card', 19) + 'Crédito</span>'
 '<span class="pm">' + ico('card', 19) + 'Débito</span>'
 '<span class="pm">' + ico('cheque', 19) + 'Cheque</span>'
 '<span class="pm">' + ico('nfc', 19) + 'NFC</span>'
 '</div>')


COOKIE_BANNER = (
  '<div class="cookie-banner" id="cookieBanner" role="dialog" aria-modal="false" '
  'aria-labelledby="cookieTitle" aria-describedby="cookieDesc" hidden>'
  '<div class="cookie-card">'
  '<h2 id="cookieTitle">Privacidade e cookies</h2>'
  '<p id="cookieDesc">Usamos o necessário para lembrar sua escolha. Com seu '
  'aceite, ativamos a contagem anônima de visitas (Vercel Web Analytics, sem '
  'cookies). Você pode mudar a preferência a qualquer momento no rodapé.</p>'
  '<div class="cookie-actions">'
  '<button type="button" class="btn green sm" data-cookie-accept>Aceitar cookies</button>'
  '<button type="button" class="btn ghost sm" data-cookie-reject>Rejeitar opcionais</button>'
  '<a href="politica-de-cookies.html">Política de Cookies</a>'
  '</div></div></div>')

def footer():
    return (
 '<footer class="foot">'
 '<svg class="footwave" viewBox="0 0 1440 64" preserveAspectRatio="none" aria-hidden="true">'
 '<path d="M0 30 C 170 52 330 74 490 48 C 630 26 780 14 920 18 C 1100 22 1300 20 1440 14 L 1440 0 L 0 0 Z" fill="#ffc20e"/>'
 '<path d="M0 24 C 170 46 330 68 490 42 C 630 20 780 8 920 12 C 1100 16 1300 14 1440 8 L 1440 0 L 0 0 Z" fill="#fff"/>'
 '</svg>'
 + FOOTER_CITY_SVG +
 '<div class="wrap"><div class="cols">'
 '<div><a class="logo" href="index.html" aria-label="Rede Minas Farma Popular – início">' + LOGO_SVG
 + '<span><small>Rede Minas</small><b class="f">Farma</b><b>Popular</b></span></a>'
 + '<div class="sg2">Cuidando de você sempre!</div></div>'
 '<div><h4>Links Rápidos</h4>'
 '<a href="medicamentos-e-genericos.html">Medicamentos</a><br>'
 '<a href="beleza-e-cuidados.html">Beleza e Cuidados</a><br>'
 '<a href="sobre.html">Nossa Loja</a><br>'
 '<a href="dicas-de-saude.html">Dicas de Saúde</a><br>'
 '<a href="contato.html">Contato</a></div>'
 '<div><h4>Contato</h4>'
 '<span class="cspan">' + ico('phone', 15) + '<a href="tel:+553135515271">(31) 3551-5271</a></span>'
 '<span class="cspan">' + ico('pin', 15) + 'Rua Diogo de Vasconcelos, 39<br>Ouro Preto – MG, 35400-000</span>'
 '<span class="cspan">' + ico('clock', 15) + 'Seg–Sex 08:30–19h · Sáb 08:30–13h · Dom fechado</span></div>'
 '<div><h4>Siga-nos</h4><div class="social">'
 '<a href="https://www.instagram.com/farmapopular.ouropreto/" target="_blank" rel="noopener" aria-label="Instagram">' + ico('instagram', 30) + '</a>'
 '<a href="https://www.facebook.com/p/Farma-Popular-Ouro-Preto-100064645796782/?locale=pt_BR" target="_blank" rel="noopener" aria-label="Facebook">' + ico('facebook', 30) + '</a>'
 '</div></div></div></div>'
 '<div class="legal"><div class="wrap">'
 '<span class="lsp">' + ico('shield', 21) + 'Compra segura • Atendimento de qualidade • Sempre com você!</span>'
 + PAYMENT +
  '</div></div>'
  '<div class="legal2"><div class="wrap">'
  '<nav class="legal-links" aria-label="Documentos e privacidade">'
  '<a href="politica-de-privacidade.html">Política de Privacidade</a>'
  '<a href="termos-de-uso.html">Termos de Uso</a>'
  '<a href="politica-de-cookies.html">Política de Cookies</a>'
  '<a href="responsabilidade.html">Aviso de Responsabilidade</a>'
  '<a href="entrega-e-troca.html">Entrega e Troca</a>'
  '<button type="button" class="cookielink" data-cookie-open>Preferências de cookies</button>'
  '</nav></div></div>'
  '</footer>'
 '<a class="wa-float" href="https://wa.me/553135515271" data-wa data-wa-message="' + WA_DEFAULT + '" target="_blank" rel="noopener" aria-label="Conversar no WhatsApp">'
 '<svg viewBox="0 0 24 24" aria-hidden="true">' + I['whatsapp'] + '</svg></a>'
 '<a class="back" href="#conteudo">' + ico('back', 15) + 'Voltar ao topo</a>'
  + COOKIE_BANNER +
  '<script src="assets/js/site.js"></script>'
 )


def page(name, active, title, script, desc, crumb, body, page_type='WebPage',
         trail=None, priority=0.5, changefreq='monthly', indexable=True,
         og_type='website'):
    """Monta uma página completa com <head> de SEO e trilha de navegação."""
    path = public_url(name)
    full_title = title + ' — ' + seo.SITE_NAME
    trail = list(trail) if trail else [(crumb, path)]
    head = seo.head_seo(full_title, desc, path, page_type=page_type,
                        trail=trail, indexable=indexable, og_type=og_type)
    register(path, priority, changefreq, indexable)
    return ('<!DOCTYPE html>\n<html lang="pt-BR">\n<head>\n'
      '<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
      '<title>' + escape(full_title) + '</title>\n'
      '<meta name="description" content="' + escape(desc) + '">\n'
      + head + '\n'
      '<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 52 52\'%3E%3Crect width=\'52\' height=\'52\' rx=\'10\' fill=\'%23c8102e\'/%3E%3Cpath d=\'M19 6h14v13h13v14H33v13H19V33H6V19h13z\' fill=\'%23ffc20e\'/%3E%3C/svg%3E">\n'
      '<link rel="stylesheet" href="assets/css/site.css">\n</head>\n<body>\n'
      + header(active, title, script, desc, trail)
      + body
      + '</div></main>\n'
      + footer()
      + '\n</body>\n</html>\n')


def emit(name, *args, **kwargs):
    write(name, page(name, *args, **kwargs))


# ---------------------------------------------------------------------------
# Produtos ilustrativos (sem preço, sem estoque, sem marcas reais)
# ---------------------------------------------------------------------------
def p(name, img, desc, cat):
    return {'name': name, 'img': img, 'desc': desc, 'cat': cat}

PRODUCTS = {
 'medicamentos': [
  p('Medicamento genérico — caixa ilustrativa', 'caixa-generico.svg',
    'Representação de embalagem de medicamento genérico. Consulte a disponibilidade e as orientações diretamente na loja.', 'Medicamentos e Genéricos'),
  p('Comprimidos — cartela ilustrativa', 'cartela-comprimidos.svg',
    'Ilustração de cartela de comprimidos. A apresentação e a disponibilidade devem ser confirmadas pela farmácia.', 'Medicamentos e Genéricos'),
  p('Xarope — frasco ilustrativo', 'frasco-xarope.svg',
    'Ilustração de frasco de xarope. Não representa produto, marca ou dosagem específica.', 'Medicamentos e Genéricos'),
  p('Cápsulas — frasco ilustrativo', 'frasco-capsulas.svg',
    'Ilustração de frasco de cápsulas. Consulte na loja as opções disponíveis.', 'Medicamentos e Genéricos'),
  p('Termômetro digital', 'termometro.svg',
    'Ilustração de termômetro digital. Verifique a disponibilidade com a farmácia.', 'Medicamentos e Genéricos'),
 ],
 'beleza': [
  p('Creme de cuidados', 'beleza-bisnaga-creme.webp',
    'Foto de bisnaga de creme. Sem marca definida: consulte a loja para conhecer as opções.', 'Beleza e Cuidados'),
  p('Shampoo', 'beleza-frasco-shampoo.webp',
    'Foto de frasco de shampoo. Disponibilidade e marcas confirmadas diretamente na loja.', 'Beleza e Cuidados'),
  p('Sabonete', 'beleza-sabonete.webp',
    'Foto de sabonete. Consulte disponibilidade e preço na farmácia.', 'Beleza e Cuidados'),
  p('Protetor solar', 'beleza-protetor-solar.webp',
    'Foto de frasco de protetor solar. Fator e apresentação devem ser conferidos na loja.', 'Beleza e Cuidados'),
  p('Desodorante', 'beleza-desodorante.webp',
    'Foto de desodorante em aerossol. Consulte as opções disponíveis na loja.', 'Beleza e Cuidados'),
 ],
 'higiene': [
  p('Pasta de dentes', 'higiene-pasta-dental.webp',
    'Foto de pasta de dentes. Consulte disponibilidade e apresentações na farmácia.', 'Higiene Pessoal'),
  p('Escova dental', 'higiene-escova-dental.webp',
    'Foto de escova dental ao lado da pasta. Verifique as opções na loja.', 'Higiene Pessoal'),
  p('Sabonete', 'higiene-sabonete.webp',
    'Foto de sabonete para higiene diária. Disponibilidade confirmada na loja.', 'Higiene Pessoal'),
  p('Álcool em gel', 'higiene-alcool-gel.webp',
    'Foto de frasco de álcool em gel. Consulte disponibilidade e apresentações.', 'Higiene Pessoal'),
  p('Luvas descartáveis', 'higiene-luvas.webp',
    'Foto de caixa de luvas descartáveis. Tamanhos e disponibilidade na loja.', 'Higiene Pessoal'),
 ],
 'infantil': [
  p('Mamadeira', 'infantil-mamadeira.webp',
    'Foto de mamadeira. Modelos e disponibilidade devem ser confirmados na loja.', 'Infantil'),
  p('Creme para bebê', 'infantil-creme-bebe.webp',
    'Foto de pote de creme para bebê. Consulte as opções disponíveis na farmácia.', 'Infantil'),
  p('Sabonete para bebê', 'infantil-sabonete.webp',
    'Foto de sabonete. Consulte disponibilidade e apresentações na loja.', 'Infantil'),
  p('Shampoo infantil', 'infantil-shampoo.webp',
    'Foto de frasco de shampoo. Verifique as opções na loja.', 'Infantil'),
  p('Termômetro digital', 'infantil-termometro.webp',
    'Foto de termômetro digital para cuidados com a família. Consulte a disponibilidade.', 'Infantil'),
 ],
 'saude': [
  p('Suplemento alimentar', 'saude-suplemento.webp',
    'Foto de pote de suplemento alimentar. Não é recomendação de uso: consulte um profissional de saúde.', 'Saúde e Bem-estar'),
  p('Termômetro digital', 'saude-termometro.webp',
    'Foto de termômetro digital. Consulte disponibilidade e preço na loja.', 'Saúde e Bem-estar'),
  p('Protetor solar', 'saude-protetor-solar.webp',
    'Foto de protetor solar. Fator e apresentação devem ser conferidos na loja.', 'Saúde e Bem-estar'),
  p('Álcool em gel', 'saude-alcool-gel.webp',
    'Foto de álcool em gel. Disponibilidade confirmada diretamente com a farmácia.', 'Saúde e Bem-estar'),
  p('Luvas descartáveis', 'saude-luvas.webp',
    'Foto de luvas descartáveis. Consulte tamanhos e disponibilidade na loja.', 'Saúde e Bem-estar'),
 ],
 'perfumaria': [
  p('Perfume', 'perfumaria-perfume.webp',
    'Foto de frasco de perfume. Marcas e disponibilidade confirmadas na loja.', 'Perfumaria'),
  p('Desodorante', 'perfumaria-desodorante.webp',
    'Foto de desodorante. Consulte as opções disponíveis na farmácia.', 'Perfumaria'),
  p('Creme perfumado', 'perfumaria-creme-perfumado.webp',
    'Foto de bisnaga de creme perfumado. Verifique a disponibilidade na loja.', 'Perfumaria'),
  p('Sabonete perfumado', 'perfumaria-sabonete.webp',
    'Foto de sabonete perfumado. Consulte disponibilidade e preço.', 'Perfumaria'),
  p('Body splash', 'perfumaria-body-splash.webp',
    'Foto de frasco de body splash. Consulte as opções na loja.', 'Perfumaria'),
 ],
}

CATEGORY_PAGES = [
 ('medicamentos', 'Medicamentos e Genéricos', 'Ouro Preto',
  'Conheça uma seleção ilustrativa de itens da linha de medicamentos e genéricos. A disponibilidade é confirmada diretamente com a loja.',
  'Medicamentos e Genéricos'),
 ('beleza', 'Beleza e Cuidados', 'Ouro Preto',
  'Uma vitrine de exemplos de produtos de beleza e cuidados pessoais. Marcas e disponibilidade devem ser conferidas na farmácia.',
  'Beleza e Cuidados'),
 ('higiene', 'Higiene Pessoal', 'Ouro Preto',
  'Itens de exemplo para a higiene do dia a dia. Consulte a farmácia para saber o que está disponível.',
  'Higiene Pessoal'),
 ('infantil', 'Infantil', 'Ouro Preto',
  'Seleção de exemplos de produtos para os cuidados com bebês e crianças. Confira a disponibilidade com a loja.',
  'Infantil'),
 ('saude', 'Saúde e Bem-estar', 'Ouro Preto',
  'Uma mostra de exemplos de produtos para saúde e bem-estar. Não há recomendação de tratamento nesta página.',
  'Saúde e Bem-estar'),
 ('perfumaria', 'Perfumaria', 'Ouro Preto',
  'Vitrine de exemplos de fragrâncias e produtos de perfumaria. Consulte marcas e disponibilidade na loja.',
  'Perfumaria'),
]

# ---------------------------------------------------------------------------
# Catálogo demonstrativo de medicamentos reais
# Dados cadastrais verificados na base de dados abertos da Anvisa:
# https://dados.anvisa.gov.br/dados/CONSULTAS/PRODUTOS/TA_CONSULTA_MEDICAMENTOS.CSV
# Situação "Ativo" confirmada em todas as registrações abaixo na consulta (16/11/2026).
# Apresentação/concentração/quantidade: NÃO confirmados para a maioria — marcados como pendentes.
# Imagens: fotografias reais das embalagens, autorizadas pelo proprietário do site
# em 23/11/2026. Fotos salvas localmente em assets/produtos/ e documentadas em docs/05-dominio/fontes-e-dados.md.
# A apresentação/fabricante da embalagem fotografada pode diferir do item entregue pela loja.
# ---------------------------------------------------------------------------
def med(slug, name, substance, reg, company, regtype, sub, image, desc,
        reference='', presentation=''):
    return {
        'slug': slug, 'name': name, 'substance': substance, 'reg': reg,
        'company': company, 'regtype': regtype, 'sub': sub, 'image': image,
        'desc': desc, 'reference': reference, 'presentation': presentation,
    }


SUB_LABEL = dict((slug, label) for slug, label, _ in SUBCATS)

MEDICINES = [
 med('novalgina-dipirona-monoidratada', 'Novalgina', 'dipirona monoidratada',
     '186200018', 'Opella Healthcare Brazil Ltda', 'Novo (medicamento de referência, conforme Anvisa)',
     'dor-febre', 'novalgina.webp',
     'Medicamento de referência à base de dipirona monoidratada, registrado na Anvisa. '
     'Não apresentamos indicações terapêuticas: leia a bula e consulte um profissional de saúde.',
     reference='Medicamento de referência desde 12/11/2012 (dado da base Anvisa).',
     presentation='O site oficial do fabricante relaciona as linhas comprimidos 1 g, '
                  'comprimidos 500 mg, solução oral, gotas, efervescente 1 g e supositório. '
                  'Confirme qual apresentação corresponde ao registro e à embalagem na loja.'),
 med('tylenol-paracetamol', 'Tylenol', 'paracetamol',
     '157211214', 'Kenvue Ltda.', 'Novo (medicamento de referência, conforme Anvisa)',
     'dor-febre', 'tylenol.webp',
     'Medicamento à base de paracetamol, com registro ativo na Anvisa. '
     'Este é um catálogo informativo: não indicamos uso, dose ou tratamento.'),
 med('alivium-ibuprofeno', 'Alivium', 'ibuprofeno',
     '178170807', 'Cosmed Indústria de Cosméticos e Medicamentos S.A.',
     'Novo (medicamento de referência, conforme Anvisa)',
     'dor-febre', 'alivium.webp',
     'Medicamento à base de ibuprofeno, com registro ativo na Anvisa. '
     'Consulte a bula oficial antes de usar e tire dúvidas com um profissional de saúde.'),
 med('paracetamol-clorfeniramina-fenilefrina', 'Paracetamol + clorfeniramina + fenilefrina',
     'paracetamol, maleato de clorfeniramina e cloridrato de fenilefrina',
     '143810263', 'Cimed Indústria S.A', 'Genérico',
     'gripes-resfriados', 'paracetamol-clorfeniramina-fenilefrina.webp',
     'Medicamento genérico de associação registrado na Anvisa, com o princípio ativo '
     'informado acima. Sem alegações terapêuticas nesta vitrine.'),
 med('loratadina-generico', 'Loratadina — Genérico', 'loratadina',
     '155840465', 'Brainfarma Indústria Química e Farmacêutica S.A', 'Genérico',
     'alergias', 'loratadina-generico.webp',
     'Medicamento genérico à base de loratadina, com registro ativo na Anvisa. '
     'Não substitui orientação profissional.'),
 med('cetirizina-generico', 'Dicloridrato de cetirizina — Genérico', 'dicloridrato de cetirizina',
     '103700518', 'Laboratório Teuto Brasileiro S/A', 'Genérico',
     'alergias', 'cetirizina-generico.webp',
     'Medicamento genérico à base de dicloridrato de cetirizina, registrado na Anvisa. '
     'Consulte a bula e um profissional de saúde.'),
 med('omeprazol-generico', 'Omeprazol — Genérico', 'omeprazol',
     '105830969', 'Germed Farmacêutica Ltda', 'Genérico',
     'saude-digestiva', 'omeprazol-generico.webp',
     'Medicamento genérico à base de omeprazol, com registro ativo na Anvisa. '
     'Sem recomendação de uso ou tratamento nesta página.'),
]

BULA_URL = 'https://consultas.anvisa.gov.br/#/bulario/'

MED_NOTICE = (
 '<div class="notice">' + ico('alert', 22) +
 '<div><strong>Vitrine informativa.</strong> Os medicamentos abaixo existem e têm registro '
 'ativo na Anvisa (dados consultados em 16/11/2026), mas <strong>este site não vende, não informa '
 'preço, estoque ou disponibilidade local</strong> e não faz recomendações de tratamento. '
 'As fotos mostram embalagens de referência; apresentação e fabricante podem diferir do item disponível na loja. Confira a bula, o preço e a disponibilidade '
 'diretamente com a Farma Popular Ouro Preto.</div></div>')


def subfilters(current):
    out = ['<a href="medicamentos-e-genericos.html"%s>Todos <span class="count">%d</span></a>'
           % (' class="on"' if current == '' else '', len(MEDICINES))]
    for slug, label, href in SUBCATS:
        n = sum(1 for m in MEDICINES if m['sub'] == slug)
        out.append('<a href="%s"%s>%s <span class="count">%d</span></a>'
                   % (href, ' class="on"' if current == slug else '', label, n))
    return '<nav class="subfilters" aria-label="Subcategorias de medicamentos">' + ''.join(out) + '</nav>'


def medicine_card(m):
    msg = 'Olá! Gostaria de consultar a disponibilidade de: %s — %s (Reg. Anvisa %s).' % (
        m['name'], m['substance'], m['reg'])
    searchable = m['name'] + ' ' + m['substance'] + ' ' + m['company'] + ' ' + m['reg'] + ' ' + m['desc']
    return (
 '<article class="product" data-search="%s">'
 '<div class="pmedia"><img src="assets/produtos/%s" alt="Foto da embalagem de %s" loading="lazy">'
 '<span class="demo">FOTO DO PRODUTO</span></div>'
 '<div class="pbody">'
 '<span class="pcat">%s · Reg. %s</span>'
 '<h3 class="pname">%s</h3>'
 '<p class="psub">Princípio ativo: %s</p>'
 '<p class="pdesc">%s</p>'
 '<div class="pprice">' + ico('tag', 18) + '<span>Consulte disponibilidade e preço'
 '<span class="est">Confirmados diretamente com a farmácia.</span></span></div>'
 '<div class="pactions">'
 '<a class="btn red sm" href="produto-%s.html">Ver detalhes %s</a>'
 '<a class="btn green sm" data-wa data-wa-message="%s">Consultar pelo WhatsApp %s</a>'
 '</div>'
 '<p class="pmeta">Ilustração sem marca. Dados: Anvisa.</p>'
 '</div></article>'
 ) % (escape(searchable, quote=True), m['image'], escape(m['name'], quote=True),
      SUB_LABEL[m['sub']], m['reg'], escape(m['name']), escape(m['substance']),
      escape(m['desc']), m['slug'], ico('arrow', 14),
      escape(msg, quote=True), ico('whatsapp', 15))


def medicine_listing_body(current=''):
    items = [m for m in MEDICINES if not current or m['sub'] == current]
    label = SUB_LABEL.get(current, 'Medicamentos e Genéricos')
    head = ('<div class="sec-head"><div><h2>%s <span class="rl">registrados na Anvisa</span></h2>'
            '<p>Seleção demonstrativa para consulta. A venda é finalizada diretamente com a farmácia.</p></div>'
            '<span class="tag">' + ico('info', 15) + ' %d produto(s) nesta lista</span></div>'
            ) % (escape(label), len(items))
    return (
      MED_NOTICE
      + head
      + subfilters(current)
      + '<div id="searchTerm" class="tag" hidden></div>'
      + '<div class="grid">' + ''.join(medicine_card(m) for m in items) + '</div>'
      + '<div id="emptySearch" class="empty" hidden>'
      + '<h3>Nenhum medicamento encontrado</h3>'
      + '<p>Não localizamos esse termo entre os itens desta vitrine. A farmácia pode ter outras opções.</p>'
      + '<a class="btn red sm" data-wa data-wa-message="Olá! Gostaria de consultar a disponibilidade de um medicamento.">Consultar pelo WhatsApp ' + ico('arrow', 14) + '</a>'
      + '</div>'
      + '<div class="cta"><div><h2>Precisa de mais informações? <span>Fale com a Farma Popular.</span></h2>'
      '<p>Preço, estoque, apresentação e disponibilidade devem ser confirmados diretamente com a loja.</p></div>'
      '<a class="btn green" data-wa data-wa-message="Olá! Gostaria de informações sobre medicamentos da Farma Popular Ouro Preto.">'
      + ico('whatsapp', 19) + 'Consultar pelo WhatsApp</a></div>'
      )


def spec_row(term, value):
    return '<dt>%s</dt><dd>%s</dd>' % (term, value)


def detail_body(m):
    msg = 'Olá! Gostaria de consultar este produto pelo WhatsApp: %s — %s (Reg. Anvisa %s).' % (
        m['name'], m['substance'], m['reg'])
    specs = (
      spec_row('Nome / denominação', escape(m['name']))
      + spec_row('Princípio ativo', escape(m['substance']))
      + spec_row('Categoria', 'Medicamentos e Genéricos › ' + escape(SUB_LABEL[m['sub']]))
      + spec_row('Registro Anvisa', '%s (situação ativa na consulta de 16/11/2026)' % m['reg'])
      + spec_row('Detentor do registro', escape(m['company']))
      + spec_row('Classificação', escape(m['regtype']))
      + spec_row('Apresentação / concentração', escape(m['presentation']) if m['presentation']
                 else 'Pendente de confirmação — consulte a bula e a embalagem.')
      + spec_row('Quantidade da embalagem', 'Pendente de confirmação — consulte a bula e a embalagem.')
      + (spec_row('Referência (dado Anvisa)', escape(m['reference'])) if m['reference'] else '')
    )
    related = [x for x in MEDICINES if x['sub'] == m['sub'] and x['slug'] != m['slug']]
    related_html = ''
    if related:
        related_html = ('<section class="related"><div class="sec-head"><div>'
          '<h2>Também nesta <span class="rl">categoria</span></h2></div></div>'
          '<div class="grid">' + ''.join(medicine_card(x) for x in related[:3]) + '</div></section>')

    return (
 '<div class="detail">'
 '<div class="detail-media"><img src="assets/produtos/%s" alt="Foto da embalagem de %s">'
 '<span class="demo">FOTO DA EMBALAGEM</span></div>'
 '<div class="detail-info">'
 '<h2>%s</h2><p class="substance">%s</p>'
 '<p style="font-size:14px;line-height:1.65;color:#5b4a4a">%s</p>'
 '<dl class="spec">%s</dl>'
 '<div class="pending">' + ico('alert', 19) +
 '<div><strong>Dados pendentes de confirmação:</strong> apresentação, concentração, forma farmacêutica '
 'e quantidade da embalagem não foram verificados em fonte oficial para este item. '
'A foto mostra uma embalagem de referência, que pode diferir da apresentação disponível na loja. '
 'Preço, estoque e disponibilidade também não são informados neste site.</div></div>'
 '<div class="pubula">' + ico('info', 22) +
 '<div>Consulte sempre a <strong>bula oficial</strong> no Bulário da Anvisa: '
 '<a href="%s" target="_blank" rel="noopener">abrir Bulário Eletrônico Anvisa</a>. '
 'Pesquise pelo número de registro <strong>%s</strong> antes de usar qualquer medicamento.</div></div>'
 '<div class="warnbox"><strong>Aviso importante:</strong> esta página é uma vitrine informativa. '
 'Não contém indicações, contraindicações, posologia ou orientação médica. '
 'Leia a bula, não pratique automedicação e procure um profissional de saúde em caso de dúvida.</div>'
 '<a class="btn green" data-wa data-wa-message="%s">%s Consultar este produto pelo WhatsApp %s</a>'
 '<p class="pmeta" style="margin-top:12px">Atendimento pelo WhatsApp (31) 3551-5271. '
 'Nenhuma venda, carrinho ou pagamento é realizado neste site.</p>'
 '</div></div>'
 + related_html
 ) % (m['image'], escape(m['name'], quote=True), escape(m['name']),
      escape(m['substance']), escape(m['desc']), specs, BULA_URL, m['reg'],
      escape(msg, quote=True), ico('whatsapp', 19), ico('arrow', 14))


NOTICE = (
 '<div class="notice">' + ico('alert', 22) +
 '<div><strong>Antes de pedir:</strong> as fotos abaixo mostram <strong>exemplos de produtos</strong>. Marcas, apresentações e fabricantes podem diferir dos itens disponíveis na loja. '
 'Este site não apresenta preços, estoque ou condições confirmadas da farmácia, não faz alegações médicas '
 'e não recomenda tratamentos. Não há carrinho, checkout ou pagamento online: pedidos e consultas são '
 'encaminhados pelo WhatsApp. Confirme disponibilidade, preço e orientações diretamente com a loja.</div></div>')


def product_card(item):
    msg = 'Olá! Gostaria de consultar a disponibilidade de: %s (%s).' % (item['name'], item['cat'])
    searchable = item['name'] + ' ' + item['cat'] + ' ' + item['desc']
    return (
 '<article class="product" data-search="%s">'
 '<div class="pmedia"><img src="assets/produtos/%s" alt="Foto de %s" loading="lazy">'
 '<span class="demo">FOTO DO PRODUTO</span></div>'
 '<div class="pbody">'
 '<span class="pcat">%s</span>'
 '<h3 class="pname">%s</h3>'
 '<p class="pdesc">%s</p>'
 '<div class="pprice">' + ico('tag', 18) + '<span>Consulte disponibilidade e preço'
 '<span class="est">Informação confirmada diretamente com a loja.</span></span></div>'
 '<a class="btn red sm pbtn" data-wa data-wa-message="%s">Pedir pelo WhatsApp %s</a>'
 '<p class="pmeta">Foto de produto. Marca e apresentação podem diferir do item disponível na loja. Nenhum valor ou estoque é afirmado neste site.</p>'
 '</div></article>'
 ) % (escape(searchable, quote=True), item['img'], escape(item['name'], quote=True),
      escape(item['cat']), escape(item['name']), escape(item['desc']),
      escape(msg, quote=True), ico('arrow', 14))


def category_body(key):
    title = dict((k, t) for k, t, *_ in CATEGORY_PAGES)[key]
    cards = ''.join(product_card(x) for x in PRODUCTS[key])
    return (
      NOTICE
      + '<div class="sec-head"><div><h2>Nossa seleção <span class="rl">em fotos</span></h2>'
      + '<p>Veja exemplos do tipo de produto encontrado nesta categoria. '
      + 'Para saber o que está disponível hoje, fale com a farmácia.</p></div>'
      + '<span class="tag">' + ico('info', 15) + 'Até 5 itens por categoria</span></div>'
      + '<div id="searchTerm" class="tag" hidden></div>'
      + '<div class="grid" id="produtos">' + cards + '</div>'
      + '<div id="emptySearch" class="empty" hidden>'
      + '<h3>Nenhum item ilustrativo encontrado</h3>'
      + '<p>Não localizamos esse termo entre os produtos de exemplo desta página. '
      + 'A farmácia pode ter outras opções disponíveis.</p>'
      + '<a class="btn red sm" data-wa data-wa-message="Olá! Gostaria de consultar a disponibilidade de um produto.">Consultar pelo WhatsApp ' + ico('arrow', 14) + '</a>'
      + '<div class="mini-links">'
      + ''.join('<a href="%s">%s</a>' % (href, label) for _, label, href, _ in CATS)
      + '</div>'
      + '</div>'
      + '<div class="cta"><div><h2>Não encontrou o que procura? <span>Pergunte à Farma Popular.</span></h2>'
      + '<p>Compras na loja, retirada na loja e entrega. Consulte disponibilidade, preço e condições diretamente com a equipe.</p></div>'
      + '<a class="btn green" data-wa data-wa-message="Olá! Gostaria de consultar a disponibilidade de produtos na Farma Popular Ouro Preto.">'
      + ico('whatsapp', 19) + 'Consultar pelo WhatsApp</a></div>'
    )


# ---------------------------------------------------------------------------
# Páginas informativas
# ---------------------------------------------------------------------------
def sobre_body():
    return (
 '<div class="two">'
 '<div class="panel"><h2>Sobre a <span class="rl">Farma Popular Ouro Preto</span></h2>'
 '<p>Somos a Farma Popular Ouro Preto. Você pode comprar na loja, retirar na loja ou solicitar entrega. '
 'As condições de cada serviço devem ser confirmadas diretamente com a equipe.</p>'
 '<ul>'
 '<li>' + ico('pin', 18) + '<span><strong>Endereço:</strong> Rua Diogo de Vasconcelos, 39, Ouro Preto – MG, 35400-000.</span></li>'
 '<li>' + ico('phone', 18) + '<span><strong>Telefone:</strong> <a href="tel:+553135515271">(31) 3551-5271</a>.</span></li>'
 '<li>' + ico('clock', 18) + '<span><strong>Horário:</strong> segunda a sexta, 08:30–19h; '
 'sábado, 08:30–13h; domingo, fechado.</span></li>'
 '</ul>'
 '<a class="btn red sm" href="contato.html">Ver contato e localização ' + ico('arrow', 14) + '</a>'
 '</div>'
 '<div class="panel"><h2>Onde <span class="rl">nos encontrar</span></h2>'
 '<img class="mapbox" src="assets/map.png" alt="Mapa com a localização da Farma Popular na Rua Diogo de Vasconcelos, 39, Ouro Preto">'
 '<a class="maplink" href="https://www.google.com/maps/search/?api=1&query=Rua+Diogo+de+Vasconcelos%2C+39%2C+Ouro+Preto%2C+MG%2C+35400-000" target="_blank" rel="noopener">'
 + ico('pin', 19) + 'Abrir endereço no Google Maps ' + ico('arrow', 14) + '</a>'
 '</div></div>'
 '<div class="sec-head"><div><h2>Como a farmácia <span class="rl">atende você</span></h2>'
 '<p>Serviços informados pela loja. Detalhes e disponibilidade devem ser confirmados pelo telefone ou WhatsApp.</p></div></div>'
 '<div class="info-grid">'
 '<div class="info"><div class="ico">' + ico('bag', 26) + '</div><h3>Compra na loja</h3>'
 '<p>Escolha os produtos diretamente no estabelecimento da Rua Diogo de Vasconcelos, 39.</p></div>'
 '<div class="info"><div class="ico">' + ico('hand', 26) + '</div><h3>Retirada na loja</h3>'
 '<p>Confirme com a equipe como funciona a retirada do seu pedido na farmácia.</p></div>'
 '<div class="info"><div class="ico">' + ico('truck', 26) + '</div><h3>Entrega</h3>'
 '<p>A farmácia informa que realiza entrega. Consulte abrangência e condições diretamente com a loja.</p></div>'
 '</div>'
 '<div class="sec-head"><div><h2>Formas de <span class="rl">pagamento</span></h2>'
 '<p>Informações informadas pela farmácia. Confirme na loja antes de finalizar qualquer compra.</p></div></div>'
 '<div class="info-grid">'
 '<div class="info"><div class="ico">' + ico('card', 26) + '</div><h3>Cartões</h3>'
 '<p>Cartão de crédito e cartão de débito.</p></div>'
 '<div class="info"><div class="ico">' + ico('cheque', 26) + '</div><h3>Cheques</h3>'
 '<p>Cheques são informados como forma de pagamento. Confirme as condições na loja.</p></div>'
 '<div class="info"><div class="ico">' + ico('nfc', 26) + '</div><h3>Pagamento por celular</h3>'
 '<p>Pagamento por dispositivo móvel via NFC.</p></div>'
 '</div>'
 '<div class="cta"><div><h2>Precisa de alguma informação? <span>Fale com a gente.</span></h2>'
 '<p>Este site não efetua vendas ou pagamentos online. Pedidos e dúvidas são encaminhados pelo WhatsApp.</p></div>'
 '<a class="btn green" data-wa data-wa-message="Olá! Gostaria de informações sobre a Farma Popular Ouro Preto.">'
 + ico('whatsapp', 19) + 'Falar pelo WhatsApp</a></div>'
 )


def contato_body():
    return (
 '<div class="two">'
 '<div class="panel"><h2>Fale com a <span class="rl">Farma Popular</span></h2>'
 '<p>Use os canais abaixo para tirar dúvidas, consultar disponibilidade ou encaminhar seu pedido. '
 'O site não realiza vendas, carrinho ou pagamento online.</p>'
 '<ul>'
 '<li>' + ico('phone', 18) + '<span><strong>Telefone:</strong> <a href="tel:+553135515271">(31) 3551-5271</a>.</span></li>'
 '<li>' + ico('pin', 18) + '<span><strong>Endereço:</strong> Rua Diogo de Vasconcelos, 39, Ouro Preto – MG, 35400-000.</span></li>'
 '<li>' + ico('clock', 18) + '<span><strong>Horário:</strong> segunda a sexta, 08:30–19h; '
 'sábado, 08:30–13h; domingo, fechado.</span></li>'
 '<li>' + ico('instagram', 18) + '<span><strong>Instagram:</strong> <a href="https://www.instagram.com/farmapopular.ouropreto/" target="_blank" rel="noopener">@farmapopular.ouropreto</a>.</span></li>'
 '<li>' + ico('facebook', 18) + '<span><strong>Facebook:</strong> <a href="https://www.facebook.com/p/Farma-Popular-Ouro-Preto-100064645796782/?locale=pt_BR" target="_blank" rel="noopener">Farma Popular Ouro Preto</a>.</span></li>'
 '</ul>'
 '<a class="btn red sm" data-wa data-wa-message="Olá! Gostaria de consultar disponibilidade e preço na Farma Popular Ouro Preto.">'
 + ico('whatsapp', 17) + 'Pedir pelo WhatsApp</a>'
 '</div>'
 '<div class="panel"><h2>Como <span class="rl">chegar</span></h2>'
 '<img class="mapbox" src="assets/map.png" alt="Mapa com a localização da Farma Popular na Rua Diogo de Vasconcelos, 39, Ouro Preto">'
 '<p>Rua Diogo de Vasconcelos, 39<br>Ouro Preto – MG, 35400-000</p>'
 '<a class="maplink" href="https://www.google.com/maps/search/?api=1&query=Rua+Diogo+de+Vasconcelos%2C+39%2C+Ouro+Preto%2C+MG%2C+35400-000" target="_blank" rel="noopener">'
 + ico('pin', 19) + 'Abrir no Google Maps ' + ico('arrow', 14) + '</a>'
 '</div></div>'
 '<section id="whatsapp" class="panel" style="margin-top:26px">'
 '<h2>Sobre o <span class="rl">WhatsApp</span></h2>'
 '<p>O atendimento pelo WhatsApp usa o número <strong>(31) 3551-5271</strong>, '
 'confirmado em 23/11/2026 pelo link publicado no perfil oficial do Instagram da farmácia.</p>'
 '<p>Ao clicar em qualquer botão de consulta, uma conversa é aberta com o nome e a '
 'apresentação do produto já preenchidos. Você também pode ligar para o número acima '
 'ou usar as redes sociais. O site não realiza vendas nem pagamentos online.</p>'
 '</section>'
 '<div class="info-grid">'
 '<div class="info"><div class="ico">' + ico('bag', 26) + '</div><h3>Compras na loja</h3>'
 '<p>Compre diretamente no estabelecimento.</p></div>'
 '<div class="info"><div class="ico">' + ico('hand', 26) + '</div><h3>Retirada na loja</h3>'
 '<p>Confirme as condições de retirada com a equipe.</p></div>'
 '<div class="info"><div class="ico">' + ico('truck', 26) + '</div><h3>Entrega</h3>'
 '<p>A farmácia informa entrega. Consulte disponibilidade e condições.</p></div>'
 '</div>'
 '<div class="cta"><div><h2>Quer saber se temos o que você precisa? <span>Pergunte pelo WhatsApp.</span></h2>'
 '<p>Não publicamos preços, estoque ou condições confirmadas neste site. Tudo deve ser verificado com a loja.</p></div>'
 '<a class="btn green" data-wa data-wa-message="Olá! Gostaria de consultar a disponibilidade de um produto na Farma Popular Ouro Preto.">'
 + ico('whatsapp', 19) + 'Consultar disponibilidade</a></div>'
 )


TIPS = [
 ('Leia sempre a embalagem e a bula', 'Antes de usar qualquer produto, confira as informações da embalagem e da bula. Em caso de dúvida, peça orientação a um profissional de saúde.'),
 ('Respeite o prazo de validade', 'Verifique a data de validade dos produtos que você guarda em casa e não utilize itens vencidos.'),
 ('Guarde os produtos com segurança', 'Mantenha medicamentos e produtos de cuidado fora do alcance de crianças e em local adequado, conforme a embalagem.'),
 ('Não compartilhe medicamentos', 'Cada pessoa pode ter necessidades diferentes. Evite emprestar ou usar medicamentos indicados para outra pessoa.'),
 ('Anote suas dúvidas', 'Antes de ligar ou escrever para a farmácia, anote o nome do produto e suas dúvidas para agilizar o atendimento.'),
 ('Procure um profissional quando precisar', 'Este conteúdo é apenas informativo e não substitui avaliação, diagnóstico ou recomendação de um profissional de saúde.'),
]


def dicas_body():
    tips = ''.join(
      '<div class="tip"><div class="num">%d</div><div><h3>%s</h3><p>%s</p></div></div>' % (i, escape(t), escape(d))
      for i, (t, d) in enumerate(TIPS, 1))
    return (
 '<div class="notice">' + ico('alert', 22) +
 '<div><strong>Conteúdo informativo geral.</strong> Estas dicas não são recomendações de tratamento, '
 'não substituem orientação profissional e não devem ser usadas para decidir o uso de medicamentos.</div></div>'
 '<div class="sec-head"><div><h2>Cuidados <span class="rl">no dia a dia</span></h2>'
 '<p>Orientações gerais de organização e segurança. Para qualquer dúvida sobre produtos, fale com a farmácia.</p></div></div>'
 '<div class="tips-list">' + tips + '</div>'
 '<div class="cta"><div><h2>Tem alguma dúvida sobre produtos? <span>A Farma Popular pode ajudar.</span></h2>'
 '<p>Consulte disponibilidade, preço e informações diretamente com a equipe pelo WhatsApp ou pelo telefone.</p></div>'
 '<a class="btn green" data-wa data-wa-message="Olá! Tenho uma dúvida sobre produtos da Farma Popular Ouro Preto.">'
 + ico('whatsapp', 19) + 'Falar pelo WhatsApp</a></div>'
 )


# ---------------------------------------------------------------------------
# Páginas legais (modelos ilustrativos)
# ---------------------------------------------------------------------------
def legal_body(page):
    out = ['<div class="panel legal-doc">']
    out.append('<div class="modelalert">' + ico('alert', 22) +
               '<div><strong>MODELO ILUSTRATIVO.</strong> Este texto é genérico e '
               'precisa ser revisado pelo proprietário e por profissional competente '
               'antes da publicação. Campos entre [COLCHETES] devem ser preenchidos.</div></div>')
    out.append('<p class="legal-lead">' + escape(page['lead']) + '</p>')
    for sec in page['sections']:
        out.append('<h2>' + escape(sec['h']) + '</h2>')
        for para in sec.get('p', []):
            out.append('<p>' + escape(para) + '</p>')
        if sec.get('ul'):
            out.append('<ul>' + ''.join('<li>' + escape(x) + '</li>' for x in sec['ul']) + '</ul>')
    out.append('<p class="legal-date">Modelo preparado em 23/11/2026.</p>')
    out.append('</div>')
    return ''.join(out)


# Escrita dos arquivos
# ---------------------------------------------------------------------------
def write(name, content):
    dest = ROOT / public_path(name).lstrip('/')
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(rewrite_links(content), encoding='utf-8')
    print('OK  ' + public_path(name))


def notfound_body():
    return ('<div class="panel">'
      '<p class="legal-lead">O endereço acessado não existe ou foi movido. '
      'Use o menu acima para continuar navegando ou volte para a página inicial.</p>'
      '<p><a class="btn red sm" href="index.html">Ir para a página inicial</a> '
      '<a class="btn green sm" data-wa data-wa-message="Olá! Preciso de ajuda para encontrar um item no site.">'
      + ico('whatsapp', 17) + 'Falar no WhatsApp</a></p>'
      '</div>')


FILES_BY_KEY = {
    'medicamentos': 'medicamentos-e-genericos.html',
    'beleza': 'beleza-e-cuidados.html',
    'higiene': 'higiene-pessoal.html',
    'infantil': 'infantil.html',
    'saude': 'saude-e-bem-estar.html',
    'perfumaria': 'perfumaria.html',
}

SUB_HREF = dict((slug, href) for slug, _label, href in SUBCATS)
MED_URL = public_url('medicamentos-e-genericos.html')


def main():
    SITEMAP.clear()
    register('/', 1.0, 'weekly')  # home (index.html, mantida à mão)

    # Categorias ilustrativas (sem medicamentos — esses têm catálogo próprio)
    for key, title, script, desc, crumb in CATEGORY_PAGES:
        if key == 'medicamentos':
            continue
        name = FILES_BY_KEY[key]
        emit(name, key, title, script, desc, crumb, category_body(key),
             page_type='CollectionPage', priority=0.7)

    # Listagem geral e listagens por subcategoria (medicamentos reais)
    emit('medicamentos-e-genericos.html', 'medicamentos', 'Medicamentos e Genéricos',
         'Ouro Preto',
         'Medicamentos reais com registro ativo na Anvisa. Vitrine informativa: preço e disponibilidade são confirmados na farmácia.',
         'Medicamentos e Genéricos', medicine_listing_body(''),
         page_type='CollectionPage', priority=0.9, changefreq='weekly')
    for slug, label, href in SUBCATS:
        emit(href, 'medicamentos', label + ' — Medicamentos', 'Ouro Preto',
             'Medicamentos de %s com registro ativo na Anvisa. Consulte disponibilidade e preço na farmácia.' % label,
             'Medicamentos e Genéricos › ' + label, medicine_listing_body(slug),
             page_type='CollectionPage', priority=0.8,
             trail=[('Medicamentos e Genéricos', MED_URL),
                    (label, public_url(href))])

    # Páginas de detalhe dos medicamentos
    for m in MEDICINES:
        name = 'produto-%s.html' % m['slug']
        emit(name, 'medicamentos', m['name'], 'Ouro Preto',
             'Ficha informativa de %s (%s). Registro Anvisa %s. Vitrine informativa — sem venda online.' % (
                 m['name'], m['substance'], m['reg']),
             'Medicamentos e Genéricos › %s › %s' % (SUB_LABEL[m['sub']], m['name']),
             detail_body(m), page_type='ItemPage', priority=0.7,
             trail=[('Medicamentos e Genéricos', MED_URL),
                    (SUB_LABEL[m['sub']], public_url(SUB_HREF[m['sub']])),
                    (m['name'], public_url(name))])

    emit('sobre.html', 'sobre', 'Sobre a Farmácia', 'Ouro Preto',
         'Informações sobre a Farma Popular Ouro Preto: endereço, horário informado, serviços e formas de pagamento.',
         'Sobre a farmácia', sobre_body(), page_type='AboutPage', priority=0.6)
    emit('contato.html', 'contato', 'Contato e Localização', 'Ouro Preto',
         'Telefone, endereço, Google Maps, redes sociais e horário informado da Farma Popular Ouro Preto.',
         'Contato e localização', contato_body(), page_type='ContactPage', priority=0.7)
    emit('dicas-de-saude.html', 'dicas', 'Dicas de Saúde', 'Ouro Preto',
         'Orientações gerais e informativas de organização e segurança. Não é recomendação de tratamento.',
         'Dicas de Saúde', dicas_body(), priority=0.6)

    # Páginas legais / obrigatórias: modelos ainda não revisados → noindex
    for doc in LEGAL_PAGES:
        emit(doc['file'], 'sobre', doc['title'], doc['script'], doc['desc'],
             doc['crumb'], legal_body(doc), indexable=False,
             priority=0.3, changefreq='yearly')

    # Página 404 (Vercel serve dist/404.html automaticamente)
    emit('404.html', 'inicio', 'Página não encontrada', 'Ops!',
         'O endereço acessado não existe ou foi movido. Volte para a página inicial.',
         'Página não encontrada', notfound_body(), indexable=False)

    return SITEMAP


if __name__ == '__main__':
    main()
