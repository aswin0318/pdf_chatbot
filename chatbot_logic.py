import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

from langchain_huggingface import HuggingFaceEndpoint
from langchain_huggingface import HuggingFaceEndpointEmbeddings

from dotenv import load_dotenv
load_dotenv()

HF_API_KEY = os.getenv("HF_API_KEY")

embedding_model = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2",
    huggingfacehub_api_token=HF_API_KEY
)

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    huggingfacehub_api_token=HF_API_KEY,
    task="text-generation",
    max_new_tokens=256,
    temperature=0.3
)

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

vector_store = None

chat_history = []


def upload_document(file_path):

    global vector_store

    loader = PyPDFLoader(file_path)

    documents = loader.load()

    chunks = splitter.split_documents(
        documents
    )

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory="./chroma_db"
    )

    return "Document Uploaded"


def ask_question(query):

    global vector_store

    docs = vector_store.similarity_search(
        query,
        k=4
    )

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    prompt = f"""
Answer the question only from the provided context.

Context:
{context}

Question:
{query}

Answer:
"""

    answer = llm.invoke(prompt)

    chat_history.append(
        {
            "question": query,
            "answer": answer
        }
    )

    return answer