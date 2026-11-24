# Decisões de arquitetura (ADRs)

Cada ADR registra uma decisão que seria fácil de questionar no futuro. O formato
é curto: **contexto → decisão → consequências**. ADRs não são regras absolutas;
se uma decisão for revertida, escreva um novo ADR em vez de apagar o antigo.

| ADR | Decisão | Status |
|---|---|---|
| [001](ADR-001-site-estatico.md) | Site estático, sem backend | Aceita |
| [002](ADR-002-gerador-unico.md) | Um gerador central para as páginas internas | Aceita |
| [003](ADR-003-fotos-autorizadas.md) | Fotos reais somente com autorização; antes, ilustrações rotuladas | Aceita (com ressalva de licença) |
| [004](ADR-004-paginas-legais.md) | Páginas legais como modelos ilustrativos, revisáveis | Aceita (pendente de revisão) |
| [005](ADR-005-consentimento-cookies.md) | Consentimento em `localStorage`, scripts opcionais desligados | Aceita |
