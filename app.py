import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter


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
    st.write('Made by [Temidayo Oyewo](https://x.com/oyewoday)')

def main():
    st.header("Chat with your file")
    uploaded_pdf = st.file_uploader("Upload your file", type='pdf')

   
    if uploaded_pdf is not None:
        pdf_reader = PdfReader(uploaded_pdf)

        # num_pages = len(pdf_reader.pages)
        # st.write(f"Uploaded file: {uploaded_pdf.name}")
        # st.write(f"The PDF file has {num_pages} pages.")
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        chunks = text_splitter.split_text(text=text)
        st.write(chunks)

if __name__ == '__main__':
    main()