# ADR-002 — Um gerador central para as páginas internas

- **Data:** 16/11/2026
- **Status:** Aceita

## Contexto
São 25 páginas internas com cabeçalho, rodapé, navegação e cards repetidos.
Editar cada HTML à mão gerou risco de divergência (links diferentes, horários
diferentes, cards desatualizados).

## Decisão
Manter um único gerador (`src/application/generator.py`, antes `build_pages.py`)
como fonte da verdade para páginas internas. Todo conteúdo comum — menu, faixa de
categorias, rodapé, horários, WhatsApp, textos legais — sai dele. A home é
exceção, por preservar a identidade já aprovada.

## Consequências
- Uma mudança de horário ou de número de WhatsApp propaga para todas as páginas.
- Nunca se edita um HTML gerado diretamente; edita-se a fonte e roda-se o build.
- A home exige atenção extra: seu CSS e seu cabeçalho são inline e podem divergir.

## Evolução prevista
Extrair os dados do catálogo para `src/domain/catalog.py`, separando domínio de
renderização. Isso é uma refinamento da mesma decisão, não uma reversão.
