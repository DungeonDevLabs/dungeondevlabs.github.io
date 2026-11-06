# Architecture Map

- `assets/dungeon_dev.png` — imagem de referência (mago com lobo).
- `pixelart.py` — converte a referência em pixel art: reduz para N pixels de largura (média por bloco, `Image.BOX`), limita a paleta (`quantize`, median cut, sem dithering) e amplia com NEAREST. Suporta PNG com transparência (alpha tudo-ou-nada, xadrez na janela, PNG/export mantêm o fundo transparente). Janela Tkinter com sliders de pixels (16–512) e cores (4–256, padrão 128), grade opcional, "Salvar PNG" e "Salvar como código Python" (`export_py`: paleta (chaves de 1 ou 2 chars) + uma string por linha de pixels). CLI: `python pixelart.py img.png [out.png] [largura] [cores]`.

Sem endpoints/schemas. Dependência: Pillow.

## Home page (GitHub Pages: dungeondevlabs.github.io, repo DungeonDevLabs/Home)
- `index.html` — página estática única (seções: Home/hero, The Forge, Quests, Arsenal, Guild). Usa `assets/logo.png` e `assets/home_img.png`.
- `style.css` — paleta em variáveis CSS `:root` (void/bg/surface/line, indigo, violet, cyan, mint; extraída do logo) + tema claro via `[data-theme="light"]`. Fontes: Inter (texto), Press Start 2P e Silkscreen (toques pixel).
- `script.js` — toggle de tema (persistido em localStorage) e ano do rodapé.
- `.gitignore` — ignora `__pycache__`, editores e `assets/*_draft*.png`.
Sem build, sem dependências.
