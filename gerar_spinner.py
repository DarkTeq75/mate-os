#!/usr/bin/env python3
import math, sys, os
from PIL import Image, ImageDraw

DEST = sys.argv[1] if len(sys.argv) > 1 else "."
N = 48            # numero de quadros
TAM = 48          # tamanho de cada quadro (px)
ESPESSURA = 4.0   # espessura do traco (px)
SS = 8            # supersampling para bordas suaves

raio = (TAM - ESPESSURA) / 2 - 1
os.makedirs(DEST, exist_ok=True)

for i in range(N):
    t = i / N
    comp = 10 + 170 * (0.5 - 0.5 * math.cos(2 * math.pi * t))
    centro = -90 + 720 * t
    ini = centro - comp / 2
    fim = centro + comp / 2

    G = TAM * SS
    img = Image.new("RGBA", (G, G), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    c = G / 2
    r = raio * SS
    w = ESPESSURA * SS
    R = r + w / 2
    d.arc([c - R, c - R, c + R, c + R], ini, fim, fill=(255, 255, 255, 255), width=int(w))
    for ang in (ini, fim):
        x = c + r * math.cos(math.radians(ang))
        y = c + r * math.sin(math.radians(ang))
        d.ellipse([x - w / 2, y - w / 2, x + w / 2, y + w / 2], fill=(255, 255, 255, 255))
    img = img.resize((TAM, TAM), Image.LANCZOS)
    img.save(os.path.join(DEST, f"spinner-{i}.png"))

print(f"{N} quadros gerados em {DEST}")
