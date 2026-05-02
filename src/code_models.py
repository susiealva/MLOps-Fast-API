# --------------------------------------
# Ejemplo de carga y filtrado de dataset
# --------------------------------------
# Descarga el dataset desde KaggleHub, lo carga y filtra solo España.

import kagglehub  # Para descargar datasets de Kaggle
import os  # Operaciones de sistema
import pandas as pd  # Manipulación de datos

# Descargar la última versión del dataset
path = kagglehub.dataset_download("gauravtopre/bank-customer-churn-dataset")
print("Path to dataset files:", path)

# Seleccionar el primer archivo descargado
archivo = os.listdir(path)[0]

# Ruta completa al archivo CSV
ruta_completa = os.path.join(path, archivo)

# Leer el CSV en un DataFrame
df = pd.read_csv(ruta_completa)

print("¡Éxito! Dataset cargado.")
print(df.head())
print(df.info())

# Filtrar solo registros de España
df = df.loc[df['country'] == 'Spain']

# Eliminar la columna del país (no se usa en predicción)
df.drop(columns='country', inplace=True)

print(df)