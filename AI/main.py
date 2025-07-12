from fastapi import FastAPI
from routes import chat, history
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

app.include_router(chat.router)
app.include_router(history.router)

@app.get("/")
def read_root():
    print("GROQ_API_KEY dari main.py:", os.getenv("GROQ_API_KEY"))
    return {"message": "API aktif"} 