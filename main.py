import os
import argparse
import yaml
from dotenv import load_dotenv
from settings import Settings


def export_envs(environment: str = "dev") -> None:
    env_path = f"config/.env.{environment}"
    load_dotenv(dotenv_path=env_path)


def load_secrets():
    # Funkcja wczytuje dane z secrets.yaml do zmiennych środowiskowych
    if os.path.exists("secrets.yaml"):
        with open("secrets.yaml", "r") as f:
            secrets = yaml.safe_load(f)
            if secrets:
                for key, value in secrets.items():
                    os.environ[key] = str(value)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Load environment variables.")
    parser.add_argument("--environment", type=str, default="dev")
    args = parser.parse_args()


    export_envs(args.environment)


    load_secrets()


    settings = Settings()

    print("APP_NAME:   ", settings.APP_NAME)
    print("ENVIRONMENT:", settings.ENVIRONMENT)
    print("SECRET:     ", settings.MY_SECRET_KEY)
