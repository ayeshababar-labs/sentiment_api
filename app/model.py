import pickle
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer

def build_pipeline():
    return Pipeline([('tfidf', TfidfVectorizer()),
                     ('clf', LogisticRegression())])

def load_model(model_path):
    with open(model_path, "rb") as f:
        return pickle.load(f)

def save_model(pipeline, model_path):
    with open(model_path, "wb") as f:
        pickle.dump(pipeline, f)