# Fontes dos dados e pendências de confirmação

Este documento registra a origem das informações do catálogo demonstrativo de medicamentos
da Farma Popular Ouro Preto.

## Fontes consultadas

| Fonte | Uso | Data da consulta |
|---|---|---|
| [Anvisa — Dados Abertos, base de medicamentos](https://dados.anvisa.gov.br/dados/CONSULTAS/PRODUTOS/TA_CONSULTA_MEDICAMENTOS.CSV) (`TA_CONSULTA_MEDICAMENTOS.CSV`) | Nome do produto, substância(s), detentor do registro, classificação regulatória, número de registro, situação e produto de referência | 16/11/2026 |
| [Anvisa — Bulário Eletrônico](https://consultas.anvisa.gov.br/#/bulario/) | Link oficial para consulta de bulas (a busca é feita pelo número de registro) | 16/11/2026 |
| [Site oficial Novalgina](https://www.novalgina.com.br/) | Apresentações relacionadas pelo fabricante (comprimidos 1 g, 500 mg, solução oral, gotas, efervescente 1 g e supositório) | 16/11/2026 |
| Ficha da empresa no Google Maps (dados enviados pelo proprietário) | Endereço, telefone e horários completos | 23/11/2026 |
| Link publicado no perfil oficial do Instagram da farmácia (`farmapopular.ouropreto`), redirecionando para `https://wa.me/553135515271` | Confirmação de que o telefone (31) 3551-5271 é o canal oficial de WhatsApp | 23/11/2026 |
| Confirmação do proprietário da farmácia (registrada neste projeto) | Autorização para usar fotografias de embalagens no site | 23/11/2026 |

O script `research_anvisa.py` reproduz a leitura da base oficial e o resumo da situação
dos registros. A base é exportada em UTF-8/CP1252, delimitada por `;`.

**Drogaria Araujo:** citada apenas como referência geral de boas práticas de organização
de vitrine farmacêutica. Nenhum texto, imagem, código, marca, componente ou elemento de
identidade visual foi copiado. Cores, tipografia, tokens e componentes continuam sendo
os da Farma Popular Ouro Preto.

## Medicamentos cadastrados e registros verificados

Todos os registros abaixo apresentam **situação ativa** em pelo menos uma apresentação
na base oficial consultada em 16/11/2026.

| Produto | Princípio ativo (dado Anvisa) | Registro Anvisa | Detentor do registro (dado Anvisa) |
|---|---|---|---|
| Novalgina | dipirona monoidratada | 186200018 | Opella Healthcare Brazil Ltda |
| Tylenol | paracetamol | 157211214 | Kenvue Ltda. |
| Alivium | ibuprofeno | 178170807 | Cosmed Indústria de Cosméticos e Medicamentos S.A. |
| Paracetamol + clorfeniramina + fenilefrina | paracetamol, maleato de clorfeniramina, cloridrato de fenilefrina | 143810263 | Cimed Indústria S.A |
| Loratadina — Genérico | loratadina | 155840465 | Brainfarma Indústria Química e Farmacêutica S.A |
| Dicloridrato de cetirizina — Genérico | dicloridrato de cetirizina | 103700518 | Laboratório Teuto Brasileiro S/A |
| Omeprazol — Genérico | omeprazol | 105830969 | Germed Farmacêutica Ltda |

> Observação: Tylenol (157211214) e Alivium (178170807) também possuem linhas com
> situação "Inativo" na base — referentes a apresentações mais antigas. Por isso o site
> informa "situação ativa na consulta" em vez de afirmar que todas as apresentações estão ativas.

## Imagens

Em **23/11/2026** o proprietário confirmou autorização para usar fotografias de
embalagens no site. As sete fotos abaixo foram baixadas, normalizadas para WebP
(máx. 900×900) e salvas localmente em `assets/produtos/`, para não depender de CDNs
de terceiros. Os cartões e as fichas passaram a exibir o selo **"FOTO DO PRODUTO"**.

| Arquivo | Produto | Foto obtida de |
|---|---|---|
| `novalgina.webp` | Novalgina | Drogaria Araujo (`novalgina-1g-10-comprimidos`) |
| `tylenol.webp` | Tylenol | Drogasil (`tylenol-500mg-10-comprimidos`) |
| `alivium.webp` | Alivium | Pague Menos (`alivium-400mg-10-comprimidos`) |
| `paracetamol-clorfeniramina-fenilefrina.webp` | Paracetamol + clorfeniramina + fenilefrina | Drogasil (`Resfenol 5 cápsulas`) — produto de referência do registro 143810263 |
| `loratadina-generico.webp` | Loratadina genérico | Droga Raia / Drogasil (`loratadina 10 mg genérico`) |
| `cetirizina-generico.webp` | Dicloridrato de cetirizina genérico | Cosmos (`cetirizina 10 mg Medley, 12 comprimidos`) |
| `omeprazol-generico.webp` | Omeprazol genérico | Cosmos (`omeprazol 20 mg EMS, 28 cápsulas`) |

**Ressalva mantida no site:** as fotos mostram embalagens de referência. Para os
quatro genéricos não foi encontrada foto do lote do detentor do registro cadastrado
(Brainfarma, Cimed, Teuto e Germed), então a imagem pode apresentar outro fabricante
ou outra apresentação. Por isso o site continua afirmando que apresentação,
concentração, forma e quantidade da embalagem são **dados pendentes**, e as fichas
e a vitrine dizem explicitamente que a embalagem fotografada pode diferir do item
disponível na loja.

Se a farmácia tiver fotos das embalagens que realmente vende, basta substituir os
arquivos em `assets/produtos/` mantendo os mesmos nomes — nenhuma outra alteração
no gerador `build_pages.py` é necessária.

As demais cinco vitrines também passaram a usar fotos reais em **23/11/2026**,
com autorização do proprietário. Cada agente pesquisou uma categoria; as 25 fotos
foram baixadas, normalizadas (WebP, até 900×900, fundo branco) e salvas localmente.
Os cartões exibem **FOTO DO PRODUTO** e o aviso de que marca e apresentação podem
diferir do item disponível na loja.

| Categoria | Arquivo | Foto obtida de |
|---|---|---|
| Beleza e Cuidados | `beleza-bisnaga-creme.webp` | Farmax Loja (creme para mãos Farmax) |
| Beleza e Cuidados | `beleza-frasco-shampoo.webp` | Walmart (shampoo Equate Coconut Milk) |
| Beleza e Cuidados | `beleza-sabonete.webp` | Freepik (foto livre, sabonete branco) |
| Beleza e Cuidados | `beleza-protetor-solar.webp` | Cirúrgica Salutar (protetor solar Nutriex FPS 60) |
| Beleza e Cuidados | `beleza-desodorante.webp` | Mais Viva (desodorante roll-on +Viva) |
| Higiene Pessoal | `higiene-pasta-dental.webp` | Freepik (bisnaga branca genérica) |
| Higiene Pessoal | `higiene-escova-dental.webp` | Freepik (escova com pasta) |
| Higiene Pessoal | `higiene-sabonete.webp` | Freepik (barra de sabão) |
| Higiene Pessoal | `higiene-alcool-gel.webp` | Farmam (álcool em gel 70%, 250 ml) |
| Higiene Pessoal | `higiene-luvas.webp` | Fastepis (luvas de látex Inoven) |
| Infantil | `infantil-mamadeira.webp` | Drogaria São Paulo (mamadeira Petita 125 ml) |
| Infantil | `infantil-creme-bebe.webp` | Freepik (pote de creme genérico) |
| Infantil | `infantil-sabonete.webp` | Drogaria São Paulo (sabonete Bebê Vida, Davene) |
| Infantil | `infantil-shampoo.webp` | Walmart (shampoo Johnson's Calming) |
| Infantil | `infantil-termometro.webp` | Soluciones Médicas (termômetro digital) |
| Saúde e Bem-estar | `saude-suplemento.webp` | Claroshop (vitamina D3 Naturagel) |
| Saúde e Bem-estar | `saude-termometro.webp` | Soluciones Médicas (termômetro digital) |
| Saúde e Bem-estar | `saude-protetor-solar.webp` | Net Suprimentos (Nutriex FPS 60) |
| Saúde e Bem-estar | `saude-alcool-gel.webp` | Doce Erva (álcool em gel 70%) |
| Saúde e Bem-estar | `saude-luvas.webp` | Kajavet (luvas nitrílicas Talge) |
| Perfumaria | `perfumaria-perfume.webp` | Sanborns (perfume Calvin Klein Eternity) |
| Perfumaria | `perfumaria-desodorante.webp` | Alara Perú (desodorante Dove) |
| Perfumaria | `perfumaria-creme-perfumado.webp` | Drogaria Araujo (creme Creamy Skincare) |
| Perfumaria | `perfumaria-sabonete.webp` | Farmagerty (sabonete Granado) |
| Perfumaria | `perfumaria-body-splash.webp` | Vogue / Globo (body splash Cuide-se Bem) |

> **Atenção às fontes:** algumas fotos vêm de bancos de imagens (Freepik, inclusive
> uma imagem "premium") e de matéria editorial (Vogue/Globo). Embora o proprietário
> tenha autorizado o uso de fotos de produtos, vale confirmar se essas fontes específicas
> exigem licença ou atribuição antes de publicar. Se preferir, troque apenas os arquivos
> em `assets/produtos/` mantendo os mesmos nomes — o site não muda.

As fotos são **exemplos de produtos**, não um compromisso de que a marca ou a
apresentação fotografada esteja disponível na Farma Popular. Preço, estoque e
disponibilidade continuam sem publicação no site.

## Dados confirmados em 23/11/2026

- **WhatsApp confirmado:** o próprio perfil do Instagram da farmácia publica um link
  para `https://wa.me/553135515271`. `SITE_CONFIG.whatsappVerified` foi ajustado para
  `true` e todos os botões passaram a abrir `wa.me` com mensagem pré-preenchida.
- **Horários confirmados:** segunda a sexta, 08:30–19h; sábado, 08:30–13h; domingo,
  fechado. Publicados na barra superior, no rodapé e nas páginas Sobre e Contato.
- **Endereço e telefone:** R. Diogo de Vasconcelos, 39, Ouro Preto/MG, 35400-000 e
  (31) 3551-5271 — já presentes no site.

> Uma avaliação pública no Google diz "Ninguém atende o telefone!". Isso reforça a
> preferência pelo WhatsApp como canal de pedido, mas não foi usado para alterar dados
> da farmácia nem para publicar a avaliação no site.

## Dados ainda pendentes de confirmação

- **Apresentação, concentração, forma farmacêutica e quantidade da embalagem:** não
  confirmados na base de dados abertos para a maioria dos itens. Exceção: Novalgina,
  cujas linhas de apresentação constam no site oficial do fabricante.
- **Bula específica por registro:** o site abre o Bulário da Anvisa e informa o número
  de registro para a busca; não há links diretos para PDFs verificados.
- **Preço, estoque e disponibilidade local:** nunca publicados — devem ser confirmados
  com a farmácia.

## Regras editoriais adotadas

- Nenhuma indicação terapêutica, contraindicação, posologia ou modo de uso foi escrito.
- Nenhum dado de bula foi transcrito sem fonte oficial.
- Nenhuma informação de preço, estoque ou condição comercial foi inventada.
- Todas as páginas de medicamentos reforçam que se trata de vitrine informativa e que
  a venda é fechada diretamente com a Farma Popular Ouro Preto.
