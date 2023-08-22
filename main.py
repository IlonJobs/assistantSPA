import streamlit as st
from streamlit_option_menu import option_menu
import settings_page, chat,about,knowledge

st.set_page_config(page_title="Help assistant")

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        with st.sidebar:
            app = option_menu(
                menu_title='Navigation ',
                options=['About', 'Chat','Knowledge base','Settings' ],
                icons=['house-fill', 'chat-fill', 'book', 'person-circle'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px",
                                 "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"}, }

            )

        if app == "About":
            about.app()
        if app == "Knowledge base":
            knowledge.app()
        if app == "Chat":
            chat.main()
        if app == "Settings":
            settings_page.app()


    run()
