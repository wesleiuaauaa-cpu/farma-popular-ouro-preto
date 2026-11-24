# Validação

Antes de qualquer publicação, rode os comandos abaixo na raiz do projeto.

```powershell
python build_site.py       # regera src/ → HTML → dist/
python validate_site.py    # links internos, arquivos locais e contagens
git status --short         # deve ficar vazio depois do build
```

## O que `validate_site.py` confere

- Páginas HTML publicadas.
- Ausência de `href="#"`.
- Existência de todos os arquivos locais referenciados por `href`/`src`.
- Contagem de cards e de botões `data-wa` por página.

## O que precisa de navegador

O script Python não detecta overflow, imagens quebradas em renderização nem
problemas de hover. Para isso, suba o servidor local:

```powershell
python -m http.server 8765 --bind 127.0.0.1
# http://localhost:8765/
```

Checklist visual mínimo:

- 320 / 375 / 768 / 1366 px sem rolagem horizontal.
- Todas as imagens carregando.
- Submenu "Medicamentos" abre e permanece aberto até o último item.
- Aviso de cookies aceita, rejeita e reabre pelo rodapé.
- Links `wa.me` abrindo com mensagem preenchida.

O relatório completo da última auditoria está em `docs/04-operacao/auditoria.md`.
