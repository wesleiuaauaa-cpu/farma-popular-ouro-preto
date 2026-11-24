# Auditoria de prontidão — build e publicação

**Data:** 24/11/2026  
**Objeto:** projeto Farma Popular Ouro Preto (site estático)  
**Pergunta respondida:** o projeto está pronto para o build e bom para subir?

## Veredito resumido

| Item | Situação |
|---|---|
| Build reproduzível | ✅ Pronto |
| Estrutura de links e arquivos | ✅ Sem erros |
| Renderização responsiva | ✅ Sem erros |
| Acessibilidade básica | ✅ Sem erros |
| Segredos no repositório | ✅ Nenhum |
| **Publicação pública** | ⚠️ **Condicionada** — ver pendências abaixo |

**Resposta direta:** está pronto para gerar o build e para subir ao GitHub/Vercel do ponto de vista técnico. **Não está pronto para ficar publicado ao público final** enquanto os 13 campos dos modelos legais não forem preenchidos e revisados e a licença de algumas fotos não for confirmada.

---

## O que foi verificado

### 1. Build e repositório

- `python build_site.py` executado do zero: `dist/` gerado com **26 páginas HTML**, mais `assets/`, `docs/` e os Markdown públicos.
- As 26 páginas da raiz e as 26 de `dist/` são **idênticas em nome e conteúdo** — não há divergência.
- Após regenerar o build, `git status` ficou **limpo**: o resultado é reproduzível e o `dist/` versionado está atualizado.
- `vercel.json` aponta `outputDirectory: "dist"`, com `cleanUrls: true` e `trailingSlash: false`.
- Histórico remoto sincronizado: commit `caa7a7c` enviado para `origin/main`.

### 2. Links e arquivos

- **65 URLs internas únicas** verificadas: nenhuma aponta para arquivo inexistente.
- Nenhum `href="#"` (link fake) restante.
- `validate_site.py`: nenhum arquivo local ausente.
- Links externos (WhatsApp, Google Maps, Instagram, Facebook, Bulário da Anvisa) são intencionais e usam `target="_blank" rel="noopener"` quando aplicável.

### 3. Imagens

- **32 fotos WebP** válidas (7 medicamentos + 25 itens das cinco vitrines), todas abaixo de 900×900.
- Nenhuma imagem quebrada em nenhuma largura testada.
- Risco registrado: algumas fotos vêm de bancos de imagem (Freepik, inclusive uma "premium") e de matéria editorial (Vogue/Globo). A autorização do proprietário cobre o uso de fotos de produtos, mas **a licença dessas fontes específicas deve ser confirmada**. Detalhes em `docs/fontes.md`.

### 4. Navegador (104 verificações)

- 26 páginas × 4 larguras (320, 375, 768, 1366 px).
- Zero overflow horizontal.
- Zero erros de console.
- Todas com `<html lang="pt-BR">`, um único `<h1>`, link "Pular para o conteúdo" e 5 links legais no rodapé.
- Comportamentos conferidos separadamente:
  - **Submenu Medicamentos:** permanece aberto durante todo o movimento do mouse até o último item, em 1366/1024/821 px; no mobile as 4 subcategorias têm 44 px de altura e navegam corretamente.
  - **Cookies:** aviso aparece na primeira visita, aceitar/rejeitar persiste após recarregar, botão do rodapé reabre, nenhum script de terceiros é carregado hoje.
  - **WhatsApp:** links `wa.me` com mensagem pré-preenchida, número confirmado `(31) 3551-5271`.

### 5. Segurança e higiene

- Nenhum token, senha ou segredo encontrado nos arquivos versionados.
- `.gitignore` exclui rascunhos, capturas, arquivos do mockup original e diretórios de ferramentas locais.
- O arquivo que continha o token do GitHub não faz parte do projeto — a autenticação fica apenas no ambiente do `gh`.

---

## Pendências antes de publicar

### Bloqueantes para publicação pública

1. **Preencher os 13 campos entre colchetes** das páginas legais:

   | Página | Campos |
   |---|---|
   | Política de Privacidade | 6 |
   | Termos de Uso | 1 |
   | Política de Cookies | 2 |
   | Aviso de Responsabilidade | 1 |
   | Entrega e Troca | 3 |

   Editar `legal_content.py`, rodar `python build_site.py` e conferir o resultado. O texto continua exibindo o selo "MODELO ILUSTRATIVO" — ele deve ser removido apenas quando a revisão terminar (a lógica está em `legal_body()` em `build_pages.py`).

2. **Revisão jurídica/contábil:** razão social, CNPJ, e-mail do encarregado de dados, prazos de entrega/troca e a política real da loja.

3. **Licença das fotos de bancos/editoriais:** confirmar ou substituir os arquivos indicados em `docs/fontes.md`.

### Não bloqueantes (melhorias futuras)

- Conectar Analytics: colocar o script em `OPTIONAL_SCRIPTS` em `assets/js/site.js` e atualizar a Política de Cookies. Isso já foi preparado.
- Anexar domínio próprio na Vercel e conferir HTTPS.
- Publicar a nota de avaliações do Google apenas se a farmácia decidir — ela foi deliberadamente mantida fora do site.
- Preencher apresentação/concentração/embalagem e links diretos de bula quando houver fonte oficial confirmada.

---

## Como repetir a auditoria

```powershell
python build_site.py          # regera dist/ e as páginas
python validate_site.py       # links, arquivos e contagens
git status --short            # deve ficar vazio após o build
```

Para a checagem visual em navegador, use o servidor local:

```powershell
python -m http.server 8765 --bind 127.0.0.1
# http://localhost:8765/
```

O relatório original desta auditoria, com os números brutos, está registrado neste arquivo. Quando o projeto mudar, atualize a data e reexecute os comandos acima antes de alterar o veredito.

## Relação com os outros documentos

- `docs/DEPLOY.md` — como publicar na Vercel (o passo seguinte a esta auditoria).
- `docs/fontes.md` — origem dos dados e das fotos (base das pendências 3).
- `docs/MAPA_DOCUMENTACAO.md` — índice explicativo de toda a documentação do projeto.
- `README.md` — visão geral e rotas.
- `DESIGN.md` — sistema visual e componentes.
