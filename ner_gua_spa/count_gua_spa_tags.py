import re, collections

# Archivos del repo
FILES = [("train","gua_spa_train.txt"),
         ("dev","gua_spa_dev.txt"),
         ("test","gua_spa_test.txt")]

# Conjunto de posibles etiquetas de idioma
TAGS = {"gn","es","spa","mix","ne","foreign"}

def detect_label_col(path, max_probe=2000):
    """Detecta en qué columna aparecen más etiquetas (gn/es/spa/mix/ne/foreign)."""
    counts = collections.Counter()
    with open(path, encoding="utf-8") as f:
        for k, line in enumerate(f, 1):
            line = line.strip()
            if not line or line.startswith("#"): 
                continue
            cols = re.split(r"\s+", line)
            for i, c in enumerate(cols):
                if c in TAGS:
                    counts[i] += 1
            if k >= max_probe:
                break
    return counts.most_common(1)[0][0] if counts else None  # índice 0-based

def count_file(path, col):
    """Cuenta tokens por etiqueta en la columna detectada."""
    c = collections.Counter()
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            cols = re.split(r"\s+", line)
            if col >= len(cols):
                continue
            tag = cols[col]
            if tag == "spa": tag = "es"  # normalizar español
            if tag in {"gn","es","mix","ne","foreign"}:
                c[tag] += 1
    c["considered"] = c["gn"] + c["es"] + c["mix"] + c["ne"] + c["foreign"]
    return c

def main():
    # Detectar columna en 'train' y usar la misma para todos los splits
    col = detect_label_col(FILES[0][1])
    if col is None:
        print("No pude detectar la columna de etiquetas. Revisá el formato de los .txt"); return
    print(f"[i] Usando columna {col+1} (0-based={col}) para las etiquetas.\n")

    totals = collections.Counter()
    rows = []

    for split, path in FILES:
        c = count_file(path, col)
        rows.append((split, c["gn"], c["es"], c["mix"], c["ne"], c["foreign"], c["considered"]))
        totals.update(c)
        print(f"== {split} ==")
        print(f"gn={c['gn']}  es={c['es']}  mix={c['mix']}  ne={c['ne']}  foreign={c['foreign']}")
        print(f"total(gn+es+mix+ne+foreign)={c['considered']}\n")

    print("== TOTAL ==")
    print(f"gn={totals['gn']}  es={totals['es']}  mix={totals['mix']}  ne={totals['ne']}  foreign={totals['foreign']}")
    print(f"total(gn+es+mix+ne+foreign)={totals['considered']}\n")

    # CSV
    with open("gua_spa_counts.csv","w",encoding="utf-8") as w:
        w.write("split,gn,es,mix,ne,foreign,total_considered\n")
        for r in rows:
            w.write(",".join([r[0]]+[str(x) for x in r[1:]])+"\n")
        w.write("TOTAL,{gn},{es},{mix},{ne},{foreign},{tot}\n".format(
            gn=totals["gn"], es=totals["es"], mix=totals["mix"],
            ne=totals["ne"], foreign=totals["foreign"], tot=totals["considered"]))
    print("[OK] Guardado: gua_spa_counts.csv")

if __name__ == "__main__":
    main()
