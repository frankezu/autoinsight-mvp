import streamlit as st
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_google_genai import ChatGoogleGenerativeAI

@st.cache_resource(show_spinner=False)
def get_cached_agent(_df, api_key):
    """
    Crea y retorna una instancia en caché del agente de Pandas 
    conectado a Gemini. Evita re-instanciar el LLM en cada mensaje.
    """
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash", 
        google_api_key=api_key, 
        temperature=0
    )
    
    agent = create_pandas_dataframe_agent(
        llm, 
        _df, 
        verbose=False, 
        allow_dangerous_code=True,
        agent_type="zero-shot-react-description",
        handle_parsing_errors=True
    )
    
    return agent
