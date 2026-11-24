# ADR-005 — Consentimento em localStorage, scripts opcionais desligados

- **Data:** 23/11/2026
- **Status:** Aceita

## Contexto
Ferramentas de análise e publicidade podem ser adicionadas depois. A LGPD exige
consentimento prévio para cookies não essenciais.

## Decisão
Exibir aviso com "Aceitar cookies" e "Rejeitar opcionais", salvar a escolha em
`localStorage` (`fp_cookie_consent`) e oferecer "Preferências de cookies" no
rodapé para alterar a decisão. Nenhum script opcional é carregado hoje; deixar
um array `OPTIONAL_SCRIPTS` em `assets/js/site.js` para uso futuro.

## Consequências
- A escolha persiste entre visitas e é reversível pelo usuário.
- Ao adicionar Analytics, basta registrar o script no array — ele só injeta
  depois do aceite, e a Política de Cookies deve ser atualizada.
- Bloquear `localStorage` no navegador faz o aviso reaparecer; isso é aceitável.
