import os
import shutil

from fastapi import (
    FastAPI,
    UploadFile,
    File,
    Form,
    HTTPException
)

from fastapi.responses import HTMLResponse

from chatbot_logic import (
    upload_document,
    ask_question
)

app = FastAPI(
    title="PDF RAG Chatbot"
)

os.makedirs(
    "uploads",
    exist_ok=True
)

@app.get("/", response_class=HTMLResponse)
def home():
    try:
        with open(
            "index.html",
            "r",
            encoding="utf-8"
        ) as file:
            return HTMLResponse(
                content=file.read()
            )

    except FileNotFoundError:
        return HTMLResponse(
            content="<h1>index.html not found</h1>",
            status_code=404
        )


@app.post("/upload")
async def upload_pdf(
    file: UploadFile = File(...)
):

    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="No file selected"
        )

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed"
        )

    try:
        file_path = f"uploads/{file.filename}"

        with open(
            file_path,
            "wb"
        ) as buffer:
            shutil.copyfileobj(
                file.file,
                buffer
            )

        message = upload_document(
            file_path
        )

        return {
            "message": message
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@app.post("/chat")
async def chat(
    question: str = Form(...)
):

    if not question.strip():
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty"
        )

    try:
        answer = ask_question(
            question
        )

        return {
            "answer": answer
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )