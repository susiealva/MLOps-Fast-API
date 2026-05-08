# --------------------------------------
# Configuración central de la aplicación
# --------------------------------------
# Define la clase Settings para cargar variables de entorno y configuración.

from pydantic_settings import BaseSettings  # Para gestión de settings y validación
from pydantic import ConfigDict  # Para configuración de Pydantic v2
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
        "../mlruns/1/models/m-4ae70bcfd9524ee38f2045a89f3d0fca/artifacts"
    )  # Ruta por defecto al modelo MLflow

    model_config = ConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

# Instancia global de settings
settings = Settings()
