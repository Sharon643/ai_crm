import re

from langchain_core.tools import tool

from app.database.database import SessionLocal

from app.schemas.tools_response import ToolResponse

from app.services.meeting_preparation_service import (
    get_meeting_context,
)

from app.ai.meeting_preparation import (
    generate_meeting_brief,
)


@tool
def meeting_preparation(user_input: str):
    """
    Prepare a meeting brief for a healthcare professional.
    """

    db = SessionLocal()

    try:

        match = re.search(
            r"Dr\.?\s+[A-Za-z]+\s+[A-Za-z]+",
            user_input,
        )

        if not match:
            return ToolResponse(
                type="meeting",
                success=False,
                message="Please specify the doctor's name.",
            )

        doctor = match.group()

        context = get_meeting_context(
            db,
            doctor,
        )

        if context is None:
            return ToolResponse(
                type="meeting",
                success=False,
                message=f"No information found for {doctor}.",
            )

        brief = generate_meeting_brief(
            context
        )

        return ToolResponse(
            type="meeting",
            success=True,
            message=brief,
        )

    finally:

        db.close()