from fastapi import APIRouter, HTTPException
from services.history_service import get_history, get_history_detail

router = APIRouter()

@router.get("/history/{user_id}")
def history_list(user_id: str):
    return get_history(user_id)

@router.get("/history/detail/{chat_id}")
def history_detail(chat_id: int):
    result = get_history_detail(chat_id)
    if result:
        return result
    raise HTTPException(404, "Chat tidak ditemukan") 