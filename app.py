import streamlit as st
from streamlit_chat import message
import pandas as pd
import numpy as np

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    st.set_page_config(page_title="Help assistant")
    st.header('Help assistant header')

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for mes in st.session_state.messages:
        if mes["role"]=='assistant':
            message(mes["content"])
        elif mes["role"]=='user':
            message(mes["content"], is_user=True)


    # React to user input
    if prompt := st.chat_input("What is up?"):

        message(prompt, is_user=True)  # align's the message to the right
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        response = f"Echo: {prompt}"
        message(response)  # align's the message to the right
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == '__main__':
    main()


