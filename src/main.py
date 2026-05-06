
# -----------------------------
# API principal con FastAPI
# -----------------------------
# Este archivo define la aplicación FastAPI, configura CORS,
# incluye los routers y expone el endpoint de health check.

from fastapi import FastAPI  # Framework principal para la API
from fastapi.middleware.cors import CORSMiddleware  # Middleware para CORS
from src.core.logger import logger  # Logger centralizado
from src.core.config import settings  # Configuración de la app
from src.api import predict  # Rutas de predicción

# Instancia principal de la aplicación FastAPI
app = FastAPI(
    title="Bank Churn Prediction API",
    description="API for predicting customer churn using a trained ML model.",
    version="0.1.0"
)

# Configuración de CORS para permitir peticiones desde cualquier origen
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir el router de predicción
app.include_router(predict.router)

# Endpoint de health check para monitoreo
@app.get("/health")
async def health_check():
    logger.info("Health check requested")
    return {"status": "ok"}
