from fastapi import APIRouter, status
from pydantic import BaseModel, Field
from services.inference_service import predict_churn

router = APIRouter()

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

@router.post("/predict", status_code=status.HTTP_200_OK)
def predict(data: CustomerData):
    pred = predict_churn(data.dict())
    return {"churn_prediction": pred}
