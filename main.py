import os
import shutil

from fastapi import FastAPI
from fastapi import UploadFile
from fastapi import File
from fastapi import Form

from fastapi.responses import HTMLResponse

from chatbot_logic import (
    upload_document,
    ask_question
)

app = FastAPI()

os.makedirs(
    "uploads",
    exist_ok=True
)


@app.get("/", response_class=HTMLResponse)
def home():

    with open(
        "index.html",
        "r",
        encoding="utf-8"
    ) as file:

        return HTMLResponse(
            content=file.read()
        )


@app.post("/upload")
async def upload_pdf(
    file: UploadFile = File(...)
):

    file_path = f"uploads/{file.filename}"

    with open(
        file_path,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    upload_document(file_path)

    return {
        "message": "PDF Uploaded Successfully"
    }


@app.post("/chat")
async def chat(
    question: str = Form(...)
):

    answer = ask_question(
        question
    )

    return {
        "answer": answer
    }