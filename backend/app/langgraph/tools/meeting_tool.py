from langchain_core.tools import tool

from app.schemas.tools_response import ToolResponse


@tool
def meeting_preparation(user_input: str):
    """
    Generate a meeting briefing for a Healthcare Professional using
    previous CRM interactions and outstanding follow-up items.
    """

    return ToolResponse(
        type="meeting",
        success=True,
        message="Meeting Preparation is under development.",
        payload=None,
    )