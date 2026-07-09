from datetime import date, datetime

from langchain_core.tools import tool

from app.ai.extractor import extract_interaction
from app.database.session import get_session
from app.services.hcp_service import (
    create_hcp,
    get_hcp_by_name,
)
from app.services.interaction_service import (
    create_interaction,
)
from langchain_core.tools import tool

from app.ai.edit_interaction import extract_edit
from app.schemas.tools_response import ToolResponse


from app.database.database import SessionLocal
from app.utils.message_builder import build_edit_message


@tool
def log_interaction(user_input: str):
    """
    Extract an interaction and return it to the frontend.
    The interaction is NOT saved here.
    """

    interaction = extract_interaction(user_input)

    return ToolResponse(
        type="log",
        success=True,
        message="I've extracted the interaction details. Please review them before saving.",
        payload=interaction.model_dump(),
    )


@tool
def edit_interaction(user_input: str):
    """
    Edit the extracted interaction.
    """

    edit = extract_edit(user_input)

    

    return ToolResponse(
        type="edit",
        success=True,
        message=build_edit_message(edit.field,edit.value,),
        payload={
            "field": edit.field,
            "value": edit.value,
        },
    )

@tool
def search_hcp(user_input: str):
    """Search an HCP."""

    return {
        "status": "success",
        "message": f"Searching HCP: {user_input}",
    }


@tool
def interaction_history(user_input: str):
    """Retrieve interaction history."""

    return {
        "status": "success",
        "message": f"History for: {user_input}",
    }


@tool
def followup_recommendation(user_input: str):
    """Generate follow-up recommendation."""

    return {
        "status": "success",
        "message": f"Recommended follow-up for: {user_input}",
    }


TOOLS = [
    log_interaction,
    edit_interaction,
    search_hcp,
    interaction_history,
    followup_recommendation,
]