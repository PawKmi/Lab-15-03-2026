from settings import Settings


def test_settings_load():
    # Sprawdzamy czy Settings wczytuje dane (ładowane przez pytest-dotenv)
    settings = Settings()
    assert settings.ENVIRONMENT == "test"
    assert settings.APP_NAME == "Aplikacja-Testowa"


