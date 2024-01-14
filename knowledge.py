import streamlit as st
from langchain.text_splitter import CharacterTextSplitter
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Qdrant
import qdrant_client
#from langchain import HuggingFaceHub
#from langchain_community.embeddings import HuggingFaceEmbeddings
import os


def get_text(update_docs):
    text=""
    for doc in update_docs:
        raw_text = str(doc.read(), "utf-8")
        text+=raw_text
    return text

def get_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator='.',
        chunk_size=300,
        chunk_overlap=60,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks
def get_vector_store():

    client = qdrant_client.QdrantClient(
        st.secrets["QDRANT_HOST"],
        api_key=st.secrets["QDRANT_API_KEY"]
    )

    embeddings = OpenAIEmbeddings()
    #embeddings = SentenceTransformerEmbeddings(model_name="kev216/sentence-embedding-LaBSE")
    model_name = "kev216/sentence-embedding-LaBSE"
    #embeddings = HuggingFaceEmbeddings(model_name = model_name)
    vector_store = Qdrant(
        client=client,
        collection_name=st.secrets["QDRANT_COLLECTION_NAME"],
        embeddings=embeddings,
    )

    return vector_store

def app():
    st.title('База знаний')
    st.markdown('---')
    if not st.session_state.settings_isset:
        st.warning('Не заполнены настройки!')
    else:
        st.subheader('Обновить данные в хранилище')
        # collectionName = st.text_input('Укажите имя коллекции в БД:', help='укажите имя collection в БД')
        collectionName = st.secrets["QDRANT_COLLECTION_NAME"]
        create_new_collection = st.checkbox('перезаписать коллекцию', help='перезаписываеть коллекцию, если она уже существует')
        update_docs = st.file_uploader('Загрузите файлы и нажмите кнопку **Выполнить**', accept_multiple_files=True,type="txt")
        if st.button('Выполнить'):
            with st.container():
                st.write(collectionName)
                st.write('Перезаписать коллекцию:', create_new_collection)
                # create your client
                client = qdrant_client.QdrantClient(st.secrets["QDRANT_HOST"],
                                                    api_key=st.secrets["QDRANT_API_KEY"]
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
                    st.write('Коллекция перезаписана:', status_operation)

            text_in_docs = get_text(update_docs)

            text_chunks = get_chunks(text_in_docs)
            vectorstore = get_vector_store()
            vectorstore.add_texts(text_chunks)