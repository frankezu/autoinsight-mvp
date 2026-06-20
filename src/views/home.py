import streamlit as st
import pandas as pd
import altair as alt

def render_home(df):
    """
    Renderiza la vista principal (Inicio) con métricas, gráficos analíticos y diseño minimalista.
    """
    if df.empty:
        st.warning("El dataset está vacío o no se ha podido cargar.")
        return

    # 1. Hero Section
    st.markdown("""
    <div style='text-align: center; padding: 2rem 0; font-family: "Inter", sans-serif;'>
        <h1 style='font-size: 2.8rem; color: #111827; margin-bottom: 15px; font-weight: 800; letter-spacing: -1px;'>Bienvenido a AutoInsight</h1>
        <p style='font-size: 1.15rem; color: #4b5563; max-width: 800px; margin: 0 auto; line-height: 1.6;'>
            Redefiniendo la experiencia de compra automotriz. Una plataforma que integra un catálogo de inventario dinámico con inteligencia artificial responsiva.
        </p>
    </div>
    <hr style='border: none; border-top: 1px solid #e5e7eb; margin: 10px 0 30px 0;'>
    """, unsafe_allow_html=True)

    # 2. MÉTRICAS DINÁMICAS
    total_vehiculos = f"{len(df):,}".replace(",", ".")
    precio_promedio = f"${int(df['askprice'].mean()):,}".replace(",", ".")
    marca_popular = df['brand'].mode()[0].capitalize()
    km_promedio = f"{int(df['kmdriven'].mean()):,}".replace(",", ".")
    
    st.markdown("<p style='color: #6b7280; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 15px; font-weight: 600;'>Resumen del Inventario en Tiempo Real</p>", unsafe_allow_html=True)
    
    m1, m2, m3, m4 = st.columns(4)
    m1.metric(label="Vehículos en Stock", value=total_vehiculos)
    m2.metric(label="Precio Promedio (CLP)", value=precio_promedio)
    m3.metric(label="Marca Popular", value=marca_popular)
    m4.metric(label="Kilometraje Promedio", value=f"{km_promedio} km")

    st.markdown("<hr style='border: none; border-top: 1px solid #e5e7eb; margin: 30px 0 30px 0;'>", unsafe_allow_html=True)

    # 3. GRÁFICO: VOLUMEN POR MARCA (Mejorado)
    st.markdown("<h3 style='color: #111827; font-size: 1.1rem; margin-bottom: 20px;'>Marcas con mayor stock</h3>", unsafe_allow_html=True)
    
    df_marcas = df['brand'].value_counts().head(8).reset_index()
    df_marcas.columns = ['brand', 'count']

    # Gráfico de barras horizontales con etiquetas
    c1 = alt.Chart(df_marcas).mark_bar(
        cornerRadiusTopRight=5, cornerRadiusBottomRight=5, color='#374151'
    ).encode(
        x=alt.X('count', title=None, axis=alt.Axis(format='d')),
        y=alt.Y('brand', sort='-x', title=None),
        tooltip=['brand', 'count']
    )
    text = c1.mark_text(align='left', baseline='middle', dx=3, color='#4b5563').encode(text='count')
    
    st.altair_chart((c1 + text), use_container_width=True)

    st.markdown("<hr style='border: none; border-top: 1px solid #e5e7eb; margin: 30px 0 30px 0;'>", unsafe_allow_html=True)

    # 4. CARACTERÍSTICAS
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("<h3 style='color: #111827; font-size: 1.1rem;'>Catálogo Estructural</h3>", unsafe_allow_html=True)
        st.markdown("<p style='color: #6b7280; font-size: 0.95rem; line-height: 1.6;'>Interfaz minimalista diseñada para precisión de búsqueda.</p>", unsafe_allow_html=True)
    with col2:
        st.markdown("<h3 style='color: #111827; font-size: 1.1rem;'>Asesoría Inteligente</h3>", unsafe_allow_html=True)
        st.markdown("<p style='color: #6b7280; font-size: 0.95rem; line-height: 1.6;'>Agente virtual que analiza datos y compara opciones en tiempo real.</p>", unsafe_allow_html=True)
    with col3:
        st.markdown("<h3 style='color: #111827; font-size: 1.1rem;'>Decisión Informada</h3>", unsafe_allow_html=True)
        st.markdown("<p style='color: #6b7280; font-size: 0.95rem; line-height: 1.6;'>Cruzamos información financiera y técnica para asegurar la mejor calidad-precio.</p>", unsafe_allow_html=True)

    # 5. FOOTER
    st.markdown("""
    <div style='text-align: center; margin-top: 50px; padding: 2rem; border-top: 1px solid #e5e7eb;'>
        <p style='font-size: 14px; color: #4b5563; max-width: 850px; margin: 0 auto; line-height: 1.6; font-family: "Inter", sans-serif;'>
            <strong>Nota de Infraestructura (MVP):</strong> Esta plataforma opera como un Producto Mínimo Viable orientado a validar la integración de modelos de lenguaje (LLMs) con bases de datos relacionales en memoria. Actualmente utiliza un dataset internacional adaptado financieramente (CLP) para propósitos de demostración técnica. 
            <br><br>
            La eficiencia lograda con este volumen de datos valida nuestra arquitectura de procesamiento, confirmando que el sistema es completamente escalable y aplicable a inventarios reales del mercado automotriz chileno. La herramienta integra análisis estadístico mediante Pandas y visualización reactiva con Altair.
            <br><br>
            <span style='color: #111827; font-weight: 600;'>Desarrollado para Samsung Innovation Campus por: Ariel Leiva y Franco Bernal.</span>
        </p>
    </div>
    """, unsafe_allow_html=True)