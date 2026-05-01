import os
import subprocess

def download_telco_dataset():
    # Asegura que la carpeta data/ existe
    os.makedirs('data', exist_ok=True)
    # Descarga el dataset de Kaggle
    try:
        subprocess.run([
            'kaggle', 'datasets', 'download', 
            '-d', 'blastchar/telco-customer-churn',
            '-p', 'data', '--unzip'
        ], check=True)
        print('Dataset descargado y descomprimido en data/')
    except Exception as e:
        print('Error al descargar el dataset:', e)

if __name__ == "__main__":
    download_telco_dataset()
