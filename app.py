import os
import streamlit as st

# Obtener el puerto que Render asigna
port = int(os.environ.get("PORT", 8501))

st.header('Lanzar una moneda')
number_of_trials = st.slider('¿Número de intentos?', 1, 1000, 10)
start_button = st.button('Ejecutar')

if start_button:
    st.write(f'Experimento con {number_of_trials} intentos en curso.')

st.write('Esta aplicación aún no es funcional. En construcción.')

# Lanzar Streamlit en el puerto correcto
if __name__ == "__main__":
    st.run(port=port)
