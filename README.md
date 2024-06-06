# FileChat App

FileChat is a Streamlit-based application that allows users to chat with their files. It extracts text from uploaded PDF or Excel files, enables users to ask questions about the content of those files, and provides conversational responses based on the extracted text.

## Prerequisites

Before running the application, ensure you have the following dependencies installed:

- Python (version 3.6 or higher)
- Streamlit
- PyPDF2
- langchain (and its dependencies)
- google (for Google Generative AI)
- streamlit-extras
- faiss-cpu (for FAISS vector database)

You can install the dependencies using pip:

```bash
pip install streamlit PyPDF2 langchain streamlit-extras faiss-cpu
```

Additionally, you'll need to have a Google API key for Google Generative AI. Set the `GOOGLE_API_KEY` environment variable with your API key.

## How to Run

To run the application, execute the following command in your terminal:

```bash
streamlit run app.py
```

This will start the Streamlit server, and you can access the FileChat app in your web browser.

## Features

- **File Upload**: Users can upload PDF or Excel files containing text.
- **Text Extraction**: The application extracts text from the uploaded files using PyPDF2.
- **Text Splitting**: The extracted text is split into chunks using RecursiveCharacterTextSplitter from langchain.
- **Text Embedding**: The chunks of text are embedded using Google Generative AI Embeddings.
- **Vector Database (FAISS)**: The embedded text chunks are stored in a FAISS vector database for efficient similarity search.
- **Conversational AI**: Users can ask questions about the content of the files, and the application provides conversational responses based on the embedded text.
- **User Interface**: The app has a user-friendly interface built with Streamlit, featuring a sidebar for file upload and a main section for user interaction.

## Customization

You can customize the application by modifying the following:

- **Embedding Models**: You can change the embedding models used for text embedding by modifying the `model` parameter in the `GoogleGenerativeAIEmbeddings` and `ChatGoogleGenerativeAI` instances.
- **Text Splitting Parameters**: Adjust the parameters of `RecursiveCharacterTextSplitter` for text splitting, such as `chunk_size` and `chunk_overlap`.
- **Vector Database**: The application uses FAISS for storing and retrieving embedded text chunks. You can configure FAISS settings based on your requirements.
- **UI Elements**: Customize the UI elements, such as header text, input fields, and button labels, to match your preferences.

## About the Author

This FileChat app was made by [Temidayo Oyewo](https://x.com/oyewodayo) for educational and demonstration purposes.

## License

This project is licensed under the [MIT License](LICENSE).
