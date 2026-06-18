import streamlit as st

def render_home():
    """
    Renderiza la vista principal (Inicio).
    """
    st.title("AutoInsight MVP")
    st.markdown("""
    Bienvenido a AutoInsight. Esta plataforma te permite explorar el mercado de vehículos usados, 
    analizar tendencias y estimar precios de reventa.
    
    ### ¿Qué puedes hacer aquí?
    - **Buscador de Vehículos:** Filtra y explora el catálogo de autos.
    - **Asesor Chatbot:** Interactúa con un asistente virtual para recibir recomendaciones y analizar precios.
    """)
