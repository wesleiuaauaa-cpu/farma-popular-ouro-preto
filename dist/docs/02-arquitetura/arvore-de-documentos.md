# Árvore de documentos

Este é o documento **sobre os documentos**: um inventário que explica para que
cada arquivo serve, quem deve lê-lo e quando atualizá-lo. Não contém regras de
negócio nem dados da farmácia — apenas orienta a navegação.

O índice de entrada está em `docs/README.md`; aqui o foco é o **inventário e as
regras de manutenção**.

## Estrutura completa

```
README.md                                   ← único documento na raiz (GitHub)
docs/
├── README.md                               ← índice de entrada
├── 01-visao-geral/
│   └── escopo-e-objetivos.md               ← o que o site faz e não faz
├── 02-arquitetura/
│   ├── arquitetura-hexagonal.md            ← camadas, portas e adaptadores
│   ├── arvore-de-pastas.md                 ← onde cada coisa vive e por quê
│   ├── arvore-de-documentos.md             ← este inventário
│   └── identidade-visual.md                ← cores, tipografia, componentes
├── 03-decisoes/
│   ├── README.md                           ← índice das ADRs
│   ├── ADR-001-site-estatico.md
│   ├── ADR-002-gerador-unico.md
│   ├── ADR-003-fotos-autorizadas.md
│   ├── ADR-004-paginas-legais.md
│   └── ADR-005-consentimento-cookies.md
├── 04-operacao/
│   ├── build-e-deploy.md                   ← build local e Vercel
│   ├── auditoria.md                        ← veredito e evidências
│   └── validacao.md                        ← comandos e checklist
└── 05-dominio/
    ├── fontes-e-dados.md                   ← origem de dados, registros e fotos
    ├── catalogo.md                         ← medicamentos e vitrines
    └── pendencias.md                       ← o que depende de decisão humana
```

## Inventário

| Documento | Para que serve | Público | Quando atualizar |
|---|---|---|---|
| `README.md` | Visão geral, rotas, dados confirmados e comandos | Quem chega ao repositório | Ao mudar rotas, dados da loja ou entrypoints |
| `docs/README.md` | Índice e convenção de numeração | Todo mundo | Ao criar ou renomear um documento |
| `docs/01-visao-geral/escopo-e-objetivos.md` | Limites do produto e públicos | Dono do projeto e equipe | Ao mudar o que o site faz ou deixa de fazer |
| `docs/02-arquitetura/arquitetura-hexagonal.md` | Camadas, portas e direção das dependências | Quem desenvolve | Ao alterar a estrutura de `src/` |
| `docs/02-arquitetura/arvore-de-pastas.md` | Mapa físico do repositório | Quem desenvolve | Ao criar/mover pastas |
| `docs/02-arquitetura/arvore-de-documentos.md` | Inventário e regras da documentação | Quem escreve documentação | Ao criar, renomear ou apagar um `.md` |
| `docs/02-arquitetura/identidade-visual.md` | Tokens, tipografia, componentes e regras de uso | Designer e quem altera o visual | Ao alterar cores, fontes ou componentes |
| `docs/03-decisoes/README.md` | Índice das decisões registradas | Quem questiona uma escolha | Ao registrar uma nova decisão |
| `docs/03-decisoes/ADR-*.md` | Contexto, decisão e consequências | Quem vai manter no longo prazo | Ao tomar/reverter uma decisão estrutural |
| `docs/04-operacao/build-e-deploy.md` | Build local e publicação na Vercel | Quem publica | Ao mudar o build ou a hospedagem |
| `docs/04-operacao/auditoria.md` | Veredito e evidências de prontidão | Dono do projeto | Antes de cada publicação relevante |
| `docs/04-operacao/validacao.md` | Comandos e checklist visual | Quem valida | Ao mudar os scripts de checagem |
| `docs/05-dominio/fontes-e-dados.md` | Origem dos dados, registros e fotos | Quem revisa conteúdo e direitos | Ao trocar uma fonte, foto ou dado |
| `docs/05-dominio/catalogo.md` | O que está cadastrado e o que é pendente | Quem revisa o catálogo | Ao adicionar/alterar produtos |
| `docs/05-dominio/pendencias.md` | Consolidação do que depende de pessoa | Dono do projeto | Ao confirmar ou resolver uma pendência |

## O que **não** é documentação

Estes arquivos vivem na raiz, mas são **entrypoints**, não documentos descritivos:

- `build_pages.py`, `build_site.py`, `validate_site.py`, `research_anvisa.py`,
  `src/domain/legal.py` — wrappers finos que delegam para `src/`.
- `vercel.json` — configuração da hospedagem.
- `.gitignore` — regras do Git.

O conteúdo real desses entrypoints está em `src/domain`, `src/application`,
`src/infrastructure` e `src/interface`.

## Regras de manutenção

1. **Fonte única da verdade.** Dados de medicamentos, vitrines e textos legais
   vivem em `src/`. A documentação descreve; nunca duplica para "facilitar".
2. **Home é exceção.** `index.html` preserva a identidade aprovada. Mudanças
   estruturais nela precisam ser replicadas no gerador e no `assets/css/site.css`.
3. **Documento novo, índice novo.** Ao criar um `.md`, inclua-o no inventário
   acima e em `docs/README.md`.
4. **Pendência não é erro escondido.** Se algo não foi confirmado, registre em
   `docs/05-dominio/pendencias.md` e mantenha o aviso visível no site.
5. **Auditoria antes de publicar.** Rode `python build_site.py`,
   `python validate_site.py` e confira `git status --short`.
6. **Decisões novas, ADRs novos.** Não reescreva o passado: escreva um novo ADR
   que revogue o anterior.
