import streamlit as st
import pandas as pd
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_groq import ChatGroq # <--- NUEVA IMPORTACIÓN

def render_chatbot(df):
    """
    Renderiza la vista del Asesor Chatbot y lo conecta con el DataFrame usando Groq.
    """
    # Clave de API GROQ
    api_key = "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" 

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "¡Hola! Soy tu asistente. ¿En qué te puedo ayudar hoy?"}
        ]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Escribe tu consulta..."):
        
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Pensando..."):
                try:
                    # Usamos caché para que el agente no se re-instancie en cada pregunta
                    @st.cache_resource(show_spinner=False)
                    def get_fast_agent(_df, _api_key):
                        llm = ChatGroq(
                            temperature=0, 
                            groq_api_key=_api_key, 
                            model_name="llama-3.3-70b-versatile"
                        )
                        return create_pandas_dataframe_agent(
                            llm, 
                            _df, 
                            verbose=False, 
                            allow_dangerous_code=True,
                            agent_type="zero-shot-react-description",
                            max_iterations=3  # <-- CLAVE: Evita bucles largos de razonamiento
                        )
                    
                    agent = get_fast_agent(df, api_key)
                    
                    # 3. Ejecutar la consulta
                    # Instruimos al agente que solo la 'Final Answer' debe ser en español,
                    # para no romper el parser interno de Langchain que busca las palabras en inglés.
                    instruccion = "You MUST use English for your Thought and Action steps, but your 'Final Answer' MUST be in Spanish, friendly, and concise. User query: "
                    response = agent.invoke(instruccion + prompt)
                    respuesta_texto = response.get("output") if isinstance(response, dict) else response
                    
                    # Mostrar y guardar respuesta
                    st.markdown(respuesta_texto)
                    st.session_state.messages.append({"role": "assistant", "content": respuesta_texto})
                    
                except Exception as e:
                    error_msg = str(e)
                    if "429" in error_msg or "Rate limit" in error_msg:
                        mensaje_error = "⚠️ Has alcanzado el límite de consultas gratuitas de la Inteligencia Artificial por ahora. Por favor, intenta de nuevo en un par de minutos."
                        st.error(mensaje_error)
                        # Removemos el mensaje vacío que queda si hay error
                        if st.session_state.messages[-1]["role"] == "user":
                            pass # Opcional: podrías eliminar el mensaje del usuario si falla
                    else:
                        st.error(f"Ocurrió un error al consultar los datos: {e}")