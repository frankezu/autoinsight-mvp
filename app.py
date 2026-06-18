import streamlit as st

# Configuración inicial de la página (DEBE ser la primera llamada a st)
st.set_page_config(
    page_title="AutoInsight MVP",
    layout="wide"
)

# Importaciones de los módulos locales
from src.data_loader import get_cleaned_data
from src.styles import apply_custom_styles
from src.views.home import render_home
from src.views.catalog import render_catalog
from src.views.chatbot import render_chatbot

def main():
    # 1. Inyectar CSS y estilos
    apply_custom_styles()

    # 2. Cargar los datos desde el CSV limpio
    df = get_cleaned_data()

    # 3. Construir la barra lateral (Sidebar) de navegación
    with st.sidebar:
        st.title("AutoInsight")
        st.markdown("Navegación del prototipo:")
        menu = st.radio("Ir a:", ["Inicio", "Buscador", "Asesor Chatbot"])
        
        st.markdown("---")
        st.caption("Desarrollado para Samsung Innovation Campus 2026")

    # 4. Renderizar la vista correspondiente según el menú seleccionado
    if menu == "Inicio":
        render_home()
        
    elif menu == "Buscador":
        render_catalog(df)
        
    elif menu == "Asesor Chatbot":
        render_chatbot(df)

if __name__ == "__main__":
    main()
