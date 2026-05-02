
# API con FastAPI
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.logger import logger
from core.config import settings
from api import predict

app = FastAPI(
	title="Bank Churn Prediction API",
	description="API for predicting customer churn using a trained ML model.",
	version="0.1.0"
)

app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

app.include_router(predict.router)

@app.get("/health")
async def health_check():
	logger.info("Health check requested")
	return {"status": "ok"}
