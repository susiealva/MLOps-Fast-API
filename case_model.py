import pandas as pd
import numpy as np
from sklearn.datasets import load_breast_cancer

# Cargar el dataset
data = load_breast_cancer()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

print("Dataset cargado correctamente en el DataFrame 'df'")