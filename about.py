import streamlit as st
from streamlit_chat import message

def app():
    st.title('Описание')
    st.markdown('---')
    st.markdown('Реализация чата с **LLM Chat GPT-3.5** и с **собственной базой знаний**. База знаний реализована на векторном хранилище QDRANT. '
            'У пользователя есть выбор к какому источнику обращаться.')
