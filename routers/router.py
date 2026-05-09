from fastapi import APIRouter
from models.models import ChatRequest
from crud.crud import askRouter

router = APIRouter()

@router.post("/chat")
async def chat(req: ChatRequest):
  response = await askRouter(req.message)
  return {"Ответ": response}