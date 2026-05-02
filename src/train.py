# Script principal con MLFlow

##Importar librerías.
import os
import pickle
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_squared_error
import pandas as pd

mlflow.set_experiment("Diabetes_Prediction")
mlflow.sklearn.autolog()

##Cargar y preprocesar el dataset.
class run_training():
    def __init__(self,df):
        self.df = df

    def run(self):
        X = self.df.drop(columns="target")
        y = self.df["target"]
    
        ##Dividir en train/test.
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        ##Definir y entrenar el modelo.
        with mlflow.start_run(run_name="Logistic_Regression_Baseline"):
            model = LogisticRegression()
            model.fit(X_train, y_train)

            predictions = model.predict(X_test)
            mse = mean_squared_error(y_test, predictions)
            print(f"Entrenamiento completado. MSE: {mse}")

            ##Loggear parámetros, métricas y modelo con MLFlow
            mlflow.log_param("model_type", "LogisticRegression")
            mlflow.log_metric("mse", mse)
            mlflow.sklearn.log_model(model, "model")

#if __name__ == "__main__":
#    run_training()

##Guardar el modelo entrenado.