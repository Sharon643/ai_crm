from langchain_core.tools import tool

from app.schemas.tools_response import ToolResponse


@tool
def visit_planner(user_input: str):
    """
    Prioritize and plan HCP visits for the day based on CRM data.
    """

    return ToolResponse(
        type="planner",
        success=True,
        message="Visit Planner is under development.",
        payload=None,
    )