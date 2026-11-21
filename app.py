import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="Tablero de Riesgos - Acerías Paz del Río 2030",
    page_icon="📊",
    layout="wide"
)

# Estilos para que el tablero ocupe todo el ancho, sin el menú ni el pie de Streamlit
st.markdown("""
    <style>
        #MainMenu, footer, header {visibility: hidden;}
        .block-container {
            padding-top: 0.5rem;
            padding-bottom: 0;
            max-width: 1320px;
        }
    </style>
""", unsafe_allow_html=True)

# Tablero interactivo (simulador del precio del acero, mapa de transversalidad,
# escenarios de estrés, valor por respuesta y tablero de 10 alertas).
# Documento integrador · Gestión de Riesgos III · Universidad El Bosque
# Jeisson David Burgos Murillo y Johan Arley Contreras Cruz
html = (Path(__file__).parent / "tablero.html").read_text(encoding="utf-8")
components.html(html, height=3500, scrolling=True)
