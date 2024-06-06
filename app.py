import streamlit as st
from dotenv import load_dotenv
import pickle
from streamlit_extras.add_vertical_space import add_vertical_space
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
from langchain.vectorstores import FAISS
import os



# sidebar content
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text +=page.extract_text()
    return text

def get_text_chuncks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000,chunk_overlap= 1000)
    chuncks = text_splitter.split_text(text)
    return chuncks

def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    try:
        vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    except Exception as e:
        print("Error embedding content:", e)
        raise  # Re-raise the exception to halt execution
    vector_store.save_local("faiss_index")


def get_conversational_chain():
    prompt_templates = """
    Answer the questions as detailed as possible from the provided context, make sure to provide all the details,
    if the answer is not in the provided context just say, "Answer is not is available in the context", 
    don't provide the wrong answer
    Context:\n {context}?\n
    Question:\n{question}\n

    Answer: 
    """

    model = ChatGoogleGenerativeAI(model="models/embedding-001",temperature=0.3)

    prompt = PromptTemplate(template=prompt_templates, input_variables=["context","question"])
    chain = load_qa_chain(model, chain_type="stuff",prompt=prompt)
    return chain

def user_input(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")

    new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    docs = new_db.similarity_search(user_question)

    chain = get_conversational_chain()

    response = chain(
        {"input_documents":docs, "question":user_question},
        return_only_outputs=True
    )
    print(response)
    st.write("Reply: ", response["output_text"])



def main():
    st.header("Chat with your file")

    user_question = st.text_input("Ask a qestion from your Files")

    if user_question:
        user_input(user_question)
   
    with st.sidebar:
        st.title('File chat app')
        pdf_docs = st.file_uploader("Upload your PDF or Excel files and click on Submit to process",accept_multiple_files = True)

        if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                raw_text = generate_pdf_text(pdf_docs)
                text_chuncks = get_text_chuncks(raw_text)
                get_vector_store(text_chuncks)
                st.success("Done")

if __name__ == '__main__':
    main()