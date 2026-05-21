import streamlit as st
import pickle
import os # <--- 1. Agregamos esta librería básica de Python

# 2. Le decimos a Python que averigüe dónde está guardado este 'app.py'
carpeta_actual = os.path.dirname(__file__)

# 3. Creamos la ruta correcta hacia el modelo combinando las carpetas
ruta_modelo = os.path.join(carpeta_actual, "../models/modelo_listo.pkl")

# 4. Cargamos el modelo usando esa ruta inteligente
with open(ruta_modelo, "rb") as archivo_modelo:
    modelo = pickle.load(archivo_modelo)

# Diccionario sencillo para traducir el número a nombre de flor
nombres_flores = {
    0: "Iris Setosa",
    1: "Iris Versicolor",
    2: "Iris Virginica"
}

# Diseño pag
st.title("🌸 LIVASQUE Predictor de Flores Iris")
st.write("Mueve los controles de abajo para ingresar las medidas y predecir el tipo de flor.")

# Controles slider
ancho_petalo = st.slider("Ancho del pétalo", min_value=0.0, max_value=4.0, step=0.1)
largo_petalo = st.slider("Largo del pétalo", min_value=0.0, max_value=4.0, step=0.1)
ancho_sepalo = st.slider("Ancho del sépalo", min_value=0.0, max_value=4.0, step=0.1)
largo_sepalo = st.slider("Largo del sépalo", min_value=0.0, max_value=4.0, step=0.1)

# Boton de prediccion
if st.button("Predecir la flor"):
    datos_ingresados = [[ancho_petalo, largo_petalo, ancho_sepalo, largo_sepalo]]
    
    numero_prediccion = modelo.predict(datos_ingresados)[0]
    resultado_final = nombres_flores[numero_prediccion]

    st.write("La flor es de tipo:", resultado_final)
