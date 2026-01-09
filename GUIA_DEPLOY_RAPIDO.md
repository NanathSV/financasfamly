# 🚀 Guia de Implantação Rápida (Grátis e Permanente)

Siga estes passos para colocar o **Social Command Center** online em menos de 5 minutos.

## Passo 1: Preparar o GitHub
1. Acesse [github.com](https://github.com) e faça login.
2. Clique no botão **"New"** para criar um novo repositório.
3. Nomeie como `social-command-center` e deixe como **Public** ou **Private**.
4. Clique em **"Create repository"**.
5. No seu computador, extraia o arquivo ZIP que te enviei.
6. Faça o upload de todos os arquivos da pasta extraída para o seu repositório no GitHub.

## Passo 2: Publicar no Streamlit Cloud
1. Acesse [share.streamlit.io](https://share.streamlit.io).
2. Clique em **"Continue with GitHub"**.
3. Clique no botão azul **"Create app"**.
4. Clique em **"Yup, I have an app"**.
5. Preencha os campos:
   - **Repository**: Selecione `seu-usuario/social-command-center`.
   - **Main file path**: Digite `app.py`.
6. Clique em **"Deploy!"**.

## Passo 3: Configurar sua Chave de IA (Opcional)
Para que a análise automática funcione no site publicado:
1. No painel do Streamlit Cloud, vá em **Settings** > **Secrets**.
2. Você pode colar sua chave do Gemini lá ou simplesmente digitá-la na barra lateral do site sempre que usar.

---

## 📂 Arquivos incluídos no seu pacote:
- `app.py`: O coração da aplicação.
- `database.py`: Gerenciamento do banco de dados SQLite.
- `ai_engine.py`: Integração com a inteligência artificial.
- `requirements.txt`: Lista de bibliotecas que o servidor vai instalar automaticamente.
- `.streamlit/config.toml`: Configurações visuais do tema Dark Mode.
- `social_metrics.db`: Seu banco de dados inicial (já com dados de exemplo).

---
**Dica de Ouro:** O Streamlit Cloud é gratuito para sempre para apps comunitários. Seus dados ficarão salvos no arquivo `.db` dentro do servidor!
