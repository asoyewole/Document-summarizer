import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_community.chat_models import ChatOpenAI
from htmlTemplate import css, bot_template, user_template
from langchain_community.llms import huggingface_hub
from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")


def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text


def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    text_chunks = text_splitter.split_text(text)
    text_chunks = [summarizer(chunk, max_length=150, min_length=40, do_sample=False)[
        0]['summary_text'] for chunk in text_chunks]
    return text_chunks


def get_vector_store(text_chunks):
    embeddings = HuggingFaceInstructEmbeddings(
        model_name='hkunlp/instructor-xl')
    # Create the database of vectors
    vector_store = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vector_store


def get_conversation_chain(vector_store):
    llm = huggingface_hub.HuggingFaceHub(
        repo_id="google/flan-t5-large",
        model_kwargs={"temperature": 0.5, "max_length": 512})
    memory = ConversationBufferMemory(memory_key='chat_history',
                                      return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vector_store.as_retriever(),
        memory=memory
    )
    return conversation_chain


def handle_user_input(user_question):
    load_dotenv()
    prompt = f"Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up answers.\n\n"
    context = "\n\n".join(
        [chunk for chunk in st.session_state.text_chunks if len(chunk.strip()) > 0])
    prompt += context + "\n\nQuestion: " + user_question + "\nHelpful Answer:"

    response = st.session_state.conversation({'question': prompt})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)


def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with Multiple PDF",
                       page_icon=":books:")

    st.write(css, unsafe_allow_html=True)
    if 'conversation' not in st.session_state:
        st.session_state.conversation = None

    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = None

    st.header("Chat with Multiple PDF :books:")
    user_question = st.text_input("Ask a question from your documents:")
    if user_question:
        handle_user_input(user_question)

    with st.sidebar:
        st.subheader("Your Documents")
        pdf_docs = st.file_uploader(
            'Upload your PDFs here and click "Process"', accept_multiple_files=True)
        if st.button('Process'):
            with st.spinner("Processing"):
                # get pdf text
                raw_text = get_pdf_text(pdf_docs)

                # Get the text chunks
                text_chunks = get_text_chunks(raw_text)
                st.session_state.text_chunks = text_chunks

                # create vector store using embeddings
                vector_store = get_vector_store(text_chunks)

                # Create conversation chain
                st.session_state.conversation = get_conversation_chain(
                    vector_store)


if __name__ == '__main__':
    main()
