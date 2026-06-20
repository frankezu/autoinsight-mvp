# AutoInsight - Proyecto SIC 2026

## Equipo
- Ariel Leiva (GitHub: @Ariel-Leiva)
- Franco Bernal (GitHub: @frankezu)

## Dataset
- **Fuente**: [Kaggle - mohitkumar282/used-car-dataset](https://www.kaggle.com/datasets/mohitkumar282/used-car-dataset)
- **Filas**: 14,993
- **Columnas**: 11
- **Licencia**: Uso Público (Extraído de portales online de vehículos)

## Pregunta de análisis
¿Cómo impactan el kilometraje (`kmdriven`), la edad del auto (`age`) y el tipo de transmisión en el precio de reventa estimado de los vehículos usados? (Prototipo MVP validado con datos del mercado de India, escalable al mercado local).

## Hallazgo principal
El precio de los vehículos usados disminuye de manera predecible a medida que aumenta el kilometraje y la edad del auto (depreciación). Además, los vehículos con transmisión automática tienden a retener un mayor valor de reventa. **Nota:** Los precios originales en Rupias Indias (INR) han sido convertidos a Pesos Chilenos (CLP) para demostrar la viabilidad del MVP en un contexto local.

## Link al dashboard
*(Rellena aquí con la URL de tu app desplegada en Streamlit Community Cloud)*
https://[tu-proyecto].streamlit.app

---

### Instrucciones para ejecución local
1. Clona el repositorio.
2. Instala las dependencias con `pip install -r requirements.txt`.
3. Ejecuta el notebook `notebooks/01_eda.ipynb` para cargar y limpiar los datos (conversión a pesos chilenos y limpieza de strings).
4. Ejecuta la aplicación web mediante el comando:
   ```bash
   streamlit run app.py
   ```
