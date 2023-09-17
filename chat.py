import streamlit as st
from streamlit_chat import message
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
import knowledge
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)





def main():

    st.header('Chat with')
    sources = ["Chat GPT", "База знаний"]
    st.session_state.DataSource = st.selectbox(" ", sources)
    st.markdown('---')
    if st.session_state.DataSource == 'Chat GPT':
        chatAI = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')
    elif st.session_state.DataSource == 'База знаний':
        template = """
        Use the following context (delimited by <ctx></ctx>) and the chat history (delimited by <hs></hs>) to answer the question.
        If you don't know the answer, just say 'Извините, ответ не найден.', don't try to make up an answer:
        ------
        <ctx>
        {context}
        </ctx>
        ------
        <hs>
        {history}
        </hs>
        ------
        {question}
        Answer:
        """
        PROMPT = PromptTemplate(
            template=template, input_variables=["history", "context", "question"])
        llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')
        memory = ConversationBufferWindowMemory(memory_key="history", input_key="question", k=2)
        chain_type_kwargs = {"verbose": False, "prompt": PROMPT, "memory": memory}
        vectorstore = knowledge.get_vector_store()
        qa = RetrievalQA.from_chain_type(
            llm=llm,
            return_source_documents=True,
            chain_type="stuff",
            chain_type_kwargs=chain_type_kwargs,
            retriever=vectorstore.as_retriever(search_kwargs={"k": 20})
        )
    chat_container = st.container()

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
        st.session_state.messages.append(HumanMessage(content=user_question))

        with st.spinner('Формулирую ответ...'):
            if st.session_state.DataSource == 'Chat GPT':
                response = chatAI(st.session_state.messages)
                answer_ai = response.content
            elif st.session_state.DataSource == 'База знаний':
                response = qa({"query": user_question})
                answer_ai = response['result']
        with chat_container: message(answer_ai,allow_html=True)
        # Add assistant response to chat history
        st.session_state.messages.append(AIMessage(content=answer_ai))

if __name__ == '__main__':
    main()


