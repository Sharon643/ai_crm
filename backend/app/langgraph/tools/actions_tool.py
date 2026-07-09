from langchain_core.tools import tool

from app.schemas.tools_response import ToolResponse


@tool
def extract_action_items(user_input: str):
    """
    Extract follow-up tasks and action items from an interaction.
    """

    return ToolResponse(
        type="actions",
        success=True,
        message="Action Items Extractor is under development.",
        payload=None,
    )