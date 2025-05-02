from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()
modelo = joblib.load("modelo_entrenado.pkl")

@app.post("/predecir")
def predecir(data: dict):
    df = pd.DataFrame([data])
    pred = modelo.predict(df)
    return {"prediccion": int(pred[0])}
