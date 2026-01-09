import streamlit as st
from database import create_tables

st.set_page_config(
    page_title="Controle Financeiro Familiar",
    layout="wide"
)

create_tables()

st.title("💰 Controle Financeiro Familiar")
st.markdown("""
Sistema simples para organizar a renda da casa, gastos e visualizar tudo em um dashboard claro.
Use o menu lateral para navegar.
""")
