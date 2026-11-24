# Mapa da documentação

Este é o documento **sobre os documentos** do projeto: um índice que explica para que
cada arquivo serve, quem deve lê-lo e quando atualizá-lo. Ele não contém regras de
negócio nem dados da farmácia — apenas orienta a navegação.

## Como a documentação está organizada

```
Projeto
├── README.md              ← comece aqui
├── DESIGN.md              ← identidade visual
├── docs/
│   ├── MAPA_DOCUMENTACAO.md   ← este arquivo (índice)
│   ├── AUDITORIA.md           ← prontidão para build/publicação
│   ├── DEPLOY.md              ← como subir na Vercel
│   └── fontes.md              ← origem dos dados e fotos
├── build_pages.py         ← gerador das páginas internas
├── build_site.py          ← gerador do dist/
├── legal_content.py       ← textos dos modelos legais
├── research_anvisa.py     ← pesquisa reproduzível na Anvisa
├── validate_site.py       ← validação rápida de links/arquivos
└── vercel.json            ← configuração de publicação
```

## Inventário

| Documento | Para que serve | Público | Quando atualizar |
|---|---|---|---|
| `README.md` | Visão geral, rotas, dados confirmados, funcionamento e manutenção | Quem vai mexer no projeto | Ao mudar rotas, dados da loja ou configuração |
| `DESIGN.md` | Sistema visual: cores, tipografia, tokens, componentes e regras de uso | Designer ou quem alterar o visual | Ao alterar identidade, cores ou componentes |
| `docs/MAPA_DOCUMENTACAO.md` | Explica o próprio conjunto de documentos | Todo mundo, especialmente quem chega agora | Ao criar, renomear ou apagar um documento |
| `docs/AUDITORIA.md` | Veredito e evidências de prontidão para build/publicação | Dono do projeto e quem vai publicar | Antes de cada publicação relevante |
| `docs/DEPLOY.md` | Passo a passo do build local e do deploy na Vercel | Quem vai publicar | Ao mudar o processo de build ou de hospedagem |
| `docs/fontes.md` | Fontes dos dados (Anvisa, Google, Instagram) e de todas as fotos, com pendências | Quem revisa conteúdo e direitos de imagem | Ao trocar foto, dado ou pendência |
| `vercel.json` | Configuração técnica da Vercel (output, URLs limpas) | Ferramenta / quem publica | Ao mudar a pasta de build ou o comportamento de URLs |

## Documentos que **não** são documentação

Estes arquivos aparecem na raiz, mas são código ou apoio técnico — não devem ser
confundidos com documentos descritivos:

- `build_pages.py`: gera as 25 páginas internas a partir dos dados centralizados.
- `build_site.py`: copia tudo para `dist/`.
- `legal_content.py`: conteúdo dos modelos legais (é **dado**, não relatório).
- `research_anvisa.py`: reproduz a consulta à base aberta da Anvisa.
- `validate_site.py`: verifica links e arquivos localmente.
- `.impeccable/design.json` e `.impeccable/audit/`: apoio da ferramenta de design/auditoria visual; não são documentação de projeto.

## Regras simples de manutenção

1. **Fonte única da verdade.** Dados de medicamentos, vitrines, horários e textos legais
   vivem nos `.py`, não repetidos em cada HTML. As páginas são geradas; edite o gerador
   e rode `python build_site.py`.
2. **Home é exceção.** `index.html` mantém a identidade visual aprovada e é ajustada
   à mão. Mudanças estruturais nela precisam ser replicadas no `build_pages.py`
   (cabeçalho, rodapé e CSS inline) para não haver divergência.
3. **Documento novo, índice novo.** Ao adicionar um `.md` em `docs/`, inclua uma linha
   no inventário acima e, se for público, adicione-o ao `build_site.py` na lista
   `PUBLIC_MD`.
4. **Pendência não é erro escondido.** Se algo não foi confirmado (preço, bula,
   licença de imagem, campo legal), registre em `docs/fontes.md` ou `docs/AUDITORIA.md`
   e mantenha o aviso visível no site. Nunca invente o dado para "completar".
5. **Auditoria antes de publicar.** Rode `python build_site.py`, `python validate_site.py`
   e confira `git status --short` (deve ficar limpo). O detalhamento está em
   `docs/AUDITORIA.md`.

## Estado atual resumido

- Build reproduzível, 26 páginas, repositório sincronizado.
- 104 verificações de navegador sem problemas.
- Pendências humanas: 13 campos legais, revisão jurídica e licença de algumas fotos.

O veredito completo e os números estão em `docs/AUDITORIA.md`.
