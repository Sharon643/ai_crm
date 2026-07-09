from langchain_core.tools import tool

from app.ai.edit_interaction import extract_edit

from app.schemas.tools_response import ToolResponse

from app.utils.message_builder import (
    build_edit_message,
)


@tool
def edit_interaction(user_input: str):
    """
   Edit the extracted interaction form.
    """

    edit = extract_edit(user_input)

    return ToolResponse(
        type="edit",
        success=True,
        message=build_edit_message(
            edit.field,
            edit.value,
        ),
        payload={
            "field": edit.field,
            "value": edit.value,
        },
    )