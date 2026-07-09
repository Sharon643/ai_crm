from langchain_core.tools import tool

from app.database.database import SessionLocal

from app.schemas.tools_response import ToolResponse

from app.services.action_item_service import (
    get_pending_actions,
)


@tool
def action_items(user_input: str):
    """
    Retrieve pending action items.
    """

    db = SessionLocal()

    try:

        actions = get_pending_actions(db)

        payload = []

        for action in actions:

            payload.append({
                "id": action.id,
                "hcp_name": action.hcp.name,
                "title": action.title,
                "priority": action.priority,
                "status": action.status,
            })

        return ToolResponse(
            type="actions",
            success=True,
            message="I've gathered your pending action items. Opening Action Items...",
            payload={
                "actions": payload
            },
        )

    finally:

        db.close()