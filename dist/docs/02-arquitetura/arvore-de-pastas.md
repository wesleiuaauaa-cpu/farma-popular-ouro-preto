# Árvore de pastas

Visão física do repositório e o motivo de cada pasta.

```
.
├── index.html                  HOME aprovada (não gerada)
├── pages/                      25 páginas geradas, por domínio
│   ├── medicamentos/           12 (lista, subcategorias e fichas)
│   ├── categorias/             5 vitrines
│   ├── institucionais/         3 (sobre, contato, dicas)
│   └── legais/                 5 documentos
├── build_pages.py              entrypoint → src/application/generator.py
├── build_site.py               entrypoint → src/infrastructure/build.py
├── validate_site.py            entrypoint → src/infrastructure/validator.py
├── research_anvisa.py          entrypoint → src/interface/research.py
├── legal_content.py            entrypoint → src/domain/legal.py
├── vercel.json                 config da Vercel (outputDirectory: dist)
├── .gitignore                  exclui rascunhos e ferramentas locais
├── assets/
│   ├── css/site.css            estilos das páginas internas
│   ├── js/site.js              WhatsApp, menu, busca e cookies
│   ├── fonts/                  fontes locais
│   ├── produtos/*.webp         32 fotos reais
│   └── produtos/*.svg          ilustrações antigas (referência)
├── src/                        código em camadas hexagonais
│   ├── domain/                 núcleo (dados e regras)
│   ├── application/            casos de uso (geração de páginas)
│   ├── infrastructure/         adaptadores (build, validação)
│   └── interface/              adaptadores de entrada (CLI)
├── docs/                       documentação em árvore temática
└── dist/                       build publicável (Vercel)
    ├── index.html              home
    └── pages/                  25 páginas (mesma árvore)
    ├── assets/                 cópia de assets/
    └── docs/                   cópia de docs/
```

## Por que os entrypoints ficam na raiz

São a interface pública do projeto. Quem usa o site digita `python build_site.py`
há meses; manter os mesmos nomes evita quebrar automações e a documentação. Eles
são pequenos e apenas delegam — a regra de negócio está em `src/`.

## Por que `dist/` é versionado

A Vercel não precisa executar Python: o build é gerado localmente e commitado.
Isso torna o deploy determinístico — o que está no repositório é exatamente o que
será publicado. Se preferir build na nuvem, configure um `package.json` com o
comando `python3 build_site.py` e remova `outputDirectory` do `vercel.json`.
