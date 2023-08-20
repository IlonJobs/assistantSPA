import streamlit as st
from streamlit_chat import message
from langchain.vectorstores import Qdrant
import qdrant_client
import pandas as pd
import numpy as np
import os
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)


def main():
    st.set_page_config(page_title="Help assistant")

    st.title('Help assistant.')

    # Добавление элементов в боковую панель
    with st.sidebar:
        st.subheader('Обновить данные в хранилище')
        collectionName = st.text_input('Collection name:',help='enter a collection name to add your data')
        create_new_collection = st.checkbox('rewrite collection',help='rewrite collection if it exist')
        update_docs = st.file_uploader('Upload your files and click Process button',accept_multiple_files=True)
        if st.button('Process'):
            with st.container():
                st.write(collectionName)
                st.write('Create a new collection:',create_new_collection)
                # create your client
                client = qdrant_client.QdrantClient(st.secrets["QDRANT_HOST"],
                                                    api_key = st.secrets["QDRANT_API_KEY"]
                    )
                if create_new_collection:
                    # !!!!create collection!!!!!
                    collection_config = qdrant_client.http.models.VectorParams(
                        size=1536,  # 768 for instructor-xl, 1536 for OpenAI
                        distance=qdrant_client.http.models.Distance.COSINE
                    )

                    status_operation = client.recreate_collection(
                        collection_name=collectionName,
                        vectors_config=collection_config
                    )
                    st.write('Status:',status_operation)

    chat_container = st.container()

    chatAI = ChatOpenAI(temperature=0,model_name='gpt-3.5-turbo')

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = [SystemMessage(content='you are a polite assistant.')]

    # Display chat messages from history on app rerun
    for mes in st.session_state.messages:
        if mes.type=='human':
            with chat_container: message(mes.content, is_user=True,allow_html=True)
        elif mes.type=='ai':
            with chat_container: message(mes.content,allow_html=True)

    # React to user input
    if user_question := st.chat_input("Напишите Ваш вопрос..."):

        with chat_container: message(user_question, is_user=True)  # align's the message to the right
        # Add user message to chat history
        # st.session_state.messages.append({"role": "user", "content": prompt})
        st.session_state.messages.append(HumanMessage(content=user_question))
        with st.spinner('Формулирую ответ...'):
            response = chatAI(st.session_state.messages)

        with chat_container: message(response.content,allow_html=True)
        # Add assistant response to chat history
        # st.session_state.messages.append({"role": "assistant", "content": response})
        st.session_state.messages.append(AIMessage(content=response.content))
        # st.write(st.session_state.messages[1].type)
if __name__ == '__main__':
    main()


