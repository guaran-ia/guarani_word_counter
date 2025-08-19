from datasets import load_dataset

def count_words(text):
    return len(text.strip().split())

# Cargar el subset de Guaraní
print(" Cargando dataset 'facebook/belebele' subset 'grn_Latn'...")
ds = load_dataset("facebook/belebele", name="grn_Latn", split="test")
print(f" Total de oraciones: {len(ds)}")

# Campos en guaraní
text_fields = ["flores_passage", "question", "mc_answer1", "mc_answer2", "mc_answer3", "mc_answer4"]

# Calcular palabras
total_words = 0
for example in ds:
    for field in text_fields:
        total_words += count_words(example[field])

print(f"Total de palabras estimadas en guaraní: {total_words}")
