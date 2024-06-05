import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space

# sidebar content
with st.sidebar:
    st.title('File chat app')
    st.markdown('''
    ## About
    This app is an LLM-powered chatbot built using:
    - [Streamlit](https://streamlit.io/)
    - [LangChain](https://python.langchain.com/)
    - [OpenAI](https://platform.openai.com/docs/models) LLM model
    ''')
    add_vertical_space(5)
    st.write('Made by [Temidayo Oyewo](https://x.xom/oyewoday)')