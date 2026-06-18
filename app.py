import streamlit as st
import pandas as pd
import os

st.title("Dashboard de Autos")

@st.cache_data
def load_data():
    file_path = os.path.join("data", "used_cars_dataset_v2_clean.csv")
    if not os.path.exists(file_path):
        st.error(f"No se encontró el dataset en: {file_path}")
        return pd.DataFrame()
    return pd.read_csv(file_path)

df = load_data()

if not df.empty:
    st.write("Dataset cargado correctamente. Primeras filas:")
    st.dataframe(df.head())
    
    # Aquí puedes agregar tus filtros, KPIs y visualizaciones.
else:
    st.warning("Por favor, ejecuta el notebook para descargar los datos primero.")
