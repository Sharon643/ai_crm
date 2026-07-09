from langchain_core.tools import tool

from app.ai.extractor import extract_interaction
from app.schemas.tools_response import ToolResponse


@tool
def log_interaction(user_input: str):
    """
    Extract an interaction and return it to the frontend.
    """

    interaction = extract_interaction(user_input)

    return ToolResponse(
        type="log",
        success=True,
        message="I've extracted the interaction details. Please review them before saving.",
        payload=interaction.model_dump(),
    )