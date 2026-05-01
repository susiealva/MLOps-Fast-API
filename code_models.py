import kagglehub
import os
import pandas as pd

# Download latest version
path = kagglehub.dataset_download("gauravtopre/bank-customer-churn-dataset")
print("Path to dataset files:", path)

archivo = os.listdir(path)[0]

# ruta completa
ruta_completa = os.path.join(path, archivo)

# leemos el CSV
df = pd.read_csv(ruta_completa)

print("¡Éxito! Dataset cargado.")
print(df.head())
print(df.info())

# nos quedamos solo con España
df = df.loc[df['country'] == 'Spain']

# y elimino la columna del país, porque no la necesito para las predicciones
df.drop(columns='country', inplace=True)

print(df)