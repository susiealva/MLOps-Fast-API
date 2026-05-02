# --------------------------------------
# Logger centralizado para la aplicación
# --------------------------------------
# Configura el logger para toda la app con formato y nivel adecuado.

import logging  # Módulo estándar de logging
import sys  # Para salida estándar

# Crear logger principal
logger = logging.getLogger("mlops-app")
logger.setLevel(logging.INFO)  # Nivel por defecto

# Handler para imprimir en consola
handler = logging.StreamHandler(sys.stdout)
# Formato de los mensajes de log
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Evitar agregar múltiples handlers si ya existe
if not logger.handlers:
    logger.addHandler(handler)
