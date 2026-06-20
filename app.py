import streamlit as st

st.set_page_config(
    page_title="AutoInsight",
    layout="wide"
)

from src.styles import apply_custom_styles
from src.data_loader import get_cleaned_data
from src.views.home import render_home
from src.views.catalog import render_catalog
from src.views.chatbot import render_chatbot

apply_custom_styles()
df = get_cleaned_data()

st.markdown(
    """
    <div style='font-family: "Inter", sans-serif; font-size: 46px; font-weight: 900; letter-spacing: -2px; color: #111827; margin-top: -25px; margin-bottom: 10px;'>
        AutoInsight<span style='color: #2563eb;'>.</span>
    </div>
    """,
    unsafe_allow_html=True
)

tab1, tab2, tab3 = st.tabs(["Inicio", "Catálogo", "Asistente"])

with tab1:
    render_home(df)

with tab2:
    render_catalog(df)

with tab3:
    render_chatbot(df)
