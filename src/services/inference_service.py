
# --------------------------------------
# Servicio de inferencia para predicción de churn
# --------------------------------------
# Contiene la lógica para preprocesar la entrada y llamar al modelo MLflow.

import pandas as pd  # Manipulación de datos
from core.logger import logger  # Logger centralizado
from models.mlflow_model import MLFlowModel  # Abstracción del modelo MLflow

# Instanciar el modelo MLflow una sola vez
model = MLFlowModel()

def predict_churn(input_dict: dict) -> int:
    """
    Preprocesa los datos de entrada, realiza la predicción y retorna el resultado.
    """
    # Preprocesamiento mínimo (ajustar según tu pipeline real)
    input_dict["gender"] = 1 if input_dict["gender"].lower() == "male" else 0
    columns = [
        "credit_score", "gender", "age", "tenure", "balance",
        "products_number", "credit_card", "active_member", "estimated_salary"
    ]
    input_df = pd.DataFrame([input_dict], columns=columns)
    
    try:
        pred = model.predict(input_df)
        logger.info(f"Predicción realizada para input: {input_dict} → {pred[0]}")
        return int(pred[0])
    
    except Exception as e:
        logger.error(f"Error en predicción: {e}")
        raise
