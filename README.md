
# MLOps-Fast-API
El objetivo de este challenge es poner en práctica lo aprendido de MLFlow y la puesta en producción de un modelo.

# Creación de entorno conda (opcional recomendado)

Si prefieres usar conda para un entorno reproducible, ejecuta:

```bash
conda env create -f environment.yml
conda activate mlops-fastapi
```

Esto instalará todas las dependencias necesarias en un entorno limpio.

# Instalación y descarga automática del dataset

1. Instala las dependencias:
	```bash
	pip install -r requirements.txt
	```

2. Configura tu token de Kaggle:
	- Descarga tu archivo `kaggle.json` desde tu cuenta de Kaggle (https://www.kaggle.com/ -> Account -> Create New API Token).
	- Cópialo en la ruta `~/.kaggle/kaggle.json` o exporta la variable de entorno:
	  ```bash
	  export KAGGLE_USERNAME=TU_USUARIO
	  export KAGGLE_KEY=TU_API_KEY
	  ```

3. Descarga el dataset automáticamente:
	```bash
	python src/load_data.py
	```

Esto descargará y descomprimirá el dataset de Bank Customer Churn (https://www.kaggle.com/datasets/gauravtopre/bank-customer-churn-dataset) en la carpeta `data/`.