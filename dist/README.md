# Farma Popular Ouro Preto — site institucional

Site estático da Farma Popular Ouro Preto. A home aprovada (`index.html`) foi mantida
visualmente; as páginas internas foram criadas reaproveitando a mesma identidade visual
(cores, fontes, botões, cards e rodapé).

## Rotas criadas

| Página | Arquivo |
|---|---|
| Início (home aprovada) | `index.html` |
| Medicamentos e genéricos (7 medicamentos reais) | `pages/medicamentos/medicamentos-e-genericos.html` |
| Subcategoria: Dor e febre | `pages/medicamentos/medicamentos-dor-e-febre.html` |
| Subcategoria: Gripes e resfriados | `pages/medicamentos/medicamentos-gripes-e-resfriados.html` |
| Subcategoria: Alergias | `pages/medicamentos/medicamentos-alergias.html` |
| Subcategoria: Saúde digestiva | `pages/medicamentos/medicamentos-saude-digestiva.html` |
| Detalhes de cada medicamento (7 páginas) | `pages/medicamentos/produto-<slug>.html` |
| Beleza e cuidados (vitrine com fotos) | `pages/categorias/beleza-e-cuidados.html` |
| Higiene pessoal | `pages/categorias/higiene-pessoal.html` |
| Infantil | `pages/categorias/infantil.html` |
| Saúde e bem-estar | `pages/categorias/saude-e-bem-estar.html` |
| Perfumaria | `pages/categorias/perfumaria.html` |
| Sobre a farmácia | `pages/institucionais/sobre.html` |
| Contato e localização | `pages/institucionais/contato.html` |
| Dicas de saúde | `pages/institucionais/dicas-de-saude.html` |
| Política de Privacidade (modelo) | `pages/legais/politica-de-privacidade.html` |
| Termos de Uso (modelo) | `pages/legais/termos-de-uso.html` |
| Política de Cookies (modelo) | `pages/legais/politica-de-cookies.html` |
| Aviso de Responsabilidade (modelo) | `pages/legais/responsabilidade.html` |
| Entrega e Troca (modelo) | `pages/legais/entrega-e-troca.html` |

As cinco páginas legais estão linkadas no rodapé de **todas** as páginas. O conteúdo
é **modelo ilustrativo** (`src/domain/legal.py`) e precisa ser preenchido/revisado antes
de publicar. O aviso de cookies usa `localStorage` e não carrega nada de terceiros
hoje; a estrutura para scripts opcionais está em `assets/js/site.js`.

O build final para publicação fica em `dist/` (rode `python build_site.py`).
Instruções completas em `docs/04-operacao/build-e-deploy.md`.

## Publicado

- **Produção:** https://farma-popular-ouro-preto.vercel.app
- **Repositório conectado:** https://github.com/wesleiuaauaa-cpu/farma-popular-ouro-preto
- **Projeto na Vercel:** `wesleiuaauaa-6571/farma-popular-ouro-preto`

O push para `main` dispara um novo deploy automático. Cada commit com `dist/`
atualizado vira uma versão pública.

A página extra de **Dicas de Saúde** foi criada para dar destino real aos botões
"Veja mais" e "Conheça nossas dicas" da home.

## ⚠️ Antes de publicar — validar o WhatsApp

**Confirmado em 23/11/2026.** O número **(31) 3551-5271** é o canal oficial de WhatsApp:
o próprio perfil do Instagram da farmácia publica um link para `https://wa.me/553135515271`.
Todos os botões abrem a conversa com nome e apresentação do produto pré-preenchidos.

Configuração centralizada em `assets/js/site.js`:

```js
var SITE_CONFIG = {
  whatsappNumber: '553135515271', // confirmado via Instagram oficial
  whatsappVerified: true,
  defaultMessage: '...'
};
```

Se a loja trocar de número, altere **somente** `whatsappNumber`.

## Dados confirmados em 23/11/2026

- **Horários:** segunda a sexta, 08:30–19h; sábado, 08:30–13h; domingo, fechado
  (ficha da empresa no Google Maps). Publicados na barra superior, rodapé, Sobre e Contato.
- **Endereço:** R. Diogo de Vasconcelos, 39, Ouro Preto/MG, 35400-000.
- **Telefone:** (31) 3551-5271.

## ⚠️ Dados que precisam de confirmação
- **Preços, estoque e condições**: não são publicados. Todos os produtos usam o texto
  "Consulte disponibilidade e preço".
- **Apresentação, concentração, forma e quantidade da embalagem**: não verificados na
  base oficial para a maioria dos medicamentos — marcados como pendentes nas fichas.
- **Imagens**: fotos reais das 7 embalagens e das 5 vitrines de produtos, autorizadas
  pelo proprietário em 23/11/2026 e salvas localmente em `assets/produtos/`.
  Fontes, ressalvas e alerta sobre imagens de bancos em `docs/05-dominio/fontes-e-dados.md`.

## Catálogo de medicamentos (vitrine informativa)

Sete medicamentos reais, com registro ativo verificado na base de dados abertos da Anvisa,
distribuídos em quatro subcategorias com listagens próprias: Dor e febre (3), Gripes e
resfriados (1), Alergias (2) e Saúde digestiva (1). Cada item tem uma página de detalhe
com dados cadastrais, avisos, link para o Bulário da Anvisa e botão de consulta.

A seta do menu em **Medicamentos** agora corresponde a esse submenu real. A seta de
**Beleza e Cuidados** foi removida porque não há subcategorias cadastradas com conteúdo.

Fontes, registros verificados e pendências: **`docs/05-dominio/fontes-e-dados.md`**.

## Dados usados (informados)

- Nome: Farma Popular Ouro Preto
- Endereço: Rua Diogo de Vasconcelos, 39, Ouro Preto – MG, 35400-000
- Telefone: (31) 3551-5271 (`tel:+553135515271`)
- Horário: seg–sex 08:30–19h; sáb 08:30–13h; dom fechado
- Serviços: compra na loja, retirada na loja e entrega
- Pagamento: cartão de crédito, cartão de débito, cheques e NFC
- Instagram: https://www.instagram.com/farmapopular.ouropreto/
- Facebook: https://www.facebook.com/p/Farma-Popular-Ouro-Preto-100064645796782/?locale=pt_BR

> Observação: a home continha marcas de cartão (Visa/Mastercard/Elo) no rodapé que não
> estavam entre as formas de pagamento informadas, substituídas por crédito, débito,
> cheque e NFC. Os horários semanais do mockup voltaram a ser exibidos após confirmação
> pela ficha da empresa no Google Maps em 23/11/2026.

## Funcionalidades

- Navegação consistente em todas as páginas + faixa com as 6 categorias.
- Menu mobile acessível (botão `aria-expanded`, fechar com Esc/fora/clique).
- Busca da home redireciona para `pages/medicamentos/medicamentos-e-genericos.html?q=...` e filtra os
  medicamentos cadastrados (sem backend).
- Botões de consulta com mensagem pré-preenchida contendo nome, princípio ativo e registro
  do medicamento, abertos no WhatsApp validado da farmácia.
- Links para `tel:`, Google Maps e redes sociais.
- Sem carrinho, checkout ou pagamento online.

## Responsividade

Ajustes feitos nos media queries já existentes (sem solução paralela):

- **Breakpoints:** `1024px` (grades 2 colunas), `820px` (menu mobile, coluna única),
  `560px` (produtos 1 coluna, faixa de categorias com rolagem horizontal) e `380px`
  (espaçamentos laterais menores). A home também usa `480px` para tipografia fluida.
- `clamp()` aplicado aos títulos e à tipografia da hero em telas pequenas.
- Alvos de toque ampliados: busca, links do rodapé, migalhas, categorias, itens do menu
  (44 px) e links inline de contato (área de toque estendida sem alterar o layout).
- Menu mobile com `max-height`/`overflow-y`, fechamento por Esc/clique fora e `aria-expanded`.
- Botão flutuante do WhatsApp com `env(safe-area-inset-*)` e espaço extra no rodapé
  para não cobrir conteúdo.
- Mapa das páginas institucionais em proporção fixa (`object-fit: contain`) em telas estreitas.

## Impeccable (qualidade visual)

O projeto usa a skill Impeccable v4.10.0 instalada em `.opencode/skills/impeccable`
(comando `/impeccable`). A identidade visual está documentada em `docs/02-arquitetura/identidade-visual.md` e no
sidecar `.impeccable/design.json`. Relatórios de auditoria ficam em `.impeccable/audit/`.

Última auditoria: **18/20 (Excellent)** — sem P0/P1/P2; 3 avisos P3 de ritmo de texto.

## Manutenção

As páginas internas são geradas por `build_pages.py` para manter navegação, cards e
rodapé idênticos. Depois de editar o script:

```bash
python build_pages.py
python validate_site.py   # checa links internos e arquivos locais
```

## Organização do código (hexagonal)

O código vivo em `src/`, separado por responsabilidade:

- `src/domain/` — núcleo: dados e regras do negócio (textos legais).
- `src/application/` — casos de uso: geração das páginas.
- `src/infrastructure/` — adaptadores: build em `dist/` e validação.
- `src/interface/` — adaptador de entrada: pesquisa na base da Anvisa.

Na raiz ficam apenas entrypoints finos com os mesmos nomes de sempre
(`build_pages.py`, `build_site.py`, `validate_site.py`, `research_anvisa.py`,
`src/domain/legal.py`). Detalhes em `docs/02-arquitetura/arquitetura-hexagonal.md`
e `docs/02-arquitetura/arvore-de-pastas.md`.

A documentação está em árvore temática em `docs/`; comece por `docs/README.md`.

Arquivos compartilhados:

- `assets/css/site.css` — estilos das páginas internas
- `assets/js/site.js` — configuração do WhatsApp, menu e busca
- `research_anvisa.py` — reproduz a consulta à base oficial da Anvisa usada no catálogo
- `docs/05-dominio/fontes-e-dados.md` — fontes, registros verificados e pendências de confirmação
- `docs/04-operacao/auditoria.md` — veredito de prontidão para build/publicação e evidências
- `docs/04-operacao/build-e-deploy.md` — passo a passo de build e deploy na Vercel
- `docs/README.md` — índice que explica toda a documentação do projeto
- `assets/produtos/*.webp` — 32 fotos reais (7 medicamentos + 5 vitrines × 5 itens)
- `assets/produtos/*.svg` — ilustrações antigas mantidas apenas como referência

Para testar localmente:

```bash
python -m http.server 8765
# http://localhost:8765/index.html
```
