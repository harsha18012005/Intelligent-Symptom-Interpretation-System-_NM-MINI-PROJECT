import re
import spacy

nlp = spacy.load("en_core_web_sm")

def clean_and_tokenize(text):
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text.lower())
    doc = nlp(text)
    return " ".join([token.lemma_ for token in doc])
