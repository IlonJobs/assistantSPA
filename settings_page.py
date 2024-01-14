import streamlit as st

def app():
    st.title('Settings page')
    st.markdown('---')
    st.checkbox('Использовать настройки по умолчанию',value=st.session_state.default_settings,on_change=set_default_settings)
    qdrant_settings = st.container()
    openai_settings = st.container()

    with qdrant_settings:
        st.header('Qdrant')
        st.session_state.QDRANT_HOST = st.text_input('Укажите имя хоста Qdrant:', help='укажите имя хоста')
        st.session_state.QDRANT_COLLECTION_NAME = st.text_input('Укажите имя коллекции в БД:', help='укажите имя collection в БД')
        st.session_state.QDRANT_API_KEY = st.text_input('API Qdrant:', help='укажите ключ Qdrant')

    with openai_settings:
        st.header('OpenAI')
        st.session_state.OPENAI_API_KEY = st.text_input('API OpenAI:', help='укажите ключ API')


def set_default_settings():
    st.session_state.default_settings = not st.session_state.default_settings
    change_settings()
def change_settings():
    if st.session_state.default_settings:
        st.session_state.OpenAI_API = st.secrets['OPENAI_API_KEY']
        st.session_state.Qdrant_API = st.secrets['QDRANT_API_KEY']
        st.session_state.Qdrant_host = st.secrets['QDRANT_HOST']
        st.session_state.Qdrant_collection = st.secrets['QDRANT_COLLECTION_NAME']
        st.session_state.settings_isset = True
    else:
        st.session_state.OpenAI_API = st.session_state.OPENAI_API_KEY
        st.session_state.Qdrant_API = st.session_state.QDRANT_API_KEY
        st.session_state.Qdrant_host = st.session_state.QDRANT_HOST
        st.session_state.Qdrant_collection = st.session_state.QDRANT_COLLECTION_NAME
        if st.session_state.OpenAI_API and st.session_state.Qdrant_API and st.session_state.Qdrant_host and st.session_state.Qdrant_collection:
            st.session_state.settings_isset = True
        else:
            st.session_state.settings_isset = False

