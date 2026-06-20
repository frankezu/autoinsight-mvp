import streamlit as st

def apply_custom_styles():
    """
    Inyecta código CSS para personalizar el diseño de la aplicación.
    Puedes agregar tus estilos aquí.
    """
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

        /* Oculta los enlaces de anclaje de Streamlit */
        h1 a, h2 a, h3 a, h4 a, h5 a, h6 a {
            display: none !important;
        }
                
        /* Minimalist and clean style (adaptable to light/dark mode) */
        html, body, .stApp, h1, h2, h3, h4, h5, h6, p, li, a, button, input, label, th, td, div[data-testid="stMarkdownContainer"] {
            font-family: "Inter", sans-serif !important;
        }
        
        /* Premium, larger, bolder, uppercase tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 32px;
            border-bottom: 1px solid rgba(128, 128, 128, 0.2);
        }
        .stTabs [data-baseweb="tab"] {
            padding: 12px 0;
        }
        .stTabs [data-baseweb="tab"] p {
            font-weight: 700 !important;
            font-size: 18px !important;
            text-transform: uppercase !important;
            letter-spacing: 1px !important;
        }
        
        /* Minimalist Buttons */
        .stButton>button {
            border-radius: 4px;
            border: 1px solid rgba(128, 128, 128, 0.3);
            background-color: transparent;
            transition: all 0.2s ease;
        }
        .stButton>button:hover {
            border-color: rgba(128, 128, 128, 0.6);
            background-color: rgba(128, 128, 128, 0.05);
        }
        
        /* Clean expanders */
        .streamlit-expanderHeader {
            border: none;
            background-color: transparent;
        }
        div[data-testid="stExpander"] {
            border: 1px solid #e5e7eb;
            border-radius: 6px;
        }
        
        /* Estilos para inputs y selectboxes */
        .stTextInput>div>div>input {
            border-radius: 6px !important;
            border: 1px solid #d1d5db !important;
            transition: all 0.2s ease;
        }
        .stTextInput>div>div>input:focus {
            border-color: #111827 !important;
            box-shadow: 0 0 0 1px #111827 !important;
        }
        .stSelectbox>div>div>div {
            border-radius: 6px !important;
            border: 1px solid #d1d5db !important;
            transition: all 0.2s;
        }
        
        /* Contenedor principal: limitar el ancho máximo para una lectura cómoda (estilo SaaS real) */
        .main .block-container {
            max-width: 1100px !important;
            padding-top: 2rem !important;
            padding-bottom: 3rem !important;
        }

        /* Hide default Streamlit decorations for a true minimalist feel */
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)
