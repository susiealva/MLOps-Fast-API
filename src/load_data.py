
# --------------------------------------
# Script para descargar el dataset base
# --------------------------------------
# Descarga el dataset de Kaggle y lo descomprime en la carpeta data/

import os  # Operaciones de sistema
import subprocess  # Para ejecutar comandos externos

def download_dataset():
    """
    Descarga y descomprime el dataset de Kaggle en la carpeta data/.
    Requiere tener instalado kaggle CLI y configurado el API token.
    """
    # Asegura que la carpeta data/ existe
    os.makedirs('data', exist_ok=True)
    # Descarga el dataset de Kaggle
    try:
        subprocess.run([
            'kaggle', 'datasets', 'download', 
            '-d', 'gauravtopre/bank-customer-churn-dataset',
            '-p', 'data', '--unzip'
        ], check=True)
        print('Dataset descargado y descomprimido en data/')
    except Exception as e:
        print('Error al descargar el dataset:', e)

# Punto de entrada del script
if __name__ == "__main__":
    download_dataset()
