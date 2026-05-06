
# MLOps-Fast-API

Proyecto de predicción de churn con MLflow + FastAPI.

## Inicio Rápido

1. Instala dependencias (elige una opción):

```bash
# Opción A: conda
conda env create -f environment.yml
conda activate mlops-fastapi

# Opción B: pip
pip install -r requirements.txt
```

2. Crea tu configuración local:

```bash
cp .env.example .env
```

3. Configura credenciales de Kaggle (si no tienes el CSV en `data/`):

```bash
mkdir -p ~/.kaggle
cp /ruta/a/kaggle.json ~/.kaggle/kaggle.json
chmod 600 ~/.kaggle/kaggle.json
```

4. Descarga datos y entrena:

```bash
python src/load_data.py
python src/train.py
```

5. Usa el modelo más reciente en `.env`:

```bash
ls -td mlruns/*/models/*/artifacts | head -n 1
```

Copia esa ruta en `MLFLOW_MODEL_PATH` dentro de `.env`.

## Ejecutar

Terminal 1 (MLflow UI):

```bash
mlflow ui
```

Terminal 2 (API):

```bash
uvicorn src.main:app --reload
```

## Probar rápido

Health check:

```bash
curl http://127.0.0.1:8000/health
```

Predicción:

```bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "credit_score": 650,
    "gender": "Male",
    "age": 35,
    "tenure": 5,
    "balance": 50000.0,
    "products_number": 2,
    "credit_card": 1,
    "active_member": 1,
    "estimated_salary": 60000.0
  }'
```

Tests:

```bash
pytest
```

## Problemas Comunes

- Error de Kaggle: revisa `~/.kaggle/kaggle.json` y permisos (`chmod 600`).
- Puerto ocupado para MLflow: `mlflow ui --port 5001`.
- Modelo no encontrado: valida `MLFLOW_MODEL_PATH` y que exista `MLmodel` en esa ruta.