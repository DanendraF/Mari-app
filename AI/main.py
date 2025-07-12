from fastapi import FastAPI
from routes import chat, history
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

app.include_router(chat.router)
app.include_router(history.router) 