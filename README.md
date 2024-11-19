**Document Summarizer**  
This project allows users to interactively chat with content extracted from multiple PDF documents using a conversational AI model. It uses OpenAI's GPT-based model for answering questions and retrieving relevant information from the uploaded PDFs. The interface is built using Streamlit, providing an intuitive and responsive user experience.

![pdf summarizer flowchart](https://github.com/user-attachments/assets/de717e14-705e-4ba0-b5be-5d5f932d9e2b)

**Features**
1. Upload and process multiple PDF files.
2. Extract and split text into manageable chunks for efficient retrieval.
3. Create a vectorized index of the text using FAISS (Facebook AI Similarity Search).
4. Utilize a conversational memory to maintain context across chat interactions.
5. Generate dynamic responses using OpenAI’s GPT models.
6. Scrollable chat interface with styled bot and user messages.
7. Seamless and user-friendly UI with fixed input and header areas.

**Project Architecture**
The project is structured into the following main components:

**PDF Processing**: Reads and extracts text from uploaded PDFs using PyPDF2.
Text Chunking: Breaks down large text into smaller, overlapping chunks for optimal processing.
**Vector Store Creation**: Embeds the chunks into vector representations using OpenAI's embeddings and indexes them with FAISS.
**Conversational Chain**: Uses a retrieval-based system with OpenAI's chat model for answering user queries.
**Streamlit UI**: Provides an interactive and user-friendly interface to upload files, ask questions, and view responses.

**Example Use Case**
Upload Documents:
Upload financial reports, research papers, or business documents.
Ask Questions:
"What are the main points of this document?"
"Summarize the policies related to AI and ML."
Receive Contextual Responses:
Get precise answers tailored to the document content.

**Technologies Used**
Python: Core programming language.
Streamlit: For building the interactive web application.
OpenAI GPT API: For natural language processing and conversational responses.
FAISS: For efficient vector-based similarity search.
PyPDF2: For extracting text from PDF files.

**Future Improvements**
Add support for other file formats (e.g., Word documents).
Enable multi-user sessions with distinct memory states.
Improve chatbot responsiveness with additional tuning.
Provide a feature for saving and exporting chat history.
