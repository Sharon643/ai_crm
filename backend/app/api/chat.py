from fastapi import APIRouter

from app.schemas.chat import ChatRequest
from app.langgraph.graph import graph

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


@router.post("/")
def chat(request: ChatRequest):

    result = graph.invoke(
        {
            "message": request.message,
        }
    )

    return result["result"]