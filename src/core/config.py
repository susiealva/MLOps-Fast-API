# --------------------------------------
# Configuración central de la aplicación
# --------------------------------------
# Define la clase Settings para cargar variables de entorno y configuración.

from pydantic import BaseSettings  # Para gestión de settings y validación
import os  # Acceso a variables de entorno

# Clase de configuración principal
class Settings(BaseSettings):
    api_host: str = "0.0.0.0"  # Host de la API
    api_port: int = 8000  # Puerto de la API
    debug: bool = False  # Modo debug
    environment: str = "development"  # Entorno de ejecución
    log_level: str = "INFO"  # Nivel de logging
    mlflow_model_path: str = os.getenv(
        "MLFLOW_MODEL_PATH",
        "../notebooks/mlruns/0/models/m-11c0f253c3724676a211147a6b69a300/artifacts"
    )  # Ruta por defecto al modelo MLflow

    class Config:
        env_file = ".env"  # Archivo de variables de entorno
        env_file_encoding = "utf-8"

# Instancia global de settings
settings = Settings()
