import streamlit as st

def app():
    st.header('Settings page')
    st.markdown('---')
    st.markdown('>**OpenAI**')
    st.markdown('---')
    st.markdown('>**Qdrant**')
    st.text_input('Укажите имя хоста Qdrant:', help='укажите имя хоста')
    st.text_input('Укажите имя коллекции в БД:', help='укажите имя collection в БД')
    st.text_input('API Qdrant:', help='укажите ключ API')
    st.markdown('---')
