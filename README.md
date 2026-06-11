# PDF RAG Chatbot using LangChain, FastAPI, ChromaDB, and LLMs

## Overview

This project demonstrates a simple Retrieval-Augmented Generation (RAG) application built using LangChain.

Users can:

* Upload a PDF document
* Ask questions about the document
* Retrieve relevant content using semantic search
* Generate answers using a Large Language Model (LLM)

The application is intentionally kept simple to help understand the core concepts behind RAG systems.

---

# Architecture

```text
PDF
 ↓
Document Loader
 ↓
Text Splitter
 ↓
Embeddings
 ↓
ChromaDB
 ↓
Retriever
 ↓
Prompt
 ↓
LLM
 ↓
Response
```

---

# Technologies Used

## Backend

* FastAPI
* LangChain
* ChromaDB

## Document Processing

* PyPDFLoader
* RecursiveCharacterTextSplitter

## Vector Database

* ChromaDB

## Embedding Models

Examples:

```text
amazon.titan-embed-text-v2:0
sentence-transformers/all-MiniLM-L6-v2
nomic-embed-text
```

## Large Language Models

Examples:

```text
amazon.nova-lite-v1:0
TinyLlama/TinyLlama-1.1B-Chat-v1.0
microsoft/Phi-3-mini-4k-instruct
llama3.2
mistral
```

---

# Project Structure

```text
pdf_chatbot/

│
├── main.py
├── chatbot_logic.py
├── index.html
├── requirements.txt
├── README.md
│
├── uploads/
│
└── chroma_db/
```

---

# Features

* PDF Upload
* Document Loading
* Text Chunking
* Embedding Generation
* Chroma Vector Database
* Similarity Search
* Context Retrieval
* Conversational Question Answering
* Chat History Support
* Bedrock Support
* Hugging Face Support
* Ollama Support

---

# RAG Workflow

## Step 1: Upload PDF

The user uploads a PDF document through the web interface.

---

## Step 2: Document Loader

```python
PyPDFLoader
```

Loads PDF pages into LangChain Document objects.

Example:

```text
Page 1 → Document
Page 2 → Document
Page 3 → Document
```

---

## Step 3: Text Splitting

```python
RecursiveCharacterTextSplitter
```

Large documents are split into smaller chunks.

Configuration:

```python
chunk_size = 1000
chunk_overlap = 200
```

Example:

```text
Document
 ↓
Chunk 1
Chunk 2
Chunk 3
Chunk 4
```

---

## Step 4: Generate Embeddings

Each chunk is converted into vector representations.

Example:

```text
Chunk
 ↓
[0.25, -0.84, 0.11, ...]
```

Embedding models:

### Amazon Bedrock

```text
amazon.titan-embed-text-v2:0
```

### Hugging Face

```text
sentence-transformers/all-MiniLM-L6-v2
```

### Ollama

```text
nomic-embed-text
```

---

## Step 5: Store in ChromaDB

```python
Chroma
```

Stores vectors for semantic retrieval.

Example:

```text
Vector
 ↓
ChromaDB
```

---

## Step 6: Retrieve Relevant Chunks

```python
similarity_search()
```

User Question:

```text
Where is Arun from?
```

Retriever searches the vector database and returns the most relevant chunks.

Example:

```text
Chunk:
Arun Simon is from Thodupuzha.
```

---

## Step 7: Generate Response

The retrieved chunks are injected into the prompt.

Example:

```text
Context:
Arun Simon is from Thodupuzha.

Question:
Where is Arun from?
```

The LLM uses this context to generate the answer.

---

# Supported Model Providers

The RAG pipeline remains exactly the same.

Only the Embedding Model and LLM change.

---

# Option 1: Amazon Bedrock

## Embedding Model

```text
amazon.titan-embed-text-v2:0
```

## LLM

```text
amazon.nova-lite-v1:0
```

## LangChain Integration

```python
from langchain_aws import ChatBedrock
from langchain_aws import BedrockEmbeddings
```

## Advantages

* Managed by AWS
* Production Ready
* IAM Integration
* No Infrastructure Management

---

# Option 2: Hugging Face Inference API

## Embedding Model

```text
sentence-transformers/all-MiniLM-L6-v2
```

## LLM

```text
TinyLlama/TinyLlama-1.1B-Chat-v1.0
```

Alternative:

```text
microsoft/Phi-3-mini-4k-instruct
```

## LangChain Integration

```python
from langchain_huggingface import HuggingFaceEndpoint
from langchain_huggingface import HuggingFaceEndpointEmbeddings
```

## Advantages

* Easy Setup
* API Based
* No GPU Required
* Ideal for Demos

## Requirements

```text
HF_API_KEY
```

---

# Option 3: Ollama (Self Hosted)

## Embedding Model

```text
nomic-embed-text
```

## LLM

```text
llama3.2
```

Alternatives:

```text
mistral
qwen3
gemma3
```

## LangChain Integration

```python
from langchain_ollama import ChatOllama
from langchain_ollama import OllamaEmbeddings
```

## Advantages

* Fully Local
* No API Costs
* Offline Usage
* Better Privacy

## Install Ollama

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Pull Models:

```bash
ollama pull llama3.2

ollama pull nomic-embed-text
```

Start Ollama:

```bash
ollama serve
```

---

# Installation

Create Virtual Environment:

```bash
python3 -m venv venv
```

Activate Environment:

## Linux

```bash
source venv/bin/activate
```

## Windows

```bash
venv\Scripts\activate
```

Install Dependencies:

```bash
pip install -r requirements.txt
```

---

# AWS Bedrock Setup

## IAM Permissions

```json
{
  "Effect": "Allow",
  "Action": [
    "bedrock:InvokeModel",
    "bedrock:InvokeModelWithResponseStream"
  ],
  "Resource": "*"
}
```

Attach the role to the EC2 instance.

---

## Enable Models

Enable access to:

```text
amazon.titan-embed-text-v2:0

amazon.nova-lite-v1:0
```

from the Bedrock Console.

---

# Running the Application

Start FastAPI:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

Open:

```text
http://localhost:8000
```

or

```text
http://<EC2-PUBLIC-IP>:8000
```

---

# API Endpoints

## Upload PDF

```http
POST /upload
```

Form Data:

```text
file
```

Response:

```json
{
  "message": "Document Uploaded Successfully"
}
```

---

## Ask Question

```http
POST /chat
```

Form Data:

```text
question
```

Response:

```json
{
  "answer": "Generated response"
}
```


---

# Learning Objectives

This project demonstrates the core components of a Retrieval-Augmented Generation system.

* Document Loaders
* Text Splitters
* Embeddings
* Vector Databases
* Similarity Search
* Retrieval
* Prompt Construction
* Large Language Models
* FastAPI Integration
* LangChain Pipelines

---

# Key Takeaway

RAG is model-agnostic.

The workflow remains:

```text
Loader
 ↓
Splitter
 ↓
Embeddings
 ↓
Vector Database
 ↓
Retriever
 ↓
Prompt
 ↓
LLM
 ↓
Response
```

Whether you use:

* Amazon Bedrock
* Hugging Face
* Ollama
* OpenAI
* Anthropic

the RAG architecture remains fundamentally the same.
