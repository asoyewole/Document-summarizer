import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmlTemplate import css, bot_template, user_template


# Function to extract text from PDF files
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        try:
            pdf_reader = PdfReader(pdf)
            for page in pdf_reader.pages:
                page_text = page.extract_text()
                if page_text:  # Ensure text exists
                    text += page_text
        except Exception as e:
            st.error(f"Error reading {pdf.name}: {e}")
    return text


# Function to split text into smaller chunks
def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks


# Function to create a vector store from text chunks
def get_vector_store(text_chunks):
    try:
        embeddings = OpenAIEmbeddings()
        vector_store = FAISS.from_texts(
            texts=text_chunks, embedding=embeddings)
        return vector_store
    except Exception as e:
        st.error(f"Error creating vector store: {e}")
        return None


# Function to create a conversational retrieval chain
def get_conversation_chain(vector_store):
    try:
        llm = ChatOpenAI(model="gpt-4o", temperature=0.5)
        memory = ConversationBufferMemory(
            memory_key='chat_history', return_messages=True)
        conversation_chain = ConversationalRetrievalChain.from_llm(
            llm=llm,
            retriever=vector_store.as_retriever(),
            memory=memory
        )
        return conversation_chain
    except Exception as e:
        st.error(f"Error initializing conversation chain: {e}")
        raise


# Function to handle user input and display conversation
def handle_user_input(user_question):
    try:
        if not st.session_state.conversation:
            st.warning("Please upload and process documents first.")
            return

        response = st.session_state.conversation({'question': user_question})
        st.session_state.chat_history = response['chat_history']

        # Display chat history
        for i, message in enumerate(st.session_state.chat_history):
            if i == 0:
                st.markdown('<div class="chat-container">',
                            unsafe_allow_html=True)
            if i % 2 == 0:
                st.write(user_template.replace(
                    "{{MSG}}", message.content), unsafe_allow_html=True)
            else:
                st.write(bot_template.replace(
                    "{{MSG}}", message.content), unsafe_allow_html=True)

            if i == len(st.session_state.chat_history) - 1:
                st.markdown('</div>', unsafe_allow_html=True)
    except Exception as e:
        st.error(f"error handling user input: {e}")


# Main application
def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with Multiple PDFs",
                       page_icon=":books:")

    st.write(css, unsafe_allow_html=True)

    # Initialize Streamlit session state variables
    if 'conversation' not in st.session_state:
        st.session_state.conversation = None

    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = None

    # Header
    st.header("Chat with Multiple PDFs :books:")
    user_question = st.text_input("Ask a question from your documents:")
    if user_question:
        handle_user_input(user_question)

    # Sidebar for uploading and processing PDFs
    with st.sidebar:
        st.subheader("Your Documents")
        pdf_docs = st.file_uploader(
            'Upload your PDFs here and click "Process"', accept_multiple_files=True, type=["pdf"])
        if st.button('Process'):
            if pdf_docs:
                with st.spinner("Processing..."):
                    # Extract text from uploaded PDFs
                    raw_text = get_pdf_text(pdf_docs)

                    # Split text into chunks
                    text_chunks = get_text_chunks(raw_text)

                    # Create vector store
                    vector_store = get_vector_store(text_chunks)
                    if vector_store:
                        # Initialize conversation chain
                        st.session_state.conversation = get_conversation_chain(
                            vector_store)
            else:
                st.warning("Please upload at least one PDF file.")


if __name__ == '__main__':
    main()
