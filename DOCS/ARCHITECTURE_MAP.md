# Architecture Map

- `assets/dungeon_dev.png` — imagem de referência (mago com lobo).
- `pixelart.py` — converte a referência em pixel art: reduz para N pixels de largura (média por bloco, `Image.BOX`), limita a paleta (`quantize`, median cut, sem dithering) e amplia com NEAREST. Suporta PNG com transparência (alpha tudo-ou-nada, xadrez na janela, PNG/export mantêm o fundo transparente). Janela Tkinter com sliders de pixels (16–512) e cores (4–256, padrão 128), grade opcional, "Salvar PNG" e "Salvar como código Python" (`export_py`: paleta (chaves de 1 ou 2 chars) + uma string por linha de pixels). CLI: `python pixelart.py img.png [out.png] [largura] [cores]`.

Sem endpoints/schemas. Dependência: Pillow.

## Home page (GitHub Pages: dungeondevlabs.github.io, repo DungeonDevLabs/dungeondevlabs.github.io)
- `index.html` — página estática única (Home/hero, Quests, Arsenal). Textos com `data-i18n`/`data-i18n-html`. Cards de Quests baseados nos repos da org (Vision, ThirdEye). Rodapé: `assets/logo-completa.png` + aviso de imagens geradas por IA / IAs como copilotos de desenvolvimento. Hero tem faixa "Desenvolvido com IA" com ícones `assets/ai/claude.svg`, `deepseek.svg` e `gemini.svg` (sem botões CTA). Assets: `home_img.png`, `logo.png` (favicon), `dragons/*.gif` (copiados de DungeonDevLabs/Vision/gallery).
- `style.css` — paleta em variáveis CSS `:root` (void/bg/surface/line, indigo, violet, cyan, mint; extraída do logo) + tema claro via `[data-theme="light"]`. Fontes: Inter (texto), Press Start 2P e Silkscreen (toques pixel).
- `script.js` — dicionário i18n EN/PT-BR (idioma inicial por `navigator.language`, botão EN/PT persiste em localStorage `lang`), toggle de tema e ano do rodapé. Novo texto: adicionar a chave nos dois idiomas.
- `.gitignore` — ignora `__pycache__`, editores e `assets/*_draft*.png`.
Sem build, sem dependências.
- `DOCS/README_STANDARD.md` — padrão de README bilíngue (EN + PT no mesmo arquivo) para repos públicos da org.
- `DOCS/PROJECT_PAGE_STANDARD.md` — padrão do `DUNGEON.md` que cada repo da org usa para montar seu card em Quests. `script.js` (`PROJECTS` + `parseDungeon`) renderiza os cards, com descoberta automática dos repos públicos via API do GitHub e `DUNGEON.md` remoto sobrescrevendo o fallback local. `index.html` tem `<meta name="google" content="notranslate">` (o site já é bilíngue) e CSS/JS com `?v=N` para cache-bust (incrementar a cada mudança).
- Caminhos de imagem: no `script.js`, `./assets/...` = arquivo do próprio site (fallback); qualquer outro caminho vem do repo do projeto (`raw.githubusercontent.com/DungeonDevLabs/<repo>/HEAD/<caminho>`).
