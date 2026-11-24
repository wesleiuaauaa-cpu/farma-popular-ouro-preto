# Escopo e objetivos

## O que é

Site institucional e vitrine informativa da **Farma Popular Ouro Preto**, com
navegação real entre categorias, fichas de medicamentos com dados registrados na
Anvisa, páginas de conteúdo, formulários de contato via WhatsApp e documentos
legais. É um projeto **estático**: não há backend, banco de dados nem login.

## O que o site faz

- Apresenta a farmácia, endereço, telefone, horários e formas de pagamento confirmados.
- Organiza o catálogo em medicamentos (com 4 subcategorias reais) e cinco vitrines de produtos.
- Exibe, para cada medicamento, nome, princípio ativo, detentor do registro e número Anvisa.
- Abre o WhatsApp com mensagem pré-preenchida para consulta de disponibilidade e preço.
- Oferece aviso de cookies com aceite/rejeição e preferência persistida localmente.
- Linka, no rodapé de todas as páginas, os cinco documentos legais.

## O que o site **não** faz

- Não vende, não tem carrinho, checkout, pagamento ou reserva online.
- Não publica preço, estoque ou garantia de disponibilidade.
- Não prescreve, não diagnostica e não substitui a leitura da bula nem o profissional de saúde.
- Não publica avaliações de terceiros nem dados que não foram confirmados pela farmácia.

## Públicos

| Público | O que procura |
|---|---|
| Cliente da farmácia | Produto, endereço, horário, como falar com a loja |
| Proprietário | Confirmar dados, aprovar textos legais, acompanhar pendências |
| Quem desenvolve/manutém | Gerador, camadas, build e deploy |

## Critérios de qualidade adotados

- Identidade visual aprovada na home preservada em todas as páginas.
- Responsividade de 320 px a desktop, sem overflow horizontal.
- Acessibilidade básica: `lang`, skip link, foco visível, `alt`, alvos de toque de 44 px.
- Dados verificáveis: Anvisa para registros, Google/Instagram para dados da loja.
- Build reproduzível e_publicado em `dist/`.
