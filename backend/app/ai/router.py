from langchain_core.messages import HumanMessage, SystemMessage

from app.ai.llm import llm
from app.ai.prompts import ROUTER_PROMPT
from app.schemas.router import RouteDecision

structured_llm = llm.with_structured_output(
    RouteDecision
)


def decide_route(message: str) -> RouteDecision:
    return structured_llm.invoke(
        [
            SystemMessage(
                content=ROUTER_PROMPT
            ),
            HumanMessage(
                content=message
            ),
        ]
    )