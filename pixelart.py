"""Converte a imagem em pixel art de verdade: grade de N pixels + paleta limitada, sem suavizar.

Uso:  python pixelart.py [imagem]                    -> janela (sliders de pixels e cores)
      python pixelart.py imagem saida.png [larg] [cores]  -> só exporta
"""
import string
import sys
from PIL import Image, ImageDraw

SRC = sys.argv[1] if len(sys.argv) > 1 else "assets/dungeon_dev.png"
CHARS = string.digits + string.ascii_letters + "+/"  # 1 char por cor (até 64); 2 chars acima disso


def pixelate(src, width, colors):
    h = max(1, round(src.height * width / src.width))
    small = src.resize((width, h), Image.BOX)  # média por bloco: cor fiel, sem borrão depois do zoom
    rgb = small.convert("RGB").quantize(colors, method=Image.MEDIANCUT, dither=Image.NONE).convert("RGB")
    mask = small.getchannel("A").point(lambda v: 255 if v >= 128 else 0)  # transparência: pixel ou tudo ou nada
    out = Image.new("RGBA", small.size, (0, 0, 0, 0))
    out.paste(rgb, mask=mask)
    return out


def view(img, zoom, grid, checker=True):
    if checker:  # mostra transparência como xadrez cinza
        bg = Image.new("RGB", img.size)
        bg.putdata([(40, 40, 48) if (i % img.width + i // img.width) % 2 else (64, 64, 72) for i in range(img.width * img.height)])
        bg.paste(img, mask=img.getchannel("A"))
        img = bg
    big = img.resize((img.width * zoom, img.height * zoom), Image.NEAREST)
    if grid and zoom >= 6:
        g = ImageDraw.Draw(big)
        for x in range(0, big.width, zoom):
            g.line([(x, 0), (x, big.height)], fill=(0, 0, 0))
        for y in range(0, big.height, zoom):
            g.line([(0, y), (big.width, y)], fill=(0, 0, 0))
    return big


def export_py(img, path):
    """Salva o desenho como código Python: paleta + uma string por linha de pixels."""
    pal = sorted(set(img.getdata()))
    k = 1 if len(pal) <= 64 else 2  # chars por pixel (2 chars => até 4096 cores)
    key = lambda i: CHARS[i // 64] + CHARS[i % 64] if k == 2 else CHARS[i]
    idx = {c: key(i) for i, c in enumerate(pal)}
    rows = ["".join(idx[img.getpixel((x, y))] for x in range(img.width)) for y in range(img.height)]
    with open(path, "w", encoding="utf8") as f:
        f.write("from PIL import Image\n\n")
        f.write(f"PALETTE = {{{', '.join(f'{key(i)!r}: {c}' for i, c in enumerate(pal))}}}\n")
        f.write("ROWS = [\n" + "".join(f"    {r!r},\n" for r in rows) + "]\n\n")
        f.write(f"K = {k}\nimg = Image.new('RGBA', (len(ROWS[0]) // K, len(ROWS)))\n")
        f.write("for y, row in enumerate(ROWS):\n    for x in range(img.width):\n        img.putpixel((x, y), PALETTE[row[x * K:x * K + K]])\n")
        f.write("img.resize((img.width * 8, img.height * 8), Image.NEAREST).show()\n")


if __name__ == "__main__":
    src = Image.open(SRC).convert("RGBA")
    if len(sys.argv) > 2:
        w = int(sys.argv[3]) if len(sys.argv) > 3 else 160
        c = int(sys.argv[4]) if len(sys.argv) > 4 else 128
        out = pixelate(src, w, c)
        view(out, max(1, 1024 // w), False, checker=False).save(sys.argv[2])
        sys.exit()

    import tkinter as tk
    from tkinter import filedialog
    from PIL import ImageTk

    root = tk.Tk()
    root.title("Pixel Art")
    lbl = tk.Label(root)
    lbl.pack()
    wid = tk.Scale(root, from_=16, to=min(512, src.width), orient="horizontal", length=700, label="Pixels de largura")
    wid.set(160)
    wid.pack()
    col = tk.Scale(root, from_=4, to=256, orient="horizontal", length=700, label="Número de cores")
    col.set(128)
    col.pack()
    grid = tk.BooleanVar()
    tk.Checkbutton(root, text="Mostrar grade (só com zoom grande, poucos pixels)", variable=grid).pack()
    st = {}

    def render(*_):
        st["img"] = pixelate(src, wid.get(), col.get())
        st["photo"] = ImageTk.PhotoImage(view(st["img"], max(1, 900 // wid.get()), grid.get()))
        lbl.config(image=st["photo"])

    def save_png():
        f = filedialog.asksaveasfilename(defaultextension=".png")
        if f:
            view(st["img"], max(1, 1024 // wid.get()), False, checker=False).save(f)

    def save_py():
        f = filedialog.asksaveasfilename(defaultextension=".py")
        if f:
            export_py(st["img"], f)

    wid.config(command=render)
    col.config(command=render)
    grid.trace_add("write", render)
    bar = tk.Frame(root)
    bar.pack(pady=4)
    tk.Button(bar, text="Salvar PNG", command=save_png).pack(side="left", padx=4)
    tk.Button(bar, text="Salvar como código Python", command=save_py).pack(side="left", padx=4)
    render()
    root.mainloop()
