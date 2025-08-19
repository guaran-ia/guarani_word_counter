import pandas as pd
import re

# Cargar el CSV
df = pd.read_csv("jojajovai_all (1).csv")

# Función para contar palabras
def count_words(text):
    if pd.isna(text):
        return 0
    words = re.findall(r'\b\w+\b', str(text))
    return len(words)

# Conteo de palabras en cada idioma
total_words_gn = df['gn'].apply(count_words).sum()
total_words_es = df['es'].apply(count_words).sum()

print(total_words_gn, total_words_es)
