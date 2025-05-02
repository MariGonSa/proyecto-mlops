# Proyecto Final - MLOps 🧠

Este proyecto implementa un modelo de machine learning para predecir la calidad del vino (dataset Wine Quality) con un flujo completo de MLOps que incluye entrenamiento, reentrenamiento, API de consumo, conteinerización, CI/CD, y versionamiento de modelo/datos.

---

## 👩‍💻 Estudiante

- **Mariana González Sancho**  
- Desarrollado individualmente  
- GitHub: [@MariGonSa](https://github.com/MariGonSa)

---

## 🔀 Branches utilizados

- `main` – rama principal de entrega  
- `develop` – desarrollo  
- `staging` – pruebas

---

## 🧪 Dataset utilizado

- [Wine Quality Dataset (white)](https://archive.ics.uci.edu/ml/datasets/wine+quality)
- Archivo: `winequality-white.csv`

---

## 🤖 Modelo de Machine Learning

- Algoritmo: `RandomForestClassifier`
- Librerías: `scikit-learn`, `pandas`, `joblib`

---

## ⚙️ Scripts incluidos

- `modelo_vino.ipynb`: Notebook con el entrenamiento original
- `reentrenamiento.py`: Script que automatiza el reentrenamiento
- `main.py`: API creada con FastAPI
- `Dockerfile`: Conteinerización para despliegue
- `.github/workflows/deploy.yml`: CI/CD con GitHub Actions

---

## 🔁 Reentrenamiento con CI/CD

Cada vez que se hace `push` a la rama `main`, se ejecuta:

1. Instalación de dependencias
2. Reentrenamiento del modelo
3. Generación de `modelo_entrenado.pkl`

---

## ☁️ Versionamiento con DVC

- Dataset y modelo están versionados con DVC

---

## 📦 Ejecutar el API localmente (FastAPI)

```bash
uvicorn main:app --reload
