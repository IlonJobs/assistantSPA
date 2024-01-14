import streamlit as st
from streamlit_option_menu import option_menu
import settings_page, chat,about,knowledge,read_excel

st.set_page_config(layout='wide')

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
                options=['Описание', 'Чат','База знаний','Анализ файла','Настройки' ],
                icons=['house-fill', 'chat-fill', 'book','filetype-xlsx', 'person-circle'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px",
                                 "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"}, }

            )

        if "settings_isset" not in st.session_state:
            st.session_state.settings_isset = False
        if "default_settings" not in st.session_state:
            st.session_state.default_settings = False
        if app == "Описание":
            about.app()
        if app == "База знаний":
            knowledge.app()
        if app == "Анализ файла":
            read_excel.app()
        if app == "Чат":
            chat.main()
        if app == "Настройки":
            settings_page.app()


    run()
