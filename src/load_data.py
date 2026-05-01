import os
import subprocess

def download_dataset():
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

if __name__ == "__main__":
    download_dataset()
