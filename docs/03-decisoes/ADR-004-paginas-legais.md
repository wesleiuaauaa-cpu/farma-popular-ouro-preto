# ADR-004 — Páginas legais como modelos ilustrativos

- **Data:** 23/11/2026
- **Status:** Aceita, pendente de revisão

## Contexto
O site lida com medicamentos e coleta consentimento de cookies. Mesmo sem
formulários, são esperadas Política de Privacidade, Termos de Uso, Política de
Cookies, Aviso de Responsabilidade e condições de entrega/troca. Os dados
jurídicos reais (CNPJ, razão social, DPO, prazos) não foram fornecidos.

## Decisão
Criar as cinco páginas com texto genérico, campos entre `[COLCHETES]` e um selo
visível "MODELO ILUSTRATIVO". O conteúdo vive em `src/domain/legal.py`.

## Consequências
- Nenhum dado jurídico foi inventado.
- O selo só deve ser removido após preenchimento e revisão por profissional competente.
- A publicação pública fica condicionada a essa revisão (ver `docs/04-operacao/auditoria.md`).
