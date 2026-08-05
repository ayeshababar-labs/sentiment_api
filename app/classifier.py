from transformers import pipeline

TOPICS = [
    "technology",
    "sports",
    "politics",
    "business",
    "entertainment",
    "health",
    "science"
]

def load_classifier_model():
    return pipeline(
        "zero-shot-classification",
        model="facebook/bart-large-mnli"
    )

def classify_topic(model, text: str) -> dict:
    result = model(text, TOPICS)
    return {
        "text": text,
        "topic": result["labels"][0],  
        "confidence": round(result["scores"][0], 3),
        "all_topics": [
            {"topic": label, "confidence": round(score, 3)}
            for label, score in zip(result["labels"], result["scores"])
        ]
    }
