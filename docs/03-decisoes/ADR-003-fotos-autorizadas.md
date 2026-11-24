# ADR-003 — Fotos reais somente com autorização

- **Data:** 23/11/2026
- **Status:** Aceita, com ressalva

## Contexto
As primeiras versões usavam ilustrações SVG rotuladas "ILUSTRAÇÃO — NÃO É FOTO
DA EMBALAGEM", porque packshots de fabricantes são material protegido. O
proprietário confirmou posteriormente autorização para usar fotos de produtos.

## Decisão
Baixar fotos reais, normalizá-las para WebP e salvá-las localmente em
`assets/produtos/`, substituindo as ilustrações nos 7 medicamentos e nas 5
vitrines. Manter o aviso de que marca e apresentação podem diferir do item
disponível na loja.

## Consequências
- O site não depende de CDN de terceiros para exibir as fotos.
- Fotos de bancos de imagem e de matéria editorial ainda precisam de confirmação
  de licença/atribuição — registrado em `docs/05-dominio/fontes-e-dados.md`.
- Se a farmácia tiver fotos das embalagens que realmente vende, basta trocar os
  arquivos mantendo os nomes.
