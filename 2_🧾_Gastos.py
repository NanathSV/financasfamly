import streamlit as st
import pandas as pd
from database import get_connection
from datetime import date

st.header("🧾 Gastos")

conn = get_connection()

data = st.date_input("Data", value=date.today())
descricao = st.text_input("Descrição")
valor = st.number_input("Valor", min_value=0.0)
categoria = st.selectbox("Categoria", ["Necessidades", "Desejos"])
tag = st.text_input("Tag (ex: alimentação, moradia)")

if st.button("Adicionar gasto"):
    conn.execute("""
        INSERT INTO gastos (data, descricao, valor, categoria, tag)
        VALUES (?, ?, ?, ?, ?)
    """, (data, descricao, valor, categoria, tag))
    conn.commit()
    st.success("Gasto registrado!")

st.divider()

df = pd.read_sql("SELECT * FROM gastos", conn)
st.dataframe(df)
