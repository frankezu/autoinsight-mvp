import streamlit as st
import pandas as pd

def render_catalog(df):
    """
    Renderiza la vista del catálogo o buscador de vehículos.
    """
    st.title("Buscador de Vehículos")
    st.markdown("Utiliza los filtros de la izquierda para explorar el catálogo.")
    
    if df.empty:
        st.warning("El dataset está vacío. Por favor, verifica la carga de datos.")
        return

    # Contenedor de filtros en un expansor para mantener la interfaz limpia
    with st.expander("Filtros de Búsqueda", expanded=True):
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            marcas = df['brand'].dropna().unique()
            selected_brand = st.selectbox("Marca", options=["Todas"] + sorted(list(marcas)))
            
            # El modelo depende de la marca seleccionada
            if selected_brand != "Todas":
                modelos = df[df['brand'] == selected_brand]['model'].dropna().unique()
            else:
                modelos = df['model'].dropna().unique()
            selected_model = st.selectbox("Modelo", options=["Todos"] + sorted(list(modelos)))
            
        with col2:
            min_year = int(df['year'].min())
            max_year = int(df['year'].max())
            selected_years = st.slider("Rango de Años", min_value=min_year, max_value=max_year, value=(min_year, max_year))
            
            max_km = int(df['kmdriven'].max())
            selected_km = st.slider("Kilometraje máximo", min_value=0, max_value=max_km, value=max_km, step=5000)
            st.caption(f"KM seleccionado: **{selected_km:,} km**".replace(",", "."))

        with col3:
            max_price = int(df['askprice'].max())
            selected_price = st.slider("Precio máximo (CLP)", min_value=0, max_value=max_price, value=max_price, step=500000)
            st.caption(f"Precio seleccionado: **${selected_price:,} CLP**".replace(",", "."))
            
            transmisiones = df['transmission'].dropna().unique()
            selected_trans = st.selectbox("Transmisión", options=["Todas"] + list(transmisiones))

        with col4:
            combustibles = df['fueltype'].dropna().unique()
            selected_fuel = st.selectbox("Combustible", options=["Todos"] + list(combustibles))
            
            dueños = df['owner'].dropna().unique()
            selected_owner = st.selectbox("Dueño", options=["Todos"] + list(dueños))

    # Filtrar datos
    filtered_df = df.copy()
    
    if selected_brand != "Todas":
        filtered_df = filtered_df[filtered_df['brand'] == selected_brand]
    if selected_model != "Todos":
        filtered_df = filtered_df[filtered_df['model'] == selected_model]
        
    filtered_df = filtered_df[
        (filtered_df['year'] >= selected_years[0]) & 
        (filtered_df['year'] <= selected_years[1])
    ]
    
    filtered_df = filtered_df[filtered_df['kmdriven'] <= selected_km]
    filtered_df = filtered_df[filtered_df['askprice'] <= selected_price]
    
    if selected_trans != "Todas":
        filtered_df = filtered_df[filtered_df['transmission'] == selected_trans]
    if selected_fuel != "Todos":
        filtered_df = filtered_df[filtered_df['fueltype'] == selected_fuel]
    if selected_owner != "Todos":
        filtered_df = filtered_df[filtered_df['owner'] == selected_owner]
        
    st.write(f"**Mostrando {len(filtered_df)} resultados:**")
    
    # Formatear números en la tabla con separador de miles usando puntos (.)
    styled_df = filtered_df.head(100).style.format(
        formatter={
            "askprice": lambda x: f"${int(x):,}".replace(",", ".") if pd.notna(x) else "",
            "kmdriven": lambda x: f"{int(x):,}".replace(",", ".") if pd.notna(x) else "",
            "year": lambda x: f"{int(x)}" if pd.notna(x) else "",
            "age": lambda x: f"{int(x)}" if pd.notna(x) else ""
        }
    )
    st.dataframe(styled_df, use_container_width=True)

