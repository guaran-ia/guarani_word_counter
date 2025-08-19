sum_grammar_counts_dedup.py << 'PY'
import pandas as pd, glob, re

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

PYint(f"  Pares únicos (es,gn): {len(seen):,}"))) ================")
python sum_grammar_counts_dedup.py
