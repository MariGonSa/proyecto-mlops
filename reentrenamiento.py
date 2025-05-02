import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

df = pd.read_csv("winequality-white.csv", sep=";")
X = df.drop("quality", axis=1)
y = df["quality"]

modelo = RandomForestClassifier()
modelo.fit(X, y)

joblib.dump(modelo, "modelo_entrenado.pkl")
