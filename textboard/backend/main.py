from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

messages = []

class Message(BaseModel):
    text: str

@app.get("/")
def health():
    return {"status": "ok"}

@app.get("/messages")
def get_messages():
    return messages

@app.post("/messages")
def post_message(msg: Message):
    messages.append(msg.text)
    return {"message": msg.text}
