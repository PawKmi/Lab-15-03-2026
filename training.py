from pathlib import Path

import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier


MODEL_PATH = Path("model.joblib")


def load_data():
    return load_iris()


def train_model():
    data = load_data()
    model = RandomForestClassifier(random_state=42)
    model.fit(data.data, data.target)
    return model


def save_model(model, path: Path = MODEL_PATH):
    joblib.dump(model, path)


if __name__ == "__main__":
    model = train_model()
    save_model(model)
    print(f"Model saved to {MODEL_PATH}")