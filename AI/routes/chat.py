from fastapi import APIRouter
from models.schemas import ChatRequest, ChatResponse
from services.chat_service import process_chat

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
def chat_endpoint(req: ChatRequest):
    return process_chat(req) 