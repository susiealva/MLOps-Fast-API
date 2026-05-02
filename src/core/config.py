from pydantic import BaseSettings
import os

class Settings(BaseSettings):
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    debug: bool = False
    environment: str = "development"
    log_level: str = "INFO"
    mlflow_model_path: str = os.getenv("MLFLOW_MODEL_PATH", "../notebooks/mlruns/0/models/m-11c0f253c3724676a211147a6b69a300/artifacts")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
