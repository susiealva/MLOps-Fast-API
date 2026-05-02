
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

## Instalación y descarga automática del dataset

2. Configura tu token de Kaggle:
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

3. Descarga el dataset automáticamente:
	```bash
	python src/load_data.py
	```

Esto descargará y descomprimirá el dataset de Bank Customer Churn (https://www.kaggle.com/datasets/gauravtopre/bank-customer-churn-dataset) en la carpeta `data/`.


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

1. Copia `.env.example` a `.env` y ajusta rutas si es necesario.
2. Puedes modificar parámetros en `src/config/config.yaml` para cambiar el comportamiento global.


## Entrenamiento y despliegue del modelo

### 1. Entrenamiento y logging con MLflow

Ejecuta el script de entrenamiento para preprocesar, entrenar y guardar el modelo con MLflow:

```bash
python src/train.py
```
Esto generará un modelo MLflow en la carpeta de experimentos (`mlruns/`).

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

## Notas de mejores prácticas

- Separación de lógica: API, servicios, modelos y utilidades.
- Logging estructurado y centralizado.
- Configuración desacoplada y versionada.
- Validación estricta de datos de entrada.
- Fácil extensión para nuevos modelos, servicios o endpoints.