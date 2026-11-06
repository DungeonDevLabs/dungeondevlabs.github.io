# Padrão de página de projeto (DUNGEON.md)

Cada repositório da org que aparece em **Quests / Projects** na home deve ter um `DUNGEON.md` na raiz.
O site lê `https://raw.githubusercontent.com/DungeonDevLabs/<repo>/HEAD/DUNGEON.md` e monta o card; se o arquivo não existir, usa os dados de fallback em `script.js` (`PROJECTS`).
Para um repo novo aparecer, adicione `{ repo, name, ... }` em `PROJECTS` (o `DUNGEON.md` sobrescreve o resto).

## Template (copie para a raiz do repo)

```md
---
name: Vision
icon: 🐉
status: in progress
tags: Android, Pixel art
summary_en: One sentence, up to 120 characters, what it is.
summary_pt: Uma frase, até 120 caracteres, o que é.
preview: gallery/purple.gif, gallery/emerald.gif, gallery/ruby.gif, gallery/ice.gif
ai_images: true
privacy_en: privacy.md
privacy_pt: privacidade.md
---

Texto livre (não aparece na home): notas, links, roadmap.
```

## Regras
- Front matter entre `---`, uma linha `chave: valor` por campo. **Sem listas YAML**: `tags` e `preview` são separados por vírgula.
- `name`: nome exibido. `icon`: um emoji. `status`: texto curto livre (ex.: `in progress`, `shipped`) — opcional.
- `summary_en` / `summary_pt`: obrigatórios, uma frase cada.
- `tags`: até 4. `preview`: até 4 imagens/GIFs, caminhos relativos à raiz do repo (quadradas, pixel art) — opcional.
- `privacy_en` / `privacy_pt`: caminho (relativo à raiz do repo) da política de privacidade em cada idioma. **Todo app publicado na Play Store deve ter** (a loja exige o link). Se o repo só tem uma versão, preencha só o campo existente. Ex.: Vision usa `privacy.md` / `privacidade.md`; ThirdEye usa `public/politica-de-privacidade.md`. A URL pública é `https://github.com/DungeonDevLabs/<repo>/blob/main/<caminho>`. Por enquanto o campo é só documentação: a home ainda não exibe esse link.
- `ai_images: true` mostra o aviso "imagens geradas por IA" sob as imagens de `preview`.
- Todo texto é inserido como texto puro (nada de HTML/Markdown no card).
