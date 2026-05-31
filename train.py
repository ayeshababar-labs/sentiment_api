import os
from app.model import build_pipeline, save_model

# Define model path relative to the project root
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'model', 'sentiment_model.pkl')

# Small training set — swap with real data if you want
texts = [
    "I love this product", "This is amazing", "Best thing ever",
    "Absolutely wonderful experience", "Really happy with this",
    "This is terrible", "Worst experience ever", "I hate this",
    "Completely disappointed", "Never buying again"
]
labels = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]  # 1=positive, 0=negative


pipeline = build_pipeline()
pipeline.fit(texts, labels)
save_model(pipeline, MODEL_PATH)
