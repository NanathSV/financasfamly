import streamlit as st
import pandas as pd
from database import get_connection

st.header("🏠 Casa e Pessoas")

conn = get_connection()

st.subheader("➕ Adicionar pessoa")

nome = st.text_input("Nome")
contribui = st.checkbox("Contribui com renda?")
renda = st.number_input("Renda mensal", min_value=0.0, disabled=not contribui)

if st.button("Adicionar pessoa"):
    conn.execute(
        "INSERT INTO pessoas (nome, contribui, renda) VALUES (?, ?, ?)",
        (nome, int(contribui), renda if contribui else 0)
    )
    conn.commit()
    st.success("Pessoa adicionada com sucesso!")

st.divider()

df = pd.read_sql("SELECT * FROM pessoas", conn)

st.subheader("✏️ Editar pessoas")

if not df.empty:
    pessoa_id = st.selectbox("Selecione a pessoa", df["id"])
    pessoa = df[df["id"] == pessoa_id].iloc[0]

    novo_nome = st.text_input("Nome", pessoa["nome"])
    novo_contribui = st.checkbox("Contribui com renda?", value=bool(pessoa["contribui"]))
    nova_renda = st.number_input(
        "Renda mensal",
        value=float(pessoa["renda"]),
        disabled=not novo_contribui
    )

    if st.button("Salvar alterações"):
        conn.execute("""
            UPDATE pessoas
            SET nome = ?, contribui = ?, renda = ?
            WHERE id = ?
        """, (
            novo_nome,
            int(novo_contribui),
            nova_renda if novo_contribui else 0,
            pessoa_id
        ))
        conn.commit()
        st.success("Dados atualizados!")
else:
    st.info("Nenhuma pessoa cadastrada ainda.")
