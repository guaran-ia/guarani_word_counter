import os, zipfile, csv

# <<< EDITAR ESTAS DOS RUTAS >>>
zip_path = r"C:\Users\NISSEI\Downloads\coreguapa.zip"
extract_folder = r"C:\Users\NISSEI\Downloads\coreguapa"
out_csv = r"C:\Users\NISSEI\Downloads\coreguapa_word_counts.csv"
# <<< FIN DE EDICIÓN >>>

# 1) Extraer ZIP (si aún no fue extraído)
os.makedirs(extract_folder, exist_ok=True)
with zipfile.ZipFile(zip_path, 'r') as z:
    z.extractall(extract_folder)

# 2) Recorrer todos los .txt y contar PALABRAS (split por espacio)
total = 0
rows = []
for root, _, files in os.walk(extract_folder):
    for name in files:
        if not name.lower().endswith(".txt"):
            continue
        p = os.path.join(root, name)
        try:
            with open(p, "r", encoding="utf-8", errors="ignore") as f:
                n = len(f.read().split())
        except Exception as e:
            print(f"Error leyendo {p}: {e}")
            n = 0
        rows.append([os.path.relpath(p, extract_folder), n])
        total += n

# 3) Guardar detalle + TOTAL
with open(out_csv, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["file", "words"])
    w.writerows(rows)
    w.writerow(["__TOTAL__", total])

print(f"Archivos .txt: {len(rows)}")
print(f"TOTAL PALABRAS: {total}")
print(f"Detalle por archivo: {out_csv}")

