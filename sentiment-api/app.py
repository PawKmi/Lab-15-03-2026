from fastapi import FastAPI

from api.models.sentiment import PredictRequest, PredictResponse

app = FastAPI()


@app.post("/predict")
def predict(request: PredictRequest) -> PredictResponse:
    return PredictResponse(prediction="positive")