import streamlit as st
import pandas as pd
import plotly.express as px
from database import get_connection
from rules import regra_70_20_10

conn = get_connection()

st.header("📊 Dashboard")

pessoas = pd.read_sql(
    "SELECT renda FROM pessoas WHERE contribui = 1",
    conn
)

renda_total = pessoas["renda"].sum()
divisao = regra_70_20_10(renda_total)

col1, col2, col3 = st.columns(3)
col1.metric("🏠 Necessidades (70%)", f"R$ {divisao['necessidades']:,.2f}")
col2.metric("💼 Poupança (20%)", f"R$ {divisao['poupanca']:,.2f}")
col3.metric("🎉 Desejos (10%)", f"R$ {divisao['desejos']:,.2f}")

st.divider()

gastos = pd.read_sql("SELECT * FROM gastos", conn)

if not gastos.empty:
    fig = px.pie(gastos, values="valor", names="tag", title="Gastos por Tag")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("Nenhum gasto registrado ainda.")
