# Arquitetura hexagonal (portas e adaptadores)

O projeto é small e estático, mas segue a mesma separação de preocupações da
arquitetura hexagonal: **regras e dados no centro, detalhes técnicos na borda**.
Isso evita que mudança de hospedagem, de ferramenta de validação ou de形式 de
saída obrigue a reescrever o catálogo.

## Camadas na prática

```
src/
├── domain/          NÚCLEO — dados e regras do negócio, sem dependência de I/O
│   └── legal.py         textos dos documentos legais (modelos)
├── application/     CASOS DE USO — monta as páginas a partir do núcleo
│   └── generator.py     header, footer, cards, fichas e renderização
├── infrastructure/  ADAPTADORES — filesystem, validação e build
│   ├── build.py         gera dist/
│   └── validator.py     conferência de links e arquivos
└── interface/       ADAPTADORES DE ENTRADA — CLI
    └── research.py      leitura da base aberta da Anvisa
```

Na raiz ficam apenas **entrypoints finos** (`build_pages.py`, `build_site.py`,
`validate_site.py`, `research_anvisa.py` e `legal_content.py`). Eles não contêm
regra de negócio: apenas definem a raiz do projeto e delegam para `src/`. Assim
os comandos de sempre continuam funcionando:

```powershell
python build_pages.py     # gera as páginas internas
python build_site.py      # gera dist/
python validate_site.py   # valida links e arquivos
python research_anvisa.py # reproduz a consulta à Anvisa
```

## Portas (contratos implícitos)

| Porta | Contrato | Adaptador atual |
|---|---|---|
| Escrita de páginas | receber nome + HTML e gravar em disco | `src/infrastructure/build.py` |
| Leitura de catálogo | fornecer medicamentos, vitrines e textos legais | `src/domain/legal.py` + dados em `src/application/generator.py` |
| Validação | receber a raiz e apontar links/arquivos inválidos | `src/infrastructure/validator.py` |
| Pesquisa regulatória | receber registros e produzir resumo da Anvisa | `src/interface/research.py` |

A troca de qualquer adaptador (por exemplo, publicar em outro host ou trocar o
validador) não exige mudar o núcleo — é exatamente o ponto da arquitetura.

## Dependências

O núcleo não importa `Path`, `subprocess` ou `__file__` para localizar a raiz;
quem define a raiz é o entrypoint, via variável de ambiente
`FARMA_PROJECT_ROOT`. Os adaptadores recebem essa raiz. Isso mantém o domínio
independente do sistema de arquivos.

## Limites conhecidos

- A home `index.html` não é gerada: ela preserva a identidade aprovada e tem CSS
  inline próprio. Mudanças estruturais nela precisam ser replicadas no gerador e
  no `assets/css/site.css`.
- O catálogo e a renderização ainda compartilham um único módulo
  (`src/application/generator.py`). Uma evolução natural seria extrair o catálogo
  para `src/domain/catalog.py`; isso pode ser feito depois sem mudar os HTMLs.
