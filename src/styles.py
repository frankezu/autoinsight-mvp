import streamlit as st

def apply_custom_styles():
    """
    Inyecta código CSS para personalizar el diseño de la aplicación.
    Puedes agregar tus estilos aquí.
    """
    st.markdown("""
        <style>
        /* Ejemplo: Cambiar el color de fondo de la app */
        /* .stApp { background-color: #0e1117; } */
        
        /* Ejemplo: Personalizar botones */
        /*
        .stButton>button {
            border-radius: 8px;
            border: 1px solid #FF4B4B;
        }
        */
        </style>
    """, unsafe_allow_html=True)
