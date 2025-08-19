# guarani_word_counter
Scripts y utilidades para contar palabras en corpus en guaraní y jopará. Usado en el proyecto GuaranIA.
# Guaraní Word Counter 

Este repositorio contiene scripts para calcular el número de palabras en diversos corpus en guaraní y jopará, utilizados dentro del proyecto **GuaranIA**.

Cada script está adaptado al formato particular de cada dataset y puede ser ejecutado de manera independiente.

## 📁 Estructura del repositorio

```
guarani_word_counter/
├── coreguapa/
│   └── count_coreguapa.py
├── jajovai/
│   └── count_jajovai.py
├── grammar/
│   └── sum_grammar_counts_dedup.py
├── josa_joffun_joemo/
│   └── hf_guarani_counts_inclusive.py
├── belebele/
│   └── belebele.py
├── tatoeba/
│   └── count_tatoeba.py
├── ner_gua_spa/
│   └── count_gua_spa_tags.py
├── data/
│   └── (archivos de entrada opcionales)
├── requirements.txt
└── README.md
```


## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/guaran-ia/guarani_word_counter.git
cd guarani_word_counter
