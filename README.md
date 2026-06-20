# AutoInsight - Proyecto C&P Samsung Innovation Campus 2026

**Repositorio:** [GitHub - AutoInsight](https://github.com/frankezu/autoinsight-app)

## Equipo
- Ariel Leiva (GitHub: [@Ariel-Leiva](https://github.com/Ariel-Leiva))
- Franco Bernal (GitHub: [@frankezu](https://github.com/frankezu))

## Dataset
- **Fuente**: [Kaggle - mohitkumar282/used-car-dataset](https://www.kaggle.com/datasets/mohitkumar282/used-car-dataset)
- **Filas**: 14,993
- **Columnas**: 11
- **Licencia**: Uso Público (Extraído de portales online de vehículos)

## Pregunta de análisis
¿Cómo podemos utilizar un catálogo de datos de vehículos para construir un MVP de venta de autos usados con Inteligencia Artificial integrada, que mejore y simplifique la experiencia de los usuarios?

## Hallazgo principal
El análisis de los datos nos permitió estructurar un catálogo robusto. Basándonos en esta información, construimos **AutoInsight**, un prototipo MVP de venta de autos usados con Inteligencia Artificial integrada. Nuestra plataforma permite explorar el mercado actual mediante filtros dinámicos y consultar con un Asesor Virtual Inteligente que ayuda a los usuarios a encontrar el vehículo ideal de manera fundamentada. *(Nota: validado con datos de India convertidos a CLP para simular escalabilidad local).*

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
