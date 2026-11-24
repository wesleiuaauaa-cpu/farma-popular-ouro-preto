# Publicação (Vercel)

O projeto é um site **estático**: não há servidor, banco de dados ni variáveis
de ambiente obrigatórias. Qualquer host estático serve o conteúdo.

## Build local

```powershell
python build_site.py
```

O comando:

1. executa `build_pages.py`, que regenera todas as páginas internas a partir de
   `build_pages.py` + `src/domain/legal.py`;
2. cria a pasta `dist/` com:
   - todos os `.html` públicos (home + 25 páginas internas),
   - `assets/` (CSS, JS, fontes e imagens),
   - `docs/` e os arquivos `README.md` / `docs/02-arquitetura/identidade-visual.md`.

> A home `index.html` **não** é gerada automaticamente: ela foi ajustada à mão
> para preservar a identidade aprovada. Se mexer nela, rode o build na mesma.

## Vercel

O arquivo `vercel.json` já aponta `outputDirectory: dist` e usa URLs limpas
(`/pages/institucionais/sobre` em vez de `/pages/institucionais/sobre.html`).

1. Faça commit de `dist/` junto com o resto (o build é versionado de propósito,
   para a Vercel não precisar executar Python).
2. Na Vercel: **Add New → Project** → selecione este repositório.
   - Framework Preset: **Other**
   - Build Command: **deixe vazio**
   - Output Directory: **dist** (já vem do `vercel.json`)
3. Deploy.

Se preferir que a Vercel gere o build sozinha, crie um `package.json` com
`"build": "python3 build_site.py"` e remova `outputDirectory` do `vercel.json`.
Nesse caso é preciso garantir que Python 3 esteja disponível no ambiente de build.

## Domínio e HTTPS

Depois do primeiro deploy, em **Project → Settings → Domains** é possível
anexar o domínio próprio. A Vercel emite HTTPS automaticamente.

## Antes de publicar (checklist)

As páginas em `src/domain/legal.py` são **modelos ilustrativos**. Antes de ir ao ar:

- [ ] preencher `[RAZÃO SOCIAL]`, `[CNPJ]`, `[E-MAIL DE CONTATO]`,
      `[E-MAIL DO ENCARREGADO]` e `[DATA DA ÚLTIMA REVISÃO]`;
- [ ] revisar os textos com quem responda juridicamente pela empresa;
- [ ] confirmar se as fotos de bancos de imagens exigem licença/atribuição
      (ver `docs/05-dominio/fontes-e-dados.md`);
- [ ] se for adicionar Analytics/Ads, colocar o script em `OPTIONAL_SCRIPTS`
      em `assets/js/site.js` — ele só carrega após o visitante aceitar cookies;
- [ ] atualizar `pages/legais/politica-de-cookies.html` com a lista real de cookies.

## Links para conferir depois do deploy

- `/` (home)
- `/pages/institucionais/sobre`, `/pages/institucionais/contato`, `/pages/institucionais/dicas-de-saude`
- `/pages/medicamentos/medicamentos-e-genericos` e as 4 subcategorias
- `/pages/legais/politica-de-privacidade`, `/pages/legais/termos-de-uso`,
  `/pages/legais/politica-de-cookies`, `/pages/legais/responsabilidade`,
  `/pages/legais/entrega-e-troca` — todos linkados no rodapé.
