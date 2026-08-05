from keybert import KeyBERT

def load_keybert_model():
    return KeyBERT()

def extract_keywords(model, text: str) -> dict:
    keywords = model.extract_keywords(
        text,
        keyphrase_ngram_range=(1, 2),
        stop_words="english",
        top_n=5
    )

    return {
        "text": text,
        "keywords": [{"keyword": keyword, "score": score} for keyword, score in keywords]
    }