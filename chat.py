import streamlit as st
from streamlit_chat import message


import pandas as pd
import numpy as np

from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)


def main():

    st.header('Chat with GPT')
    st.markdown('---')





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
        st.session_state.messages.append(HumanMessage(content=user_question))
        with st.spinner('Формулирую ответ...'):
            response = chatAI(st.session_state.messages)

        with chat_container: message(response.content,allow_html=True)
        # Add assistant response to chat history
        st.session_state.messages.append(AIMessage(content=response.content))

if __name__ == '__main__':
    main()


