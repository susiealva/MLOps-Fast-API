import mlflow.pyfunc
from core.logger import logger
from core.config import settings

class MLFlowModel:
    def __init__(self, model_path: str = None):
        self.model_path = model_path or settings.mlflow_model_path
        try:
            self.model = mlflow.pyfunc.load_model(self.model_path)
            logger.info(f"Modelo MLflow cargado desde {self.model_path}")
        except Exception as e:
            logger.error(f"Error cargando el modelo MLflow: {e}")
            self.model = None

    def predict(self, input_df):
        if self.model is None:
            raise RuntimeError("Modelo no disponible")
        return self.model.predict(input_df)
