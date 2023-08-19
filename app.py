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

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    st.set_page_config(page_title="Help assistant")
    st.title('title')
    st.header('Help assistant.')

    # Включение автоматической прокрутки
    st.markdown("""
        <style>
            .message {
                overflow-y: scroll !important;
                max-height: 400px;
            }
        </style>
    """, unsafe_allow_html=True)

    chat = ChatOpenAI(model_name='gpt-3.5-turbo',
                      temperature=0)

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = [SystemMessage(content='you are a polite assistant.')]

    # Display chat messages from history on app rerun
    for mes in st.session_state.messages:
        if mes.type=='human':
            message(mes.content, is_user=True,allow_html=True)
        elif mes.type=='ai':
            message(mes.content,allow_html=True)


    # React to user input
    if user_question := st.chat_input("What is up?"):

        message(user_question, is_user=True)  # align's the message to the right
        # Add user message to chat history
        # st.session_state.messages.append({"role": "user", "content": prompt})
        st.session_state.messages.append(HumanMessage(content=user_question))
        with st.spinner('Thinking...'):
            response = chat(st.session_state.messages)

        message(response.content,allow_html=True)  # align's the message to the right
        # Add assistant response to chat history
        # st.session_state.messages.append({"role": "assistant", "content": response})
        st.session_state.messages.append(AIMessage(content=response.content))
        # st.write(st.session_state.messages[1].type)
if __name__ == '__main__':
    main()


