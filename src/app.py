import streamlit as st
import pickle

# Cargar el modelo que ya tenia
archivo_modelo = open("../models/modelo_listo.pkl", "rb")
modelo = pickle.load(archivo_modelo)
archivo_modelo.close()

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