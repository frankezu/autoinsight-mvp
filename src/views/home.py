import streamlit as st

def render_home():
    """
    Renderiza la vista principal (Inicio) con un diseño más distribuido y profesional.
    """
    # 1. Hero Section (Centrado y llamativo)
    st.markdown("""
    <div style='text-align: center; padding: 2rem 0; font-family: "Inter", sans-serif;'>
        <h1 style='font-size: 2.8rem; color: #111827; margin-bottom: 15px; font-weight: 800;'>Bienvenido a AutoInsight</h1>
        <p style='font-size: 1.15rem; color: #4b5563; max-width: 800px; margin: 0 auto; line-height: 1.6;'>
            Redefiniendo la experiencia de compra automotriz. Una plataforma que integra un catálogo de inventario dinámico con inteligencia artificial responsiva para ofrecer asesoría inmediata y personalizada.
        </p>
    </div>
    <hr style='border: none; border-top: 1px solid #e5e7eb; margin: 10px 0 30px 0;'>
    """, unsafe_allow_html=True)

    # 2. Características en Columnas (Aprovecha el ancho de la pantalla)
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("<h3 style='color: #111827; font-size: 1.1rem;'>🔍 Catálogo Estructural</h3>", unsafe_allow_html=True)
        st.markdown("<p style='color: #6b7280; font-size: 0.95rem; line-height: 1.6;'>Explora nuestra base de vehículos mediante una interfaz minimalista, diseñada en torno a la precisión de búsqueda y la fluidez de la experiencia del usuario.</p>", unsafe_allow_html=True)

    with col2:
        st.markdown("<h3 style='color: #111827; font-size: 1.1rem;'>🤖 Asesoría Inteligente</h3>", unsafe_allow_html=True)
        st.markdown("<p style='color: #6b7280; font-size: 0.95rem; line-height: 1.6;'>Interactúa en tiempo real con un agente virtual integrado. Capacitado para analizar datos, comparar opciones y entregar feedback inmediato frente a cualquier consulta.</p>", unsafe_allow_html=True)

    with col3:
        st.markdown("<h3 style='color: #111827; font-size: 1.1rem;'>📊 Decisión Informada</h3>", unsafe_allow_html=True)
        st.markdown("<p style='color: #6b7280; font-size: 0.95rem; line-height: 1.6;'>Cruzamos la información financiera y técnica de cada vehículo para asegurar que obtengas la mejor relación calidad-precio dentro del mercado.</p>", unsafe_allow_html=True)

    # Espaciador nativo
    st.write("")
    st.write("")

    # 3. Caja de Arquitectura Técnica (Rellena visualmente y suma valor)
    st.markdown("""
    <div style='background-color: #f8fafc; padding: 2rem; border-radius: 12px; border: 1px solid #e2e8f0; margin: 2rem 0; font-family: "Inter", sans-serif;'>
        <h4 style='color: #0f172a; margin-top: 0; margin-bottom: 10px;'>⚙️ Arquitectura del Sistema</h4>
        <p style='color: #475569; font-size: 0.95rem; margin: 0; line-height: 1.6;'>
            Esta plataforma opera mediante una integración fluida de tecnologías modernas: <strong>Streamlit</strong> maneja el frontend reactivo, <strong>Pandas</strong> procesa el catálogo estructurado en memoria, y el motor LLM de alta velocidad provee el razonamiento analítico para las respuestas del chatbot.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # 4. Nota de Infraestructura (Footer sutil y elegante)
    st.markdown("""
    <div style='text-align: center; margin-top: 20px;'>
        <p style='font-size: 12px; color: #9ca3af; max-width: 850px; margin: 0 auto; line-height: 1.6; font-family: "Inter", sans-serif;'>
            <strong>Nota de Infraestructura (MVP):</strong> Esta plataforma opera como un Producto Mínimo Viable orientado a validar la integración de modelos de lenguaje (LLMs) con bases de datos. Actualmente utiliza un dataset internacional adaptado financieramente (CLP) para propósitos de demostración. La eficiencia lograda con este volumen de datos valida nuestra innovación tecnológica, confirmando que la arquitectura es completamente escalable y aplicable a inventarios reales del mercado chileno.
        </p>
    </div>
    """, unsafe_allow_html=True)