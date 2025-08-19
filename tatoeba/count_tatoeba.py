import pandas as pd
isolated_sentences = pd.read_csv(
    filepath_or_buffer='./tatoeba_isolated_sentences_guarani/grn_sentences.tsv',
    sep='\t',
    header=None
)
sentences_guarani_spanish = pd.read_csv(
    filepath_or_buffer='guarani_spanish.tsv',
    sep='\t',
    header=None
)
isolated_sentences
sentences_guarani_spanish
guarani_sentences = pd.concat([isolated_sentences[2], sentences_guarani_spanish[1], sentences_spanish_guarani[3]])
guarani_sentences_set = set(guarani_sentences)
isolated_sentences[2]
isolated_sentences_set
len(guarani_sentences_set)
guarani_sentences_list = list(isolated_sentences_set)
guarani_sentences_list[0]
word_count = 0

for sentence in list(guarani_sentences_set):
    words = sentence.split()
    word_count += len(words)

print(f"Simple Word Count: {word_count}")
