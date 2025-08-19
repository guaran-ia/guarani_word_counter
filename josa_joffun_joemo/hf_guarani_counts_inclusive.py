import pandas as pd
import glob
import re
import os

# Patrones de archivos CSV que deben ser considerados
patterns = [
    "grammar/guarani/translations-62k-*.csv",
    "grammar/guarani/translations/*/total.csv",
]

files = []
for p in patterns:
    files.extend(glob.glob(p))

if not files:
    print("No encontré archivos para sumar. ¿Estás en la carpeta del repo?")
    raise SystemExit(1)

tot_es = 0
tot_gn = 0
seen = set()
SPACE_RE = re.compile(r"\s+")

def norm(s: str) -> str:
    s = str(s).strip()
    s = SPACE_RE.sub(" ", s)
    return s

def count_words(text: str) -> int:
    text = text.strip()
    return 0 if not text else len(text.split())

# Procesar archivos
for path in files:
    try:
        df = pd.read_csv(path, header=None)
    except Exception as e:
        print(f"Error leyendo {path}: {e}")
        continue

    if df.shape[1] < 2:
        print(f"Archivo con menos de 2 columnas: {path}")
        continue

    for _, row in df.iterrows():
        es, gn = norm(row[0]), norm(row[1])
        pair = (es, gn)
        if pair in seen:
            continue
        seen.add(pair)
        tot_es += count_words(es)
        tot_gn += count_words(gn)

print("===========================================")
print(f"Pares únicos (es, gn): {len(seen):,}")
print(f"Total palabras español: {tot_es:,}")
print(f"Total palabras guaraní: {tot_gn:,}")
print("===========================================")
