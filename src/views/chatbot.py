import streamlit as st

def render_chatbot(df):
    """
    Renderiza la vista del Asesor Chatbot.
    """
    st.title("Asesor Chatbot")
    st.markdown("Consulta con nuestro asesor inteligente sobre qué auto comprar o si un precio es justo.")
    
    # Esqueleto de la interfaz del chat
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Mostrar historial de mensajes
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Input del usuario
    if prompt := st.chat_input("Pregúntame sobre algún vehículo..."):
        # Agregar mensaje del usuario al historial
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Mostrar mensaje del usuario
        with st.chat_message("user"):
            st.markdown(prompt)

        # Simular respuesta del asistente (Aquí conectarías tu LLM)
        response = f"Echo: Has preguntado sobre '{prompt}'. (Conecta aquí tu modelo de IA)"
        
        # Mostrar respuesta
        with st.chat_message("assistant"):
            st.markdown(response)
        
        # Agregar respuesta al historial
        st.session_state.messages.append({"role": "assistant", "content": response})
