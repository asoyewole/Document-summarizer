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


Chat with Multiple PDFs
This project allows users to interactively chat with content extracted from multiple PDF documents using a conversational AI model. It uses OpenAI's GPT-based model for answering questions and retrieving relevant information from the uploaded PDFs. The interface is built using Streamlit, providing an intuitive and responsive user experience.

Features
Upload and process multiple PDF files.
Extract and split text into manageable chunks for efficient retrieval.
Create a vectorized index of the text using FAISS (Facebook AI Similarity Search).
Utilize a conversational memory to maintain context across chat interactions.
Generate dynamic responses using OpenAI’s GPT models.
Scrollable chat interface with styled bot and user messages.
Seamless and user-friendly UI with fixed input and header areas.
Project Architecture
The project is structured into the following main components:

PDF Processing: Reads and extracts text from uploaded PDFs using PyPDF2.
Text Chunking: Breaks down large text into smaller, overlapping chunks for optimal processing.
Vector Store Creation: Embeds the chunks into vector representations using OpenAI's embeddings and indexes them with FAISS.
Conversational Chain: Uses a retrieval-based system with OpenAI's chat model for answering user queries.
Streamlit UI: Provides an interactive and user-friendly interface to upload files, ask questions, and view responses.
Setup Instructions
Follow these steps to set up and run the project locally:

1. Clone the Repository
bash
Copy code
git clone https://github.com/yourusername/chat-with-multiple-pdfs.git
cd chat-with-multiple-pdfs
2. Create a Python Virtual Environment
bash
Copy code
python3 -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
3. Install Dependencies
Install all required Python packages listed in the requirements.txt file:

bash
Copy code
pip install -r requirements.txt
4. Set Up Environment Variables
Create a .env file in the project directory and add your OpenAI API Key:

makefile
Copy code
OPENAI_API_KEY=your_openai_api_key
5. Run the Application
Run the Streamlit application:

bash
Copy code
streamlit run app.py
6. Upload and Chat
Use the sidebar to upload multiple PDFs.
Click "Process" to extract and vectorize the content.
Type your questions in the input box, and the bot will respond with relevant answers.
File Structure
bash
Copy code
chat-with-multiple-pdfs/
│
├── app.py                     # Main application file
├── requirements.txt           # List of Python dependencies
├── .env                       # Environment variables
├── htmlTemplate.py            # Styled HTML templates for chat messages
├── README.md                  # Project documentation (this file)
└── utils/
    ├── pdf_processor.py       # Functions for extracting and chunking text
    ├── vector_store.py        # FAISS vector store creation and management
    ├── conversational_chain.py # Setup for conversation chain
    └── css.py                 # Custom CSS for UI styling
Key Steps to Understand the Project
PDF Upload and Processing:

Upload multiple PDF documents using the Streamlit sidebar.
Extract text from each file with PyPDF2.
Break down large text into smaller overlapping chunks to improve AI responses.
Vectorizing Text:

Use OpenAI embeddings to convert text chunks into vector representations.
Store the vectors in FAISS for efficient similarity search.
Conversational AI:

Employ OpenAI's GPT models to retrieve and respond with the most relevant information.
Maintain conversation context using a memory buffer.
UI Features:

A scrolling chat interface keeps the header and input box fixed.
Display styled bot and user messages with avatars for an intuitive experience.
Customization
Update Bot and User Avatars
Edit the bot_template and user_template in htmlTemplate.py to use custom avatar images.

Adjust Text Chunk Size
Modify the chunk_size and chunk_overlap values in the get_text_chunks function to change how text is divided.

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
