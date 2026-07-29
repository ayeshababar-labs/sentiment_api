

def predict_sentiment(model, text: str) -> dict:
    result = model(text)[0]
    return {
        "text": text,
        "sentiment": result["label"].lower(),  # POSITIVE → positive
        "confidence": round(result["score"], 3)
    }