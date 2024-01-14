import streamlit as st
import pandas as pd
# from pandasai import PandasAI
# from pandasai.llm.openai import OpenAI




def app():
    st.title('Read excel file')
    st.markdown('---')
    if not st.session_state.settings_isset:
        st.warning('Не заполнены настройки!')
    else:
        st.write("Временно отключено!")
        # uploaded_file = st.file_uploader('Загрузите файлы и нажмите кнопку **Прочитать файлы**',type="xlsx")
        # if st.button('Прочитать файлы'):
        #     if uploaded_file is not None:
        #         if "xlsl_files" not in st.session_state:
        #             st.session_state.xlsl_files = []
        #         xls = pd.ExcelFile(uploaded_file)
        #         sheet_names = xls.sheet_names
        #     with st.expander("Данные из файла"):
        #         tabs = st.tabs(sheet_names)
        #         for n in range(len(sheet_names)):
        #             with tabs[n]:
        #                 df = pd.read_excel(uploaded_file,sheet_name=sheet_names[n])
        #                 st.session_state.xlsl_files.append(df)
        #                 st.write(df)
        # st.session_state.user_prompt = st.text_area('Ваш запрос',)
        # if st.button('Выполнить',disabled=st.session_state.settings_isset):
        #     llm = OpenAI(model_name='gpt-3.5-turbo',api_token=st.secrets["OPENAI_API_KEY"])
        #     pandas_ai = PandasAI(llm)
        #     with st.spinner('Формулирую ответ...'):
        #         response = pandas_ai.run(st.session_state.xlsl_files[0], prompt = st.session_state.user_prompt)
        #         st.write(response)