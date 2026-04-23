from fastapi import FastAPI

from sentiment_api.api.models.sentiment import PredictRequest, PredictResponse
from sentiment_api.inference import (
    load_classifier,
    load_encoder,
    predict_sentiment,
)

app = FastAPI()

encoder = load_encoder()
classifier = load_classifier()


@app.post("/predict")
def predict(request: PredictRequest) -> PredictResponse:
    prediction = predict_sentiment(
        text=request.text,
        encoder=encoder,
        classifier=classifier,
    )
    return PredictResponse(prediction=prediction)
