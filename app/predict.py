
def predict_sentiment(model, text: str) -> dict:
    prediction = model.predict([text])[0]
    probability = model.predict_proba([text])[0]
    return {
        "text": text,
        "sentiment": "positive" if prediction == 1 else "negative",
        "confidence": round(max(probability), 3)
    }