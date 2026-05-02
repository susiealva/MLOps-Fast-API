import pandas as pd
from core.logger import logger
from models.mlflow_model import MLFlowModel

model = MLFlowModel()

def predict_churn(input_dict: dict) -> int:
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
