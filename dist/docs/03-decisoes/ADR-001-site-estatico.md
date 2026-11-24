# ADR-001 — Site estático, sem backend

- **Data:** 16/11/2026
- **Status:** Aceita

## Contexto
A farmácia precisa de presença online com catálogo informativo, contato e páginas
institucionais. Não há equipe para manter servidor, banco ou sistema de pedidos.
Além disso, medicamentos não podem ser vendidoslivremente sem receita e sem
dispensação presencial.

## Decisão
Publicar um site estático (HTML/CSS/JS), sem carrinho, checkout, pagamento,
cadastro ou estoque. Toda consulta é encaminhada ao WhatsApp ou telefone.

## Consequências
- Baixo custo, hospedagem simples (Vercel ou qualquer CDN), sem superfície de ataque de servidor.
- Preço, estoque e disponibilidade nunca são afirmados no site — são confirmados na loja.
- Busca e filtros funcionam no cliente, sobre dados já presentes na página.
- Qualquer funcionalidade transacional futura exigirá nova decisão e novo ADR.
