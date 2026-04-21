from pathlib import Path

import joblib
from cleantext import clean
from sentence_transformers import SentenceTransformer

MODEL_DIR = Path("models")
ENCODER_PATH = MODEL_DIR / "sentence_transformer.model"
CLASSIFIER_PATH = MODEL_DIR / "classifier.joblib"

LABELS = {
    0: "negative",
    1: "neutral",
    2: "positive",
}


def preprocess_text(text: str) -> str:
    return clean(text, lower=True)


def load_encoder():
    return SentenceTransformer(str(ENCODER_PATH))


def load_classifier():
    return joblib.load(CLASSIFIER_PATH)


def predict_sentiment(text: str, encoder, classifier) -> str:
    cleaned_text = preprocess_text(text)
    embedding = encoder.encode([cleaned_text])
    prediction = classifier.predict(embedding)[0]
    return LABELS[int(prediction)]