# --------------------------------------
# Abstracción para cargar y usar modelo MLflow
# --------------------------------------
# Clase para encapsular la carga y predicción con modelos MLflow.

import mlflow.pyfunc  # MLflow para modelos genéricos
from src.core.logger import logger  # Logger centralizado
from src.core.config import settings  # Configuración global

class MLFlowModel:
    """
    Clase para cargar un modelo MLflow y realizar predicciones.
    """
    def __init__(self, model_path: str = None):
        # Usar ruta por parámetro o la de settings
        self.model_path = model_path or settings.mlflow_model_path

        try:
            # Cargar el modelo MLflow
            self.model = mlflow.pyfunc.load_model(self.model_path)
            logger.info(f"Modelo MLflow cargado desde {self.model_path}")
        
        except Exception as e:
            logger.error(f"Error cargando el modelo MLflow: {e}")
            self.model = None

    def predict(self, input_df):
        """
        Realiza la predicción usando el modelo cargado.
        """
        if self.model is None:
            raise RuntimeError("Modelo no disponible")
        return self.model.predict(input_df)
