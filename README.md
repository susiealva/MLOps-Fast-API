
# MLOps-Fast-API
El objetivo de este challenge es poner en práctica lo aprendido de MLFlow y la puesta en producción de un modelo.

## Creación de entorno

Puedes usar conda para un entorno reproducible o pip con un entorno virtual. **No es necesario instalar las dependencias con pip si ya creaste el entorno conda usando `environment.yml`.**

**Opción 1: Conda (recomendado)**
```bash
conda env create -f environment.yml
conda activate mlops-fastapi
```
Esto instalará todas las dependencias necesarias en un entorno limpio.

**Opción 2: pip y entorno virtual**
```bash
pip install -r requirements.txt
```

## Reproducción rápida (paso a paso)

Ejecuta estos pasos desde la raíz del proyecto para reproducir el flujo completo:

```bash
conda env create -f environment.yml
conda activate mlops-fastapi
python src/load_data.py
python src/train.py
mlflow ui
```

En otra terminal (con el mismo entorno activado), levanta la API:

```bash
uvicorn src.main:app --reload
```

Verificaciones rápidas:

```bash
ls -lh data/
pytest
```

## Instalación y descarga automática del dataset

1. Configura tu token de Kaggle:
	 - Descarga tu archivo `kaggle.json` desde tu cuenta de Kaggle (https://www.kaggle.com/ -> Account -> Create New API Token).
	 - Opción recomendada: copia el archivo a la ruta `~/.kaggle/kaggle.json` ejecutando:
		 ```bash
		 mkdir -p ~/.kaggle
		 cp /ruta/al/archivo/kaggle.json ~/.kaggle/kaggle.json
		 chmod 600 ~/.kaggle/kaggle.json
		 ```
	 - Alternativamente, puedes exportar las variables de entorno (extrae los valores de tu kaggle.json):
		 ```bash
		 export KAGGLE_USERNAME=TU_USUARIO
		 export KAGGLE_KEY=TU_API_KEY
		 ```

2. Descarga el dataset automáticamente:
	```bash
	python src/load_data.py
	```

Esto descargará y descomprimirá el dataset de Bank Customer Churn (https://www.kaggle.com/datasets/gauravtopre/bank-customer-churn-dataset) en la carpeta `data/`.
Si el archivo `data/Bank Customer Churn Prediction.csv` ya existe, puedes continuar directamente con el entrenamiento.


## Estructura del proyecto (mejores prácticas MLOps)

```
src/
	core/         # Logging, configuración centralizada
	models/       # Lógica de modelos ML (MLflow, etc)
	services/     # Lógica de negocio (predicción, validaciones)
	api/          # Rutas FastAPI
	utils/        # Helpers y utilidades
	config/       # Archivos de configuración YAML/env
main.py         # Entrypoint FastAPI
tests/          # Pruebas automáticas (pytest)
```

## Configuración y variables de entorno

1. Crea un archivo `.env` en la raíz del proyecto (no existe `.env.example` en este repositorio).
2. Define al menos estas variables:

```env
API_HOST=0.0.0.0
API_PORT=8000
DEBUG=true
ENVIRONMENT=development
LOG_LEVEL=INFO
MLFLOW_MODEL_PATH=mlruns/0/models/<model-id>/artifacts
```

`MLFLOW_MODEL_PATH` debe apuntar al modelo que quieres servir en la API.
3. Puedes modificar parámetros en `src/config/config.yaml` para cambiar el comportamiento global.


## Entrenamiento y despliegue del modelo

### 1. Entrenamiento y logging con MLflow

Ejecuta el script de entrenamiento para preprocesar, entrenar y guardar el modelo con MLflow:

```bash
python src/train.py
```
Esto generará nuevos runs/modelos en `mlruns/` y metadata en `mlflow.db`.

Para visualizar experimentos y métricas:

```bash
mlflow ui
```

Por defecto, la UI queda disponible en `http://127.0.0.1:5000`.

### 2. Servir la API de predicción

Lanza el servidor de desarrollo:

```bash
uvicorn src.main:app --reload
```
La API estará disponible en http://localhost:8000

#### Endpoints principales

- `GET /health` — Health check para monitoreo
- `POST /predict` — Predicción de churn. Ejemplo de payload:

```json
{
	"credit_score": 650,
	"gender": "Male",
	"age": 35,
	"tenure": 5,
	"balance": 50000.0,
	"products_number": 2,
	"credit_card": 1,
	"active_member": 1,
	"estimated_salary": 60000.0
}
```

Respuesta:
```json
{"churn_prediction": 0}
```

La documentación interactiva está disponible en `/docs`.

## Pruebas automáticas

Ejecuta todos los tests con:

```bash
pytest
```

Incluye pruebas para `/health` y `/predict` (válido/inválido).

## Troubleshooting rápido

### 1. Error de autenticación con Kaggle

Si `python src/load_data.py` falla por credenciales:

```bash
mkdir -p ~/.kaggle
cp /ruta/al/archivo/kaggle.json ~/.kaggle/kaggle.json
chmod 600 ~/.kaggle/kaggle.json
```

También puedes usar variables de entorno:

```bash
export KAGGLE_USERNAME=TU_USUARIO
export KAGGLE_KEY=TU_API_KEY
```

### 2. Puerto 5000 ocupado al ejecutar MLflow UI

Si `mlflow ui` no inicia porque el puerto está en uso:

```bash
mlflow ui --port 5001
```

### 3. Error: modelo MLflow no encontrado en la API

Si la API falla al cargar el modelo, revisa `MLFLOW_MODEL_PATH` en `.env`.
Debe apuntar a una ruta existente, por ejemplo:

```env
MLFLOW_MODEL_PATH=mlruns/0/models/<model-id>/artifacts
```

Puedes listar modelos disponibles con:

```bash
find mlruns -type f -name MLmodel
```

## Notas de mejores prácticas

- Separación de lógica: API, servicios, modelos y utilidades.
- Logging estructurado y centralizado.
- Configuración desacoplada y versionada.
- Validación estricta de datos de entrada.
- Fácil extensión para nuevos modelos, servicios o endpoints.