# Documentação do projeto

Esta pasta contém a documentação do site **Farma Popular Ouro Preto**. O documento
de entrada do repositório é o `README.md` da raiz (convenção do GitHub); aqui a
documentação é organizada por responsabilidade, seguindo a mesma separação de
preocupações usada no código.

## Árvore

```
docs/
├── README.md                       ← este índice
├── 01-visao-geral/
│   └── escopo-e-objetivos.md       ← o que o site faz e o que não faz
├── 02-arquitetura/
│   ├── arquitetura-hexagonal.md    ← camadas, portas e adaptadores
│   ├── arvore-de-pastas.md         ← onde cada coisa vive e por quê
│   ├── arvore-de-documentos.md     ← inventário e regras da documentação
│   └── identidade-visual.md        ← cores, tipografia e componentes
├── 03-decisoes/
│   ├── README.md                   ← índice das decisões (ADRs)
│   ├── ADR-001-site-estatico.md
│   ├── ADR-002-gerador-unico.md
│   ├── ADR-003-fotos-autorizadas.md
│   ├── ADR-004-paginas-legais.md
│   └── ADR-005-consentimento-cookies.md
├── 04-operacao/
│   ├── build-e-deploy.md           ← build local e Vercel
│   ├── auditoria.md                ← veredito e evidências
│   └── validacao.md                ← comandos de conferência
└── 05-dominio/
    ├── fontes-e-dados.md           ← origem dos dados, registros e fotos
    ├── catalogo.md                 ← medicamentos e vitrines
    └── pendencias.md               ← o que depende de decisão humana
```

## Convenção de numeração

Os diretórios `01` a `05` são apenas ordem de leitura. Eles não afetam o build e
podem ser renomeados desde que os links sejam atualizados. A sequência vai do
mais geral para o mais específico:

1. **Visão geral** — contexto para quem chega agora.
2. **Arquitetura** — como o projeto está estruturado.
3. **Decisões** — por que escolhemos cada caminho (ADRs).
4. **Operação** — como gerar, validar e publicar.
5. **Domínio** — dados, conteúdo e pendências do negócio.

## Regra de ouro

Se uma informação precisa ser usada pelo gerador, ela mora em código
(`src/domain/`) e a documentação apenas a descreve. Nunca edite um HTML gerado
para corrigir conteúdo — edite a fonte em `src/` e rode `python build_site.py`.
