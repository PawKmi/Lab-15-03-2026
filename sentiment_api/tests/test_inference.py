from sentiment_api.inference import (
    load_classifier,
    load_encoder,
    predict_sentiment,
)


def test_model_loads():
    encoder = load_encoder()
    classifier = load_classifier()

    assert encoder is not None
    assert classifier is not None


def test_prediction_returns_valid_label():
    encoder = load_encoder()
    classifier = load_classifier()

    prediction = predict_sentiment(
        text="This is amazing",
        encoder=encoder,
        classifier=classifier,
    )

    assert prediction in {"negative", "neutral", "positive"}


def test_multiple_inputs():
    encoder = load_encoder()
    classifier = load_classifier()

    samples = [
        "I love this",
        "It's okay",
        "This is terrible",
    ]

    for text in samples:
        prediction = predict_sentiment(
            text=text,
            encoder=encoder,
            classifier=classifier,
        )
        assert prediction in {"negative", "neutral", "positive"}
