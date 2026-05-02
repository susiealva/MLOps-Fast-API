# --------------------------------------
# Rutas de predicción para la API
# --------------------------------------
# Define el endpoint /predict y el esquema de entrada con validación.

from fastapi import APIRouter, status  # Para definir rutas y estados HTTP
from pydantic import BaseModel, Field  # Validación de datos de entrada
from services.inference_service import predict_churn  # Lógica de predicción

# Instancia del router para agrupar endpoints
router = APIRouter()

# Esquema de entrada para la predicción
class CustomerData(BaseModel):
    credit_score: int = Field(..., ge=0, le=1000)
    gender: str = Field(..., regex="^(Male|Female)$", description="Male or Female")
    age: int = Field(..., ge=18, le=120)
    tenure: int = Field(..., ge=0, le=50)
    balance: float = Field(..., ge=0)
    products_number: int = Field(..., ge=1, le=10)
    credit_card: int = Field(..., ge=0, le=1)
    active_member: int = Field(..., ge=0, le=1)
    estimated_salary: float = Field(..., ge=0)

# Endpoint de predicción
@router.post("/predict", status_code=status.HTTP_200_OK)
def predict(data: CustomerData):
    """
    Recibe los datos del cliente, llama al servicio de predicción y retorna el resultado.
    """
    pred = predict_churn(data.dict())
    return {"churn_prediction": pred}
