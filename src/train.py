
# ----------------------------------------------------
# Script principal con MLFlow para Bank Customer Churn
# ----------------------------------------------------
# Este script realiza el preprocesamiento, entrenamiento y logging del modelo
# siguiendo las mejores prácticas de MLOps y alineado con la API de predicción.

import os  # Para operaciones de sistema si se requieren
import mlflow  # MLflow para tracking de experimentos
import mlflow.sklearn  # MLflow para modelos sklearn
import pandas as pd  # Manipulación de datos
from sklearn.model_selection import train_test_split  # División de datos
from sklearn.linear_model import LogisticRegression  # Modelo de regresión logística
from sklearn.ensemble import RandomForestClassifier  # Modelo de bosque aleatorio
from sklearn.metrics import mean_squared_error, accuracy_score  # Métrica de evaluación
from sklearn.preprocessing import StandardScaler  # Escalado de variables numéricas

# 1. Configurar el experimento de MLflow
mlflow.set_experiment("Bank_Customer_Churn")  # Nombre del experimento en MLflow
mlflow.sklearn.autolog()  # Habilita autologging para sklearn

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
    with mlflow.start_run(run_name="RandomForest_Classifier"):
        model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
    
        # 2. Entrenar el modelo
        model.fit(X_train, y_train)
        
        # 3. Predicción y métrica
        predictions = model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        # Nota: Si es clasificación, podrías querer registrar también el 'accuracy'
        acc = accuracy_score(y_test, predictions)
        
        print(f"Entrenamiento completado. MSE: {mse} | Accuracy: {acc}")
        
        # 4. Logging manual en MLflow
        mlflow.log_param("model_type", "RandomForest")
        mlflow.log_param("n_estimators", 100)
        mlflow.log_param("max_depth", 5)
        
        mlflow.log_metric("mse", mse)
        mlflow.log_metric("accuracy", acc)
        
        # Guardar el modelo en el registro de MLflow
        mlflow.sklearn.log_model(model, "random_forest_model")

# 4. Entry point del script
if __name__ == "__main__":
    train_and_log()  # Ejecutar pipeline completo