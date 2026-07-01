# Catálogo Automotriz con asistente de IA

Proyecto desarrollado para el programa **[Samsung Innovation Campus](https://innovationcampus.cl/): C&P** (edición 2026).

El sistema (**AutoInsight**) es un prototipo MVP que integra un Asistente Virtual de IA capaz de procesar un catálogo de vehículos usados en tiempo real. Su objetivo es guiar a los usuarios hacia las mejores oportunidades del mercado, basándose en la influencia del año de fabricación, el kilometraje y el tipo de transmisión sobre la depreciación del vehículo. La solución está desplegada como una aplicación web interactiva utilizando Streamlit.

## Equipo
- [Ariel Leiva](https://github.com/Ariel-Leiva)
- [Franco Bernal](https://github.com/frankezu)

## Dataset
- **Fuente**: [Kaggle - mohitkumar282/used-car-dataset](https://www.kaggle.com/datasets/mohitkumar282/used-car-dataset)
- **Filas**: 14,993
- **Columnas**: 11
- **Licencia**: Uso Público (Extraído de portales online de vehículos)

## Pregunta de análisis
¿Cuáles son los principales atributos que influyen en la depreciación de un vehículo en el mercado de usados, y cómo podemos utilizar Inteligencia Artificial sobre estos datos para ayudar a los usuarios a tomar decisiones de compra rentables y fundamentadas?

## Hallazgo principal
El análisis exploratorio reveló que la depreciación de un vehículo está fuertemente determinada por la intersección del **año de fabricación, kilometraje y tipo de transmisión**. Los autos automáticos y de bajo kilometraje retienen un valor premium significativamente superior. Dado que calcular manualmente el impacto de estas variables es complejo para un comprador promedio, concluimos que la mejor solución analítica era construir **AutoInsight**: un prototipo MVP con un Asistente Virtual de IA capaz de procesar este catálogo en tiempo real y guiar a los usuarios hacia las mejores oportunidades del mercado. *(Nota: validado con datos de India convertidos a CLP para simular escalabilidad local).*

---

### Instrucciones para ejecución local
1. Clona el repositorio.
2. Instala las dependencias con `pip install -r requirements.txt`.
3. Ejecuta el notebook `notebooks/eda.ipynb` para cargar y limpiar los datos (conversión a pesos chilenos y limpieza de strings).
4. Ejecuta la aplicación web mediante el comando:
   ```bash
   streamlit run app.py
   ```
