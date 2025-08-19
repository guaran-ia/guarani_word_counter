import re, argparse, csv, os, unicodedata
from datasets import load_dataset
import fasttext

PRESETS = {
    "joemo":  ("mmaguero/gn-emotion-recognition",         "texto"),
    "joff":   ("mmaguero/gn-offensive-language-identification", "text"),
    "joffun": ("mmaguero/gn-humor-detection",             "text"),
}

URL_RE     = re.compile(r'https?://\S+|www\.\S+', re.I)
MENTION_RE = re.compile(r'@\w+')
HASHTAG_RE = re.compile(r'#(\w+)')  # "#palabra" -> "palabra"
WORD_RE    = re.compile(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñÃÕãẽĩõũỹẼĨÕŨỸ]+")

def keep_letters_only(s: str) -> str:
    out=[]
    for ch in s:
        cat=unicodedata.category(ch)
        if cat.startswith("L") or cat.startswith("M") or ch in " '’–-":
            out.append(ch)
        else:
            out.append(" ")
    return "".join(out)

def clean_text(raw: str) -> str:
    if not raw: return ""
    if "|||" in raw: raw = raw.split("|||", 1)[0]        # corta etiqueta final
    raw = URL_RE.sub(" ", raw)
    raw = MENTION_RE.sub(" ", raw)
    main()_ == "__main__":rdado: {args.save}")ows)ewline="") as f:os.path.dirname(args.save) else None"]]guardar)")