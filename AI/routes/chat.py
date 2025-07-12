from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
import os
import httpx

router = APIRouter()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

@router.post("/chat")
async def chat_legacy(request: Request):
    data = await request.json()
    question = data.get("message") or data.get("question") or ""
    if not question:
        return JSONResponse(content={"reply": "Pertanyaan tidak boleh kosong."})

    system_prompt = "Kamu adalah asisten digital yang ahli di bidang pertanian Indonesia. Jawab dengan bahasa Indonesia yang sopan dan mudah dipahami."

    payload = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ],
        "max_tokens": 512,
        "temperature": 0.7
    }

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    print("GROQ_API_KEY:", GROQ_API_KEY)
    print("Payload:", payload)
    print("Headers:", headers)

    async with httpx.AsyncClient() as client:
        response = await client.post(GROQ_API_URL, json=payload, headers=headers)
        print("Groq response status:", response.status_code)
        print("Groq response body:", response.text)
        if response.status_code == 200:
            result = response.json()
            reply = result["choices"][0]["message"]["content"]
            return JSONResponse(content={"reply": reply})
        else:
            return JSONResponse(content={"reply": "Maaf, terjadi kesalahan pada AI Groq."}, status_code=500)

# Endpoint /api/chatbot tetap dummy/optional
@router.post("/api/chatbot")
async def chatbot_endpoint(request: Request):
    data = await request.json()
    question = data.get("message") or data.get("question") or ""
    if not question:
        return JSONResponse(content={"reply": "Pertanyaan tidak boleh kosong."})
    return JSONResponse(content={"reply": "Gunakan endpoint /chat untuk jawaban AI Groq."}) 