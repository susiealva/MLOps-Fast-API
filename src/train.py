
# ----------------------------------------------------
# Script principal con MLFlow para Bank Customer Churn
# ----------------------------------------------------
# Este script realiza el preprocesamiento, entrenamiento y logging del modelo
# siguiendo las mejores prácticas de MLOps y alineado con la API de predicción.

import os  # Para operaciones de sistema si se requieren
import mlflow  # MLflow para tracking de experimentos
import pandas as pd  # Manipulación de datos

# preparación de datos
from sklearn.model_selection import train_test_split  # División de datos
from sklearn.preprocessing import StandardScaler  # Escalado de variables numéricas

# modelos
import mlflow.sklearn  # MLflow para modelos sklearn
from sklearn.linear_model import LogisticRegression  # Modelo de regresión logística
from sklearn.ensemble import RandomForestClassifier  # Modelo de bosque aleatorio
import mlflow.xgboost  # MLflow para modelos de ensamblaje xgboost
from xgboost import XGBClassifier
from sklearn.neural_network import MLPClassifier  # Modelo de red neuronal

# evaluación
from sklearn.metrics import mean_squared_error, accuracy_score  # Métricas de evaluación

# 1. Configurar el experimento de MLflow
mlflow.set_experiment("Bank_Customer_Churn")  # Nombre del experimento en MLflow
mlflow.sklearn.autolog()  # Habilita autologging de datasets

# 2. Función para cargar y preprocesar el dataset
def load_and_preprocess_data(path="data/Bank Customer Churn Prediction.csv"):
    """
    Carga el dataset, renombra la columna objetivo, codifica variables categóricas,
    elimina columnas irrelevantes y escala variables numéricas.
    """
    df = pd.read_csv(path)  # Cargar datos desde CSV
    # Renombrar la columna objetivo para consistencia
    df = df.rename(columns={"churn": "target"})

    # Filtrar solo registros donde country sea 'spain' (en minúsculas)
    df = df[df["country"].str.lower() == "spain"]

    # Codificar género: Male=1, Female=0
    df["gender"] = df["gender"].map({"Male": 1, "Female": 0})

    # Eliminar columnas que no se usan en el modelo
    drop_cols = ["customer_id", "country"]
    df = df.drop(columns=drop_cols)

    # Escalar variables numéricas (excepto las binarias/categóricas)
    num_cols = [c for c in df.columns if c not in ["gender",
                                                   "credit_card",
                                                   "active_member",
                                                   "products_number",
                                                   "target"]]
    scaler = StandardScaler()
    df[num_cols] = scaler.fit_transform(df[num_cols])

    return df

# 3. Función principal de entrenamiento y logging
def train_and_log():
    """
    Ejecuta el pipeline de entrenamiento: carga datos, divide en train/test,
    entrena un modelo de regresión logística, evalúa y loggea todo en MLflow.
    """
    df = load_and_preprocess_data()  # Cargar y preprocesar datos

    # Separar variables predictoras y objetivo
    X = df.drop(columns="target")
    y = df["target"]

    # División en train/test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Entrenamiento y logging con MLflow
    with mlflow.start_run(run_name="MLP_Model"):
        
        mlp = MLPClassifier(
            hidden_layer_sizes=(16, 8), 
            max_iter=500, 
            activation='relu', 
            solver='adam', 
            random_state=42
        )

        # 2. Entrenar el modelo
        mlp.fit(X_train, y_train)

        # 3. Predicción y métrica
        predictions = mlp.predict(X_test)
        acc = accuracy_score(y_test, predictions)
        
        # Registro en MLflow
        mlflow.log_param("layers", "100, 50")
        mlflow.log_param("activation", "relu")
        mlflow.log_metric("accuracy", acc)
                
        # Guardar el modelo en el registro de MLflow
        mlflow.sklearn.log_model(mlp, "mlp_model")

# 4. Entry point del script
if __name__ == "__main__":
    train_and_log()  # Ejecutar pipeline completo