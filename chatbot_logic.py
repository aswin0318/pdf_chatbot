import os

from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

from langchain_aws import ChatBedrock
from langchain_aws import BedrockEmbeddings

from langchain_core.output_parsers import StrOutputParser

load_dotenv()

embedding_model = BedrockEmbeddings(
    model_id="amazon.titan-embed-text-v2:0"
)

llm = ChatBedrock(
    model_id="amazon.nova-lite-v1:0",
    model_kwargs={
        "temperature": 0.3,
        "maxTokens": 256
    }
)

parser = StrOutputParser()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

vector_store = None

chat_history = []


def load_or_create_vector_store():

    global vector_store

    if (
        os.path.exists("./chroma_db")
        and os.listdir("./chroma_db")
    ):
        print("Loading existing ChromaDB...")

        vector_store = Chroma(
            persist_directory="./chroma_db",
            embedding_function=embedding_model
        )

    return vector_store


def upload_document(file_path):

    global vector_store

    print("Loading PDF...")

    loader = PyPDFLoader(file_path)

    documents = loader.load()

    print(f"Pages Loaded: {len(documents)}")

    print("Splitting Documents...")

    chunks = splitter.split_documents(
        documents
    )

    print(f"Chunks Created: {len(chunks)}")

    print("Creating ChromaDB...")

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory="./chroma_db"
    )

    print("Vector Store Created Successfully")

    return "Document Uploaded Successfully"


def format_chat_history():

    if not chat_history:
        return "No previous conversation."

    history_text = ""

    for item in chat_history[-5:]:

        history_text += (
            f"User: {item['question']}\n"
            f"Assistant: {item['answer']}\n\n"
        )

    return history_text


def ask_question(query):

    global vector_store

    if vector_store is None:
        vector_store = load_or_create_vector_store()

    if vector_store is None:
        return "Please upload a document first."

    print(f"Question: {query}")

    docs = vector_store.similarity_search(
        query,
        k=4
    )

    print(f"Retrieved Chunks: {len(docs)}")

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    history = format_chat_history()

    prompt = f"""
You are a helpful assistant.

Use the provided context and previous conversation
to answer the user's question.

Previous Conversation:
{history}

Context:
{context}

Question:
{query}
"""

    chain = llm | parser

    answer = chain.invoke(prompt)

    chat_history.append(
        {
            "question": query,
            "answer": answer
        }
    )

    return answer